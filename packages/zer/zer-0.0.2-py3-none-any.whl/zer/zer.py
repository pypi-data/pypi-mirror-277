"""
Zer is a Python module for code reduction and automation.

Module version: 0.0.2 alpha.
Publisher: ZerProg studio.
"""

import os as oss
import datetime
import sys
from tqdm import tqdm

class DateTime:
    '''The DateTime class works with date and time information.'''
    def date(separator='-',null=True):
        if null==True:
            Date = ['','']
            if datetime.date.today().day<=9:
                Date[0]='0'
            if datetime.date.today().month<=9:
                Date[1]='0'
            return f'{Date[0]}{datetime.date.today().day}{separator}{Date[1]}{datetime.date.today().month}{separator}{datetime.date.today().year}'
        return f'{datetime.date.today().day}{separator}{datetime.date.today().month}{separator}{datetime.date.today().year}'
    def day(null=True):
        if null==True:
            if datetime.date.today().day<=9:
                return f'0{datetime.date.today().day}'
        return datetime.date.today().day
    def month(null=True):
        if null==True:
            if datetime.date.today().month<=9:
                return f'0{datetime.date.today().month}'
        return datetime.date.today().month
    def year():
        return datetime.date.today().year
    def time(separator='-', null=True):
        if null==True:
            Time = ['','','']
            if datetime.datetime.now().hour<=9:
                Time[0]='0'
            if datetime.datetime.now().minute<=9:
                Time[1]='0'
            if datetime.datetime.now().second<=9:
                Time[2]='0'
            return f'{Time[0]}{datetime.datetime.now().hour}{separator}{Time[1]}{datetime.datetime.now().minute}{separator}{Time[2]}{datetime.datetime.now().second}'
        return f'{datetime.datetime.now().hour}{separator}{datetime.datetime.now().minute}{separator}{datetime.datetime.now().second}'
    def second(null=True):
        if null==True:
            if datetime.datetime.now().second<=9:
                return f'0{datetime.datetime.now().second}'
        return datetime.datetime.now().second
    def minute(null=True):
        if null==True:
            if datetime.datetime.now().minute<=9:
                return f'0{datetime.datetime.now().minute}'
        return datetime.datetime.now().minute
    def hour(null=True):
        if null==True:
            if datetime.datetime.now().hour<=9:
                return f'0{datetime.datetime.now().hour}'
        return datetime.datetime.now().hour
 
class os:
    '''
    The OS class works with information about the operating system.
    '''
    def nameuser():
        '''Getting username'''
        for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
            user = oss.environ.get(name)
            if user:
                return user
    def name():
        '''
        Getting the name of the operating system.
        '''
        return oss.uname().sysname
    def namepc():
        '''
        Getting the computer name.
        '''
        return oss.uname().nodename
    def version():
        '''
        Getting the operating system version.
        '''
        return oss.uname().version
    
class email:
    def send(Sender,Password,To,Theme,Text,Info=True):
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        """
        Sending an email. Only Gmail is supported.

        Sender: Sender's email.
        Pass: Password from the sender's Email.
        To: Recipient's email.
        Theme: Email Subject.
        Text: Email text.
        Info: If True, it displays information like 'sending...' and 'The letter was sent successfully.' to the console. Errors are always displayed.
        """
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(Sender, Password)

            msg = MIMEMultipart()

            msg["Sender"] = Sender
            msg["To"] = To
            msg["Subject"] = Theme

            content = f'{Text}'
            msg.attach(MIMEText(content, "plain"))

            if Info==True:
                print("Sending...")
            server.sendmail(Sender, To, msg.as_string())
            if Info==True:
                print("The letter was sent successfully.")
        except Exception as error:
            if error.errno==-2:
                print('\033[31mError: failed to contact the server or the name was entered incorrectly.\033[0;0m')
                return
            else:
                print(f'\033[31mError: {error}\033[0;0m')

    def send_files(Sender, Password,To,Theme,text=None, Html=None,Pathfile=None, Info=True):
        '''
        Send an email with HTML and other files attached. Only Gmail is supported.

        Sender: Sender's email.
        Pass: Password from the sender's Email.
        To: Recipient's email.
        Theme: Email Subject.
        Text: Email text.
        Html: Path to the HTML file.
        Pathfile: Path to the folder (without folders inside) with files. Supports text, image, audio, application... files
        Info: If True, it displays information like 'sending...' and 'The letter was sent successfully.' to the console. Errors are always displayed.
        '''
        import smtplib
        import mimetypes
        from email import encoders
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        from email.mime.image import MIMEImage
        from email.mime.audio import MIMEAudio
        from email.mime.application import MIMEApplication
        from email.mime.base import MIMEBase

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        try:
            server.login(Sender, Password)
            msg = MIMEMultipart()
            msg["Sender"] = Sender
            msg["To"] = To
            msg["Subject"] = Theme

            if text:
                msg.attach(MIMEText(text))

            if Html:
                try:
                    with open(Html) as file:
                        Html = file.read()
                except IOError:
                    Html = None
                msg.attach(MIMEText(Html, "html"))

            if Pathfile:
                if Info==True:
                    print("Loading files...")
                if Pathfile[len(Pathfile)-1]!='/' or Pathfile[len(Pathfile)-1]!='\\':
                    Pathfile+='/'
                for file in tqdm(os.listdir(Pathfile)):
                    try:
                        filename = os.path.basename(file)
                        ftype, encoding = mimetypes.guess_type(file)
                        file_type, subtype = ftype.split("/")
                    except:
                        print('File recognition error.')

                    if file_type == "text":
                        with open(f"{Pathfile}{file}") as f:
                            file = MIMEText(f.read())
                    elif file_type == "image":
                        with open(f"{Pathfile}{file}", "rb") as f:
                            file = MIMEImage(f.read(), subtype)
                    elif file_type == "audio":
                        with open(f"{Pathfile}{file}", "rb") as f:
                            file = MIMEAudio(f.read(), subtype)
                    elif file_type == "application":
                        with open(f"{Pathfile}{file}", "rb") as f:
                            file = MIMEApplication(f.read(), subtype)
                    else:
                        with open(f"{Pathfile}{file}", "rb") as f:
                            file = MIMEBase(file_type, subtype)
                            file.set_payload(f.read())
                            encoders.encode_base64(file)

                    file.add_header('content-disposition', 'attachment', filename=filename)
                    msg.attach(file)

            if Info==True:
                print("Sending...")
            server.sendmail(Sender, To, msg.as_string())

            if Info==True:
                print("The letter was sent successfully.")
        except Exception as error:
            if error.errno==-2:
                print('\033[31mError: The server could not be contacted or the name specified was incorrect.\033[0;0m')
                return
            print(f'Error: {error}')

def survey(text, yes, no):
    """
    Printing a question to the console.

    text: Text that will be displayed.
    yes: positive answer option.
    no: no answer option.
    """
    while True:
        inp = input(text)
        inp = inp.strip()
        inp = inp.lower()
        if inp==yes:
            return 'yes'
        if inp==no:
            return 'no'

def opensite(url):
    '''
    Opening a site in a browser.
    '''
    strar = url[:5]
    if strar!='https' and strar!='http:':
        temp=url
        url=f'http:/{temp}'
    if oss.name=='posix' or os.name=='Linux':
        oss.system(f"open '{url}'")
    if oss.name=='nt' or os.name=='Windows':
        oss.system(f"start '{url}'")

        