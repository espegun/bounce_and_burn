class Ball(object):

    def __init__(self, name, radius, x_pos, y_pos, color):

        assert isinstance(name, str)
        self.name = name

        assert isinstance(radius, (int, float))
        assert radius > 0
        self.radius = radius

        assert isinstance(x_pos, (int, float))
        self.x_pos = x_pos
        assert isinstance(y_pos, (int, float))
        self.y_pos = y_pos

        assert isinstance(color, tuple)
        assert len(color) == 3
        self.color = color

        print(f"Ball '{name}' created")


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


#b = Ball("Test1", 10, (255, 0, 0))
