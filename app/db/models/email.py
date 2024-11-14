from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.models import Base


class Email(Base):
    __tablename__ = 'email'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    username = Column(String, nullable=False)
    ip_address = Column(String, nullable=False)
    created_at = Column(String, default=datetime.utcnow)

    location = relationship("Location", back_populates="email", uselist=False)
    device_info = relationship("DeviceInfo", back_populates="email", uselist=False)
    sentences_hostage = relationship("SentencesHostage", back_populates="email")
    sentences_explos = relationship("SentencesExplos", back_populates="email")
    sentences_not_suspicious = relationship("SentencesNotSuspicious", back_populates="email")
