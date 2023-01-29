"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage
# Controls the threshold of detecting green screen pixel
THRESHOLD = 1.05555
# Controls the upper bound for black pixel
BLACK_PIXEL = 310
def combine(bg, me):
    for x in range(bg.width):
        for y in range(bg.height):
            pixel_me = me.get_pixel(x, y)
            avg = (pixel_me.red + pixel_me.blue + pixel_me.green) // 3
            total = pixel_me.red + pixel_me.blue + pixel_me.green
            if pixel_me.green > avg * THRESHOLD and total > BLACK_PIXEL:
                pixel_bg = bg.get_pixel(x, y)
                pixel_me.red = pixel_bg.red
                pixel_me.blue = pixel_bg.blue
                pixel_me.green = pixel_bg.green
    return me

def main():
    """
    TODO:
    """
    fg = SimpleImage('image_contest/55688.jpg')
    bg = SimpleImage('image_contest/99999.jpeg')
    bg.make_as_big_as(fg)
    combined_img = combine(bg, fg)
    combined_img.show()
    #黑色部分請用RGB相加=100


if __name__ == '__main__':
    main()
