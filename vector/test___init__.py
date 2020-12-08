from unittest import TestCase
from vector import Vector


class TestVector(TestCase):
    def test_if_vectors_are_equals_then_return_true(self):
        first_vector = Vector([1, 2, 3, 4, 5])
        second_vector = Vector([1, 2, 3, 4, 5])
        self.assertEqual(True, first_vector == second_vector)

    def test_if_vector_is_empty_then_throw_ValueError_exception(self):
        with self.assertRaises(ValueError):
            v = Vector([])

    def test_if_vector_is_not_iterable_then_throw_TypeError_exception(self):
        with self.assertRaises(TypeError):
            v = Vector(12345)

    def test_if_vector_is_string_then_return_true(self):
        first_vector = Vector("12345")
        second_vector = Vector("12345")
        self.assertEqual(True, first_vector == second_vector)

    def test_vector_to_string(self):
        v = Vector([1, 2, 3])
        v_str = str(v)
        self.assertEqual("Vector: (1, 2, 3)", v_str)

    def test_plus_of_vectors(self):
        first_vector = Vector([1, 2, 3])
        result = first_vector.plus(Vector([3, 2, 1]))
        self.assertEqual(Vector([4, 4, 4]), result)

    def test_other_plus_of_vector(self):
        first_vector = Vector([8.218, -9.341])
        result = first_vector.plus(Vector([-1.129, 2.111]))
        result = Vector([round(x, 3) for x in result.coordinates])
        self.assertEqual(True, Vector([7.089, -7.23]) == result)

    def test_minus_of_vector(self):
        first_vector = Vector([7.119, 8.215])
        result = first_vector.minus(Vector([-8.223, 0.878]))
        result = Vector([round(x, 3) for x in result.coordinates])
        self.assertEqual(True, Vector([15.342, 7.337]) == result)

    def test_other_minus_of_vector(self):
        first_vector = Vector([4, 4, 4])
        result = first_vector.minus(Vector([3, 2, 1]))
        self.assertEqual(Vector([1, 2, 3]), result)

    def test_scalar_of_vector(self):
        first_vector = Vector([1, 2, 3])
        result = first_vector.times_scalar(2)
        self.assertEqual(Vector([2, 4, 6]), result)

    def test_other_scalar_of_vector(self):
        first_vector = Vector([1.671, -1.012, -0.318])
        result = first_vector.times_scalar(7.41)
        result = Vector([round(x, 3) for x in result.coordinates])
        self.assertEqual(True, Vector([12.382, -7.499, -2.356]) == result)

    def test_magnitude_of_vector(self):
        v = Vector([-0.211, 7.437])
        magnitude = v.magnitude()
        magnitude = round(magnitude, 3)
        self.assertEqual(7.44, magnitude)

    def test_other_magnitude_of_vector(self):
        v = Vector([8.813, -1.331, -6.247])
        magnitude = v.magnitude()
        magnitude = round(magnitude, 3)
        self.assertEqual(10.884, magnitude)

    def test_direction_of_vector(self):
        v = Vector([5.581, -2.136])
        direction = v.normalized()
        direction = Vector([round(x, 3) for x in direction.coordinates])
        self.assertEqual(True, Vector([0.934, -0.357]) == direction)

    def test_other_direction_of_vector(self):
        v = Vector([1.996, 3.108, -4.554])
        direction = v.normalized()
        direction = Vector([round(x, 3) for x in direction.coordinates])
        self.assertEqual(True, Vector([0.34, 0.53, -0.777]) == direction)

    def test_first_dot_example(self):
        first_vector = Vector([1, 2, 3])
        second_vector = Vector([3, 2, 1])
        result = round(first_vector.dot(second_vector), 3)
        self.assertEqual(10, result)

    def test_second_dot_example(self):
        first_vector = Vector([7.887, 4.138])
        second_vector = Vector([-8.802, 6.776])
        result = round(first_vector.dot(second_vector), 3)
        self.assertEqual(-41.382, result)

    def test_third_dot_example(self):
        first_vector = Vector([-5.955, -4.904, -1.874])
        second_vector = Vector([-4.496, -8.755, 7.103])
        result = round(first_vector.dot(second_vector), 3)
        self.assertEqual(56.397, result)

    def test_first_angle_example(self):
        first_vector = Vector([3.183, -7.627])
        second_vector = Vector([-2.668, 5.319])
        result = round(first_vector.angle_with(second_vector), 3)
        self.assertEqual(3.072, result)

    def test_second_angle_example(self):
        first_vector = Vector([7.35, 0.221, 5.188])
        second_vector = Vector([2.751, 8.259, 3.985])
        result = round(first_vector.angle_with(second_vector, True), 3)
        self.assertEqual(60.276, result)
