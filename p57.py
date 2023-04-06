# 链表实现
class Node():
    def __init__(self, item): # 初始化
        self.item = item
        self.next = None  # 最初不存在

# 传入节点数据
a = Node(1) #类实例化为对象
b = Node(2)
c = Node(3)

# 创建链接
a.next = b # a的下一个是b
b.next = c # b的下一个是c

print(a.item)
print(a.next.item)
print(a.next.next.item)
print(b.item)
print(b.next.item)