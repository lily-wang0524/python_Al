# 二叉搜索树——删除
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
    # 中序遍历
    def in_order(self,root):
        if root:  # root不为空，递归结束条件
            self.in_order(root.lchild) # 访问左孩子
            print(root.data, end = ',') # 打印本身
            self.in_order(root.rchild) # 访问右孩子

    def __remove_node_1(self, node): # 情况1：叶子节点
        # 判断是否为根节点
        if not node.parent: 
            self.root = None  # 根节点为None，即删除根节点
        if node == node.parent.lchild: # node为左孩子
            node.parent.lchild = None
        else: # node为右孩子
            node.parent.rchild = None
    
    def __remove_node_21(self,node): # 情况2.1：只有一个左孩子
        if not node.parent: # 根节点
            self.root = node.lchild # 根节点为node的左孩子
            node.lchild.parent = None # 左孩子的父亲为空
        elif node == node.parent.lchild: # node是父亲的左孩子
            node.parent.lchild = node.lchild # node父亲的左孩子变为node的左孩子
            node.lchild.parent = node.parent # node左孩子的父亲变为node的父亲
        else: # node是父亲的右孩子
            node.parent.rchild = node.lchild # node父亲的右孩子变为node的左孩子
            node.lchild.parent = node.parent # node左孩子的父亲变为node的父亲
    
    def __remove_node_22(self,node): # 情况2.2：只有一个右孩子
        if not node.parent: # 根节点
            self.root = node.rchild # 根节点为node的右孩子
            node.rchild.parent = None # 根节点没有父节点
        elif node == node.parent.lchild: # node是父亲的左孩子
            node.parent.lchild = node.rchild # node父亲的左孩子变为node的右孩子
            node.rchild.parent = node.parent # node右孩子的父亲变为node的父亲
        else: # node为父亲的右孩子
            node.parent.rchild = node.rchild # node父亲的右孩子变为node的右孩子
            node.rchild.parent = node.parent # node右孩子的父亲变为node的父亲
    
    def delete(self,val): # 删除操作（合并）
        if self.root: # 不是空树
            node = self.query_no_rec(val)  # 找到该节点 这步错了
            if not node: # node不存在
                return False
            if not node.lchild and not node.rchild: # 叶子节点
                self.__remove_node_1(node) # 情况1
            elif not node.rchild: # node只有左孩子
                self.__remove_node_21(node)  # 情况2.1
            elif not node.lchild: # node只有右孩子
                self.__remove_node_22(node) # 情况2.2
            else: # 情况3 即有左孩子又有右孩子
                # 找min_node，右子树的最小节点
                min_node = node.rchild # min_node在右子树上
                while min_node.lchild: # 直到没有左孩子
                    min_node = min_node.lchild  # min_node一直往左孩子移动，寻找
                node.data = min_node.data # 互换两者的值
                # 删除min_node
                if min_node.rchild: # 只有右孩子
                    self.__remove_node_22(min_node)
                else: # min_node为叶子节点
                    self.__remove_node_1(min_node)

tree = BST([1,4,2,5,3,8,6,9,7])
tree.in_order(tree.root)
print("")

# 删除值
tree.delete(4)
tree.delete(8)
tree.in_order(tree.root)