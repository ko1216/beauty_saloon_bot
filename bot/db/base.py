from datetime import date, timedelta, datetime

from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseModel:
    """
            Базовая модель в базе данных
        """
    __abstract__ = True
    creation_date = Column(DateTime, default=date.today())
    upd_date = Column(DateTime, onupdate=date.today())

    @property
    def no_upd_time(self) -> timedelta:
        """
        Получить время, которое модель не обновлялась
        :return: timedelta
        """
        return self.upd_date - datetime.now()  # type: ignore
