def inssort(list):
    for i in range(1, len(list)):
        temp = list[i]
        j = i - 1
        while j >= 0 and list[j] > temp:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = temp
    return list


try:
    l = []
    n = int(input('Enter number of elements\n'))
    print('Enter all the ', n, ' elements')
    for i in range(n):
        l.append(int(input()))
    print('Original list : ', l)
    sl = inssort(l)
    print('Sorted list : ', sl)
except Exception:
    print('No valid data entered\n')
