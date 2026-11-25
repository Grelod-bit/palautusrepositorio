class TennisGame:
    SCORE_NAMES = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    PLAYERS = {
        -1: "player2",
        1: "player1",
    }

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        score = ""

        if self.m_score1 == self.m_score2:
            score = self.get_equal_score()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            score = self.get_advantage_score()
        else:
            score = self.get_regular_score()

        return score

    def get_equal_score(self):
        if self.m_score1 <= 2:
            score = TennisGame.SCORE_NAMES[self.m_score1] + "-All"
        else:
            score = "Deuce"

        return score

    def get_advantage_score(self):
        difference = self.m_score1 - self.m_score2
        absolute_diff = abs(difference)
        player_ahead = ""
        if absolute_diff == 1:
            if difference >= 0:
                player_ahead = "player1"
            else:
                player_ahead = "player2"

            score = "Advantage " + player_ahead

        elif absolute_diff >= 2:
            if difference >= 0:
                player_ahead = "player1"
            else:
                player_ahead = "player2"

            score = "Win for " + player_ahead

        return score

    def get_regular_score(self):
        for i in range(1, 3):
            if i == 1:
                temp_score = self.m_score1
            else:
                score = score + "-"
                temp_score = self.m_score2

            if temp_score == 0:
                score = score + "Love"
            elif temp_score == 1:
                score = score + "Fifteen"
            elif temp_score == 2:
                score = score + "Thirty"
            elif temp_score == 3:
                score = score + "Forty"
        return score
