import time

class Decorator():
    def __init__(self,func): #func是被装饰的函数
        self.func = func

    def defer_time(self): #增加的功能函数
        time.sleep(5) #延时运行5秒
        print("延时结束了！")
    
    def __call__(self, *args, **kwds) : #实例化方法,调用功能函数
        self.defer_time()
        self.func() 

@Decorator
def fun1():
    print("延时之后我才开始执行。")

fun1()

#import time
 
class Decorator:
    def __init__(self, func):
        self.func = func
 
    def defer_time(self,time_sec):
        time.sleep(time_sec)
        print(f"{time_sec}s延时结束了")
 
    def __call__(self, time):
        self.defer_time(time)
        self.func()
 
@Decorator
def f1():
    print("延时之后我才开始执行")
 
f1(5)