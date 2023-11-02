from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from sqlalchemy.orm import sessionmaker

from bot.commands.start import start
from bot.commands.registration import CANCEL_BOARD
from bot.db.feedback import Feedback, create_feedback


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

    url = 'https://yandex.ru/maps/org/milky_club/162803279667/?display-text=Milky%20Club&filter=chain_id%3A14369906521&ll=37.600844%2C55.784751&mode=search&sctx=ZAAAAAgBEAAaKAoSCZ5eKcsQz0JAEdOgaB7A4EtAEhIJQnxgx38B9T8RXqJ6a2Cr4T8iBgABAgMEBSgAOABAzZIHSAFqAnJ1ggEUY2hhaW5faWQ6MTQzNjk5MDY1MjGdAc3MTD2gAQCoAQC9AQ6vLeLCAQazztO%2B3gTqAQDyAQD4AQCCAhRjaGFpbl9pZDoxNDM2OTkwNjUyMYoCAJICAJoCDGRlc2t0b3AtbWFwc6oCsgExNDM2OTkwNjUyMSwzNzcxMzU2MDQzMSwxMTYwNDA4ODI5OTMsNjAwMjY1NSw2MDg4MzE5NTYxOCwyMzA0MDgwODk4NDYsMzc2NjcyNjQ2NzMsMjQwOTUwMTQ0Nzc4LDIzMTU2ODU2OTI5NywzOTY1MjY1MzA2MCwyNjAzNDgzODg0LDM3NjY2MTcyNTEyLDM5NjgwMTE4NTgsMTUxNDg2NzcwMzgsMjE3NzgwNjEzMzU0sAIB&sll=37.600844%2C55.784751&sspn=0.052291%2C0.021976&text=%7B%22text%22%3A%22Milky%20Club%22%2C%22what%22%3A%5B%7B%22attr_name%22%3A%22chain_id%22%2C%22attr_values%22%3A%5B%2214369906521%22%5D%7D%5D%7D&z=14.65'
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
