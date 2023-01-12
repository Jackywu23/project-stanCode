"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Hand-in person: Jacky
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10        # 100 frames per second
NUM_LIVES = 3			# Number of attempts

# import moving step from Class
vx = BreakoutGraphics.get_vx()
vy = BreakoutGraphics.get_vy()


def main():
    """
    After run the program, a window with bricks, a ball, and a paddle will be shown. The game can be started once
    gamer click his/her mouse. The ball will be dropped in a random direction and gamer needs to prevent the ball drops
    out the bottom edge of the window. Once the ball has dropped out the window, it will return back to its original
    position waiting next click to start. The player has 3 chances to eliminate all bricks to win the game.
    """
    global vx, vy
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    brick_remain = graphics.brick_num

    while True:
        if lives > 0 and graphics.switch is True:
            graphics.ball.move(vx, vy)
            # set boundary conditions for top, left, and right edges
            if graphics.ball.x+graphics.ball.width > graphics.window.width or graphics.ball.x < 0:
                vx = -vx
            if graphics.ball.y < 0:
                vy = -vy
            # set boundary condition for bottom edge and reset the game once player fail to catch the ball
            elif graphics.ball.y > graphics.window.height:
                graphics.switch = False
                graphics.window.remove(graphics.ball)
                graphics.window.add(graphics.ball, x=(graphics.window.width-graphics.ball.width)/2,
                                    y=(graphics.window.height-graphics.ball.height)/2)
                vx = BreakoutGraphics.get_vx()
                lives -= 1

            # rebound condition and erase bricks if the ball hit them and rebound if hit the paddle
            flag = False
            for i in range(2):
                if flag is True:
                    break
                for j in range(2):
                    obj = graphics.window.get_object_at(graphics.ball.x + i*graphics.ball.width, graphics.ball.y +
                                                        j*graphics.ball.height)
                    if obj is not None:
                        if obj is graphics.paddle:
                            vy = -BreakoutGraphics.get_vy()
                        else:
                            graphics.window.remove(obj)
                            brick_remain -= 1
                            rebound()
                        flag = True
                        break

            if brick_remain == 0:
                break

        pause(FRAME_RATE)


def rebound():
    """
    rebound function
    """
    global vx, vy
    vy = -vy


if __name__ == '__main__':
    main()
