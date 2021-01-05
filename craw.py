from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from requests import get  # to make GET request
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as bs
import requests
from selenium.webdriver.common.keys import Keys
import time
from multiprocessing import Pool,freeze_support
from selenium.common.exceptions import UnexpectedAlertPresentException



def craw(code_list):
    err=''
    종목명 = []
    매출액_17 = []
    매출액_18 = []
    매출액_19 = []
    매출액_20 = []

    당기순이익_17 = []
    당기순이익_18 = []
    당기순이익_19 = []
    당기순이익_20 = []

    ROA_17 = []
    ROA_18 = []
    ROA_19 = []
    ROA_20 = []

    ROE_17 = []
    ROE_18 = []
    ROE_19 = []
    ROE_20 = []

    EPS_17 = []
    EPS_18 = []
    EPS_19 = []
    EPS_20 = []

    BPS_17 = []
    BPS_18 = []
    BPS_19 = []
    BPS_20 = []

    DPS_17 = []
    DPS_18 = []
    DPS_19 = []
    DPS_20 = []

    PER_17 = []
    PER_18 = []
    PER_19 = []
    PER_20 = []

    PBR_17 = []
    PBR_18 = []
    PBR_19 = []
    PBR_20 = []

    자산총계_17 = []
    자산총계_18 = []
    자산총계_19 = []
    자산총계_20 = []

    자본총계_17 = []
    자본총계_18 = []
    자본총계_19 = []
    자본총계_20 = []

    부채총계_17 = []
    부채총계_18 = []
    부채총계_19 = []
    부채총계_20 = []

    부채비율_17 = []
    부채비율_18 = []
    부채비율_19 = []
    부채비율_20 = []
    test1=''
    # 매출액,영업이익,당기순익
    # 크롬드라이버 켜기
    # 코랩에서는 chrome_options> options
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-features=NetworkService")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-features=VizDisplayCompositor")
    driver = webdriver.Chrome('chromedriver', options=options)
    driver.implicitly_wait(3)
    url = 'http://asp01.fnguide.com/SVO2/asp/SVD_Main.asp?pGB=1&gicode=A028260&cID=&MenuYn=Y&ReportGB=&NewMenuID=101&stkGb=701'
    driver.get(url)
    # 크롬드라이버 조작
    driver.find_element_by_id('SearchText')  # 현재 크롬에 떠 있는 웹페이지에서 id 속성 값이 id 인 element를 찾음
    driver.find_element_by_id('SearchText').clear()
    driver.find_element_by_id('SearchText').send_keys(code_list)  # typing
    driver.find_element_by_id('SearchText').send_keys(Keys.ENTER)
    html = driver.page_source  # 페이지의 elements모두 가져오기
    soup = BeautifulSoup(html, 'html.parser')  # BeautifulSoup사용하기




    name = soup.select('#giName')
    # 코랩에서는 td:nth-type 에서 td:nth-of-type td도 하나씩뺴야한다!!!
    sub_매출액_17 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(1) > td:nth-of-type(1)')
    sub_매출액_18 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(1) > td:nth-of-type(2)')
    sub_매출액_19 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(1) > td:nth-of-type(3)')
    sub_매출액_20 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(1) > td:nth-of-type(4)')

    sub_당기순이익_17 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(4) > td:nth-of-type(1)')
    sub_당기순이익_18 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(4) > td:nth-of-type(2)')
    sub_당기순이익_19 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(4) > td:nth-of-type(3)')
    sub_당기순이익_20 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(4) > td:nth-of-type(4)')

    sub_ROA_17 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(17) > td:nth-of-type(1)')
    sub_ROA_18 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(17) > td:nth-of-type(2)')
    sub_ROA_19 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(17) > td:nth-of-type(3)')
    sub_ROA_20 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(17) > td:nth-of-type(4)')

    sub_ROE_17 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(18) > td:nth-of-type(1)')
    sub_ROE_18 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(18) > td:nth-of-type(2)')
    sub_ROE_19 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(18) > td:nth-of-type(3)')
    sub_ROE_20 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(18) > td:nth-of-type(4)')

    sub_EPS_17 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(19) > td:nth-of-type(1)')
    sub_EPS_18 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(19) > td:nth-of-type(2)')
    sub_EPS_19 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(19) > td:nth-of-type(3)')
    sub_EPS_20 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(19) > td:nth-of-type(4)')

    sub_BPS_17 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(20) > td:nth-of-type(1)')
    sub_BPS_18 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(20) > td:nth-of-type(2)')
    sub_BPS_19 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(20) > td:nth-of-type(3)')
    sub_BPS_20 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(20) > td:nth-of-type(4)')

    sub_DPS_17 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(21) > td:nth-of-type(1)')
    sub_DPS_18 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(21) > td:nth-of-type(2)')
    sub_DPS_19 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(21) > td:nth-of-type(3)')
    sub_DPS_20 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(21) > td:nth-of-type(4)')

    sub_PER_17 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(22) > td:nth-of-type(1)')
    sub_PER_18 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(22) > td:nth-of-type(2)')
    sub_PER_19 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(22) > td:nth-of-type(3)')
    sub_PER_20 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(22) > td:nth-of-type(4)')

    sub_PBR_17 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(23) > td:nth-of-type(1)')
    sub_PBR_18 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(23) > td:nth-of-type(2)')
    sub_PBR_19 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(23) > td:nth-of-type(3)')
    sub_PBR_20 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(23) > td:nth-of-type(4)')

    sub_자산총계_17 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(7) > td:nth-of-type(1)')
    sub_자산총계_18 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(7) > td:nth-of-type(2)')
    sub_자산총계_19 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(7) > td:nth-of-type(3)')
    sub_자산총계_20 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(7) > td:nth-of-type(4)')

    sub_자본총계_17 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(8) > td:nth-of-type(1)')
    sub_자본총계_18 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(8) > td:nth-of-type(2)')
    sub_자본총계_19 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(8) > td:nth-of-type(3)')
    sub_자본총계_20 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(8) > td:nth-of-type(4)')

    sub_부채총계_17 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(9) > td:nth-of-type(1)')
    sub_부채총계_18 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(9) > td:nth-of-type(2)')
    sub_부채총계_19 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(9) > td:nth-of-type(3)')
    sub_부채총계_20 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(9) > td:nth-of-type(4)')

    sub_부채비율_17 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(13) > td:nth-of-type(1)')
    sub_부채비율_18 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(13) > td:nth-of-type(2)')
    sub_부채비율_19 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(13) > td:nth-of-type(3)')
    sub_부채비율_20 = soup.select('#highlight_D_A > table > tbody > tr:nth-of-type(13) > td:nth-of-type(4)')

    # 크롬드라이버 조작
    # driver.find_element_by_id('compGnb').click()

    #   sub_영업활동_17=soup.select('#divCashY > table > tbody > tr:nth-of-type(1) > td:nth-of-type(1)')
    #   sub_영업활동_18=soup.select('#divCashY > table > tbody > tr:nth-of-type(1) > td:nth-of-type(2)')
    #   sub_영업활동_19=soup.select('#divCashY > table > tbody > tr:nth-of-type(1) > td:nth-of-type(3)')

    #   sub_투자활동_17=soup.select('#divCashY > table > tbody > tr:nth-of-type(84) > td:nth-of-type(1) > span')
    #   sub_투자활동_18=soup.select('#divCashY > table > tbody > tr:nth-of-type(84) > td:nth-of-type(2) > span')
    #   sub_투자활동_19=soup.select('#divCashY > table > tbody > tr:nth-of-type(84) > td:nth-of-type(3) > span')

    #   sub_재무활동_17=soup.select('#divCashY > table > tbody > tr:nth-of-type(121) > td:nth-of-type(1) > span')
    #   sub_재무활동_18=soup.select('#divCashY > table > tbody > tr:nth-of-type(121) > td:nth-of-type(2) > span')
    #   sub_재무활동_19=soup.select('#divCashY > table > tbody > tr:nth-of-type(121) > td:nth-of-type(3) > span')

    for i in sub_매출액_19:
        err=i.text.strip()
    if err != '':
        for i in name:
            종목명.append(i.text.strip())
        for i in sub_매출액_17:
            매출액_17.append(i.text.strip())
        for i in sub_매출액_18:
            매출액_18.append(i.text.strip())
        for i in sub_매출액_19:
            매출액_19.append(i.text.strip())
        for i in sub_매출액_20:
            매출액_20.append(i.text.strip())

        for i in sub_당기순이익_17:
            당기순이익_17.append(i.text.strip())
        for i in sub_당기순이익_18:
            당기순이익_18.append(i.text.strip())
        for i in sub_당기순이익_19:
            당기순이익_19.append(i.text.strip())
        for i in sub_당기순이익_20:
            당기순이익_20.append(i.text.strip())

        for i in sub_ROA_17:
            ROA_17.append(i.text.strip())
        for i in sub_ROA_18:
            ROA_18.append(i.text.strip())
        for i in sub_ROA_19:
            ROA_19.append(i.text.strip())
        for i in sub_ROA_20:
            ROA_20.append(i.text.strip())

        for i in sub_ROE_17:
            ROE_17.append(i.text.strip())
        for i in sub_ROE_18:
            ROE_18.append(i.text.strip())
        for i in sub_ROE_19:
            ROE_19.append(i.text.strip())
        for i in sub_ROE_20:
            ROE_20.append(i.text.strip())

        for i in sub_EPS_17:
            EPS_17.append(i.text.strip())
        for i in sub_EPS_18:
            EPS_18.append(i.text.strip())
        for i in sub_EPS_19:
            EPS_19.append(i.text.strip())
        for i in sub_EPS_20:
            EPS_20.append(i.text.strip())

        for i in sub_BPS_17:
            BPS_17.append(i.text.strip())
        for i in sub_BPS_18:
            BPS_18.append(i.text.strip())
        for i in sub_BPS_19:
            BPS_19.append(i.text.strip())
        for i in sub_BPS_20:
            BPS_20.append(i.text.strip())

        for i in sub_DPS_17:
            DPS_17.append(i.text.strip())
        for i in sub_DPS_18:
            DPS_18.append(i.text.strip())
        for i in sub_DPS_19:
            DPS_19.append(i.text.strip())
        for i in sub_DPS_20:
            DPS_20.append(i.text.strip())

        for i in sub_PER_17:
            PER_17.append(i.text.strip())
        for i in sub_PER_18:
            PER_18.append(i.text.strip())
        for i in sub_PER_19:
            PER_19.append(i.text.strip())
        for i in sub_PER_20:
            PER_20.append(i.text.strip())

        for i in sub_PBR_17:
            PBR_17.append(i.text.strip())
        for i in sub_PBR_18:
            PBR_18.append(i.text.strip())
        for i in sub_PBR_19:
            PBR_19.append(i.text.strip())
        for i in sub_PBR_20:
            PBR_20.append(i.text.strip())

        for i in sub_자산총계_17:
            자산총계_17.append(i.text.strip())
        for i in sub_자산총계_18:
            자산총계_18.append(i.text.strip())
        for i in sub_자산총계_19:
            자산총계_19.append(i.text.strip())
        for i in sub_자산총계_20:
            자산총계_20.append(i.text.strip())

        for i in sub_자본총계_17:
            자본총계_17.append(i.text.strip())
        for i in sub_자본총계_18:
            자본총계_18.append(i.text.strip())
        for i in sub_자본총계_19:
            자본총계_19.append(i.text.strip())
        for i in sub_자본총계_20:
            자본총계_20.append(i.text.strip())

        for i in sub_부채총계_17:
            부채총계_17.append(i.text.strip())
        for i in sub_부채총계_18:
            부채총계_18.append(i.text.strip())
        for i in sub_부채총계_19:
            부채총계_19.append(i.text.strip())
        for i in sub_부채총계_20:
            부채총계_20.append(i.text.strip())

        for i in sub_부채비율_17:
            부채비율_17.append(i.text.strip())
        for i in sub_부채비율_18:
            부채비율_18.append(i.text.strip())
        for i in sub_부채비율_19:
            부채비율_19.append(i.text.strip())
        for i in sub_부채비율_20:
            부채비율_20.append(i.text.strip())
        driver.quit()
    else:
        print('에러')
        driver.quit()



    return 종목명, 매출액_17, 매출액_18, 매출액_19, 매출액_20, 당기순이익_17, 당기순이익_18, 당기순이익_19, 당기순이익_20, ROA_17, ROA_18, ROA_19, ROA_20, ROE_17, ROE_18, ROE_19, ROE_20, EPS_17, EPS_18, EPS_19, EPS_20, BPS_17, BPS_18, BPS_19, BPS_20, DPS_17, DPS_18, DPS_19, DPS_20, PER_17, PER_18, PER_19, PER_20, PBR_17, PBR_18, PBR_19, PBR_20, 자산총계_17, 자산총계_18, 자산총계_19, 자산총계_20, 자본총계_17, 자본총계_18, 자본총계_19, 자본총계_20, 부채총계_17, 부채총계_18, 부채총계_19, 부채총계_20, 부채비율_17, 부채비율_18, 부채비율_19, 부채비율_20
#   ,영업활동_17,영업활동_18,영업활동_19,투자활동_17,투자활동_18,투자활동_19,재무활동_17,재무활동_18,재무활동_19

def craw_df(a):

    # ------------------------------
    종목명 = []
    매출액_17 = []
    매출액_18 = []
    매출액_19 = []
    매출액_20 = []

    당기순이익_17 = []
    당기순이익_18 = []
    당기순이익_19 = []
    당기순이익_20 = []

    ROA_17 = []
    ROA_18 = []
    ROA_19 = []
    ROA_20 = []

    ROE_17 = []
    ROE_18 = []
    ROE_19 = []
    ROE_20 = []

    EPS_17 = []
    EPS_18 = []
    EPS_19 = []
    EPS_20 = []

    BPS_17 = []
    BPS_18 = []
    BPS_19 = []
    BPS_20 = []

    DPS_17 = []
    DPS_18 = []
    DPS_19 = []
    DPS_20 = []

    PER_17 = []
    PER_18 = []
    PER_19 = []
    PER_20 = []

    PBR_17 = []
    PBR_18 = []
    PBR_19 = []
    PBR_20 = []

    자산총계_17 = []
    자산총계_18 = []
    자산총계_19 = []
    자산총계_20 = []

    자본총계_17 = []
    자본총계_18 = []
    자본총계_19 = []
    자본총계_20 = []

    부채총계_17 = []
    부채총계_18 = []
    부채총계_19 = []
    부채총계_20 = []

    부채비율_17 = []
    부채비율_18 = []
    부채비율_19 = []
    부채비율_20 = []

    dic_value = [종목명, 매출액_17, 매출액_18, 매출액_19, 매출액_20, 당기순이익_17, 당기순이익_18, 당기순이익_19, 당기순이익_20, ROA_17, ROA_18
        , ROA_19, ROA_20, ROE_17, ROE_18, ROE_19, ROE_20, EPS_17, EPS_18, EPS_19, EPS_20, BPS_17, BPS_18, BPS_19, BPS_20, DPS_17,
                 DPS_18, DPS_19, DPS_20, PER_17, PER_18, PER_19, PER_20, PBR_17, PBR_18, PBR_19, PBR_20, 자산총계_17, 자산총계_18, 자산총계_19,
                 자산총계_20, 자본총계_17, 자본총계_18, 자본총계_19, 자본총계_20, 부채총계_17, 부채총계_18, 부채총계_19, 부채총계_20, 부채비율_17, 부채비율_18,
                 부채비율_19, 부채비율_20]
    dic_key =  ['종목명',' 매출액_17',' 매출액_18',' 매출액_19',' 매출액_20',' 당기순이익_17',' 당기순이익_18',' 당기순이익_19',' 당기순이익_20',' ROA_17',' ROA_18',
                ' ROA_19',' ROA_20',' ROE_17',' ROE_18',' ROE_19',' ROE_20',' EPS_17',' EPS_18',' EPS_19',' EPS_20',' BPS_17',' BPS_18',' BPS_19',' BPS_20',' DPS_17',
                'DPS_18',' DPS_19',' DPS_20',' PER_17',' PER_18',' PER_19',' PER_20',' PBR_17',' PBR_18',' PBR_19',' PBR_20',' 자산총계_17',' 자산총계_18',' 자산총계_19',
                 '자산총계_20',' 자본총계_17',' 자본총계_18',' 자본총계_19',' 자본총계_20',' 부채총계_17',' 부채총계_18',' 부채총계_19',' 부채총계_20',' 부채비율_17',' 부채비율_18',
                 '부채비율_19',' 부채비율_20']

    for i in range(0, len(a)):
        for j in range(0, len(dic_value)):
            # 데이터 리스트가 들어간 리스트 생성
            try:
                dic_value[j].append(a[i][j][0])
            except:
                pass
    return dic_key,dic_value
