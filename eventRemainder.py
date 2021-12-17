from smtplib import SMTP
from pwinput import pwinput
import countdown
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print("\n \n ** EVENT REMAINDER PROGRAM STARTING ** \n \n ")
email_id = input('Email ID : ')
password = pwinput()

reciever_id = input("\n Reciever's Email ID : ")

# Establishing the SMTP server.
try:
    smtp = SMTP('smtp.gmail.com' , 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email_id,password)

except Exception as e:
    print(" You may wanna enable less secure apps access to conitnue with the execution of this program : \n https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4PgdI8VHVpjVE4QJGzFVlhHXfjRFrLIz7msBslaJijnRpS8pYDZUpx3TkQrY9MHqOrqbAMhAa5xGMFv-n0fsgB47NP6lA \n Or The Authentication failed.")
    quit()
print('Authentication Successful ! \n ')

#Accepting Input.

on_going = True
info_list = list()
print("\n To exit , leave the subject blank. \n ")
while on_going:
    subject = input("\n Subject : ")
    if(subject==""):
        on_going = False
    else:
        info = input("\n A short elaboration of the event : ")
        time = input("\n The time inverval after which you want to be reminded (in hours) : ")
        info_list.append([subject,info,time])

print("The {} events have been added !".format(len(info_list)))

time_stamps = list()
time = 0
for i in range(len(info_list)):
    print('*'*100)
    event = info_list[i]
    if len(time_stamps) == 0:
        time = int(event[2])
        time_stamps.append(time)
        countdown.countdown_hours(time, event[0])

    else:
        time = int(event[2]) - time_stamps[0]
        time_stamps[0] = int(event[2])
        countdown.countdown_hours(time, event[0])

    # print(event)
    msg = MIMEMultipart()
    msg['Subject'] = event[0]
    msg.attach(MIMEText(event[1]))

    smtp.sendmail(from_addr=email_id,to_addrs=reciever_id,msg=msg.as_string())
    print("\n \n Email sent !")

