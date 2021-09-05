import sys

import pygame


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

        # Will be defined in separate methods
        self.MAX_ACC = 18
        self.actions_taken = []
        self.x_speed = None
        self.y_speed = None
        self.x_acc = None
        self.y_acc = None

        assert isinstance(color, tuple)
        assert len(color) == 3
        self.color = color

        if keyboard_controls_set is not None:
            if keyboard_controls_set == 1:
                # Maybe: Use decorators to define (decorated functions) versions of set_acc
                # https://www.datacamp.com/community/tutorials/decorators-python

                # self.keyboard_controls = {pygame.K_UP: "up", pygame.K_DOWN: "down", pygame.K_RIGHT: "right", pygame.K_LEFT: "left"}
                self.keyboard_controls = {pygame.K_UP: "up",
                                          pygame.K_DOWN: "down",
                                          pygame.K_RIGHT: "right",
                                          pygame.K_LEFT: "left"}
            elif keyboard_controls_set == 2:
                self.keyboard_controls = {}  # TBD
            else:
                raise ValueError(f"{keyboard_controls_set} is not a value keyboard_controls_set entry.")
        else:
            self.keyboard_controls = None

        print(f"Ball '{name}' created")

    def feed_keys_pressed(self, keys_pressed):
        """
        Applicable only to human players (balls).
        Receive all keys pressed, store all the actions which have
        been taken this round for this ball.
        """

        assert self.is_human()

        self.actions_taken = []

        for key in self.keyboard_controls:
            if keys_pressed[key]:
                print(f"{self.name}: {self.keyboard_controls[key]}")
                self.actions_taken.append(self.keyboard_controls[key])
        print(f"{self.name}: {self.actions_taken}")

    def act_on_actions_taken(self):
        """
        Receive a list of all the actions which have been taken this
        round, then modify the ball behavior based on it.
        This method should be used for human and AI players.
        """

        x_acc = 0
        y_acc = 0

        for action_taken in self.actions_taken:
            if action_taken == "up":
                y_acc -= self.MAX_ACC
            elif action_taken == "down":
                y_acc += self.MAX_ACC
            elif action_taken == "right":
                x_acc += self.MAX_ACC
            elif action_taken == "left":
                x_acc -= self.MAX_ACC
            else:
                raise Exception(f"Unknown action {action_taken}!")

        self.set_acc(x_acc, y_acc)

    def is_human(self):

        return self.ball_type == "human"

    def is_ai(self):

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

    def full_update(self, time_delta):

        """
        Assuming no other interactions:
        1) Update acceleration based on actions taken
        2) Update speed based on acceleration
        3) Update position based on speed.
        """

        self.act_on_actions_taken()
        self.update_speed(time_delta)
        self.update_pos(time_delta)
