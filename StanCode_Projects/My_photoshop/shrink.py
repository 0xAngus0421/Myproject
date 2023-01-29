"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str,
    :return img: SimpleImage,
    """
    img = SimpleImage(filename)
    blank_canvas = SimpleImage.blank(img.width // 2, img.height // 2)
    for x in range(blank_canvas.width):
        for y in range(blank_canvas.height):
            b_p = blank_canvas.get_pixel(x, y)
            img_p = img.get_pixel(x*2, y*2)
            b_p.red = img_p.red
            b_p.blue = img_p.blue
            b_p.green = img_p.green
    return blank_canvas


def main():
    """
    TODO:
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
