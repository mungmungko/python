# tuple function
RED = (255, 0, 0)
custom_color = [255, 0, 0]

# Built in Function
# 비파괴적인 연산에 대해서는 튜플도 가능
print(len(RED))
print(sorted(RED))
print(sorted(RED, reverse=True))

# method 차이
# tuple .index .count 비파괴적인 함수
# list 비파괴적/파괴적 함수