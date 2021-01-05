import pandas as pd

def kospi_code_list(kospi_filename):
    df1 = pd.read_excel(kospi_filename, engine='openpyxl')
    # 코드만 리스트에 넣기
    kospi_list = df1['종목코드']

    ## 좌축 0 을 찾기생성       9900 >> 009900
    kospi = []
    for a in kospi_list:
        a = str(a)
        kospi.append(a.zfill(6))

    return kospi

def kosdaq_code_list(kosdaq_filename):
    df2 = pd.read_excel(filename2, engine='openpyxl')
    # 코드만 리스트에 넣기
    kodaq_list = df2['종목코드']

    ## 좌축 0 을 찾기생성       9900 >> 009900
    kosdaq = []
    for a in kodaq_list:
        a = str(a)
        kosdaq.append(a.zfill(6))

    return kosdaq
