import random
import math

#calculate distance between two points
def distance(x1, y1, x2, y2):
    x_diff = x1 - x2
    y_diff = y1 - y2
    dist = math.sqrt(x_diff ** 2 + y_diff ** 2)
    return dist

def estimate_pi(num_pts):
    circle_cnt = 0
    for i in range(num_pts):
        #randomly generate x,y
        x = random.random()
        y = random.random()
        #check if in circle
        dist = distance(x,y,0.5,0.5)
        if dist <= 0.5:
            circle_cnt += 1

        #increment our count
    return 4 * (circle_cnt / num_pts)

print(estimate_pi(1000000))
