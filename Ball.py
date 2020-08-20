class Ball(object):

    def __init__(self, radius, color):

        # radius must be a positive number
        assert isinstance(radius, (int, float))
        assert radius > 0
        
        assert len(col) == 3
        
        print("Ball created")


    def set_pos(self, x, y):

        self.x_pos = x
        self.y_pos = y

    def set_speed(self, x, y):

        "speed in pixels/second"

        self.x_speed = x
        self.y_speed = y


    def update_pos(self, time_delta):

        "time_delta in seconds."

        self.x_pos += time_delta * self.x_speed
        self.y_pos += time_delta * self.y_speed


    def set_acc(self, x, y):

        "acc in pixels/seconds**2"

        self.x_acc = x
        self.y_acc = y

        
    def update_speed(self, time_delta):

        "time_delta in seconds."

        self.x_speed += time_delta * self.x_acc
        self.y_speed += time_delta * self.y_acc


b = Ball()
