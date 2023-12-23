# part 1

def is_vowel(char: str):
    if char in 'aeiou':
        return True
    else:
        return False


print(is_vowel('e'))


# part 2

def count_vowels_iter(sentence: str):
    count = 0
    for letter in sentence:
        if letter in 'aeiou':
            count = count + 1
    return count


print(count_vowels_iter("loud"))


# part 3

def count_vowels_rec(sentence: str):
    if len(sentence) == 0:
        return 0
    first_char = sentence[0]
    if first_char in 'aeiou':
        return 1 + count_vowels_rec(sentence[1:])
    else:
        return count_vowels_rec(sentence[1:])


print(count_vowels_rec('loud'))


# part 4

def my_reduce(values, start_value, op):
    currentValue = start_value
    for value in values:
        currentValue = op(currentValue, value)
    return currentValue


values = [1, 2, 3, 4, 5]
print(my_reduce(values, 0, lambda x, y: x + y))
