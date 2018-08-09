# Uses python3
# Find the minimum number of coins with denominations 1, 5, 10 that changes m
import sys

def get_change(amount):
    coins = [10, 5, 1]
    result = []
    for coin in coins:
        while amount >= coin:
            amount = amount - coin
            result.append(coin)
    return len(result)

if __name__ == "__main__":
    n = int(input())
    print(get_change(n))