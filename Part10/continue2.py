# 1 2 4 5 7 8..
for n in range(1, 31):
    if n % 3 == 0:
        continue # skip
    print(n)

# while
n = 0
end = 31
while n < end:
    n += 1
    if n % 3 == 0:
        continue
    print(n)