n = 10

def findPrimeNumbers(n):
    odd = []
    for i in n:
        if i % 2 == 1:
            odd.append(i)

    print(odd)


findPrimeNumbers(n)