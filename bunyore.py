def number_to_word(num):
    vernacular_numbers = {
        1: 'emu', 2: 'bbiri', 3: 'ssatu', 4: 'nnya', 5: 'ttaano',
        6: 'mukaaga', 7: 'musanvu', 8: 'munaana', 9: 'mwenda', 10: 'kkumi',
        11: 'kumi na emu', 12: 'kumi na bbiri', 13: 'kumi na ssatu', 14: 'kumi na nnya', 15: 'kumi na ttaano',
        16: 'kumi na mukaaga', 17: 'kumi na musanvu', 18: 'kumi na munaana', 19: 'kumi na mwenda', 20: 'amakumi abbiri',
        30: 'asatu', 40: 'ana', 50: 'ataano'
    }
    
    if num in vernacular_numbers:
        return vernacular_numbers[num]
    
    if 21 <= num <= 50 and num % 10 != 0:
        tens_digit = num // 10 * 10
        ones_digit = num % 10
        return f"{vernacular_numbers[tens_digit]}-{vernacular_numbers[ones_digit]}"
    
    return "Number out of range (1-50)"

def word_to_number(word):
    vernacular_numbers = {
        'emu': 1, 'bbiri': 2, 'ssatu': 3, 'nnya': 4, 'ttaano': 5,
        'mukaaga': 6, 'musanvu': 7, 'munaana': 8, 'mwenda': 9, 'kkumi': 10,
        'kkumi na emu': 11, 'kkumi na bbiri': 12, 'kkumi na ssatu': 13, 'kkumi na nnya': 14, 'ttaano': 15,
        'kkumi na mukaaga': 16, 'kkumi na musanvu': 17, 'kkumi na munaana': 18, 'kkumi na mwenda': 19, 'amakumi abbiri': 20,
        'asatu': 30, 'ana': 40, 'ataano': 50
    }
    
    # Handling the case where the word contains a hyphen
    if '-' in word:
        tens_word, ones_word = word.split('-')
        return vernacular_numbers[tens_word] + vernacular_numbers[ones_word]
    
    return vernacular_numbers.get(word.lower(), "Invalid word")

# Testing the functions
while True:
    user_input = input("Enter a number (1-50) or a word: ")
    
    if user_input.isdigit():
        num = int(user_input)
        print(number_to_word(num))
    else:
        print(word_to_number(user_input))