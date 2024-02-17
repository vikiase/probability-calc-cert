import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.balls_for_each_color = kwargs  #dictionary
        self.contents = []
        for color, count in self.balls_for_each_color.items():
            for i in range(count):
                self.contents.append(color)

    def draw(self, number_of_draws):
        removed_balls = []
        if number_of_draws > len(self.contents):
            return self.contents
        else:
            for i in range(number_of_draws):
                x = random.randint(0, len(self.contents)-1)
                removed_balls.append(self.contents[x])
                self.contents.remove(self.contents[x])
        return removed_balls

    def print(self):
        return self.contents
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_balls_list = []    #hotovo
    hat_content = []            #hotovo
    hat_content = hat.contents
    right = 0
    # tvorba expected_balls listu
    for color, count in expected_balls.items():
        for i in range(count):
            expected_balls_list.append(color)

    # experiment
    def draw_balls(num_balls_drawn, hat_content):
        drawn_balls = []
        copy = hat_content.copy()
        for j in range(num_balls_drawn):
            if not copy:
                break
            x = random.randint(0, len(copy)-1)
            drawn_balls.append(copy[x])
            del copy[x]
        return drawn_balls
    def isRight(new, expected):
        for color, count in expected.items():
            if color not in new:
                return False
            if new[color] != count:
                return False
            return True

    for k in range(num_experiments):
        new_hat_content = draw_balls(num_balls_drawn, hat_content)
        # tvorba new hat content slovniku
        new_hat_content_dict = {}
        for color in new_hat_content:
            if color in new_hat_content_dict:
                new_hat_content_dict[color] += 1
            else:
                new_hat_content_dict[color] = 1
        #srovnani

        if isRight(new_hat_content_dict, expected_balls):
            right += 1
    #vypocitani pravdepodobnosti
    if right == 0:
        probability = 0
    else:
        probability = right/num_experiments
    return probability
