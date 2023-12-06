def insertion_sort(values):
    comparisons = 0
    for i in range(1, len(values)):
        key = values[i]
        j = i - 1
        while j >= 0 and key < values[j]:
            values[j + 1] = values[j]
            j -= 1
            comparisons += 1
        values[j + 1] = key

    return values, comparisons



unsorted = [4, 3, 7, 1, 8, 2]
sorted_list, num_comparisons = insertion_sort(unsorted)
print(sorted_list)
print(f'Number of comparisons: {num_comparisons}')

max_elements = 30
for length in range(1, max_elements):
    unsorted = list(range(length, 0, -1))
    sorted_list, num_comparisons = insertion_sort(unsorted)

    print(f'{num_comparisons:03d}', '*' * (num_comparisons // 10))


def binary_search(values, to_find, start_index, end_index):
    comparisons = 0

    while start_index <= end_index:
        mid_index = (start_index + end_index) // 2
        mid_value = values[mid_index]

        comparisons += 1

        if mid_value == to_find:
            return comparisons, True
        elif mid_value < to_find:
            start_index = mid_index + 1
        else:
            end_index = mid_index - 1

    return comparisons, False


max_elements = 10000000
for length in range(1, max_elements, 500000):
    values = list(range(1, (2 * length) + 1, 2))
    num_comparisons, found = binary_search(values, length + 1, 0, len(values) - 1)
    print(f'{num_comparisons:03d}', '*' * (num_comparisons // 4))

