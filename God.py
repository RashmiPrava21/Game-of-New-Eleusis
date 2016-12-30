import new_eleusis
import random

class God:
    instantiated = False
    instance = False

    def __init__(self):
        """
        Please don't use this method to construct the objects, use get_instance
        static method.
        """
        self.__rule_expression = None
        self.__board_state = []
        self.__player_score = list()
        self.__rounds_played = 0
        self.__card = []
        self.__players = []
        self.__rule_obj = None
        if God.instantiated:
            raise Exception("This is a single Ton class")

    @staticmethod
    def get_instance():

        """
        We included this method to make the God class a singleton class
        because in game there will be only one God
        :return: The instance of the God class
        """
        if God.instantiated is False:
            God.instance = God()
            God.instantiated = True
        return God.instance

    def set_rule(self, rule_expression):
        """
        please check readMe file to know the syntax and semantics of
        rule expression.
        :type rule_expression: rule expression string
        """
        self.__rule_expression = rule_expression
        self.__rule_obj = new_eleusis.parse(rule_expression)

    def __update_board_state(self, card, result):
        """
        Update the board state by either adding a new tuple if the result is correct
        or adding the card to the incorrect list of the last tuple if the result is
        incorrect.
        Inputs: latest card played, result of played card
        Outputs: None
        """
        if result:
            # add new tuple with card as first element and empty list as second element
            self.__board_state.append((card, []))
        else:
            # add card to the end of the list in the last tuple
            self.__board_state[-1][1].append(card)

    def get_board_state(self):
        """
        This method creates a deep clone of board_state
        list( ) is only the shallow copy
        :return: returns the board state
        """
        result = list()
        for item in self.__board_state:
            if isinstance(item, list):
                result.append(list(item))
            else:
                result.append(item)
        return result

    def get_player_score(self, player_id):
        """
        :param player_id: player_id will be passed a first parameter while god creating
        player instance
        :return: score for the player
        """
        return self.__player_score[player_id]

    def __validate_with_rule(self, card):
        """
        :param card: card which we want to evaluate with rule
        :return: True or False
        """
        board = self.__board_state
        return self.__rule_obj.evaluate((board[-2][0], board[-1][0], card))

    def register_player(self, player_obj):
        """
        This method calls set_playerid method in player instance obj
        :param player_obj: expecting the player instance object
        :return: None
        """
        length = len(self.__players)
        self.__players.append(player_obj)
        player_obj.set_playerid(length)

    def get_shuffled_deck(self):
        deck = []
        for suit in ['C', 'D', 'H', 'S']:
            for i in range(1, 14):
                deck.append(new_eleusis.number_to_value(i) + suit)
        random.shuffle(deck)
        return deck

    def __update_score(self, player_id, result):
        """
        :param player_id: player_id to whom you want to udpate the score
        :param result: scores are based on the result
        :return:
        """
        player_score = 0
        if self.__rounds_played > 20:
            if result is True:
                player_score = 1
            else:
                player_score = 2
        self.__player_score[player_id] += player_score

    def play(self):
        """
        After registering all the players, calling play method will start the game
        :return:
        """
        # calculating how many 52 decks we need
        deck_count = (13*len(self.__players))/52 + 1
        cards_deck = list()
        for i in range(0, deck_count):
            cards_deck.extend(self.get_shuffled_deck())
        random.shuffle(cards_deck)

        # start distributing 13 cards to each player
        for i in range(0, len(self.__players)):
            player_cards = cards_deck[i:i+13]
            self.__card.append(player_cards)
            self.__players[i].set_cards(player_cards)

        # get ready step, this method help players to do any preprocess step
        for i in range(0, len(self.__players)):
            self.__players[i].pre_step()
        game_done = False
        while self.__rounds_played < 200:
            for i in range(0, len(self.__players)):
                card = self.__players[i].play_card()
                if card is None:
                    game_done = True
                    break
                result = self.__validate_with_rule(card)
                self.__update_score(i, result)
                self.__update_board_state(card, result)
                if game_done is True:
                    break
            self.__rounds_played += 1

        for i in range(0, len(self.__players)):
            rule = self.__players[i].get_rule()
            self.__player_score[i] -= self.test_hypothesis(rule)

    def test_hypothesis(self, player_rule_expression):
        """
        Test hypothesis against rule for all possible cards. If the hypothesis is correct
        for those all cards, return True. If it does not pass all cards test, add 15
        to the playerScore and return False. This decision tree will always produce a
        rule that describes the current board.
        input:
        output: True if correct, False otherwise
        returns: score with expression
        """
        num_correct = 0
        trials = 52*52*52
        # for trial in range(0, trials):
        for card0 in self.get_shuffled_deck():
            for card1 in self.get_shuffled_deck():
                for card2 in self.get_shuffled_deck():
                    # use our_rule to pick a card, then play that card. Test against dealer_rule
                    god_result = self.__rule_obj.evaluate((card0, card1, card2))
                    if (god_result == 'False') or (god_result == False):
                        god_result = False
                    else:
                        god_result = True
                    player_rule_obj = new_eleusis.parse(player_rule_expression)
                    our_result = player_rule_obj.evaluate((card0, card1, card2))
                    if (our_result == 'False') or (our_result == False):
                        our_result = False
                    else:
                        our_result = True

                    if god_result == our_result:
                        num_correct += 1
        # print results
        percent_correct = (num_correct * 1.0) / trials
        return percent_correct * 75

if __name__ == '__main__':
    god_instance = God()