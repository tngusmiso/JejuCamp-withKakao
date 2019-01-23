#-*- coding: utf-8 -*-

print(range(10000))     # range(0,10)   #0부터 10개
print(type(range(10)))  # class 'range'

for i in range(10):
    print(i)
print('--------')

for i in range(2,10,2):
    print(i)
print('--------')

sumi = 0
for i in range(2,101,2):
    sumi += i
print(sumi)
print('--------')


#구구단
    # for i in range(1,10):
    #     print('{} x {} = {}'.format(2,i,2*i))

for j in range(2,10):
    for i in range(1,10):
        print('{} x {} = {}'.format(j,i,j*i))


# 구구단을 리스트로 만들기
l = []
for i in range(10):
    l.append(i)
l2 = [i for i in range(10)]
l3 = ['{} x {} = {}'.format(i,j,i*j) for i in range(2,10) for j in range(1,10)]

print(l)
print(l2)
print(l3)