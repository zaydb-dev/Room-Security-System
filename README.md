# Raspberry-Pi-Room-Security-System

### OVERVIEW<br>
A Python based room security system that uses a PIR sensor, a camera and a Raspberry Pi to detect motion and email an alert.<p>

### FEATURES<br>
-PIR sensor detects motion<br>
-Alarm sound is played<br>
-USB camera takes a photo<br> 
-The photo is sent in an email configured using SMTP with a secure TLS connection<p>

### KEY HARDWARE & LIBRARIES<br>
-Raspberry Pi 4 Model B<br>
-PIR Motion Sensor<br>
-gpiozero, opencv-python, smtplib, pygame, os, signal libraries used.<p>

### PREREQUISITES<br>
#### Hardware:<br>
  -Raspberry Pi (compatible with all 40 pin GPIO models, though older ones may experience slower image processing via opencv)<br>
  -A PIR Motion Sensor<br> 
  -A USB Camera connected to the Pi<br>
  -Speaker for audio output<br>
  -Female-to-Female jumper wires<br>
#### Software:<br>
  -Raspberry Pi OS<br>
  -Python 3.13.5 or later installed<br>
  -This script is preconfigured to use gmail for the alert sending email address, using another mail service requires changing the MAIL_HOSTNAME and PORT_NUMBER variables. This information is readily found online for all major email platforms.<br>
  -When using gmail, ensure that the sender email has 2FA enabled and that a 16-character App Password has been generated to use in place of the account's regular password.<p>
### WIRING:<br>
  -Ensure the PIR sensor is connected as follows:<br>
    1. VCC -> Pi 5V<br>
    2. GND -> Pi Gnd<br> 
    3. OUT -> GPIO 18<br>
  -Note: Configure the sensor's delay and senstivity knobs to your liking, the script will work regardless of what type of sensor is used.<p>
### SETUP AND INSTALLATION:<br>
  -Clone the repo:<br>
  ```git clone https://github.com/zaydb-dev/Room-Security-System.git```<br>
  -Enter the project directory:<br>
  ```cd Room-Security-System```<br> 
  -Install OpenCV (image processing) and Pygame (audio playback):<br>
  ```sudo apt update```<br>
  ```sudo apt install libopencv-dev python3-opencv python3-pygame python3-gpiozero python3-dotenv -y```<br>   
  -Create the folder where the script will save intruder images and record the filepath, this will be used to set the INTRUDER_PHOTO_PATH environment variable later.<br>
### CONFIGURATION AND SECURITY:<br>
  -To protect credentials, thus project uses Environment Variables rather than hard coding passwords into the script.<br>
    1. Enable 2FA on your Gmail account and generate a 16 character App Password (tutorials for this are widely available online)<br>
    2. In the same directory as the script, create a file named ".env" with the following plain text:<br>
    ```ALERT_SENDER_EMAIL="your-email@gmail.com"```<br>
    ```EMAIL_APP_PASSWORD="xxxx xxxx xxxx xxxx"```<br>
    ```TO_EMAIL_ADDRESS="destination@gmail.com"```<br>
    3. You can also set your alarm sound and where the intruder images will be stored in the same .env file:<br>
    ```ALARM_SOUND_PATH="insert sound file path here"```<br>
    ```INTRUDER_PHOTO_PATH="inster intruder photo folder path here"```<br>
### EXECUTION:<br>
  -Once you've done all of the above, you should be ready to go! Launch the security system:<br>
  ```python3 room_security_system.py```<br>
  -Detection: When the PIR sensor is triggered, the .mp3 alarm will play, and an image will be captured.<br>
  -Emailing: The script will automatically log into the SMTP server and send the image to your TO_EMAIL_ADDRESS.<br>
  -Shutdown: To stop the system, press Ctrl + C.<br>
### CREDITS AND LICENSE:<br>
  -This project is licensed under the MIT License.<br>
  -Author: Zayd Boutaleb (Feel free to reach out via https://ca.linkedin.com/in/zayd-boutaleb-a657ba30a)
  

  
  
  
  

  

  
  




