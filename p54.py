# 迷宫问题
#迷宫
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x, y: (x+1, y),
    lambda x, y: (x, y+1),
    lambda x, y: (x-1, y),
    lambda x, y: (x, y-1)
] # lambda函数，匿名函数，是简单函数的简写版本
  # 向下，右，向上，左顺序寻找

# 迷宫求解
def maze_path(x1,y1,x2,y2): #（x1，y1）表示初始起点，(x2,y2)表示终点坐标
    stack = []  # 创建空栈,栈内存储元组，即各点坐标
    stack.append((x1, y1)) #起点位置进栈，(x1,y1)为起点坐标的元组
    
    while len(stack) > 0: #栈不空时，栈空没有路
        curNode = stack[-1] #栈顶位置，当前节点的坐标（x，y）
        if curNode[0] == x2 and curNode[1] == y2:  # 当前节点为终点
            for p in stack: #遍历输出坐标点
                print(p)
            return True
        # 当前坐标的四个方向，(x+1,y)/(x-1,y)/(x,y+1)/(x,y-1),坐标移动
        for dir in dirs:   # dir为一个lambda式,输出为元组
            nextNode = dir(curNode[0],curNode[1]) # dir的lambda式需要x，y两个参数，curNode[0]=x,curNode[1]=y
            # 下一个节点能走，即值为0
            if maze[nextNode[0]][nextNode[1]] == 0: #二维列表取数用maze[x][y]，x=nextNode[0],y=nextNode[1]
                stack.append(nextNode)  # 进栈
                maze[nextNode[0]][nextNode[1]] = 2 # 表示该点走过了
                break  # 只要找到一个可以走的位置就结束for循环
        else: # for循环结束后仍然没有找到可前进的路
            stack.pop() # 出栈
        
    # while循环中没有return，则未找到路    
    print("没有路")
    return False

maze_path(1,1,8,8)
