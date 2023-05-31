def ssort(list):
    for i in range(len(list) - 1):
        minpos = i
        for j in range(i, len(list)):
            if list[minpos] > list[j]:
                minpos = j
        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp


nums = []
n = int(input('Enter the size'))
for i in range(n):
    nums.append(int(input('Enter the value')))
print('Your list is : ', nums)
ssort(nums)
print(nums)
