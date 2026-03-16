import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

# This class is responsible for sending notifications with the deal flight details.
class NotificationManager:
    def __init__(self):
        self.email = os.getenv('TESTING_EMAIL')
        self.APP_PASSWORD = os.getenv('APP_PASSWORD')

    def send_email(self, message_body):
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.APP_PASSWORD)
            email_message = f"Subject:New Low Flight Price Found!\n\n{message_body}"

            connection.sendmail(
                from_addr=self.email,
                to_addrs=self.email,
                msg=email_message.encode('utf-8')
            )
