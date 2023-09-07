# str_func.py
# upper
text = "AbCdE"
text = text.upper()
print(text) # non-destructive 비파괴적

# lower
text = "AbCdE"
text = text.lower()
print(text) # non-destructive 비파괴적

# count
text = "aCbCdCeC".count('C')

# isalpha - 알파벳 체크
text = "10yearsold"
check = text.isalpha()
print(check)

# isnumeric - 숫자만 체크
text = "10yearsold"
check = text.isnumeric()
print(check)

# isalnum - 문자 숫자로만 체크
text = "10yearsold"
check = text.isalnum()
print(check)

# ljust, center, rjust
text1 = "hello".ljust(10) # 좌측 정렬
text2 = "hello".center(10) # 중앙 정렬
text3 = "hello".rjust(10) # 우측 정렬
print(text1, text2, text3, sep='-')

# len(v) - 길이 length
text = "abcdefg"
print(len(text))