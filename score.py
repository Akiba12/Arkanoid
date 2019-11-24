class Score:

    # constructor
    def __init__(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(450, 10, text=self.score, font=('Courier', 15), fill=color)

    def hit(self):
        # increase score by 1
        self.score += 1

        # write new score
        self.canvas.itemconfig(self.id, text=self.score)

    def get_score(self):
        return self.score