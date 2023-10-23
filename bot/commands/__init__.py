__all__ = ['register_user_commands']

from aiogram import Router, F
from aiogram.filters import CommandStart, Command

from bot.commands.callback_data import ServicesCallbackData
from bot.commands.help import help_command, help_func
from bot.commands.contacts import contacts_command
from bot.commands.services import services_command, services_callback
from bot.commands.start import start


def register_user_commands(router: Router) -> None:
    router.message.register(start, CommandStart())
    router.message.register(help_command, Command(commands=['help']))
    router.message.register(help_func, F.text == 'Помощь')
    router.message.register(contacts_command, F.text == 'Контакты')
    router.message.register(services_command, F.text == 'Записаться')

    # router.callback_query.register(call_services_func, F.data == 'manicure')
    router.callback_query.register(services_callback, ServicesCallbackData.filter())
