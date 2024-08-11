import random


def monte_carlo_pi(num_points):
    points_inside_circle = 0
    total_points = num_points

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = x ** 2 + y ** 2
        if distance <= 1:
            points_inside_circle += 1

    return 4 * points_inside_circle / total_points


number_points = 1000000
estimated_pi = monte_carlo_pi(number_points)
print(f"Approximate value of pi using Monte-Carlo method and {number_points} points: {estimated_pi}")
