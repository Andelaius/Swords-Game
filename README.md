# Swords-Game
### This is an implementation of the game Swords, a two-player game traditionally played with hands. This implementation is single-player, incorporating an AI opponent. 

## Rules of the Game:
Each player starts with one sword in each hand.
Players take turns either attacking or splitting (when possible).
An attack consists a player choosing one of their hands to hit one of the hands of the opponent.
An attack adds the number of swords from the chosen hand of the attacker to the chosen hand of the onpponent.
A split can only be executed when a player has one hand that has either 2 or 4 swords and one hand that is disarmed.
A split results in even distribution of swords across hands; an uneven split of swords is not allowed.
When a player's hand holds 5 swords, that hand becomes disarmed (holds 0 swords) and unusable.
When a player's hand is attacked and the number of swords >5, the attacked hand then holds the remainder of swords (new number / 5).
A player has lost once they are completely disarmed (both of their hands equal zero).

## How to Play:
The commands to attack or split are those words verbatum, respectively.
The commands to choose a right hand or left hand are r and l, respectively.
