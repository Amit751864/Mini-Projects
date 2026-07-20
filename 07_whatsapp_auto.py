''' twilio
datetime
time sleep
timedelta is difference btw two times
step1 -twilio cilent stepup
step2 user input
step3 scheduling logic
step4 send message
'''
#step1 install required libraries
from twilio.rest import Client
from datetime import datetime,timedelta
import time

########
#step 2\twilio credintials
account_sid ='ACf52d73cb996330c38254205de910dd49'
auth_token = 'd89993f7583f46d9b717d38fd2958c12'

client = Client(account_sid,auth_token)

#####
#step3 user input design a send message function

def send_whatsapp_message(recipent_number,message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=message_body,
            to=f'whatsapp:{recipent_number}'
        )
        print(f"Message sent successfully ! Message SID{message.sid}")
    except Exception as e:
        print("An error Occurred")   
#step 4 user input
name=(input("Enter the recipient name = "))
recipent_number=input("Enter your recipent no with country code = ")
message_body =input(f'enter the message you want to send to{name}: ')  

#step 5 parse date/time and calculation delay
date_str = input("enter the date send the message(YYYY-MM-DD):")
time_str =input('enter the time to send the message (HH:MM in 24 hours format):')

#datetime
schedule_datetime = datetime.strptime(f"{date_str} {time_str}","%Y-%m-%d %H:%M")
current_datetime = datetime.now()

#calculate delay
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <=0:
    print("the specified time is in past .please enter a future date and time:")
else: 
    print(F"Message sceduled to be sent to{name} at {schedule_datetime},")

    ######
    # wait until the scheduled time
    time.sleep(delay_seconds)   #1000
    
    #send the mess
    send_whatsapp_message(recipent_number,message_body)





