# Uses python3
import sys
'''
def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10
'''

def get_fibonacci_last_digit_fast(n):
    if (n <= 1):
        return n
    f = []
    # 0th and 1st number are 0 and 1
    f.append(0)
    f.append(1)

    for i in range(2, n+1):
        f.append((f[i-1] % 10) + (f[i-2] % 10))
    return f[n] % 10


if __name__ == '__main__':
    #input = sys.stdin.read()
    n = int(input())
    print(get_fibonacci_last_digit_fast(n))