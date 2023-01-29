"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename:
    :return:
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    blank_canvas = SimpleImage.blank(original_mt.width, original_mt.height * 2)
    mirror_image = SimpleImage(filename)
    for x in range(mirror_image.width):
        for y in range(mirror_image.height):
            img_p = mirror_image.get_pixel(x, y)
            b_p1 = blank_canvas.get_pixel(x, y)
            b_p2 = blank_canvas.get_pixel(x, blank_canvas.height-1-y)
            b_p1.red = img_p.red
            b_p1.green = img_p.green
            b_p1.blue = img_p.blue

            b_p2.red = img_p.red
            b_p2.green = img_p.green
            b_p2.blue = img_p.blue
    return blank_canvas


def main():
    """
    TODO:
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
