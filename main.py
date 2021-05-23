lis = []


def factorial(n):
    fact = 1
    for num in range(2, n+1):
        fact = fact * num
    return (fact)


if __name__ == '__main__':
    for i in range(1, 50):
        lis.append(factorial(i))

    print("Factorial :: ", lis)

