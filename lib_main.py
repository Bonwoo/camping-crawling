import sys
import lib_telegram #telegram.py
from datetime import datetime


# 현재시간 리턴
def getTime():
    return str(datetime.today())

# 텔레그램 메시지 전송
def sendTelegram(msg):
    lib_telegram.sendTelegram(msg)
    

