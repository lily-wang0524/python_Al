#带有参数的装饰器
def funA(fn):
    # 定义一个嵌套函数
    def funC(*args, **kwargs):
        fn(*args, **kwargs)
        print("running!")
    return funC

@funA
def funB(arc):
    print("funB():", arc)

@funA
def funD(name,arc):
    print(name,arc)

funB("Hello.")
funD("funD","world!")

#作为装饰器的函数带有参数
def funcA(type): #传送装饰器的参数
    def funcB(fn): #定义装饰器
        def funcC(*args,**kwargs):  #传送执行函数的参数
            if type == "文件":
                print("文件：funcA")
            else:
                print("其他：funcA")
            return fn(*args, ** kwargs)
        return funcC
    return funcB

@funcA("文件")
def funcD(a,b):
    print("学习进度：", a, b)

if __name__ == '__main__':
    funcD(30, 60)
