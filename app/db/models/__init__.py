from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .device_info import DeviceInfo
from .email import Email
from .location import Location
from .sentences_explos import SentencesExplos
from .sentences_hostage import SentencesHostage
from .sentences_not_suspicious import SentencesNotSuspicious
