"""온도 표기법
섭씨 Celsius C
화씨 Fahrenheit F
절대온도 Kelvin K

섭씨에서 화씨로 변환: F = C x 9/5 + 32
화씨에서 섭씨로 변환: C = (F - 32) x 5/9
섭씨에서 켈빈으로 변환: K = C + 273.15
켈빈에서 섭씨로 변환: C = K - 273.15
"""

def convert_temperature(t, unit):
    if unit == 'C':
        c = t
        f = c * 1.8 + 32
        k = c + 273.15
    elif unit == 'F':
        f = t
        c = (f - 32) / 1.8
        k = c + 273.15
    elif unit == 'K':
        k = t
        c = k - 273.15
        f = c*1.8 + 32
    else:
        c, f, k = False, False, False
    return c, f, k

# 함수 실행
t = 30
t_expr = convert_temperature(t, 'C')
print(t_expr)
t_expr = convert_temperature(t, 'F')
print(t_expr)
t_expr = convert_temperature(t, 'K')
print(t_expr)
