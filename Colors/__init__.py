from colorsys import hsv_to_rgb


def colorwheel(theta, saturation=1, value=1):
    try:
        return hsv_to_rgb(theta / 360, saturation, value)
    except:
        return 0


def mixColors(a, b):
    try:
        c = []
        for i in range(3):
            c.append(int((a[i] + b[i]) / 2))
        return tuple(c)
    except:
        try:
            return (a * b) % 0xFFFFFF
        except:
            return (0, 0, 0)

class Colors():
    white = (255, 255, 255)
    lightGrey = (196, 196, 196)
    grey = (128, 128, 128)
    darkGrey = (64, 64, 64)
    lightBlack = (10, 10, 10)
    black = (0, 0, 0)

    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    yellow = (255, 255, 0)
    orange = (255, 128, 0)




charValues = {
    'a': 17,
    'A': 18,
    'b': 19,
    'B': 20,
    'c': 21,
    'C': 22,
    'd': 23,
    'D': 24,
    'e': 25,
    'E': 26,
    'f': 27,
    'F': 28,
    'g': 29,
    'G': 30,
    'h': 31,
    'H': 32,
    'i': 33,
    'I': 34,
    'j': 35,
    'J': 36,
    'k': 37,
    'K': 38,
    'l': 39,
    'L': 40,
    'm': 41,
    'M': 42,
    'n': 43,
    'N': 44,
    'o': 45,
    'O': 46,
    'p': 47,
    'P': 48,
    'q': 49,
    'Q': 50,
    'r': 51,
    'R': 52,
    's': 53,
    'S': 54,
    't': 55,
    'T': 56,
    'u': 57,
    'U': 58,
    'v': 59,
    'V': 60,
    'w': 61,
    'W': 62,
    'x': 63,
    'X': 64,
    'y': 65,
    'Y': 66,
    'z': 67,
    'Z': 68,
    '1': 69,
    '2': 70,
    '3': 71,
    '4': 72,
    '5': 73,
    '6': 74,
    '7': 75,
    '8': 76,
    '9': 77,
    '0': 78
}


def myhash(plaintext):

    acc = len(plaintext) + 88
    for char in plaintext:
        if char in charValues:
            v = charValues[char]
            acc *= v
            acc += 86793051
        else:
            acc += 37
        acc = acc % 0xFFFFFF
    
    return acc 

def textToHashedColor(text):
    return myhash(text)


def main():
    print(textToHashedColor('Hello'))
    print(textToHashedColor('Hello World'))


if __name__ == '__main__':
    main()