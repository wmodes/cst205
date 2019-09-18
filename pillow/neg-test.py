from PIL import Image
im = Image.open('images/teacher.jpg')

def negative_image(pixel):
    # return tuple(map(lambda a : 255 - a, pixel))
    return (255-pixel[0], 255-pixel[1], 255-pixel[2])

negative_list = map( negative_image, im.getdata() )

"""
or with list comprehension,
neg_list = [(255-p[0], 255-p[1], 255-p[2]) for p in im.getdata()]
"""

im.putdata(list(negative_list))
im.show()
# im.save('images/negative.jpg')