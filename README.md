# ISS-International-Space-Station-Notifier

## Requirements
pip install requests

## What is International Space Station Notifier?
It is a software that notifies the user when the International Space Station is above the user's head implemented with requests, time, datetime, smtplib, and os python modules.

## How does it work?
The software uses requests to get data from 2 APIs. The first API serves to get the latitude and longitude of the International Space Station. The second API serves to determine Sunsets and Sunrises. Next, the software checks if ISS is overhead and if it is night time. If both conditions are met the user will receive an email informing him that the ISS is above in the sky. If the program will run for 24 hours the user will receive 2-3 emails notifying him that ISS is above head.

### Gmail configuration
Step 1:  Make sure you've got the correct smtp address for your email provider: smtp.gmail.com   
Step 2: Go to https://myaccount.google.com/  
Select Security on the left and scroll down to How you sign in to Google. Enable 2-Step Verification.     
Step 3: Click on 2-Step Verification again, and scroll to the bottom.   
<ul>
  <li>There you can add an App password.</li>
  <li>Select Other from the dropdown list and enter an app name, e.g. Python Mail, then click Generate.</li>    
  <li>COPY THE PASSWORD - This is the only time you will ever see the password. It is 16 characters with no spaces.</li>
  <li>Use this App password in your Python code instead of your normal password.</li>
</ul>     

Step 4: Add a port number by changing your code to this:       
smtplib.SMTP("smtp.gmail.com", port=587)
