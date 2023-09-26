nums = [1, 2, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
basket = ['banana', 'banana', 'banana', 'apple', 'melon']

# set()
print(list(set(nums)))
print(list(set(basket)))

# collections Counter
from collections import Counter
print(Counter(nums))
print(Counter(basket)['banana'])
new_basket = dict(Counter(basket))
print(new_basket)

text = 'asadsfhaoisdhlkafnlgkn;lijasengadslksdlkasdf'
print(Counter(text).most_common(1))
new_text = Counter(text)
print(new_text)
print(new_text.most_common(1))