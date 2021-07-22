import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import math

df = pd.read_csv('data.csv')

df['freq'] = df['Outlet ID'].map(df['Outlet ID'].value_counts())


sales_purchase=[]
freq_purchase=[]
for i in range (9):
    i=i+1
    mask = df['freq'] == i
    freq1 = pd.DataFrame(df[mask])
    freq_purchase.append(freq1.shape[0])
    sales = freq1['Sales Value'].sum()
    sales_purchase.append(sales)
    print(f'Total number of outlets who purchased {i} times are: {freq1.shape[0]}')
    print(f'Total Sales for outlets who purchased {i} times: {sales}')
    print('\n')
    

plt.plot(freq_purchase, sales_purchase , color='c', label='sales')
plt.xlabel("Sales")
plt.ylabel("Freq")
plt.title("Sales and Frequency")
plt.legend()
plt.show()
