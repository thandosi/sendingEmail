import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


s = smtplib.SMTP('smtp.gmail.com', 587)
sender_email_id = 'siyanjomeni@gmail.com'
receiver_email_id = 'ayamzazi@gmail.com , siyanjomemi@gmail.com, thapelo@lifechoices.co.za'
password = input("Enter senders email password")
subject = "greetings"
msg = MIMEMultipart()
msg['From'] = sender_email_id
msg['To'] = receiver_email_id
msg['Subject'] = subject

s.starttls()
# Authentication
s.login(sender_email_id, password)
# message to be sent
message = "hello"
message = message + "Hello"
msg.attach(MIMEText(message, "plain"))
text = msg.as_string()
# sending the mail
s.sendmail(sender_email_id, receiver_email_id, message)
# terminating the session
s.quit()

