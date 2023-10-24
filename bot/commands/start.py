from aiogram import types
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import (
    ReplyKeyboardBuilder, ReplyKeyboardMarkup, InlineKeyboardBuilder,
    InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButtonPollType
)


async def start(message: types.Message) -> None:
    # await message.answer('Привет!\nБот запущен') - вариант запуска через команду

    menu_builder = ReplyKeyboardBuilder()
    # menu_builder.button(
    #     text='Помощь',
    # )
    # menu_builder.add(
    #     KeyboardButton(text='Отправить контакт', request_contact=True),
    # )
    # menu_builder.row(
    #     KeyboardButton(text='Отправить голосование', request_poll=KeyboardButtonPollType())
    # )

    menu_builder.row(
        KeyboardButton(text='Записаться'),
        KeyboardButton(text='Программа лояльности'),
        KeyboardButton(text='Наши услуги'),
        KeyboardButton(text='Собрать Дизайн'),
        KeyboardButton(text='Прайс лист'),
        KeyboardButton(text='Акции'),
        KeyboardButton(text='Оставить отзыв'),
        KeyboardButton(text='Контакты'),
    )
    menu_builder.adjust(2)

    await message.answer(
        'Меню',
        reply_markup=menu_builder.as_markup(resize_keyboard=True)
    )
