# import time
# intial=time.time()
# k=0
# while(k<45):
#     print('this is shadab bhai')
#     k+=1
# print('while loop ran in:',time.time()-intial,'secs')
# initial2=time.time()
# for i in range(45):
#     print('this is shadab bhai')
# print('for loop ran in:',time.time()-initial2,'secs')
# localtime=time.asctime(time.localtime(time.time()))
# localtime = time.asctime()
# print(localtime)
# from datetime import date
# today=date.today()
# print(today)
from datetime import datetime

# Getting Datetime from timestamp
date_time = datetime.fromtimestamp(1887639476)
print("Datetime from timestamp:", date_time)
