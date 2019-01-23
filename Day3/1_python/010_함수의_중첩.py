#-*- coding: utf-8 -*-

def one(X):
    def two(Y):
        return Y ** X
    return two

f = one(2)
print(f(3)) # print(one(2)(3))
print(f(4)) # print(one(2)(4))


suhyun = print
suhyun("hello")


'''
저는 카카오에 주식을 1000주 보유하고 있습니다. 현재 카카오의 주가는 10만원이에요.
제가 보유하고 있는 재산을 계산하는 함수를 만들어 주세요.
input : 1000, 100000
output : 1억
'''

kakaostock = int(input('주식 수를 입력하세요: '))
kakaoprice = int(input('주가를 입력하세요: '))

def kakao(stock, price):
    return stock * price
print(kakao(kakaostock,kakaoprice))

def kakao2():   # 인자로 전달하지 않아도 외부에 선언된 변수를 사용할 수 있다.
    return kakaostock * kakaoprice
print(kakao2())