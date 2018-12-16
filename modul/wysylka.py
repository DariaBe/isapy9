import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def wyslij_emaila(temat, tresc):
    """Funkcja wysla e-maila o okreslonym temacie i tresci
        :param temat: temat maila
        :param tresc: tresc maila
        :return:"""
    mail = MIMEMultipart()
    mail['Subject'] = temat
    mail['To'] = 'bobadaria@yahoo.com'
    mail['From'] = 'isapy@int.pl'

    body = MIMEText(tresc)
    mail.attach(body)

    serwer = smtplib.SMTP('poczta.int.pl')
    serwer.login('isapy@int.pl', 'isapython;')
    serwer.send_message(mail)
    serwer.quit()

    print('Wyslano email')

