class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality=dict['nationality']
        self.assists=dict['assists']
        self.goals=dict['goals']
        self.games=dict['games']
        self.team=dict['team']


    def __str__(self):
        return f"{self.name:20} {self.team:<20} {self.goals:<3} + {self.assists:3}  = {self.goals+self.assists:3}"



