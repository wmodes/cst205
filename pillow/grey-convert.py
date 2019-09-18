from PIL import Image

im = Image.open('images/teacher.jpg')

def median(pixel):
    my_list = list(pixel)
    my_list.sort()
    return (my_list[1],) * 3

def pile_higher(pixel):
    

# average
# new_list = map( lambda a : (int((a[0]+a[1]+a[2])/3),) * 3, im.getdata() )
# red channel
new_list = map( lambda a : (a[0],) * 3, im.getdata() )
# blue channel
# new_list = map( lambda a : (a[2],) * 3, im.getdata() )
# experiment, median
#new_list = map(median, im.getdata() )



"""
or,
new_list = [ ((a[0]+a[1]+a[2])//3,)*3 for a in im.getdata() ]
"""

im.putdata(list(new_list)) 
im.show()