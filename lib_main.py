import sys
import lib_telegram #telegram.py
from datetime import datetime

PG_LIST = { '쿠팡' : 1, '웰킵스' : 2}

# 현재시간 리턴
def getTime():
    return str(datetime.today())

# 텔레그램 메시지 전송
def sendTelegram(msg):
    lib_telegram.sendTelegram(msg)
    

# 딕셔너리 값을 화면에 표시하여 값을 읽음
def choiceLIST(list):
    while True :
        i = 0
        # for 상품출력
        for key in list.keys():
            i = i + 1
            print('{}. {}'.format(str(i), key))

        choice = input('숫자를 입력하세요[Q:종료] : ')

        # Q를 입력하면 종료
        if str(choice).upper == 'Q' :
            print('프로그램을 종료합니다.')
            sys.exit()            

        if choice.isdecimal == False: # 숫자만 입력가능
            continue
        elif int(choice) > i : #LIST보다 큰 값을 입력한 경우            
            continue
        else :
            print(choice)
            return choice