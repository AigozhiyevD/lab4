# Task 1

def generator(N):
    for i in range(N):
        yield i ** 2

N = 10
for j in generator(N):
    print(j)

# Task 2

def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input())
print(",".join(str(num) for num in even_numbers(n)))

# Task 3

def div34(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
for num in div34(n):
    print(num)

# Task 4

def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input())
b = int(input())

for square in squares(a, b):
    print(square)

# Task 5

def degradaciya(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())

for num in degradaciya(n):
    print(num)