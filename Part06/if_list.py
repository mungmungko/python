# if list, tuple, sequence - in 연산자
# case1 soccer, baseball, baketball
sport = 'soccer'
if sport == 'soccer' or sport == 'baseball' or sport == 'basketball':
    print("조사항목포함")
else:
    print("비조사항목")

# case2 list count
sport = 'soccer'
check_sports = ['soccer', 'baseball', 'basketball']
if check_sports.count(sport):
    print("조사항목포함")
else:
    print("비조사항목")

# case 3 in 연산자
sport = 'soccer'
check_sports = ['soccer', 'baseball', 'basketball']
if sport in check_sports:
    print("조사항목포함")
else:
    print("비조사항목")