import datetime

from sqlalchemy import Column, Integer, VARCHAR, DATE

from .base import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    #  Telegram user id
    user_id = Column(Integer, primary_key=True, unique=True, nullable=False)

    #  Telegram user name
    username = Column(VARCHAR(32), unique=False, nullable=True)

    #  Registration date
    reg_date = Column(DATE, default=datetime.date.today())

    #  Last update date
    upd_date = Column(DATE, onupdate=datetime.date.today())

    def __str__(self):
        return f'<User:{self.user_id}>'
