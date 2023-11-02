import logging

from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.orm import sessionmaker

from .base import BaseModel, Base


class Feedback(Base, BaseModel):
    """
    Таблица для записи фидбэка пользователя
    """
    __tablename__ = 'feedbacks'

    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.user_id'))

    def __str__(self):
        return f'Отзыв "{self.text[:10]}..." от пользователя с id {self.user_id}'


async def create_feedback(user_id: int, feedback_text: str, session_maker: sessionmaker) -> Feedback | None:
    async with session_maker() as session:
        async with session.begin():
            feedback = Feedback(
                text=feedback_text,
                user_id=user_id
            )
            try:
                session.add(feedback)
            except ProgrammingError as e:
                logging.error(e)
                return None
            else:
                return feedback
