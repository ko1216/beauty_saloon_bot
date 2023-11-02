from aiogram import types
from aiogram.types import KeyboardButton, WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder


async def start(message: types.Message) -> None:

    menu_builder = ReplyKeyboardBuilder()

    menu_builder.row(
        KeyboardButton(text='Записаться'),
        KeyboardButton(text='Программа лояльности'),
        KeyboardButton(text='Наши услуги'),
        KeyboardButton(text='Собрать Дизайн'),
        KeyboardButton(text='Прайс лист', web_app=WebAppInfo(url='https://milky-club.ru/prices/')),
        KeyboardButton(text='Акции'),
        KeyboardButton(text='Оставить отзыв'),
        KeyboardButton(text='Контакты'),
    )
    menu_builder.adjust(2)

    await message.answer(
        'Меню',
        reply_markup=menu_builder.as_markup(resize_keyboard=True)
    )
