import pandas as pd
from pandas import DataFrame
from app.db.models.email import Email
from app.db.postgre_darabase import session_maker
import logging


def the_full_content_of_an_object_by_email(email_to_get):
    with session_maker() as session:
        email_info = session.query(Email).filter(Email.email == email_to_get).first()
        if not email_info:
            return None

        result = {
            "email": email_info.email,
            "username": email_info.username,
            "ip_address": email_info.ip_address,
            "created_at": email_info.created_at,
        }

        if email_info.location:
            result["location"] = {
                "latitude": email_info.location.latitude,
                "longitude": email_info.location.longitude,
                "city": email_info.location.city,
                "country": email_info.location.country
            }

        if email_info.device_info:
            result["device_info"] = {
                "browser": email_info.device_info.browser,
                "os": email_info.device_info.os,
                "device_id": email_info.device_info.device_id
            }

        result["sentences_hostage"] = [sentence.sentence for sentence in email_info.sentences_hostage]
        result["sentences_explos"] = [sentence.sentence for sentence in email_info.sentences_explos]
        result["sentences_not_suspicious"] = [sentence.sentence for sentence in email_info.sentences_not_suspicious]

        return result
