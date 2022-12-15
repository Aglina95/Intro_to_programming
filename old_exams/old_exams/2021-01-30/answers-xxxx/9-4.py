import math

def is_close(chair, other_chair):
    """Computes the distance between two points (x1, y1) and (x2, y2) using the 
    formula (x1-x2)^2 + (y1-y2)^2 and returning the square root of this.""" 
    distance = (chair[0] - other_chair[0])**2 + (chair[1] - other_chair[1])**2
    distance = math.sqrt(distance)
    return distance <= 1.5

def ensure_proximity(chair_list):
    # YOUR CODE HERE
    pass


chair_list = [[1, 1], [3, 2], [0, 1]] # has a close pair, so something must be removed 
print(ensure_proximity(chair_list))
