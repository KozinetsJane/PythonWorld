a = input("Ведите А: ")
a = int(a)
b = input("Введите В: ")
b = int(b)
sum = 0
for i in range(a, b + 1):
    sum += i
print(sum)