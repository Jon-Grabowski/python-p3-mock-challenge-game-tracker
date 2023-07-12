class Game:
    def __init__(self, title):
        self.title = title
        self._results = []
        self._players = []

    def __repr__(self):
        return f'{self.title}'

    def get_title(self):
        return self._title 
    def set_title(self, title):
        if not hasattr(self, "_title"):
            if isinstance(title, str) and len(title) > 0:    
                self._title = title
            else:
                raise Exception("Must enter a game title.")
        else:
            raise Exception("Game title can not be changed.")
    title = property(get_title, set_title)
        
    def results(self, new_result=None):
        from classes.result import Result
        if isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results
    
    def players(self, new_player=None):
        from classes.player import Player
        if isinstance(new_player, Player):
            self._players.append(new_player)
        return self._players
    
    def average_score(self, player):
        pass 