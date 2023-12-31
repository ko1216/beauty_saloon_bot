from typing import Callable, Dict, Any, Awaitable, Union

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from bot.db.users import is_user_exists, create_user


class RegisterCheck(BaseMiddleware):
    """
    Middleware будет вызываться каждый раз, когда пользователь будет отправлять боту сообщения (или нажимать
    на кнопку в инлайн-клавиатуре).
    """
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: Dict[str, Any]
    ) -> Any:

        session_maker = data['session_maker']
        user = event.from_user

        if not await is_user_exists(user_id=user.id, session_maker=session_maker):
            await create_user(user_id=user.id,
                              username=user.username, session_maker=session_maker)

        return await handler(event, data)
