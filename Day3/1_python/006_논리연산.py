#-*- coding: utf-8 -*-

a = True    # 1
b = False   # 0

print(a and b)  # and는 *
print(a or b)   # or는 +
print(not a)

print(bool(1))
print(bool('hello'))
print(bool(' '))
print(bool(''))
print(bool(0))

for i in range(100):    # 0부터 99까지의 숫자 중에
    if i % 3 == 0  or i % 5 == 0:   # 3과 5의 배수를 출력
        print(i)