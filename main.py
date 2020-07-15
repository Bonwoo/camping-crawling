import getpass
import coupang # 쿠팡 크롤러
import os
from lib_main import PG_LIST, choiceLIST


if __name__ == "__main__":

    index = int(choiceLIST(PG_LIST)) - 1 # 입력받은 항목을 인덱스 번호로 저장
    if list(PG_LIST.keys())[index] == '쿠팡' :
        print('쿠팡 프로그램을 시작합니다...')            
        coupang.startCrawler()
        
