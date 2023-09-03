# Use for scrolling text
import time
import sys

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
    def __init__(self, name):
        self.name = name

class Player(Character):
    def __init__(self, name):
        super().__init__(name)
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def use_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

class Enemy(Character):
    def __init__(self, name):
        super().__init__(name)

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

                                       # Left Path Story
            if go_direction == "Left" or go_direction == "left":
                horror_left_lines1 = [
                    "\nYou begin walking down the road to the left.",
                    "As you walk past the houses that line the path,\n",
                    "you realize that every single house is completely identical to the last.",
                    '\n"None of this makes any sense, why would they build these houses here?"\n',
                    "You think to yourself as you stop in front of one of the houses to get a closer look.",
                    "\nAs you scan your eyes across the strange structure, you notice the blinds rustle slightly.",
                    "The distance from the sidewalk to the window is too far to make out too many details.",
                    "You quickly power on your camera and look into the viewfinder.",
                    "You zoom into a single area in the window where you can see the blinds being bent back;\n",
                    "\nIs someone(something?) watching you?."]
                horror_left_lines2 = [      # Lines if player take picture
                    "\nYou focus the camera on the gap in the blinds and snap a photo.",
                    "\nThe flash lights up the exterior of the house for the briefest moment before\n",
                    "it is shrouded in darkness once again.\n",
                    "The moment the flash hits the window, the blinds pull back into place and\n",
                    "an ear-splitting animalistic cry of pain bursts through the night air.",
                    "\nYou start to step backwards to run, but it's too late.",
                    "\nThe screeching begins to multiply from all directions and",
                    "the sound of shattering glass fills the air.",
                    "\nTall, grey, lanky humanoid creatures burst from the windows of each house",
                    "Their bodies are grey almagamations of long-decayed flesh sewn together with oozing black tendrils.",
                    "\nTheir faces look as though they have been sewn on as well.."
                    "In a matter of seconds, a dozen or so of the Residents are on top you of you"
                ]
                horror_left_lines3 = [] # Lines if run away
                scroll_text(horror_left_lines1)
                horror_left_decision = input("\nWhat do you do? (take picture/run away): ")
                if horror_left_decision == "take picture":
                    scroll_text(horror_left_lines2) 
                elif horror_left_decision == "run away":
                    scroll_text(horror_left_lines3)
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
