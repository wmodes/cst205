import math
from PIL import Image

# constant
target_color = (112, 231, 77) # greenscreen green
# adjusts sensitivity to picking up target_color
# in 3d color space max dist = 441
max_dist = 128


def color_distance(color_1, color_2):
    red_diff = math.pow((color_1[0] - color_2[0]), 2)
    green_diff = math.pow((color_1[1] - color_2[1]), 2)
    blue_diff = math.pow((color_1[2] - color_2[2]), 2)
    return math.sqrt(red_diff + green_diff + blue_diff)

def remove_chroma(a, b):
    dist = color_distance(target_color, b)
    if dist > max_dist:
        return(a)
    # calculate how much more the background should contribute
    # to the image vs the greenscreen image
    # think of this as a 0.0-1.0 alpha value for the 
    # greenscreen image
    # when the color dist is 0, f() = 0.0 (100% bkgd)
    # when the color dist is max_dist, f() = 1.0 (100% greenscrn)
    alpha = (dist / max_dist) ** 2
    # print("alpha:", alpha)
    # how to conbine the under and over layers based on the alpha
    # value took a little research
    # wikipedia said this is called alpha blending
    # https://en.wikipedia.org/wiki/Alpha_compositing
    # and stack overflow gave the super easy equation
    # https://stackoverflow.com/questions/746899/how-to-calculate-an-rgb-colour-by-specifying-an-alpha-blending-amount
    #    out = alpha * new + (1 - alpha) * old
    # so we use this equation on each pixel_diff
    new_pixel = (int(alpha * b[0] + (1 - alpha) * a[0]),
                 int(alpha * b[1] + (1 - alpha) * a[1]),
                 int(alpha * b[2] + (1 - alpha) * a[2]))
    return (new_pixel)

def chromakey(src, dest):
    offset_x = src.width - dest.width
    offset_y = src.height - dest.height
    dest_x = 0
    for src_x in range(offset_x, src.width):
            dest_y = 0
            for src_y in range(offset_y, src.height):
                # print("sx:", src_x, "sy:", src_y, "dx:", dest_x, "dy:", dest_y)
                src_pixel = src.getpixel((src_x, src_y))
                new_pixel = src_pixel
                if (dest_y < dest.height and dest_x < dest.width):
                    dest_pixel = dest.getpixel((dest_x,dest_y)) 
                    # print(dest_pixel, color_distance(dest_pixel, target_color))
                    # if this pixel isn't close to target color we show it
                    if color_distance(target_color, dest_pixel) > max_dist:
                        new_pixel = dest_pixel
                    else:
                        # if this pixel IS close to target color, 
                        # we show it inversely proportional to how close it is
                        new_pixel = remove_chroma(src_pixel, dest_pixel)
                src.putpixel((src_x,src_y), new_pixel)
                dest_y += 1
            dest_x += 1
    return src

background = Image.open("../images/bit.jpg")
greenscreen = Image.open("../images/dinosaur.png")

new_image = chromakey(background, greenscreen)
new_image.show()
