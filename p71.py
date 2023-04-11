# 二叉搜索树查询
import random

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

    def query(self, node, val): # 递归写查询
        if not node: # 节点不存在
            return None # 返回none
        elif val > node.data: # 值大于当前节点的值，往右子树找
            node = self.query(node.rchild, val) # 变量node是返回的node的赋值
        elif val < node.data: # 值小于当前节点的值，往左子树找
            node = self.query(node.lchild, val) 
        else: # val == node.data
            node = node # 值相等时返回节点
        return node
    def query_no_rec(self, val): # 非递归查询
        p = self.root  # p指针初始指向根节点
        while p: # 不是空树
            if val < p.data: # 值小于当前节点，往左找
                p = p.lchild # p指针下移
            elif val > p.data: # 值大于当前节点,往右找
                p = p.rchild # p指针往右下移
            else: # val == p.data
                return p # 退出循环
            return None

li = list(range(0,10,2)) # 0-9的偶数
random.shuffle(li)
tree = BST(li) # 创建树
node = tree.root
# print(node.data)
print(tree.query(node, 5)) # 递归
print(tree.query_no_rec(4)) # 非递归