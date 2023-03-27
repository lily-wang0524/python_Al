#选择排序的优化，使用原地排序
#根据无序区第一个位置的值与后续值的大小对比，若后面的值更小，则交换无序区第一个位置的数值。
def select_sort(li):
    for i in range(len(li)-1): #遍历n-1趟
        min_loc = i #无序区最小值的索引，暂定为i
        for j in range(i+1,len(li)): #无序区范围(i,n),但第一个值无需与本身对比，因此改为(i+1,n)
            if li[j] < li[min_loc]: #选出无序区中最小的值
                min_loc = j #变更无序区最小值的索引
            print(li)
        li[i],li[min_loc] = li[min_loc],li[i] #遍历一趟，交换无序区最小值到无序区的第一个位置
        # print(li)

lis = [3,4,2,1]
select_sort(lis)

