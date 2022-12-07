# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Jacob", color = "#3531ff", callback = name_callback, cb_name = "jacob")
define t = Character("Tommy", color = "#FF0044")
define m = Character("Mathew", color = "#FF0044", callback = name_callback, cb_name = "mathew")
define narrator = Character(callback = name_callback, cb_name = None)

define pov = Character("[povname]", callback = name_callback, cb_name = "pov")


transform midright:
    xalign 0.85
    zoom 0.4
    yoffset 150

transform midleft:
    xalign 0.15
    zoom 0.4
    yoffset 150


# background images
image bg lab = im.Scale("bg lab.jpg", 1920, 1080)

# character images
image mathew = At("mathew.png", sprite_highlight('mathew'))
image mathew angry = At("mathew angry.png", sprite_highlight('mathew'))
image mathew explain = At("mathew explain.png", sprite_highlight('mathew'))
image jacob = At("jacob.png", sprite_highlight('jacob'))
image jacob scold = At("jacob scold.png", sprite_highlight('jacob'))




# The game starts here.

label start:
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg lab

    $ povname = renpy.input("What is your name?", length=32)
    $ povname = povname.strip()
    if not povname:
        $ povname = "Cyrus"
    pov "My name is [povname]."
    
    # Narrator
    "You are sneaking down the corridor with your team behind you."
    "Suddenly you hear a crash and whip your head around."

    show mathew at midright with moveinright

    # These display lines of dialogue.

    m "Hi [povname], How was your day?"

    menu:
        "My day was great thank you":
            call GoodDay
        "My day was not too good":
            call BadDay

    "This code is the end of the start block"

    # This ends the game.

    return

    
    label GoodDay:
        show mathew explain
        m "That's great to hear!"
        return
    
    label BadDay:
        show mathew angry
        m "WTF bro??"

        show jacob at midleft with moveinleft
        j "What seems to be the problem?"

    
        show mathew explain
        m "[povname] is having a bad day!"
        show mathew angry
        m "That's horrible!"
        
        show mathew 
        pov "I've just been stressed about finals."
        pov "I don't know what the big deal is."

        show jacob scold
        j "Mathew you're overreacting."
        return

