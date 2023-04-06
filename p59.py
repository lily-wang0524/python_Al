# 链表的插入与删除
class Node():

    def __init__(self, item):
        self.item = item
        self.next = None

# 尾插法
def creat_linklist_tail(li): # 参数li：列表
    head = Node(li[0]) # head节点指针，传入链表的第一个元素
    tail = head # 起始的tail指针也是第一个元素
    # tail = Node(li[0]) 
    for element in li[1:]: # 从列表的第2位开始加入到链表
        node = Node(element)  # 节点的值
        tail.next = node # 从链表尾部节点链接到该点
        tail = node  # 移动tail指针，指向新加入链表的node
    return  head # 从链表的头到尾输出，首先仍需返回head

# 遍历链表
def print_lk(lk): # 参数lk：链表
    while lk: # lk.next不为none
        print(lk.item, end = " ") # 打印值
        lk = lk.next  # 进入下一个点
