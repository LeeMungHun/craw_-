import pandas as pd

def save_xlsx(dic_key,dic_value,filename):
    dict_data={}
    for j in range(0, len(dic_key)):
        dict_data[dic_key[j]]=dic_value[j]
    df = pd.DataFrame(dict_data)

    df.to_excel('{}.xlsx'.format(filename), sheet_name='매출_당기순이익')