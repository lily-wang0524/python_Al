# 二叉搜索树的用递归写插入函数

class BiTreeNode(): # 二叉树节点
    def __init__(self, data) -> None: # 属性
        self.data = data # 树的值
        self.lchild = None # 左孩子
        self.rchild = None # 右孩子
        self.parent = None # 父节点

# 二叉搜索树 binary search tree
class BST():
    def __init__(self): # 创建空树
        self.root = None # 根节点为空

    # 递归插入
    def insert(self, node, val): # node是指二叉树中当前指向的节点，初始一般为根节点，val是指插入的值
        if not node or node.data == val:  # 该节点不存在或节点的值与插入的值相同
            node = BiTreeNode(val) # 创建一个节点插入到树中（最后一步）或者是插入的值的节点直接与原节点相重合
        
        elif val < node.data:  # 插入的值小于当前节点的值
            # 往当前节点的左边插,当前节点的也就往左孩子找
            node.lchild = self.insert(node.lchild,val) # 左孩子为根节点的子树上，node.lchild(当前点的左孩子) = node(插入的节点)
            node.lchild.parent = node  # 连接父节点
        else:  # val > node.data
            node.rchild = self.insert(node.rchild,val) # 当前节点的右孩子是插入的节点
            node.rchild.parent = node # 连接父节点 

        return node # 返回

    
    # 前序遍历
    def pre_order(self, root):
        if root:   # root不为空
            print(root.data, end = ',')
            self.pre_order(root.lchild)  # 访问左孩子
            self.pre_order(root.rchild)  # 访问右孩子


tree = BST() 
node = BiTreeNode(10) # 树的根节点
# 插入数值
tree.insert(node,5) 
tree.insert(node,19) 
tree.insert(node,8)
tree.insert(node,3)
tree.pre_order(node)
