# 시작 숫자
num_7 = 0

# 빈칸
number_of_legs = 0 #snake_case - python
NumberOfLegs = 0 #CamelCase - python class
numberOfLegs = 0 #mixedCase 잘 쓰지 않는다

# 소문자 대문자
# 보통 변하지 않는 상수 값은 대문자로 함
GRAVITY = 9.8
name = "머쓱이"
age = 10

# 한글
name = "스펜서"
age = 99
print(name, age)

# 특수문자 _ 허용
# [] {} ()

# 파이썬 예약된 용어
# if for 등을 변수명으로 사용하면 안됨
import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
  'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
    'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# 자주 사용하는 함수
# print = "text"

# 보너스 - 함수 변수에 저장하기
출력 = print
출력("와 이게 되네?")