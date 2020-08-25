# File Name    :- bulk_email_sender.py
# Type         :- Python program
# last modify  :- 25 Aug 2020
# sent email through smtp connection
# In setting of senders mail id Less secure app access must be ON >>>   account setting >  security > Less Secure access > ON
# In Email text file in one line only one email should be placed
# enter correct email text file
# Email text file should be at same path of the project file


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def emm(clients):
    sender = input("Enter name of sender : ")
    email_account = input("Enter Email of sender : ")
    passwords = input("Enter password of sender's email : ")
    subject = input("Enter Subject of your mail : ")
    texts = input("Type your mail : ")
    for i in clients:
     message = MIMEMultipart()
     message["from"] = sender
     message["to"]= i
     message["subject"] = subject
     message.attach(MIMEText(texts))
     with smtplib.SMTP(host="smtp.gmail.com" , port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(email_account,passwords)
            smtp.send_message(message)
            print(f"Successfully sent to ==> {i}")


var1=int(input("Enter 1 to insert email file \nEnter 2 to enter email manully\nEnter 3 for help\nEnter your choice ==>"))
if var1 == 1:
    email_file = input("Enter file name : ")
    clients = open(email_file, "r")
    emm(clients)
if var1 == 2:
    emaill2 = []
    count = 0
    while count < 1:
        emaill = input("Enter email : ")
        emaill2.insert(1, emaill)
        count = int(input("To continue press 0 : "))
        print(emaill2)
    emm(emaill2)
if var1 == 3:
    help = "\x1b[31m1 >>> On pressing 1 you have to give a file name which is placed at the same location of project file...\n" \
       "  >>> File must be with extension .txt ...\n" \
       "  >>> In file arrangement of emails like ..one email in one line\x1b[39m\n" \
       "\x1b[34m2 >>> On pressing 2 you have to give emails you want to enter..\n" \
       "  >>> enter one email and then press 0 to continue to add emails in the list..\n" \
       "  >>> once the list of the email complete then press 1 in place of 0 then the list is completed and further process is start..\x1b[39m\n" \
       "\x1b[31m**** if you get errors :- 1.. Check internet connection.\n" \
       "                          2.. On less secure app access in your gmail setting.\n" \
       "                          3.. Check all modules and packages are install or not\x1b[39m"
    print(help)

