# Use python3
import random
'''
def maxPairwiseProductSlow(n, a):
    result = 0
    for i in range(0, n):
        for j in range(i+1, n):
            if a[i]*a[j] > result:
                result = a[i]*a[j]
    return result
'''

def maxPairwiseProductFast(n, a):
    max_index1 = 0
    for i in range(n):
        if (max_index1 == 0) or (a[i] > a[max_index1]):
            max_index1 = i
    max_index2 = 0
    for j in range(n):
        if (j != max_index1) and ((max_index2 == 0) or a[j] > a[max_index2]):
            max_index2 = j       
    result = a[max_index1] * a[max_index2]
    return result

def main():
    # Stress Test Implementation
    '''
    while True:
        n = random.randint(2, 10)
        a = random.sample(range(0, 100000), n)
        print(a)
        
        result1 = maxPairwiseProductSlow(n, a)
        result2 = maxPairwiseProductFast(n, a)
        
        if result1 == result2:
            print('OK')
        else:
            print('Wrong answer: ', result1, result2)
            return
        '''      
    n = int(input())
    a = [int(x) for x in input().split()]
    assert(len(a) == n)   
    result = maxPairwiseProductFast(n, a)
    print (result)
    
if __name__ == "__main__":
    main()