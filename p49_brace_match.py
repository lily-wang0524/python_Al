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
    def is_empty(self): # 栈为空
        return len(self.stack) == 0  # 列表长度为0，为空栈

# 括号匹配问题
def brace_match(str): # str为字符串
    stack = Stack() # 创建空栈
    match = {')': '(', ']': '[', '}': '{'} # 符号匹配字典
    for ch in str: # 遍历字符串里的每个字符
        if ch in {'(','[','{'}:  # '(','[','{'的集合
            stack.push(ch)  # 进栈
        else: # 符号不是'(','[','{'
            if stack.is_empty(): # 栈是空的，没有左边的括号入栈
                return False  #报错
            elif stack.get_top() == match[ch]: #栈顶值对比
                stack.pop()  # 出栈
            else: #栈顶值与括号不匹配 stack.get_top != match[ch]
                return False
    
    if stack.is_empty(): #遍历结束字符串，栈为空
        return True  
    else: #栈不为空
        return False

print(brace_match('{([[]({}[]())])}'))
print(brace_match('[]{}([})'))

