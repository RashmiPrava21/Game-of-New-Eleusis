# Game-of-New-Eleusis #
------
New Eleusis is a slightly simplified version of Eleusis game.
 
If you want to build another Eleusis player and want to compete against other players, please follow these steps

* Folder structure
* API's need to expose
* Understanding internal data structure
* Syntax and Semantics of rule expression
* Scoring
* how to run

## Folder structure ##
Create a package in the players folder with your player name, and make sure to have a player.py file and fully implemented Player class, we will discuss what makes a Player class fully implemented.

## API's need to expose

* ***set_playerid( player__id )***
   This method is called from God which will give player Id, which we use for further communication with God.
* ***set_cards( cards )***
   God will give 13 cards before start of the game, you can use any of these 13 cards any number of times, but you need to use only given 13 cards.
* ***pre_step()***
  After cards distribution, God will call pre_step method, so that players can do any preprocessing steps here.
* ***play_card()***
When God calls this method you need to return the card or None, None returns says player is ready to return rule instead of the card.
* ***get_rule()***
When God calls this method player need to return the rule, it currently has.
* ***card_result( result )***
When you return card using play_card method, the feedback for the card is given using card_result method. feedback is boolean value True says return card is valid, False says return card is invalid.

## Understanding internal data structure
Most important question is how a player know what other players played. God internally maintains an entire board_state of the game, this board_state says what other players played.

The data structure for board state is python list of tuples. Each tuple has two elements.

    [ ( 5S, [ 6S ] ), ( 4D, [] ), ( 5C, [ 1D,6H,8S ] ) ]

The first value in a tuple is correct card some player played. The second value in a tuple is wrong cards played after correct card.

## Syntax and Semantics of rule expression
please refer to the new_eleusis.rtf file, open in MS word.

*** sample Rule expression and Description ***
> Alternate colour cards, i.e. a Black colour card need to be followed by red colour card and vice versa.

    if(equal(color(previous), B), equal(color(current), R), equal(color(current), B))

> Black colour card  always need to be followed by red colour card

    if(equal(color(previous), B), equal(color(current), R), True)

> playing card need to be royal card i.e. Jack, Queen or King

    if(is_royal(current), True, False)

## Scoring
A Player who has a minimum score is the winner.

* For every wrong card player will get +2 points
* For every right card player will get +1 points
* For the first 20 cards, player don't get any points.
* After rule is returned, your rule is validated with all possible cards. you will get  ***-(num__correct / all_possible_cards)*75***

## How to run

