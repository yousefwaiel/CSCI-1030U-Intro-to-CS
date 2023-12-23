def sequential_search(values, to_find):
    comparison_count = 0
    for i in range(len(values)):
        comparison_count += 1
        if values[i] == to_find:
            return True, comparison_count
    return False, comparison_count


for size in [10,100,1000,10000]:
    values = list(range(size))
    result, comp_count = sequential_search(values, -1)
    print(f'{size:06d}:', '*' * (comp_count//100))