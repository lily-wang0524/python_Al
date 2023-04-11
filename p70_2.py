# 二叉搜索树普通办法写插入函数

class BiTreeNode(): # 二叉树节点
    def __init__(self, data) -> None: # 属性
        self.data = data # 树的值
        self.lchild = None # 左孩子
        self.rchild = None # 右孩子
        self.parent = None # 父节点

# 二叉搜索树 binary search tree
class BST():
    def __init__(self, li=None): # 创建树
        self.root = None # 根节点为空
        # 创建二叉搜索树
        if li: 
            for val in li:
                self.insert_no_dec(val) # 循环插入值

    def insert_no_dec(self,val): # 非递归插入
        p = self.root # 创建指针p，p起始指向根节点
        if not p: # p指向节点为空，空树，
            self.root = BiTreeNode(val)  # 创建根节点
            return 
        
        while True: # 循环
            if val < p.data: # 插入值小于p指向节点的值
                if p.lchild: # 左孩子节点存在
                    p = p.lchild # 指针移动至新的节点
                else: # 左孩子不存在
                    p.lchild = BiTreeNode(val) # 插入值
                    p.lchild.parent = p # 连接父节点
                    return  # 结束循环，返回
            
            elif val > p.data: # 插入值大于p指向节点的值
                if p.rchild:  # 右孩子存在
                    p = p.rchild # 指针移动至新节点
                else: # 右孩子不存在
                    p.rchild = BiTreeNode(val) # 插入值
                    p.rchild.parent = p # 连接父节点
                    return # 结束循环，返回
            else: # val == p.data
                return # 不用插入
            
    # 前序遍历
    def pre_order(self,root):
        if root:   # root不为空
            print(root.data, end = ',')
            self.pre_order(root.lchild)  # 访问左孩子
            self.pre_order(root.rchild)  # 访问右孩子

    # 中序遍历
    def in_order(self, root):
        if root:  # root不为空，递归结束条件
            self.in_order(root.lchild) # 访问左孩子
            print(root.data, end = ',') # 打印本身
            self.in_order(root.rchild) # 访问右孩子

    # 后序遍历
    def post_order(self, root):
        if root: # root不为空，递归结束条件
            self.post_order(root.lchild) # 访问左孩子
            self.post_order(root.rchild) # 访问右孩子
            print(root.data, end = ',') # 打印本身
    
tree = BST([4,6,7,9,2,1,3,5,8]) # 对象实例化

# 遍历二叉树
tree.pre_order(tree.root)
print("") 
tree.in_order(tree.root)
print("")
tree.post_order(tree.root)
