# 함수


def add(a, b):
    return a + b

result = add(5, 3)
print('result = ' , result)


# 함수 독스트링(docstrings) 사용
def multi(x,y):
    """multi(x,y): x*y 결과값을 리턴한다..."""
    return x*y

re = multi(5, 3)
print(multi.__doc__)
print('re=', re)

# 값을 여러 개 반환하기
def add_sub(a,b):
    return a+b, a-b
re = add_sub(30, 20)
print(type(re))
print('re=', re)


# 몫과 나머지 구하기
def get_qr(x,y):
    return(x//y, x%y)
result = get_qr(7,2)
print('get_qr(7,2) : 몫=', result[0], result[1])

# 언페킹 사용하기 :함수명.
x1 = [10, 20, 30]
print_params(*x1)

# 가변인수 (vraible argument) : 인수의 개수가 정해지지 않을 때
def print_args(*args):
    for e in args:
        print(e)

print_args('a', 'b', 'c')
print_args(10,20,30,40,50,60,70)
print_args(True)
