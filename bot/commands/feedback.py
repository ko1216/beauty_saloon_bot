from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from sqlalchemy.orm import sessionmaker

from bot.commands.start import start
from bot.commands.registration import CANCEL_BOARD
from bot.db.feedback import create_feedback
from bot.services.bitly import get_short_link

yandex_url = 'https://yandex.ru/maps/213/moscow/chain/milky_club/14369906521/filter/chain_id/14369906521/?ll=37.637525%2C55.774105&sll=37.654865%2C55.762013&sspn=0.107714%2C0.084145&z=12.74'


class MessageForm(StatesGroup):
    waiting_for_feedback = State()


async def feedback_menu(message: types.Message):

    menu = ReplyKeyboardBuilder()

    menu.row(
        KeyboardButton(text='Яндекс Карты'),
        KeyboardButton(text='Сообщение администрации'),
        KeyboardButton(text='Назад в меню'),
    )
    menu.adjust(2)

    await message.answer('Вы можете оставить отзыв на картах Yandex, нажав на соответствующую кнопку.\n'
                         'Также вы можете написать напрямую руководству.',
                         reply_markup=menu.as_markup(resize_keyboard=True))


async def send_yandex_location(message: types.Message):

    url = await get_short_link(yandex_url)
    await message.answer(url, parse_mode='HTML')


async def send_feedback_message(message: types.Message, state: FSMContext):

    await state.set_state(MessageForm.waiting_for_feedback)
    await message.answer('Напишите здесь свой отзыв :)',
                         reply_markup=CANCEL_BOARD)


async def reg_feedback_message(message: types.Message, state: FSMContext, session_maker: sessionmaker):
    if message.text == 'Отмена':
        await state.clear()
        return await start(message)

    await state.update_data(feedback=message.text)
    data = await state.get_data()
    feedback = await create_feedback(
        user_id=message.from_user.id,
        feedback_text=data['feedback'],
        session_maker=session_maker
    )
    await state.clear()

    if feedback:
        await message.answer('Спасибо за ваш отзыв!:3')
    else:
        await message.answer('При отправке сообщения что-то пошло не так')
    return await start(message)
