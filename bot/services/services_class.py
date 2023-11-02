#  This code was useless for this app and need a serious upgrade
#  I wrote this while iam learning the aiogram library, and wanted to create some template logic to many branch of logic
#  So I will try to create some templateview logic like in Django at next projects

"""
from aiogram import types
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class OptionsCallbackData(CallbackData):
    def __init__(self, action):
        super().__init__(prefix='services')
        self.action = action


class OptionsMarkupView:

    #  This class is a template to work with any screen of inline options
    #  It could be upgrade for itself with new methods or with adding some Mixins.
    #  Also, you can use the super() method to reuse some functionality.


    def __init__(self, options: list, items_per_row: int, actions, title: str = None, text: str = None,
                 previous_screen=None):
        self.options = options
        self.items_per_row = items_per_row
        self.previous_screen = previous_screen
        if title:
            self.title = title.lower()
        self.selected_options = []
        self.text = text
        self.actions = actions

    def __repr__(self):
        return {self.title: self.text}

    def options_markup(self, back_button: bool = False, confirm_button: bool = False) -> InlineKeyboardBuilder:

# This is a constructor method that collects inline buttons depending on the number of options passed,
        # the number of objects on the line, and also adds a button back to the previous template
        # if the value True is passed
        # :return: markup

        markup = InlineKeyboardBuilder()

        for option in self.options:
            for service in self.actions:
                service_value = service.value
                if option.lower() == service_value:
                    markup.button(text=option, callback_data=OptionsCallbackData(action=service))

        if back_button:
            # callback_data = OptionsCallbackData(action='back')
            markup.button(text='Назад', callback_data=OptionsCallbackData(action='back').pack())

        if confirm_button:
            # callback_data = OptionsCallbackData(action='confirm')
            markup.button(text='Подтвердить выбор', callback_data=OptionsCallbackData(action='confirm').pack())

        markup.adjust(self.items_per_row)
        return markup

    async def send_options(self, text: str, message: types.Message) -> None:

        # This method sends the screen with chosen options and message with variable text.
        # :param text: str - text of message which we want to send to user
        # :param message: types.Message object

        markup = self.options_markup()
        await message.answer(text, reply_markup=markup.as_markup())

    async def option_callback(self, call: types.CallbackQuery, callback_data: OptionsCallbackData) -> None:

        # This method return to previous screen or show chosen options and save it

        if callback_data.action == 'back' and self.previous_screen:
            # Go to the previous user's screen
            await self.previous_screen.send_options('Выберите опцию:', call.message)
        elif callback_data.action == 'confirm' and not self.selected_options:
            await call.message.answer('Вы не выбрали ни одной опции.')
        elif callback_data.action != 'confirm':
            option = callback_data.action
            self.selected_options.append(option)
            options_text = '\n'.join([f'Вы выбрали {option}' for option in self.selected_options])
            await call.message.edit_text(options_text)
        else:
            options_text = "\n".join([option for option in self.selected_options])
            # Here we can add some functionality to send our selected data to Database
            # And then here we can use self.selected_options.clear()
            # Also here we can change attr confirm_button to False and send_options again
            await call.message.edit_text(f'Вы подтвердили выбранные услуги:\n{options_text}')

    @staticmethod
    async def pure_callback(call: types.CallbackQuery, callback_data: OptionsCallbackData, new_screens: list, texts: dict):

        # This method handles callback data to transition to the next screen without collecting options.

        for obj in new_screens:
            if callback_data.action.lower() == obj.title:
                for key, text in texts.items():
                    if key == obj.title:
                        await obj.send_options(text, call.message)
"""
