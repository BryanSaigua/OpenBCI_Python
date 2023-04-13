from time import localtime, asctime
import time
import datetime


a = datetime.datetime.now()
b = datetime.timedelta(seconds=8)
c = a + b

print(a)
print(c)
if datetime.datetime.now() == ( a + datetime.timedelta(seconds=8)):
    print(datetime.datetime.now())
    print('hola')

# print(a)
# print(c)