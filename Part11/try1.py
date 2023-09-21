try:
    1/0 # ZeroDivisionError
except:
    pass # 아무것도 하지 않는다.

try:
    1/0 # ZeroDivisionError
except Exception as e:
    print(e)
print("정상 종료")

try:
    # 1 + "가" # TypeError
    int('가') # ValueError
except ValueError as ve:
    print(f'>>> {ve}')
except Exception as e:
    print(f'>>> {e}')

try:
    num = 3/0
    print(num)
except Exception as e:
    print(e)
finally:
    print('try문 종료 - 마무리 수행')

# 최종정리
try:
    # 수행, 시도할 코드
    pass
except ValueError:
    # ValueError 예외처리
    pass
except (ZeroDivisionError, TypeError):
    # ZeroDivisionError, TypeError 다중 예외 처리
    pass
except Exception:
    # 그 외 예외 + default 예외 처리
    pass
finally:
    # 무조건적으로 마무리코드로 수행은 되야한다!
    pass