# 堆排序的内置模块
import heapq
import random

li = list(range(20)) #生成随机列表
random.shuffle(li) #打乱顺序

#创建小根堆
heapq.heapify(li) 
print(li)

#实现堆排序
heap = []
for i in range(len(li)):
    x = heapq.heappop(li) # 每次取出小根堆对顶的元素
    heap.append(x)
print(heap)

#创建小根堆方法2
lis = list(range(10))
random.shuffle(lis)
heap2 = []
for i in lis:
    heapq.heappush(heap2, i) #将元素加入堆中

print(heap2)
