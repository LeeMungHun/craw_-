import time
from multiprocessing import Pool,freeze_support
from selenium.common.exceptions import UnexpectedAlertPresentException

import code_list,craw,save_xlsx

if __name__ == "__main__":
    freeze_support()
    start_time = time.time()
    kospi=code_list.kospi_code_list('kospi.xlsx')
    kosdaq=code_list.kospi_code_list('kosdaq.xlsx')
    try:
        pool = Pool(processes=4) # 4개의 프로세스를 사용합니다.
        a=pool.map(craw.craw,kospi) # 코스피 133 137
        dic_key,dic_value=craw.craw_df(a)
        save_xlsx.save_xlsx(dic_key, dic_value, '코스피재무제표')
        print('코스피완료')

        b=pool.map(craw.craw,kosdaq) # 코스피 133 137
        dic_key,dic_value=craw.craw_df(b)
        save_xlsx.save_xlsx(dic_key,dic_value,'코스닥재무제표')
        print('코스닥완료')
    except UnexpectedAlertPresentException as e:
        print(e.__dict__["msg"])

