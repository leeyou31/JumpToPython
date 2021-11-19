# 집합(set)자료형 : { 값, , ,}
# 요소의 순서가 정해져 있지 않다(unordered)
# 요소의 중복(X)

s = {1,5,2,2,3,3,7}
print('s=', s)

print(8 in s)


s = set('apple')
print('s=', s)

s = set('자바211기 화이팅!')
print('s=', s)

s = set()
print('type(s)', type(s))

a = {1,2,3,4,5,6}
b = {3,4,5,6,7,8}
print('a=', a)
print('b=', b)

s = a | b
print('a | b = ', a | b )
s = set.union(a,b)

s = a & b
s = a - b


# set 조작하기
a = {1,2,3,4}
print('a=', a)


# 로또 번호 생성기 만들기

import random
lotto=random.sample(range(1,46),6)
print(lotto)


import random
print(int(random.random()*45)+1)
print('______________________lotto gen program______________')
print()
print('몇 세트를 만드시겠습니까?')
set_num = int(input('정수입력:'))
print('_________________________')

for n in range(set_num):
    lotto=set()
    while len(lotto) < 6:
        lotto.add(int(random.random()*45) +1)
    print(lotto)
            
