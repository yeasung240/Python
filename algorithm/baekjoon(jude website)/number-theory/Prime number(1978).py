# Finding the prime number
# Time complexitiy is n because it searches all the numbers from n

n = int(input())
def prime(n):
    for i in range(2,n):
        if not n%i:
            return False
    return True
prime(n)

# Finding prime number with a more efficient method. 
n = int(input())
import math
def prime(n):
    for i in range(2,int(math.sqrt(n)+1)): # it includes sqrt value (ex. 9)
        if not n%i:
            return False
    return True
prime(n)
