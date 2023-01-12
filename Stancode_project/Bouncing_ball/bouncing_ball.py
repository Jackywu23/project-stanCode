"""
File: bouncing_ball.py
Name: Jacky Wu
-------------------------
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity and 0 as y velocity. Each bounce reduces
y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# create a empty window
window = GWindow(800, 500, title='bouncing_ball.py')
# global variable
switch = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.

    pre-condition: create a ball at START_X, START_y position, and wait at that
                    position till first click
    post-condition: After click, ball starts to drop and will be bounced after hit
                    on the ground, the vertical speed will be reduced every bounce.
                    When vertical speed comes to zero, only horizontal speed left.
                    After ball runs out of window on right hand side, it will return
                    back to initiated stage. It will free drop again after another click
    """
    global switch
    ball = GOval(SIZE, SIZE)
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball, x=START_X, y=START_Y)
    vy = 0
    count = 0
    onmouseclicked(active)

    out_of_box = False
    while True:
        if switch is True:
            # prevent ball running out of box (bottom)
            if out_of_box is True:
                dx = VX
                ball.move(dx, 0)
            # restart
            if ball.x > window.width + 3*ball.width:
                window.remove(ball)
                out_of_box = False
                switch = False
                window.add(ball, x=START_X, y=START_Y)
                vy = 0
                count += 1
            if count == 3:
                break
            # Normal loop
            else:
                ball_position, vy = freefall(vy, ball)
                if vy < 0 and ball_position.y+ball.height >= window.height:
                    out_of_box = True
                elif ball_position.y+ball.height >= window.height:
                    vy = -vy*REDUCE
        else:
            pass
        pause(DELAY)


def freefall(vy, ball):
    """
    parameters: vertical velocity and object ball
    return: updated object ball and updated vertical velocity
    """
    # speed
    vy += GRAVITY
    # xy position
    dx = VX
    dy = vy+(0.5*GRAVITY)
    ball.move(dx, dy)
    return ball, vy


def active(mouse):
    """
    If mouse event is triggered, open switch
    """
    global switch
    switch = True


if __name__ == "__main__":
    main()
