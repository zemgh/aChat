from datetime import datetime

from sqlalchemy import String, Integer, ForeignKey, Index, Null
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import Base


class UserTopics(Base):
    __tablename__ = 'user_topics'

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), primary_key=True)
    topic_id: Mapped[int] = mapped_column(Integer, ForeignKey('topics.id'), primary_key=True)

    __table_args__ = [
        Index('index_user_id', 'user_id')
    ]


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    telegram_id: Mapped[int] = mapped_column(Integer, default=Null)

    name: Mapped[String] = mapped_column(String(50), nullable=False, unique=True)
    email: Mapped[String] = mapped_column(String(50), nullable=False, unique=True)
    password: Mapped[String] = mapped_column(String(100), nullable=False)

    is_active: Mapped[bool] = mapped_column(default=True)
    is_admin: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    topics = relationship('Topic', secondary=UserTopics.__table__, back_populates='topics')
    gender = relationship('Gender', uselist=False, back_populates='user')



class Topic(Base):
    __tablename__ = 'topics'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[String] = mapped_column(String(50), nullable=False, unique=True)
    is_active: Mapped[bool] = mapped_column(default=True)

    users = relationship('Topic', secondary=UserTopics.__table__, back_populates='users')


class Gender(Base):
    __tablename__ = 'genders'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[String] = mapped_column(String(50), nullable=False, unique=True)
    is_active: Mapped[bool] = mapped_column(default=True)

    user = relationship('User', back_populates='gender')
