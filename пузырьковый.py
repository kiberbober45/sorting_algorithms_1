n = int(input())
mas = list(map(int, input().split()))
count = 0  # количество изменений

for i in range(n - 1):
    for j in range(n - i - 1):  # оптимизация за счёт сокращения крайнего массива,
        if mas[j] > mas[j + 1]:
            count += 1
            mas[j], mas[j + 1] = mas[j + 1], mas[j]

print(*mas)
print(count)
