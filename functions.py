import math


def volume(radius):
    """Returns the volume of a sphere with radius."""
    volume = (4.0 / 3.0) * math.pi * radius ** 3
    return volume


print(volume(2))


def triangle_area(base, height):
    """Returns the are of a triangle with base and height."""
    return 0.5 * base * height


print(triangle_area(3, 6))


def cm(feet=0, inches=0):
    """Convert a lenght from feet and inches to centimeters."""
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inches_to_cm + feet_to_cm


print(cm(5, 8))
