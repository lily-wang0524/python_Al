# 用队列求解迷宫问题
from collections import deque  # 调用队列模块
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

def print_r(path): # 根据元组最后一位索引值，找到前一个点元素，依次输出点的坐标。path为含有三维元组的列表
    curNode = path[-1] # 当前的元素为列表的最后一个元素，可以理解为终点为最后一个元素

    realpath = [] # 存储找到的路径所经过的点坐标

    while curNode[2] != -1: # 当前不是起点坐标，则循环，从终点开始往回倒。
        realpath.append(curNode[0:2]) # 循环最开始的curNode是终点，将其坐标添加到路径列表中，后续的元素为根据终点倒推的点
        curNode = path[curNode[2]] #curNode[2]是经过现在点的上一个点在path列表中的下标，根据下标找到该点的值，并替换curNode
    realpath.append(curNode[0:2]) # 结束while循环，当需要将起点加入到路径列表中，起点即为curNode[2]==-1的点
    realpath.reverse()  # 列表中数据的反转
    for n in realpath: #遍历打印路径的各点
        print(n) 

def maze_path_queue(x1,y1,x2,y2): # 输入起点和终点
    queue = deque() # 创建空队列
    queue.append((x1,y1,-1)) # 起点坐标进队，最后一位存储的是上一个点坐标在列表中的下标，起点前没有元素，指定为-1
    path = []  # 存储所有出队的点坐标

    while len(queue) > 0: # 队列不为空，队列空了就没路了
        curNode = queue.popleft() # 目前的点坐标为队列的队首，并出队
        path.append(curNode) # 出队的点加入到列表中

        if curNode[0] == x2 and curNode[1] == y2: # 现坐标点与终点坐标一致，找到终点
            print_r(path)  # 自定义函数，输出path列表中相应的值
            return True
        for node in dirs: # 遍历上下左右找下一个可以走的点
            nextNode = node(curNode[0],curNode[1])  #下一个点的坐标
            if maze[nextNode[0]][nextNode[1]] == 0:  # 下一个点坐标对应的值为0，路可以走
                queue.append((nextNode[0], nextNode[1], len(path)-1)) # 每次循环的curNode位于path的最末尾
                maze[nextNode[0]][nextNode[1]] = 2 # 标记该点已走
    else:
        print("no path")
        return False        
    
maze_path_queue(1,1,8,8)