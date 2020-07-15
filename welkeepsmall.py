import lib_telegram
import time
from datetime import datetime
from selenium import webdriver
import sys

# 웰킵스 몰

#url = r'http://www.welkeepsmall.com/shop/shopdetail.html?branduid=997657&xcode=023&mcode=002&scode=&special=1&GfDT=am93Vw%3D%3D'
#url = r'http://www.welkeepsmall.com/shop/shopdetail.html?branduid=997657'
INTERVAL_SECOND = 10 # 새로고침




def getStock(url):   
    driver.get(url)    
    try :
        element = driver.find_element_by_class_name('soldout') # 재고 태그
        if element.text == 'SOLD OUT':
            return 0
    except :
        print('sold out 태그못찾음')        
        return 1

if __name__ == "__main__" :
    if len(sys.argv) != 2 :
        print("80 or 94 or hand 를 같이 입력해주세요(ex : python welkeepsmall.py 80)")
        sys.exit()
    
    driver = webdriver.Chrome()        

    if sys.argv[1] == "80" :
        # KF80
        url = r'http://www.welkeepsmall.com/shop/shopdetail.html?branduid=997657'
    elif sys.argv[1] == "94" :
        # KF94
        url = r'http://www.welkeepsmall.com/shop/shopdetail.html?branduid=997669'
    elif sys.argv[1].upper() == "HAND":
        # 손소독제
        url = r'http://www.welkeepsmall.com/shop/shopdetail.html?branduid=898874'
    
    
    driver.implicitly_wait(INTERVAL_SECOND) # 첫 로딩후 대기시간

    tt = str(datetime.today())
    lib_telegram.sendTelegram('웰킵스 마스크['+sys.argv[1]+'] 재고 확인 시작(' + tt + ')')    


    while 1:

        stock = getStock(url)
        msg = "주문가능 수량(" + tt + ") : " + str(stock)

        print(msg)
        if stock != 0:
            print('입고 확인... 메시지를 보냅니다...')
            lib_telegram.sendTelegram(msg)
            lib_telegram.sendTelegram(url)

        #driver.implicitly_wait(INTERVAL_SECOND) # 새로고침 대기시간
        time.sleep(INTERVAL_SECOND)
        tt = str(datetime.today())

        
