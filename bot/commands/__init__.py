__all__ = ['register_user_commands']

from aiogram import Router, F
from aiogram.filters import CommandStart, Command

from bot.commands.service_commands import test_service_markup, on_service_button_clicked, TestServiceCallbackData, \
    TestManicureCallbackData, TestPedicureCallbackData, TestManPedCallbackData, \
    TestBrowsCallbackData, TestEpilationCallbackData, on_submenu_button_clicked
from bot.commands.help import help_command, help_func
from bot.commands.contacts import contacts_command
from bot.commands.start import start


def register_user_commands(router: Router) -> None:
    router.message.register(start, CommandStart())
    router.message.register(help_command, Command(commands=['help']))
    router.message.register(help_func, F.text == 'Помощь')
    router.message.register(contacts_command, F.text == 'Контакты')

    router.message.register(test_service_markup, F.text == 'Записаться')
    router.callback_query.register(on_service_button_clicked, TestServiceCallbackData.filter())
    router.callback_query.register(on_submenu_button_clicked, TestManicureCallbackData.filter())
    router.callback_query.register(on_submenu_button_clicked, TestPedicureCallbackData.filter())
    router.callback_query.register(on_submenu_button_clicked, TestManPedCallbackData.filter())
    router.callback_query.register(on_submenu_button_clicked, TestBrowsCallbackData.filter())
    router.callback_query.register(on_submenu_button_clicked, TestEpilationCallbackData.filter())
