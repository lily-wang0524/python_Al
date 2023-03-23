import time #调用时间模块

#时间装饰器
def cal_time(func): 
    def wrapper(*args, **kwargs): #函数参数不确定的时候，用*args和**kwargs，前者叫位置参数，后者叫关键字参数。
        t1 = time.time()
        result = func(*args, **kwargs) #运行被装饰的函数
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__,t2-t1)) #func.__name__装饰器的函数，表示函数名称
        return result
    
    return wrapper

def linear_search(li,val):
    for ind, v in enumerate(li): #使用enumerate函数，输出索引和值
        if v == val:  #当当前值等于所需要的值
            return ind  #返回索引
    else:
        return None
    

lis = [1,4,3,5,6,2]    
# cal_time(linear_search)(lis,3)  #等于@cal_time (语法糖)