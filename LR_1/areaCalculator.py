from math import *

class NonExistentTriangleError(Exception):
    pass

class InvalidSideLengthValue(Exception):
    pass

def calculateArea(a, b, c):
    # Check if a triangle side lengths greater than zero
    if a > 0 and b > 0 and c > 0:
        # Check if a triangle with provided side lengths exists
        if a + b > c and a + c > b and b + c > a:
            # Calculate the semi-perimeter
            s = (a + b + c) / 2

            # Calculate the area using Heron's formula
            area = sqrt(s * (s - a) * (s - b) * (s - c))
            return area
        else:
            raise NonExistentTriangleError('A triangle with provided side lengths does not exist')
    else:
        raise InvalidSideLengthValue('Provided side lengths cannot be negative')