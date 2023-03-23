def binary_search(li,val):  #li是列表，val是需要查找的值
    left = 0  #left初次索引
    right = len(li) - 1 #right的初次索引
    while left <= right:
        mid = (left + right) // 2 #向下取整
        if li[mid] == val:
            return mid
        elif li[mid] > val: #待查值在mid的左侧
            right = mid - 1  #更新right的值
        else:  #li[mid] < val 待查值在mid右侧
            left = mid + 1
        
    else:  #对应最后一个if
        return None 

#验证代码   
lis = [1,2,3,4,5,6,7,8]
bin = binary_search(lis,3)
print(bin)