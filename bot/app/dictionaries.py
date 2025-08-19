import app.keyboards as kb
import app.states as st

ATTITUDE = {"1": "Вы бы не выбрали курс как МФК",
            "2": "Курс слабый, важное упускается",
            "3": "Курс бесполезен, знания устарели",
            "4": "Преподаватель пропускает занятия",
            "5": "Преподаватель отвлекается на байки",
            "6": "Преподаватель некомпетентен",
            "7": "Негативное отношение к студентам",
            "8": "Пропуск"}

ORGANIZATION = {"bit": 'Организация и быт факультета',
                "admin": 'Работа администрации',
                "psycho": 'Работа психолога',
                "atm": 'Атмосфера на факультете(уровень спокойствия, отсутствие враждебности)',
                "sch": 'Расписание пар',
                "exa": 'Расписание зачетной и экзаменационной сессии'}

COURSES = {
    "1": {
        "name": "Первый курс",
        "teachers": [
            {
                "name": 'Скворцов Дмитрий Александрович (Химические основы биологических процессов)',
                "prefix": "skv",
                "states": {
                    "mark": st.Prepods.skvortsov_mark,
                    "att": st.Prepods.skvortsov_att,
                    "com": st.Prepods.skvortsov_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("skv"),
                    "att": kb.keyboard_att("skv"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Бачева Анна Владимировна (Химические основы биологических процессов)',
                "prefix": "bac",
                "states": {
                    "mark": st.Prepods.bacheva_mark,
                    "att": st.Prepods.bacheva_att,
                    "com": st.Prepods.bacheva_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("bac"),
                    "att": kb.keyboard_att("bac"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Апяри Владимир Владимирович (Аналитическая химия)',
                "prefix": "apa",
                "states": {
                    "mark": st.Prepods.apari_mark,
                    "att": st.Prepods.apari_att,
                    "com": st.Prepods.apari_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("apa"),
                    "att": kb.keyboard_att("apa"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Смоленков Александр Дмитриевич (Аналитическая химия)',
                "prefix": "smo",
                "states": {
                    "mark": st.Prepods.smolenkov_mark,
                    "att": st.Prepods.smolenkov_att,
                    "com": st.Prepods.smolenkov_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("smo"),
                    "att": kb.keyboard_att("smo"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Михеев Иван Владимирович (Аналитическая химия)',
                "prefix": "mih",
                "states": {
                    "mark": st.Prepods.miheev_mark,
                    "att": st.Prepods.miheev_att,
                    "com": st.Prepods.miheev_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("mih"),
                    "att": kb.keyboard_att("mih"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Рожманова Нина Борисовна (Аналитическая химия)',
                "prefix": "roz",
                "states": {
                    "mark": st.Prepods.rozhmanova_mark,
                    "att": st.Prepods.rozhmanova_att,
                    "com": st.Prepods.rozhmanova_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("roz"),
                    "att": kb.keyboard_att("roz"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Чикурова Наталья Юрьевна (Аналитическая химия)',
                "prefix": "chi",
                "states": {
                    "mark": st.Prepods.chikurova_mark,
                    "att": st.Prepods.chikurova_att,
                    "com": st.Prepods.chikurova_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("chi"),
                    "att": kb.keyboard_att("chi"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Веселова Ирина Анатольевна (Аналитическая химия)',
                "prefix": "ves",
                "states": {
                    "mark": st.Prepods.veselova_mark,
                    "att": st.Prepods.veselova_att,
                    "com": st.Prepods.veselova_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("ves"),
                    "att": kb.keyboard_att("ves"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Белякова Галина Алексеевна (Ботаника низших растений)',
                "prefix": "bel",
                "states": {
                    "mark": st.Prepods.belyakova_mark,
                    "att": st.Prepods.belyakova_att,
                    "com": st.Prepods.belyakova_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("bel"),
                    "att": kb.keyboard_att("bel"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Камзолкина Ольга Владимировна (Ботаника низших растений)',
                "prefix": "cam",
                "states": {
                    "mark": st.Prepods.camzolkina_mark,
                    "att": st.Prepods.camzolkina_att,
                    "com": st.Prepods.camzolkina_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("cam"),
                    "att": kb.keyboard_att("cam"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Понизовская Валерия Борисовна (Ботаника низших растений)',
                "prefix": "pon",
                "states": {
                    "mark": st.Prepods.ponizovskaya_mark,
                    "att": st.Prepods.ponizovskaya_att,
                    "com": st.Prepods.ponizovskaya_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("pon"),
                    "att": kb.keyboard_att("pon"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Шнырева Алла Викторовна  (Ботаника низших растений)',
                "prefix": "shn",
                "states": {
                    "mark": st.Prepods.shnireva_mark,
                    "att": st.Prepods.shnireva_att,
                    "com": st.Prepods.shnireva_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("shn"),
                    "att": kb.keyboard_att("shn"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Чудаев Дмитрий Алексеевич (Ботаника низших растений)',
                "prefix": "chu",
                "states": {
                    "mark": st.Prepods.chudaev_mark,
                    "att": st.Prepods.chudaev_att,
                    "com": st.Prepods.chudaev_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("chu"),
                    "att": kb.keyboard_att("chu"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Тарасов Константин Львович (Ботаника низших растений)',
                "prefix": "tar",
                "states": {
                    "mark": st.Prepods.tarasov_mark,
                    "att": st.Prepods.tarasov_att,
                    "com": st.Prepods.tarasov_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("tar"),
                    "att": kb.keyboard_att("tar"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Бубнова Екатерина Николаевна (Ботаника низших растений)',
                "prefix": "bub",
                "states": {
                    "mark": st.Prepods.bubnova_mark,
                    "att": st.Prepods.bubnova_att,
                    "com": st.Prepods.bubnova_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("bub"),
                    "att": kb.keyboard_att("bub"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Корзун Леонид Петрович (Зоология позвоночных) ',
                "prefix": "cor",
                "states": {
                    "mark": st.Prepods.corzun_mark,
                    "att": st.Prepods.corzun_att,
                    "com": st.Prepods.corzun_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("cor"),
                    "att": kb.keyboard_att("cor"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Горбань Артемий Александрович (Зоология позвоночных)',
                "prefix": "gor",
                "states": {
                    "mark": st.Prepods.gorban_mark,
                    "att": st.Prepods.gorban_att,
                    "com": st.Prepods.gorban_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("gor"),
                    "att": kb.keyboard_att("gor"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Грицышин Владимир Андреевич (Зоология позвоночных)',
                "prefix": "gri",
                "states": {
                    "mark": st.Prepods.gricishin_mark,
                    "att": st.Prepods.gricishin_att,
                    "com": st.Prepods.gricishin_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("gri"),
                    "att": kb.keyboard_att("gri"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Трофимец Алексей Викторович (Зоология позвоночных)',
                "prefix": "tro",
                "states": {
                    "mark": st.Prepods.trofimec_mark,
                    "att": st.Prepods.trofimec_att,
                    "com": st.Prepods.trofimec_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("tro"),
                    "att": kb.keyboard_att("tro"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Идиятуллина Сабира Шамильевна (Зоология позвоночных)',
                "prefix": "idi",
                "states": {
                    "mark": st.Prepods.idiyatulina_mark,
                    "att": st.Prepods.idiyatulina_att,
                    "com": st.Prepods.idiyatulina_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("idi"),
                    "att": kb.keyboard_att("idi"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Авилова Ксения Всеволодовна (Зоология позвоночных)',
                "prefix": "avi",
                "states": {
                    "mark": st.Prepods.avilova_mark,
                    "att": st.Prepods.avilova_att,
                    "com": st.Prepods.avilova_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("avi"),
                    "att": kb.keyboard_att("avi"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Полунов Александр Юрьевич (Отечественная история)',
                "prefix": "pol",
                "states": {
                    "mark": st.Prepods.polunov_mark,
                    "att": st.Prepods.polunov_att,
                    "com": st.Prepods.polunov_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("pol"),
                    "att": kb.keyboard_att("pol"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Ульянова Любовь Владимировна (Отечественная история)',
                "prefix": "uli",
                "states": {
                    "mark": st.Prepods.ulianova_mark,
                    "att": st.Prepods.ulianova_att,
                    "com": st.Prepods.ulianova_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("uli"),
                    "att": kb.keyboard_att("uli"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Прошкина Анастасия Владимировна (Математический анализ)',
                "prefix": "pro",
                "states": {
                    "mark": st.Prepods.proshkina_mark,
                    "att": st.Prepods.proshkina_att,
                    "com": st.Prepods.proshkina_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("pro"),
                    "att": kb.keyboard_att("pro"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Чечкина Александра Григорьевна (Математический анализ)',
                "prefix": "che1",
                "states": {
                    "mark": st.Prepods.chechkina1_mark,
                    "att": st.Prepods.chechkina1_att,
                    "com": st.Prepods.chechkina1_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("che1"),
                    "att": kb.keyboard_att("che1"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Карелина Наталья Александровна (Иностранный язык)',
                "prefix": "kar1",
                "states": {
                    "mark": st.Prepods.karelina1_mark,
                    "att": st.Prepods.karelina1_att,
                    "com": st.Prepods.karelina1_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("kar1"),
                    "att": kb.keyboard_att("kar1"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Малахова Мария Сергеевна (Иностранный язык)',
                "prefix": "mal1",
                "states": {
                    "mark": st.Prepods.malahova1_mark,
                    "att": st.Prepods.malahova1_att,
                    "com": st.Prepods.malahova1_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("mal1"),
                    "att": kb.keyboard_att("mal1"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Васильева Арина Евгеньевна (Иностранный язык)',
                "prefix": "vas1",
                "states": {
                    "mark": st.Prepods.vasilieva1_mark,
                    "att": st.Prepods.vasilieva1_att,
                    "com": st.Prepods.vasilieva1_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("vas1"),
                    "att": kb.keyboard_att("vas1"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Аветисян Нелли Гургеновна (Иностранный язык)',
                "prefix": "ave1",
                "states": {
                    "mark": st.Prepods.avetisyan1_mark,
                    "att": st.Prepods.avetisyan1_att,
                    "com": st.Prepods.avetisyan1_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("ave1"),
                    "att": kb.keyboard_att("ave1"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Михайловская Мария Валерьевна (Иностранный язык)',
                "prefix": "miha1",
                "states": {
                    "mark": st.Prepods.mihailovskaya1_mark,
                    "att": st.Prepods.mihailovskaya1_att,
                    "com": st.Prepods.mihailovskaya1_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("miha1"),
                    "att": kb.keyboard_att("miha1"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Спирин Сергей Александрович (Практическая биоинформатика)',
                "prefix": "spi",
                "states": {
                    "mark": st.Prepods.spirin_mark,
                    "att": st.Prepods.spirin_att,
                    "com": st.Prepods.spirin_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("spi"),
                    "att": kb.keyboard_att("spi"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Алексеевский Андрей Владимирович (Практическая биоинформатика)',
                "prefix": "ale",
                "states": {
                    "mark": st.Prepods.alexeevskii_mark,
                    "att": st.Prepods.alexeevskii_att,
                    "com": st.Prepods.alexeevskii_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("ale"),
                    "att": kb.keyboard_att("ale"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Рюмина Екатерина Даниловна (Практическая биоинформатика)',
                "prefix": "ryu",
                "states": {
                    "mark": st.Prepods.ryumina_mark,
                    "att": st.Prepods.ryumina_att,
                    "com": st.Prepods.ryumina_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("ryu"),
                    "att": kb.keyboard_att("ryu"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Алешина Юлия Александровна (Практическая биоинформатика)',
                "prefix": "ales",
                "states": {
                    "mark": st.Prepods.aleshina_mark,
                    "att": st.Prepods.aleshina_att,
                    "com": st.Prepods.aleshina_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("ales"),
                    "att": kb.keyboard_att("ales"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Маслова Валентина Дмитриевна (Практическая биоинформатика)',
                "prefix": "mas",
                "states": {
                    "mark": st.Prepods.maslova_mark,
                    "att": st.Prepods.maslova_att,
                    "com": st.Prepods.maslova_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("mas"),
                    "att": kb.keyboard_att("mas"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Ириоглов Роман Андреевич (Практическая биоинформатика)',
                "prefix": "iri",
                "states": {
                    "mark": st.Prepods.irioglov_mark,
                    "att": st.Prepods.irioglov_att,
                    "com": st.Prepods.irioglov_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("iri"),
                    "att": kb.keyboard_att("iri"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Русинов Иван Сергеевич (Практическая биоинформатика)',
                "prefix": "rus",
                "states": {
                    "mark": st.Prepods.rusinov_mark,
                    "att": st.Prepods.rusinov_att,
                    "com": st.Prepods.rusinov_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("rus"),
                    "att": kb.keyboard_att("rus"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Солдатова Светлана Викторовна (Физическая культура)',
                "prefix": "sol",
                "states": {
                    "mark": st.Prepods.soldatova_mark,
                    "att": st.Prepods.soldatova_att,
                    "com": st.Prepods.soldatova_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("sol"),
                    "att": kb.keyboard_att("sol"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Шумилов Сергей Юрьевич  (Физическая культура)',
                "prefix": "shu",
                "states": {
                    "mark": st.Prepods.shumilov_mark,
                    "att": st.Prepods.shumilov_att,
                    "com": st.Prepods.shumilov_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("shu"),
                    "att": kb.keyboard_att("shu"),
                    "com": kb.keyboard_com,
                }
            },
        ]
    },
    "2": {
        "name": "Второй курс",
        "teachers": [
            {
                "name": 'Яковенко Леонид Владимирович (Физика)',
                "prefix": "yak",
                "states": {
                    "mark": st.Prepods.yakovenko_mark,
                    "att": st.Prepods.yakovenko_att,
                    "com": st.Prepods.yakovenko_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("yak"),
                    "att": kb.keyboard_att("yak"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Беляев Алексей Вячеславович (Физика)',
                "prefix": "bel",
                "states": {
                    "mark": st.Prepods.belyaev_mark,
                    "att": st.Prepods.belyaev_att,
                    "com": st.Prepods.belyaev_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("bel"),
                    "att": kb.keyboard_att("bel"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Хомутов Геннадий Борисович (Физика)',
                "prefix": "hom",
                "states": {
                    "mark": st.Prepods.homutov_mark,
                    "att": st.Prepods.homutov_att,
                    "com": st.Prepods.homutov_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("hom"),
                    "att": kb.keyboard_att("hom"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Нифантьев Илья Эдуардович (Органическая химия)',
                "prefix": "nif",
                "states": {
                    "mark": st.Prepods.nifantiev_mark,
                    "att": st.Prepods.nifantiev_att,
                    "com": st.Prepods.nifantiev_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("nif"),
                    "att": kb.keyboard_att("nif"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Ивченко Павел Васильевич (Органическая химия)',
                "prefix": "ivc",
                "states": {
                    "mark": st.Prepods.ivchenko_mark,
                    "att": st.Prepods.ivchenko_att,
                    "com": st.Prepods.ivchenko_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("ivc"),
                    "att": kb.keyboard_att("ivc"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Брусова Галина Павловна (Органическая химия)',
                "prefix": "bru",
                "states": {
                    "mark": st.Prepods.brusova_mark,
                    "att": st.Prepods.brusova_att,
                    "com": st.Prepods.brusova_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("bru"),
                    "att": kb.keyboard_att("bru"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Трубников Артем Владиславович (Органическая химия)',
                "prefix": "tru",
                "states": {
                    "mark": st.Prepods.trubnikov_mark,
                    "att": st.Prepods.trubnikov_att,
                    "com": st.Prepods.trubnikov_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("tru"),
                    "att": kb.keyboard_att("tru"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Зиновкина Людмила Андреевна (Методология научных исследований)',
                "prefix": "zin",
                "states": {
                    "mark": st.Prepods.zinovkina_mark,
                    "att": st.Prepods.zinovkina_att,
                    "com": st.Prepods.zinovkina_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("zin"),
                    "att": kb.keyboard_att("zin"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Ловать Максим Львович (Физиология человека и животных)',
                "prefix": "lov",
                "states": {
                    "mark": st.Prepods.lovat_mark,
                    "att": st.Prepods.lovat_att,
                    "com": st.Prepods.lovat_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("lov"),
                    "att": kb.keyboard_att("lov"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Марченко Дарья Михайловна (Физиология человека и животных)',
                "prefix": "mar",
                "states": {
                    "mark": st.Prepods.marchenko_mark,
                    "att": st.Prepods.marchenko_att,
                    "com": st.Prepods.marchenko_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("mar"),
                    "att": kb.keyboard_att("mar"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Шубина Татьяна Александровна (Физиология человека и животных)',
                "prefix": "shu",
                "states": {
                    "mark": st.Prepods.shubina_mark,
                    "att": st.Prepods.shubina_att,
                    "com": st.Prepods.shubina_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("shu"),
                    "att": kb.keyboard_att("shu"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Крушинская Янина Валерьевна (Физиология человека и животных)',
                "prefix": "kru",
                "states": {
                    "mark": st.Prepods.krushinskaya_mark,
                    "att": st.Prepods.krushinskaya_att,
                    "com": st.Prepods.krushinskaya_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("kru"),
                    "att": kb.keyboard_att("kru"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Карелина Наталья Александровна (Иностранный язык)',
                "prefix": "kar2",
                "states": {
                    "mark": st.Prepods.karelina2_mark,
                    "att": st.Prepods.karelina2_att,
                    "com": st.Prepods.karelina2_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("kar2"),
                    "att": kb.keyboard_att("kar2"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Аветисян Нелли Гургеновна (Иностранный язык)',
                "prefix": "ave2",
                "states": {
                    "mark": st.Prepods.avetisyan2_mark,
                    "att": st.Prepods.avetisyan2_att,
                    "com": st.Prepods.avetisyan2_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("ave2"),
                    "att": kb.keyboard_att("ave2"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Малахова Мария Сергеевна (Иностранный язык)',
                "prefix": "mal12",
                "states": {
                    "mark": st.Prepods.malahova12_mark,
                    "att": st.Prepods.malahova12_att,
                    "com": st.Prepods.malahova12_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("mal12"),
                    "att": kb.keyboard_att("mal12"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Васильева Арина Евгеньевна (Реферирование и перевод)',
                "prefix": "vas2",
                "states": {
                    "mark": st.Prepods.vasilieva2_mark,
                    "att": st.Prepods.vasilieva2_att,
                    "com": st.Prepods.vasilieva2_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("vas2"),
                    "att": kb.keyboard_att("vas2"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Малахова Мария Сергеевна (Реферирование и перевод)',
                "prefix": "mal22",
                "states": {
                    "mark": st.Prepods.malahova22_mark,
                    "att": st.Prepods.malahova22_att,
                    "com": st.Prepods.malahova22_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("mal22"),
                    "att": kb.keyboard_att("mal22"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Зинкевич Арсений (Информатика)',
                "prefix": "zink",
                "states": {
                    "mark": st.Prepods.zinkevich_mark,
                    "att": st.Prepods.zinkevich_att,
                    "com": st.Prepods.zinkevich_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("zink"),
                    "att": kb.keyboard_att("zink"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Шаповалов Иван (Информатика)',
                "prefix": "sha",
                "states": {
                    "mark": st.Prepods.shapovalov_mark,
                    "att": st.Prepods.shapovalov_att,
                    "com": st.Prepods.shapovalov_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("sha"),
                    "att": kb.keyboard_att("sha"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Школиков Алексей (Информатика)',
                "prefix": "shk",
                "states": {
                    "mark": st.Prepods.shkolikov_mark,
                    "att": st.Prepods.shkolikov_att,
                    "com": st.Prepods.shkolikov_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("shk"),
                    "att": kb.keyboard_att("shk"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Босов Дмитрий (Информатика)',
                "prefix": "bos",
                "states": {
                    "mark": st.Prepods.bosov_mark,
                    "att": st.Prepods.bosov_att,
                    "com": st.Prepods.bosov_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("bos"),
                    "att": kb.keyboard_att("bos"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Хлебников Даниил (Информатика, последний семинар, про декораторы)',
                "prefix": "hle",
                "states": {
                    "mark": st.Prepods.hlebnikov_mark,
                    "att": st.Prepods.hlebnikov_att,
                    "com": st.Prepods.hlebnikov_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("hle"),
                    "att": kb.keyboard_att("hle"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Ноздрин Владимир (Информатика, предпоследний семинар, про субпроцессы)',
                "prefix": "noz",
                "states": {
                    "mark": st.Prepods.nozdrin_mark,
                    "att": st.Prepods.nozdrin_att,
                    "com": st.Prepods.nozdrin_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("noz"),
                    "att": kb.keyboard_att("noz"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Звездин Дмитрий (Информатика, семинар про классы)',
                "prefix": "zve",
                "states": {
                    "mark": st.Prepods.zvezdin_mark,
                    "att": st.Prepods.zvezdin_att,
                    "com": st.Prepods.zvezdin_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("zve"),
                    "att": kb.keyboard_att("zve"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Якушев Александр (Информатика, семинар про обработку исключений и JSON)',
                "prefix": "yac",
                "states": {
                    "mark": st.Prepods.yacushev_mark,
                    "att": st.Prepods.yacushev_att,
                    "com": st.Prepods.yacushev_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("yac"),
                    "att": kb.keyboard_att("yac"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Аристова Елизавета (Информатика, семинар про дизайн графиков)',
                "prefix": "ari",
                "states": {
                    "mark": st.Prepods.aristova_mark,
                    "att": st.Prepods.aristova_att,
                    "com": st.Prepods.aristova_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("ari"),
                    "att": kb.keyboard_att("ari"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Селиванник Вера Леонидовна (Физическая культура)',
                "prefix": "sel",
                "states": {
                    "mark": st.Prepods.selivannik_mark,
                    "att": st.Prepods.selivannik_att,
                    "com": st.Prepods.selivannik_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("sel"),
                    "att": kb.keyboard_att("sel"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Мадилов Константин Николаевич (Физическая культура)',
                "prefix": "mad",
                "states": {
                    "mark": st.Prepods.madilov_mark,
                    "att": st.Prepods.madilov_att,
                    "com": st.Prepods.madilov_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("mad"),
                    "att": kb.keyboard_att("mad"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Мирзоев Карахан Агахан оглы (Дифференциальные уравнения)',
                "prefix": "mir",
                "states": {
                    "mark": st.Prepods.mirzoev_mark,
                    "att": st.Prepods.mirzoev_att,
                    "com": st.Prepods.mirzoev_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("mir"),
                    "att": kb.keyboard_att("mir"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Чечкина Александра Григорьевна (Дифференциальные уравнения)',
                "prefix": "che2",
                "states": {
                    "mark": st.Prepods.chechkina2_mark,
                    "att": st.Prepods.chechkina2_att,
                    "com": st.Prepods.chechkina2_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("che2"),
                    "att": kb.keyboard_att("che2"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Спирин Сергей Александрович (Практическая биоинформатика)',
                "prefix": "spi",
                "states": {
                    "mark": st.Prepods.spirin_mark,
                    "att": st.Prepods.spirin_att,
                    "com": st.Prepods.spirin_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("spi"),
                    "att": kb.keyboard_att("spi"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Алексеевский Андрей Владимирович (Практическая биоинформатика)',
                "prefix": "ale",
                "states": {
                    "mark": st.Prepods.alexeevskii_mark,
                    "att": st.Prepods.alexeevskii_att,
                    "com": st.Prepods.alexeevskii_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("ale"),
                    "att": kb.keyboard_att("ale"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Рюмина Екатерина (Практическая биоинформатика)',
                "prefix": "ryu",
                "states": {
                    "mark": st.Prepods.ryumina_mark,
                    "att": st.Prepods.ryumina_att,
                    "com": st.Prepods.ryumina_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("ryu"),
                    "att": kb.keyboard_att("ryu"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Диброва Дарья (Практическая биоинформатика)',
                "prefix": "dib",
                "states": {
                    "mark": st.Prepods.dibrova_mark,
                    "att": st.Prepods.dibrova_att,
                    "com": st.Prepods.dibrova_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("dib"),
                    "att": kb.keyboard_att("dib"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Алешина Юлия (Практическая биоинформатика)',
                "prefix": "ales",
                "states": {
                    "mark": st.Prepods.aleshina_mark,
                    "att": st.Prepods.aleshina_att,
                    "com": st.Prepods.aleshina_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("ales"),
                    "att": kb.keyboard_att("ales"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Жарикова Анастасия (Практическая биоинформатика)',
                "prefix": "zha",
                "states": {
                    "mark": st.Prepods.zharikova_mark,
                    "att": st.Prepods.zharikova_att,
                    "com": st.Prepods.zharikova_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("zha"),
                    "att": kb.keyboard_att("zha"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Ириоглов Роман (Практическая биоинформатика)',
                "prefix": "iri",
                "states": {
                    "mark": st.Prepods.irioglov_mark,
                    "att": st.Prepods.irioglov_att,
                    "com": st.Prepods.irioglov_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("iri"),
                    "att": kb.keyboard_att("iri"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Каргов Сергей Игоревич (Физическая химия)',
                "prefix": "karg",
                "states": {
                    "mark": st.Prepods.kargov_mark,
                    "att": st.Prepods.kargov_att,
                    "com": st.Prepods.kargov_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("karg"),
                    "att": kb.keyboard_att("karg"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Обрезкова Мария Васильевна (Физическая химия)',
                "prefix": "obr",
                "states": {
                    "mark": st.Prepods.obrezkova_mark,
                    "att": st.Prepods.obrezkova_att,
                    "com": st.Prepods.obrezkova_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("obr"),
                    "att": kb.keyboard_att("obr"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Жирякова Марина Владимировна (Физическая химия)',
                "prefix": "zhi",
                "states": {
                    "mark": st.Prepods.zhiryakova_mark,
                    "att": st.Prepods.zhiryakova_att,
                    "com": st.Prepods.zhiryakova_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("zhi"),
                    "att": kb.keyboard_att("zhi"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Бедняков Александр Сергеевич (Физическая химия)',
                "prefix": "bed",
                "states": {
                    "mark": st.Prepods.bedmyakov_mark,
                    "att": st.Prepods.bedmyakov_att,
                    "com": st.Prepods.bedmyakov_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("bed"),
                    "att": kb.keyboard_att("bed"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Куценко Владимир Александрович (Введение в математическую статистику)',
                "prefix": "kuc",
                "states": {
                    "mark": st.Prepods.kucenko_mark,
                    "att": st.Prepods.kucenko_att,
                    "com": st.Prepods.kucenko_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("kuc"),
                    "att": kb.keyboard_att("kuc"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Филичкина Елена Михайловна (Введение в математическую статистику)',
                "prefix": "fil",
                "states": {
                    "mark": st.Prepods.filichkina_mark,
                    "att": st.Prepods.filichkina_att,
                    "com": st.Prepods.filichkina_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("fil"),
                    "att": kb.keyboard_att("fil"),
                    "com": kb.keyboard_com,
                }
            },
        ]
    },
    "3": {
        "name": "Третий курс",
        "teachers": [
            {
                "name": 'Дмитриев Сергей Евгеньевич (Генная инженерия)',
                "prefix": "dmi1",
                "states": {
                    "mark": st.Prepods.dmitriev1_mark,
                    "att": st.Prepods.dmitriev1_att,
                    "com": st.Prepods.dmitriev1_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("dmi1"),
                    "att": kb.keyboard_att("dmi1"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Борисов Виталий Борисович (Биохимия)',
                "prefix": "bor",
                "states": {
                    "mark": st.Prepods.borisov_mark,
                    "att": st.Prepods.borisov_att,
                    "com": st.Prepods.borisov_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("bor"),
                    "att": kb.keyboard_att("bor"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Силецкий Сергей Алексеевич (Биохимия)',
                "prefix": "sil",
                "states": {
                    "mark": st.Prepods.sileckii_mark,
                    "att": st.Prepods.sileckii_att,
                    "com": st.Prepods.sileckii_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("sil"),
                    "att": kb.keyboard_att("sil"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Миронов Андрей Александрович (Биоинформатика последовательностей)',
                "prefix": "mir",
                "states": {
                    "mark": st.Prepods.mironov_mark,
                    "att": st.Prepods.mironov_att,
                    "com": st.Prepods.mironov_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("mir"),
                    "att": kb.keyboard_att("mir"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Вржещ Петр Владимирович (Кинетика ферментативных реакций)',
                "prefix": "vrz",
                "states": {
                    "mark": st.Prepods.vrzhech_mark,
                    "att": st.Prepods.vrzhech_att,
                    "com": st.Prepods.vrzhech_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("vrz"),
                    "att": kb.keyboard_att("vrz"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Кривошей Александр Владимирович (Кинетика ферментативных реакций)',
                "prefix": "kri",
                "states": {
                    "mark": st.Prepods.krivoshei_mark,
                    "att": st.Prepods.krivoshei_att,
                    "com": st.Prepods.krivoshei_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("kri"),
                    "att": kb.keyboard_att("kri"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Котова Ирина Борисовна (Микробиология)',
                "prefix": "kot",
                "states": {
                    "mark": st.Prepods.kotova_mark,
                    "att": st.Prepods.kotova_att,
                    "com": st.Prepods.kotova_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("kot"),
                    "att": kb.keyboard_att("kot"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Малахова Дина Викторовна (Микробиология)',
                "prefix": "malah",
                "states": {
                    "mark": st.Prepods.malahova12_mark,
                    "att": st.Prepods.malahova12_att,
                    "com": st.Prepods.malahova12_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("malah"),
                    "att": kb.keyboard_att("malah"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Сорокина Елена Владимировна (Микробиология)',
                "prefix": "sor",
                "states": {
                    "mark": st.Prepods.sorokina_mark,
                    "att": st.Prepods.sorokina_att,
                    "com": st.Prepods.sorokina_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("sor"),
                    "att": kb.keyboard_att("sor"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Кремнева Мария Константиновна (Микробиология)',
                "prefix": "kre",
                "states": {
                    "mark": st.Prepods.kremneva_mark,
                    "att": st.Prepods.kremneva_att,
                    "com": st.Prepods.kremneva_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("kre"),
                    "att": kb.keyboard_att("kre"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Коротецкая Мария Валерьевна (Методы исследования биологических макромолекул)',
                "prefix": "koro",
                "states": {
                    "mark": st.Prepods.koroteckaya_mark,
                    "att": st.Prepods.koroteckaya_att,
                    "com": st.Prepods.koroteckaya_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("koro"),
                    "att": kb.keyboard_att("koro"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Олейников Илья Павлович (Методы исследования биологических макромолекул)',
                "prefix": "ole",
                "states": {
                    "mark": st.Prepods.oleinikov_mark,
                    "att": st.Prepods.oleinikov_att,
                    "com": st.Prepods.oleinikov_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("ole"),
                    "att": kb.keyboard_att("ole"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Кудрявцева София Станиславовна (Методы исследования биологических макромолекул)',
                "prefix": "kud",
                "states": {
                    "mark": st.Prepods.kudryavceva_mark,
                    "att": st.Prepods.kudryavceva_att,
                    "com": st.Prepods.kudryavceva_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("kud"),
                    "att": kb.keyboard_att("kud"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Стройлова Юлия Юрьевна (Методы исследования биологических макромолекул)',
                "prefix": "str",
                "states": {
                    "mark": st.Prepods.stroilova_mark,
                    "att": st.Prepods.stroilova_att,
                    "com": st.Prepods.stroilova_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("str"),
                    "att": kb.keyboard_att("str"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Зоров Савва Дмитриевич (Методы исследования биологических макромолекул)',
                "prefix": "zor",
                "states": {
                    "mark": st.Prepods.zorov_mark,
                    "att": st.Prepods.zorov_att,
                    "com": st.Prepods.zorov_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("zor"),
                    "att": kb.keyboard_att("zor"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Бархатов Владимир Игоревич (Методы исследования биологических макромолекул)',
                "prefix": "barh",
                "states": {
                    "mark": st.Prepods.barhatov_mark,
                    "att": st.Prepods.barhatov_att,
                    "com": st.Prepods.barhatov_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("barh"),
                    "att": kb.keyboard_att("barh"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Хайрова Светлана Раисовна (Иностранный язык)',
                "prefix": "hai3",
                "states": {
                    "mark": st.Prepods.hairova3_mark,
                    "att": st.Prepods.hairova3_att,
                    "com": st.Prepods.hairova3_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("hai3"),
                    "att": kb.keyboard_att("hai3"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Малахова Мария Сергеевна (Иностранный язык)',
                "prefix": "mal3",
                "states": {
                    "mark": st.Prepods.malahova3_mark,
                    "att": st.Prepods.malahova3_att,
                    "com": st.Prepods.malahova3_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("mal3"),
                    "att": kb.keyboard_att("mal3"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Аветисян Нелли Гургеновна (Иностранный язык)',
                "prefix": "ave3",
                "states": {
                    "mark": st.Prepods.avetisyan3_mark,
                    "att": st.Prepods.avetisyan3_att,
                    "com": st.Prepods.avetisyan3_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("ave3"),
                    "att": kb.keyboard_att("ave3"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Васильева Арина Евгеньевна (Реферирование и перевод)',
                "prefix": "vas3",
                "states": {
                    "mark": st.Prepods.vasilieva3_mark,
                    "att": st.Prepods.vasilieva3_att,
                    "com": st.Prepods.vasilieva3_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("vas3"),
                    "att": kb.keyboard_att("vas3"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Хайрова Светлана Раисовна (Реферирование и перевод)',
                "prefix": "hai3",
                "states": {
                    "mark": st.Prepods.hairova3_mark,
                    "att": st.Prepods.hairova3_att,
                    "com": st.Prepods.hairova3_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("hai3"),
                    "att": kb.keyboard_att("hai3"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Михайловская Мария Валерьевна (Реферирование и перевод)',
                "prefix": "miha3",
                "states": {
                    "mark": st.Prepods.mihailovskaya3_mark,
                    "att": st.Prepods.mihailovskaya3_att,
                    "com": st.Prepods.mihailovskaya3_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("miha3"),
                    "att": kb.keyboard_att("miha3"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Калайдзидис Яннис Леонтьевич (Математическая статистика)',
                "prefix": "kal",
                "states": {
                    "mark": st.Prepods.kalaidsizis_mark,
                    "att": st.Prepods.kalaidsizis_att,
                    "com": st.Prepods.kalaidsizis_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("kal"),
                    "att": kb.keyboard_att("kal"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Буник-Фаренвальд Виктория Ивановна (Молекулярные основы биологических функций (спецкурс по выбору I))',
                "prefix": "bun",
                "states": {
                    "mark": st.Prepods.bunik_mark,
                    "att": st.Prepods.bunik_att,
                    "com": st.Prepods.bunik_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("bun"),
                    "att": kb.keyboard_att("bun"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Терентьев Антон Алексеевич (Нейрофизиология (спецкурс по выбору I))',
                "prefix": "ter",
                "states": {
                    "mark": st.Prepods.terentiev_mark,
                    "att": st.Prepods.terentiev_att,
                    "com": st.Prepods.terentiev_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("ter"),
                    "att": kb.keyboard_att("ter"),
                    "com": kb.keyboard_com,
                }
            },
        ]
    },
    "4": {
        "name": "Четвертый курс",
        "teachers": [
            {
                "name": 'Челомбитько Мария Александровна (Гистология)',
                "prefix": "chel",
                "states": {
                    "mark": st.Prepods.chelombitko_mark,
                    "att": st.Prepods.chelombitko_att,
                    "com": st.Prepods.chelombitko_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("chel"),
                    "att": kb.keyboard_att("chel"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Чуркина Александра Сергеевна (Гистология)',
                "prefix": "chu",
                "states": {
                    "mark": st.Prepods.churkina_mark,
                    "att": st.Prepods.churkina_att,
                    "com": st.Prepods.churkina_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("chu"),
                    "att": kb.keyboard_att("chu"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Павлюченкова Анастасия Никитична (Гистология)',
                "prefix": "pav",
                "states": {
                    "mark": st.Prepods.bubnova_mark,
                    "att": st.Prepods.bubnova_att,
                    "com": st.Prepods.bubnova_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("pav"),
                    "att": kb.keyboard_att("pav"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Анисенко Андрей Николаевич (Вирусология)',
                "prefix": "ani",
                "states": {
                    "mark": st.Prepods.anisenko_mark,
                    "att": st.Prepods.anisenko_att,
                    "com": st.Prepods.anisenko_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("ani"),
                    "att": kb.keyboard_att("ani"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Щигал Ольга Евгеньевна (Вирусология)',
                "prefix": "shi",
                "states": {
                    "mark": st.Prepods.shigal_mark,
                    "att": st.Prepods.shigal_att,
                    "com": st.Prepods.shigal_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("shi"),
                    "att": kb.keyboard_att("shi"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Машковская Анна Владимировна (Вируусология)',
                "prefix": "mash",
                "states": {
                    "mark": st.Prepods.mashkovskaya_mark,
                    "att": st.Prepods.mashkovskaya_att,
                    "com": st.Prepods.mashkovskaya_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("mash"),
                    "att": kb.keyboard_att("mash"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Шилов Евгений Сергеевич (Иммунология)',
                "prefix": "shil",
                "states": {
                    "mark": st.Prepods.shilov_mark,
                    "att": st.Prepods.shilov_att,
                    "com": st.Prepods.shilov_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("shil"),
                    "att": kb.keyboard_att("shil"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Скобеева Виктория Александровна (Эволюционная биология)',
                "prefix": "sko",
                "states": {
                    "mark": st.Prepods.skobeeva_mark,
                    "att": st.Prepods.skobeeva_att,
                    "com": st.Prepods.skobeeva_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("sko"),
                    "att": kb.keyboard_att("sko"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Швядас Витаутас-Юозапас Каятоно (Инженерная энзимология)',
                "prefix": "shv",
                "states": {
                    "mark": st.Prepods.shvyadas_mark,
                    "att": st.Prepods.shvyadas_att,
                    "com": st.Prepods.shvyadas_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("shv"),
                    "att": kb.keyboard_att("shv"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Пензар Дмитрий Дмитриевич (Машинное обучение)',
                "prefix": "pen",
                "states": {
                    "mark": st.Prepods.penzar_mark,
                    "att": st.Prepods.penzar_att,
                    "com": st.Prepods.penzar_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("pen"),
                    "att": kb.keyboard_att("pen"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Зинкевич Арсений (Машинное обучение)',
                "prefix": "zink",
                "states": {
                    "mark": st.Prepods.zinkevich_mark,
                    "att": st.Prepods.zinkevich_att,
                    "com": st.Prepods.zinkevich_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("zink"),
                    "att": kb.keyboard_att("zink"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Босов Дмитрий (Машинное обучение)',
                "prefix": "bos",
                "states": {
                    "mark": st.Prepods.bosov_mark,
                    "att": st.Prepods.bosov_att,
                    "com": st.Prepods.bosov_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("bos"),
                    "att": kb.keyboard_att("bos"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Хлебников Даниил (Машинное обучение)',
                "prefix": "xleb",
                "states": {
                    "mark": st.Prepods.xlebnikov_mark,
                    "att": st.Prepods.xlebnikov_att,
                    "com": st.Prepods.xlebnikov_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("xleb"),
                    "att": kb.keyboard_att("xleb"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Носкова Елизавета (Машинное обучение)',
                "prefix": "nos",
                "states": {
                    "mark": st.Prepods.noskova_mark,
                    "att": st.Prepods.noskova_att,
                    "com": st.Prepods.noskova_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("nos"),
                    "att": kb.keyboard_att("nos"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Голышев Сергей Александрович (Электронная микроскопия, спецкурс)',
                "prefix": "gol",
                "states": {
                    "mark": st.Prepods.golishev_mark,
                    "att": st.Prepods.golishev_att,
                    "com": st.Prepods.golishev_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("gol"),
                    "att": kb.keyboard_att("gol"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Мулкиджанян Армен Яковлевич (Молекулярная биоэнергетика, спецкурс)',
                "prefix": "mul",
                "states": {
                    "mark": st.Prepods.mulkidzhanyan_mark,
                    "att": st.Prepods.mulkidzhanyan_att,
                    "com": st.Prepods.mulkidzhanyan_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("mul"),
                    "att": kb.keyboard_att("mul"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Головин Андрей Викторович (Моделирование структур биополимеров, спецкурс)',
                "prefix": "golo",
                "states": {
                    "mark": st.Prepods.golovin_mark,
                    "att": st.Prepods.golovin_att,
                    "com": st.Prepods.golovin_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("golo"),
                    "att": kb.keyboard_att("golo"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Покровский Вадим Сергеевич (Экспериментальная онкология, спецкурс)',
                "prefix": "pok",
                "states": {
                    "mark": st.Prepods.pokrovskii_mark,
                    "att": st.Prepods.pokrovskii_att,
                    "com": st.Prepods.pokrovskii_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("pok"),
                    "att": kb.keyboard_att("pok"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Аветисян Нелли Гургеновна (Методология специальности на английском языке, факультатив)',
                "prefix": "ave4",
                "states": {
                    "mark": st.Prepods.avetisyan4_mark,
                    "att": st.Prepods.avetisyan4_att,
                    "com": st.Prepods.avetisyan4_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("ave4"),
                    "att": kb.keyboard_att("ave4"),
                    "com": kb.keyboard_com,
                }
            },
        ]
    },
    "5": {
        "name": "Пятый курс",
        "teachers": [
            {
                "name": 'Сергиев Пётр Владимирович (Молекулярная биология)',
                "prefix": "ser",
                "states": {
                    "mark": st.Prepods.sergiev_mark,
                    "att": st.Prepods.sergiev_att,
                    "com": st.Prepods.sergiev_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("ser"),
                    "att": kb.keyboard_att("ser"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Шепелев Никита Михайлович (Молекулярная биология)',
                "prefix": "she",
                "states": {
                    "mark": st.Prepods.shepelev_mark,
                    "att": st.Prepods.shepelev_att,
                    "com": st.Prepods.shepelev_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("she"),
                    "att": kb.keyboard_att("she"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Никитин Михаил Александрович (Современное естествознание)',
                "prefix": "nik",
                "states": {
                    "mark": st.Prepods.nikitin_mark,
                    "att": st.Prepods.nikitin_att,
                    "com": st.Prepods.nikitin_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("nik"),
                    "att": kb.keyboard_att("nik"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Хмелевская Светлана Анатольевна (Философия)',
                "prefix": "hme",
                "states": {
                    "mark": st.Prepods.hmelevskaya_mark,
                    "att": st.Prepods.hmelevskaya_att,
                    "com": st.Prepods.hmelevskaya_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("hme"),
                    "att": kb.keyboard_att("hme"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Качалкин Анатолий Николаевич (Русский язык и культура речи)',
                "prefix": "kac",
                "states": {
                    "mark": st.Prepods.kachalkin_mark,
                    "att": st.Prepods.kachalkin_att,
                    "com": st.Prepods.kachalkin_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("kac"),
                    "att": kb.keyboard_att("kac"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Северин Федор Федорович (Molecular biology of the cell (in English))',
                "prefix": "sev",
                "states": {
                    "mark": st.Prepods.severin_mark,
                    "att": st.Prepods.severin_att,
                    "com": st.Prepods.severin_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("sev"),
                    "att": kb.keyboard_att("sev"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Соловьев Андрей Геннадьевич (Биоинженерия вирусных частиц (спецкурс по выбору I))',
                "prefix": "sol",
                "states": {
                    "mark": st.Prepods.soloviev_mark,
                    "att": st.Prepods.soloviev_att,
                    "com": st.Prepods.soloviev_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("sol"),
                    "att": kb.keyboard_att("sol"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Чиганов Ярослав Геннадьевич (Проектирование, построение и анализ баз данных (спецкурс по выбору I))',
                "prefix": "chi",
                "states": {
                    "mark": st.Prepods.chiganov_mark,
                    "att": st.Prepods.chiganov_att,
                    "com": st.Prepods.chiganov_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("chi"),
                    "att": kb.keyboard_att("chi"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Дмитриев Сергей Евгеньевич (Systems biology of aging (in English; спецкурс по выбору II))',
                "prefix": "dmi2",
                "states": {
                    "mark": st.Prepods.dmitriev2_mark,
                    "att": st.Prepods.dmitriev2_att,
                    "com": st.Prepods.dmitriev2_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("dmi2"),
                    "att": kb.keyboard_att("dmi2"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Зайцев Сергей Владимирович (Integrative mechanisms of diabetes: cellular and molecular aspects\n(in English; спецкурс по выбору II))',
                "prefix": "zai",
                "states": {
                    "mark": st.Prepods.zaicev_mark,
                    "att": st.Prepods.zaicev_att,
                    "com": st.Prepods.zaicev_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("zai"),
                    "att": kb.keyboard_att("zai"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Сперанская Светлана Сергеевна (Немецкий язык (факультатив))',
                "prefix": "spe",
                "states": {
                    "mark": st.Prepods.speranskaya_mark,
                    "att": st.Prepods.speranskaya_att,
                    "com": st.Prepods.speranskaya_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("spe"),
                    "att": kb.keyboard_att("spe"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Дикарева Ксения Андреевна (Французский язык (факультатив))',
                "prefix": "dik",
                "states": {
                    "mark": st.Prepods.dikareva_mark,
                    "att": st.Prepods.dikareva_att,
                    "com": st.Prepods.dikareva_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("dik"),
                    "att": kb.keyboard_att("dik"),
                    "com": kb.keyboard_com,
                }
            },
            {
                "name": 'Карелина Наталья Александровна (Методология специальности на английском языке (факультатив))',
                "prefix": "kar5",
                "states": {
                    "mark": st.Prepods.karelina5_mark,
                    "att": st.Prepods.karelina5_att,
                    "com": st.Prepods.karelina5_com,
                },
                "keyboards": {
                    "mark": kb.keyboard_marks("kar5"),
                    "att": kb.keyboard_att("kar5"),
                    "com": kb.keyboard_com,
                }
            },
        ]
    },
}