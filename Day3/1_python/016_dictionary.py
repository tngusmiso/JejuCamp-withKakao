#-*- coding: utf-8 -*-

# dict{ key : value }
d = {'name':'suhyun', 'age':23, 'height':165}
print( d['name'] )  # 키 값으로 value를 찾을 수 있다.

'''
딕셔너리는
    1. 순서가 없다.
    2. 키 값은 중복될 수 없다.
    3. 값을 추가하거나 삭제할 수 없다.
'''

d['money'] = 100
print(d)
