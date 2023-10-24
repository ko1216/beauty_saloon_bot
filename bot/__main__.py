from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
import asyncio
import logging
import os
from dotenv import load_dotenv
from sqlalchemy import URL

from bot.commands.help import bot_commands
from commands import register_user_commands

from db import BaseModel, create_async_engine, get_session_maker, proceed_schemas

load_dotenv()
token: str = os.getenv('BOT_TOKEN')
db_username: str = os.getenv('DB_USERNAME')
db_pass: str = os.getenv('DB_PASS')
db_name: str = os.getenv('DB_NAME')


async def main() -> None:
    #  Включаем логирование для отслеживания работы бота
    logging.basicConfig(level=logging.DEBUG)

    #  Заполняем список комманд теми, что записали в пакете commands
    commands_for_bot = []
    for cmd in bot_commands:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))

    dp = Dispatcher()
    bot = Bot(token=token)

    #  регистрируем комманды для меню подсказок в боте
    await bot.set_my_commands(commands=commands_for_bot)

    register_user_commands(dp)

    postgres_url = URL.create(
        "postgresql+asyncpg",
        username=db_username,
        password=db_pass,
        host="localhost",
        database=db_name,
    )

    async_engine = create_async_engine(postgres_url)
    session_maker = get_session_maker(async_engine)
    await proceed_schemas(async_engine, BaseModel.metadata)

    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
