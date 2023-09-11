# 팩토리얼
# 4! = 4 * 3!
# 3! = 3 * 2!
# 2! = 2 * 1

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)

print(factorial(10))