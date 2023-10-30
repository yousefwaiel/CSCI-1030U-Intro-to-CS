# Lab 04

# part 1

# TODO: YOUR is_vowel() FUNCTION GOES HERE

def is_vowel(char: str):
    condition = bool()
    if char in "aeiou":
        condition = True
    else:
        condition = False
    return condition


# part 2

# TODO: YOUR count_vowels_iter() FUNCTION GOES HERE

def count_vowels_iter(sentence: str):
    amount = int()
    for n in range(len(sentence)):
        if sentence[n] in "aeiou":
            amount += 1

    return amount

# part 3

# TODO: YOUR count_vowels_rec() FUNCTION GOES HERE




# part 4

# TODO: YOUR myreduce() FUNCTION GOES HERE
