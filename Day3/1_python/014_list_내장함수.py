#-*- coding: utf-8 -*-

l = [100,200,300,400]

print(type(l))
print(dir(l))

l.append(500)
l.append(100)

# l.clear() # 빈 배열로 만든다.
# l.copy()  # 배열을 복사

print(l)
print(l.count(100))

l.extend([100,200,300]) # 리스트를 통째로 추가
print(l)
print(l.index(100)) # 처음 만나는 100의 인덱스를 반환

l.insert(3,10000)   # 인덱스 3자리에 10000을 삽입
print(l)

print(l.pop())  # 맨 마지막의 값을 꺼내서 없애줌. 꺼낸 값을 반환 
print(l)

l.remove(100)   # 처음 만난 100을 삭제 
#del l[2]
print(l)

l.sort()    # l 자체를 정렬
print(l)

l.reverse() # 순서를 뒤집는다.
print(l)

print(sorted(l))    # l을 직접 변경하지 않고, 정렬된 값만을 반환 (python 내장 함수)