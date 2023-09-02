# Used for scrolling text
import time
import sys
# Characters

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

class Player(Character):
    def __init__(self, name):
        super().__init__(name, health=100)
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def use_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

class Enemy(Character):
    def __init__(self, name, health=100):
        super().__init__(name, health)

# Items

class Item:
    def __init__(self, description):
        self.description = description

# Weapon Items

class Weapon(Item):
    def __init__(self, description, ammo=None, durability=None):
        super().__init__(description)
        self.ammo = ammo
        self.durability = durability


class Pistol(Weapon): # Will be included in future stories
    def __init__(self, description, ammo=4):
        super().__init__(description, ammo)

    def shoot(self):
        if self.ammo > 0:
            self.ammo -= 1
        else:
            print("Out of ammo!")

class Knife(Weapon):
    def __init__(self, description, durability=100):
        self.description = description
        self.durability = durability

    def knife_attack(self):
        self.durability -= 10

# Hp Item

class HpItem(Item):
    def __init__(self, hp):
        super().__init__(description="This looks healthy.")
        self.hp = hp
    
    def heal(self, player):
        player.heath += self.hp

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

# Scrolling text function
def scroll_text(lines, delay=0.03):
    for line in lines:
        if line.endswith('.'):
            line = line + '\n'
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)

# Run Game
def startGame(genre):
    # Welcome message & story/character customization
    scroll_text("Welcome to the Interactive Adventure Experience!\n")
    input("Press Enter to continue: ")
    playerName = input("Choose a name for your character: ")
    player = Player(playerName)

    # Story intro function
    def horror_story_intro():
        horror_lines1 = [
            f"You are {player.name}.",
            "You live in Evergreen, a small town in Maine.",
            "It is a cool autumn night in September.",
            "You are a nature photographer; You walk through the dark outskirts of town where the\n",
            "trees stand tall and sway back and forth against the night breeze.",
            "The wind blows chillingly against your face as the moon rises in the sky in front of you.",
            "\nYou look further ahead and you notice you are approaching a T in the road.",
            "As you approach the intersection, the air grows still, and the previous\n",
            "sounds of the nightlife which one filled the air cease entirely.",
            "\nA strange anticipation fills you.."]
        
        scroll_text(horror_lines1)

        while True:
            look_direction = input("Look to the left or to the right?: ") 

            if look_direction == "Left" or look_direction == "left":
                horror_lines2 = [
                    "You look down the road to the left and see it leads towards a seemingly endless stretch of houses,\n",
                    "not a single light can be seen in any of them.",
                    "They look as though they were just recently built.",
                    "Streetlights line the street as well, though their bulbs glow dimly,\n",
                    "almost as if they were dying."]
                
                scroll_text(horror_lines2, 0.06)
                break

            elif look_direction == "Right" or look_direction == "right":
                horror_lines3=[
                    "You turn your head to look down the road to your right.",
                    "This path is completely obscured by evergreen trees on both sides.",
                    "The only light illuminating the path is the streaks of moonlight breaking through the canopy.",
                    "You cannot tell where it leads, but a strange curiosity builds as the trees sway."]
                
                scroll_text(horror_lines3, 0.06)
                break
            else:
                scroll_text("Invalid direction. Please try again.")
    
        while True:
            go_direction = input("Which direction do you go?: ")
            if go_direction != "Left" or go_direction != "left" or go_direction != "Right" or go_direction != "right":
                scroll_text("Invalid direction. Please try again.")
            else:
                break

    # Runs story creation function for genre
    if genre == "Horror" or genre == "horror":
        horror_story_intro()
        if go_direction == "Left" or go_direction == "left":

# Start Game
startGame("horror")
