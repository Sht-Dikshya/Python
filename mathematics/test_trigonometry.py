import math
from mathematics.trigonometry import sine
from mathematics.trigonometry import cosine

def test_sine():
    sin_45= sine(math.pi/4)
    assert math.isclose(sin_45, math.sin(math.pi/4), rel_tol= 0.1)

def test_cosine():
    cos_45= cosine(math.pi/4)
    assert math.isclose(cos_45, math.cos(math.pi/4), rel_tol= 0.1)