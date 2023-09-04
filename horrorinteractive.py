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

#   Message for invalid inputs
invalid_choice = "\nInvalid choice, please try again."

# Welcome message
scroll_text("Welcome to Horror Interactive!\n")
input("Press Enter to continue: ")

# Option to replay game
def play_again_prompt():
    replay_option = input("\nWould you like to play again? (y/n): ")
    if replay_option.lower() == "y":
        start_game()
    else:
        scroll_text("\nThanks for playing.")
        while True:
            input("\nPress Enter to exit.")
            break

# Run Game
def start_game():
    # Horror story main function
    def horror_story_main():
        while True:
            player = input("Choose a name for your character: ")
            if player == '':
                scroll_text("\nPlayer name cannot be blank.")
            else:
                break
            
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
            if look_direction1.lower() == "left":
                scroll_text(horror_lines_main2)
                break
            elif look_direction1.lower() == "right":  
                scroll_text(horror_lines_main3)
                break
            else:
                scroll_text(invalid_choice)

        while True:
            look_direction2 = input("\nLook in the opposite direction? (y/n): ")
            if look_direction2.lower() == 'n':
                break
            elif look_direction2.lower() == 'y':
                if look_direction1.lower() == "left":
                    scroll_text(horror_lines_main3)
                    break
                elif look_direction1.lower() == "right":
                    scroll_text(horror_lines_main2)
                    break
            else:
                scroll_text(invalid_choice)
        # Choose correct story for player direction
        while True:
            go_direction = input("\nWhich direction do you go? (left/right): ")

            # Left Path Story
            if go_direction.lower() == "left":
                def horror_story_left():
                    horror_left_lines1 = [     # Lines if player takes left path
                        "\nYou begin walking down the road to the left.",
                        "As you walk past the houses that line the path,\n",
                        "you realize that every single house is completely identical to the last.",
                        '\n"None of this makes any sense, why would they build these houses here?"\n',
                        "You think to yourself as you stop in front of one of the houses to get a closer look\n",
                        "\nAs you scan your eyes across the strange structure, you notice the blinds rustle slightly.",
                        "The sidewalk is too far from the window to make out too many details.",
                        "You quickly power on your camera and look into the viewfinder.",
                        "You zoom into the window where you can see the blinds being bent back.",
                        "\nThe only thing you can make out is a bony finger poking through the gap."
                    ]
                    scroll_text(horror_left_lines1)
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
                        "It is morning; you must have passed out due to pure terror and exhaustion.",
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
                    while True:
                        horror_left_decision = input("\nWhat do you do? (take picture/run away): ")
                        if horror_left_decision.lower() == "take picture":
                            scroll_text(horror_left_lines2)
                            play_again_prompt()
                            break 
                        elif horror_left_decision.lower() == "run away":
                            scroll_text(horror_left_lines3)
                            play_again_prompt()
                            break
                        else:
                            scroll_text(invalid_choice)
                horror_story_left()
                break

            # Right Path Story
            elif go_direction.lower() == "right":
                def horror_story_right():
                    horror_right_lines1 = [         # Lines if player goes down right path
                        "\nYou begin walking down the road to the right.",
                        "\nAs you walk further down the path, the forest on both sides of the road\n",
                        "continues to get thicker and thicker, leaving only small slivers of moonlight\n",
                        "to guide you forward.",
                        "\nEventually, you see that the path leads to more forest, with a smaller trail leading further\n",
                        "into the trees.",
                        "\nYou make it to the end of the road and begin walking down the trail further into the dark forest.",
                        "You are feeling very uneasy from the overwhelming feeling of uncertainty as to what lies ahead.",
                        "\nEventually, you begin to see a faint white fluorescent light flickering up ahead.",
                        "As you get closer, you realize that the light is coming from a small shed in the middle of a clearing.",
                        "\nYou approach the shed and notice that the door is wide open.",
                        "There isn't much space inside; the only thing inside is a concrete floor with a trapdoor in the center."
                    ]
                    scroll_text(horror_right_lines1)

                    horror_right_lines2 = [         # Lines if player exits shed
                        "\nYou decide that this place is too strange, and you turn around and begin walking back.",
                        "\nYou only make it about 100 feet before you heard the galloping of a large animal in the trees.",
                        "The sound gets closer and closer until a large creature bursts from the trees.",
                        "It stands at about 8 feet tall.",
                        "It looks like a mass of dead animal parts that has been sewn together to resemble a moose.",
                        "The pieces of its body are tied together with oozing black tendrils.",
                        "\nIt stares at you with empty sockets.",
                        "\nYou start to back away, but it charges at you faster than any animal you've ever seen.",
                        "It charges headfirst into your chest and skewers you with its antlers.",
                        "\nThen the others come out to begin your transformation.",
                        "\nGame Over."
                    ]
                    horror_right_lines3 = [        # Lines if player enters trapdoor
                        "\nYou open the trap door which reveals a ladder leading down to some sort of basement.",
                        "\nYou start climbing down the ladder, but as soon as you reach the ground, the trapdoor\n",
                        "slams shut above you and a clicking sound can be heard.",
                        "\nYou look around and see a wall of monitors showing security footage from different areas in the forest."
                        "\nSuddenly, the sound of multiple stomping boots comes from around the corner.",
                        "4 soldiers turn the corner, all of them wearning full kevlar armor and pointing\n",
                        "an assault rifle in your direction.",
                        '\n"Who are you? How did you get in here?"\n',
                        "Yells one of the guards\n",
                        '\n"It doesn\'t matter, we have to take care of him.',
                        "Says another guard\n"
                    ]
                    horror_right_lines4 = [        # Lines if player resists soldiers
                        "\nYou reach out and grab the barrel of one of the solder's gun.",
                        "\nThe other soldiers react immediately and fire into you,",
                        "killing you almost instantly.",
                        "\nThey throw your body outside and sit and watch it from the security cameras.",
                        "\nOnly a few moments later, a pack of mangled looking wolves with black ooze\n",
                        "dripping from open wounds on their bodies pounce on your body and tear it apart.",
                        "\nThey carry your body parts away to their leader."
                        "\nGame Over."
                    ]
                    horror_right_lines5 = [        # Lines if player doesn't resist soldiers
                        "\nYou close your eyes and accept your fate.",
                        "\nYou consider crying out to reason with them, but before you get the chance,\n",
                        "a solider approaches you and injects a syringe into your neck.",
                        "\nYou awake the next morning in your bed.",
                        "No matter how hard you try, you can't seem to remember what happened after you went down\n",
                        "that trapdoor.",
                        "\nYou have escaped.",
                        "\nGame Over."
                    ]
                    while True:
                        horror_right_decision1 = input("\nWhat do you do? (go back/enter trapdoor: )")
                        if horror_right_decision1.lower() == "go back":
                            scroll_text(horror_right_lines2)
                            play_again_prompt()
                            break
                        elif horror_right_decision1.lower() == "enter trapdoor":
                            scroll_text(horror_right_lines3)
                            horror_right_decision2 = input("\nWhat do you do? (resist/accept): ")
                            if horror_right_decision2.lower() == "resist":
                                scroll_text(horror_right_lines4)
                                play_again_prompt()
                                break
                            elif horror_right_decision2.lower() == "accept":
                                scroll_text(horror_right_lines5)
                                play_again_prompt()
                                break
                            else:
                                scroll_text(invalid_choice)
                        else:
                            scroll_text(invalid_choice)

                horror_story_right()
                break
            else:   # If player enters invalid path direction
                scroll_text(invalid_choice)

    horror_story_main()
# Start Game
start_game()
