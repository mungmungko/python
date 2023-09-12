# Conditional Breakpoint
for x in range(100):
    print(x)

# Conditional Breakpoint
member = ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']
for user in member.copy():
    if user[0] in ['A', 'a']:
         member.remove(user)
print(member)