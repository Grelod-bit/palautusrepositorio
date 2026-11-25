class TennisGame:
    SCORE_NAMES = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def __init__(self, p1_name, p2_name):
        self.p1_name = p1_name
        self.p2_name = p2_name
        self.p1_score = 0
        self.p2_score = 0

    def won_point(self, player_name):
        if player_name == self.p1_name:
            self.p1_score += 1
        else:
            self.p2_score += 1

    def get_score(self):
        if self.p1_score == self.p2_score:
            return self.get_equal_score()
        elif self.p1_score >= 4 or self.p2_score >= 4:
            return self.get_advantage_score()

        return self.get_regular_score()

    def get_equal_score(self):
        if self.p1_score <= 2:
            score = self.SCORE_NAMES[self.p1_score] + "-All"
        else:
            score = "Deuce"

        return score

    def get_advantage_score(self):
        difference = self.p1_score - self.p2_score
        absolute_diff = abs(difference)
        player_ahead = "player1" if difference > 0 else "player2"

        if absolute_diff == 1:
            score = "Advantage " + player_ahead

        elif absolute_diff >= 2:
            score = "Win for " + player_ahead

        return score

    def get_regular_score(self):
        return f"{self.SCORE_NAMES[self.p1_score]}-{self.SCORE_NAMES[self.p2_score]}"
