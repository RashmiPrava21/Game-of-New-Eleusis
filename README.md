# Game-of-New-Eleusis #
------
New Eleusis is a slightly simplified version of Eleusis game.

If you want to build another Eleusis player and want to compete against other players, please follow these steps

* Folder structure
* API's need to expose
* Understanding internal data structure
* Syntax and Semantics of rule expression
* Scoring

## Folder structure ##
Create a package in the players folder with your player name, and make sure to have a player.py file and fully implemented Player class, we will discuss what makes a Player class fully implemented.

## API's need to expose

* ***set_playerid( player__id )***
   This method is called from God which will give player Id, which we use for further communication with God.
* * **set_cards( cards )** *
   God will give 13 cards before start of the game, you can use any of these 13 cards any number of times, but you need to use only given 13 cards.
* * **pre_step()** *
  After cards distribution, God will call pre_step method, so that players can do any preprocessing steps here.
* * **play_card()** *
When God calls this method you need to return the card or None, None returns says player is ready to return rule instead of the card.
* * ** get_rule() ** *
When God calls this method player need to return the rule, it currently has.
* * **card_result( result )** *
When you return card using play_card method, the feedback for the card is given using card_result method. feedback is boolean value True says return card is valid, False says return card is invalid.