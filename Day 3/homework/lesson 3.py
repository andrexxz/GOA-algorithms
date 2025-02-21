# Positional Number System Conversion

def convert_base(number, from_base, to_base):
    decimal = int(str(number), from_base)
    return format(decimal, 'X' if to_base == 16 else 'o' if to_base == 8 else 'b' if to_base == 2 else '')
