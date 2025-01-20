# 함수 (공백에 유의하기)
def say_hello():
  print("hello how r u?")

say_hello()

# parameters
def say_name(name="anonymous"):
  print("hello", name , "how are you?")

say_name("영률")
say_name()

# 계산기
def plus(a=0, b=0):
  print("덧셈 : ", a+b)

def minus(a=0, b=0):
  print("뺄셈 : " , a-b)

def multiply(a=0, b=0):
  print("곱셈 : ", a*b)

def divide(a=0, b=1):
  print("나눗셈 : ", a/b)

def power_of(a=0):
  print("제곱 : ", a*a)

plus()
minus()
multiply()
divide()
power_of()

plus(1,1)
minus(2,1)
multiply(2,2)
divide(4,2)
power_of(2)


# 문자열 포맷팅
my_name = "영률"
my_age = 26

print(f"안녕 내 이름은 {my_name}이고 나이는 {my_age}이야")


# if문
winner = 10

if winner > 10:
  print("10보다 큽니다.")
elif winner < 10:
  print("10보다 작습니다.")
else:
  print("10입니다.")

#입력 받기
age = input("How old are you?")

# 문자열 -> 숫자로 변환
int(age)

#변수의 타입 알기
type(age)