from math import sqrt


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError

            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        plus_coordinates = [x + y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(plus_coordinates)

    def minus(self, v):
        minus_coordinates = [x - y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(minus_coordinates)

    def times_scalar(self, c):
        scalar_coordinates = [c * x for x in self.coordinates]
        return Vector(scalar_coordinates)

    def magnitude(self):
        sqrt_coordinates = [x ** 2 for x in self.coordinates]
        return sqrt(sum(sqrt_coordinates))

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1./magnitude)
        except ZeroDivisionError:
            raise Exception("Cannot normalize the zero vector")
