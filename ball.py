import random

from field import canvas


class Ball:
    # constructor
    def __init__(self, canvas, platform, score, color):
        self.canvas = canvas
        self.platform = platform
        self.score = score

        # create ball with r=15px and given color, put at the coord=245,100
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        # available directions
        directions = [-2, -1, 1, 2]
        random.shuffle(directions)

        # set ball's position
        self.x = directions[0]
        self.y = -2
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        # Check does ball hit the floor
        self.hit_bottom = False

    # Check does the ball hit the platform
    def hit_platform(self, pos):
        platform_pos = self.canvas.coords(self.platform.id)
        # if ball and platform coordinates match
        if pos[2] >= platform_pos[0] and pos[0] <= platform_pos[2]:
            if pos[3] >= platform_pos[1] and pos[3] <= platform_pos[3]:
                # increase the score
                self.score.hit()
                # return if ball hits platform
                return True
        # return if not
        return False


    # Draw ball
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 2
        #if ball hits floor
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            canvas.create_text(250, 120, text='You lost.\n Final score: {}'.format(self.score.get_score()), font=('Courier', 30), fill='red',)
        # if ball hits platform
        if self.hit_platform(pos) == True:
            self.y = -2
        # if ball hita right wall
        if pos[0] <= 0:
            self.x = 2
        # if ball hits left wall
        if pos[2] >= self.canvas_width:
            self.x = -2

