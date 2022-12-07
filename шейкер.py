massiv_sh = [0, -1, 5, -2, 3]
left = 0
right = len(massiv_sh) - 1

while left <= right:#если на опр чпсти массива перестановки не происходят->эта часть отсортирована
    for i in range(left, right, +1):#при 1 итерации минимальный элемент сдвигается на первую позицию, а максимальный
        if massiv_sh[i] > massiv_sh[i + 1]:#на 1 позицию вправо
            massiv_sh[i], massiv_sh[i + 1] = massiv_sh[i + 1], massiv_sh[i]
    right -= 1

    for i in range(right, left, -1):
        if massiv_sh[i - 1] > massiv_sh[i]:
            massiv_sh[i], massiv_sh[i - 1] = massiv_sh[i - 1], massiv_sh[i]
    left += 1

print(massiv_sh)
