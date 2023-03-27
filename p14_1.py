#选择排序
def select_sort_simple(li):
    li_new = [] #新建空列表
    for i in range(len(li)): #循环n次
        min_val = min(li) #找到每次列表中的最小值
        li_new.append(min_val) #将找到的最小值添加到新列表中
        li.remove(min_val) #移除现列表中的最小值
    return li_new

li = [3,5,8,2,4,7,6]
print(select_sort_simple(li))

