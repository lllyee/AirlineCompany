import pandas as pd
datafile='/Users/yiliu/lllyeeData/air_data.csv'
cleanedfile='/Users/yiliu/lllyeeData/data_cleaned.csv'
data=pd.read_csv(datafile,encoding='utf-8')
data = data[data['SUM_YR_1'].notnull()*data['SUM_YR_2'].notnull()]
index1 = data['SUM_YR_1'] != 0
index2 = data['SUM_YR_2'] != 0
index3 = (data['SEG_KM_SUM'] == 0) & (data['avg_discount'] == 0)
data = data[index1 | index2 | index3]
data.to_csv(cleanedfile)
