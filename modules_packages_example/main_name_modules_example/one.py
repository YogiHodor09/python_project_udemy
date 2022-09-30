def func():
    print('Func in one.py file !')


print('TOP LEVEL IN ONE.PY')

def func1():
    pass


def func2():
    pass


if __name__ == '__main__':
    print('One.py is being run directly!')
    func1()
    func2()
