from re import sub

def encode(text):
    return sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1),
               text)

def decode(text):
    return sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)),
               text)