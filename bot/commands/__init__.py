__all__ = ['register_user_commands']

from aiogram import Router, F
from aiogram.filters import CommandStart, Command

from bot.commands.about_servises import get_post_about_services
from bot.commands.create_design import show_service_menu, on_button_clicked, ServiceCallbackData, on_options_clicked, \
    ManPedOptionsCallbackData, BrowsOptionsCallbackData
from bot.commands.feedback import feedback_menu, send_yandex_location, send_feedback_message, MessageForm, \
    reg_feedback_message
from bot.commands.promotions import get_info_about_promotions
from bot.commands.registration import registration, reg_fullname, reg_date_of_birth, RegForm, reg_phone_number
from bot.commands.service_commands import test_service_markup, on_service_button_clicked, TestServiceCallbackData, \
    TestManicureCallbackData, TestPedicureCallbackData, TestManPedCallbackData, \
    TestBrowsCallbackData, TestEpilationCallbackData, on_submenu_button_clicked
from bot.commands.help import help_command, help_func
from bot.commands.contacts import conctact_menu, mendeleevskaya_info, myasnitskaya_info, \
    baumanskaya_info
from bot.commands.start import start


def register_user_commands(router: Router) -> None:
    router.message.register(start, CommandStart())
    router.message.register(start, F.text == 'Назад в меню')
    router.message.register(help_command, Command(commands=['help']))
    router.message.register(help_func, F.text == 'Помощь')
    router.message.register(conctact_menu, F.text == 'Контакты')
    router.message.register(registration, F.text == 'Программа лояльности')
    router.message.register(get_post_about_services, F.text == 'Наши услуги')
    router.message.register(test_service_markup, F.text == 'Записаться')
    router.message.register(show_service_menu, F.text == 'Собрать Дизайн')
    router.message.register(get_info_about_promotions, F.text == 'Акции')
    router.message.register(feedback_menu, F.text == 'Оставить отзыв')
    router.message.register(send_yandex_location, F.text == 'Яндекс Карты')
    router.message.register(send_feedback_message, F.text == 'Сообщение администрации')
    router.message.register(mendeleevskaya_info, F.text == 'Менделеевская')
    router.message.register(baumanskaya_info, F.text == 'Бауманская')
    router.message.register(myasnitskaya_info, F.text == 'Мясницкая ул')

    router.callback_query.register(on_service_button_clicked, TestServiceCallbackData.filter())
    router.callback_query.register(on_submenu_button_clicked, TestManicureCallbackData.filter())
    router.callback_query.register(on_submenu_button_clicked, TestPedicureCallbackData.filter())
    router.callback_query.register(on_submenu_button_clicked, TestManPedCallbackData.filter())
    router.callback_query.register(on_submenu_button_clicked, TestBrowsCallbackData.filter())
    router.callback_query.register(on_submenu_button_clicked, TestEpilationCallbackData.filter())
    router.callback_query.register(on_button_clicked, ServiceCallbackData.filter())
    router.callback_query.register(on_options_clicked, ManPedOptionsCallbackData.filter())
    router.callback_query.register(on_options_clicked, BrowsOptionsCallbackData.filter())

    router.message.register(reg_fullname, RegForm.waiting_for_fullname)
    router.message.register(reg_date_of_birth, RegForm.waiting_for_date_of_birth)
    router.message.register(reg_phone_number, RegForm.waiting_for_phone_number)
    router.message.register(reg_feedback_message, MessageForm.waiting_for_feedback)
