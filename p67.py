
# 树的实例：模拟文件系统
# 树是链式存储
class Node(): # 创建文件节点的类，及其属性（父节点，孩子节点）
    def __init__(self, name, type = "dir"):  # 节点初始属性,文件名，文件类型
        self.name = name  # 文件名
        self.type = type # 文件类型
        # 文件相互间关系
        self.children = [] # 孩子节点，孩子节点可以有很多，所以是列表
        self.parent = None # 父节点，父节点只有一个的，不一定需要有这个指向

class FileSystemTree(): # 创建文件根目录——数据结构（树）
    def __init__(self) -> None: # 树的属性
        self.root = Node("/")  # 树的根节点，类似于链表的head结点 

n = Node("hello")
n2 = Node("world")
n3 = Node("yoyo")
n.children.append(n2)
n.children.append(n3)
n2.parent = n
n3.parent = n
for nm in n.children:
    print(nm.name)
