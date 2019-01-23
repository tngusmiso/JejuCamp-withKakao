#-*- coding: utf-8 -*-

# 함수의 요소
def one():
    pass        # pass : 있으나 마나 한 빈 공간. def 되어있는 함수 밑에는 적어도 한 줄이 있어야 에러가 안남
print(one())    # return값 없음 = None

def two(x):
    return x*2  
print(two(10))

def three():
    print('hello')  # 이 부분이 먼저 출력됨
print(three())  # return값 없음 = None