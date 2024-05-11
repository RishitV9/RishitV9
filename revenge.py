import smtplib
import ssl
from email.message import EmailMessage

# Define email sender and receiver
email_sender = 'getscammed123failure@gmail.com'
email_password = "bkxx pian jiwr fpan"

victims = ['dan.zhao.us@gmail.com']

# Set the subject and body of the email
subject = 'YOU IDIOTS 0'
body = """
Your data has been leaked you BOT THIS IS WHY WE DONT MESS WITH TECH SUPPORT!!!!!!!!!!!!!!!!!!!!!!!!!!!! - Someone you know well.
Think of this as a little revenge.
"""
times = int(input("How many times do you what to spam? "))

em = EmailMessage()
em['From'] = email_sender
em['To'] = victims[0]
em['Subject'] = subject
em.set_content(body)

# Add SSL (layer of security)
context = ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    for victim in victims:
        print("spamming ", victim, "...")
        replace_string = "0"
        new_string = ""
        for i in range(times):
            print("Sending ", i + 1, "/", times, "...")
            
            new_string = str(i + 1)
            subject = subject.replace(replace_string, new_string)
            replace_string = new_string

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = victim
            em['Subject'] = subject
            em.set_content(body)

            smtp.sendmail(email_sender, victim, em.as_string())
