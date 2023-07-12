from .player import Player
class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        self.all.append(self)
        self.player.results(self)
        self.game.results(self)
        self.game.players(self.player)

    def __repr__(self):
        return f"<{self.player} scored {self.score} in {self.game}>"
    def get_score(self):
        return self._score 
    def set_score(self, score):
        if 1 <= score <= 5000:
            self._score = score
        else:
            raise Exception("Score must be between 1-5000.")
    score = property(get_score, set_score)

    def get_player(self):
        return self._player 
    def set_player(self, player):
        from .player import Player
        if isinstance(player, Player):
            self._player = player
        else:
            raise Exception("Must be an instance of Player")
    player = property(get_player, set_player)
        
    def get_game(self):
        return self._game 
    def set_game(self, game):
        from .game import Game
        if isinstance(game, Game):
            self._game = game
        else:
            raise Exception("Must be an instance of Game")
    game = property(get_game, set_game)