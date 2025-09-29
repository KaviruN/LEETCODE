n = 100

def findPrimeNumbers(n):
    odd = []
    for i in range(n):
        if i % 2 == 1:
            odd.append(i)

    print(odd)


findPrimeNumbers(n)