# filter(기준함수, 시퀀스데이터)
# for로 양수만 추출
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
new_nums = []
for n in nums:
    if n > 0:
        new_nums.append(n)
print(new_nums)


# 함수
def positive_number_list(nums):
    new_nums = []
    for n in nums:
        if n > 0:
            new_nums.append(n)
    return new_nums

nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
print(positive_number_list(nums))



# function + filter
def positive_number(n):
    return n > 0

nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
new_nums = filter(positive_number, nums) # 기준함수
print(list(new_nums))
new_nums = map(positive_number, nums) # 적용함수
print(list(new_nums))


# lambda + filter
nums = [-3, 3, -5, 0, 5, 1, 2, -1, -2]
new_nums = filter(lambda x: x > 0, nums) # 기준함수
print(list(new_nums))