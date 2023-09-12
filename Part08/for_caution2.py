# for문 도중 member의 remove > 넘어가는 데이터가 생김
member = ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']
for user in member.copy():
    if user[0] in ['A', 'a']:
        member.remove(user)
print(member)

# for문 도중 member의 append > 
member = ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']
for user in member[:]:
    if user[0] in ['A', 'a']:
         member.append(user)
print(member)