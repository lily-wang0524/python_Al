from collections import deque  # 双向队列模块

# 单向队列
que = deque() # 创建空队列
que.append(1) # 队尾进队
print(que.popleft()) # 队首出队

# 用于双向队列
que.appendleft(2) # 队首进队
print(que.pop()) # 队尾出队

# deque()参数应用
que2 = deque([0,1,2,3,4], 5) # 创建非空队列，且定义队列的规模为5
que2.append(5) # 队满，仍进队
print(que2.popleft()) # 队满进队后，原队首数据自动出队，现出队数据为1.

# deque()队满性质-另一端自动出队
# 读取文件的后几行，普通操作，读取整个文件，切片后几行，内存占比大
def tail(n):  # n是需要读取的数量
    with open('p52_test.txt', 'r') as f:  # with语句自动化关闭资源，不需要手动关闭
        q = deque(f, n) # 队列内容为文件f，队列规模为n，获取队尾的n列
        return q

for line in tail(4):
    print(line, end = "")