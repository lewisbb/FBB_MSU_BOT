from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

status_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Студент', callback_data='student')],
    [InlineKeyboardButton(text='Выпускник', callback_data='graduated')], [InlineKeyboardButton(text="Назад", callback_data='back_reg')]])

grad_year = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='2025', callback_data='grad_2025')],
                                                  [InlineKeyboardButton(text='2024', callback_data='grad_2024')],
                                                  [InlineKeyboardButton(text='2023', callback_data='grad_2023')],
                                                  [InlineKeyboardButton(text='Более ранний год', callback_data='grad_Ранний год')],
                                                  [InlineKeyboardButton(text="Назад", callback_data='back_reg')]])

course_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='2 (1 курс)', callback_data='cs_1')],
                                                  [InlineKeyboardButton(text='4 (2 курс)', callback_data='cs_2')],
                                                  [InlineKeyboardButton(text='6 (3 курс)', callback_data='cs_3')],
                                                  [InlineKeyboardButton(text='8 (4 курс)', callback_data='cs_4')],
                                                  [InlineKeyboardButton(text='10 (5 курс)', callback_data='cs_5')],
                                                  [InlineKeyboardButton(text="Назад", callback_data='back_reg')]])

def keyboard_marks(prefix):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='1 ⭐', callback_data=f'{prefix}_mark_1'),
                                                  InlineKeyboardButton(text='6 ⭐', callback_data=f'{prefix}_mark_6')],
                                                  [InlineKeyboardButton(text='2 ⭐', callback_data=f'{prefix}_mark_2'),
                                                  InlineKeyboardButton(text='7 ⭐', callback_data=f'{prefix}_mark_7')],
                                                  [InlineKeyboardButton(text='3 ⭐', callback_data=f'{prefix}_mark_3'),
                                                  InlineKeyboardButton(text='8 ⭐', callback_data=f'{prefix}_mark_8')],
                                                  [InlineKeyboardButton(text='4 ⭐', callback_data=f'{prefix}_mark_4'),
                                                  InlineKeyboardButton(text='9 ⭐', callback_data=f'{prefix}_mark_9')],
                                                  [InlineKeyboardButton(text='5 ⭐', callback_data=f'{prefix}_mark_5'),
                                                  InlineKeyboardButton(text='10 ⭐', callback_data=f'{prefix}_mark_10')],
                                                  [InlineKeyboardButton(text='Пропустить преподавателя', callback_data=f'{prefix}_skip_teacher')], 
                                                  [InlineKeyboardButton(text='Назад', callback_data=f'{prefix}_back')]])
    return keyboard


def keyboard_marks_org(prefix):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='1 ⭐', callback_data=f'{prefix}_mark_1'),
                                                  InlineKeyboardButton(text='6 ⭐', callback_data=f'{prefix}_mark_6')],
                                                  [InlineKeyboardButton(text='2 ⭐', callback_data=f'{prefix}_mark_2'),
                                                  InlineKeyboardButton(text='7 ⭐', callback_data=f'{prefix}_mark_7')],
                                                  [InlineKeyboardButton(text='3 ⭐', callback_data=f'{prefix}_mark_3'),
                                                  InlineKeyboardButton(text='8 ⭐', callback_data=f'{prefix}_mark_8')],
                                                  [InlineKeyboardButton(text='4 ⭐', callback_data=f'{prefix}_mark_4'),
                                                  InlineKeyboardButton(text='9 ⭐', callback_data=f'{prefix}_mark_9')],
                                                  [InlineKeyboardButton(text='5 ⭐', callback_data=f'{prefix}_mark_5'),
                                                  InlineKeyboardButton(text='10 ⭐', callback_data=f'{prefix}_mark_10')],
                                                  [InlineKeyboardButton(text='Пропустить', callback_data=f'{prefix}_skip')], 
                                                  [InlineKeyboardButton(text='Назад', callback_data=f'{prefix}_back')]])
    return keyboard

def keyboard_att(prefix):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Вы бы не выбрали курс как МФК', callback_data=f'{prefix}_att_1')],
                                                      [InlineKeyboardButton(text='Курс слабый, важное упускается', callback_data=f'{prefix}_att_2')],
                                                      [InlineKeyboardButton(text='Курс бесполезен, знания устарели', callback_data=f'{prefix}_att_3')],
                                                      [InlineKeyboardButton(text='Преподаватель пропускает занятия', callback_data=f'{prefix}_att_4')],
                                                      [InlineKeyboardButton(text='Преподаватель отвлекается на байки', callback_data=f'{prefix}_att_5')],
                                                      [InlineKeyboardButton(text='Преподаватель некомпетентен', callback_data=f'{prefix}_att_6')],
                                                      [InlineKeyboardButton(text='Негативное отношение к студентам', callback_data=f'{prefix}_att_7')],
                                                      [InlineKeyboardButton(text='Пропустить', callback_data=f'{prefix}_att_8'), InlineKeyboardButton(text='Назад', callback_data=f'{prefix}_back')]])
    return keyboard


keyboard_com = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Пропустить', callback_data='skip_name')]])

