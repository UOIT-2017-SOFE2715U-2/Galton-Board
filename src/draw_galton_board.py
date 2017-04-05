from PIL import Image
from PIL import ImageDraw
import imageio
import numpy as np
from math import log10

container_width_in_marbles = 3
circle_fill = (0, 255, 0)
circle_outline = (0, 0, 255)
lines_fill = (255,0,0)
lines_width = 3


def draw_marble(x, y):
    box = [x - radius, y - radius, x + radius, y + radius]
    Draw = ImageDraw.Draw(img)
    Draw.ellipse(box, circle_fill, circle_outline)
    return img


def draw_vertical_separators():
    for i in xrange(0, number_of_separators):
        Draw.line([((i * container_width_in_pixels), 0),((i * container_width_in_pixels), height)],fill=lines_fill, width=lines_width)
    return img


def simulate( queue, levels):  #, marbles_in_container):
    # set global variables
    global number_of_separators
    global container_width_in_pixels
    global container_width_in_marbles
    global radius
    global img
    global Draw
    global width
    global height

    max_filled = max(np.bincount(queue))

    width = 1600
    minimum_height = 800
    diameter = int(27.0/log10(max_filled))
    number_of_separators = levels + 1
    container_width_in_pixels = (width / (number_of_separators - 1))

    container_width_in_marbles = container_width_in_pixels / diameter
    # readjust with of container
    container_width_in_pixels = diameter * container_width_in_marbles
    width = container_width_in_pixels * levels
    #diameter = height / (max_filled / container_width_in_marbles)
    radius = diameter/2
    height = diameter * ((max_filled / container_width_in_marbles) + 1)
    if height < minimum_height:
        height = minimum_height

    img = Image.new('RGB', (width, height), (255, 255, 255, 0))
    Draw = ImageDraw.Draw(img)
    ########################################################################
    columns = [None] * levels
    # this list to track how many marbles in specific container
    marbles_dropped = [0] * levels
    draw_vertical_separators()
    i = 0
    for container_number in queue:
        marbles_dropped[container_number] += 1
        horizontal_sequence = (marbles_dropped[container_number] - 1) %   container_width_in_marbles
        vertical_sequence = (marbles_dropped[container_number] -1) /   container_width_in_marbles
        x = ((horizontal_sequence * radius * 2) + radius) + (container_width_in_pixels * container_number)
        y = height - (radius + (vertical_sequence * radius * 2))

        draw_marble(x, y)
        img.save('../img_output/' + str(len(queue)) + '/' + str(len(queue)) + '_' + str(i).zfill(len(str(len(queue)))) + '.png')
        i += 1
    #img.save('../img_output/'+ str(len(queue)) + '_' + str(i).zfill(len(str(len(queue)))) + '.png')
    img.show()
