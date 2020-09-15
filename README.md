# Sending email using Python smtplib

## Install smtplib
> pip install secure-smtplib

## Run script
> python send_email.py

if smtp failed to send email (Auth Error which is usually because you enabled 2 way Authorization) and your error looks like this: </br>
smtplib.SMTPAuthenticationError: (534, b'5.7.9 Application-specific password required. Learn more at\n5.7.9  https://support.google.com/mail/?p=InvalidSecondFactor f126sm23029039wmf.13 - gsmtp')

## 1. Allow access to your Google Account
To give access to your Google Account Open this url [Unlock Captcha](https://accounts.google.com/b/0/DisplayUnlockCaptcha)

## 2. Create & use App Passwords
If you use 2-Step-Verification and get a "password incorrect" error when you sign in, you can try to use an App Password.

1 Go to your Google Account. </br>
2 Select Security. </br>
3 Under "Signing in to Google," select App Passwords. You may need to sign in. If you don’t have this option, it might be because: </br>
	<pre>`a` 2-Step Verification is not set up for your account. </br>
	`b` 2-Step Verification is only set up for security keys. </br>
	`c` Your account is through work, school, or other organization. </br>
	`d` You turned on Advanced Protection. </pre> </br> 
4 At the bottom, choose Select app "Other" and name it "Python email sender" and then Generate. </br>
5 Follow the instructions to enter the App Password. The App Password is the 16-character code in the yellow bar on your device. </br>
6 Tap Done.
