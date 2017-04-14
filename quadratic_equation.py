from math import sqrt


def get_roots(a, b, c):
    discriminant = (b ** 2 - 4 * a * c)
    root1 = (-b - sqrt(abs(discriminant))) / (2 * a)
    root2 = (-b + sqrt(abs(discriminant))) / (2 * a)

    if discriminant <= 0:
        return None, None
    else:
        return root1, root2
