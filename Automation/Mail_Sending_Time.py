import smtplib
from email.message import EmailMessage
import schedule
import time

def send_mail(sender , app_password , receiver , subject , body):

    msg = EmailMessage()

    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    msg.set_content(body)

    smtp = smtplib.SMTP_SSL("smtp.gmail.com" , 465)

    smtp.login(sender , app_password)

    smtp.send_message(msg)

    smtp.quit()

    print("Marvellous Mail Sent Succesfully")

def Mail():
    
    sender_email = "nehajthorat.sits.it@gmail.com"

    app_password = "qhxe oabm jxwj jncw"

    receiver_email = "nehaathorat12345@gmail.com"

    subject = "Test mail from python script"

    body = """Otanjoubi Omedetou Neha San. 諦めない。Welcome to JAPAN !!
    
    Regards,
    Neha Thorat
    """

    send_mail(sender_email , app_password , receiver_email , subject , body)

def main():

    schedule.every(1).minutes.do(Mail)

    print("Automation Started")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()