# 栈的基本操作stack
class Stack():
    def __init__(self):
        self.stack = [] #初始为空列表
    
    def push(self,element): #压栈 element：压入的值
        self.stack.append(element) #往空列表中添加值。
        # 不需要return是因为append添加后，需要输出的是现列表，而现列表不需要特意使用return来输出

    def pop(self): # 出栈 
        return self.stack.pop()  # 用列表的删除函数pop()，并返回删除的值，得到出栈的数
    
    def get_top(self): # 取栈顶
        if len(self.stack) > 0: # 判断列表是否有数值
            return self.stack[-1]  # 返回列表的最后一个值
        else:
            None
    
stack = Stack() #类实例化
# 1.进栈
stack.push(2)
stack.push(6)
stack.push("hello")

# 2.出栈
print(stack.pop())

# 3.取栈顶
print(stack.get_top())