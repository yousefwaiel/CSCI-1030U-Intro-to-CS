def main():
    # part 1

    pets = ['Spot', 'Boots', 'Mrs. Fluffington', 'Lenny', 'Bowser', 'Gina']
    count = 0
    pet_name_lengths = []

    # TODO: YOUR CODE TO COUNT THE NUMBER OF PETS AND THE LENGTH OF PET NAMES GOES HERE

    for n in pets:
        count += 1

    for n in pets:
        pet_name_lengths.append(len(n))

    print(count)

    print(f'There are {count} pets in the list.')
    print(f'The word lengths of each word are {pet_name_lengths}.')

    # part 2

    words = ['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']
    word_vowel_ratios = []

    # TODO: YOUR CODE TO COUNT THE NUMBER OF VOWELS AND CONSONANTS IN EACH WORD TO CALCULATE THE RATIOS
    for word in words:
        vowel_count = sum(1 for letter in word if letter in "aeiou")
        constant_count = len(word) - vowel_count

        ratio = vowel_count / constant_count
        word_vowel_ratios.append(ratio)

    print(f"The vowel to constant ratio of each word are {word_vowel_ratios}")




if __name__ == "__main__":
    main()