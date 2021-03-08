import sys


class Ball(object):
    def __init__(
        self, ball_type, name, radius, x_pos, y_pos, color, keyboard_controls_set=None
    ):

        if ball_type not in ["human", "AI", "passive"]:
            raise ValueError(f"Illegal ball_type: {ball_type}")
        self.ball_type = ball_type

        if not isinstance(name, str):
            raise TypeError("name is not a str.")
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

        if keyboard_controls_set is not None:
            if keyboard_controls_set == 1:
                self.keyboard_controls = {273: "up", 274: "down", 275: "right", 276: "left"}
            elif keyboard_controls_set == 2:
                self.keyboard_controls = {}  # TBD
            else:
                raise ValueError(f"{keyboard_controls_set} is not a value keyboard_controls_set entry.")
        else:
            self.keyboard_controls = None

        print(f"Ball '{name}' created")

    def feed_event(self, event):

        """Feed a single event (e.g. a key pressed) from the main game flow. Let the ball decide how to affect it's own
        actions."""

        # TBD
        # Check against self.human_controls

        print("TBD!! The Ball.feed_event has to process events!")
        print(f"{self.get_name()} processing event {event}.")

    def is_human(self):

        return self.ball_type == "human"

    def is_AI(self):

        return self.ball_type == "AI"

    def is_passive(self):

        return self.ball_type == "passive"

    def get_name(self):

        return self.name

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
