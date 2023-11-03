from datetime import datetime

from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from sqlalchemy.orm import sessionmaker

from bot.commands.start import start
from bot.db.users import update_user


class RegForm(StatesGroup):
    waiting_for_fullname = State()
    waiting_for_date_of_birth = State()
    waiting_for_phone_number = State()


CANCEL_BOARD = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Отмена'), ],
    ],
    resize_keyboard=True
)

BOARD_WITH_REQUEST_NUMBER = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Поделиться номером', request_contact=True), ],
        [KeyboardButton(text='Отмена'), ],
    ],
    resize_keyboard=True
)


async def registration(message: types.Message, state: FSMContext):

    await state.set_state(RegForm.waiting_for_fullname)
    await message.answer('Введите ваши имя и фамилию\nПример: Иван Иванов',
                         reply_markup=CANCEL_BOARD)


async def reg_fullname(message: types.Message, state: FSMContext):

    if message.text == 'Отмена':
        await state.clear()
        return await start(message)

    await state.update_data(fullname=message.text)
    await state.set_state(RegForm.waiting_for_date_of_birth)
    await message.answer('Отлично!\nТеперь введите дату рождения в формате "дд.мм.гггг"',
                         reply_markup=CANCEL_BOARD)


async def reg_date_of_birth(message: types.Message, state: FSMContext):

    if message.text == 'Отмена':
        await state.clear()
        return await start(message)

    try:
        date_of_birth = datetime.strptime(message.text, '%d.%m.%Y')

        current_time = datetime.now()
        min_year = 1950

        if date_of_birth > current_time:
            await message.answer('Дата рождения не может быть в будущем')
        elif date_of_birth.year < min_year:
            await message.answer('Пожалуйста, укажите дату рождения после 1950 года')
        else:
            await state.update_data(date_of_birth=date_of_birth)
            await state.set_state(RegForm.waiting_for_phone_number)
            await message.answer('Отлично!\nТеперь отправьте свой номер телефона',
                                 reply_markup=BOARD_WITH_REQUEST_NUMBER)
    except ValueError:
        await message.answer('Отправьте корректную дату рождения в формате "дд.мм.гггг"')


async def reg_phone_number(message: types.Message, state: FSMContext, session_maker: sessionmaker):

    if message.text and message.text != 'Отмена':
        await message.answer('Просто нажмите на кнопку поделиться')
    if message.text == 'Отмена':
        await state.clear()
        return await start(message)

    if message.contact:
        if message.contact.user_id == message.from_user.id:
            await state.update_data(phone_number=message.contact.phone_number)

            data = await state.get_data()
            user = await update_user(
                user_id=message.from_user.id,
                fullname=data['fullname'],
                date_of_birth=data['date_of_birth'],
                mobile_number=data['phone_number'],
                session_maker=session_maker
            )
            await state.clear()
            if user:
                await message.answer('Вы успешно прошли регистрацию!')
            else:
                await message.answer('Случилось что-то странное\nВозможно вы уже зарегистрированы?')

            return await start(message)
