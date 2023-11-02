from enum import Enum

from aiogram import types
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder


class ServiceAction(str, Enum):
    manicure = 'маникюр'
    pedicure = 'педикюр'
    brows = 'брови'


class ServiceCallbackData(CallbackData, prefix='0'):
    action: ServiceAction


class ManPedOptions(str, Enum):
    cat_eye = 'Кошачий глаз'
    top_with_effects = 'Топ с эффектами(на все ногти)'
    reflective_coating = 'Светоотражающее покрытие'
    piercing = 'Пирсинг'
    french = 'Френч'
    sliders = 'Слайдеры'
    foil = 'Фольга'
    painting = 'Арт дизайн/Роспись'
    confirm = 'подтвердить'
    cancel = 'отмена'


class ManPedOptionsCallbackData(CallbackData, prefix='1'):
    action: ManPedOptions


class BrowsOptions(str, Enum):
    eyebrow_modeling = 'моделирование бровей'
    eyebrow_tinting = 'окрашивание бровей'
    eyelash_tinting = 'окрашивание ресниц'
    eyebrow_lamination = 'ламинирование бровей'
    confirm = 'подтвердить'
    cancel = 'отмена'


class BrowsOptionsCallbackData(CallbackData, prefix='2'):
    action: BrowsOptions


async def show_service_menu(message: types.Message):
    markup = InlineKeyboardBuilder()

    for action in ServiceAction:
        markup.button(text=action.value.title(),
                      callback_data=ServiceCallbackData(action=action).pack())

    markup.adjust(2)
    await message.answer('Выберите одну из услуг и настройте свой дизайн :)',
                         reply_markup=markup.as_markup())


def get_options_menu(action: ServiceAction):
    markup = InlineKeyboardBuilder()

    if action == ServiceAction.manicure:
        for option in ManPedOptions:
            if option.value != 'подтвердить' and option.value != 'отмена':
                markup.button(text=option.value.capitalize(),
                              callback_data=ManPedOptionsCallbackData(action=option).pack())
                markup.adjust(2)
            else:
                markup.row(InlineKeyboardButton(text=option.value.capitalize(),
                                                callback_data=ManPedOptionsCallbackData(action=option).pack()))

    elif action == ServiceAction.pedicure:
        for option in ManPedOptions:
            if option.value != 'подтвердить' and option.value != 'отмена':
                markup.button(text=option.value.capitalize(),
                              callback_data=ManPedOptionsCallbackData(action=option).pack())
                markup.adjust(2)
            else:
                markup.row(InlineKeyboardButton(text=option.value.capitalize(),
                                                callback_data=ManPedOptionsCallbackData(action=option).pack()))

    elif action == ServiceAction.brows:
        for option in BrowsOptions:
            if option.value != 'подтвердить' and option.value != 'отмена':
                markup.button(text=option.value.capitalize(),
                              callback_data=BrowsOptionsCallbackData(action=option).pack())
                markup.adjust(2)
            else:
                markup.row(InlineKeyboardButton(text=option.value.capitalize(),
                                                callback_data=BrowsOptionsCallbackData(action=option).pack()))

    return markup


async def on_button_clicked(call: CallbackQuery, callback_data: ServiceCallbackData, state: FSMContext):

    action = callback_data.action
    markup = get_options_menu(action)
    await state.update_data(current_markup=markup)
    await call.message.edit_text(text=f'Вы находитесь в разделе {action.value.title()}'
                                      f'\nВыберите одну или более опций дизайна',
                                 reply_markup=markup.as_markup())
    await call.answer()


async def on_options_clicked(call: CallbackQuery, callback_data: ServiceCallbackData, state: FSMContext):
    action = callback_data.action
    current_state = await state.get_data()

    if 'selected_options' not in current_state:
        current_state['selected_options'] = []

    if action.value.lower() == 'подтвердить' and action.value.lower() != 'отмена':
        if current_state['selected_options']:
            #  Здесь же до очистки состояния мы можем передавать данные в БД
            await call.message.edit_text(text=f'Вы подтвердили: {", ".join(current_state["selected_options"])}')
            await state.clear()
        else:
            await call.message.edit_text(
                text='Вы не выбрали ни одну из услуг\nВернитесь в прошлое меню и попробуйте еще раз')

    elif action.value.lower() == 'отмена':
        await call.message.edit_text(text='Действие отменено')
        await state.clear()
        return

    else:
        current_state['selected_options'].append(action.value)
        await state.update_data(selected_options=current_state['selected_options'])

        if 'current_markup' in current_state:
            current_markup = current_state['current_markup']
            await call.message.edit_text(
                text=f'Ваш выбор: {", ".join(current_state["selected_options"])}\nХотите подтвердить?',
                reply_markup=current_markup.as_markup())

    await call.answer()
