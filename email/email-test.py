import smtplib
# email package modules
from email.message import EmailMessage
import getpass

try:
  server = smtplib.SMTP('smtp.gmail.com', 587)
  #server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
  server.ehlo()
except:
  print("Something went wrong.")

# make connection secure
server.starttls()

print ("""Some smtp servers require enhanced security (two-factor
authentication, etc). If you are using google's smtp server, 
you may have to enable less secure apps at 
https://myaccount.google.com/lesssecureapps?pli=1""")
mypwd = getpass.getpass('Enter your gmail password: ')

my_email = "wmodes@csumb.edu"

msg = EmailMessage()

msg['Subject'] = "A message to my flock"
# msg['From'] = my_email
msg['From'] = "god@heaven.org"
# msg['To'] = "wmodes@csumb.edu"
msg['To'] = "zhutchinson@csumb.edu"
msg.set_content("Stop sinning. I'm watching you know.")

# could also place "with" inside a for loop for multiple images
with open('screen3.png', 'rb') as fp:
    img_data = fp.read()

# check out imghdr to automatically detect image subtype
msg.add_attachment(img_data, maintype='image', subtype='png')

server.login(my_email, mypwd)

server.send_message(msg)
server.quit()