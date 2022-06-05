import smtplib

MY_EMAIL = "testingemailpython0101@gmail.com"
MY_PASS = "testingemail"
RECEIVER_MAIL = "testingemailpython0101@gmail.com"

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def notify(self, receiver_mail, msg):
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(user=MY_EMAIL, password=MY_PASS)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=receiver_mail, msg=msg)
