
# Finding the prime number
# Time complexitiy is n because it searches all the numbers from n

n = int(input())
def prime(n):
    for i in range(2,n):
        if not n%i:
            return False
    return True
prime(n)
