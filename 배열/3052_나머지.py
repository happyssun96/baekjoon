numbers = []
for i in range(10):
    n = int(input())
    numbers.append(n % 42)
numbers = set(numbers)
print(len(numbers))
