class Ball(object):

    def __init__(self, ball_type, name, radius, x_pos, y_pos, color, keyboard_controls=None):

        assert ball_type in ["human", "AI", "passive"]
        self.ball_type = ball_type

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


        if keyboard_controls is not None:
            self.keyboard_controls = self._transform_keyboard_controls({273: "up",
                                                                        274: "down",
                                                                        275: "right",
                                                                        276: "left"})
        else:
            self.keyboard_controls = None

        print(f"Ball '{name}' created")


    def _transform_keyboard_controls(self, keyboard_controls):

        """Assign a dictionary {event(int) : function} to each ball."""

        print(keyboard_controls)

        assert len(keyboard_controls) == 4
        assert "left" in keyboard_controls.values()
        assert "right" in keyboard_controls.values()
        assert "up" in keyboard_controls.values()
        assert "downl" in keyboard_controls.values()

        #self.event_handler(

        #273: U
        #274 D
        #275 R
        #276 L

        sys.exit(1)

        self.my_events = {}  # TBD!!! Set human controls.

        return hum


    def feed_event(self, event):

        """Feed a single event (e.g. a key pressed) from the main game flow. Let the ball decide how to affect it's own
        actions."""

        # TBD
        # Check against self.human_controls

        print(f"{self.get_name()} processing event {event}.")

        pass



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
