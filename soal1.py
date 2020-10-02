import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('202009020838.csv')

#soal 1 a
container = df['timestamp'].str.split(" ",n = 1, expand = True)
tgl = container[0].str.split("/",n = 0, expand = True)
df['tanggal'] = tgl[1]
df['tanggal'] = df['tanggal'].astype(int)
df['tgl'] = container[0]
df['tgl'] = pd.to_datetime(df['tgl'])
df['waktu'] = container[1]
print(df)
data1 = df.loc[(df['sensor_id']==265) & (df['tanggal'] == 31)] 
data2 = df.loc[(df['sensor_id']==271) & (df['tanggal'] == 31)] 
data3 = df.loc[(df['sensor_id']==277) & (df['tanggal'] == 31)]
data4 = df.loc[(df['sensor_id']==283) & (df['tanggal'] == 31)]
data1.plot(x='waktu', y='total', kind='bar')
data2.plot(x='waktu', y='total', kind='bar')
data3.plot(x='waktu', y='total', kind='bar')
data4.plot(x='waktu', y='total', kind='bar')
# plt.show()

#soal1 b
data1_1 = df.loc[(df['sensor_id']==265) & (df['tgl']>='08/17/2020') & (df['tgl']<='08/31/2020')] 
data2_1 = df.loc[(df['sensor_id']==271) & (df['tgl']>='08/17/2020') & (df['tgl']<='08/31/2020')] 
data3_1 = df.loc[(df['sensor_id']==277) & (df['tgl']>='08/17/2020') & (df['tgl']<='08/31/2020')]
data4_1 = df.loc[(df['sensor_id']==283) & (df['tgl']>='08/17/2020') & (df['tgl']<='08/31/2020')]
# print(data1_1)
data1_1.plot(x='tgl', y='total', kind='bar')
data2_1.plot(x='tanggal', y='total', kind='bar')
data3_1.plot(x='tanggal', y='total', kind='bar')
data4_1.plot(x='tanggal', y='total', kind='bar')
plt.show()
