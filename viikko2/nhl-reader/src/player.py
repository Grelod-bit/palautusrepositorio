class Player:
    def __init__(self, dictionary):
        self.name = dictionary['name']
        self.nationality=dictionary['nationality']
        self.assists=dictionary['assists']
        self.goals=dictionary['goals']
        self.games=dictionary['games']
        self.team=dictionary['team']


    def __str__(self):
        return f"{self.name:20} {self.team:<20} {self.goals:<3} + {self.assists:3}  = {self.goals+self.assists:3}"
