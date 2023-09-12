# enumerate()
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
# 0번째 색깔은 red
# 1번째 색깔은 orange

index = 0
for color in rainbow:
    print(f'{index+1}번째 색깔은 {color}')
    index += 1

for color in enumerate(rainbow):
    print(f'{color[0]}번째 색깔은 {color[1]}')

# enumerate() + 여러개 변수 할당
for index, color in enumerate(rainbow):
    print(f'{index}번째 색깔은 {color}')