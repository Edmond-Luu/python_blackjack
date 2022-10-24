# Python Blackjack Game

![image](https://user-images.githubusercontent.com/26613209/197585174-abb0eafe-f872-43ef-86a4-b33f16cfca98.png)

Welcome to my Python Blackjack game, the first major Python project that I made completely from scratch after learning Python. While this game is a fun and simple game that we all know about, this Python program has many features that many people would not even consider.

To test out the file, install <a href="https://python.org" rel="noreferrrer" target="_blank">Python</a> and use a text-editor like <a href="https://code.visualstudio.com" rel="noreferrer">Visual Studio Code</a>.

In this game, the user starts out with a set amount of money that can be adjusted and can place bets and keep playing until the user runs out of money or if the user types "q" in the input instead of an actual bet. After betting, the player is dealt 2 cards and can hit or stay. Afterwards, the dealer will get its cards and the game will automatically calculate the totals to decide who wins.

Here are some of the features of my Python Blackjack game:
* The minimum bet can be set and when a bet below the minimum bet is placed, there will be an error message asking the user to try again.
* If the user does not have enough money to place the minimum bet, the game is over.
* If the user places a bet that is above the amount of money available or if the user enters a non-integer value (except for "q," the command to quit), the game will display an error message and will ask the user to try again.
* On the first 2 cards dealt, the user, if he/she has sufficient funds, can choose to double. Doubling is basically being dealt a third card as the final card while doubling the current bet. It is optimal to double in this game if the user has a total value of 10 or 11 on his/her initial 2 cards since there will be a good chance that a 10, Jack, Queen, or King is dealt, either of which would bring up the total to 20 or 21, respectively.
  * If doubling is not allowed or if not possible due to insufficient funds, the game will automatically omit that option on its input prompt and users who attempt to select the double option will be given an error message and will be asked to try again.
* Jack, Queen, and King cards will automatically be converted to 10's.
* Ace cards will be converted to 11's if the total is less than 21. Otherwise, Aces will be converted to 1's.

I plan to add a functionality that would allow users to do a split if they have a pair of matching card values on the first 2 cards dealt. This process may be a little complex since it would require an additional hand on top of the current hand being played. Essentially, the user would now be playing 2 hands separately if this was the case.
