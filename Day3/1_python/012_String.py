#-*- coding: utf-8 -*-

a = 'hello'
name = 'suhyun'
nameTwo = 'Python'
nameThree = 'llSKHU CSE limsuhyunl'
val = 10

print(type(10)) # 데이터타입
print(dir(a))   # 가지고 있는 속성을 보여줌

# String.format
print('hello', name, '!!, my Name is', nameTwo)
print('hello {} !!, my Name is {}'.format(name, nameTwo))

# indexing
print(name[0])   # s
print(name[1])   # u
print(name[2:4]) # hy

# 변수명[start:stop:step]   
print(nameThree[2::2])  # slicing (인덱스2부터 시작, 끝까지, 2칸씩 건너뛴다)
print(nameThree[::-1])  # 순서 반전


print(nameThree.index('h'))
print(nameThree.count('u')) # 대문자는 미포함
print(nameThree.strip('l')) # 문자열의 양 끝에 존재하는 인자로 받아온 값을 없애준다.


