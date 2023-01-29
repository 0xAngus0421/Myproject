"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width,height=paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle,x=(self.window.width-self.paddle.width)/2,y=self.window.height-paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2,ball_radius*2,x=self.window.width/2-ball_radius,y=self.window.height/2-ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        onmouseclicked(self.start_game)
        onmousemoved(self.change_position)
        # Draw bricks
        for row in range(brick_rows):
            for col in range(brick_cols):
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT, x=BRICK_WIDTH * col + BRICK_SPACING * col,
                                   y=BRICK_HEIGHT * row + BRICK_SPACING * row)
                self.brick.filled = True
                if row == 0 or row == 1 :
                    self.brick.fill_color = 'red'
                if row == 2 or row == 3 :
                    self.brick.fill_color = 'orange'
                if row == 4 or row == 5:
                    self.brick.fill_color = 'yellow'
                if row == 6 or row == 7 :
                    self.brick.fill_color = 'green'
                if row == 8 or row == 9 :
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick)

        self.start_x = self.window.width/2-ball_radius
        self.start_y = self.window.height/2-ball_radius
        self.r = brick_rows
        self.c = brick_cols
        self.count = 0 #when count equal to number of bricks :Gameover
        self.open = False#It's a switch to control whether the breakout game is start or not

    def change_position(self,event):
        self.window.add(self.paddle,event.x-self.paddle.width/2,self.window.height-PADDLE_OFFSET)

    def reset_ball(self):
        self.ball.x =  self.window.width/2-BALL_RADIUS
        self.ball.y =  self.window.height/2-BALL_RADIUS
        self.__dx = 0
        self.__dy = 0
        self.open = False

    def ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    def set_dx(self):
        self.__dx = -self.__dx

    def set_dy(self):
        self.__dy = -self.__dy

    def start_game(self,event):
        if not self.open :
            self.ball_velocity()
            self.open = True

    def remove_brick(self):
        maybe_obj1 = self.window.get_object_at(self.ball.x,self.ball.y)
        maybe_obj2 = self.window.get_object_at(self.ball.x+BALL_RADIUS*2, self.ball.y)
        maybe_obj3 = self.window.get_object_at(self.ball.x, self.ball.y+BALL_RADIUS*2)
        maybe_obj4 = self.window.get_object_at(self.ball.x+BALL_RADIUS*2, self.ball.y+BALL_RADIUS*2)

        if maybe_obj1 is not None:
            if maybe_obj1 is not self.paddle:
                self.window.remove(maybe_obj1)
                self.count +=1
                self.set_dy()
            elif maybe_obj1 is self.paddle:
                if self.get_dy() > 0:
                    self.set_dy()
        elif maybe_obj2 is not None:
            if maybe_obj2 is not self.paddle:
                self.window.remove(maybe_obj2)
                self.count += 1
                self.set_dy()
            elif maybe_obj2 is self.paddle:
                if self.get_dy() > 0:
                    self.set_dy()
        elif maybe_obj3 is not None:
            if maybe_obj3 is not self.paddle:
                self.window.remove(maybe_obj3)
                self.count += 1
                self.set_dy()
            elif maybe_obj3 is self.paddle:
                if self.get_dy() > 0:
                    self.set_dy()
        elif maybe_obj4 is not None:
            if maybe_obj4 is not self.paddle:
                self.window.remove(maybe_obj4)
                self.count += 1
                self.set_dy()
            elif maybe_obj4 is self.paddle:
                if self.get_dy() > 0:
                    self.set_dy()