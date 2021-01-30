import random

class Policy:
    def __init__(self):
        pass

    def guess_click_location(self, circles):
        random_x = random.randint(15, 450)
        return (random_x, 680)
