n = 10

def findPrimeNumbers(n):
    odd = []
    for i in range(n):
        if i % 2 == 1 and i % 3 != 0 and i % 5 != 0:
            odd.append(i)

    


findPrimeNumbers(n)