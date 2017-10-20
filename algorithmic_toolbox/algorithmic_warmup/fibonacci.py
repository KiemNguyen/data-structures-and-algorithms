# Uses python3
'''
# Recursive solution, very slow
def calc_fib(n):
    if (n <= 1):
        return n
    return calc_fib(n - 1) + calc_fib(n - 2)
'''

def calc_fib(n):
    if (n <= 1):
        return n
    f = []
    # 0th and 1st number are 0 and 1
    f.append(0)
    f.append(1)

    for i in range(2, 46):
        f.append(f[i-1] + f[i-2])
    return f[n]
    
n = int(input())
print(calc_fib(n))