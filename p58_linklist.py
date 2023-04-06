# 链表的创建与遍历
class Node():

    def __init__(self, item):
        self.item = item
        self.next = None

# 头插法
def creat_linklist_head(li): # 传入参数为列表
    head = Node(li[0]) # 最开始的head指针，指向列表第一个元素
    for element in li[1:]: # 从列表的第2个元素开始插入到列表中
        node = Node(element)  # 列表元素传入链表节点
        node.next = head # 将该节点与前一个点链接
        head = node # 指针head指向新插入的元素
    return head  # 返回链表的第一个元素

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

lk_head = creat_linklist_head([1,2,3])
lk_tail = creat_linklist_tail([1,4,8,6,3])
print_lk(lk_head)
print_lk(lk_tail)

# 删除链表元素
curNode = lk_tail # 定义目前的节点，是lk_tail的head
p = curNode.next # 要删除的点是curNode后面的元素
curNode.next = curNode.next.next #将curNode与p后面的元素连接
print_lk(lk_tail) 

# 插入链表
p = Node(6) # 插入的点
curNode = lk_head # curNode的值
p.next = curNode.next # p点尾部与插入位置的后一个元素连接
curNode.next = p # p点与前面的curNode连接
print_lk(lk_head)