def merge(a, b):  # слияние и сортировка двух списков методом двух указателей
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    while i < len(a):
        c.append(a[i])
        i += 1
    while j < len(b):
        c.append(b[j])
        j += 1

    return c


def splt(s):  # рекурсивный алгритм
    if len(s) == 1:
        return s
    mdl = len(s) // 2
    lf = splt(s[:mdl])
    rg = splt(s[mdl:])
    return merge(lf, rg)


print(splt([5, 2, 9, 6, 0, 3, 4, 1, 2]))
