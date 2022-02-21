# l = [1,2,3,4,'last']
# print(l[0],l[-1])
# del l[-2]
# print(l)
# l2 = l.copy()
# l2[0] = 'first'
# l2.append('SECOND')
# l2.insert(0,'FIRST')
# print(l2)
# pop = l2.pop()
# print(pop)
# l2.remove('first')
# print(l2)
# l.extend(l2)
# print(l.index(1))
# l.reverse()
# print(l)

# cor = 2,2,2,5,2,2,2
# print(type(cor))
# print(cor.index(5))
# print(cor.count(2))
# print(*cor,sep=',')

# d = {
#     'name':'kirill',
#     'age':100
# }
# print(list(d.values()))
# name = 'kirill'
# age = 123
# weight = 80.9
# str = 'hello my name is {name} my age: {age} and mu weight: {weight}'.format(name=name,age=age,weight=weight)
# str = f'hello my name is {name} my age: {age} and mu weight: {weight}'
# print(str)

#################### distraction ##############################
# list = [1,2,3,4]
# a,*_,d = list
# print(a,_,d,sep=',')

# l1 = [1,2,3]
# l2 =[*l1]
# # print(l1 is l2)
# # print(l1 == l2)
#
# d = {
#     'name': 'bobik',
#     'age': 155,
#     'status': False
# }
#
# def test(**kwargs):
#     print(kwargs)
#
# test(**d)
# def decor(func):
#     def inner(*args,**kwargs):
#         print('*'*20)
#         func(*args,**kwargs)
#         print('*' * 20)
#     return inner
#
# @decor
# def greeting(name):
#     print('Hell0y', name)
#
# greeting('max')

# var  = 'global'
#
# def a():
#     var = 'a'
#     # print(locals())
#     def b():
#         # var = 'b'
#         # print(locals())
#         def c():
#             nonlocal var
#             var = 'b'
#             print(var)
#             # print(locals())
#         c()
#         print(var)
#     b()
#     print(var)
# a()

















