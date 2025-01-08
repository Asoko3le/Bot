from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton,   InlineKeyboardMarkup)


mainmenu1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Я знаю направление☑️', callback_data='znayu')],
    [InlineKeyboardButton(text='Пройти мини-тест📝', callback_data='STEST')]
])




mainmenuwith = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Подробнее про направление📍', callback_data='Podrobnee')],
    [InlineKeyboardButton(text='Выбрать вуз🏫', callback_data='Vyzi2')],
    [InlineKeyboardButton(text='Обзор всех направлений🔍', callback_data='Obzor2')],
    [InlineKeyboardButton(text='Дополнительно🖇', callback_data='Dop')]
])


Dop = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Выбрать другое направление🔍', callback_data='znayu')],
    [InlineKeyboardButton(text='Пройти тест на направление📝', callback_data='STEST')],
    [InlineKeyboardButton(text='Бесплатные курсы📚', url = 'https://dopobr.petersburgedu.ru')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])




Vyzi2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Физ-мат🧮', callback_data='Fm2')],
    [InlineKeyboardButton(text='Гуманитарные✍', callback_data='Gm2')],
    [InlineKeyboardButton(text='Хим-био🧪', callback_data='Hm2')]
])

FizMat2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Инженер', callback_data='Popinz1')],
    [InlineKeyboardButton(text='IT-специалист', callback_data='Popit1')],
    [InlineKeyboardButton(text='Экономист', callback_data='Popecon1')],
    [InlineKeyboardButton(text='Финансист', callback_data='Popfin1')],
    [InlineKeyboardButton(text='Бухгалтер', callback_data='Popbuh1')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Dop')]
])
Gym2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Маркетолог', callback_data='Popmark1')],
    [InlineKeyboardButton(text='Адвокат', callback_data='Popadv1')],
    [InlineKeyboardButton(text='Журналист', callback_data='Popzhur1')],
    [InlineKeyboardButton(text='Преподаватель', callback_data='Popprep1')],
    [InlineKeyboardButton(text='Психолог', callback_data='Poppsihol1')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Dop')]
])
HimBio2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Химик', callback_data='Pophim1')],
    [InlineKeyboardButton(text='Эколог', callback_data='Popecol1')],
    [InlineKeyboardButton(text='Психотерапевт', callback_data='Poppsihoter1')],
    [InlineKeyboardButton(text='Аллерголог', callback_data='Popall1')],
    [InlineKeyboardButton(text='Ботаник', callback_data='Popbot1')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Dop')]
])






































# region OBZOR2

Obzor2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Физ-мат🧮', callback_data='Fm1')],
    [InlineKeyboardButton(text='Гуманитарные✍', callback_data='Gm1')],
    [InlineKeyboardButton(text='Хим-био🧪', callback_data='Hm1')]
])

FizMat1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Инженер', callback_data='Popinz')],
    [InlineKeyboardButton(text='IT-специалист', callback_data='Popit')],
    [InlineKeyboardButton(text='Экономист', callback_data='Popecon')],
    [InlineKeyboardButton(text='Финансист', callback_data='Popfin')],
    [InlineKeyboardButton(text='Бухгалтер', callback_data='Popbuh')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Dop')]
])
Gym1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Маркетолог', callback_data='Popmark')],
    [InlineKeyboardButton(text='Адвокат', callback_data='Popadv')],
    [InlineKeyboardButton(text='Журналист', callback_data='Popzhur')],
    [InlineKeyboardButton(text='Преподаватель', callback_data='Popprep')],
    [InlineKeyboardButton(text='Психолог', callback_data='Poppsihol')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Dop')]
])
HimBio1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Химик', callback_data='Pophim')],
    [InlineKeyboardButton(text='Эколог', callback_data='Popecol')],
    [InlineKeyboardButton(text='Психотерапевт', callback_data='Poppsihoter')],
    [InlineKeyboardButton(text='Аллерголог', callback_data='Popall')],
    [InlineKeyboardButton(text='Ботаник', callback_data='Popbot')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Dop')]
])

# endregion
# region -
Popinz = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Курсы📚', url = 'https://clck.ru/3FcvCm')],
    [InlineKeyboardButton(text='Вузы🏫', callback_data='Popinz1')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])

Popit = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Курсы📚',url = 'https://clck.ru/3FcvCm')],
    [InlineKeyboardButton(text='Вузы🏫', callback_data='Vyz')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])

Popecon = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Курсы📚', url = 'https://clck.ru/3FcvCm')],
    [InlineKeyboardButton(text='Вузы🏫', callback_data='Vyz')],
    [InlineKeyboardButton(text='Назад', callback_data='main')]
])

Popfin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Курсы📚', url = 'https://clck.ru/3FcvCm')],
    [InlineKeyboardButton(text='Вузы🏫', callback_data='Vyz')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])

Popbuh = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Курсы📚', url = 'https://clck.ru/3FcvCm')],
    [InlineKeyboardButton(text='Вузы🏫', callback_data='Vyz')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])

Popmark = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Курсы📚', url = 'https://clck.ru/3FcvCm')],
    [InlineKeyboardButton(text='Вузы🏫', callback_data='Vyz')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])

Popadv = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Курсы📚', url = 'https://clck.ru/3FcvCm')],
    [InlineKeyboardButton(text='Вузы🏫', callback_data='Vyz')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])

Popzhur = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Курсы📚', url = 'https://clck.ru/3FcvCm')],
    [InlineKeyboardButton(text='Вузы🏫', callback_data='Vyz')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])

Popprep = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Курсы📚', url = 'https://clck.ru/3FcvCm')],
    [InlineKeyboardButton(text='Вузы🏫', callback_data='Vyz')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])

Poppsihol = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Курсы📚', url = 'https://clck.ru/3FcvCm')],
    [InlineKeyboardButton(text='Вузы🏫', callback_data='Vyz')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])

Pophim = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Курсы📚', url = 'https://clck.ru/3FcvCm')],
    [InlineKeyboardButton(text='Вузы🏫', callback_data='Vyz')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])

Popecol = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Курсы📚', url = 'https://clck.ru/3FcvCm')],
    [InlineKeyboardButton(text='Вузы🏫', callback_data='Vyz')],
    [InlineKeyboardButton(text='Назад🏫📌', callback_data='main')]
])

Poppsihoter = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Курсы📚', url = 'https://clck.ru/3FcvCm')],
    [InlineKeyboardButton(text='Вузы🏫', callback_data='Vyz')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])

Popall = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Курсы📚', url = 'https://clck.ru/3FcvCm')],
    [InlineKeyboardButton(text='Вузы🏫', callback_data='Vyz')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])

Popbot = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Курсы📚', url = 'https://clck.ru/3FcvCm')],
    [InlineKeyboardButton(text='Вузы🏫', callback_data='Vyz')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])


# endregion






















# region
Obzor1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Физ-мат🧮', callback_data='Fm')],
    [InlineKeyboardButton(text='Гуманитарные✍', callback_data='Gm')],
    [InlineKeyboardButton(text='Хим-био🧪', callback_data='Hm')]
])

FizMat = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Инженер', callback_data='Sinz')],
    [InlineKeyboardButton(text='IT-специалист', callback_data='Sit')],
    [InlineKeyboardButton(text='Экономист', callback_data='Sec')],
    [InlineKeyboardButton(text='Финансист', callback_data='Sfin')],
    [InlineKeyboardButton(text='Бухгалтер', callback_data='Sbuh')],
    [InlineKeyboardButton(text='Назад📌', callback_data='znayu')]
])

HimBio = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Химик', callback_data='Shim')],
    [InlineKeyboardButton(text='Эколог', callback_data='Secol')],
    [InlineKeyboardButton(text='Психотерапевт', callback_data='Spsihoter')],
    [InlineKeyboardButton(text='Аллерголог', callback_data='Sall')],
    [InlineKeyboardButton(text='Ботаник', callback_data='Sbot')],
    [InlineKeyboardButton(text='Назад📌', callback_data='znayu')]
])

Gym = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Маркетолог', callback_data='Smark')],
    [InlineKeyboardButton(text='Адвокат', callback_data='Sadv')],
    [InlineKeyboardButton(text='Журналист', callback_data='Szhur')],
    [InlineKeyboardButton(text='Преподаватель', callback_data='Sprep')],
    [InlineKeyboardButton(text='Психолог', callback_data='Spsihol')],
    [InlineKeyboardButton(text='Назад📌', callback_data='znayu')]
])



Sinz = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Верно!✅', callback_data='main')],
    [InlineKeyboardButton(text='Поменять↺', callback_data='Fm')]
])

stest = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Пройти!📍', callback_data='starttest')],
    [InlineKeyboardButton(text='Вернутся📌', callback_data='main')]
])


#endregion
# region
vop1 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='А', callback_data='1a')],
    [InlineKeyboardButton(text='B', callback_data='1b')],
    [InlineKeyboardButton(text='C', callback_data='1c')]
])
vop2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='A', callback_data='2a')],
    [InlineKeyboardButton(text='B', callback_data='2b')],
    [InlineKeyboardButton(text='C', callback_data='2c')]
])
vop3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='A', callback_data='3a')],
    [InlineKeyboardButton(text='B', callback_data='3b')],
    [InlineKeyboardButton(text='C', callback_data='3c')]
])
vop4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='A', callback_data='4a')],
    [InlineKeyboardButton(text='B', callback_data='4b')],
    [InlineKeyboardButton(text='C', callback_data='4c')]
])
vop5 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='A', callback_data='5a')],
    [InlineKeyboardButton(text='B', callback_data='5b')],
    [InlineKeyboardButton(text='C', callback_data='5c')]
])
vop6 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='A', callback_data='6a')],
    [InlineKeyboardButton(text='B', callback_data='6b')],
    [InlineKeyboardButton(text='C', callback_data='6c')]
])
vop7 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='A', callback_data='7a')],
    [InlineKeyboardButton(text='B', callback_data='7b')],
    [InlineKeyboardButton(text='C', callback_data='7c')]
])
vop8 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='A', callback_data='8a')],
    [InlineKeyboardButton(text='B', callback_data='8b')],
    [InlineKeyboardButton(text='C', callback_data='8c')]
])
vop9 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='A', callback_data='9a')],
    [InlineKeyboardButton(text='B', callback_data='9b')],
    [InlineKeyboardButton(text='C', callback_data='9c')]
])
vop10 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='A', callback_data='10a')],
    [InlineKeyboardButton(text='B', callback_data='10b')],
    [InlineKeyboardButton(text='C', callback_data='10c')]
])
vop11 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='A', callback_data='11a')],
    [InlineKeyboardButton(text='B', callback_data='11b')],
    [InlineKeyboardButton(text='C', callback_data='11c')]
])
vop12 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='A', callback_data='12a')],
    [InlineKeyboardButton(text='B', callback_data='12b')],
    [InlineKeyboardButton(text='C', callback_data='12c')]
])
vop13 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='A', callback_data='13a')],
    [InlineKeyboardButton(text='B', callback_data='13b')],
    [InlineKeyboardButton(text='C', callback_data='13c')]
])
vop14 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='A', callback_data='14a')],
    [InlineKeyboardButton(text='B', callback_data='14b')],
    [InlineKeyboardButton(text='C', callback_data='14c')]
])
vop15 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='A', callback_data='15a')],
    [InlineKeyboardButton(text='B', callback_data='15b')],
    [InlineKeyboardButton(text='C', callback_data='15c')]
])


YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='mxpr', callback_data='main')]
])


# endregion







