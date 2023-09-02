# Used for scrolling text & random nums
import time
import sys
import random

# Scrolling text function
def scroll_text(lines, delay=0.03):
    for line in lines:
        if line.endswith('.'):
            line = line + '\n'
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)

class Character:
    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def attack(self, target, damage=20, crit=random.randint(1,4)):
        self.target = target
        if crit == 1:
            damage *= 1.25
        target.health -= damage
        
class Player(Character):
    def __init__(self, name):
        super().__init__(name, health=100)
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def use_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

    def attack(self, target, damage=20, crit=random.randint(1,4)):
        super().attack(target, damage, crit)
    def heal(self, chance=random.randint(1,8), amount=20):
        self.chance = chance
        self.amount = amount
        if chance >= 1 and chance <= 4:     # 50% chance hp + 20
            self.health += amount
        elif chance > 4 and chance <= 7:    # 37.5% chance hp + 30
            self.amount += 10
            self.health += self.amount
        elif chance == 8:                   # 12.5% chance hp + 42.5
            self.amount += 20
            self.health += self.amount
        else:
            print("An unexpected error has occured when generating random int")

class Enemy(Character):
    def __init__(self, name, health=100):
        super().__init__(name, health)

    def attack(self, target, damage=25):
        self.damage = damage
        target.health -= damage

# Doors, Chests, and Keys

class Door:
    def __init__(self, num, locked=True):
        self.num = num
        self.locked = locked

class KeyItem:
    def __init__(self, name):
        self.name = name

class Chest:
    def __init__(self, *items, locked=True):
        self.items = items
        self.locked = locked

# Welcome message & story/character creation
scroll_text("Welcome to the Interactive Adventure Experience!\n")
input("Press Enter to continue: ")
     #       Add prompt to select genre here
playerName = input("Choose a name for your character: ")
player = Player(playerName)

# Run Game
def startGame(genre):
    # Horror story main function
    def horror_story():
        horror_lines1 = [
            f"\nYou are {player.name}.",
            "\nYou live in Evergreen, a small town in Maine.",
            "It is a cool autumn night in September.",
            "You are a nature photographer; You walk through the dark outskirts of town where the\n",
            "trees stand tall and sway back and forth against the night breeze.",
            "The wind blows chillingly against your face as the moon rises in the sky in front of you.",
            "\nYou look further ahead and you notice you are approaching a T in the road.",
            "As you approach the intersection, the air grows still, and the previous\n",
            "sounds of the nightlife which one filled the air cease entirely.",
            "\nYou are filled with a strange anticipation.."]
        
        scroll_text(horror_lines1)

        # Lines for look direction choices
        horror_lines2 = [
                    "\nYou look down the road to the left and see it leads towards a seemingly endless stretch of houses,\n",
                    "not a single light can be seen coming from any of them.",
                    "They look as though they were just recently built.",
                    "Streetlights line the street as well, though their bulbs glow dimly,\n",
                    "almost as if they were dying."]
        horror_lines3=[
                    "You turn your head to look down the road to your right.",
                    "This path is completely obscured by evergreen trees on both sides.",
                    "The only light illuminating the path is the streaks of moonlight breaking through the canopy.",
                    "You cannot tell where it leads, but a strange curiosity builds as the trees sway."]
        
        while True:
            look_direction1 = input("Look to the left or to the right? (left/right): ") 
            if look_direction1 == "Left" or look_direction1 == "left":
                scroll_text(horror_lines2)
                break
            elif look_direction1 == "Right" or look_direction1 == "right":  
                scroll_text(horror_lines3)
                break
            else:
                scroll_text("Invalid direction, please try again.")

        while True:
            look_direction2 = input("\nLook in the opposite direction? (y/n): ")
            if look_direction2 == 'N' or look_direction2 == 'n':
                break
            elif look_direction2 == 'Y' or look_direction2 == 'y':
                if look_direction1 == "Left" or look_direction1 == "left":
                    scroll_text(horror_lines3)
                    break
                elif look_direction1 == "Right" or look_direction1 == "right":
                    scroll_text(horror_lines2)
                    break
        # Choose correct story for player direction
        while True:
            go_direction = input("\nWhich direction do you go? (left/right): ")
            if go_direction == "Left" or go_direction == "left":
                            # Left Path Story
                def horror_story_leftpath():
                    horror_left_lines1 = [
                        "\nYou begin walking down the road to the left.",
                        "As you walk past the houses that line the path,\n",
                        "you realize that every single house is completely identical to the last.",
                        '\n"None of this makes any sense, why would they build these houses here?"\n',
                        "You think to yourself as you stop in front of one of the houses to get a closer look.",
                        "\n"
                    ]
                    scroll_text(horror_left_lines1)
                horror_story_leftpath()
                break
            elif go_direction == "Right" or go_direction == "right":
                    # Right Path Story
                def horror_story_rightpath():
                    pass
                horror_story_rightpath()
        
    # Runs story creation function for genre
    if genre == "Horror" or genre == "horror":
        horror_story()

# Start Game
startGame("horror")
