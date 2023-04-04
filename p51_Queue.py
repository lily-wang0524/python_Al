# 实现简单的队列
class Queue(): # 队列,类的括号里填的是继承关系
    def __init__(self,size): #初始化属性设置
        self.queue = [0 for i in range(size)]  # 创建初始列表，列表长度确定且都为0
        self.size = size # 队列规模
        self.rear = 0 # 队尾指针初始位置
        self.front = 0 # 队首指针初始位置

    def push(self, element): # 入队
        if not self.is_filled():  # 队列不满才能入队
            self.rear = (self.rear + 1) % self.size  # 找到插入队列的位置
            self.queue[self.rear] = element # 填入元素
        else:
            # 报错，raise()函数，手动设置异常，IndexError异常指列表索引超出范围
            raise IndexError("Queue is filled.") 

    def pop(self): # 出队
        if not self.is_empty(): # 队列不空才能出队
            self.front = (self.front + 1) % self.size  # 找到队尾最后一个元素要删除的位置，最开始front指针指向空位
            return self.queue[self.front]  # 返回这个值，不需要pop操作，后续插入的数值可直接覆盖，pop的时间复杂度较高
        else:
            raise IndexError("Queue is empty.")
        
    def is_empty(self):  # 队列是否为空
        return self.rear == self.front  # 队尾与队首的位置相同时，队列为空，即两者相同时，返回True

    def is_filled(self): # 队满
        return self.front == (self.rear + 1) % self.size # 队尾往前一步是队首的时候，将返回True
    
queue = Queue(10) #队列实例化

# 1.入队
for i in range(9):
    queue.push(i)


# 2.出队
print(queue.pop())

# # 3.队空或队满判断
print(queue.is_empty())
queue.push(9)
print(queue.is_filled())
