def count_letters_vowels_consonants(word):
    letter_count = 0
    vowel_count = 0
    consonant_count = 0

    vowels = set("aeiouAEIOU")

    for char in word:
        if char.isalpha():  
            letter_count += 1
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return letter_count, vowel_count, consonant_count


word = input("Type Something: ")

letters, vowels, consonants = count_letters_vowels_consonants(word)

print(f"Number of letters: {letters}")
print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")
