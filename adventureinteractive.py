# Use for scrolling text
import time
import sys

# Scrolling text function
def scroll_text(lines, delay=0.01):
    for line in lines:
        if line.endswith('.'):
            line = line + '\n'
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)

# Player 
class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def use_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

# Doors, Chests, and Keys
class Door:
    def __init__(self, num, locked=True):
        self.num = num
        self.locked = locked

class Key:
    def __init__(self, name):
        self.name = name

class Chest:
    def __init__(self, *items, locked=True):
        self.items = items
        self.locked = locked

# Welcome message & story/character creation
scroll_text("Welcome to Adventure Interactive!\n")
input("Press Enter to continue: ")
player = input("Choose a name for your character: ")

# Run Game
def start_game(genre):
    # Horror story main function
    def horror_story_main():
        horror_lines_main1 = [
            f"\nYou are {player}.",
            "\nYou live in Evergreen, a small town in Maine.",
            "It is a cool autumn night in September.",
            "You are a nature photographer; You walk through the dark outskirts of town where the\n",
            "trees stand tall and sway back and forth against the night breeze.",
            "The wind blows chillingly against your face as the moon rises in the sky in front of you.",
            "\nYou look further ahead and you notice you are approaching a T in the road.",
            "As you approach the intersection, the air grows still, and the previous\n",
            "sounds of the nightlife which one filled the air cease entirely.",
            "\nYou are filled with a strange anticipation.."]
        
        scroll_text(horror_lines_main1)

        # Lines for look direction choices
        horror_lines_main2 = [
            "\nYou look down the road to the left and see it leads towards a seemingly endless stretch of houses,\n",
            "not a single light can be seen coming from any of them.",
            "They look as though they were just recently built.",
            "Streetlights line the street as well, though their bulbs glow dimly,\n",
            "almost as if they were dying."]
        horror_lines_main3 = [
            "\nYou turn your head to look down the road to your right.",
            "This path is completely obscured by evergreen trees on both sides.",
            "The only light illuminating the path is the streaks of moonlight breaking through the canopy.",
            "You cannot tell where it leads, but a strange curiosity builds as the trees sway."]
        
        while True:
            look_direction1 = input("Look to the left or to the right? (left/right): ") 
            if look_direction1 == "Left" or look_direction1 == "left":
                scroll_text(horror_lines_main2)
                break
            elif look_direction1 == "Right" or look_direction1 == "right":  
                scroll_text(horror_lines_main3)
                break
            else:
                scroll_text("Invalid direction, please try again.")

        while True:
            look_direction2 = input("\nLook in the opposite direction? (y/n): ")
            if look_direction2 == 'N' or look_direction2 == 'n':
                break
            elif look_direction2 == 'Y' or look_direction2 == 'y':
                if look_direction1 == "Left" or look_direction1 == "left":
                    scroll_text(horror_lines_main3)
                    break
                elif look_direction1 == "Right" or look_direction1 == "right":
                    scroll_text(horror_lines_main2)
                    break
        # Choose correct story for player direction
        while True:
            go_direction = input("\nWhich direction do you go? (left/right): ")

            # Left Path Story
            if go_direction == "Left" or go_direction == "left":
                def horror_story_left():
                    horror_left_lines1 = [
                        "\nYou begin walking down the road to the left.",
                        "As you walk past the houses that line the path,\n",
                        "you realize that every single house is completely identical to the last.",
                        '\n"None of this makes any sense, why would they build these houses here?"\n',
                        "You think to yourself as you stop in front of one of the houses to get a closer look.",
                        "\nAs you scan your eyes across the strange structure, you notice the blinds rustle slightly.",
                        "The sidewalk is too far from the window to make out too many details.",
                        "You quickly power on your camera and look into the viewfinder.",
                        "You zoom into the window where you can see the blinds being bent back.",
                        "\nThe only thing you can make out is a bony finger poking through the gap."
                    ]
                    horror_left_lines2 = [      # Lines if player takes a picture
                        "\nYou focus the camera on the gap in the blinds and snap a photo.",
                        "\nThe flash lights up the exterior of the house for the briefest moment before\n",
                        "it is shrouded in darkness once again.",
                        "\nThe moment the flash hits the window, the blinds pull back into place and\n",
                        "an ear-splitting animalistic cry of pain bursts through the night air.",
                        "\nYou start to step backwards to run, but it's too late.",
                        "\nThe screeching begins to multiply from all directions and\n",
                        "the sound of shattering glass fills the air.",
                        "\nTall, grey, lanky humanoid creatures burst from the windows of each house.",
                        "Their bodies are grey amalgamations of long-decayed flesh sewn together with oozing black tendrils.",
                        "Their faces look as though they have been sewn on as well..\n"
                        "\nIn a matter of seconds, a dozen or so of the Residents are on top of you."
                        "\nYou are torn apart.",
                        "\nYour new body prepares its new home.",
                        "\nGame Over."
                    ]
                    horror_left_lines3 = [      # Lines if player runs away
                        "\nYou decide that this place is too strange to explore at night.",
                        "You begin running in the opposite direction back to where you started.",
                        "You hear a strange harmony of screams in the distance as you move further away.",
                        "\nThankfully, the screams do not get any closer, and the sounds of the crickets and cicadas\n",
                        "return to drone on as if nothing was ever wrong.",
                        "Your heart races as you quickly trace your path back towards the safety of your home.",
                        "\nYou rush through the door and immediately bolt it shut behind you.",
                        "You breathe a sigh of relief as you sit on the couch to ponder who could've been behind that window.",
                        "Around 5 minutes later, you hear what sounds like a large animal walking around outside.",
                        "The sound gets closer and closer until it reaches your front door.",
                        "\nSuddenly, 3 loud bangs come from the door.",
                        "\nYou run out of the living room and lock yourself in the bathroom.",
                        "You lay shaking in the bathtub as you try to drown out the banging.",
                        "\nYou suddenly jolt awake.",
                        "It is morning, you must have passed out due to pure terror and exhaustion.",
                        "You walk into your living room and open the front door.",
                        "The door is covered in deep scratches, as well as strange reddish-brown and black stains.",
                        "\nYou look down to see a piece of paper wedged under your welcome mat.",
                        "You pick it up and inspect the contents.",
                        "In jagged, near illegible handwriting reads the words:\n",
                        "\nProperty for sale!",
                        "\nEvergreen Residents' Estates\n",
                        "\nBelow the text is a blurry image of one of the houses that lined the path.\n"
                        "\nYou have escaped?"
                        "\nGame Over."
                    ]
                    scroll_text(horror_left_lines1)
                    horror_left_decision = input("\nWhat do you do? (take picture/run away): ")
                    if horror_left_decision == "take picture":
                        scroll_text(horror_left_lines2) 
                    elif horror_left_decision == "run away":
                        scroll_text(horror_left_lines3)
                horror_story_left()
                break
            # Right Path Story
            elif go_direction == "Right" or go_direction == "right":
                def horror_story_right():
                    pass
                horror_story_right()

    # Run the appropriate genre-specific story
    while True:
        if genre == "Horror" or genre == "horror":
            horror_story_main()
            break
        else:
            print("Invalid genre selection. Please choose a valid genre.")

# Start Game
genre = input("Choose a genre for your adventure (horror | crime | fantasy): ")
start_game(genre)
