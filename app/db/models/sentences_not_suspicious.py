from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.models import Base


class SentencesNotSuspicious(Base):
    __tablename__ = 'sentences_not_suspicious'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sentence = Column(String, nullable=False)
    email_id = Column(Integer, ForeignKey('email.id'), nullable=False)

    email = relationship("Email", back_populates="sentences_not_suspicious")
