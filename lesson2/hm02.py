# написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
# - первый записывает в эту переменную запись
# - второй возвращает все записи
#
# запишите 5 тудушек
# и выведете все
# def notebook():
#     todo_list:list[str] = []
#
#     def save(new_todo:str) -> None:
#         nonlocal todo_list
#         todo_list.append(new_todo)
#
#     def delete(del_todo:str) -> None:
#         nonlocal todo_list
#         todo_list.remove(del_todo)
#
#     def all() -> list[str]:
#         print(todo_list)
#         return todo_list
#
#     return all,save,delete
# all,save,delete = notebook()
# save('eat')
# save('sleep')
# save('drink')
# all()
# delete('eat')
# all()

# вивести послідовність Фібоначі, кількість вказана в знінній,
#   наприклад: x = 10 -> 1 1 2 3 5 8 13 21 34 55
#   (число з послідовності - це сума попередніх двох чисел)
# fib1 = fib2 = 1
#
# n = int(input('n: '))
#
# print(fib1, fib2,end=' ')
#
# for i in range(2, n) :
#     fib1, fib2 = fib2, fib1 + fib2
#     print(fib2, end=' ')


# порахувати кількість парних і непарних цифр числа,
#   наприклад: х = 225688 -> п = 5, н = 1;
#          х = 33294 -> п = 2, н = 3
# par = 0
# nepar = 0
# x = input('num: ')
# for i in x:
#     if int(i) %2 ==0:
#         par = par + int(i)
#     else:
#         nepar = nepar + int(i)
#
# print('sum par: ',par,'sum nepar: ',nepar)

# прога, що виводить кількість кожного символа з введеної строки, наприклад: st = 'as 23 fdfdg544'  # введена строка
# 'a' -> 1  # вивело в консолі
# 's' -> 1
# ' ' -> 2
# '2' -> 1
# '3' -> 1
# 'f' -> 2
# 'd' -> 2
# 'g' -> 1
# '5' -> 1
# '4' -> 2
# arr = []
# st = 'as 23 fdfdg544'
# for i in st:
#     arr.append(i)
# for i in arr:
#     print(f'{i} - ',arr.count(i))









