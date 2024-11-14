from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.models import Base


class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True, autoincrement=True)
    latitude = Column(String, nullable=False)
    longitude = Column(String, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    email_id = Column(Integer, ForeignKey('email.id'), nullable=False)

    email = relationship("Email", back_populates="location")
