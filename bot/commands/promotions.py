from aiogram import types


async def get_info_about_promotions(message: types.Message):
    article = 'https://telegra.ph/Nashi-uslugi-11-01'
    await message.answer(article, parse_mode='HTML')
