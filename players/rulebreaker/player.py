import new_eleusis
import DecisionTree as dt
import God

class Player:
    def __init__(self):
        self.player_id = None
        self.our_hand = []
        self.our_rule_expression = None
        self.decision_tree = dt.DecisionTree()
        self.god_instance = God.God.get_instance()
        self.num_correct = 0
        self.num_incorrect = 0
        self.card_played = None
        self.num_consecutive_correct = 0
        self.confidence_value = 50

    def set_playerid(self, player_id):
        """
        player_id will set by the god
        :param player_id: player_id is unique for every player
        :return:
        """
        self.player_id = player_id

    def set_cards(self, cards):
        """
        cards will be given by the card every card we returns will be validated against their cards
        :param cards:
        :return:
        """
        self.our_hand = cards

    def pre_step(self):
        """
        This is pre_step that will be called before starting play
        :return:
        """
        board_state = self.god_instance.get_board_state()
        self.decision_tree.add(board_state[-3][0], board_state[-2][0], board_state[-1][0])
        self.our_rule_expression = self.decision_tree.get_hypo_expression()

    def play_card(self):
        """
        :return: next card to be returned
        """
        guess = True
        if self.num_correct > self.num_incorrect:
            guess = False
        else:
            guess = True
        if self.num_consecutive_correct >= self.confidence_value:
            return None
        for i in range(0,len(self.our_hand)):
            our_rule_obj = new_eleusis.parse(self.our_rule_expression)
            board_state = self.god_instance.get_board_state()
            our_result = our_rule_obj.evaluate(board_state[-2][0], board_state[-1][0], self.our_hand[i])
            our_result = bool(our_result)
            if our_result == guess:
                self.card_played = self.our_hand[i]
                return self.our_hand[i]
        return self.our_hand[0]

    def card_result(self, result):
        result = bool(result)
        board_state = self.god_instance.get_board_state()
        self.decision_tree.add( board_state[-2][0], board_state[-1][0], self.card_played)
        self.our_rule_expression = self.decision_tree.get_hypo_expression()
        if result:
            self.num_consecutive_correct += 1
        else:
            self.num_consecutive_correct = 0

    def get_rule(self):
        """
        This method will be called by God
        :return: rule
        """
        self.our_rule_expression  = self.decision_tree.get_hypo_expression()
        return self.our_rule_expression
