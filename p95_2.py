# 分数运算
class Fraction(): # 分数运算的类
    def __init__(self,a,b): # 传入参数属性，a，b是数字
            self.a = a # 分子
            self.b = b # 分母
            x = self.gcd(a, b) # 分子分母的最大公约数，x不是属性，不需要加self
            # 约分，分子和分母都除以最大公约数
            self.a = a / x # 分子化简
            self.b = b /x # 分母化简

            
    def gcd(self, a, b): # a,b最大公约数
        while b > 0:
                r = a % b
                a = b 
                b = r
        return a
    
    def lcm(self, a, b): # 最小公倍数
          # 12 ，16 最大公约数为4
          # LCM = (12/4) * (16/4) * 4
          x = self.gcd(a, b)
          return a / x * b # (a / x) * (b / x) * x 的化简
    
    def __add__(self, other): # 加法,是内置函数
          # 1/12 + 1/20
          # 分母化成最小公倍数
          a = self.a # 分子
          b = self.b # 分母
          c = other.a # 分子
          d = other.b # 分母
          den = self.lcm(b, d) # 找到分母的最小功倍数，作为分母
          num_a = den / b * a  # 换算分子a
          num_c = den / d * c  # 换算分子c
          num = num_a + num_c # 分子相加
          return Fraction(num, den) # 分子分母化简
    
    def __str__(self) -> str: # 类中的字符串显示的函数
          return "%d/%d" %(self.a, self.b) # %d表示十进制的整数
    
f = Fraction(30,16) # 实例化类
print(f)

a = Fraction(1, 12) # 1/12 实例化类
b = Fraction(1, 20) # 1/20 实例化类
print(a + b)