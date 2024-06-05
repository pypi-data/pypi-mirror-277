"""
Zer is a Python module for code reduction and automation.

Module version: 0.0.1 alpha.
Publisher: ZerProg studio.
"""

import os as oss
import datetime
import sys

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
    
def send(From,Password,To,Theme,Text):
    """
    Sending an email message

    From: Sender's email
    Pass: Password from the sender's Email
    To: Recipient's email
    Theme: Email Subject
    Text: Text Email
    """
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    try:
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.starttls()
        smtp_server.login(From, Password)

        msg = MIMEMultipart()

        msg["From"] = From
        msg["To"] = To
        msg["Subject"] = Theme

        content = f'{Text}'
        msg.attach(MIMEText(content, "plain"))

        smtp_server.sendmail(From, To, msg.as_string())
        return
    except Exception as error:
        if error.errno==-2:
            print('\033[31mError: failed to contact the server or the specified name is incorrect.\033[0;0m')
            return
        else:
            print(f'\033[31mError: {error}\033[0;0m')

def survey(text, yes, no):
    """
    Question in the console.

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

        