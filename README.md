# Raspberry-Pi-Room-Security-System

OVERVIEW<br>
A Python based room security system that uses a PIR sensor, a camera and a Raspberry Pi to detect motion and email an alert.<p>

FEATURES<br>
-PIR sensor detects motion<br>
-Alarm sound is played<br>
-USB camera takes a photo<br> 
-The photo is sent in an email configured using SMTP with a secure TLS connection<p>

KEY HARDWARE & LIBRARIES<br>
-Raspberry Pi 4 Model B<br>
-PIR Motion Sensor<br>
-gpiozero, opencv-python, smtplib, pygame, os, signal libraries used.<p>

PREREQUISITES<br>
Hardware:<br>
  -Raspberry Pi (compatible with all 40 pin GPIO models, though older ones may experience slower image processing via opencv)<br>
  -A PIR Motion Sensor<br> 
  -A USB Camera connected to the Pi<br>
  -Speaker for audio output<br>
Software:<br>
  -Raspberry Pi OS<br>
  -Python 3.13.5 or later installed<br>
  -This script is preconfigured to use gmail for the alert sending email address, using another mail service requires changing the MAIL_HOSTNAME and PORT_NUMBER variables. This information is readily found online for all major email platforms.<br>
  -When using gmail, ensure that the sender email has 2FA enabled and that a 16-character App Password has been generated to use in place of the account's regular password.<p>

  
  




