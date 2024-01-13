import random

def merge(l):
    if len(l) > 1:
        mid = len(l) // 2
        lh = l[:mid]
        rh = l[mid:]
        merge(lh)
        merge(rh)
        i = j = k = 0
        while i < len(lh) and j < len(rh):
            if lh[i] < rh[j]:
                l[k] = lh[i]
                i += 1
            else:
                l[k] = rh[j]
                j += 1
            k += 1
        while i < len(lh):
            l[k] = lh[i]
            i += 1
            k += 1
        while j < len(rh):
            l[k] = rh[j]
            j += 1
            k += 1
    return l


def insort(l):
    for i in range(1, len(l)):
        key = l[i]
        j = i - 1
        while j >= 0 and key < l[j]:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = key
    return l


new = []
for i in range(10):
    new.append(random.randint(0, 999))
print('Unsorted list : \n', new)
print('Sorting using merge sort : \n', merge(new))
new = []
for i in range(10):
    new.append(random.randint(0, 999))
print('Unsorted list : \n', new)
print('Sorting using insertion sort : \n', insort(new))
