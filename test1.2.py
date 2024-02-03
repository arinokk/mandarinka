def is_prime(a):
    for i in range(2,a):
        if a%i==0:
           return False
    return True
def prime():
    for i in range(2,101):
        if is_prime(i):
            print(i)
prime()