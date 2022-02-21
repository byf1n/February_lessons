# i = 0
# print(bool(i))
# print(type(i))

# 30 / 6 - type: 'float'  5.0
# 30 // 6 - type: 'int'   5
# 5 ** 5 - СТЕПИНЬ  25
# 17 % 4 - ОСТАЧА   1, бо (16 + 1)
#
# i = 9
# i += 9  # i = i + 9  ... /=, *=, %= и тд.
# print(i)
#
# if True:    # - if який завжди відпрацьовує /// if False: - нiколи
#     print('true')
# i = False
# if not i:
#     print('false')
# import time
# i = 1000
# while i > 0:
#     time.sleep(0.03)
#     print(i, '- 7 =', i-7)
#     i-=7
# else:
#     print('я умер прости(')

# for i in range(1000,7,-7):
#     print(i,'- 7 =',i-7)
# else:
#     print('у умер прости(')

# i='123456'
# print(i[-1  ])
# Create the dictionary of Bob's and Alice's salary data
salaries = [{'Alice': 10, 'Bob': 24000},
            {'Alice': 12, 'Bob': 48000},
            {'Alice': 9, 'Bob': 66000}]

# Use the sorted() function with key argument to create a new dic.
# Each dictionary list element is "reduced" to the value stored for key 'Alice'
sorted_salaries = sorted(salaries, key=lambda d: d['Alice'])

# Print everything to the shell
print(sorted_salaries)