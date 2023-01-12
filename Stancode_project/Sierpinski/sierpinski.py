"""
File: sierpinski.py
Name: Jacky Wu
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	pre-condition: input constants into a function called sierpinski_triangle
	post-condition: draw a image into a separated window
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: how many time to run iteration (recursive)
	:param length: the length of triangle
	:param upper_left_x: the x coordinate of upper left point of triangle
	:param upper_left_y: the y coordinate of upper left point of triangle
	:return: drawing of sierpinski_triangle
	"""
	if order == 0:
		pass
	else:
		tri_1 = GLine(upper_left_x, upper_left_y, upper_left_x+length*0.5, upper_left_y+length*0.866)
		tri_2 = GLine(upper_left_x+length*0.5, upper_left_y+length*0.866, upper_left_x+length, upper_left_y)
		tri_3 = GLine(upper_left_x+length, upper_left_y, upper_left_x, upper_left_y)
		tri_1.filled = True
		tri_2.filled = True
		tri_3.filled = True
		window.add(tri_1)
		window.add(tri_2)
		window.add(tri_3)

		# top-left
		sierpinski_triangle(order-1, length/2, upper_left_x, upper_left_y)

		# top-right
		sierpinski_triangle(order-1, length/2, upper_left_x+length/2, upper_left_y)

		# bottom:
		sierpinski_triangle(order-1, length/2, upper_left_x+length*0.25, upper_left_y+length*0.433)


if __name__ == '__main__':
	main()