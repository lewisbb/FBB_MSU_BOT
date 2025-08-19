import datetime
import logging
import traceback
from typing import List

from aiogram import types, F, Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
import app.keyboards as kb
import app.states as st
from app.states import Organization
import app.dictionaries as dicty
from aiogram.types import ReplyKeyboardRemove, Message
from aiogram.filters import StateFilter
from aiogram.utils.keyboard import InlineKeyboardBuilder

from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, DateTime, text
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, Session
from sqlalchemy.sql import func

logger = logging.getLogger(__name__)
router = Router()

ATTITUDE = dicty.ATTITUDE
ORGANIZATION = dicty.ORGANIZATION
COURSES = dicty.COURSES
ALL_PREFIXES = [t["prefix"] for course in COURSES.values() for t in course["teachers"]]
ORG_PREFIXES = list(ORGANIZATION.keys())

Base = declarative_base()
DATABASE_URL = "sqlite:///survey.db"
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class TeacherRating(Base):
    __tablename__ = 'teacher_ratings'
    id = Column(Integer, primary_key=True)
    survey_id = Column(Integer, ForeignKey('surveys.id'))
    teacher_prefix = Column(String(20), nullable=False)
    teacher_name = Column(String(100), nullable=False)
    mark = Column(String(20))
    att = Column(String(50))
    com = Column(Text)
    survey = relationship("Survey", back_populates="teacher_ratings")

class OrgRating(Base):
    __tablename__ = 'org_ratings'
    id = Column(Integer, primary_key=True)
    survey_id = Column(Integer, ForeignKey('surveys.id'))
    category = Column(String(10), nullable=False)
    rating = Column(Integer, nullable=True)  # Разрешены NULL-значения
    survey = relationship("Survey", back_populates="org_ratings")

class Survey(Base):
    __tablename__ = 'surveys'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False, unique=True)  # Добавлено поле для ID пользователя Telegram
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    name = Column(String(100), nullable=False)
    status = Column(String(20), nullable=False)
    grad_stat = Column(String(10))
    stud_course = Column(String(10), nullable=False)
    teacher_ratings = relationship("TeacherRating", back_populates="survey")
    org_ratings = relationship("OrgRating", back_populates="survey")

def create_tables():
    Base.metadata.create_all(bind=engine)
    with engine.connect() as conn:
        conn.execute(text("PRAGMA journal_mode=WAL;"))
        conn.execute(text("PRAGMA synchronous=NORMAL;"))
        conn.commit()

create_tables()

def check_user_exists(user_id: int) -> bool:
    """Проверяет, существует ли пользователь с таким ID в базе данных"""
    try:
        with SessionLocal() as session:
            existing_user = session.query(Survey).filter(Survey.user_id == user_id).first()
            return existing_user is not None
    except Exception as e:
        logger.error(f"Error checking user existence: {e}")
        return False

def create_comment_keyboard(prefix: str):
    builder = InlineKeyboardBuilder()
    builder.button(text="Пропустить", callback_data=f"{prefix}_com_skip")
    builder.button(text="Назад", callback_data=f"{prefix}_com_back")
    builder.adjust(2) 
    return builder.as_markup()

@router.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext):
    # Проверяем, проходил ли пользователь уже опрос
    user_id = message.from_user.id
    if check_user_exists(user_id):
        await message.answer("Вы уже проходили опрос. Спасибо за участие!")
        return
    
    await state.set_state(st.Register.name)
    await state.update_data(user_id=user_id)  # Сохраняем ID пользователя в состоянии
    await message.answer(
        'Привет! 😇😇😇\nЭто - опрос по качеству образования на ФББ МГУ. Данный опрос могут проходить как студенты, так и выпускники факультета. Результаты опроса будут обсуждаться на заседаниях комиссии по качеству образования для того, чтобы сделать процесс обучения на факультете лучше. В комиссию по качеству образования входят заместители декана по учебной, учебно-методической и научной работе, а также пятеро избранных Студенческим советом представителей студентов. \n\n Для прохождения опроса введите ФИО (нажмите "Пропустить", если хотите сохранить анонимность):',
        reply_markup=kb.keyboard_com
    )

@router.message(st.Register.name)
async def register_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(st.Register.status)
    await message.answer('Кем Вы являетесь?', reply_markup=kb.status_keyboard)

@router.callback_query(F.data == "skip_name", st.Register.name)
async def skip_name(callback: types.CallbackQuery, state: FSMContext):
    try:
        await callback.answer()
    except TelegramBadRequest as e:
        if "query is too old" in str(e):
            logger.warning(f"Expired callback skipped: {callback.data}")
            return
        raise
        
    await state.update_data(name="Аноним")
    await state.set_state(st.Register.status)
    await callback.message.answer('Кем Вы являетесь?', reply_markup=kb.status_keyboard)

@router.callback_query(F.data == 'student')
async def process_callback(callback: types.CallbackQuery, state: FSMContext):
    try:
        await callback.answer()
    except TelegramBadRequest as e:
        if "query is too old" in str(e):
            logger.warning(f"Expired callback skipped: {callback.data}")
            return
        raise
        
    await state.update_data(status='Студент')
    await state.set_state(st.Register.stud_course)
    await callback.message.answer("Какой семестр вы закончили?", reply_markup=kb.course_keyboard)

@router.callback_query(F.data == 'graduated')
async def process_callback(callback: types.CallbackQuery, state: FSMContext):
    try:
        await callback.answer()
    except TelegramBadRequest as e:
        if "query is too old" in str(e):
            logger.warning(f"Expired callback skipped: {callback.data}")
            return
        raise
        
    await state.set_state(st.Register.grad_stat)
    await state.update_data(status='Выпускник')
    await callback.message.answer('Какой Вы год выпуска?', reply_markup=kb.grad_year)

@router.callback_query(lambda c: c.data.startswith("grad_"))
async def callback(callback: types.CallbackQuery, state: FSMContext):
    try:
        await callback.answer()
    except TelegramBadRequest as e:
        if "query is too old" in str(e):
            logger.warning(f"Expired callback skipped: {callback.data}")
            return
        raise
        
    year = callback.data.split("_")[1]
    await state.update_data(grad_stat=year)
    await state.set_state(st.Register.stud_course)
    await callback.message.answer('За какой семестр хотите пройти опрос?', reply_markup=kb.course_keyboard)

@router.callback_query(F.data == "back_reg")
async def back_registration(callback: types.CallbackQuery, state: FSMContext):
    try:
        await callback.answer()
    except TelegramBadRequest as e:
        if "query is too old" in str(e):
            logger.warning(f"Expired callback skipped: {callback.data}")
            return
        raise
        
    current_state = await state.get_state()
    
    if current_state == st.Register.status:
        await state.set_state(st.Register.name)
        await callback.message.answer('Для прохождения опроса введите ФИО:', reply_markup=kb.keyboard_com)
        
    elif current_state == st.Register.grad_stat:
        await state.set_state(st.Register.status)
        await callback.message.answer('Кем Вы являетесь?', reply_markup=kb.status_keyboard)
        
    elif current_state == st.Register.stud_course:
        data = await state.get_data()
        if data.get('status') == 'Выпускник':
            await state.set_state(st.Register.grad_stat)
            await callback.message.answer('Какой Вы год выпуска?', reply_markup=kb.grad_year)
        else:
            await state.set_state(st.Register.status)
            await callback.message.answer('Кем Вы являетесь?', reply_markup=kb.status_keyboard)

@router.callback_query(lambda c: c.data.startswith("cs_"))
async def choose_course(callback: types.CallbackQuery, state: FSMContext):
    try:
        await callback.answer()
    except TelegramBadRequest as e:
        if "query is too old" in str(e):
            logger.warning(f"Expired callback skipped: {callback.data}")
            return
        raise
        
    course = callback.data.split("_")[1]
    if course not in COURSES:
        await callback.answer("Неизвестный курс")
        return
        
    course_data = COURSES[course]
    teachers = course_data["teachers"]
    
    await state.update_data(
        stud_course=course,
        all_teachers=[t["prefix"] for t in teachers],
        completed_teachers=[]
    )
    
    first_teacher = teachers[0]
    await state.set_state(first_teacher["states"]["mark"])
    await state.update_data(current_teacher=first_teacher["prefix"])
    
    await callback.message.answer(
        f'Оцените предметы и их ведение в семестре:\n\n<b>{first_teacher["name"]}</b>',
        reply_markup=first_teacher["keyboards"]["mark"],
        parse_mode="HTML"
    )

@router.callback_query(lambda c: c.data.endswith("_skip_teacher"))
async def handle_skip_teacher(callback: types.CallbackQuery, state: FSMContext):
    try:
        await callback.answer()
    except TelegramBadRequest as e:
        if "query is too old" in str(e):
            logger.warning(f"Expired callback skipped: {callback.data}")
            return
        raise

    parts = callback.data.split('_')
    prefix = '_'.join(parts[:-2])
    
    data = await state.get_data()
    current_teacher = data.get("current_teacher")
    
    if current_teacher != prefix:
        await callback.answer("Пожалуйста, завершите текущего преподавателя")
        return
    
    await state.update_data({
        f"{prefix}_mark": "пропущено",
        f"{prefix}_att": "пропущено",
        f"{prefix}_com": "пропущено"
    })
    
    completed = data.get("completed_teachers", [])
    completed.append(prefix)
    all_teachers = data["all_teachers"]
    await state.update_data(completed_teachers=completed)
    
    remaining = [p for p in all_teachers if p not in completed]
    
    if remaining:
        next_teacher_prefix = remaining[0]
        course_data = COURSES[data["stud_course"]]
        next_teacher = None
        for t in course_data["teachers"]:
            if t["prefix"] == next_teacher_prefix:
                next_teacher = t
                break
        
        if not next_teacher:
            await callback.answer("Ошибка: преподаватель не найден")
            return
        
        await state.update_data(current_teacher=next_teacher_prefix)
        await state.set_state(next_teacher["states"]["mark"])
        
        await callback.message.answer(
            f'Оцените предметы и их ведение в семестре:\n\n<b>{next_teacher["name"]}</b>',
            reply_markup=kb.keyboard_marks(next_teacher_prefix),
            parse_mode="HTML"
        )
    else:
        logger.info(f"Завершен опрос преподавателей (после пропуска) для пользователя {callback.from_user.id}")
        await state.update_data(teachers_completed=True)
        await state.set_state(Organization.bit)
        await callback.message.answer(
            f'Теперь оцените организацию факультета:\n\n<b>{ORGANIZATION["bit"]}</b>',
            reply_markup=kb.keyboard_marks_org("bit"),
            parse_mode="HTML"
        )

all_teacher_states = []
for course in COURSES.values():
    for teacher in course["teachers"]:
        all_teacher_states.append(teacher["states"]["mark"])
        all_teacher_states.append(teacher["states"]["att"])
        all_teacher_states.append(teacher["states"]["com"])

@router.callback_query(lambda c: c.data.endswith("_back"), StateFilter(*all_teacher_states))
async def handle_teacher_back(callback: types.CallbackQuery, state: FSMContext):
    try:
        await callback.answer()
    except TelegramBadRequest as e:
        if "query is too old" in str(e):
            logger.warning(f"Expired callback skipped: {callback.data}")
            return
        raise
    
    data = await state.get_data()
    current_teacher_prefix = data.get("current_teacher")
    
    if not current_teacher_prefix:
        await callback.answer("Ошибка: текущий преподаватель не определен")
        return
    
    course = data.get("stud_course")
    if not course:
        await callback.answer("Ошибка: курс не определен")
        return
    teacher = None
    for t in COURSES.get(course, {}).get("teachers", []):
        if t["prefix"] == current_teacher_prefix:
            teacher = t
            break
    
    if not teacher:
        logger.error(f"Преподаватель с префиксом '{current_teacher_prefix}' не найден в курсе '{course}'")
        await callback.answer("Преподаватель не найден")
        return
    
    current_state = await state.get_state()
    states = teacher["states"]
    if current_state == states["att"]:
        await state.set_state(states["mark"])
        await callback.message.answer(
            f'Оцените предметы и их ведение в семестре:\n\n<b>{teacher["name"]}</b>',
            reply_markup=teacher["keyboards"]["mark"],
            parse_mode="HTML"
        )
    elif current_state == states["com"]:
        await state.set_state(states["att"])
        await callback.message.answer(
            f'Выберите негативную характеристику курса:\n\n<b>{teacher["name"]}</b>',
            reply_markup=teacher["keyboards"]["att"],
            parse_mode="HTML"
        )
    elif current_state == states["mark"]:
        all_teachers = data.get("all_teachers", []) 
        if not all_teachers:
            await callback.answer("Ошибка: список преподавателей пуст")
            return   
        try:
            current_index = all_teachers.index(current_teacher_prefix)
        except ValueError:
            await callback.answer("Ошибка: текущий преподаватель не найден в списке")
            return
        
        if current_index == 0:
            await state.set_state(st.Register.stud_course)
            await callback.message.answer(
                'За какой семестр хотите пройти опрос?',
                reply_markup=kb.course_keyboard
            )
        else:
            prev_teacher_prefix = all_teachers[current_index - 1]
            prev_teacher = None
            for t in COURSES[course]["teachers"]:
                if t["prefix"] == prev_teacher_prefix:
                    prev_teacher = t
                    break
            
            if not prev_teacher:
                logger.error(f"Предыдущий преподаватель с префиксом '{prev_teacher_prefix}' не найден")
                await callback.answer("Предыдущий преподаватель не найден")
                return
            await state.update_data(current_teacher=prev_teacher_prefix)
            prev_mark = data.get(f"{prev_teacher_prefix}_mark")
            if prev_mark == "пропущено":
                await state.set_state(prev_teacher["states"]["mark"])
                await callback.message.answer(
                    f'Оцените предметы и их ведение в семестре:\n\n<b>{prev_teacher["name"]}</b>',
                    reply_markup=prev_teacher["keyboards"]["mark"],
                    parse_mode="HTML"
                )
            else:
                await state.set_state(prev_teacher["states"]["com"])
                await callback.message.answer(
                    f'Напишите краткий комментарий курсу (необязательно):\n\n<b>{prev_teacher["name"]}</b>',
                    reply_markup=create_comment_keyboard(prev_teacher_prefix),
                    parse_mode="HTML"
                )
    else:
        logger.warning(f"Неизвестное состояние для кнопки Назад: {current_state}")
        await callback.answer("Не удалось обработать запрос")
    

@router.callback_query(lambda c: any(c.data.startswith(f"{prefix}_") for prefix in ALL_PREFIXES))
async def handle_teacher_action(callback: types.CallbackQuery, state: FSMContext):
    try:
        await callback.answer()
    except TelegramBadRequest as e:
        if "query is too old" in str(e):
            logger.warning(f"Expired callback skipped: {callback.data}")
            return
        raise
    
    if callback.data.endswith("_back"):
        return
    
    data = await state.get_data()
    current_teacher_prefix = data.get("current_teacher")
    
    if not current_teacher_prefix:
        await callback.answer("Ошибка: преподаватель не определен")
        return
    
    parts = callback.data.split("_")
    prefix = parts[0]
    action_type = parts[1]
    
    if prefix != current_teacher_prefix:
        await callback.answer("Пожалуйста, завершите текущего преподавателя")
        return
    if action_type == "com" and len(parts) > 2 and parts[2] == "skip":
        await state.update_data({f"{prefix}_com": "пропущено"})
        await handle_teacher_comment(callback.message, state, skip_message=True)
        return
    
    if action_type == "att" and len(parts) > 2 and parts[2] == "skip":
        value = "skip"
    else:
        value = "_".join(parts[2:]) if len(parts) > 2 else ""
    
    data_key = f"{prefix}_{action_type}"
    save_value = ATTITUDE.get(value, value) if action_type == "att" else value
    await state.update_data({data_key: save_value})
    
    if action_type == "mark":
        next_action = "att"
    elif action_type == "att":
        next_action = "com"
    else:
        await callback.answer("Неизвестное действие")
        return
    
    course_data = COURSES[data["stud_course"]]
    teacher = None
    for t in course_data["teachers"]:
        if t["prefix"] == prefix:
            teacher = t
            break
    
    if not teacher:
        await callback.answer("Преподаватель не найден")
        return
    
    next_state = teacher["states"][next_action]
    await state.set_state(next_state)
    
    message_text = f'Оцените предметы и их ведение в семестре:\n\n<b>{teacher["name"]}</b>\n\n'
    if next_action == "att":
        message_text += 'Выберите негативную характеристику курса:'
        reply_markup = teacher["keyboards"][next_action]
    else:
        message_text += 'Напишите краткий комментарий курсу (необязательно):'
        reply_markup = create_comment_keyboard(prefix)
    
    await callback.message.answer(
        message_text,
        reply_markup=reply_markup,
        parse_mode="HTML"
    )

@router.message(StateFilter(*[t["states"]["com"] for c in COURSES.values() for t in c["teachers"]]))
async def handle_teacher_comment(message: Message, state: FSMContext, skip_message=False):
    
    data = await state.get_data()
    current_teacher_prefix = data.get("current_teacher")
    
    if not current_teacher_prefix:
        await message.answer("Ошибка: преподаватель не определен")
        await state.clear()
        return
    
    if not skip_message:
        comment = message.text
        await state.update_data({f"{current_teacher_prefix}_com": comment})
    
    completed = data.get("completed_teachers", [])
    completed.append(current_teacher_prefix)
    all_teachers = data["all_teachers"]
    
    await state.update_data(completed_teachers=completed)
    
    remaining = [p for p in all_teachers if p not in completed]
    
    if remaining:
        next_teacher_prefix = remaining[0]
        course_data = COURSES[data["stud_course"]]
        next_teacher = None
        for t in course_data["teachers"]:
            if t["prefix"] == next_teacher_prefix:
                next_teacher = t
                break
        
        if not next_teacher:
            await message.answer("Ошибка: следующий преподаватель не найден")
            return
        
        await state.update_data(current_teacher=next_teacher_prefix)
        await state.set_state(next_teacher["states"]["mark"])
        
        await message.answer(
            f'Оцените предметы и их ведение в семестре:\n\n<b>{next_teacher["name"]}</b>',
            reply_markup=next_teacher["keyboards"]["mark"],
            parse_mode="HTML"
        )
    else:
        logger.info(f"Завершен опрос преподавателей для пользователя {message.from_user.id}")
        await state.update_data(teachers_completed=True)
        await state.set_state(Organization.bit)
        await message.answer(
            f'Теперь оцените организацию факультета:\n\n<b>{ORGANIZATION["bit"]}</b>',
            reply_markup=kb.keyboard_marks_org("bit"),
            parse_mode="HTML"
        )

async def go_to_next_org_question(current_prefix: str, message: Message, state: FSMContext):
    keys = list(ORGANIZATION.keys())
    current_index = keys.index(current_prefix)
    next_index = current_index + 1
    
    if next_index < len(keys):
        next_prefix = keys[next_index]
        next_state = getattr(Organization, next_prefix)
        await state.set_state(next_state)
        
        await message.answer(
            f'Оцените:\n\n<b>{ORGANIZATION[next_prefix]}</b>',
            reply_markup=kb.keyboard_marks_org(next_prefix),
            parse_mode="HTML"
        )
    else:
        await finish_survey(message, state)

async def go_to_prev_org_question(current_prefix: str, message: Message, state: FSMContext):
    logger.info(f"Обработка кнопки Назад для организационного вопроса: {current_prefix}")
    keys = list(ORGANIZATION.keys())
    
    try:
        current_index = keys.index(current_prefix)
    except ValueError:
        await message.answer("⚠️ Ошибка: текущий вопрос не найден")
        return
    
    prev_index = current_index - 1

    if prev_index >= 0:
        prev_prefix = keys[prev_index]
        try:
            prev_state = getattr(Organization, prev_prefix)
        except AttributeError:
            await message.answer("⚠️ Ошибка: состояние для предыдущего вопроса не найдено.")
            return

        await state.set_state(prev_state)
        await message.answer(
            f'Оцените:\n\n<b>{ORGANIZATION[prev_prefix]}</b>',
            reply_markup=kb.keyboard_marks_org(prev_prefix),
            parse_mode = "HTML"
        )
    else:
        data = await state.get_data()
        course = data.get("stud_course")
        if not course:
            await finish_survey(message, state)
            return
            
        course_data = COURSES.get(course)
        if not course_data:
            await finish_survey(message, state)
            return
            
        teachers = course_data.get("teachers", [])
        if teachers:
            last_teacher = teachers[-1]
            last_teacher_prefix = last_teacher["prefix"]
            teacher_mark = data.get(f"{last_teacher_prefix}_mark", None)
            if teacher_mark == "пропущено":
                next_state = last_teacher["states"]["mark"]
                message_text = f'Оцените предметы и их ведение в семестре:\n\n<b>{last_teacher["name"]}</b>'
                reply_markup = last_teacher["keyboards"]["mark"]
            else:
                next_state = last_teacher["states"]["com"]
                message_text = f'Напишите краткий комментарий курсу:\n\n<b>{last_teacher["name"]}</b>'
                reply_markup = create_comment_keyboard(last_teacher_prefix)
            await state.update_data(
                completed_teachers=[t for t in data.get("completed_teachers", []) if t != last_teacher_prefix],
                teachers_completed=False,
                current_teacher=last_teacher_prefix
            )
            await state.set_state(next_state)
            
            await message.answer(
                message_text,
                reply_markup=reply_markup,
                parse_mode="HTML"
            )
        else:
            await finish_survey(message, state)

def save_survey_to_db(survey_data: dict) -> bool:
    try:
        with SessionLocal() as session:
            survey_record = Survey(
                user_id=survey_data.get('user_id'),  # Сохраняем ID пользователя
                name=survey_data.get('name', ''),
                status=survey_data.get('status', ''),
                grad_stat=survey_data.get('grad_stat', ''),
                stud_course=survey_data.get('stud_course', '')
            )
            
            teacher_ratings = []
            for prefix in survey_data.get('all_teachers', []):
                teacher_found = None
                course = survey_data.get("stud_course")
                if course in COURSES:
                    for teacher in COURSES[course]['teachers']:
                        if teacher['prefix'] == prefix:
                            teacher_found = teacher
                            break
                
                if teacher_found:
                    teacher_ratings.append(TeacherRating(
                        teacher_prefix=prefix,
                        teacher_name=teacher_found['name'],
                        mark=survey_data.get(f"{prefix}_mark", ""),
                        att=survey_data.get(f"{prefix}_att", ""),
                        com=survey_data.get(f"{prefix}_com", "")
                    ))
            
            org_ratings = []
            for prefix in ORG_PREFIXES:
                rating_value = survey_data.get(f"org_{prefix}")
                
                # Обработка числовых значений и пропусков
                if rating_value is None or rating_value == "пропущено":
                    rating_int = None
                elif isinstance(rating_value, str) and rating_value.isdigit():
                    rating_int = int(rating_value)
                else:
                    rating_int = None  # Некорректное значение
                
                org_ratings.append(OrgRating(
                    category=prefix,
                    rating=rating_int
                ))
            
            survey_record.teacher_ratings = teacher_ratings
            survey_record.org_ratings = org_ratings
            session.add(survey_record)
            session.commit()
            survey_id = survey_record.id
            logger.info(f"Survey data saved to DB: ID {survey_id}, User ID {survey_data.get('user_id')}")
        
        return True
    
    except Exception as e:
        logger.error(f"Error saving survey to database: {e}\n{traceback.format_exc()}")
        return False

async def finish_survey(message: Message, state: FSMContext):
    survey_data = await state.get_data()
    report = "📊 Ваши ответы:\n\n"
    report += f"Имя: {survey_data.get('name', '')}\nСтатус: {survey_data.get('status', '')}\n"
    
    if survey_data.get('grad_stat'):
        report += f"Год выпуска: {survey_data['grad_stat']}\n"
        
    report += f"Курс: {survey_data.get('stud_course', '')}\n\n"
    for teacher_prefix in survey_data.get('all_teachers', []):
        teacher_found = None
        course = survey_data.get("stud_course")
        if course in COURSES:
            for teacher in COURSES[course]['teachers']:
                if teacher['prefix'] == teacher_prefix:
                    teacher_found = teacher
                    break
        
        if teacher_found:
            mark = survey_data.get(f"{teacher_prefix}_mark", "не указано")
            attitude = survey_data.get(f"{teacher_prefix}_att", "не указано")
            comment = survey_data.get(f"{teacher_prefix}_com", "нет комментария")
            
            report += f"👨‍🏫 {teacher_found['name']}:\n"
            report += f"  • Оценка: {mark}\n"
            report += f"  • Характеристика: {attitude}\n"
            report += f"  • Комментарий: {comment}\n\n"
    
    report += "🏛 Оценка организации:\n"
    for prefix in ORG_PREFIXES:
        value = survey_data.get(f"org_{prefix}", "не указано")
        # Преобразование None в "не указано"
        if value is None or value == "пропущено":
            display_value = "не указано"
        else:
            display_value = value
        report += f"  • {ORGANIZATION[prefix]}: {display_value}\n"
    
    try:
        success = save_survey_to_db(survey_data)
        
        if success:
            await message.answer("✅ Опрос завершен! Ваши данные сохранены.")
        else:
            await message.answer("✅ Опрос завершен! При сохранении данных возникли проблемы, администратор уведомлен.")
        
    except Exception as e:
        logger.error(f"Error in finish_survey: {e}")
        await message.answer("✅ Опрос завершен! Спасибо за участие!")
        await message.answer(f"⚠️ При сохранении данных возникла ошибка: {str(e)}")
    
    await state.clear()

@router.callback_query(lambda c: c.data.endswith("_back"), StateFilter(Organization))
async def handle_org_back(callback: types.CallbackQuery, state: FSMContext):
    try:
        await callback.answer()
    except TelegramBadRequest as e:
        if "query is too old" in str(e):
            logger.warning(f"Expired callback skipped: {callback.data}")
            return
        raise
    
    parts = callback.data.split('_')
    prefix = parts[0]
    
    if prefix not in ORG_PREFIXES:
        logger.error(f"Неизвестный префикс организационного вопроса: {prefix}")
        await callback.answer("Ошибка: неизвестный вопрос")
        return
    
    await go_to_prev_org_question(prefix, callback.message, state)

@router.callback_query(lambda c: any(c.data.startswith(prefix) for prefix in ORG_PREFIXES), StateFilter(Organization))
async def handle_org_action(callback: types.CallbackQuery, state: FSMContext):
    try:
        await callback.answer()
    except TelegramBadRequest as e:
        if "query is too old" in str(e):
            logger.warning(f"Expired callback skipped: {callback.data}")
            return
        raise

    data_str = callback.data
    prefix = data_str.split('_')[0]
    
    if prefix not in ORG_PREFIXES:
        await callback.answer("Неизвестный вопрос")
        return
    if any(data_str.endswith(f"_{i}") for i in range(1, 11)):
        mark_value = data_str.split('_')[-1]
        await state.update_data({f"org_{prefix}": mark_value})
        await go_to_next_org_question(prefix, callback.message, state)
    elif data_str.endswith("_skip"):
        # Сохраняем None вместо строки для пропущенных вопросов
        await state.update_data({f"org_{prefix}": None})
        await go_to_next_org_question(prefix, callback.message, state)
    
@router.message(StateFilter(
    Organization.bit,
    Organization.admin,
    Organization.psycho,
    Organization.atm,
    Organization.sch,
    Organization.exa))

async def handle_org_text(message: Message):
    await message.answer("Пожалуйста, используйте клавиатуру для выбора оценки")