def step1(a, b):
    if b == 1:
        return a

    if b != 1:
        return (a * step1(a, b - 1))


a = int(input("Write a number: "))
b = int(input("Write a step: "))

print(step1(a,b))