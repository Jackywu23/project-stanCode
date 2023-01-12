"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

Hand-in person: Jacky
Making a class to set up gaming environment for breakout.py
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2, y=window_height-paddle_height-
                            paddle_offset)
        self.paddle.filled = True
        self.paddle.fill_color = "black"
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=window_width/2-ball_radius, y=window_height/2-ball_radius)
        self.ball.filled = True
        self.ball.fill_color = "black"
        self.window.add(self.ball)
        # Default initial velocity for the ball
        # Initialize our mouse listeners
        onmouseclicked(self.initiate)
        onmousemoved(self.tracker)
        # Draw bricks
        color = ["blue", "gray", "pink", "yellow", "lime", "magenta"]
        select_color = 0
        for i in range(brick_cols):
            if i > 0 and i % 2 == 0:
                select_color += 1
            for j in range(brick_rows):
                self.bricks = GRect(brick_width, brick_height, x=(brick_width+brick_spacing)*j,
                                    y=brick_offset+(brick_height+brick_spacing)*i)
                self.bricks.filled = True
                self.bricks.fill_color = color[select_color]
                self.bricks.color = color[select_color]
                self.window.add(self.bricks)
        # trigger point
        self.switch = False

        # bricks number
        self.brick_num = brick_cols*brick_rows

    def tracker(self, mouse):
        self.paddle.y = self.window.height - PADDLE_OFFSET
        self.paddle.x = mouse.x-PADDLE_WIDTH/2
        if mouse.x > self.window.width - PADDLE_WIDTH / 2:
            self.paddle.x = self.window.width-PADDLE_WIDTH
        if mouse.x < PADDLE_WIDTH/2:
            self.paddle.x = 0

    def initiate(self, click):
        self.switch = True

    @staticmethod
    def get_vx():
        """
        getter for x direction velocity
        """
        __dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            __dx = - __dx
        return __dx

    @staticmethod
    def get_vy():
        """
        getter for y direction velocity
        """
        __dy = INITIAL_Y_SPEED
        return __dy

