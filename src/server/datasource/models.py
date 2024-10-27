from datetime import datetime
from typing import Optional
from sqlalchemy import Column, Integer, String, Boolean, Float, Table, DateTime, ForeignKey, func
from pydantic import BaseModel
from sqlalchemy.orm import relationship
from database import Base

# Association tables for many-to-many relationships
team_members = Table(
    'team_members',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('team_id', Integer, ForeignKey('teams.id'), primary_key=True)
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(50), unique=True, index=True)
    username = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(100))
    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    teams = relationship("Team", secondary=team_members, back_populates="members")
    messages = relationship("Message", back_populates="author")


class Team(Base):
    __tablename__ = "teams"


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    created_in = Column(DateTime(timezone=True), server_default=func.now())
    owner_id = Column(Integer, ForeignKey('users.id'))

    # Relationships
    members = relationship("User", secondary=team_members, back_populates="teams")
    channels = relationship("Channel", back_populates="team")


class Channel(Base):
    __tablename__ = "channels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    team_id = Column(Integer, ForeignKey('teams.id'))
    created_in = Column(DateTime(timezone=True), server_default=func.now())
    is_private = Column(Boolean, default=False)

    # Relationships
    team = relationship("Team", back_populates="channels")
    messages = relationship("Message", back_populates="channel")


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    channel_id = Column(Integer, ForeignKey('channels.id'))
    author_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    is_edited = Column(Boolean, default=False)

    # Relationships
    channel = relationship("Channel", back_populates="messages")
    author = relationship("User", back_populates="messages")


