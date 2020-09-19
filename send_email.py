import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

port = 587  # For starttls
smtp_server = "smtp.gmail.com"  #'smtp.office365.com'
sender_email = "sender@mail.com"
receiver_email = "receiver@mail.com"
password = "16-character code generated from App Password" #input("Type your password and press enter:")
msg = MIMEMultipart()
msg['Subject'] = 'Testing email with attachment'
msg['From'] = sender_email
msg['To'] = receiver_email 

msgText = MIMEText('<b>%s</b>' % ("This is the body of email"), 'html')
msg.attach(msgText)

with open('python_image.png', 'rb') as fp:
        img = MIMEImage(fp.read())
        img.add_header('Content-Disposition', 'attachment', filename="python_image.png")
        msg.attach(img)

#context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls()
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())