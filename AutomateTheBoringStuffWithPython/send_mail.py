"""
This is a python script to login an email account and send a 
pre determined test mail to a predetermined recipient.

"""


import getpass

import smtplib


# Create smtp Object using the smtp server name and its port
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

# Send a hello message
smtpObj.ehlo()


# Start the TLS encryption
smtpObj.starttls()


# Get the mail ID from user
usr = input('Enter your e-mail ID': )


# Get the password from the user

psd = getpass.getpass("Enter the password: ")


# Login 
smtpObj.login(usr, psd)



# Send Test mail to the receiver
smtpObj.sendmail('sender@server.com.com', 'receiver@server.com', 'Subject: Script mail\nThis is a test mail')



# Close the seesion with the smtp server
smtpObj.quit()
