from Ball import Ball


class Game(object):
    def __init__(self):

        self.Balls = []

    def add_ball(self, ball):

        assert isinstance(ball, Ball)

        self.Balls.append(ball)

    def get_balls(self):

        return self.Balls

    def get_human_players(self):

        return [ball for ball in self.Balls if ball.is_human()]

    def get_ai_players(self):

        return [ball for ball in self.Balls if not ball.is_human()]
