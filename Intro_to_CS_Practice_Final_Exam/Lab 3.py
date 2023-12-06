def main():
    # part 1

    global vowels
    pets = ['Spot', 'Boots', 'Mrs. Fluffington', 'Lenny', 'Bowser', 'Gina']
    count = 0
    pet_name_lengths = []

    for pet in pets:
        count = count + 1

    for i in  pets:
        pet_name_lengths.append(len(i))

    print(f'There are {count} pets in the list.')
    print(f'The word lengths of each pet name are {pet_name_lengths}')


    # part 2

    words = ['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']
    word_vowel_ratios = []
    vowels = 0

    for word in words:
        vowel_count = sum(1 for letter in word if letter in 'aeiou')
        consonant_count = len(word) - vowel_count

        if consonant_count != 0:
            ratio = vowel_count / consonant_count
            word_vowel_ratios.append(ratio)
        else:
            word_vowel_ratios.append(float('inf'))

    print(f"The vowel to consonant ratios of each word are {word_vowel_ratios}.")

    














if __name__ == "__main__":
    main()