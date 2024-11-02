def build_person(first_name, last_name, age=''):

    ''' This is a function which returns dictionary
    maps to the 2 parametrs function takes
    '''
    person = {'first':first_name, 'last':last_name}

    if age:
        person['age'] = age
    return person

musician = build_person('Taylor', 'Swift',30)
cricketer = build_person('Brian', 'Lara')
print(musician)
print(cricketer)