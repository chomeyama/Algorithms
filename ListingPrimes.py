""" エラトステネスの篩 """
def Eratosthenes(n):
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5)+1, 2):
        print()
        print(i, i//2-1)
        if sieve[i//2-1]:
            k = i + i
            for j in range(i*3, n, k):
                print("(", j, j//2-1, ")", end = " ")
                sieve[j//2-1] = False
    return [2] + [i*2-1 for i in range(1, n//2) if sieve[i]]

""" なんか早いやつ """
def primes(n):
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1, int(n**0.5)//3+1):
        if sieve[i]:
            k = 3*i+1|1
            sieve[k*k//3::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
            sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2, 3] + [3*i+1|1 for i in range(1, n//3-correction) if sieve[i]]

print(Eratosthenes(100))
print(primes(100))
