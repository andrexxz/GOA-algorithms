# 1. Maximum Find Algorithm for 5 elements

def find_maximum(arr):
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val





# 5. Automatic Binary to English Conversion

def binary_to_text(binary_string):
    binary_values = binary_string.split()
    ascii_characters = [chr(int(b, 2)) for b in binary_values]
    return ''.join(ascii_characters)
