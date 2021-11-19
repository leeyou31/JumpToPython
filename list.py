# 리스트 생성 : [,,,]

print(type([]))

score = [80, 90, 100]
print(score)

person = ['james', 17, 173.5, True]
print(person)

score =[]
#score[0] = 98 !! be aware of this part...
score.append(100)
print(score)

# -range()를 사용하여 리스트 생성

r=range(0, 10)

li=list(range(10))
print('li1 = {0}'.format(li))

li = list(range(5,12))
print(f'list(range(5,12)) = {li}')


li =list(range(-4, 10, 2))
print('list(range(-4, 10, 2))={0}'.format(li))

li = list(range(10, 0, -1))
print('list(range(-4, 10, 2))={0}'.format(li))


# - in 사용
index = list(range(10))
print('index={0}'.format(index))
print(5 in index)
print(11 in index)
print('n' in "Python")
print('a' in ('a', 'b', 'c'))

# - '+' 연산자 사용
a = ['a', 'b', 'c']
b = ['d', 'e']
print('a+b = {0}'.format(a + b ))
print("Hello, " + "world")


li = [1,2,3]
print(li *3)

# - 인덱스 사용
print(li)
print(li[0])
print(li.__getitem__(2))



# - 값 식제

del li[2]
print(li)

org1 = list(range(0,10))
print(org1)


# - 요소 삭제하기(del list [], pop, remove, clear)
a= ['a', 'b', 'c']
print(a)
a.pop()
print(f'a.pop()={a}')
a.pop(0)
print(a)
li = ['a', 'b', 'x']
li.remove('x')
print(li)


#반복문(for, while) 사용
li = list(range(10))
print("li={0}".format(li))

for i in li:
    print(i, end='')


for c in 'Hello' :
    print(c, end='.')

print()

i=0

a= [34, 52, 92, 14, 13]
for idx in range(len(a)):
    a[idx] *=100
print(a)


a = list(range(10))
print('a={0}'.format(a))
    
b = [i*100 for i in range(10)]
print('b={0}'.format(b))

c = [i for i in range(10) if i %2==0]
print('c={0}'.format(c))

c = [i for i in range(10) if i %2!=0]
print('c={0}'.format(c))


# -구구단 출력 리스트 만들기

li=[]
for i in range(2, 10):
    for j in range(1, 10):
        li.append(i*j)
print(li)

print()

