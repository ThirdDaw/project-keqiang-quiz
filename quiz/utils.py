from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import datetime


def send_email_with_results(result):
    msg = MIMEMultipart()

    message = str(result)

    # setup the parameters of the message
    password = "password"
    msg['From'] = "email"
    msg['To'] = "nazarmartyn2000@gmail.com"
    msg['Subject'] = "Test Results"

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com: 587')

    server.starttls()

    server.login(msg['From'], password)

    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print("successfully sent email to %s:" % (msg['To']))


def save_result_in_file(result):
    filename = str(datetime.datetime.now().isoformat()).replace(":", " ")
    filepath = "media/results/" + filename

    print(filename)

    f = open(filepath, "w")
    f.write(str(result))
    f.close()
