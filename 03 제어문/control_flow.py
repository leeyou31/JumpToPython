# if 조건문
x = 11
if x == 10:
        print(10)
else:
    print('10이 아님')

if x > 10 and x !=1 and x <100:
    pass # TODO: 금주 완료 예정

x = 15
if x >= 10:
    print('10이상')
    if x == 15:
        print('15')
        if x == 20:
            print('20이다')
            
# 조건부 표현식 (conditional expression)
x = 5
if x == 10:
    y = x
else:
    y=0

y = x if x ==10 else 0


print ("""_자판기 메뉴_
1. 콜라
2. 사이다
3. 환타
""")

button =int(input("메뉴 번호를 누르세요:"))
if button == 1:
    print('콜라')
elif button == 2:
    print('사이다')
elif button == 3:
    print('환타')
else:
    print('잘못 누르셨어요')


i = 0
while True:
    print(i)
    i +=1
    if i == 10:
        break

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)


