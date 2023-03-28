import random
import cal_time

#插入排序
@cal_time
def insert_sort(li):
    #运行n-1趟，即需要抓牌的次数，其中i代表目前抓到的牌的索引
    for i in range(1,len(li)): 
        tmp = li[i] #需要插入的值，即手上刚抓的牌的值
        j = i - 1  #有序区的最后一张牌的索引，即手上已有牌的最后一张的下标
        #j=0时，表示有序区的第一张牌，无序区第一张牌对比的最后一个数值。
        #刚抓的牌比手上已有牌的最后一张小时，刚抓的牌需要插入到已有牌的左侧。
        while j >= 0 and tmp < li[j]: 
            li[j+1] = li[j]   #有序区的最后一张牌，往后挪一个位置，即索引值+1。
            j -= 1 #为了将无序区的第一张牌与有序区的其他牌做对比
        #1、跳出while循环，说明tmp>li[j]，位置应该在li[j]的右侧，因此tmp=li[j+1]
        #2、或者j=-1，tmp比第一张牌还小,因此tmp的索引为0，即j+1
        #其实就是在循环的末尾j=j-1，而此时条件不成立，那么成立的条件，需要j把1加回去。
        li[j+1] = tmp
    return li
       

lis = list(range(10000)) 
random.shuffle(lis) #随机打乱列表
insert_sort(lis)
print(lis)