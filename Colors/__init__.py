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
