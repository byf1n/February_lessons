def decor(func):
    count = 0
    def wrapper():
        nonlocal count
        func()
        count += 1
        print(f'{count}')
    return wrapper

@decor
def func1():
    print('func1')
@decor
def func2():
    print('func2')

func1()
func2()
func1()
func2()
func1()
func2()
func2()
func2()
func2()
func1()