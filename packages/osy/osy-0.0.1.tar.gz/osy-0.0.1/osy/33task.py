def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

# Пример списка количества предыдущих ремонтов машин "Жигули"
remonts = [5, 2, 8, 1, 6, 3]

sorted_remonts = merge_sort(remonts)

print("Количество предыдущих ремонтов машин 'Жигули' по убыванию:")
for remont in sorted_remonts:
    print(remont)