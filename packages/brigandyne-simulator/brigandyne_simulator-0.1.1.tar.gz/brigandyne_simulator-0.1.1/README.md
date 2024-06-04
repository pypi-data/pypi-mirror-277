# brigandyne-simulator
A python simulator to enable the calculation of fighting statistics in the [Brigandyne TTRPG](https://brigandyne.wordpress.com/).

If you encounter a bug, [open an issue](https://github.com/remi-rc/brigandyne-simulator/issues).

If you want to contribute, pull requests are welcome :)

Contact : Rémi Necnor, remi.necnor@gmail.com

## Installation

To install brigandyne-simulator, you can use pip:

```bash
pip install brigandyne-simulator
```

## Usage
Load the package
```python
import brigandyne as br
```

An *Actor*  is the basic implementation of character and monsters of Brigandyne. You can instantiate one with 

```python
Anton = br.Actor(combat=46, movement=35, health=22, damage=3, protection=2, name="Anton The Immortal")
```

You can print info on an Actor using the print function
```python
print(Anton)
```

You can create teams of characters and monsters 

```python
# Monsters
gobelin_1 = br.Actor(combat=32, movement=35, health=8, damage=1, protection=1, size=0, name="gobelin_1")
gobelin_2 = br.Actor(combat=31, movement=35, health=6, damage=1, protection=1, size=0, name="gobelin_2")
gobelin_3 = br.Actor(combat=30, movement=35, health=9, damage=1, protection=1, size=0, name="gobelin_3")
ogre = br.Actor(combat=45, health=31, damage=7, protection=1, movement=35, name="ogre")

# Player characters
char_1 = br.Actor(combat=45, movement=35, health=18, damage=4, protection=2, size=1, dmg_threshold_to_prone=100, name="char_1")
char_2 = br.Actor(combat=45, movement=35, health=16, damage=4, protection=2, size=1, dmg_threshold_to_prone=100, name="char_2")
char_3 = br.Actor(combat=50, movement=40, health=22, damage=5, protection=2, size=1, dmg_threshold_to_prone=100, name="char_3")

# Assemble teams
team_A = br.Team([char_1, char_1, char_3])
team_B = br.Team([gobelin_1, gobelin_2, gobelin_3, ogre])
```

And you can have them fight in order to predict the odds of a team winning the encounter

```python
N_test = 20,000  # Number of fights to perform
winrate, N_turns_mean = br.get_team_win_rate(team_A, team_B, N_test)
print("Team A wins {:.1f}% of the time, in {:.1f} turns on average".format(winrate * 100, N_turns_mean))
```
