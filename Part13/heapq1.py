import heapq
nums = [1, 2, 3, 4, 5, 6, 7, 8]

print(max(nums), min(nums))
print(heapq.nlargest(3, nums)) # 큰 수 순서대로 3 개
print(heapq.nsmallest(3, nums)) # 작은 수 순서대로 3 개
print(heapq.nlargest(3, nums)[-1]) # 3번째로 큰 수
print(heapq.nsmallest(3, nums)[-1]) # 3번째로 작은 수