from random import randint

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

def high():
    A.sort()

def low():
    A.sort(reverse=True)

n = int(input("Введите размерность: "))
A = [randint(0, 100) for _ in range(n)]
chet = []
nechet = []

for i, val in enumerate(A):
    if i % 2 == 0:
        if val % 2 == 0:
            chet.append(val)
    else:
        if val % 2 != 0:
            nechet.append(val)

if len(chet) > len(nechet):
    high()
else:
    low()

merge_sort(A)
print("Отсортированный массив:", A)