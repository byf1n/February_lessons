#ClassWork



# стврорити меню в якому потрібно реалізувати:
#
# 1) додававання нового юзера
# 2) вивід всіх юзерів
# 3) вивід всіх юзерів за віком
# 4) видалення юзера по id
# 5) заміна статуса юзера на протилежний
# 6) вихід з меню
#
# приклад юзера {'id':1,'name':'Max', 'age':35,'status':False}

users_list = []
listik = []
con = True
while con == True:
    print('1) додававання нового юзера')
    print('2) вивід всіх юзерів')
    print('3) вивід всіх юзерів за віком')
    print('4) видалення юзера по id')
    print('5) заміна статуса юзера на протилежний')
    print('6) вихід з меню')
    num = int(input('what num:'))
    if num == 1:
        id = int(input('id: '))
        name = input('name: ')
        age = int(input('age: '))
        status = bool(input('status: '))
        new_user = {f'id':{id},'name':{name},'age':{age},'status':{status}}
        users_list.append(new_user)
    elif num == 2:
        print(users_list)
    elif num == 3:
        print(sorted(users_list, key=lambda item:item['age'], reverse=True))
    elif num == 4:
        delUser = int(input('which user: '))
        del users_list[{delUser}]
    elif num == 5:
        print('change status')
    elif num == 6:
        con = False
    else:
        print('erorro!!!')




