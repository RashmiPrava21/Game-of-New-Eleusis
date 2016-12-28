"""
CMSC671: Artificial Intelligence Project Phase 2
12 December 2016
Rule Breakers:
    Vikramaditya Battina
    Sri Konuru
    Nikhil Kumar Mengani
    Alexander Spizler

This is the New Eleusis agent, containing all the required functions (setRule, rule, play, scientist, score) along with
the necessary helper functions. We call the function, play_game(gods_rule, card1, card2, card3), to play a game of New Eleusis.
"""
import random
import new_eleusis as ne
import DecisionTree as dt

"""
Global variables
"""
confidence = 0          # player's confidence in hypothesis
cards_played = 0        # total number of cards played
board = list()          # list of tuples representing game state
our_expression = ''     # Expression for our current rule (hypothesis)
our_rule = None         # Tree of our current rule (hypothesis)
rule_expression = ''    # Expression for dealer's rule
dealer_rule = None      # Tree of dealer's rule
player_score = 0         # player's score
guess_true = True        # Is card returned by selectNextCard a true or false example
decision_tree = dt.DecisionTree()   # representation of our current hypothesis in a decision tree


def check_expression(our_expression):
    pass


def play_game(gods_rule, card1, card2, card3):
    """
    Play a game of New Eleusis
    input: Expression for the rule, first two valid cards
    output: True if correct hypothesis made, False otherwise
    """
    global board, confidence, cards_played, player_score, we_returned_rule, our_expression

    # set dealer's rule
    setRule(gods_rule)

    # initialize board state
    board.append((card1, []))
    board.append((card2, []))
    board.append((card3, []))

    # get hypothesis from scientist (he plays all the cards he wants to play,
    # then returns rule)
    scientist()
    print "Our rule: " + our_expression
    correct_expression = test_hypothesis()

    print "Our score before end of game bonuses: " + str(player_score)

    if correct_expression:
        print "Logically equivalent hypothesis bonus! -75 points!"
        player_score -= 75
        if we_returned_rule:
            print "Our player returned the rule first bonus! -25 points!"
            player_score -= 25

    print "Final, awesome, score: " + str(player_score)

    return correct_expression


def scientist():
    """
    This function returns the rule your player has found. It is responsible
    for the inductive task, that is, figuring out the rule. When called,
    this function is responsible for making plays, considering the
    information gained, dealing with hypotheses*, and choosing when (after
    20+ plays) to declare success and return a rule.
    Inputs: None
    Outputs: Expression for current hypothesis if it thinks it is right,
        returns 'None' otherwise.
    :return:
    """
    global cards_played, decision_tree, our_rule, our_expression, guess_true, our_hand, we_returned_rule, num_adversaries, our_turn

    num_correct = 0
    num_adversaries = 3
    adv_stop = []
    for adv in range(num_adversaries):
        adv_stop.append(random.randrange(180) + 20)

    print "adversary limits: " + str(adv_stop)

    our_hand = get_shuffled_deck()[0:13]

    # build initial rule
    decision_tree.build_tree()
    our_expression = decision_tree.get_hypo_expression()
    our_rule = ne.parse(our_expression)
    while cards_played < 200:

        # our turn

        # decide whether or not to return hypothesis
        # print "cards played: " + str(cards_played)
        if num_correct > 50:
            we_returned_rule = True
            print "Our confident player is a real genius, and has decided to return a rule!"
            return our_expression

        # play our card
        card = select_next_card()
        print "card[" + str(cards_played) + "]: we play the " + card
        our_turn = True
        result = play(card)

        # Look at board state to determine if current hypothesis is
        # consistent. Otherwise, update hypothesis
        if result != guess_true:
            # update hypothesis with new information
            num_correct = 0
            decision_tree.build_tree()
            our_expression = decision_tree.get_hypo_expression()
            our_rule = ne.parse(our_expression)
        else:
            num_correct += 1
            if cards_played < 20:
                decision_tree.build_tree()
                our_expression = decision_tree.get_hypo_expression()
                our_rule = ne.parse(our_expression)

        # play adversary cards
        for adv in range(num_adversaries):
            # decide to randomly return rule
            if adv_stop[adv] <= cards_played:
                we_returned_rule = False
                print "Adversary " + str(adv) + " has audaciously decided to return a rule!"
                return our_expression

            # play random card
            card = get_shuffled_deck()[0]
            my_result = our_rule.evaluate((board[-2][0], board[-1][0], card))
            our_turn = False
            print "card[" + str(cards_played) + "]: adv[" + str(adv) + "] plays " + card
            result = play(card)

            # update board
            if result != my_result:
                # update hypothesis with new information
                num_correct = 0
                decision_tree.build_tree()
                our_expression = decision_tree.get_hypo_expression()
                our_rule = ne.parse(our_expression)
            else:
                num_correct += 1
                if cards_played < 20:
                    decision_tree.build_tree()
                    our_expression = decision_tree.get_hypo_expression()
                    our_rule = ne.parse(our_expression)


def get_random_card():
    """
    Select random card from a standard 52 card deck
    :return:
    """
    suits = ['C', 'D', 'H', 'S']
    suit = suits[random.randrange(4)]
    val = random.randrange(1, 14)
    return ne.number_to_value(val) + suit


def get_shuffled_deck():
    """
    Create and return a shuffled deck of cards
    :return:
    """
    deck = []
    for suit in ['C', 'D', 'H', 'S']:
        for i in range(1, 14):
            deck.append(ne.number_to_value(i) + suit)

    random.shuffle(deck)
    return deck


def select_next_card(force_true=False):
    """
    Use current hypothesis to select next card, sets flag for whether guess is
    true or false, such that it maintains an even distribution of True and False
    guesses. force_true is used to only produce True guesses when testing a
    hypothesis against god's rule at the end of the game.
    """
    global guess_true, our_rule, board, our_hand

    # decide whether to play a True guess or a False guess
    if not force_true:
        correct_guesses = len(board)
        incorrect_guesses = cards_played - correct_guesses
        if correct_guesses < incorrect_guesses:
            guess_true = True
        else:
            guess_true = False
    else:
        guess_true = True

    # randomize deck of 52 cards (change to # of cards in hand for Phase II)
    deck = get_shuffled_deck()

    # test each card until you find one that is valid (invalid if guess_true
    # is False) and return that card
    for card in deck:
        my_result = our_rule.evaluate((board[-2][0], board[-1][0], card))
        my_result = bool(my_result)
        if my_result == guess_true:
            if card in our_hand:
                # replace card from hand, and play
                return_card = card
                card_index = our_hand.index(card)
                our_hand[card_index] = get_shuffled_deck()[0]
                return return_card

    # if no desired card is found, return a random card
    guess_true = not guess_true
    return our_hand[0]


def setRule(expression):
    """
    Set the current dealer rule, using the functions provided in
    new_eleusis.py
    Inputs: String expression of dealer's rule
    Outputs: None
    """
    # Save expression as a global variable, ruleExpression
    global rule_expression, dealer_rule
    rule_expression = expression

    # Use Tree's parse(expression) to create Tree of rule
    dealer_rule = ne.parse(rule_expression)


def play(card):
    """
    Play a single card and return True or False for legal or illegal plays.
    This is probably a good place to update boardState
    Inputs: Card to play next
    Outputs: True if card successfully matches rule, false otherwise
    :param card:
    :return:
    """
    # update cards played
    global cards_played, decision_tree, our_turn
    cards_played += 1

    # Use Tree's rule.evaluate and previous two cards
    # if len(board) > 1:
    result = dealer_rule.evaluate((board[-2][0], board[-1][0], card))
    if result == "True":
        result = True
    if result == "False":
        result = False
    # result = bool(result)
    decision_tree.add(board[-2][0], board[-1][0], card, result)

    # Update board
    update_board_state(card, result)

    # Update global variable, score
    if our_turn:
        update_score(result)

    # Return if true
    return result


def test_hypothesis():
    """
    Test hypothesis against rule for next 10 cards. If the hypothesis is correct
    for those 10 cards, return True. If it does not pass the 10 card test, add 15
    to the playerScore and return False. This decision tree will always produce a
    rule that describes the current board.
    input:
    output: True if correct, False otherwise
    """
    global board, player_score

    num_correct = 0
    trials = 52*52*52
    # for trial in range(0, trials):

    print "Testing exact logical equivalency with all 3-card tuples..."

    for card0 in get_shuffled_deck():
        for card1 in get_shuffled_deck():
            for card2 in get_shuffled_deck():

                # use our_rule to pick a card, then play that card. Test against dealer_rule
                god_result = dealer_rule.evaluate((card0, card1, card2))
                if (god_result == 'False') or (god_result == False):
                    god_result = False
                else:
                    god_result = True

                our_result = our_rule.evaluate((card0, card1, card2))
                if (our_result == 'False') or (our_result == False):
                    our_result = False
                else:
                    our_result = True

                if god_result == our_result:
                    num_correct += 1

    # print results
    percent_correct = (num_correct * 1.0) / trials
    print "Our rule guesses " + str(percent_correct * 100)[0:6] + "% correctly"

    # return results
    if trials == num_correct:
        return True
    else:
        return False


def rule():
    """
    Return the current (actual) rule
    Inputs: None
    Outputs: Expression for dealer's rule
    """
    # Return expression for rule
    global rule_expression
    return rule_expression


def boardState():
    """
    Returns the formal representation of all plays so far as a sequential
    list of tuples, in order of play. Each tuple will contain a card played
    in the main sequence (that is, played successfully), then a list of all
    cards played unsuccessfully after it, which may be empty.
    Inputs: None
    Outputs: List of tuples containing all successful and unsuccessful plays
    """
    global board
    return board


def update_board_state(card, result):
    """
    Update the board state by either adding a new tuple if the result is correct
    or adding the card to the incorrect list of the last tuple if the result is
    incorrect.
    Inputs: latest card played, result of played card
    Outputs: None
    """
    global board
    if result:
        # add new tuple with card as first element and empty list as second element
        board.append((card, []))
    else:
        # add card to the end of the list in the last tuple
        board[-1][1].append(card)


def update_score(result):
    """
    Update player score. Add 1 for a successful play over 20 and under 200. Add 2
    for every failed play.
    Inputs:
    Outputs:
    """
    global cards_played, player_score
    if (cards_played > 20) and (cards_played < 200):
        if result:
            player_score += 1
        else:
            player_score += 2


def score():
    """
    Returns the score for the most recent round. (Low is better!)
    Calculate by adding points as follows: +1 for every successful play over
    20 and under 200; +2 for every failed play; +15 for a rule that is not
    equivalent to the correct rule; +30 for a rule that does not describe
    all cards on the board.
    Inputs: None
    Outputs: Score for most recent round
    """
    global player_score
    return player_score
