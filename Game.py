from Ball import Ball


class Game(object):
    def __init__(self):

        self.Balls = []

    def add_Ball(self, ball):

        assert isinstance(ball, Ball)

        self.Balls.append(ball)

    def get_Balls(self):

        return self.Balls

    def get_human_players(self):

        return [ball for ball in self.Balls if ball.is_human()]

    def get_AI_players(self):

        return [ball for ball in self.Balls if not ball.is_human()]
