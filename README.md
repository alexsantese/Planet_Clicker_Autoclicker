# Planet Clicker Clicker Bot

A python-based auto-clicker bot for the game Planet Clicker on crazygames.io
The bot uses Pillow and numpy to take screenshots of the screen and then turn them into an array so it can be iterated
through to look for certain colored pixels and then click on them when upgrades are available. 

The bot will click for a certain amount of iterations and then click to the next planet and keep going, eventually cycling back to the first planet
after it loops through.
