"""You have to generate a list of the first  fibonacci numbers, 0 being the first number. 
Then, apply the map function and a lambda expression to cube each fibonacci number and print the list."""

cube = lambda x: x ** 3


def fibonacci(n):
    l1 = [0, 1]
    if n == 0:
        l1.clear()
        return l1
    elif n == 1:
        l1.pop(1)
        return l1
    else:
        a = 0
        b = 1
        for i in range(2, n):
            c = a + b
            l1.append(c)
            a = b
            b = c
        return l1


num = int(input())
print(list(map(cube, fibonacci(num))))
