import requests
from bs4 import BeautifulSoup
import time
import lib_main

#날짜 입력 전 기본 URL
DEFAULT_URL = 'https://camping.gtdc.or.kr/DZ_reservation/reserCamping.php?xch=reservation&xid=camping_reservation&searchDate='             
            
INTERVAL_SECOND = 10 # 조회간격(초)

def getStock(url):
    #bot 감지 차단을 막기위한 헤더조작
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    data = requests.get(url, headers = headers)
    bsObj = BeautifulSoup(data.content, "html.parser")
    #print(bsObj) #접속안될때 풀어 보는 용도 

    result = bsObj.find('input', class_=r'prod-quantity__input') # 재고있는 상품은 1로 뜸
    remain = result.get('value') #string

    return remain

# 현재시간 리턴
def getTime():
    return lib_main.getTime()

# 텔레그램 메시지 전송
def sendMsg(msg):
    print(msg)
    lib_main.sendTelegram(msg) # 텔레그램 전송

# 마스크 리스트를 출력하여 어떤 마스크를 조회할지 알아본다
def getMask():
    index = int(lib_main.choiceLIST(MASK_LIST)) - 1 # 입력받은 마스크 항목을 인덱스 번호로 저장        
    mask = list(MASK_LIST.keys())[index]
    print('{}를 선택하셨습니다.'.format(mask))
    
    return mask

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
    '''       
    if url is None :
        msg = '크롤러[{}]를 시작할 수 없습니다.({})'.format(url, getTime())
        sendMsg(msg)
        return
    
    msg = '쿠팡 크롤러[{}]를 시작합니다.({})'.format(mask, getTime())
    sendMsg(msg)
    sendMsg(url)
    
    # 크롤링 작업 진행(10초마다[INTERVAL_SECOND])
    while 1:
        stock = getStock(url)        
        msg = '주문가능 수량({}) : {}'.format(getTime(), stock)        
        print(msg)

        # 수량 확인
        if stock != '0':
            msg = '수량 확인({}) : {}'.format(getTime(), stock)            
            sendMsg(msg)
            sendMsg(url)           
            
        time.sleep(INTERVAL_SECOND)
    '''       


# MAIN 으로 동작시키기 
if __name__ == "__main__" :
    startCrawler()    