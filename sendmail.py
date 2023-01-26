import smtplib, time
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

class Mail:
    def __init__(self, receiver, file):
        self.receiver = receiver
        self.file = file
        return Mail.send_mail(receiver,file)


    def send_mail(receiver, file):
        sender_email = "Isi dengan email anda...."
        receiver_email = receiver

        date = time.strftime("%d-%m-%Y")

        msg = MIMEMultipart()
        msg['Subject'] = 'SQL Backup'
        msg['From'] = sender_email
        msg['To'] = receiver_email
            
        sql = MIMEApplication(open(f"./{date}/{file}.sql", 'rb').read())
        sql.add_header('Content-Disposition', 'attachment', filename= f"{file}.sql")
        msg.attach(sql)

        try:
            with smtplib.SMTP('', 587) as smtpObj:
                smtpObj.ehlo()
                smtpObj.starttls()
                smtpObj.login(sender_email, "Isi dengan email anda....")
                smtpObj.sendmail(sender_email, receiver_email, msg.as_string())
        except Exception as e:
            return e

