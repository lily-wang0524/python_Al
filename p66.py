# 树的实例：模拟文件系统
# 树是链式存储
class Node(): # 创建文件节点的类，及其属性（父节点，孩子节点）
    def __init__(self, name, type = "dir"):  # 节点初始属性,文件名，文件类型
        self.name = name  # 文件名
        self.type = type # 文件类型
        # 文件相互间关系
        self.children = [] # 孩子节点，孩子节点可以有很多，所以是列表
        self.parent = None # 父节点，父节点只有一个的，不一定需要有这个指向

    def __repr__(self): # 内置函数，返回值
        return self.name  # 返回名字

class FileSystemTree(): # 创建文件根目录——数据结构（树）
    def __init__(self) -> None: # 树的属性
        self.root = Node("/")  # 树的根节点，类似于链表的head结点 
        self.now = self.root # now指针，当前目录

    def mkdir(self,name):  # 当前目录创建文件
        # 保证name以/结尾
        if name[-1] != "/": # name这个字符串的最后一位不是斜杠
            name += "/"  # 在name的最后加上斜杠
        new_dir = Node(name)  # 创建文件节点
        # 创建与当前文件夹的连接
        self.now.children.append(new_dir)  
        new_dir.parent = self.now 

    def ls(self):  # 展现当前目录下的所有子目录
        return self.now.children  # 返回子目录列表
    
    def cd(self,name): # 切换目录(到子目录)，支持向上返回
        # 判断是否为文件夹
        if name[-1] != "/":
            name += "/"

        if name == "../": #当前目录
            self.now = self.now.parent  # 返回目录到上级
            return
        # 找到和name相同的文件
        for child in self.now.children:
            if child.name == name: 
                self.now = child # 切换目录到child
                return  # 输出
        # 子目录中无该文件夹，报错
        raise ValueError("invaild dir")
    
tree = FileSystemTree() # 创建树
# 新建文件夹
tree.mkdir("Var/")
tree.mkdir("bin/")
tree.mkdir("usr/")
print(tree.ls()) # 展示当前子目录

# 切换到子目录
tree.cd("bin/")
tree.mkdir("python/") # 子目录中创建文件夹
print(tree.ls()) # 展示当前子目录

# 切换回上级目录
tree.cd("../")
print(tree.ls()) # 展示当前子目录

