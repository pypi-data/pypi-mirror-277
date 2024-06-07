def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] > right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def sort_repair_counts(arr):
    merge_sort(arr)
    return arr

# Пример списка количества предыдущих ремонтов машин "Жигули"
repair_counts = [3, 1, 5, 2, 4]

sorted_repair_counts = sort_repair_counts(repair_counts)
print("Отсортированное количество предыдущих ремонтов машин 'Жигули' по убыванию:")
print(sorted_repair_counts)