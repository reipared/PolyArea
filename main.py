import random

class Hat:
    def __init__(self, **balls):
        self.balls = balls
        self.contents = []
        for color, count in balls.items():
            for i in range(count):
                self.contents.append(color)

    def draw(self, num_balls):
        balls_drawn = []
        if num_balls > len(self.contents):
            num_balls = len(self.contents)
        for i in range(num_balls):
            ball_index = random.randint(0, len(self.contents)-1)
            balls_drawn.append(self.contents.pop(ball_index))
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_successful = 0
    for i in range(num_experiments):
        balls_drawn = hat.draw(num_balls_drawn)
        balls_drawn_dict = {}
        for ball in balls_drawn:
            balls_drawn_dict[ball] = balls_drawn_dict.get(ball, 0) + 1
        success = True
        for color, count in expected_balls.items():
            if balls_drawn_dict.get(color, 0) < count:
                success = False
                break
        if success:
            num_successful += 1
    return num_successful / num_experiments

hat = Hat(blue=5, red=4, green=2)
expected_balls = {"red":1, "green":2}
num_balls_drawn = 4
num_experiments = 10000
probability = experiment(hat, expected_balls, num_balls_drawn, num_experiments)
print(probability)
