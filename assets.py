import os
import json
import socket
import getpass
import requests
from time import *
from datetime import datetime

def clear():
    os.system('cls')

def user_name():
    return getpass.getuser()

def user_ip():
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    return ip

def time_of_login():
    login_time = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")
    return login_time

def welcoming_quote():
    response = requests.get("https://zenquotes.io/api/random")
    data = json.loads(response.text)
    quote = (data[0]["q"] + " -" + data[0]["a"])
    return quote