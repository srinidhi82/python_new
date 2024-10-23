def get_user_info(user_info):
    return user_info

user_info = {'name':'John', 'Age':29,'hobbies':['teacher','coach','runner','volunteer']}

if 'coach' in user_info:
    print('Primary hobby is a coach')
    
#print(user_info['hobbies'][1])

x = {'a': 10, 'b': 20}
y = {'b': 30, 'c': 40}
x.update(y)
print(x)