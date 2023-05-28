import pygame


class Ball():

    def __init__(self, color: tuple, radius: float, x_pos, y_pos, x_speed: float=0, y_speed: float=0, x_max_acc: float=1, y_max_acc: float=1):

        assert isinstance(color, tuple)
        assert len(color) == 3
        self.color = color

        assert isinstance(radius, (int, float))
        assert radius > 0
        self.radius = radius

        assert isinstance(x_pos, (int, float))
        self.x_pos = x_pos
        assert isinstance(y_pos, (int, float))
        self.y_pos = y_pos

        self.x_speed = x_speed
        self.y_speed = y_speed
        self.x_acc = 0
        self.y_acc = 0
        self.x_max_acc = x_max_acc
        self.y_max_acc = y_max_acc


    def update_acc_from_actions(self, x_acc_of_max: float, y_acc_of_max: float):
        """
        This method should be used for human and AI players.
        """
        assert x_acc_of_max >= -1
        assert x_acc_of_max <= 1
        assert y_acc_of_max >= -1
        assert y_acc_of_max <= 1
        
        x_acc = x_acc_of_max * self.x_max_acc
        y_acc = y_acc_of_max * self.y_max_acc

        self.set_acc(x_acc, y_acc)

    def get_radius(self):

        return self.radius

    def get_color(self):

        return self.color

    def get_pos(self):

        return {"x": self.x_pos, "y": self.y_pos}

    def set_pos(self, x, y):

        self.x_pos = x
        self.y_pos = y

    def set_speed(self, x, y):
        """speed in pixels/second"""

        self.x_speed = x
        self.y_speed = y

    def update_pos(self, time_delta):
        """"time_delta in seconds."""

        self.x_pos += time_delta * self.x_speed
        self.y_pos += time_delta * self.y_speed

    def set_acc(self, x, y):
        """"acc in pixels/seconds**2"""

        self.x_acc = x
        self.y_acc = y

    def update_speed(self, time_delta):
        """time_delta in seconds."""

        self.x_speed += time_delta * self.x_acc
        self.y_speed += time_delta * self.y_acc

    def update_speed_and_pos(self, time_delta):
        """
        Assuming no other interactions, like collisions:
        """

        self.update_speed(time_delta)
        self.update_pos(time_delta)

    def draw_on_surface(self, surface):

        pygame.draw.circle(
            surface,
            self.color,
            (round(self.x_pos), round(self.y_pos)),
            self.get_radius(),
            0)