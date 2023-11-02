from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def contacts_command(message: types.Message):
    contacts_markup = InlineKeyboardBuilder()
    contacts_markup.button(
        text='Менделеевская',
        url='https://yandex.ru/maps/org/milky_club/162803279667/?display-text=Milky%20Club&filter=chain_id%3A14369906521&ll=37.600844%2C55.784751&mode=search&sctx=ZAAAAAgBEAAaKAoSCZ5eKcsQz0JAEdOgaB7A4EtAEhIJQnxgx38B9T8RXqJ6a2Cr4T8iBgABAgMEBSgAOABAzZIHSAFqAnJ1ggEUY2hhaW5faWQ6MTQzNjk5MDY1MjGdAc3MTD2gAQCoAQC9AQ6vLeLCAQazztO%2B3gTqAQDyAQD4AQCCAhRjaGFpbl9pZDoxNDM2OTkwNjUyMYoCAJICAJoCDGRlc2t0b3AtbWFwc6oCsgExNDM2OTkwNjUyMSwzNzcxMzU2MDQzMSwxMTYwNDA4ODI5OTMsNjAwMjY1NSw2MDg4MzE5NTYxOCwyMzA0MDgwODk4NDYsMzc2NjcyNjQ2NzMsMjQwOTUwMTQ0Nzc4LDIzMTU2ODU2OTI5NywzOTY1MjY1MzA2MCwyNjAzNDgzODg0LDM3NjY2MTcyNTEyLDM5NjgwMTE4NTgsMTUxNDg2NzcwMzgsMjE3NzgwNjEzMzU0sAIB&sll=37.600844%2C55.784751&sspn=0.052291%2C0.021976&text=%7B%22text%22%3A%22Milky%20Club%22%2C%22what%22%3A%5B%7B%22attr_name%22%3A%22chain_id%22%2C%22attr_values%22%3A%5B%2214369906521%22%5D%7D%5D%7D&z=14.65'
    )
    contacts_markup.button(
        text='Бауманская',
        url='https://yandex.ru/maps/org/milky_club/218325616483/?display-text=Milky%20Club&filter=chain_id%3A14369906521&ll=37.595351%2C55.784976&mode=search&sctx=ZAAAAAgBEAAaKAoSCZ5eKcsQz0JAEdOgaB7A4EtAEhIJQnxgx38B9T8RXqJ6a2Cr4T8iBgABAgMEBSgAOABA3K0HSAFqAnJ1ggEUY2hhaW5faWQ6MTQzNjk5MDY1MjGdAc3MTD2gAQCoAQC9AQ6vLeLCAQazztO%2B3gTqAQDyAQD4AQCCAhRjaGFpbl9pZDoxNDM2OTkwNjUyMYoCAJICAJoCDGRlc2t0b3AtbWFwc6oCtQExNDM2OTkwNjUyMSwzNzcxMzU2MDQzMSwxMTYwNDA4ODI5OTMsMjQwOTUwMTQ0Nzc4LDIzMTU2ODU2OTI5NywzOTY1MjY1MzA2MCwyNjAzNDgzODg0LDM3NjY2MTcyNTEyLDM5NjgwMTE4NTgsMjE3NzgwNjEzMzU0LDgwNTU1MDkwMywxOTc2NzQ2NDExLDIzMjA4Mzc1NzYxOSwyMjQwMjY3NzI4MDEsMjA3ODc0MzkyNjkwsAIB&sll=37.629701%2C55.788757&sspn=0.153118%2C0.064344&text=%7B%22text%22%3A%22Milky%20Club%22%2C%22what%22%3A%5B%7B%22attr_name%22%3A%22chain_id%22%2C%22attr_values%22%3A%5B%2214369906521%22%5D%7D%5D%7D&z=11.64'
    )
    contacts_markup.button(
        text='Мясницкая ул., 15',
        url='https://yandex.ru/maps/org/milky/124480789757/?display-text=Milky%20Club&filter=chain_id%3A14369906521&ll=37.633731%2C55.763178&mode=search&sctx=ZAAAAAgBEAAaKAoSCZ5eKcsQz0JAEdOgaB7A4EtAEhIJQnxgx38B9T8RXqJ6a2Cr4T8iBgABAgMEBSgAOABAzJIHSAFqAnJ1ggEUY2hhaW5faWQ6MTQzNjk5MDY1MjGdAc3MTD2gAQCoAQC9AQ6vLeLCAQb9uYjdzwPqAQDyAQD4AQCCAhRjaGFpbl9pZDoxNDM2OTkwNjUyMYoCAJICAJoCDGRlc2t0b3AtbWFwc6oCtwExNDM2OTkwNjUyMSwyMTc3ODA2MTMzNTQsMTk3Njc0NjQxMSwyMDc4NzQzOTI2OTAsMTE2MDQwODgyOTkzLDYwODgzMTk1NjE4LDIzMjA4Mzc1NzYxOSwzNzY2NjE3MjUxMiwyNjAzNDgzODg0LDI0MDk1MDE0NDc3OCwzOTY4MDExODU4LDM3NzEzNTYwNDMxLDIyNDAyNjc3MjgwMSwyMzE0ODA1MDQ1ODgsMTUxNDg2NzcwMziwAgE%3D&sll=37.633731%2C55.763178&sspn=0.014306%2C0.006016&text=%7B%22text%22%3A%22Milky%20Club%22%2C%22what%22%3A%5B%7B%22attr_name%22%3A%22chain_id%22%2C%22attr_values%22%3A%5B%2214369906521%22%5D%7D%5D%7D&z=16.52'
    )

    await message.answer('Контакты', reply_markup=contacts_markup.as_markup())
