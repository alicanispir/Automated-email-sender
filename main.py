import datetime as dt
import smtplib
import random
from pathlib import Path
from email.message import EmailMessage

# ---------- CONFIG ----------
MY_EMAIL = "YOUR_EMAIL_ADDRESS"
MY_PASSWORD = "YOUR_PASSWORD"
BOSS_EMAIL = "YOUR_BOSS_EMAIL"
START_DATE = dt.datetime(2025, 4, 12)
TEMPLATE_FOLDER = "raise_templates"

def is_reminder_day(start_date):
    today = dt.datetime.now()
    months_passed = (today.year - start_date.year) * 12 + today.month - start_date.month
    return months_passed % 3 == 0 and today.day == start_date.day

def get_raise_email():
    template_path = Path(TEMPLATE_FOLDER) / f"raise_{random.randint(1,3)}.txt"
    with open(template_path, "r") as file:
        content = file.read()
    return content

def send_email(to_email, subject, content):
    msg = EmailMessage()
    msg["From"] = MY_EMAIL
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(content)  # Automatically handles UTF-8

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.send_message(msg)

    print(f"📨 Reminder sent to {to_email}")

def main():
    if is_reminder_day(START_DATE):
        email_content = get_raise_email()
        send_email(BOSS_EMAIL, "Quarterly Check-in: Salary Adjustment Reminder", email_content)
    else:
        print("⏳ Not reminder day yet. Come back later!")

if __name__ == "__main__":
    main()
