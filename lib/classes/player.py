class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []

    def __repr__(self):
        return f"{self.username}"

    def get_username(self):
        return self._username 
    def set_username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception("Username must be 2-16 characters long.")
    username = property(get_username, set_username)

    def results(self, new_result=None):
        from classes.result import Result
        if isinstance(new_result, Result):
            # print(self.player)
            self._results.append(new_result)
        return self._results
    
    def games_played(self):
        return [result.game for result in self.results()]
    
    def played_game(self, game):
        for result in self._results:
            if game == result.game:
                return True
        return False
    
    def num_times_played(self, game):
        return len([result for result in self._results if result.game == game])

    
    @classmethod
    def highest_scored(cls, game):
        pass 
        
