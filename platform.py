import random


class Platform:
    # constructor
    def __init__(self, canvas, color):
        self.canvas = canvas
        # create platform
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        # available positions
        start_1 = [40, 60, 90, 120, 150, 180, 200]
        random.shuffle(start_1)

        # set platform to the point
        self.starting_point_x = start_1[0]
        self.canvas.move(self.id, self.starting_point_x, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()

        # Waiting for user to press a key
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)
        self.canvas.bind_all('<KeyPress-Left>', self.move_left)
        self.started = False
        self.canvas.bind_all('<KeyPress-Return>', self.start_game)

    # move right
    def move_right(self, event):
        self.x = 2

    # move left
    def move_left(self, event):
        self.x = -2

    # start the game
    def start_game(self, event):
        self.started = True

    # Draw platform
    def draw(self):

        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)

        # If platform hits left wall then stop
        if pos[0] <= 0:
            self.x = 0

        # If platform hits right wall then stop
        elif pos[2] >= self.canvas_width:
            self.x = 0