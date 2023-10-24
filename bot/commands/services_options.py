from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.commands.callback_data import OptionsCallbackData


class OptionsMarkupView:
    """
    This class is a template to work with any screen of inline options.
    It could be upgrade for itself with new methods or with adding some Mixins.
    Also, you can use the super() method to reuse some functionality.
    """
    def __init__(self, options: list, items_per_row: int, previous_screen=None):
        self.options = options
        self.items_per_row = items_per_row
        self.previous_screen = previous_screen
        self.selected_options = []

    def options_markup(self, back_button: bool=False, confirm_button: bool=False) -> InlineKeyboardMarkup:
        """
        This is a constructor method that collects inline buttons depending on the number of options passed,
        the number of objects on the line, and also adds a button back to the previous template
        if the value True is passed
        :return: markup
        """
        buttons = []

        for option in self.options:
            callback_data = OptionsCallbackData(action=option.lower())
            button = InlineKeyboardButton(text=option, callback_data=callback_data.new())
            buttons.append(button)

        if back_button:
            callback_data = OptionsCallbackData(action='back')
            back_button = InlineKeyboardButton(text='Назад', callback_data=callback_data.new())
            buttons.append(back_button)

        if confirm_button:
            callback_data = OptionsCallbackData(action='confirm')
            confirm_button = InlineKeyboardButton(text='Подтвердить выбор', callback_data=callback_data.new())
            buttons.append(confirm_button)

        markup = InlineKeyboardMarkup(inline_keyboard=[buttons])
        markup.adjust(self.items_per_row)
        return markup

    async def send_options(self, text: str, message: types.Message) -> None:
        """
        This method sends the screen with chosen options and message with variable text.
        :param text: str - text of message which we want to send to user
        :param message: types.Message object
        """
        markup = self.options_markup()
        await message.answer(text, reply_markup=markup)

    async def option_callback(self, call: types.CallbackQuery, callback_data: OptionsCallbackData) -> None:
        """
        This method return to previous screen or show chosen options and save it
        """
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
            await call.message.edit_text(f'Вы подтвердили выбранные услуги:\n{options_text}')
