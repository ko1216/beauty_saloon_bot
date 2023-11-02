from enum import Enum

from aiogram import types
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class TestServiceAction(str, Enum):
    manicure = 'маникюр'
    pedicure = 'педикюр'
    man_ped = 'манпед'
    brows = 'брови'
    epilation = 'лазерная эпиляция'


class TestServiceCallbackData(CallbackData, prefix='test'):
    action: TestServiceAction


class TestManicureAction(str, Enum):
    removal = 'снятие'
    manicure_without_coating = 'маникюр без покрытия'
    manicure_and_coating = 'маникюр и покрытие'
    nail_extensions = 'наращивание ногтей'
    confirm = 'подтвердить'
    cancel = 'отмена'


class TestManicureCallbackData(CallbackData, prefix='manicure'):
    action: TestManicureAction


class TestPedicureAction(str, Enum):
    removal = 'снятие'
    pedicure_without_coating = 'педикюр без покрытия'
    pedicure_and_coating = 'педикюр и покрытие'
    confirm = 'подтвердить'
    cancel = 'отмена'


class TestPedicureCallbackData(CallbackData, prefix='pedicure'):
    action: TestPedicureAction


class TestManPedAction(str, Enum):
    manicure_removal = 'снятие маникюра'
    manicure_without_coating = 'маникюр без покрытия'
    manicure_and_coating = 'маникюр и покрытие'
    nail_extensions = 'наращивание ногтей'
    pedicure_removal = 'снятие педикюра'
    pedicure_without_coating = 'педикюр без покрытия'
    pedicure_and_coating = 'педикюр и покрытие'
    confirm = 'подтвердить'
    cancel = 'отмена'


class TestManPedCallbackData(CallbackData, prefix='manped'):
    action: TestManPedAction


class TestBrowsAction(str, Enum):
    eyebrow_modeling = 'моделирование бровей'
    eyebrow_tinting = 'окрашивание бровей'
    eyelash_tinting = 'окрашивание ресниц'
    eyebrow_lamination = 'ламинирование бровей'
    confirm = 'подтвердить'
    cancel = 'отмена'


class TestBrowsCallbackData(CallbackData, prefix='brows'):
    action: TestBrowsAction


class TestEpilationAction(str, Enum):
    armpits = 'подмышки'
    full_arms = 'руки полностью'
    full_legs = 'ноги полностью'
    deep_bikini = 'глубокое бикини'
    combo = 'комбо'
    confirm = 'подтвердить'
    cancel = 'отмена'


class TestEpilationCallbackData(CallbackData, prefix='epilation'):
    action: TestEpilationAction


async def test_service_markup(message: types.Message, state: FSMContext):
    await state.clear()

    markup = InlineKeyboardBuilder()

    for action in TestServiceAction:
        markup.button(text=action.value.title(),
                      callback_data=TestServiceCallbackData(action=action).pack())

    markup.adjust(2)
    await message.answer('Выберите одну из услуг и настройте свои опции :)', reply_markup=markup.as_markup())


def get_submenu_for_action(action: TestServiceAction):
    markup = InlineKeyboardBuilder()

    if action == TestServiceAction.manicure:
        for option in TestManicureAction:
            if option.value != 'подтвердить' and option.value != 'отмена':
                markup.button(text=option.value.capitalize(),
                              callback_data=TestManicureCallbackData(action=option).pack())
                markup.adjust(2)
            else:
                markup.row(InlineKeyboardButton(text=option.value.capitalize(),
                                                callback_data=TestManicureCallbackData(action=option).pack()))

    elif action == TestServiceAction.pedicure:
        for option in TestPedicureAction:
            if option.value != 'подтвердить' and option.value != 'отмена':
                markup.button(text=option.value.capitalize(),
                              callback_data=TestPedicureCallbackData(action=option).pack())
                markup.adjust(2)
            else:
                markup.row(InlineKeyboardButton(text=option.value.capitalize(),
                                                callback_data=TestPedicureCallbackData(action=option).pack()))

    elif action == TestServiceAction.man_ped:
        for option in TestManPedAction:
            if option.value != 'подтвердить' and option.value != 'отмена':
                markup.button(text=option.value.capitalize(),
                              callback_data=TestManPedCallbackData(action=option).pack())
                markup.adjust(2)
            else:
                markup.row(InlineKeyboardButton(text=option.value.capitalize(),
                                                callback_data=TestManPedCallbackData(action=option).pack()))

    elif action == TestServiceAction.brows:
        for option in TestBrowsAction:
            if option.value != 'подтвердить' and option.value != 'отмена':
                markup.button(text=option.value.capitalize(),
                              callback_data=TestBrowsCallbackData(action=option).pack())
                markup.adjust(2)
            else:
                markup.row(InlineKeyboardButton(text=option.value.capitalize(),
                                                callback_data=TestBrowsCallbackData(action=option).pack()))

    elif action == TestServiceAction.epilation:
        for option in TestEpilationAction:
            if option.value != 'подтвердить' and option.value != 'отмена':
                markup.button(text=option.value.capitalize(),
                              callback_data=TestEpilationCallbackData(action=option).pack())
                markup.adjust(2)
            else:
                markup.row(InlineKeyboardButton(text=option.value.capitalize(),
                                                callback_data=TestEpilationCallbackData(action=option).pack()))

    return markup


async def on_service_button_clicked(call: CallbackQuery, callback_data: TestServiceCallbackData, state: FSMContext):
    action = callback_data.action
    markup = get_submenu_for_action(action)
    await state.update_data(current_markup=markup)
    await call.message.edit_text(text=f'Вы находитесь в разделе {action.value.title()}\nВыберите одну или более опций',
                                 reply_markup=markup.as_markup())
    await call.answer()


async def on_submenu_button_clicked(call: CallbackQuery, callback_data: TestManicureCallbackData, state: FSMContext):

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
