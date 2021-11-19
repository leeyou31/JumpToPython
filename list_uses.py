# 리스트 조작하기

# - 요소 추가(append, extend, insert)

a = ['a', 'b', 'c']
b = ['d', 'e']
a.extend(b)
print('a.extend(b) = {0}'.format(a))


a = ['a', 'b', 'c']
b = ['d', 'e']
a.extend(b)
print('a + b = {0}'.format(a+b))

a.append(b)
print('a.append(b) = {0}'.format(a))


a = ['a', 'b', 'c']
b = ['d', 'e']

a.insert(len(a),b)
print('a.insert(len(a), b) = {0}'.format(a))



# - 리스트가 비어 있는가? 아닌가?
li = []
print("li = {0}".format(li))

if not li:
    li.append(100)


# -리스트의 할당과 복사
a= list(range(3))
print('a = {0}'.format(a))

b=a
print(id(a), id(b))
print(a is b)
b.append(3)
print('a={0}'.format(a))
print('b={0}'.format(b))

a=[0,0,0]
b= a.copy()
print(f'a is b = {a is b}')
print(id(a), id(b))
b[2] = 99
print(a,b)



# 리스트에 map() 사용하기
# map은 리스트의 요소를 지정된 함수로 처리해준다.
li = list(map(float,range(10)))
print('li=', li)

a, b = map(input("두 정수입력:").split())
print('a+b = ' , a+b)

