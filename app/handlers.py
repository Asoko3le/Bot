#region /
from aiogram import F, Router, types
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command, Filter
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import sqlite3
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton,   InlineKeyboardMarkup)


import app.keyboards as kb



# роутер, для замены dp
router = Router()


conn = sqlite3.connect('users.db')
cursor = conn.cursor()
#endregion


# region KOMANDI
def tabl(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR REPLACE INTO professions_test(user_id, nap, Inz, It, Mark, Him, Econ, Bot, "All", Psihoter, Ecol, Psiholog, Prep, Zhur, Adv, Buh, Fin) VALUES (?, NULL , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)',(user_id,))
    conn.commit()
    conn.close()

def test(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT user_id, Inz, It, Mark, Him, Econ, Bot, "All", Psihoter, Ecol, Psiholog, Prep, Zhur, Adv, Buh, Fin FROM professions_test WHERE user_id = ?' ,(user_id,))
    rows = cursor.fetchall()
    for row in rows:
        user_id = row[0]
        professions = {
            'F1': row[1],
            'F2': row[2],
            'G1': row[3],
            'H1': row[4],
            'F3': row[5],
            'H5': row[6],
            'H4': row[7],
            'H3': row[8],
            'H2': row[9],
            'G5': row[10],
            'G4': row[11],
            'G3': row[12],
            'G2': row[13],
            'F5': row[14],
            'F4': row[15]
    }
    sorted_professions = sorted(professions.items(), key=lambda x: x[1], reverse=True)
    
    mxpr = sorted_professions[0][0]
    mxpr2 = sorted_professions[1][0]
    conn.close()
    return mxpr, mxpr2

def first(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor
    cursor.execute("INSERT OR IGNORE INTO users (user_id, napravlenie) VALUES (? , ?)", (user_id, 'nety'))
    cursor.execute('INSERT OR IGNORE INTO professions_test (user_id) VALUES (?)',(user_id,))
    conn.commit()
    conn.close()

def nap(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute("SELECT napravlenie FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()

    conn.close()

    if result is None or result[0] == "nety":
        return 0
    elif result[0] == "F1":
        return 11
    elif result[0] == 'F2':
        return 12
    elif result[0] =='F3':
        return 13
    elif result[0] == 'G1':
        return 21
    elif result[0] == 'G2':
        return 22
    elif result[0] == 'G3':
        return 23
    elif result[0] == 'H1':
        return 31
    elif result[0] == 'H2':
        return 32
    elif result[0] == 'H3':
        return 32
    else:
        return 999
    
def napslovo(user_id):
    cursor.execute('SELECT napravlenie FROM users WHERE user_id = ?', (user_id,))
    res = cursor.fetchone() 
    if res:
        napravlenie_code = res[0]  
        cursor.execute('SELECT name FROM directions WHERE code = ?', (napravlenie_code,))
        res1 = cursor.fetchone() 
        if res1:
            return res1[0]  
 
def test2(user_id):
    mxpr, mxpr2 = test(user_id)
    nap1 = mxpr
    nap2 = mxpr2
    cursor.execute('SELECT name FROM directions WHERE code = ?', (nap1,))
    re11 = cursor.fetchone()
    re1 = re11[0]
    cursor.execute('SELECT name FROM directions WHERE code = ?', (nap2,))
    re22 = cursor.fetchone()
    re2 = re22[0]
    return re1,re2

#endregion





#MAIN MENU 

@router.message(CommandStart())
async def cmd_start(message: Message):
    user_id = message.from_user.id
    if nap(user_id) == 0:
        await message.answer("Привет\n\nБот для помощи в профориентации, найди: \nНа кого поступать?\nКуда поступать?\nГде подготовиться?\n\nТут постарались собрать самое важное🔥", reply_markup=kb.mainmenu1)
        first(user_id)
        tabl(user_id)
    else:
        res1 = napslovo(user_id)
        await message.answer(f"Ваше направление:\n{res1}\n\nНайди подходящие курсы в портале и реши куда поступать!", reply_markup=kb.mainmenuwith)
    
@router.callback_query(F.data=='main')
async def tsh(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    if nap(user_id) == 0:
        await callback.message.edit_text("Привет\n\nБот для помощи в профориентации, найди: \nНа кого поступать?\nКуда поступать?\nГде подготовиться?\n\nТут постарались собрать самое важное🔥", reply_markup=kb.mainmenu1)
        first(user_id)
    else:
        res1 = napslovo(user_id)
        await callback.message.edit_text(f"Ваше направление:\n{res1}\n\nНайди подходящие курсы в портале и реши куда поступать!", reply_markup=kb.mainmenuwith)





@router.callback_query(F.data=='Dop')
async def tsh(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('▼Дополнительно▼',reply_markup=kb.Dop)





@router.callback_query(F.data=='Vyzi2')
async def tsh(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Выберите направление для подбора соотвествующих вузов',reply_markup=kb.Vyzi2)


@router.callback_query(F.data=='Fm2')
async def tsh(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Выберите профессию для подбора соотвествующих вузов',reply_markup=kb.FizMat2)

@router.callback_query(F.data=='Gm2')
async def tsh(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Выберите профессию для подбора соотвествующих вузов',reply_markup=kb.Gym2)

@router.callback_query(F.data=='Hm2')
async def tsh(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Выберите профессию для подбора соотвествующих вузов',reply_markup=kb.HimBio2)


# region PODROBNEE
@router.callback_query(F.data=='Podrobnee')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('SELECT napravlenie FROM users WHERE user_id = ?',(user_id,))
    nap1 = cursor.fetchone()
    nap=nap1[0]
    cursor.execute(f'SELECT Descript FROM directions WHERE code = ?',(nap,))
    napr1 = cursor.fetchone()
    napr=napr1[0]
    cursor.execute(f'SELECT Vyzteg FROM directions WHERE code = ?',(nap,))
    aba1 = cursor.fetchone()
    aba=aba1[0]
    podrob = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вузы по направлению🏫', callback_data=f'{aba}')],
    [InlineKeyboardButton(text='Бесплатные курсы📚', url = 'https://dopobr.petersburgedu.ru')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{napr}\n',reply_markup=podrob)


# endregion

















# region Vyz

@router.callback_query(F.data == 'Popinz1')
async def tsh(callback: CallbackQuery):
    # Выполнение SQL-запроса
    cursor.execute('SELECT sokrash, vyz_sokr FROM vyz WHERE napravlenie = "Inz"')
    res = cursor.fetchall()
    
    # Создаем список для кнопок
    buttons = []
    
    # Добавляем кнопки для каждой записи в res
    for gg in res:
        buttons.append([InlineKeyboardButton(text=gg[0], callback_data=gg[1])])
    buttons.append([InlineKeyboardButton(text='Настройки поиска', callback_data='opt')])
    buttons.append([InlineKeyboardButton(text='Назад📌', callback_data='main')])
    # Создаем клавиатуру из списка кнопок
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.answer('')
    await callback.message.edit_text('Список вузов, в которых можно обучиться на профессию инженера',reply_markup=keyboard)

@router.callback_query(F.data == 'Popit1')
async def tsh(callback: CallbackQuery):
    # Выполнение SQL-запроса
    cursor.execute('SELECT sokrash, vyz_sokr FROM vyz WHERE napravlenie = "It"')
    res = cursor.fetchall()
    
    # Создаем список для кнопок
    buttons = []
    
    # Добавляем кнопки для каждой записи в res
    for gg in res:
        buttons.append([InlineKeyboardButton(text=gg[0], callback_data=gg[1])])
    buttons.append([InlineKeyboardButton(text='Настройки поиска', callback_data='opt')])
    buttons.append([InlineKeyboardButton(text='Назад📌', callback_data='main')])
    # Создаем клавиатуру из списка кнопок
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.answer('')
    await callback.message.edit_text(f'Список вузов, в которых можно обучиться на профессию It-специалиста',reply_markup=keyboard)

@router.callback_query(F.data == 'Popecon1')
async def tsh(callback: CallbackQuery):
    # Выполнение SQL-запроса
    cursor.execute('SELECT sokrash, vyz_sokr FROM vyz WHERE napravlenie = "Econ"')
    res = cursor.fetchall()
    
    # Создаем список для кнопок
    buttons = []
    
    # Добавляем кнопки для каждой записи в res
    for gg in res:
        buttons.append([InlineKeyboardButton(text=gg[0], callback_data=gg[1])])
    buttons.append([InlineKeyboardButton(text='Настройки поиска', callback_data='opt')])
    buttons.append([InlineKeyboardButton(text='Назад📌', callback_data='main')])
    # Создаем клавиатуру из списка кнопок
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.answer('')
    await callback.message.edit_text(f'Список вузов, в которых можно обучиться на профессию Экономиста',reply_markup=keyboard)

@router.callback_query(F.data == 'Popfin1')
async def tsh(callback: CallbackQuery):
    # Выполнение SQL-запроса
    cursor.execute('SELECT sokrash, vyz_sokr FROM vyz WHERE napravlenie = "Fin"')
    res = cursor.fetchall()
    
    # Создаем список для кнопок
    buttons = []
    
    # Добавляем кнопки для каждой записи в res
    for gg in res:
        buttons.append([InlineKeyboardButton(text=gg[0], callback_data=gg[1])])
    buttons.append([InlineKeyboardButton(text='Настройки поиска', callback_data='opt')])
    buttons.append([InlineKeyboardButton(text='Назад📌', callback_data='main')])
    # Создаем клавиатуру из списка кнопок
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.answer('')
    await callback.message.edit_text(f'Список вузов, в которых можно обучиться на профессию Финансиста',reply_markup=keyboard)

@router.callback_query(F.data == 'Popbuh1')
async def tsh(callback: CallbackQuery):
    # Выполнение SQL-запроса
    cursor.execute('SELECT sokrash, vyz_sokr FROM vyz WHERE napravlenie = "Buh"')
    res = cursor.fetchall()
    
    # Создаем список для кнопок
    buttons = []
    
    # Добавляем кнопки для каждой записи в res
    for gg in res:
        buttons.append([InlineKeyboardButton(text=gg[0], callback_data=gg[1])])
    buttons.append([InlineKeyboardButton(text='Настройки поиска', callback_data='opt')])
    buttons.append([InlineKeyboardButton(text='Назад📌', callback_data='main')])
    # Создаем клавиатуру из списка кнопок
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.answer('')
    await callback.message.edit_text(f'Список вузов, в которых можно обучиться на профессию Бухгалтер',reply_markup=keyboard)


@router.callback_query(F.data == 'Pophim1')
async def tsh(callback: CallbackQuery):
    # Выполнение SQL-запроса
    cursor.execute('SELECT sokrash, vyz_sokr FROM vyz WHERE napravlenie = "Him"')
    res = cursor.fetchall()
    
    # Создаем список для кнопок
    buttons = []
    
    # Добавляем кнопки для каждой записи в res
    for gg in res:
        buttons.append([InlineKeyboardButton(text=gg[0], callback_data=gg[1])])
    buttons.append([InlineKeyboardButton(text='Настройки поиска', callback_data='opt')])
    buttons.append([InlineKeyboardButton(text='Назад📌', callback_data='main')])
    # Создаем клавиатуру из списка кнопок
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.answer('')
    await callback.message.edit_text(f'Список вузов, в которых можно обучиться на профессию Химика',reply_markup=keyboard)

@router.callback_query(F.data == 'Popecol1')
async def tsh(callback: CallbackQuery):
    # Выполнение SQL-запроса
    cursor.execute('SELECT sokrash, vyz_sokr FROM vyz WHERE napravlenie = "Ecol"')
    res = cursor.fetchall()
    
    # Создаем список для кнопок
    buttons = []
    
    # Добавляем кнопки для каждой записи в res
    for gg in res:
        buttons.append([InlineKeyboardButton(text=gg[0], callback_data=gg[1])])
    buttons.append([InlineKeyboardButton(text='Настройки поиска', callback_data='opt')])
    buttons.append([InlineKeyboardButton(text='Назад📌', callback_data='main')])
    # Создаем клавиатуру из списка кнопок
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.answer('')
    await callback.message.edit_text(f'Список вузов, в которых можно обучиться на профессию Эколога',reply_markup=keyboard)

@router.callback_query(F.data == 'Poppsihoter1')
async def tsh(callback: CallbackQuery):
    # Выполнение SQL-запроса
    cursor.execute('SELECT sokrash, vyz_sokr FROM vyz WHERE napravlenie = "Psihoter"')
    res = cursor.fetchall()
    
    # Создаем список для кнопок
    buttons = []
    
    # Добавляем кнопки для каждой записи в res
    for gg in res:
        buttons.append([InlineKeyboardButton(text=gg[0], callback_data=gg[1])])
    buttons.append([InlineKeyboardButton(text='Настройки поиска', callback_data='opt')])
    buttons.append([InlineKeyboardButton(text='Назад📌', callback_data='main')])
    # Создаем клавиатуру из списка кнопок
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.answer('')
    await callback.message.edit_text(f'Список вузов, в которых можно обучиться на профессию Психотерапевта',reply_markup=keyboard)

@router.callback_query(F.data == 'Popall1')
async def tsh(callback: CallbackQuery):
    # Выполнение SQL-запроса
    cursor.execute('SELECT sokrash, vyz_sokr FROM vyz WHERE napravlenie = "All"')
    res = cursor.fetchall()
    
    # Создаем список для кнопок
    buttons = []
    
    # Добавляем кнопки для каждой записи в res
    for gg in res:
        buttons.append([InlineKeyboardButton(text=gg[0], callback_data=gg[1])])
    buttons.append([InlineKeyboardButton(text='Настройки поиска', callback_data='opt')])
    buttons.append([InlineKeyboardButton(text='Назад📌', callback_data='main')])
    # Создаем клавиатуру из списка кнопок
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.answer('')
    await callback.message.edit_text(f'Список вузов, в которых можно обучиться на профессию Аллерголога',reply_markup=keyboard)

@router.callback_query(F.data == 'Popbot1')
async def tsh(callback: CallbackQuery):
    # Выполнение SQL-запроса
    cursor.execute('SELECT sokrash, vyz_sokr FROM vyz WHERE napravlenie = "Bot"')
    res = cursor.fetchall()
    
    # Создаем список для кнопок
    buttons = []
    
    # Добавляем кнопки для каждой записи в res
    for gg in res:
        buttons.append([InlineKeyboardButton(text=gg[0], callback_data=gg[1])])
    buttons.append([InlineKeyboardButton(text='Настройки поиска', callback_data='opt')])
    buttons.append([InlineKeyboardButton(text='Назад📌', callback_data='main')])
    # Создаем клавиатуру из списка кнопок
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.answer('')
    await callback.message.edit_text(f'Список вузов, в которых можно обучиться на профессию Ботаника',reply_markup=keyboard)

@router.callback_query(F.data == 'Popmark1')
async def tsh(callback: CallbackQuery):
    # Выполнение SQL-запроса
    cursor.execute('SELECT sokrash, vyz_sokr FROM vyz WHERE napravlenie = "Mark"')
    res = cursor.fetchall()
    
    # Создаем список для кнопок
    buttons = []
    
    # Добавляем кнопки для каждой записи в res
    for gg in res:
        buttons.append([InlineKeyboardButton(text=gg[0], callback_data=gg[1])])
    buttons.append([InlineKeyboardButton(text='Настройки поиска', callback_data='opt')])
    buttons.append([InlineKeyboardButton(text='Назад📌', callback_data='main')])
    # Создаем клавиатуру из списка кнопок
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.answer('')
    await callback.message.edit_text(f'Список вузов, в которых можно обучиться на профессию Маркетолога',reply_markup=keyboard)

@router.callback_query(F.data == 'Popadv1')
async def tsh(callback: CallbackQuery):
    # Выполнение SQL-запроса
    cursor.execute('SELECT sokrash, vyz_sokr FROM vyz WHERE napravlenie = "Adv"')
    res = cursor.fetchall()
    
    # Создаем список для кнопок
    buttons = []
    
    # Добавляем кнопки для каждой записи в res
    for gg in res:
        buttons.append([InlineKeyboardButton(text=gg[0], callback_data=gg[1])])
    buttons.append([InlineKeyboardButton(text='Настройки поиска', callback_data='opt')])
    buttons.append([InlineKeyboardButton(text='Назад📌', callback_data='main')])
    # Создаем клавиатуру из списка кнопок
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.answer('')
    await callback.message.edit_text(f'Список вузов, в которых можно обучиться на профессию Адвоката',reply_markup=keyboard)

@router.callback_query(F.data == 'Popzhur1')
async def tsh(callback: CallbackQuery):
    # Выполнение SQL-запроса
    cursor.execute('SELECT sokrash, vyz_sokr FROM vyz WHERE napravlenie = "Zhur"')
    res = cursor.fetchall()
    
    # Создаем список для кнопок
    buttons = []
    
    # Добавляем кнопки для каждой записи в res
    for gg in res:
        buttons.append([InlineKeyboardButton(text=gg[0], callback_data=gg[1])])
    buttons.append([InlineKeyboardButton(text='Настройки поиска', callback_data='opt')])
    buttons.append([InlineKeyboardButton(text='Назад📌', callback_data='main')])
    # Создаем клавиатуру из списка кнопок
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.answer('')
    await callback.message.edit_text(f'Список вузов, в которых можно обучиться на профессию Журналиста',reply_markup=keyboard)


@router.callback_query(F.data == 'Popprep1')
async def tsh(callback: CallbackQuery):
    # Выполнение SQL-запроса
    cursor.execute('SELECT sokrash, vyz_sokr FROM vyz WHERE napravlenie = "Prep"')
    res = cursor.fetchall()
    
    # Создаем список для кнопок
    buttons = []
    
    # Добавляем кнопки для каждой записи в res
    for gg in res:
        buttons.append([InlineKeyboardButton(text=gg[0], callback_data=gg[1])])
    buttons.append([InlineKeyboardButton(text='Настройки поиска', callback_data='opt')])
    buttons.append([InlineKeyboardButton(text='Назад📌', callback_data='main')])
    # Создаем клавиатуру из списка кнопок
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await callback.answer('')
    await callback.message.edit_text(f'Список вузов, в которых можно обучиться на профессию Преподователь',reply_markup=keyboard)

# endregion









# region - 


@router.callback_query(F.data=='opt')
async def tsh(callback: CallbackQuery):
    opt2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Поиск по городу', callback_data= 'optcity')],
    [InlineKeyboardButton(text='Поиск по проходному балу', callback_data='optpp')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')],
])
    await callback.answer('')
    await callback.message.edit_text('Настройки поиска:',reply_markup=opt2)















@router.callback_query(F.data=='optcity')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT DISTINCT gorod FROM vyz WHERE napravlenie = "Inz"')
    res = cursor.fetchall()
    
    # Создаем список для кнопок
    buttons1 = []
    
    # Добавляем кнопки для каждой записи в res
    for gg in res:
        buttons1.append([InlineKeyboardButton(text=gg[0], callback_data=f'op{gg[0]}')])
    buttons1.append([InlineKeyboardButton(text='Назад📌', callback_data='main')])
    await callback.answer('')
    await callback.message.edit_text('Выберите город для поиска',reply_markup=buttons1)

# endregion



















# region   Psihol
@router.callback_query(F.data=='mgypsih')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "mgypsih"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Poppsihol1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='vhepsih')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "vhepsih"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Poppsihol1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='sevpsih')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "sevpsih"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Poppsihol1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='vladpsih')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "vladpsih"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Poppsihol1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='mospsih')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "mospsih"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Poppsihol1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

# endregion

# region   Prep
@router.callback_query(F.data=='Mosprep')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "Mosprep"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popprep1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='rosprep')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "rosprep"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popprep1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='belprep')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "belprep"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popprep1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='sibprep')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "sibprep"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popprep1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='sevkavprep')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "sevkavprep"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popprep1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

# endregion

# region   Zhur
@router.callback_query(F.data=='zhu1')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "zhu1"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popzhur1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='zhu2')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "zhu2"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popzhur1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='zhu3')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "zhu3"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popzhur1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='zhu4')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "zhu4"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popzhur1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='zhu5')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "zhu5"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popzhur1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

# endregion

# region   Adv
@router.callback_query(F.data=='SpbAdv5')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "SpbAdv5"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popadv1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='SpbAdv4')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "SpbAdv4"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popadv1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='SpbAdv3')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "SpbAdv3"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popadv1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='SpbAdv2')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "SpbAdv2"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popadv1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='SpbAdv1')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "SpbAdv1"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popadv1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

# endregion

# region   Mark
@router.callback_query(F.data=='InzhMark')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "InzhMark"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popmark1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='MarkRus')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "MarkRus"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popmark1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='MarkSBGY')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "MarkSBGY"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popmark1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='SPBGYMARK')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "SPBGYMARK"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popmark1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='MARKSPB')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "MARKSPB"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popmark1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

# endregion

# region   Botanik
@router.callback_query(F.data=='Mosc1Botan')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "Mosc1Botan"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popbot1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='Mosc2Botan')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "Mosc2Botan"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popbot1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='KazanBot')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "KazanBot"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popbot1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='TomskBot')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "TomskBot"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popbot1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='Kyrgan1')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "Kyrgan1"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popbot1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

# endregion

# region   All
@router.callback_query(F.data=='SpbAll')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "SpbAll"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popall1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='SpbAll2')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "SpbAll2"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popall1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)


# endregion

# region   psihoter
@router.callback_query(F.data=='Spb1Psih')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "Spb1Psih"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Poppsihoter1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='Spb2Psih')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "Spb2Psih"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Poppsihoter1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='Spb3Psih')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "Spb3Psih"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Poppsihoter1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='Spb4Psih')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "Spb4Psih"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Poppsihoter1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='Spb5Psih')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "Spb5Psih"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Poppsihoter1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

# endregion

# region   Ecol
@router.callback_query(F.data=='YralEcol')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "YralEcol"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popecol1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='MosEcol')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "MosEcol"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popecol1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='DryzhbEcol')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "DryzhbEcol"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popecol1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='YfaEcol')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "YfaEcol"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popecol1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='SpbEcol')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "SpbEcol"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popecol1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

# endregion

# region   Him
@router.callback_query(F.data=='RosDruzh')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "RosDruzh"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Pophim1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='SPBGYHim')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "SPBGYHim"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Pophim1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='tomskYn')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "tomskYn"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Pophim1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='YralYn')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "YralYn"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Pophim1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='UFYROST')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "UFYROST"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Pophim1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

# endregion

# region   Buh
@router.callback_query(F.data=='MosBuh')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "MosBuh"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popbuh1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='SpbBuh')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "SpbBuh"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popbuh1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='SPBBUHG')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "SPBBUHG"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popbuh1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='NacBuhNN')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "NacBuhNN"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popbuh1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='VolgBuh')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "VolgBuh"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popbuh1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

# endregion

# region   Fin
@router.callback_query(F.data=='MTI')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "MTI"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popfin1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='SPbFin')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "SPbFin"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popfin1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='RANGHIS')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "RANGHIS"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popfin1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='SEVFIN')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "SEVFIN"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popfin1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='YralFin')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "YralFin"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popfin1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

# endregion

# region   Econ
@router.callback_query(F.data=='NIYVHE')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "NIYVHE"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popecon1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='SPSPB')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "SPSPB"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popecon1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='MGY')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "MGY"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popecon1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='NGY')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "NGY"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popecon1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='ALTAY')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "ALTAY"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popecon1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

# endregion

# region   IT
@router.callback_query(F.data=='MGTYBay')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "MGTYBay"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popit1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='ITMO')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "ITMO"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popit1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='SPBGY')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "SPBGY"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popit1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='YrFedElc')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "YrFedElc"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popit1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='KazFed')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "KazFed"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popit1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

# endregion

# region InzhVyz


@router.callback_query(F.data=='YrFedYnElc')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "YrFedYnElc"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popinz1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='SevGosYn')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "SevGosYn"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popinz1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='MosStankin')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "MosStankin"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popinz1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

@router.callback_query(F.data=='SaintPGY')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "SaintPGY"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popinz1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)


@router.callback_query(F.data=='SaintPPYPV')
async def tsh(callback: CallbackQuery):
    cursor.execute('SELECT gorod, site, prbb, prbp, Polnoe FROM vyz WHERE vyz_sokr = "SaintPPYPV"')
    pir = cursor.fetchall()
    YrFedYnElc = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Сайт учебного заведения🌐', url=f'{pir[0][1]}')],
    [InlineKeyboardButton(text='Назад📌', callback_data='Popinz1')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{pir[0][4]}\nГород - {pir[0][0]}\nПроходной бал бюджет - {pir[0][2]}\nПроходной бал платное - {pir[0][3]}',reply_markup=YrFedYnElc)

# endregion




































































# region OBZOR 2

@router.callback_query(F.data=='Obzor2')
async def tsh(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Популярные категории направлений',reply_markup=kb.Obzor2)


@router.callback_query(F.data=='Fm1')
async def tsh(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Подборка популярных направлений с физико-математическим уклоном',reply_markup=kb.FizMat1)

@router.callback_query(F.data=='Hm1')
async def tsh(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Подборка популярных направлений с хим-био уклоном',reply_markup=kb.HimBio1)

@router.callback_query(F.data=='Gm1')
async def tsh(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Подборка популярных направлений с гуманитарным уклоном',reply_markup=kb.Gym1)

# endregion


# region PODROBNEE

@router.callback_query(F.data=='Popinz')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute(f'SELECT Descript FROM directions WHERE code = "F1"')
    napr1 = cursor.fetchone()
    napr=napr1[0]
    cursor.execute(f'SELECT Vyzteg FROM directions WHERE code = "F1"')
    aba1 = cursor.fetchone()
    aba=aba1[0]
    podrob = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вузы по направлению🏫', callback_data=f'{aba}')],
    [InlineKeyboardButton(text='Бесплатные курсы📚', url = 'https://dopobr.petersburgedu.ru')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{napr}\n',reply_markup=podrob)


@router.callback_query(F.data=='Popit')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute(f'SELECT Descript FROM directions WHERE code = "F2"')
    napr1 = cursor.fetchone()
    napr=napr1[0]
    cursor.execute(f'SELECT Vyzteg FROM directions WHERE code = "F2"')
    aba1 = cursor.fetchone()
    aba=aba1[0]
    podrob = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вузы по направлению🏫', callback_data=f'{aba}')],
    [InlineKeyboardButton(text='Бесплатные курсы📚', url = 'https://dopobr.petersburgedu.ru')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{napr}\n',reply_markup=podrob)


@router.callback_query(F.data=='Popecon')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute(f'SELECT Descript FROM directions WHERE code = "F3"')
    napr1 = cursor.fetchone()
    napr=napr1[0]
    cursor.execute(f'SELECT Vyzteg FROM directions WHERE code = "F3"')
    aba1 = cursor.fetchone()
    aba=aba1[0]
    podrob = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вузы по направлению🏫', callback_data=f'{aba}')],
    [InlineKeyboardButton(text='Бесплатные курсы📚', url = 'https://dopobr.petersburgedu.ru')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{napr}\n',reply_markup=podrob)

@router.callback_query(F.data=='Popfin')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute(f'SELECT Descript FROM directions WHERE code = "F4"')
    napr1 = cursor.fetchone()
    napr=napr1[0]
    cursor.execute(f'SELECT Vyzteg FROM directions WHERE code = "F4"')
    aba1 = cursor.fetchone()
    aba=aba1[0]
    podrob = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вузы по направлению🏫', callback_data=f'{aba}')],
    [InlineKeyboardButton(text='Бесплатные курсы📚', url = 'https://dopobr.petersburgedu.ru')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{napr}\n',reply_markup=podrob)

@router.callback_query(F.data=='Popbuh')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute(f'SELECT Descript FROM directions WHERE code = "F5"')
    napr1 = cursor.fetchone()
    napr=napr1[0]
    cursor.execute(f'SELECT Vyzteg FROM directions WHERE code = "F5"')
    aba1 = cursor.fetchone()
    aba=aba1[0]
    podrob = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вузы по направлению🏫', callback_data=f'{aba}')],
    [InlineKeyboardButton(text='Бесплатные курсы📚', url = 'https://dopobr.petersburgedu.ru')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{napr}\n',reply_markup=podrob)



@router.callback_query(F.data=='Popmark')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute(f'SELECT Descript FROM directions WHERE code = "G1"')
    napr1 = cursor.fetchone()
    napr=napr1[0]
    cursor.execute(f'SELECT Vyzteg FROM directions WHERE code = "G1"')
    aba1 = cursor.fetchone()
    aba=aba1[0]
    podrob = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вузы по направлению🏫', callback_data=f'{aba}')],
    [InlineKeyboardButton(text='Бесплатные курсы📚', url = 'https://dopobr.petersburgedu.ru')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{napr}\n',reply_markup=podrob)

@router.callback_query(F.data=='Popadv')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute(f'SELECT Descript FROM directions WHERE code = "G2"')
    napr1 = cursor.fetchone()
    napr=napr1[0]
    cursor.execute(f'SELECT Vyzteg FROM directions WHERE code = "G2"')
    aba1 = cursor.fetchone()
    aba=aba1[0]
    podrob = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вузы по направлению🏫', callback_data=f'{aba}')],
    [InlineKeyboardButton(text='Бесплатные курсы📚', url = 'https://dopobr.petersburgedu.ru')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{napr}\n',reply_markup=podrob)

@router.callback_query(F.data=='Popzhur')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute(f'SELECT Descript FROM directions WHERE code = "G3"')
    napr1 = cursor.fetchone()
    napr=napr1[0]
    cursor.execute(f'SELECT Vyzteg FROM directions WHERE code = "G3"')
    aba1 = cursor.fetchone()
    aba=aba1[0]
    podrob = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вузы по направлению🏫', callback_data=f'{aba}')],
    [InlineKeyboardButton(text='Бесплатные курсы📚', url = 'https://dopobr.petersburgedu.ru')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{napr}\n',reply_markup=podrob)

@router.callback_query(F.data=='Popprep')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute(f'SELECT Descript FROM directions WHERE code = "G4"')
    napr1 = cursor.fetchone()
    napr=napr1[0]
    cursor.execute(f'SELECT Vyzteg FROM directions WHERE code = "G4"')
    aba1 = cursor.fetchone()
    aba=aba1[0]
    podrob = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вузы по направлению🏫', callback_data=f'{aba}')],
    [InlineKeyboardButton(text='Бесплатные курсы📚', url = 'https://dopobr.petersburgedu.ru')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{napr}\n',reply_markup=podrob)

@router.callback_query(F.data=='Popsihol')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute(f'SELECT Descript FROM directions WHERE code = "G5"')
    napr1 = cursor.fetchone()
    napr=napr1[0]
    cursor.execute(f'SELECT Vyzteg FROM directions WHERE code = "G5"')
    aba1 = cursor.fetchone()
    aba=aba1[0]
    podrob = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вузы по направлению🏫', callback_data=f'{aba}')],
    [InlineKeyboardButton(text='Бесплатные курсы📚', url = 'https://dopobr.petersburgedu.ru')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{napr}\n',reply_markup=podrob)




@router.callback_query(F.data=='Pophim')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute(f'SELECT Descript FROM directions WHERE code = "H1"')
    napr1 = cursor.fetchone()
    napr=napr1[0]
    cursor.execute(f'SELECT Vyzteg FROM directions WHERE code = "H1"')
    aba1 = cursor.fetchone()
    aba=aba1[0]
    podrob = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вузы по направлению🏫', callback_data=f'{aba}')],
    [InlineKeyboardButton(text='Бесплатные курсы📚', url = 'https://dopobr.petersburgedu.ru')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{napr}\n',reply_markup=podrob)

@router.callback_query(F.data=='Popecol')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute(f'SELECT Descript FROM directions WHERE code = "H2"')
    napr1 = cursor.fetchone()
    napr=napr1[0]
    cursor.execute(f'SELECT Vyzteg FROM directions WHERE code = "H2"')
    aba1 = cursor.fetchone()
    aba=aba1[0]
    podrob = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вузы по направлению🏫', callback_data=f'{aba}')],
    [InlineKeyboardButton(text='Бесплатные курсы📚', url = 'https://dopobr.petersburgedu.ru')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{napr}\n',reply_markup=podrob)

@router.callback_query(F.data=='Poppsihoter')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute(f'SELECT Descript FROM directions WHERE code = "H3"')
    napr1 = cursor.fetchone()
    napr=napr1[0]
    cursor.execute(f'SELECT Vyzteg FROM directions WHERE code = "H3"')
    aba1 = cursor.fetchone()
    aba=aba1[0]
    podrob = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вузы по направлению🏫', callback_data=f'{aba}')],
    [InlineKeyboardButton(text='Бесплатные курсы📚', url = 'https://dopobr.petersburgedu.ru')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{napr}\n',reply_markup=podrob)

@router.callback_query(F.data=='Popall')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute(f'SELECT Descript FROM directions WHERE code = "H4"')
    napr1 = cursor.fetchone()
    napr=napr1[0]
    cursor.execute(f'SELECT Vyzteg FROM directions WHERE code = "H4"')
    aba1 = cursor.fetchone()
    aba=aba1[0]
    podrob = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вузы по направлению🏫', callback_data=f'{aba}')],
    [InlineKeyboardButton(text='Бесплатные курсы📚', url = 'https://dopobr.petersburgedu.ru')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{napr}\n',reply_markup=podrob)

@router.callback_query(F.data=='Popbot')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute(f'SELECT Descript FROM directions WHERE code = "H2"')
    napr1 = cursor.fetchone()
    napr=napr1[0]
    cursor.execute(f'SELECT Vyzteg FROM directions WHERE code = "H2"')
    aba1 = cursor.fetchone()
    aba=aba1[0]
    podrob = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Вузы по направлению🏫', callback_data=f'{aba}')],
    [InlineKeyboardButton(text='Бесплатные курсы📚', url = 'https://dopobr.petersburgedu.ru')],
    [InlineKeyboardButton(text='Назад📌', callback_data='main')]
])
    await callback.answer('')
    await callback.message.edit_text(f'{napr}\n',reply_markup=podrob)

# endregion


# region TEST

@router.callback_query(F.data=='znayu')
async def tsh(callback: CallbackQuery):
    await callback.answer('Выбирите направление')
    await callback.message.edit_text('Подборка популярных направлений, выбирите группу',reply_markup=kb.Obzor1)




@router.callback_query(F.data=='STEST')
async def tsh(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Мини-тест на 15 вопросов, которые помогут определить возможно вам симпотизирующие направления!',reply_markup=kb.stest)






@router.callback_query(F.data=='starttest')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    tabl(user_id)
    await callback.answer('')
    await callback.message.edit_text('1 вопрос \n\nЧто вам интереснее всего?\na) Работать с техническими устройствами и системами\nb) Исследовать природу и растения\nc) Помогать людям справляться с психическими проблемами',reply_markup=kb.vop1)

#1


@router.callback_query(F.data=='1a')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Inz = Inz + 1, It = It + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('2 вопрос \n\nКакой подход вам наиболее близок?\na) Анализ данных и принятие решений на основе цифр\nb) Исследование химических процессов и составов\nc) Помощь людям в поиске их внутреннего мира',reply_markup=kb.vop2)

@router.callback_query(F.data=='1b')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Bot = Bot + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('2 вопрос \n\nКакой подход вам наиболее близок?\na) Анализ данных и принятие решений на основе цифр\nb) Исследование химических процессов и составов\nc) Помощь людям в поиске их внутреннего мира',reply_markup=kb.vop2)

@router.callback_query(F.data=='1c')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Psihoter  = Psihoter + 1, Psiholog = Psiholog + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('2 вопрос \n\nКакой подход вам наиболее близок?\na) Анализ данных и принятие решений на основе цифр\nb) Исследование химических процессов и составов\nc) Помощь людям в поиске их внутреннего мира',reply_markup=kb.vop2)




@router.callback_query(F.data=='2a')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Econ = Econ + 1, Fin = Fin + 1, Buh = Buh + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('3 вопрос \n\nЧто вам ближе?\na) Заниматься исследованиями в области экологии\nb) Разрабатывать и проектировать технологические системы\nc) Создавать и управлять маркетинговыми кампаниями',reply_markup=kb.vop3)

@router.callback_query(F.data=='2b')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Him = Him + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('3 вопрос \n\nЧто вам ближе?\na) Заниматься исследованиями в области экологии\nb) Разрабатывать и проектировать технологические системы\nc) Создавать и управлять маркетинговыми кампаниями',reply_markup=kb.vop3)

@router.callback_query(F.data=='2c')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Psihoter  = Psihoter + 1, Psiholog = Psiholog + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('3 вопрос \n\nЧто вам ближе?\na) Заниматься исследованиями в области экологии\nb) Разрабатывать и проектировать технологические системы\nc) Создавать и управлять маркетинговыми кампаниями',reply_markup=kb.vop3)



@router.callback_query(F.data=='3a')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Ecol = Ecol + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('4 вопрос \n\nКакую работу вы предпочли бы?\na) Составлять стратегии для компании\nb) Работать с медицинскими или психологическими проблемами\nc) Работать с цифрами и вести учет',reply_markup=kb.vop4)

@router.callback_query(F.data=='3b')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Inz = Inz + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('4 вопрос \n\nКакую работу вы предпочли бы?\na) Составлять стратегии для компании\nb) Работать с медицинскими или психологическими проблемами\nc) Работать с цифрами и вести учет',reply_markup=kb.vop4)

@router.callback_query(F.data=='3c')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Mark = Mark + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('4 вопрос \n\nКакую работу вы предпочли бы?\na) Составлять стратегии для компании\nb) Работать с медицинскими или психологическими проблемами\nc) Работать с цифрами и вести учет',reply_markup=kb.vop4)





@router.callback_query(F.data=='4a')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Mark = Mark + 1, Fin = Fin + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('5 вопрос \n\nЧто вам нравится больше?\na) Работать в сфере науки и проводить эксперименты\nb) Разрабатывать новые IT-программы и технологии\nc) Помогать людям решать их юридические проблемы',reply_markup=kb.vop5)

@router.callback_query(F.data=='4b')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET "All" = "All" + 1, Psiholog = Psiholog + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('5 вопрос \n\nЧто вам нравится больше?\na) Работать в сфере науки и проводить эксперименты\nb) Разрабатывать новые IT-программы и технологии\nc) Помогать людям решать их юридические проблемы',reply_markup=kb.vop5)

@router.callback_query(F.data=='4c')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Buh = Buh + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('5 вопрос \n\nЧто вам нравится больше?\na) Работать в сфере науки и проводить эксперименты\nb) Разрабатывать новые IT-программы и технологии\nc) Помогать людям решать их юридические проблемы',reply_markup=kb.vop5)






@router.callback_query(F.data=='5a')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Bot = Bot + 1, Him = Him + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('6 вопрос \n\nКакой тип задач вам более интересен?\na) Анализировать финансовые данные\nb) Проводить научные эксперименты\nc) Работать с людьми в консультативной роли',reply_markup=kb.vop6)

@router.callback_query(F.data=='5b')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET It = It + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('6 вопрос \n\nКакой тип задач вам более интересен?\na) Анализировать финансовые данные\nb) Проводить научные эксперименты\nc) Работать с людьми в консультативной роли',reply_markup=kb.vop6)

@router.callback_query(F.data=='5c')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Adv = Adv + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('6 вопрос \n\nКакой тип задач вам более интересен?\na) Анализировать финансовые данные\nb) Проводить научные эксперименты\nc) Работать с людьми в консультативной роли',reply_markup=kb.vop6)






@router.callback_query(F.data=='6a')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Fin = Fin + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('7 вопрос \n\nКак вы представляете свою работу?\na) Создание новых технологий и инновационных решений\nb) Помощь в решении юридических вопросов\nc) Работа с природой и растениями',reply_markup=kb.vop7)

@router.callback_query(F.data=='6b')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Him = Him + 1, Bot = Bot + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('7 вопрос \n\nКак вы представляете свою работу?\na) Создание новых технологий и инновационных решений\nb) Помощь в решении юридических вопросов\nc) Работа с природой и растениями',reply_markup=kb.vop7)

@router.callback_query(F.data=='6c')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Psihoter  = Psihoter + 1, Psiholog = Psiholog + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('7 вопрос \n\nКак вы представляете свою работу?\na) Создание новых технологий и инновационных решений\nb) Помощь в решении юридических вопросов\nc) Работа с природой и растениями',reply_markup=kb.vop7)






@router.callback_query(F.data=='7a')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Inz = Inz + 1, It = It + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('8 вопрос \n\nКакую из этих задач вы предпочли бы решать?\na) Прогнозировать экономические тенденции и финансовые потоки\nb) Оказывать поддержку людям с психическими расстройствами\nc) Работать с законодательством и правами людей',reply_markup=kb.vop8)

@router.callback_query(F.data=='7b')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Adv = Adv + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('8 вопрос \n\nКакую из этих задач вы предпочли бы решать?\na) Прогнозировать экономические тенденции и финансовые потоки\nb) Оказывать поддержку людям с психическими расстройствами\nc) Работать с законодательством и правами людей',reply_markup=kb.vop8)

@router.callback_query(F.data=='7c')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Bot = Bot + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('8 вопрос \n\nКакую из этих задач вы предпочли бы решать?\na) Прогнозировать экономические тенденции и финансовые потоки\nb) Оказывать поддержку людям с психическими расстройствами\nc) Работать с законодательством и правами людей',reply_markup=kb.vop8)





@router.callback_query(F.data=='8a')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Econ = Econ + 1, Fin = Fin + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('9 вопрос \n\nКакую роль в жизни вы хотите играть?\na) Научного исследователя\nb) Технического эксперта\nc) Продавца или маркетолога',reply_markup=kb.vop9)

@router.callback_query(F.data=='8b')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Psihoter  = Psihoter + 1, Psiholog = Psiholog + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('9 вопрос \n\nКакую роль в жизни вы хотите играть?\na) Научного исследователя\nb) Технического эксперта\nc) Продавца или маркетолога',reply_markup=kb.vop9)

@router.callback_query(F.data=='8c')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Adv = Adv + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('9 вопрос \n\nКакую роль в жизни вы хотите играть?\na) Научного исследователя\nb) Технического эксперта\nc) Продавца или маркетолога',reply_markup=kb.vop9)







@router.callback_query(F.data=='9a')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Him = Him + 1, Bot = Bot + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('10 вопрос \n\nКак вы видите свою работу в будущем?\na) Разрабатывать сложные проекты и системы\nb) Работать в финансовых институтах или банках\nc) Проводить консультации с клиентами',reply_markup=kb.vop10)

@router.callback_query(F.data=='9b')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Inz = Inz + 1, It = It + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('10 вопрос \n\nКак вы видите свою работу в будущем?\na) Разрабатывать сложные проекты и системы\nb) Работать в финансовых институтах или банках\nc) Проводить консультации с клиентами',reply_markup=kb.vop10)

@router.callback_query(F.data=='9c')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Mark = Mark + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('10 вопрос \n\nКак вы видите свою работу в будущем?\na) Разрабатывать сложные проекты и системы\nb) Работать в финансовых институтах или банках\nc) Проводить консультации с клиентами',reply_markup=kb.vop10)






@router.callback_query(F.data=='10a')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Inz = Inz + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('11 вопрос \n\nКакую проблему вам было бы интересно решать?\na) Управление проектами и бюджетами\nb) Создание маркетинговых стратегий\nc) Работа с растениями или химическими веществами',reply_markup=kb.vop11)

@router.callback_query(F.data=='10b')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Buh = Buh + 1, Fin = Fin + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('11 вопрос \n\nКакую проблему вам было бы интересно решать?\na) Управление проектами и бюджетами\nb) Создание маркетинговых стратегий\nc) Работа с растениями или химическими веществами',reply_markup=kb.vop11)

@router.callback_query(F.data=='10c')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Psihoter  = Psihoter + 1, Psiholog = Psiholog + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('11 вопрос \n\nКакую проблему вам было бы интересно решать?\na) Управление проектами и бюджетами\nb) Создание маркетинговых стратегий\nc) Работа с растениями или химическими веществами',reply_markup=kb.vop11)





@router.callback_query(F.data=='11a')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Econ = Econ + 1, Fin = Fin + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('12 вопрос \n\nЧто вам кажется наиболее увлекательным?\na) Оказывать психологическую помощь\nb) Исследовать растения или химические вещества\nc) Разрабатывать новые технологии',reply_markup=kb.vop12)

@router.callback_query(F.data=='11b')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Mark = Mark + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('12 вопрос \n\nЧто вам кажется наиболее увлекательным?\na) Оказывать психологическую помощь\nb) Исследовать растения или химические вещества\nc) Разрабатывать новые технологии',reply_markup=kb.vop12)

@router.callback_query(F.data=='11c')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Him = Him + 1, Bot = Bot + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('12 вопрос \n\nЧто вам кажется наиболее увлекательным?\na) Оказывать психологическую помощь\nb) Исследовать растения или химические вещества\nc) Разрабатывать новые технологии',reply_markup=kb.vop12)
 




@router.callback_query(F.data=='12a')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Psihoter  = Psihoter + 1, Psiholog = Psiholog + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('13 вопрос \n\nКакие задачи вас привлекают больше всего?\na) Психологические консультации и терапия\nb) Работа с экономикой и финансами\nc) Консультирование по правовым вопросам',reply_markup=kb.vop13)

@router.callback_query(F.data=='12b')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Him = Him + 1, Bot = Bot + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('13 вопрос \n\nКакие задачи вас привлекают больше всего?\na) Психологические консультации и терапия\nb) Работа с экономикой и финансами\nc) Консультирование по правовым вопросам',reply_markup=kb.vop13)

@router.callback_query(F.data=='12c')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET It = It + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('13 вопрос \n\nКакие задачи вас привлекают больше всего?\na) Психологические консультации и терапия\nb) Работа с экономикой и финансами\nc) Консультирование по правовым вопросам',reply_markup=kb.vop13)



@router.callback_query(F.data=='13a')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Psihoter  = Psihoter + 1, Psiholog = Psiholog + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('14 вопрос \n\nЧто вам нравится делать в свободное время?\na) Исследовать и разрабатывать новые технологии\nb) Разбираться в сложных финансовых ситуациях\nc) Участвовать в природоохранных проектах',reply_markup=kb.vop14)

@router.callback_query(F.data=='13b')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Fin = Fin + 1, Econ = Econ + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('14 вопрос \n\nЧто вам нравится делать в свободное время?\na) Исследовать и разрабатывать новые технологии\nb) Разбираться в сложных финансовых ситуациях\nc) Участвовать в природоохранных проектах',reply_markup=kb.vop14)

@router.callback_query(F.data=='13c')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Adv = Adv + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('14 вопрос \n\nЧто вам нравится делать в свободное время?\na) Исследовать и разрабатывать новые технологии\nb) Разбираться в сложных финансовых ситуациях\nc) Участвовать в природоохранных проектах',reply_markup=kb.vop14)





@router.callback_query(F.data=='14a')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Inz = Inz + 1, It = It + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('15 вопрос \n\nКакую работу вы бы предпочли в кризисной ситуации?\na) Помогать людям справиться с трудностями психического здоровья\nb) Работать с природой и экологией\nc) Рекомендовать правовые решения в нестандартных ситуациях',reply_markup=kb.vop15)

@router.callback_query(F.data=='14b')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Buh = Buh + 1, Fin = Fin + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('15 вопрос \n\nКакую работу вы бы предпочли в кризисной ситуации?\na) Помогать людям справиться с трудностями психического здоровья\nb) Работать с природой и экологией\nc) Рекомендовать правовые решения в нестандартных ситуациях',reply_markup=kb.vop15)

@router.callback_query(F.data=='14c')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Ecol = Ecol + 1 WHERE user_id = ?', (user_id,))
    conn.commit()
    await callback.answer('')
    await callback.message.edit_text('15 вопрос \n\nКакую работу вы бы предпочли в кризисной ситуации?\na) Помогать людям справиться с трудностями психического здоровья\nb) Работать с природой и экологией\nc) Рекомендовать правовые решения в нестандартных ситуациях',reply_markup=kb.vop15)



@router.callback_query(F.data=='15a')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Psihoter  = Psihoter + 1, Psiholog = Psiholog + 1 WHERE user_id = ?', (user_id,))
    
    conn.commit()
    re1, re2 = test2(user_id)
    Konectest = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f'Выбрать {re1}', callback_data='smain')],
        [InlineKeyboardButton(text=f'Выбрать {re2}', callback_data='s2main')],
        [InlineKeyboardButton(text='Вернутся обратно', callback_data='main')]
    ])
    await callback.answer('')
    await callback.message.edit_text(f'Вы завершили тест, ваш результат \n\nПредпологаем - {re1} и {re2}',reply_markup=Konectest)

@router.callback_query(F.data=='15b')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Ecol = Ecol + 1 WHERE user_id = ?', (user_id,))
    
    conn.commit()
    re1, re2 = test2(user_id)
    Konectest = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f'Выбрать {re1}', callback_data='smain')],
        [InlineKeyboardButton(text=f'Выбрать {re2}', callback_data='s2main')],
        [InlineKeyboardButton(text='Вернутся обратно', callback_data='main')]
    ])
    await callback.answer('')
    await callback.message.edit_text(f'Вы завершили тест, ваш результат \n\nПредпологаем - {re1} и {re2}',reply_markup=Konectest)

@router.callback_query(F.data=='15c')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute('UPDATE professions_test SET Adv = Adv + 1 WHERE user_id = ?', (user_id,))
    
    conn.commit()
    re1, re2 = test2(user_id)
    Konectest = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f'Выбрать {re1}', callback_data='smain')],
        [InlineKeyboardButton(text=f'Выбрать {re2}', callback_data='s2main')],
        [InlineKeyboardButton(text='Вернутся обратно', callback_data='main')]
    ])
    await callback.answer('')
    await callback.message.edit_text(f'Вы завершили тест, ваш результат \n\nПредпологаем - {re1} и {re2}',reply_markup=Konectest)

    
@router.callback_query(F.data=='smain')
async def tsh(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    mxpr, mxpr2 = test(user_id)
    cursor.execute("INSERT OR REPLACE INTO users (user_id, napravlenie) VALUES (? , ?)", (user_id, mxpr))
    conn.commit
    conn.close
    res1 = napslovo(user_id)
    await callback.message.edit_text(f"Ваше направление:\n{res1}\n\nНайди подходящие курсы в портале и реши куда поступать!", reply_markup=kb.mainmenuwith)
@router.callback_query(F.data=='s2main')
async def tsh(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    mxpr, mxpr2 = test(user_id)
    cursor.execute("INSERT OR REPLACE INTO users (user_id, napravlenie) VALUES (? , ?)", (user_id, mxpr2))
    conn.commit
    conn.close
    res1 = napslovo(user_id)
    await callback.message.edit_text(f"Ваше направление:\n{res1}\n\nНайди подходящие курсы в портале и реши куда поступать!", reply_markup=kb.mainmenuwith)






# endregion




# region OBZOR 1



######
@router.callback_query(F.data=='Fm')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute ('INSERT OR REPLACE INTO users (user_id, napravlenie) VALUES(?, ?)', (user_id,'nety'))
    conn.commit()
    await callback.answer('Физико-математические')
    await callback.message.edit_text('Подборка популярных направлений с физико-математическим уклоном',reply_markup=kb.FizMat)

@router.callback_query(F.data=='Hm')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute ('INSERT OR REPLACE INTO users (user_id, napravlenie) VALUES(?, ?)', (user_id,'nety'))
    conn.commit()
    await callback.answer('Хим-био')
    await callback.message.edit_text('Подборка популярных направлений с хим-био уклоном',reply_markup=kb.HimBio)

@router.callback_query(F.data=='Gm')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute ('INSERT OR REPLACE INTO users (user_id, napravlenie) VALUES(?, ?)', (user_id,'nety'))
    conn.commit()
    await callback.answer('Гуманитарные')
    await callback.message.edit_text('Подборка популярных направлений с гуманитарным уклоном',reply_markup=kb.Gym)

    
####
@router.callback_query(F.data=='Sinz')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute ('INSERT OR REPLACE INTO users (user_id, napravlenie) VALUES(?, ?)', (user_id,'F1'))
    conn.commit()
    await callback.answer('Инженер')
    await callback.message.edit_text('Вы выбрали направление Инженер - верно?',reply_markup=kb.Sinz)

@router.callback_query(F.data=='Sit')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute ('INSERT OR REPLACE INTO users (user_id, napravlenie) VALUES(?, ?)', (user_id,'F2'))
    conn.commit()
    await callback.answer('IT-специалист')
    await callback.message.edit_text('Вы выбрали направление IT-специалист - верно?',reply_markup=kb.Sinz)


@router.callback_query(F.data=='Sec')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute ('INSERT OR REPLACE INTO users (user_id, napravlenie) VALUES(?, ?)', (user_id,'F3'))
    conn.commit()
    await callback.answer('Экономист')
    await callback.message.edit_text('Вы выбрали направление Экономист - верно?',reply_markup=kb.Sinz)


@router.callback_query(F.data=='Sfin')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute ('INSERT OR REPLACE INTO users (user_id, napravlenie) VALUES(?, ?)', (user_id,'F4'))
    conn.commit()
    await callback.answer('Финансист')
    await callback.message.edit_text('Вы выбрали направление Финансист - верно?',reply_markup=kb.Sinz)


@router.callback_query(F.data=='Sbuh')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute ('INSERT OR REPLACE INTO users (user_id, napravlenie) VALUES(?, ?)', (user_id,'F5'))
    conn.commit()
    await callback.answer('Бухгалтер')
    await callback.message.edit_text('Вы выбрали направление Бухгалтер - верно?',reply_markup=kb.Sinz)




####
@router.callback_query(F.data=='Shim')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute ('INSERT OR REPLACE INTO users (user_id, napravlenie) VALUES(?, ?)', (user_id,'H1'))
    conn.commit()
    await callback.answer('Химик')
    await callback.message.edit_text('Вы выбрали направление Химик - верно?',reply_markup=kb.Sinz)

@router.callback_query(F.data=='Secol')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute ('INSERT OR REPLACE INTO users (user_id, napravlenie) VALUES(?, ?)', (user_id,'H2'))
    conn.commit()
    await callback.answer('Эколог')
    await callback.message.edit_text('Вы выбрали направление Эколог - верно?',reply_markup=kb.Sinz)


@router.callback_query(F.data=='Spsihoter')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute ('INSERT OR REPLACE INTO users (user_id, napravlenie) VALUES(?, ?)', (user_id,'H3'))
    conn.commit()
    await callback.answer('Психотерапевт')
    await callback.message.edit_text('Вы выбрали направление Психотерапевт - верно?',reply_markup=kb.Sinz)


@router.callback_query(F.data=='Sall')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute ('INSERT OR REPLACE INTO users (user_id, napravlenie) VALUES(?, ?)', (user_id,'H4'))
    conn.commit()
    await callback.answer('Аллерголог')
    await callback.message.edit_text('Вы выбрали направление Аллерголог - верно?',reply_markup=kb.Sinz)


@router.callback_query(F.data=='Sbot')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute ('INSERT OR REPLACE INTO users (user_id, napravlenie) VALUES(?, ?)', (user_id,'H5'))
    conn.commit()
    await callback.answer('Ботаник')
    await callback.message.edit_text('Вы выбрали направление Ботаник - верно?',reply_markup=kb.Sinz)





####
@router.callback_query(F.data=='Smark')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute ('INSERT OR REPLACE INTO users (user_id, napravlenie) VALUES(?, ?)', (user_id,'G1'))
    conn.commit()
    await callback.answer('Маркетолог')
    await callback.message.edit_text('Вы выбрали направление Маркетолог - верно?',reply_markup=kb.Sinz)

@router.callback_query(F.data=='Sadv')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute ('INSERT OR REPLACE INTO users (user_id, napravlenie) VALUES(?, ?)', (user_id,'G2'))
    conn.commit()
    await callback.answer('Адвокат')
    await callback.message.edit_text('Вы выбрали направление Адвокат - верно?',reply_markup=kb.Sinz)


@router.callback_query(F.data=='Szhur')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute ('INSERT OR REPLACE INTO users (user_id, napravlenie) VALUES(?, ?)', (user_id,'G3'))
    conn.commit()
    await callback.answer('Журналист')
    await callback.message.edit_text('Вы выбрали направление Журналист - верно?',reply_markup=kb.Sinz)


@router.callback_query(F.data=='Sprep')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute ('INSERT OR REPLACE INTO users (user_id, napravlenie) VALUES(?, ?)', (user_id,'G4'))
    conn.commit()
    await callback.answer('Преподаватель')
    await callback.message.edit_text('Вы выбрали направление Преподаватель - верно?',reply_markup=kb.Sinz)


@router.callback_query(F.data=='Spsihol')
async def tsh(callback: CallbackQuery):
    user_id = callback.from_user.id
    cursor.execute ('INSERT OR REPLACE INTO users (user_id, napravlenie) VALUES(?, ?)', (user_id,'G5'))
    conn.commit()
    await callback.answer('Психолог')
    await callback.message.edit_text('Вы выбрали направление Психолог - верно?',reply_markup=kb.Sinz)



# endregion








