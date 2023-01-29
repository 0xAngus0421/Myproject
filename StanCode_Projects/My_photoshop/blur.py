"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


# def blur(old_img):
#     """
#     :param img:
#     :return:
#     """
#     blank_canvas = SimpleImage.blank(old_img.width, old_img.height)
#
#     for x in range(old_img.width):
#         for y in range(old_img.height):
#             red_sum = 0
#             green_sum = 0
#             blue_sum = 0
#             k = blank_canvas.get_pixel(x,y)
#             if x == 0 and y == 0: # 左上角
#                 a1 = old_img.get_pixel(x, y)
#                 a2 = old_img.get_pixel(x+1, y)
#                 a3 = old_img.get_pixel(x+1, y+1)
#                 a4 = old_img.get_pixel(x, y+1)
#                 red_sum = a1.red + a2.red + a3.red + a4.red
#                 green_sum = a1.green + a2.green + a3.green + a4.green
#                 blue_sum = a1.blue+a2.blue+a3.blue+a4.blue
#                 new_red1 = red_sum // 4
#                 new_green1 = green_sum // 4
#                 new_blue1 = blue_sum // 4
#                 k.red = new_red1
#                 k.blue = new_blue1
#                 k.green = new_green1
#
#             elif x == old_img.width-1 and y == 0:# 右上角
#                 b1 = old_img.get_pixel(x, y)
#                 b2 = old_img.get_pixel(x-1, y)
#                 b3 = old_img.get_pixel(x, y +1)
#                 b4 = old_img.get_pixel(x-1, y + 1)
#                 red_sum = b1.red + b2.red + b3.red + b4.red
#                 green_sum = b1.green + b2.green + b3.green + b4.green
#                 blue_sum = b1.blue + b2.blue + b3.blue + b4.blue
#                 new_red2 = red_sum // 4
#                 new_green2 = green_sum // 4
#                 new_blue2 = blue_sum // 4
#                 k.red = new_red2
#                 k.blue = new_blue2
#                 k.green = new_green2
#
#             elif x == 0 and y == old_img.height-1: #左下角
#                 c1 = old_img.get_pixel(x, y)
#                 c2 = old_img.get_pixel(x + 1, y)
#                 c3 = old_img.get_pixel(x+1, y-1)
#                 c4 = old_img.get_pixel(x , y - 1)
#                 red_sum = c1.red + c2.red + c3.red + c4.red
#                 green_sum = c1.green + c2.green + c3.green + c4.green
#                 blue_sum = c1.blue + c2.blue + c3.blue + c4.blue
#                 new_red3 = red_sum // 4
#                 new_green3 = green_sum // 4
#                 new_blue3 = blue_sum // 4
#                 k.red = new_red3
#                 k.blue = new_blue3
#                 k.green = new_green3
#             elif x == old_img.width-1 and y == old_img.height-1: #右下角
#                 d1 = old_img.get_pixel(x, y)
#                 d2 = old_img.get_pixel(x, y-1)
#                 d3 = old_img.get_pixel(x - 1,  y - 1)
#                 d4 = old_img.get_pixel(x-1, y)
#                 red_sum = d1.red + d2.red + d3.red + d4.red
#                 green_sum = d1.green + d2.green + d3.green + d4.green
#                 blue_sum = d1.blue + d2.blue + d3.blue + d4.blue
#                 new_red4 = red_sum // 4
#                 new_green4 = green_sum // 4
#                 new_blue4 = blue_sum // 4
#                 k.red = new_red4
#                 k.blue = new_blue4
#                 k.green = new_green4
#             elif old_img.width -1>= x >= 1 and y == 0:#上面
#                 e1 = old_img.get_pixel(x, y)
#                 e2 = old_img.get_pixel(x-1, y )
#                 e3 = old_img.get_pixel(x - 1, y + 1)
#                 e4 = old_img.get_pixel(x , y+1)
#                 e5 = old_img.get_pixel(x + 1, y+1)
#                 e6 = old_img.get_pixel(x + 1, y)
#                 red_sum = e1.red + e2.red + e3.red + e4.red +e5.red +e6.red
#                 green_sum = e1.green + e2.green + e3.green + e4.green +e5.green +e6.green
#                 blue_sum = e1.blue + e2.blue + e3.blue + e4.blue +e5.blue +e6.blue
#                 new_red5 = red_sum // 6
#                 new_green5 = green_sum // 6
#                 new_blue5 = blue_sum // 6
#                 k.red = new_red5
#                 k.blue = new_blue5
#                 k.green = new_green5
#             elif old_img.width -1>= x >= 1 and y == old_img.height -1 :# 下面
#                 f1 = old_img.get_pixel(x, y)
#                 f2 = old_img.get_pixel(x - 1, y)
#                 f3 = old_img.get_pixel(x - 1, y - 1)
#                 f4 = old_img.get_pixel(x, y - 1)
#                 f5 = old_img.get_pixel(x + 1, y - 1)
#                 f6 = old_img.get_pixel(x + 1, y)
#                 red_sum = f1.red + f2.red + f3.red + f4.red + f5.red + f6.red
#                 green_sum = f1.green + f2.green + f3.green + f4.green + f5.green + f6.green
#                 blue_sum = f1.blue + f2.blue + f3.blue + f4.blue + f5.blue + f6.blue
#                 new_red6 = red_sum // 6
#                 new_green6 = green_sum // 6
#                 new_blue6 = blue_sum // 6
#                 k.red = new_red6
#                 k.blue = new_blue6
#                 k.green = new_green6
#             elif x == 0 and old_img.height -1 >= y >= 1:
#                 g1 = old_img.get_pixel(x, y)
#                 g2 = old_img.get_pixel(x, y + 1)
#                 g3 = old_img.get_pixel(x + 1, y + 1)
#                 g4 = old_img.get_pixel(x, y-1)
#                 g5 = old_img.get_pixel(x + 1, y - 1)
#                 g6 = old_img.get_pixel(x + 1, y)
#                 red_sum = g1.red + g2.red + g3.red + g4.red + g5.red + g6.red
#                 green_sum = g1.green + g2.green + g3.green + g4.green + g5.green + g6.green
#                 blue_sum = g1.blue + g2.blue + g3.blue + g4.blue + g5.blue + g6.blue
#                 new_red7 = red_sum // 6
#                 new_green7 = green_sum // 6
#                 new_blue7 = blue_sum // 6
#                 k.red = new_red7
#                 k.blue = new_blue7
#                 k.green = new_green7
#             elif old_img.width -1 == x and old_img.height -1 >= y >= 1:
#                 h1 = old_img.get_pixel(x, y)
#                 h2 = old_img.get_pixel(x, y + 1)
#                 h3 = old_img.get_pixel(x - 1, y - 1)
#                 h4 = old_img.get_pixel(x, y - 1)
#                 h5 = old_img.get_pixel(x - 1, y + 1)
#                 h6 = old_img.get_pixel(x - 1, y)
#                 red_sum = h1.red + h2.red + h3.red + h4.red + h5.red + h6.red
#                 green_sum = h1.green + h2.green + h3.green + h4.green + h5.green + h6.green
#                 blue_sum = h1.blue + h2.blue + h3.blue + h4.blue + h5.blue + h6.blue
#                 new_red8 = red_sum // 6
#                 new_green8 = green_sum // 6
#                 new_blue8 = blue_sum // 6
#                 k.red = new_red8
#                 k.blue = new_blue8
#                 k.green = new_green8
#             else:
#                 i1 = old_img.get_pixel(x, y)
#                 i2 = old_img.get_pixel(x-1, y)
#                 i3 = old_img.get_pixel(x + 1, y)
#                 i4 = old_img.get_pixel(x-1, y - 1)
#                 i5 = old_img.get_pixel(x, y - 1)
#                 i6 = old_img.get_pixel(x + 1, y-1)
#                 i7 = old_img.get_pixel(x-1, y+1)
#                 i8 = old_img.get_pixel(x, y+1)
#                 i9 = old_img.get_pixel(x+1, y+1)
#                 red_sum = i1.red + i2.red + i3.red + i4.red + i5.red + i6.red+i7.red+i8.red+i9.red
#                 green_sum = i1.green + i2.green + i3.green + i4.green + i5.green + i6.green+i7.green+i8.green+i9.green
#                 blue_sum = i1.blue + i2.blue + i3.blue + i4.blue + i5.blue + i6.blue+i7.blue+i8.blue+i9.blue
#                 new_red9 = red_sum // 9
#                 new_green9 = green_sum // 9
#                 new_blue9 = blue_sum // 9
#                 k.red = new_red9
#                 k.blue = new_blue9
#                 k.green = new_green9
#     return blank_canvas

def blur(old_img):
    blurred = SimpleImage.blank(old_img.width, old_img.height)
    for x in range(old_img.width):
        for y in range(old_img.height):
            r_sum = 0
            g_sum = 0
            b_sum = 0
            count = 0
            for i in range(-1,2,1):
                for j in range(-1,2,1):
                    pixel_x = x + j
                    pixel_y = y + j
                    if 0 <= pixel_x < old_img.width:
                        if 0 <= pixel_y < old_img.height:
                            pixel = old_img.get_pixel(pixel_x,pixel_y)
                            r_sum += pixel.red
                            g_sum += pixel.green
                            b_sum += pixel.blue
                            count += 1
            new_pixel = blurred.get_pixel(x,y)
            new_pixel.red = r_sum / count
            new_pixel.green = g_sum / count
            new_pixel.blue = b_sum / count
    return blurred






def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
