"""
File: babygraphics.py
Name: Jacky Wu
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_dif = width//(len(YEARS))

    return GRAPH_MARGIN_SIZE+(year_index*x_dif)


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)

    for i in range(len(YEARS)):
        index = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(index, 0, index, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(index+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, anchor=tkinter.NW, text=YEARS[i],
                           font="times")


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    # repeat color if selected data exceed color number in the color list
    n = len(lookup_names)//len(COLORS) + 1
    new_color = COLORS*n

    height_ratio = CANVAS_HEIGHT/MAX_RANK   # ratio to let data match canvas' height

    # draw the label
    for i in range(len(lookup_names)):
        for j in range(len(YEARS)):
            index = get_x_coordinate(CANVAS_WIDTH, j)
            index_0 = get_x_coordinate(CANVAS_WIDTH, j-1)
            # If data existed in selected year, goes into this loop
            if str(YEARS[j]) in name_data[lookup_names[i]]:
                if int(name_data[lookup_names[i]][str(YEARS[j])]) > MAX_RANK:
                    canvas.create_text(index + TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, anchor=tkinter.SW,
                                       text=lookup_names[i] + " *", fill=new_color[i], font="times 12")
                else:
                    canvas.create_text(index+TEXT_DX,
                                       int(name_data[lookup_names[i]][str(YEARS[j])])*height_ratio+GRAPH_MARGIN_SIZE,
                                       anchor=tkinter.SW,
                                       text=lookup_names[i]+name_data[lookup_names[i]][str(YEARS[j])],
                                       fill=new_color[i], font="time 12")

            else:
                canvas.create_text(index + TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                   anchor=tkinter.SW, text=lookup_names[i] + " *", fill=new_color[i], font="time 12")

            # draw line
            if j > 0:
                if str(YEARS[j]) in name_data[lookup_names[i]]:
                    if int(name_data[lookup_names[i]][str(YEARS[j])]) > MAX_RANK:
                        y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                    else:
                        y = int(name_data[lookup_names[i]][str(YEARS[j])])*height_ratio+GRAPH_MARGIN_SIZE
                else:
                    y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE

                if str(YEARS[j-1]) in name_data[lookup_names[i]]:
                    if int(name_data[lookup_names[i]][str(YEARS[j-1])]) > MAX_RANK:
                        y_0 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    else:
                        y_0 = int(name_data[lookup_names[i]][str(YEARS[j-1])])*height_ratio + GRAPH_MARGIN_SIZE
                else:
                    y_0 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE

                canvas.create_line(index_0, y_0, index, y, width=LINE_WIDTH, fill=new_color[i])


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
