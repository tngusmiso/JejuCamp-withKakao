#-*- coding: utf-8 -*-

jeju = {'banana':1000, 'orange':300, 'apple':100}
print(type(jeju))
print(dir(jeju))

seoul = jeju.copy()
#listx = listy[:]   # 시작과 종료 값이 생략되어 있는 slicing
print('seoul:',id(seoul))
print('jeju:',id(jeju))

jeju['orange']=10000
print(seoul)
print(jeju.items())
