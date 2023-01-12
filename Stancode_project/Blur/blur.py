"""
File: blur.py
Name: Jacky Wu
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: The blurred image.
    :return: The image blurred another time.
    """
    n_img = SimpleImage.blank(img.width, img.height)

    for x in range(img.width):
        for y in range(img.height):
            n_img_p = n_img.get_pixel(x, y)
            count = 0
            sum_red = 0
            sum_green = 0
            sum_blue = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    nn_x = x+i
                    nn_y = y+j
                    if nn_x >= 0 and nn_y >= 0:
                        if nn_x <= img.width-1 and nn_y <= img.height-1:
                            count += 1
                            img_p = img.get_pixel(nn_x, nn_y)
                            sum_red += img_p.red
                            sum_green += img_p.green
                            sum_blue += img_p.blue
            avg_red = sum_red // count
            avg_green = sum_green // count
            avg_blue = sum_blue // count
            n_img_p.red = avg_red
            n_img_p.green = avg_green
            n_img_p.blue = avg_blue
    return n_img


def main():
    """
    pre-condition: The software will read one image from images file.
    post-condition: The software will blur original image first, then input that
                    blurred image to function called blur to do another processing.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
