#递归-print在函数之前
def func3(x):
    if x > 0:
        print(x)
        func3(x-1)

print(func3(3))

#递归-print在函数之后
def func4(x):
    if x > 0:
        func4(x-1)
        print(x)

print(func4(3))