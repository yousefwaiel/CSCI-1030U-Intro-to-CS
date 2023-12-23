def mirror_insertion_sort(a):
    for j in range(len(a) - 2, -1, -1):
        key = a[j]
        i = j + 1
        while i < len(a) and a[i] < key:
            a[i - 1] = a[i]
            i += 1
        a[i - 1] = key
    return a

print(f'{mirror_insertion_sort([5,2,4,1,3]) = }')
print(f'{mirror_insertion_sort([1,2,3,4,5]) = }')
print(f'{mirror_insertion_sort([5,4,3,2,1]) = }')
print(f'{mirror_insertion_sort([]) = }')
print(f'{mirror_insertion_sort([-1]) = }')
