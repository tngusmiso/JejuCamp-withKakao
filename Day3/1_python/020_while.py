#-*- coding: utf-8 -*-

# 반복문(while, for)
while True:
    order = input('##')
    if order == 'exit':
        break   # 반복문 탈출
    elif order == 'name':
        print('suhyun')
    else:
        pass

x = 0
while x < 10:   # x는 0부터 9까지 (총 10번) 반복
    print('hello')
    x += 1