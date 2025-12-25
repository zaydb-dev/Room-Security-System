import os
import smtplib
import mimetypes
from email.message import EmailMessage
from time import sleep
from signal import pause

# Third party imports
import cv2
from gpiozero import MotionSensor
from pygame import mixer

#Configuration
GPIO_PIN = 18 #this is the pin the pir sensor is connected to
ALARM_SOUND_PATH = os.getenv("ALARM_SOUND_PATH")
INTRUDER_PHOTO_PATH = os.getenv("INTRUDER_PHOTO_PATH") 
PORT_NUMBER = 587 
MAIL_HOSTNAME = 'smtp.gmail.com' #hostname and port number are for gmail, must be changed if using another mail service 
ALERT_SENDER_EMAIL = os.getenv("ALERT_SENDER_EMAIL")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")
TO_EMAIL_ADDRESS = os.getenv("TO_EMAIL_ADDRESS")

if not all([ALERT_SENDER_EMAIL, EMAIL_APP_PASSWORD, TO_EMAIL_ADDRESS]):
    print("FATAL ERROR: Email credentials have not been loaded")
    print("Please set ALERT_SENDER_EMAIL, EMAIL_APP_PASSOWRD and TO_EMAIL_ADDRESS in your shell environment")
    exit()

#Initializing pir variable 
pir = MotionSensor(GPIO_PIN) 

#Sound setup 
mixer.init()
alarm = mixer.Sound(ALARM_SOUND_PATH)

#Email setup
msg = EmailMessage() 

#Function setup:   

def image_capture():
    #Taking a pic 
    cam = cv2.VideoCapture(0) 

    if not cam.isOpened(): 
        print("Error: could not open camera")
        exit()
        
    ret, frame = cam.read() 

    if ret:
        full_path = os.path.join(INTRUDER_PHOTO_PATH, "intruder.jpg")
        cv2.imwrite(full_path, frame)
        print('Image saved as intruder.jpg')
    else: 
        print('Error: could not read frame')
        
    cam.release() 
    
def format_email():
    body = "Motion detected in your room."
    msg.set_content(body)
    msg['From'] = ALERT_SENDER_EMAIL
    msg['To'] = TO_EMAIL_ADDRESS
    msg['Subject'] = "INTRUDER ALERT"

def send_intruder_email(email, sender, password): 
    #Attaching image to email   
    image_path = full_path
    mime_type, _ = mimetypes.guess_type(image_path)
    mime_type, mime_subtype = mime_type.split('/')
    with open(image_path, 'rb') as img_file:
        msg.add_attachment(img_file.read(), 
                            maintype = mime_type, 
                            subtype = mime_subtype, 
                            filename=os.path.basename(image_path)) 
    #Sending email
    try:
        server = smtplib.SMTP(MAIL_HOSTNAME, PORT_NUMBER)
        server.starttls()
        server.login(sender, password)
        server.send_message(email)
        server.quit()
    except smtplib.SMTPAuthenticationError:
        print("ERROR: Authentication failed. Check email and app password.")
    except Exception as e:
        print(f"An error occured while sending email: {e}")

def motion_function():
    alarm.play()
    print("Motion Detected")
    
    image_capture()
    format_email()
    send_intruder_email(msg, ALERT_SENDER_EMAIL, EMAIL_APP_PASSWORD) 
    
    sleep(10)
    
def no_motion_function():
    print("Motion Stopped")
    
#Main script 
if __name__ == "__main__":
    pir.when_motion = motion_function
    pir.when_no_motion = no_motion_function

    try:
        pause()
    except KeyboardInterrupt:
        print("Alarm system stopped.")
