import requests
from bs4 import BeautifulSoup
import time
import lib_main

#날짜 입력 전 기본 URL
DEFAULT_URL = 'https://camping.gtdc.or.kr/DZ_reservation/reserCamping.php?xch=reservation&xid=camping_reservation&searchDate='             
            
INTERVAL_SECOND = 5 # 조회간격(초)

def getInfo(url, date, area):
    #bot 감지 차단을 막기위한 헤더조작
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    data = requests.get(url, headers = headers)
    bsObj = BeautifulSoup(data.content, "html.parser")
    #print(bsObj) #접속안될때 풀어 보는 용도 

    
    value = area+":"+date[:4]+"-"+date[4:6]+"-"+date[6:8] # 버튼에 있는 value 값
    #print('value = {}'.format(value)) # TEST 출력

    
    result = bsObj.find('button', {"value":value}) # 재고있는 상품은 1로 뜸
    
    print(result)    

    return result

# 현재시간 리턴
def getTime():
    return lib_main.getTime()

# 텔레그램 메시지 전송
def sendMsg(msg):
    print(msg)
    #lib_main.sendTelegram(msg) # 텔레그램 전송


# URL
def getUrl(date):
    return DEFAULT_URL+date[:6]


# 작업일자를 입력받아 리턴
def getDate():
    date = input("작업일자(YYYYMMDD) : ")
    #print(date.isdigit())
    return date

# 작업구역을 입력받아 리턴
def getArea():
    area = input("작업구역(A-E) : ")
    #print(area.isalpha())
    return area


# 크롤러 시작
def startCrawler():
    
    date = getDate() # 작업일자
    area = getArea() # 작업구역
    url = getUrl(date)
    print('작업일자 : {}'.format(date))
    print('작업구역 : {}'.format(area))
    print('URL : {}'.format(url))
           
    if url is None :
        msg = '크롤러[{}]를 시작할 수 없습니다.({})'.format(url, getTime())
        sendMsg(msg)
        return
    
    msg = '크롤러를 시작합니다.(작업일자{}작업구역{})'.format(date, area)
    sendMsg(msg)
    sendMsg(url)
    
    # 크롤링 작업 진행(5초마다[INTERVAL_SECOND])
    while 1:
        result = getInfo(url, date, area)        
        #msg = '주문가능 수량({}) : {}'.format(getTime(), result)        
        #print(msg)

        # 수량 확인
        if result is None:
            print('수량 없음({})'.format(getTime()))
        else:
            msg = '수량 확인({}) : {}'.format(getTime(), result)            
            sendMsg(msg)
            sendMsg(url)           
            
        time.sleep(INTERVAL_SECOND)



# MAIN 으로 동작시키기 
if __name__ == "__main__" :
    startCrawler()    