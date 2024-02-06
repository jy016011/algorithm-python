import sys
input = sys.stdin.readline
N = int(input())
primes = [2,3,5,7]
def is_prime(number):
    for num in range(2,int(number / 2 + 1)):
        if number % num == 0:
            return False
    return True

def dfs(number):
    if len(str(number)) == N:
        print(number)
        return
    else:
        for i in range(1,10,2):
            if is_prime(number * 10 + i):
                dfs(number * 10 + i)

for prime in primes:
    dfs(prime)
