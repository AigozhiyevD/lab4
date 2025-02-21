import math

# task 1

def conv(degree):
    return degree * (math.pi / 180)

degree = float(input())
radian = conv(degree)

print(radian)

# task 2

def traparea(height, base1, base2):
    return 0.5 * (base1 + base2) * height

height = float(input())
base1 = float(input())
base2 = float(input())

area = traparea(height, base1, base2)

print(area)

# task 3

def regpoarea(n, side):
    return (n * side**2) / (4 * math.tan(math.pi / n))

n = int(input())
side = float(input())

area = regpoarea(n, side)

print(area)

# task 4

def parallelogram_area(base, height):
    return base * height

base = float(input())
height = float(input())

area = parallelogram_area(base, height)

print(area)