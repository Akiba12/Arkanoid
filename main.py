import time

from ball import Ball
from field import field, canvas
from platform import Platform
from score import Score

score = Score(canvas, 'green')
platform = Platform(canvas, 'yellow')
ball = Ball(canvas, platform, score, 'red')

while not ball.hit_bottom:

    if platform.started == True:
        ball.draw()
        platform.draw()

    field.update_idletasks()

    field.update()

    # delay to make animation smooth
    time.sleep(0.01)

# Game is over
print('Game over')
time.sleep(3)