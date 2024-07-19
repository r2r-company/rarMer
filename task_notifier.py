import socket
import requests
import os
import django
from datetime import datetime

API_URL = "http://127.0.0.1:8000/api/notify/"

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rarMer.settings')
django.setup()

from tasks.models import ComputerInfo

def save_computer_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    ComputerInfo.objects.create(hostname=hostname, ip_address=ip_address, timestamp=datetime.now())

# Виклик функції для запису даних у базу
save_computer_info()

def get_computer_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return hostname, ip_address

def send_notification():
    hostname, ip_address = get_computer_info()
    data = {
        "hostname": hostname,
        "ip_address": ip_address
    }
    try:
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            print("Notification sent successfully")
        else:
            print(f"Failed to send notification: {response.status_code}")
    except Exception as e:
        print(f"Error sending notification: {e}")

if __name__ == "__main__":
    send_notification()
