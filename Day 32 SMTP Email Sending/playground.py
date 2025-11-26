import datetime as dt
import random
import smtplib

email = 'example@gmail.com'
recipient = 'example+received@gmail.com'
app_password = 'password'

# 0: Monday, 1: Tuesday, 2: Wednesday, 3: Thursday, 4: Friday, 5: Saturday, and 6: Sunday.
weekday_check = dt.datetime.weekday(dt.datetime.today())
if weekday_check == 2:
    with open("quotes.txt", "r", encoding="utf-8") as file:
        quotes_list = [line.strip() for line in file]

    subject = "Wednesday Weekly Motivational Quote"
    message = random.choice(quotes_list).encode("utf-8")
    message_string = message.decode("utf-8")
    # print(message_string, type(message_string))

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=email, password=app_password)
        connection.sendmail(from_addr=email, to_addrs=recipient,
                            msg=f"Wednesday Weekly Motivational Quote\n\n{message_string}")
