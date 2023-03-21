def Fibonacci(n) :
        # write code here
    if n < 2:
        return n
    else:
        return (Fibonacci(n - 1) + Fibonacci(n - 2))
            
        
print(Fibonacci(4))

#ChatGpt提供解决方案
# def Fibonacci(n):
#    if n <= 1:
#        return n
#    else:
#        return (Fibonacci(n-1) + Fibonacci(n-2))

# print(Fibonacci(7))