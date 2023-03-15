#汉诺塔问题——递归
class num():
    def __init__(self):
        self.x = 0 #x为每次运算
    def hanoi(self,n,a,b,c):  #第n块，a，b，c三根柱子
        if n>0:
            self.hanoi(n-1,a,c,b) #n-1块圆盘从a位置经过c移动到b
            print(f"moving from {a} from {c}") #第n块圆盘从a移到c
            self.x += 1 #移动一次计数
            self.hanoi(n-1,b,a,c) #n-1块圆盘从b位置经过a位置移到到c位置


len_n =num() #类实例化
len_n.hanoi(3,"a","b","c") #移动策略
print(len_n.x) #运行次数
