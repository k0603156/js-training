import numpy
from pandas import DataFrame
from matplotlib import pyplot
from pandas import read_excel

df = read_excel('data/시도별_월별_교통사고_20200327151519.xlsx')
print(df)
print('-' * 30)

col_list = list(df.columns)
print(col_list)
print('-' * 30)

df_traffic = df.filter(['시도별(1)','2017. 01', '2017. 02', '2017. 03', '2017. 04',
                        '2017. 05', '2017. 06', '2017. 07', '2017. 08',
                        '2017. 09', '2017. 10', '2017. 11', '2017. 12'])
print(df_traffic)
print('-' * 30)

col_list = list(df_traffic.columns)
print(col_list)
print('-' * 30)

df_traffic.drop(0, inplace=True)
print(df_traffic)
print('-' * 30)

df_traffic = df_traffic.rename(index=df_traffic['시도별(1)'])\
            .drop('시도별(1)', axis=1)
print(df_traffic)
print('-' * 30)

dic_month = {'2017. 01':'1월', '2017. 02':'2월', '2017. 03':'3월', 
             '2017. 04':'4월', '2017. 05':'5월', '2017. 06':'6월', 
             '2017. 07':'7월', '2017. 08':'8월', '2017. 09':'9월',
             '2017. 10':'10월', '2017. 11':'11월', '2017. 12':'12월'}

df_traffic.rename(columns=dic_month, inplace=True)
print(df_traffic)
print('-' * 30)

df_traffic = df_traffic.T
print(df_traffic)
print('-' * 30)

col_list = list(df_traffic.columns)
print(col_list)
print('-' * 30)

df_traffic.drop(['경기', '강원', '충북', '충남',
                 '전북', '전남', '경북', '경남', '제주', 
                 '광주', '대전', '울산', '세종'], axis=1, inplace=True)
print(df_traffic)
print('-' * 30)












