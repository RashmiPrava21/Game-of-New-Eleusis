"""
CMSC671: Artificial Intelligence Project Phase 2
12 December 2016
Rule Breakers:
    Vikramaditya Battina
    Sri Konuru
    Nikhil Kumar Mengani
    Alexander Spizler

Sample test functions to run our code. Enjoy!
"""

import unittest
import New_Eleusis_Agent_Phase2 as ag


class DecisionTreeTest(unittest.TestCase):
    @staticmethod
    def test_decision_tree():

        rule = "if(equal(color(previous), B), equal(color(current), R), equal(color(current), B))"
        card1 = "10H"
        card2 = "3S"
        card3 = "KD"
        ag.play_game(rule, card1, card2, card3)

        # rule = "if(equal(color(previous), B), equal(color(current), R), True)"
        # card1 = "10H"
        # card2 = "3S"
        # card3 = "3D"
        # result = ag.play_game(rule, card1, card2, card3)

        # rule = "if(is_royal(current), True, False)"
        # card1 = "10H"
        # card2 = "3S"
        # card3 = "KS"
        # result = ag.play_game(rule, card1, card2, card3)

        # rule = "if(equal(suit(current), suit(previous)), greater(value(current), value(previous)), True)"
        # card1 = "10H"
        # card2 = "3S"
        # card3 = "6S"
        # result = ag.play_game(rule, card1, card2, card3)


if __name__ == '__main__':
    unittest.main()
