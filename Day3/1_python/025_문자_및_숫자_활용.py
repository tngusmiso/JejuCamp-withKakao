#-*- coding: utf-8 -*-

l = [100,200,300]
print(max(l))
print(min(l))

print(chr(65))  # 숫자 -> 문자 (아스키코드)
print(ord('A')) # 문자 -> 숫자 (아스키코드)

print(bin(11))      # 2진법 
print(oct(11))      # 8진법
print(hex(11))      # 16진법

# 출력될 때는 문자열. 맨앞에 0b가 붙기 때문에 지우고 싶으면 슬라이싱 한다.
print(bin(11)[2:])  
print(oct(11)[2:])
print(hex(11)[2:])
