import pytest

from Ball import Ball

def test_Ball_get_center_distance():

    # Move to fixture?
    ball1 = Ball((255, 0, 0), 3, 0, 0)
    ball2 = Ball((0, 255, 0), 3, 3, 4)
    ball3 = Ball((0, 0, 255), 3, -3, -4)

    assert ball1.get_center_distance(ball1) == 0
    assert ball1.get_center_distance(ball2) == 5
    assert ball2.get_center_distance(ball3) == 10


def test_Ball_get_center_distance():

    # Move to fixture?
    ball1 = Ball((255, 0, 0), 3, 0, 0)
    ball2 = Ball((0, 255, 0), 3, 3, 4)
    ball3 = Ball((0, 0, 255), 3, -3, -4)

    assert ball1.collision(ball1)
    assert ball1.collision(ball2)
    assert not ball2.collision(ball3)
    