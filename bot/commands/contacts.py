from aiogram import types
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


async def conctact_menu(message: types.Message):

    menu = ReplyKeyboardBuilder()

    menu.row(
        KeyboardButton(text='Менделеевская'),
        KeyboardButton(text='Бауманская'),
        KeyboardButton(text='Мясницкая ул'),
        KeyboardButton(text='Назад в меню')
    )
    menu.adjust(1)

    await message.answer(text='Выберите подходящий вам салон и узнайте график работы и местоположение',
                         reply_markup=menu.as_markup())


async def mendeleevskaya_info(message: types.Message):
    await message.answer(text='ул. Новослободская, д. 45б, Москва\n\n'
                              'Общий номер для записи: +74954813242\n\n'
                              'График работы: ежедневно с 09:00 до 21:32')

    await message.answer_location(latitude=55.784592, longitude=37.595600)


async def baumanskaya_info(message: types.Message):
    await message.answer(text='ул. Бакунинская, д. 5, Москва\n\n'
                              'Общий номер для записи: +74954813242\n\n'
                              'График работы: ежедневно с 09:00 до 21:32')

    await message.answer_location(latitude=55.773707, longitude=37.679700)


async def myasnitskaya_info(message: types.Message):
    await message.answer(text='ул. Мясницкая, д. 15, Москва, 101000\n\n'
                              'Общий номер для записи: +74954813242\n\n'
                              'График работы: ежедневно с 09:00 до 21:32')

    await message.answer_location(latitude=55.763108, longitude=37.634874)
