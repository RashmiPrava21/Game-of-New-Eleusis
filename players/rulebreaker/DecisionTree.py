"""
CMSC671: Artificial Intelligence Project Phase 2
12 December 2016
Rule Breakers:
    Vikramaditya Battina
    Sri Konuru
    Nikhil Kumar Mengani
    Alexander Spizler

This class contains variables and methods necessary to construct and return a decision tree representing
a hypothesis for New Eleusis Phase 1.
"""

import new_eleusis as ne
import DecisionTreeNode as dtn
import DecisionTreeAttributeMap as dtam
import math
import random
import sys


class DecisionTree:

    # Helper variable used to construct the rule expression
    rule = []

    def __init__(self):
        """
        Constructor creates empty table
        Function: build decision tree recursively from table. Store DecisionTreeNodes? Return root
        """

        # Collections of similar attributes. Necessary to construct simpler rules first
        basic_attr_cur = ["color_cur", "even_cur", "is_royal_cur"]

        val_attr_cur = ["val_greater_a_cur", "val_less_2_cur", "val_greater_2_cur",
                        "val_less_3_cur", "val_greater_3_cur",
                        "val_less_4_cur", "val_greater_4_cur",
                        "val_less_5_cur", "val_greater_5_cur",
                        "val_less_6_cur", "val_greater_6_cur",
                        "val_less_7_cur", "val_greater_7_cur",
                        "val_less_8_cur", "val_greater_8_cur",
                        "val_less_9_cur", "val_greater_9_cur",
                        "val_less_10_cur", "val_greater_10_cur",
                        "val_less_j_cur", "val_greater_j_cur",
                        "val_less_q_cur", "val_greater_q_cur",
                        "val_less_k_cur"]

        suit_attr_cur = ["suit_less_D_cur", "suit_greater_D_cur", "suit_less_H_cur", "suit_greater_H_cur",
                         "suit_less_S_cur"]

        basic_attr_prev = ["color_prev", "even_prev", "is_royal_prev"]

        val_attr_prev = ["val_greater_a_prev",
                         "val_less_2_prev", "val_greater_2_prev",
                         "val_less_3_prev", "val_greater_3_prev",
                         "val_less_4_prev", "val_greater_4_prev",
                         "val_less_5_prev", "val_greater_5_prev",
                         "val_less_6_prev", "val_greater_6_prev",
                         "val_less_7_prev", "val_greater_7_prev",
                         "val_less_8_prev", "val_greater_8_prev",
                         "val_less_9_prev", "val_greater_9_prev",
                         "val_less_10_prev", "val_greater_10_prev",
                         "val_less_j_prev", "val_greater_j_prev",
                         "val_less_q_prev", "val_greater_q_prev",
                         "val_less_k_prev"]

        suit_attr_prev = ["suit_less_D_prev", "suit_greater_D_prev", "suit_less_H_prev", "suit_greater_H_prev",
                          "suit_less_S_prev"]

        basic_attr_prev2 = ["color_prev2", "even_prev2", "is_royal_prev2"]

        val_attr_prev2 = ["val_greater_a_prev2", "val_less_2_prev2", "val_greater_2_prev2",
                          "val_less_3_prev2", "val_greater_3_prev2",
                          "val_less_4_prev2", "val_greater_4_prev2",
                          "val_less_5_prev2", "val_greater_5_prev2",
                          "val_less_6_prev2", "val_greater_6_prev2",
                          "val_less_7_prev2", "val_greater_7_prev2",
                          "val_less_8_prev2", "val_greater_8_prev2",
                          "val_less_9_prev2", "val_greater_9_prev2",
                          "val_less_10_prev2", "val_greater_10_prev2",
                          "val_less_j_prev2", "val_greater_j_prev2",
                          "val_less_q_prev2", "val_greater_q_prev2",
                          "val_less_k_prev2"]

        suit_attr_prev2 = ["suit_greater_C_prev2", "suit_less_D_prev2", "suit_greater_D_prev2", "suit_less_H_prev2",
                           "suit_greater_H_prev2", "suit_less_S_prev2"]

        rel_attr_cur_prev = ["diff_card_cur_prev", "diff_suit_cur_prev", "diff_val_cur_prev", "less_cur_prev",
                             "greater_cur_prev", "color_less_cur_prev", "color_greater_cur_prev", "suit_less_cur_prev",
                             "suit_greater_cur_prev", "val_less_cur_prev", "val_greater_cur_prev"]

        rel_attr_prev_prev2 = ["diff_card_prev_prev2", "diff_suit_prev_prev2", "diff_val_prev_prev2", "less_prev_prev2",
                               "greater_prev_prev2", "color_less_prev_prev2", "color_greater_prev_prev2",
                               "suit_less_prev_prev2", "suit_greater_prev_prev2", "val_less_prev_prev2",
                               "val_greater_prev_prev2"]

        rel_attr_prev2_cur = ["diff_card_prev2_cur", "diff_suit_prev2_cur", "diff_val_prev2_cur", "less_prev2_cur",
                              "greater_prev2_cur", "color_less_prev2_cur", "color_greater_prev2_cur",
                              "suit_less_prev2_cur", "suit_greater_prev2_cur", "val_less_prev2_cur",
                              "val_greater_prev2_cur"]

        # Combine last several lists. This prevents overly complicated rules from being created.
        last_list = []
        last_list.extend(val_attr_cur)
        last_list.extend(val_attr_prev)
        last_list.extend(val_attr_prev2)
        last_list.extend(rel_attr_cur_prev)
        last_list.extend(rel_attr_prev_prev2)
        last_list.extend(rel_attr_prev2_cur)

        # List of attribute lists
        self.attribute_names = [basic_attr_cur, basic_attr_prev, basic_attr_prev2,
                                suit_attr_cur, suit_attr_prev, suit_attr_prev2,
                                last_list]

        # Create and populate attribute map
        self.attribute_map = dtam.DecisionTreeAttributeMap()
        self.populate_attribute_map()

        # Create attribute table
        self.attribute_table = []

        # Create root of hypothesis decision tree
        self.hypothesis_root = dtn.DecisionTreeNode()

    def get_hypothesis_root(self):
        """
        Returns root of hypothesis decision tree
        :return:
        """
        return self.hypothesis_root

    def populate_attribute_map(self):
        """
        Add all attributes to map from DecisionTreeNode name to tuple of (function name, function outputs list,
        function, function var list)
        :return:
        """
        '''color'''
        self.attribute_map.add("color_prev2", "color(previous2)", ['B', 'R'], ne.color, ["previous2"])
        self.attribute_map.add("color_prev", "color(previous)", ['B', 'R'], ne.color, ["previous"])
        self.attribute_map.add("color_cur", "color(current)", ['B', 'R'], ne.color, ["current"])
        '''even'''
        self.attribute_map.add("even_prev2", "even(previous2)", [True, False], ne.even, ["previous2"])
        self.attribute_map.add("even_prev", "even(previous)", [True, False], ne.even, ["previous"])
        self.attribute_map.add("even_cur", "even(current)", [True, False], ne.even, ["current"])
        '''suit'''
        self.attribute_map.add("suit_prev2", "suit(previous2)", ['C', 'D', 'H', 'S'], ne.suit, ["previous2"])
        self.attribute_map.add("suit_prev", "suit(previous)", ['C', 'D', 'H', 'S'], ne.suit, ["previous"])
        self.attribute_map.add("suit_cur", "suit(current)", ['C', 'D', 'H', 'S'], ne.suit, ["current"])
        '''is royal'''
        self.attribute_map.add("is_royal_prev2", "is_royal(previous2)", [True, False], ne.is_royal, ["previous2"])
        self.attribute_map.add("is_royal_prev", "is_royal(previous)", [True, False], ne.is_royal, ["previous"])
        self.attribute_map.add("is_royal_cur", "is_royal(current)", [True, False], ne.is_royal, ["current"])

        '''compare card to value (value(card) < val) and (value(card) > val)'''
        self.attribute_map.add("val_greater_a_prev2", "greater(value(previous2),A)", [True, False], self.val_greater, ["previous2", 1])
        self.attribute_map.add("val_less_2_prev2", "less(value(previous2),2)", [True, False], self.val_less, ["previous2", 2])
        self.attribute_map.add("val_greater_2_prev2", "greater(value(previous2),2)", [True, False], self.val_greater, ["previous2", 2])
        self.attribute_map.add("val_less_3_prev2", "less(value(previous2),3)", [True, False], self.val_less, ["previous2", 3])
        self.attribute_map.add("val_greater_3_prev2", "greater(value(previous2),3)", [True, False], self.val_greater, ["previous2", 3])
        self.attribute_map.add("val_less_4_prev2", "less(value(previous2),4)", [True, False], self.val_less, ["previous2", 4])
        self.attribute_map.add("val_greater_4_prev2", "greater(value(previous2),4)", [True, False], self.val_greater, ["previous2", 4])
        self.attribute_map.add("val_less_5_prev2", "less(value(previous2),5)", [True, False], self.val_less, ["previous2", 5])
        self.attribute_map.add("val_greater_5_prev2", "greater(value(previous2),5)", [True, False], self.val_greater, ["previous2", 5])
        self.attribute_map.add("val_less_6_prev2", "less(value(previous2),6)", [True, False], self.val_less, ["previous2", 6])
        self.attribute_map.add("val_greater_6_prev2", "greater(value(previous2),6)", [True, False], self.val_greater, ["previous2", 6])
        self.attribute_map.add("val_less_7_prev2", "less(value(previous2),7)", [True, False], self.val_less, ["previous2", 7])
        self.attribute_map.add("val_greater_7_prev2", "greater(value(previous2),7)", [True, False], self.val_greater, ["previous2", 7])
        self.attribute_map.add("val_less_8_prev2", "less(value(previous2),8)", [True, False], self.val_less, ["previous2", 8])
        self.attribute_map.add("val_greater_8_prev2", "greater(value(previous2),8)", [True, False], self.val_greater, ["previous2", 8])
        self.attribute_map.add("val_less_9_prev2", "less(value(previous2),9)", [True, False], self.val_less, ["previous2", 9])
        self.attribute_map.add("val_greater_9_prev2", "greater(value(previous2),9)", [True, False], self.val_greater, ["previous2", 9])
        self.attribute_map.add("val_less_10_prev2", "less(value(previous2),10)", [True, False], self.val_less, ["previous2", 10])
        self.attribute_map.add("val_greater_10_prev2", "greater(value(previous2),10)", [True, False], self.val_greater, ["previous2", 10])
        self.attribute_map.add("val_less_j_prev2", "less(value(previous2),J)", [True, False], self.val_less, ["previous2", 11])
        self.attribute_map.add("val_greater_j_prev2", "greater(value(previous2),J)", [True, False], self.val_greater, ["previous2", 11])
        self.attribute_map.add("val_less_q_prev2", "less(value(previous2),Q)", [True, False], self.val_less, ["previous2", 12])
        self.attribute_map.add("val_greater_q_prev2", "greater(value(previous2),Q)", [True, False], self.val_greater, ["previous2", 12])
        self.attribute_map.add("val_less_k_prev2", "less(value(previous2),K)", [True, False], self.val_less, ["previous2", 13])

        self.attribute_map.add("val_greater_a_prev", "greater(value(previous),A)", [True, False], self.val_greater, ["previous", 1])
        self.attribute_map.add("val_less_2_prev", "less(value(previous),2)", [True, False], self.val_less, ["previous", 2])
        self.attribute_map.add("val_greater_2_prev", "greater(value(previous),2)", [True, False], self.val_greater, ["previous", 2])
        self.attribute_map.add("val_less_3_prev", "less(value(previous),3)", [True, False], self.val_less, ["previous", 3])
        self.attribute_map.add("val_greater_3_prev", "greater(value(previous),3)", [True, False], self.val_greater, ["previous", 3])
        self.attribute_map.add("val_less_4_prev", "less(value(previous),4)", [True, False], self.val_less, ["previous", 4])
        self.attribute_map.add("val_greater_4_prev", "greater(value(previous),4)", [True, False], self.val_greater, ["previous", 4])
        self.attribute_map.add("val_less_5_prev", "less(value(previous),5)", [True, False], self.val_less, ["previous", 5])
        self.attribute_map.add("val_greater_5_prev", "greater(value(previous),5)", [True, False], self.val_greater, ["previous", 5])
        self.attribute_map.add("val_less_6_prev", "less(value(previous),6)", [True, False], self.val_less, ["previous", 6])
        self.attribute_map.add("val_greater_6_prev", "greater(value(previous),6)", [True, False], self.val_greater, ["previous", 6])
        self.attribute_map.add("val_less_7_prev", "less(value(previous),7)", [True, False], self.val_less, ["previous", 7])
        self.attribute_map.add("val_greater_7_prev", "greater(value(previous),7)", [True, False], self.val_greater, ["previous", 7])
        self.attribute_map.add("val_less_8_prev", "less(value(previous),8)", [True, False], self.val_less, ["previous", 8])
        self.attribute_map.add("val_greater_8_prev", "greater(value(previous),8)", [True, False], self.val_greater, ["previous", 8])
        self.attribute_map.add("val_less_9_prev", "less(value(previous),9)", [True, False], self.val_less, ["previous", 9])
        self.attribute_map.add("val_greater_9_prev", "greater(value(previous),9)", [True, False], self.val_greater, ["previous", 9])
        self.attribute_map.add("val_less_10_prev", "less(value(previous),10)", [True, False], self.val_less, ["previous", 10])
        self.attribute_map.add("val_greater_10_prev", "greater(value(previous),10)", [True, False], self.val_greater, ["previous", 10])
        self.attribute_map.add("val_less_j_prev", "less(value(previous),J)", [True, False], self.val_less, ["previous", 11])
        self.attribute_map.add("val_greater_j_prev", "greater(value(previous),J)", [True, False], self.val_greater, ["previous", 11])
        self.attribute_map.add("val_less_q_prev", "less(value(previous),Q)", [True, False], self.val_less, ["previous", 12])
        self.attribute_map.add("val_greater_q_prev", "greater(value(previous),Q)", [True, False], self.val_greater, ["previous", 12])
        self.attribute_map.add("val_less_k_prev", "less(value(previous),K)", [True, False], self.val_less, ["previous", 13])

        self.attribute_map.add("val_greater_a_cur", "greater(value(current),A)", [True, False], self.val_greater, ["current", 1])
        self.attribute_map.add("val_less_2_cur", "less(value(current),2)", [True, False], self.val_less, ["current", 2])
        self.attribute_map.add("val_greater_2_cur", "greater(value(current),2)", [True, False], self.val_greater, ["current", 2])
        self.attribute_map.add("val_less_3_cur", "less(value(current),3)", [True, False], self.val_less, ["current", 3])
        self.attribute_map.add("val_greater_3_cur", "greater(value(current),3)", [True, False], self.val_greater, ["current", 3])
        self.attribute_map.add("val_less_4_cur", "less(value(current),4)", [True, False], self.val_less, ["current", 4])
        self.attribute_map.add("val_greater_4_cur", "greater(value(current),4)", [True, False], self.val_greater, ["current", 4])
        self.attribute_map.add("val_less_5_cur", "less(value(current),5)", [True, False], self.val_less, ["current", 5])
        self.attribute_map.add("val_greater_5_cur", "greater(value(current),5)", [True, False], self.val_greater, ["current", 5])
        self.attribute_map.add("val_less_6_cur", "less(value(current),6)", [True, False], self.val_less, ["current", 6])
        self.attribute_map.add("val_greater_6_cur", "greater(value(current),6)", [True, False], self.val_greater, ["current", 6])
        self.attribute_map.add("val_less_7_cur", "less(value(current),7)", [True, False], self.val_less, ["current", 7])
        self.attribute_map.add("val_greater_7_cur", "greater(value(current),7)", [True, False], self.val_greater, ["current", 7])
        self.attribute_map.add("val_less_8_cur", "less(value(current),8)", [True, False], self.val_less, ["current", 8])
        self.attribute_map.add("val_greater_8_cur", "greater(value(current),8)", [True, False], self.val_greater, ["current", 8])
        self.attribute_map.add("val_less_9_cur", "less(value(current),9)", [True, False], self.val_less, ["current", 9])
        self.attribute_map.add("val_greater_9_cur", "greater(value(current),9)", [True, False], self.val_greater, ["current", 9])
        self.attribute_map.add("val_less_10_cur", "less(value(current),10)", [True, False], self.val_less, ["current", 10])
        self.attribute_map.add("val_greater_10_cur", "greater(value(current),10)", [True, False], self.val_greater, ["current", 10])
        self.attribute_map.add("val_less_j_cur", "less(value(current),J)", [True, False], self.val_less, ["current", 11])
        self.attribute_map.add("val_greater_j_cur", "greater(value(current),J)", [True, False], self.val_greater, ["current", 11])
        self.attribute_map.add("val_less_q_cur", "less(value(current),Q)", [True, False], self.val_less, ["current", 12])
        self.attribute_map.add("val_greater_q_cur", "greater(value(current),Q)", [True, False], self.val_greater, ["current", 12])
        self.attribute_map.add("val_less_k_cur", "less(value(current),K)", [True, False], self.val_less, ["current", 13])

        '''compare card to suit (suit(card) <> suit), C < D < H < S.'''
        self.attribute_map.add("suit_greater_C_prev2", "greater(suit(previous2),C)", [True, False], self.suit_greater, ["previous2", 'C'])
        self.attribute_map.add("suit_less_D_prev2", "less(suit(previous2),D)", [True, False], self.suit_less, ["previous2", 'D'])
        self.attribute_map.add("suit_greater_D_prev2", "greater(suit(previous2),D)", [True, False], self.suit_greater, ["previous2", 'D'])
        self.attribute_map.add("suit_less_H_prev2", "less(suit(previous2),H)", [True, False], self.suit_less, ["previous2", 'H'])
        self.attribute_map.add("suit_greater_H_prev2", "greater(suit(previous2),H)", [True, False], self.suit_greater, ["previous2", 'H'])
        self.attribute_map.add("suit_less_S_prev2", "less(suit(previous2),S)", [True, False], self.suit_less, ["previous2", 'S'])

        self.attribute_map.add("suit_greater_C_prev", "greater(suit(previous),C)", [True, False], self.suit_greater, ["previous", 'C'])
        self.attribute_map.add("suit_less_D_prev", "less(suit(previous),D)", [True, False], self.suit_less, ["previous", 'D'])
        self.attribute_map.add("suit_greater_D_prev", "greater(suit(previous),D)", [True, False], self.suit_greater, ["previous", 'D'])
        self.attribute_map.add("suit_less_H_prev", "less(suit(previous),H)", [True, False], self.suit_less, ["previous", 'H'])
        self.attribute_map.add("suit_greater_H_prev", "greater(suit(previous),H)", [True, False], self.suit_greater, ["previous", 'H'])
        self.attribute_map.add("suit_less_S_prev", "less(suit(previous),S)", [True, False], self.suit_less, ["previous", 'S'])

        self.attribute_map.add("suit_greater_C_cur", "greater(suit(current),C)", [True, False], self.suit_greater, ["current", 'C'])
        self.attribute_map.add("suit_less_D_cur", "less(suit(current),D)", [True, False], self.suit_less, ["current", 'D'])
        self.attribute_map.add("suit_greater_D_cur", "greater(suit(current),D)", [True, False], self.suit_greater, ["current", 'D'])
        self.attribute_map.add("suit_less_H_cur", "less(suit(current),H)", [True, False], self.suit_less, ["current", 'H'])
        self.attribute_map.add("suit_greater_H_cur", "greater(suit(current),H)", [True, False], self.suit_greater, ["current", 'H'])
        self.attribute_map.add("suit_less_S_cur", "less(suit(current),S)", [True, False], self.suit_less, ["current", 'S'])

        '''compare two cards (card1 <> card2)'''
        self.attribute_map.add("less_prev_prev2", "less(previous,previous2)", [True, False], ne.less, ["previous", "previous2"])
        self.attribute_map.add("greater_prev_prev2", "greater(previous,previous2)", [True, False], ne.greater, ["previous", "previous2"])
        self.attribute_map.add("less_cur_prev", "less(current,previous)", [True, False], ne.less, ["current", "previous"])
        self.attribute_map.add("greater_cur_prev", "greater(current,previous)", [True, False], ne.greater, ["current", "previous"])
        self.attribute_map.add("less_prev2_cur", "less(previous2,current)", [True, False], ne.less, ["previous2", "current"])
        self.attribute_map.add("greater_prev2_cur", "greater(previous2,current)", [True, False], ne.greater, ["previous2", "current"])

        '''compare suits of two cards (suit(card1) <> suit(card2))'''
        self.attribute_map.add("suit_less_prev_prev2", "less(suit(previous),suit(previous2))", [True, False], self.suit_less, ["previous", "previous2"])
        self.attribute_map.add("suit_greater_prev_prev2", "greater(suit(previous),suit(previous2))", [True, False], self.suit_greater, ["previous", "previous2"])
        self.attribute_map.add("suit_less_cur_prev", "less(suit(current),suit(previous))", [True, False], self.suit_less, ["current", "previous"])
        self.attribute_map.add("suit_greater_cur_prev", "greater(suit(current),suit(previous))", [True, False], self.suit_greater, ["current", "previous"])
        self.attribute_map.add("suit_less_prev2_cur", "less(suit(previous2),suit(current))", [True, False], self.suit_less, ["previous2", "current"])
        self.attribute_map.add("suit_greater_prev2_cur", "greater(suit(previous2),suit(current))", [True, False], self.suit_greater, ["previous2", "current"])

        '''compare colors of two cards (color(card1) <> color(card2)). Not sure if this one's necessary'''
        self.attribute_map.add("color_less_prev_prev2", "less(color(previous),color(previous2))", [True, False], self.color_less, ["previous", "previous2"])
        self.attribute_map.add("color_greater_prev_prev2", "greater(color(previous),color(previous2))", [True, False], self.color_greater, ["previous", "previous2"])
        self.attribute_map.add("color_less_cur_prev", "less(color(current),color(previous))", [True, False], self.color_less, ["current", "previous"])
        self.attribute_map.add("color_greater_cur_prev", "greater(color(current),color(previous))", [True, False], self.color_greater, ["current", "previous"])
        self.attribute_map.add("color_less_prev2_cur", "less(color(previous2),color(current))", [True, False], self.color_less, ["previous2", "current"])
        self.attribute_map.add("color_greater_prev2_cur", "greater(color(previous2),color(current))", [True, False], self.color_greater, ["previous2", "current"])

        '''compare values of two cards (value(card1) <> value(card2))'''
        self.attribute_map.add("val_less_prev_prev2", "less(value(previous),value(previous2))", [True, False], self.val_less, ["previous", "previous2"])
        self.attribute_map.add("val_greater_prev_prev2", "greater(value(previous),value(previous2))", [True, False], self.val_greater, ["previous", "previous2"])
        self.attribute_map.add("val_less_cur_prev", "less(value(current),value(previous))", [True, False], self.val_less, ["current", "previous"])
        self.attribute_map.add("val_greater_cur_prev", "greater(value(current),value(previous))", [True, False], self.val_greater, ["current", "previous"])
        self.attribute_map.add("val_less_prev2_cur", "less(value(previous2),value(current))", [True, False], self.val_less, ["previous2", "current"])
        self.attribute_map.add("val_greater_prev2_cur", "greater(value(previous2),value(current))", [True, False], self.val_greater, ["previous2", "current"])

        '''difference in value of two cards (value(card1) - value(card2) = {-12, -11, ..., 11, 12})'''
        '''equal(value(previous),minus1(minus1(minus1(value(current))))'''
        self.attribute_map.add("diff_val_prev_prev2", "special_diff_val_prev_prev2", range(-12, 13), self.val_diff, ["previous", "previous2"])
        self.attribute_map.add("diff_val_cur_prev", "special_diff_val_cur_prev", range(-12, 13), self.val_diff, ["current", "previous"])
        self.attribute_map.add("diff_val_prev2_cur", "special_diff_val_prev2_cur", range(-12, 13), self.val_diff, ["previous2", "current"])

        '''difference in suit of two cards (suit(card1) - suit(card2) = {-3, -2, ..., 2, 3}). C < D < H < S'''
        self.attribute_map.add("diff_suit_prev_prev2", "special_diff_suit_prev_prev2", range(-3, 4), self.suit_diff, ["previous", "previous2"])
        self.attribute_map.add("diff_suit_cur_prev", "special_diff_suit_cur_prev", range(-3, 4), self.suit_diff, ["current", "previous"])
        self.attribute_map.add("diff_suit_prev2_cur", "special_diff_suit_prev2_cur", range(-3, 4), self.suit_diff, ["previous2", "current"])

        '''difference in two cards (card1 - card2 = {1, -1, 2, -2, ..., 51, -51})'''
        self.attribute_map.add("diff_card_prev_prev2", "special_card_diff_prev_prev2", range(-52, 53), self.diff, ["previous", "previous2"])
        self.attribute_map.add("diff_card_cur_prev", "special_card_diff_cur_prev", range(-52, 53), self.diff, ["current", "previous"])
        self.attribute_map.add("diff_card_prev2_cur", "special_card_diff_prev2_cur", range(-52, 53), self.diff, ["previous2", "current"])

    def diff(self, card1, card2):
        """
        return the difference between any two cards
        :param card1:
        :param card2:
        :return:
        """
        suit_d = self.suit_diff(card1, card2)
        val_d = self.val_diff(card1, card2)
        return (suit_d * 13) + val_d

    @staticmethod
    def suit_diff(card1, card2):
        """
        return the difference in card suits
        :param card1:
        :param card2:
        :return:
        """
        suits = ['C', 'D', 'H', 'S']
        suit1 = suits.index(ne.suit(card1))
        suit2 = suits.index(ne.suit(card2))
        return suit1 - suit2

    @staticmethod
    def val_diff(card1, card2):
        """
        return difference in card values
        :param card1:
        :param card2:
        :return:
        """
        return ne.value(card1) - ne.value(card2)

    @staticmethod
    def color_less(card1, card2):
        """
        return if color of card1 is less than color of card2
        :param card1:
        :param card2:
        :return:
        """
        return ne.less(ne.color(card1), ne.color(card2))

    @staticmethod
    def color_greater(card1, card2):
        """
        return if color of card1 is greater than color of card2
        :param card1:
        :param card2:
        :return:
        """
        return ne.greater(ne.color(card1), ne.color(card2))

    @staticmethod
    def suit_less(card1, card2):
        """
        return if suit of card1 is less than suit of card2
        :param card1:
        :param card2:
        :return:
        """
        if ne.is_suit(card2):
            return ne.less(ne.suit(card1), card2)
        else:
            return ne.less(ne.suit(card1), ne.suit(card2))

    @staticmethod
    def suit_greater(card1, card2):
        """
        return if suit of card1 is greater than suit of card2
        :param card1:
        :param card2:
        :return:
        """
        if ne.is_suit(card2):
            return ne.greater(ne.suit(card1), card2)
        else:
            return ne.greater(ne.suit(card1), ne.suit(card2))

    @staticmethod
    def val_less(card1, card2):
        """
        helper function needed to compare a card with the value of a card
        :param card1:
        :param card2:
        :return:
        """
        if isinstance(card2, int):
            return ne.value(card1) < card2
        else:
            return ne.value(card1) < ne.value(card2)

    @staticmethod
    def val_greater(card1, card2):
        """
        helper function needed to compare a card with the value of a card
        :param card1:
        :param card2:
        :return:
        """
        if isinstance(card2, int):
            return ne.value(card1) > card2
        else:
            return ne.value(card1) > ne.value(card2)

    @staticmethod
    def get_attribute_value(function, var_list):
        """
        calls function with variables var_list
        :param function:
        :param var_list:
        :return:
        """
        return function(*var_list)

    def add(self, previous2, previous, current, result):
        """
        Creates a row of table. Start with only color() and isEven()
        attribute list:
            [color(previous2), color(previous), color(current), even(previous2), even(previous), even(current)
        :param previous2:
        :param previous:
        :param current:
        :param result:
        :return:
        """
        row = []
        all_attrs = []
        for sub_attr_list in self.attribute_names:
            all_attrs.extend(sub_attr_list)
        for attr_name in all_attrs:
            attr_info = self.attribute_map.get(attr_name)
            params = []
            for key in attr_info[3]:
                if key == "previous2":
                    params.append(previous2)
                elif key == "previous":
                    params.append(previous)
                elif key == "current":
                    params.append(current)
                else:
                    params.append(key)

            attr_val = self.get_attribute_value(attr_info[2], params)
            row.append(attr_val)

        row.append(result)
        self.attribute_table.append(row)

    def build_tree(self):
        """
        Call helper function to build decision tree by recursively splitting table on fields with highest information
        gain (gain ratio later) until each leaf node has only true or only false
        :return: root node if successful or None otherwise
        """
        valid_attr_names = []
        attr_index = 0

        result = False
        while not result and attr_index < len(self.attribute_names):
            valid_attr_names.extend(self.attribute_names[attr_index])
            result = self.build_decision_tree(self.attribute_table, self.hypothesis_root, list(valid_attr_names))
            attr_index += 1
        if result is False:
            print 'NO RULE FOUND! THIS SHOULD NEVER HAPPEN! GOD HELP US :P'
            return None
        return self.hypothesis_root

    def build_decision_tree(self, table, node, valid_attr_names):
        """
        Recursive helper function to build tree
        :param table:
        :param node:
        :param valid_attr_names:
        :return:
        """
        # get attribute with highest info gain (or gain ratio)
        if self.is_table_leaf(table):
            if len(table) == 0:
                result = random.randrange(0, 1, 1)
                if result is True:
                    node.set_name("True")
                else:
                    node.set_name("False")
                return True

            if table[0][-1] is True:
                node.set_name("True")
            else:
                node.set_name("False")
            return True
        if self.has_valid_attrs(valid_attr_names) is False:
            return False

        attribute_index = self.get_splitting_attribute(table, valid_attr_names)
        node.set_name(valid_attr_names[attribute_index])

        # get list of tables each with one value of attribute
        split_tables = self.get_split_tables(table, attribute_index, valid_attr_names)
        valid_attr_names[attribute_index] = None

        # set child nodes of parent
        children = []
        for item in range(len(split_tables)):
            children.append(dtn.DecisionTreeNode())
            valid_attr_names_copy = valid_attr_names[:]
            result = self.build_decision_tree(split_tables[item], children[item], valid_attr_names_copy)
            if result is False:
                return False

        node.set_child_list(children)

        return True

    @staticmethod
    def has_valid_attrs(valid_attr_names):
        """
        It will check whether it has any valid attribute to split
        :param valid_attr_names:
        :return: Boolean
        """
        for attr in valid_attr_names:
            if attr is not None:
                return True
        return False

    def is_table_leaf(self, table):
        """
        Checks whether it has same classification or not
        :param table:
        :return: Boolean
        """
        positive_examples = self.get_num_positive(table)
        negative_examples = len(table) - positive_examples

        if positive_examples == 0 or negative_examples == 0:
            return True
        return False

    def get_splitting_attribute(self, table, valid_attr_names):
        """
        Return the index of the attribute which splits the table with the highest info gain (or gain ratio)
        :param table:
        :param valid_attr_names:
        :return: Index
        """
        p = self.get_num_positive(table)
        n = len(table) - p
        max_gain_ratio = -1
        max_gr_index = -1
        for attr_index in range(len(valid_attr_names)):
            attr = valid_attr_names[attr_index]
            if attr is not None:
                values = self.get_split_tables(table, attr_index, valid_attr_names)
                gain = self.entropy(p / (n + p))
                iv = 0
                for item in values:
                    pk = self.get_num_positive(item)
                    nk = len(item) - pk
                    if pk == 0 and nk == 0:
                        gain -= 0
                        iv -= 0
                    else:
                        gain -= ((pk + nk) / (p + n)) * self.entropy(pk / (pk + nk))
                        iv -= ((pk + nk) / (p + n)) * math.log((pk + nk) / (p + n), 2)
                if gain == 0:
                    gain_ratio = 0
                else:
                    gain_ratio = gain / iv

                # print("  ", attr, " gain ratio: ", gain_ratio)
                if gain_ratio > max_gain_ratio:
                    max_gain_ratio = gain_ratio
                    max_gr_index = attr_index

        return max_gr_index

    @staticmethod
    def get_num_positive(table):
        """
        Returns number of positive examples
        :param table:
        :return:
        """
        positive_examples = 0.0
        for row in table:
            if row[-1] is True:
                positive_examples += 1
        return positive_examples

    def get_split_tables(self, table, attr_index, valid_attr_names):
        """
        Returns a lits of tables derived by splitting table by each value in attribute_name(attr_index)
        :param valid_attr_names:
        :param table:
        :param attr_index:
        :return:
        """
        attr = valid_attr_names[attr_index]
        domain = self.attribute_map.get(attr)[1]
        tables = []
        for _ in domain:
            tables.append([])

        for row in table:
            val = row[attr_index]
            dom_index = domain.index(val)
            tables[dom_index].append(row)
        return tables

    @staticmethod
    def entropy(val):
        """
        Returns a entropy for this value
        :param val:
        :return: entropy
        """
        if val == 0 or val == 1:
            return 0
        result = -(val * math.log(val, 2) + (1-val)*math.log(1-val, 2))
        return result

    def print_tree(self, root, layer=0):
        """
        Print the rule tree
        :param root:
        :param layer:
        :return:
        """
        if layer != 0:
            for i in range(0, layer - 1):
                sys.stdout.write('|   ')
            sys.stdout.write('|___')

        print root.name

        if (root.name != "True") and (root.name != "False"):
            for child in root.childList:
                self.print_tree(child, layer + 1)

    def get_hypo_expression(self):
        """
        Returns an beautifully well-formed expression for the current hypothesis
        :return:
        """
        DecisionTree.rule = []
        root_child = self.hypothesis_root.child_list()
        if len(root_child) == 0:
            return "equal(True, " + self.hypothesis_root.name + ")"
        self.expression(self.hypothesis_root, [])
        return self.rulemaking()

    def expression(self, hypothesis_root, exp1):
        """
        Takes the hypothesis root and finds the paths which are true in the decision tree
        :param hypothesis_root:
        :param exp1:
        :return:
        """
        child_list = hypothesis_root.child_list()
        if child_list:
            atr_info = self.attribute_map.get(hypothesis_root.name)
            output_list = atr_info[1]
            func_name = atr_info[0]

            for i in range(len(child_list)):

                input1 = "(equal(" + func_name + "," + str(output_list[i]) + "))"
                exp1.append(input1)

                if child_list[i].name == "False":
                    exp1.pop(len(exp1) - 1)
                elif child_list[i].name == "True":
                    exp1_copy = exp1[:]
                    DecisionTree.rule.append(exp1_copy)
                    exp1.pop(len(exp1) - 1)

                else:
                    self.expression(child_list[i], exp1)
        if exp1:
            exp1.pop(len(exp1) - 1)

    @staticmethod
    def rulemaking():
        """
        converting the rule to the form that tree in new_eleusis can parse
        :return:
        """
        exp = ''
        fexp = ''
        i = 0
        j = 0
        for orterm in DecisionTree.rule:

            for andterm in orterm:
                i += 1
                if i > 2:
                    exp = "andf(" + exp[:-1] + "),"
                    i = 2
                exp += str(andterm[1:-1]) + ","
            i = 0
            j += 1
            if j > 2:
                fexp = "orf(" + fexp[:-1] + "),"
                j = 2
            if len(orterm) != 1:
                fexp += "andf(" + exp[:-1] + "),"
            else:
                fexp += orterm[0][1:-1] + ','
            exp = ''

        if len(DecisionTree.rule) != 1:
            fexp = "orf(" + fexp[:-1] + ")"
        else:
            fexp = fexp[:-1]
        return fexp
