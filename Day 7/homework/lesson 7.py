def binary_to_english(binary_string):
    words = binary_string.split("    ")  # Words are separated by 4 spaces
    decoded_words = []
    
    for word in words:
        letters = word.split(".")  # Letters are separated by '.'
        decoded_word = "".join(
            chr(int(letter, 2) + 96) if 1 <= int(letter, 2) <= 26 else chr(int(letter, 2) + 38)
            for letter in letters
        )
        decoded_words.append(decoded_word)
    
    return " ".join(decoded_words)
