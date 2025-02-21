# 5. Automatic Binary to English Conversion

def binary_to_text(binary_string):
    binary_values = binary_string.split()
    ascii_characters = [chr(int(b, 2)) for b in binary_values]
    return ''.join(ascii_characters)
