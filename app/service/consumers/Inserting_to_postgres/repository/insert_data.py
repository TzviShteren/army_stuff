from app.db.models import Email, Location, DeviceInfo, SentencesHostage, SentencesExplos, SentencesNotSuspicious
from app.db.postgre_darabase import session_maker


def insert_data(data):
    with session_maker() as session:
        try:
            # Insert Email
            email_entry = Email(
                email=data['email'],
                username=data['username'],
                ip_address=data['ip_address'],
                created_at=data['created_at']
            )
            session.add(email_entry)
            session.commit()
            session.refresh(email_entry)

            location_data = data.get('location')
            if location_data:
                location_entry = Location(
                    latitude=location_data['latitude'],
                    longitude=location_data['longitude'],
                    city=location_data['city'],
                    country=location_data['country'],
                    email_id=email_entry.id
                )
                session.add(location_entry)

            device_info_data = data.get('device_info')
            if device_info_data:
                device_info_entry = DeviceInfo(
                    browser=device_info_data['browser'],
                    os=device_info_data['os'],
                    device_id=device_info_data['device_id'],
                    email_id=email_entry.id
                )
                session.add(device_info_entry)

            sentences = data.get('sentences', [])
            for sentence in sentences:
                if sentence in "hostage":
                    sentence_entry = SentencesHostage(
                        sentence=sentence,
                        email_id=email_entry.id
                    )
                    session.add(sentence_entry)
                elif sentence in "explosive":
                    sentence_entry = SentencesExplos(
                        sentence=sentence,
                        email_id=email_entry.id
                    )
                    session.add(sentence_entry)
                else:
                    sentence_entry = SentencesNotSuspicious(
                        sentence=sentence,
                        email_id=email_entry.id
                    )
                    session.add(sentence_entry)

            session.commit()
            print("Data inserted successfully!")

        except Exception as e:
            session.rollback()
            print(f"Error inserting data: {e}")

        finally:
            session.close()