import schedule
import time
import ssl
import smtplib
from email.message import EmailMessage

email_address = "use your Email"
email_password = "use your password"
recipient_list = ["aqinnaqin@yahoo.com", "mosesoleka@gmail.com","akinfracis74@gmail.com","adamaumaru@gmail.com"]

Email_msg = EmailMessage()
Email_msg["Subject"] = "Cohort5 Automation Email"
Email_msg["From"] = email_address
Email_msg["To"] = recipient_list
def mail():

     
    
    Email_msg.set_content("This email is to remind you of our schdule to study all pending tasks,And all member will receive this every 10 minutes! Thanks")
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
           
        smtp.login(email_address, email_password)
        smtp.sendmail(email_address, recipient_list, Email_msg.as_string())
        print("Successful sent")

        smtp.close()
mail()       
schedule.every(10).minute.do(mail)

while True:
    schedule.run_pending()
    time.sleep(1)