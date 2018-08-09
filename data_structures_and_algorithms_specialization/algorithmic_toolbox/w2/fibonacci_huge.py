# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fibonacci_huge_fast(n, m):
    if n <= 1:
        return n

    arr = [0, 1]
    previous_mod = 0
    current_mod = 1

    for i in range(n - 1):
        temp_mod = previous_mod
        previous_mod = current_mod % m
        current_mod = (temp_mod + current_mod) % m
        arr.append(current_mod)
        if current_mod == 1 and previous_mod == 0:
            index = (n % (i + 1))
            return arr[index]
    return current_mod


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_fast(n, m))
