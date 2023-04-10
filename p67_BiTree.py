from collections import deque # 队列模块

# 二叉树的简单实现
class BiTreeNode(): # 二叉树节点
    def __init__(self,data) -> None: 
        self.data = data
        self.lchild = None
        self.rchild = None

# 定位节点
a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("E")
f = BiTreeNode("F")
g = BiTreeNode("G")

# 节点关系链接
e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f

# 根节点
root = e

# 前序遍历
def pre_order(root):
    if root:   # root不为空
        print(root.data, end = ',')
        pre_order(root.lchild)  # 访问左孩子
        pre_order(root.rchild)  # 访问右孩子

pre_order(root) # 从e开始前序遍历
print("\n___________ ") # 分割线

# 中序遍历
def in_order(root):
    if root:  # root不为空，递归结束条件
        in_order(root.lchild) # 访问左孩子
        print(root.data, end = ',') # 打印本身
        in_order(root.rchild) # 访问右孩子

in_order(root) # 从e开始前序遍历
print("\n___________ ") # 分割线

# 后序遍历
def post_order(root):
    if root: # root不为空，递归结束条件
        post_order(root.lchild) # 访问左孩子
        post_order(root.rchild) # 访问右孩子
        print(root.data, end = ',') # 打印本身

post_order(root) # 从e开始前序遍历
print("\n___________ ") # 分割线

# 层次遍历——广度优先搜索
def level_order(root):
    queue = deque() # 新建队列
    queue.append(root) # 根节点入队
    while len(queue) > 0:  # 队列不空
        node = queue.popleft() # 节点出队
        print(node.data, end = ',') # 得到节点的值
        if node.lchild: # 节点的左孩子存在
            queue.append(node.lchild) # 左孩子进入队列
        if node.rchild: # 节点的右孩子存在
            queue.append(node.rchild) # 右孩子入队

level_order(root)