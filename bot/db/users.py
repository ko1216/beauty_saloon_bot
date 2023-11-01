from sqlalchemy import Column, Integer, VARCHAR, DATE, select
from sqlalchemy.exc import ProgrammingError
from sqlalchemy.orm import sessionmaker

from .base import Base, BaseModel


class User(BaseModel):
    """
            Таблица пользователя в БД
        """
    __tablename__ = 'users'

    #  Telegram user id
    user_id = Column(Integer, primary_key=True, unique=True, nullable=False)

    #  Telegram user name
    username = Column(VARCHAR(32), unique=False, nullable=True)

    fullname = Column(VARCHAR(40), nullable=True)
    date_of_birth = Column(DATE, nullable=True)
    mobile_number = Column(VARCHAR(16), nullable=True)

    def __str__(self):
        return f'<User:{self.user_id}>'


async def get_user(user_id: int, session_maker: sessionmaker) -> User:

    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(
                select(User).filter(User.user_id == user_id)  # type: ignore
            )
            return result.scalars().one()


async def create_user(user_id: int, username: str, session_maker: sessionmaker) -> None:

    async with session_maker() as session:
        async with session.begin():
            user = User(
                user_id=user_id,
                username=username
            )
            try:
                session.add(user)
                await session.commit()
            except ProgrammingError:
                #  TODO: add log
                # для логирования можно добавить табличку логов в этой БД или БД для логирования
                pass


async def update_user(user_id: int, fullname: str, date_of_birth: str, mobile_number: str, session_maker: sessionmaker) -> bool:
    """
    This func needs to update the users data, if he wants to register
    """
    async with session_maker() as session:
        async with session.begin():
            user = await session.get(User, user_id)

            if user and user.fullname is None:
                user.fullname = fullname
                user.date_of_birth = date_of_birth
                user.mobile_number = mobile_number
                return True
            else:
                return False


async def is_user_exists(user_id: int, session_maker: sessionmaker) -> bool:

    async with session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User).where(User.user_id == user_id))
            return bool(result.scalar())
