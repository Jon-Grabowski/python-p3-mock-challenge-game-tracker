#!/usr/bin/env python3
import ipdb

from classes.player import Player
from classes.game import Game
from classes.result import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    g1 = Game("Poker")
    g2 = Game("Go Fish")
    p1 = Player("Jon")
    p2 = Player("Bob")
    r1 = Result(p1, g1, 2000)
    r2 = Result(p1, g2, 500)
    r2 = Result(p2, g1, 1500)


    ipdb.set_trace()
