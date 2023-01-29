"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    # Add animation loop here!
    while True:
        pause(FRAME_RATE)

        graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        #球碰到磚塊要消除，並改變方向
        graphics.remove_brick()
        if graphics.count == graphics.r*graphics.c:
            break
        #球到視窗上方及左右要反彈
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.set_dx()
        if graphics.ball.y <= 0 :
            graphics.set_dy()

        if graphics.ball.y + graphics.ball.height >= graphics.window.height:#落到下方要重來並扣命
            lives -= 1
            graphics.reset_ball()
        if lives == 0 :#沒命就結束遊戲
            break



if __name__ == '__main__':
    main()
