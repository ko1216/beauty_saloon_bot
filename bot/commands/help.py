from aiogram import types
from aiogram.filters import CommandObject


bot_commands = (
    ('start', 'Начало работы с ботом', 'Хорошая команда для начала работы с ботом',),
    ('help', 'Помощь и справка', 'Поможет, если это будет нужно',),
    ('settings', 'Настройки', 'Настрой свой настрой',),
)


async def help_command(message: types.Message, command: CommandObject):
    if command.args:
        for cmd in bot_commands:
            if cmd[0] == command.args:
                return await message.answer(
                    f'{cmd[0]} - {cmd[1]}\n\n{cmd[2]}'
                )
        else:
            return await message.answer('Команда не найдена')

    await help_func(message)


async def help_func(message: types.Message):
    return await message.answer(
        'Помощь и справка о боте\n'
        'Для того, чтобы получить информацию о командах используй /help <команда>\n'
    )
