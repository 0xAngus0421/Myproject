"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img:
    :param figure_img:
    :return:
    """
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            img_a = figure_img.get_pixel(x, y)
            bigger = max(img_a.red, img_a.blue)
            if img_a.green > bigger * 2:
                img_b = background_img.get_pixel(x, y)
                img_a.red = img_b.red
                img_a.green = img_b.green
                img_a.blue = img_b.blue

    return figure_img


def main():
    """
    TODO:
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
