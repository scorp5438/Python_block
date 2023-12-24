list1 = []
def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

for i in range(1, 50):
    list1.append(fib(i))
print(list1)
print(list1[5-1])
