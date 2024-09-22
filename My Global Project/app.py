import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email, from_email, from_email_password):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_email_password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

def read_and_email(filename, to_email, from_email, from_email_password):
    with open(filename, 'r') as file:
        content = file.read().strip()
    
    send_email(
        subject="Location Report",
        body=f"Content of the file:\n\n{content}",
        to_email=to_email,
        from_email=from_email,
        from_email_password=from_email_password
    )

def main():
    filename = r"C:\\Users\\meera\\Downloads\\Location_Report.txt"
    to_email = "reciever@gmail.com"
    from_email = "sender@gmail.com"
<<<<<<< HEAD
    from_email_password = "oeao hmtq vvud fvfx"
=======
    from_email_password = "password"
>>>>>>> 0a1666d34a9ee3201a55ad7a06990912367685bb
    read_and_email(filename, to_email, from_email, from_email_password)

if __name__ == "__main__":
    main()
    
