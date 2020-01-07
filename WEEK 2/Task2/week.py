import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Question1
data1 = pd.read_csv(r"C:\Users\HP\Desktop\Python1code\test.csv")
size1 = data1.size
print(size1)
data1 = data1.replace('?', np.nan)
print(data1.head())

#Question2
data2 = pd.read_csv(r"C:\Users\HP\Desktop\Python1code\train.csv")
size2 = data2.size
print(size2)
data2 = data2.replace('?',np.nan)
print(data2.head())

#Question3
data3 = pd.read_csv(r"C:\Users\HP\Desktop\Python1code\Book.csv")
plt.suptitle("Stock price Comparison 2007-2017")


a=np.array([2007,2009,2011,2013,2015,2017])
b=np.array(data3['MSFT'])[:5]
plt.subplot(2,3,1)
plt.plot(a,b)
plt.title('MSFT')


a=np.array([2007,2009,2011,2013,2015,2017])
b=np.array(data3['GOOG'])[:6]
plt.subplot(2,3,2)
plt.plot(a,b)
plt.title('GOOG')


a=np.array([2007,2009,2011,2013,2015,2017])
b=np.array(data3['SBUX'])[:6]
plt.subplot(2,3,3)
plt.plot(a,b)
plt.title('SBUX')


a=np.array([2007,2009,2011,2013,2015,2017])
b=np.array(data3['ADBE'])[:6]
plt.subplot(2,3,4)
plt.plot(a,b)
plt.title('ADBE')


a=np.array([2007,2009,2011,2013,2015,2017])
b=np.array(data3['NFLX'])[:6]
plt.subplot(2,3,5)
plt.plot(a,b)
plt.title('NFLX')


a=np.array([2007,2009,2011,2013,2015,2017])
b=np.array(data3['ORCL'])[:6]
plt.subplot(2,3,6)
plt.plot(a,b)
plt.title('ORCL')
plt.show()
