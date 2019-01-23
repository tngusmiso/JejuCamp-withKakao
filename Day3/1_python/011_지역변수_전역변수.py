#-*- coding: utf-8 -*-

# 지역변수
x = 10
def one(a):
    a = a + 10
    return a
x = one(x)
print(x)

# 전역변수
i = 10
def suhyun():
    global i    # 함수 밖의 변수값을 변경하기 위해서 global을 써야함.(잘 안씀)
    i += 10
suhyun()
print(i)