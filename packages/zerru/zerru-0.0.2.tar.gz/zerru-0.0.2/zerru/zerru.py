"""
Zer-ru — это модуль zer на русском! Для сокращения и автоматизации кода.

Версия модуля: 0.0.2 alpha.
Издатель: ZerProg studio.
"""

import os as oss
import datetime
import sys
from tqdm import tqdm

class DateTime:
    '''Класс DateTime работает с информацией о дате и времени.'''
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
    Класс os работает с информацией об операционной системе.
    '''
    def nameuser():
        '''Получение имени пользователя.'''
        for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
            user = oss.environ.get(name)
            if user:
                return user
    def name():
        '''
        Получение названия операционной системы.
        '''
        return oss.uname().sysname
    def namepc():
        '''
        Получение имени компьютера.
        '''
        return oss.uname().nodename
    def version():
        '''
        Получение версии операционной системы.
        '''
        return oss.uname().version

class email:
    def send(Sender,Password,To,Theme,Text,Info=True):
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        '''
        Отправка электронного письма. Поддерживается только Gmail.

        Sender: Email отправителя.
        Pass: Пароль от Email отправителя.
        To: Email получателя.
        Theme: Тема Email.
        Text: Текст Email.
        Info: Если True то выводит в консоль информацию по типу 'отправка...' и 'Письмо было успешно отправлено.'. Ошибки выводятся всегда.
        '''
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
                print("Отправка...")
            server.sendmail(Sender, To, msg.as_string())

            if Info==True:
                print("Письмо было успешно отправлено.")
            return
        except Exception as error:
            if error.errno==-2:
                print('\033[31mОшибка: не удалось связатся с сервером или указано неверно имя.\033[0;0m')
                return
            else:
                print(f'\033[31mОшибка: {error}\033[0;0m')

    def send_files(Sender, Password,To,Theme,text=None, Html=None,Pathfile=None, Info=True):
        '''
        Отправка электронного письма с вложеным HTML и другими файлами. Поддерживается только Gmail.
        
        Sender: Email отправителя.
        Pass: Пароль от Email отправителя.
        To: Email получателя.
        Theme: Тема Email.
        Text: Текст Email.
        Html: Путь к файлу HTML.
        Pathfile: Путь к папке(без папок внутри) с файлами. Поддержка файлов text, image, audio, application...
        Info: Если True то выводит в консоль информацию по типу 'отправка...' и 'Письмо было успешно отправлено.'. Ошибки выводятся всегда.
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
                    print("Загрузка файлов...")
                if Pathfile[len(Pathfile)-1]!='/' or Pathfile[len(Pathfile)-1]!='\\':
                    Pathfile+='/'
                for file in tqdm(os.listdir(Pathfile)):
                    try:
                        filename = os.path.basename(file)
                        ftype, encoding = mimetypes.guess_type(file)
                        file_type, subtype = ftype.split("/")
                    except:
                        print('Ошибка распознания файлов.')

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
                print("Отправка...")
            server.sendmail(Sender, To, msg.as_string())

            if Info==True:
                print("Письмо было успешно отправлено.")
        except Exception as error:
            if error.errno==-2:
                print('\033[31mОшибка: не удалось связаться с сервером или указано неверное имя.\033[0;0m')
                return
            print(f'Ошибка: {error}')

def survey(text, yes, no):
    """
    Вывод вопроса в консоль.

    text: Текст который будет выведен.
    yes: Вариант положительного ответа.
    no: Вариант отрицательного ответа.
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
    Открытие сайта в браузере.
    '''
    strar = url[:5]
    if strar!='https' and strar!='http:':
        temp=url
        url=f'http:/{temp}'
    if oss.name=='posix' or os.name=='Linux':
        oss.system(f"open '{url}'")
    if oss.name=='nt' or os.name=='Windows':
        oss.system(f"start '{url}'")

        