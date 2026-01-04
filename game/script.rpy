# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

default chapters_read = False
default drawing_tablet = False
default drawing_software = False


# The game starts here.

label start:

    # normal sprite
    show e normal
    e "Hey you!"
    e "So I heard you want to learn how to draw?"
    show e thinking
    # thinking sprite
    e "That's sure an ambitious goal"
    e "Regardless..."
    show e normal
    # normal sprite
    e "enjoy the incoherent ramblings of someone who's been trying to learn to draw for the past 6 years"
    
    while not (chapter_read and drawing_tablet and drawing_software):
        menu:
            "What advice are you looking for?"

            "Just looking for some general art advice" if not chapters_read:
                $ chapters_read = True
                # holding up 1 finger
                e "Chapter 1"
                e "decide what you want to learn to draw"
                show e thinking
                # thinking sprite
                # show a pic of an animal (meow)
                e "Animals?"
                # show a pic of good food (toast)
                e "Food?"
                # uh... landscape.. yeah
                e "Landscapes?"
                # show people (like oc, trust)
                e "But probably people..."
                show e normal
                # normal sprite
                e "And if not, well, this will probably be kinda boring for you"

                # holding up 2 fingers
                e "Chapter 2"
                # picture of oc hard at work drawing
                e "Practice"
                e "Yep, the classic advice"
                e "But practice systematically"
                # line -> box -> basic shapes
                e "Learn to draw good lines, then boxes, then basic shapes"
                # show drawabox.com on the board
                e "Check out drawabox.com! If you have the will to draw 100 boxes~"
                e "Practicing efficiently is hard, but if you really want to be efficient"
                # show my own system of draw cmp repeat
                show e excited
                # excited sprite
                e "I highly recommend oriday's system of "draw, compare, repeat""
                # https://www.youtube.com/watch?v=AB9yTNfE3go&t=649s
                
                # holding up 3 fingers
                e "Chapter 3"
                # eyes
                e "Observation"
                # drawing a tree exactly as it is, vs a cartoon simplification ofi t
                # normal sprite
                show e normal
                e "Learn to draw what you are seeing"
                e "Not what you think you see!"
                e "Those are two strictly different things"
                # drawing face guidelines
                e "Learning how to draw guidelines"
                # human using box/sphere/cylinder
                e "and using boxes/spheres/cylinders to rough out the placement of limbs will be very helpful!"

                # holding up 4 fingers
                e "Chapter 4"
                # just pull up various anatomy references
                e "Anatomy"
                e "?????"
                show e thinking
                # thinking sprite
                e "Why is this here"
                e "Very important"
                e "Good foundations"
                show e normal
                # normal sprite
                e "You should learn if you can stomach it"

                # holding up 5 fingers
                e "Chapter 5"
                # show a picture of all the studies ive done...
                show e normal
                # normal sprite
                e "Drawing studies"
                e "There's a lot of these"
                # first pic
                e "Gesture drawings"
                # 2nd pic
                e "Pose studies"
                # 3rd pic
                e "Composition studies"
                # 4th pic
                # these are all on the same page
                e "Style studies"
                show e excited
                # excited sprite
                e "Pay attention to things like lines of action"
                menu:
                    "what are lines of action?":
                        show e thinking
                        # thinking sprite
                        e "lines of action guide the viewer's eyes on where to look"
                        # normal sprite
                        show e normal
                        e "they convey a sense of movement"
                        # show a stiff line of action
                        e "if your line of action is too stiff, it can make a drawing look boring or uninteresting"
                        e "leaving the viewer with an "offputting" feeling"
                        e "While this may be something you're going for"
                        e "oftentimes it isn't"
                        # show a very dynamic line of action
                        e "Good lines of action make for really dynamic and interesting pieces"
                        # show drawing through pose studies with a line of action
                        e "so it's good to practice recognizing lines of action in different pose studies you're doing"
                        # excited sprite
                        show e excited
                        e "and learning how to create your own"
                        # normal sprite
                        show e normal
                    "for sure":
                e "Study artists that you enjoy!"
                # show some old studies... i dont have a lot
                e "Figure out what you like about their style"
                e "Break down what they do"
                # thinking sprite
                show e thinking
                e "How they use lines, how they color, their composition"
                e "The amount of detail they put in to different parts"

                # 3 and 3 fingers
                e "Chapter 6"
                e "Rendering!"
                # normal sprite
                show e normal
                e "Learning rendering systems"
                e "or learning how to build your own"
                e "can greatly speed up the amount of time you spend rendering"
                # show tppo's yt
                e "I highly recommend checking out tppo on youtube"
                e "He breaks down how a lot of great artists render"
                show e thinking
                # thinking sprite
                e "I use a method similar to the chinese rendering system"
                # process of base color + multiply shadow + multiply shadow + light + refine
                e "Base color"
                e "Then a base shadow"
                e "Then a second, more detailed shadow to show occlusion"
                e "Adding in the lighting"
                e "And then refining with details"
                # normal sprite
                show e normal
                # ugly phase is real guys show a pic
                e "Remember, there's always an "ugly phase" during rendering"
                e "You just have to"
                # excited sprite
                show e excited
                e "trust the process~"

                # 2 and 5 fingers
                e "Chapter 7"
                e "Background!"
                # show pictures of backgrounds
                e "Just pray"
                e "Actually a great way to relax when I'm tired of drawing humans"
                # thinking sprite
                show e thinking
                e "It's good to note that sometimes backgrounds don't need that much detail"
                e "Random shapes + gaussian blur are the way to go"

                # normal sprite
                show e normal
                e "Some more random notes"
                # show an array of human, animal, object, landscape, lighting refernces
                e "Find references!"
                e "When you don't know how to imagine something accurately yet"
                e "It's a great idea to use references"
                # show 3d models
                # thinking sprite
                show e thinking
                e "3d models let you pose them however you like"
                e "But can be a bit finnicky or stiff"
                # normal sprite
                show e normal
                # the one website i forgor
                e "There's a lot of references online of real people posing"
                e "Or you can just take really ugly pictures of yourself"
                e "If you don't know how to draw something"
                e "Just use a reference!"
                # pinterest i guess
                e "Pinterest has great references"
                # angry sprite
                show e angry
                e "Just don't use the AI though!!!"

                # normal sprite
                show e normal
                e "but in the end"
                e "you should draw what you really want to draw"
                # thinking sprite
                show e thinking
                e "the best way to learn is a hyperfixation and too much time"
                e "because if you don't have a will to improve"
                e "you'll never draw a lot"
                # excited sprite
                show e excited
                e "so have fun!"

            "What drawing tablet should I get?" if not drawing_tablet:
                $ drawing_tablet = True
                # thinking sprite
                show e thinking
                e "so maybe you're considering buying a drawing tablet"
                e "because digital art is all that"
                e "so what should you get?"

                # holding up 1 finger
                e "First option!"
                # wacom (the super small one), huion
                e "A pen tablet"
                e "These come without screens, and serve to map your screen onto the tablet surface"
                e "There's a bit of a learning curve, because they have on screens"
                # holding up a little cash
                e "But they're cheap and easy to purchase"
                # normal sprite
                show e normal
                e "And are super portable because most of them aren't that big"
                e "The small wacoms are also great for playing osu..."
                e "If you're into that"
                # angry sprite
                show e angry
                e "THESE ARE NOT OSU TABLETS THEY ARE DRAWING TABLETS"

                # holding up 2 fingers
                e "Next"
                # wacom, huion, xpen tablets
                e "Screen/display tablets"
                e "These act as a sort of second monitor of your computer"
                # excited sprite
                show e excited
                e "So they're easier to use"
                # wacom cintique with the fucking measurements
                # normal sprite
                show e normal
                e "These can get biiggggggggg though"
                e "And they are not as portable"
                e "Also, because of their size, some of them may require an external power source"
                # holding up a bit more cash
                e "Their pricing can also get very expensive quickly"
                e "Typically around $200+ range for a decent one"

                # holding up 3 fingers
                e "Lastly"
                # show a picture of ipad/microsoft surface pro
                e "Standalone tablets"
                e "The most commonly seen one is an ipad!"
                e "These are basically just tablets that you can draw on"
                e "They act as a completely separate device"
                # genshin on ipad screen
                # excited sprite
                show e excited
                e "You can even play your favorite video games on them"
                e "They're very easy to use and portable"
                # thinking sprite
                show e thinking
                e "But depending on the pen sensitivity, youre drawing experience may vary"
                e "It also depends on how much you like drawing on screens"
                # holding up a ton of cash
                e "Because they're tablets, good quality ones are very expensive"
                # normal sprite
                show e normal

            "What kind of drawing software should I use?" if not drawing_software:
                $ drawing_software = True
                # show pen and paper on screen
                # thinking sprite
                show e thinking
                e "Pen and paper can always work"
                e "But if you want to draw digitally"
                # normal sprite
                show e normal
                e "Then you need to pick a software"
                # show krita logo on screen on the left
                e "Krita is a great free option, and comes with basically anything you could want"
                # show csp logo in the middle
                e "Clip studio paint has a one time paid option on PC that goes on sale"
                e "And comes with an insane asset library"
                # show sai + photoshop logos on the right slihgtly overlapping each other
                e "Other common options are Paint Tool SAI or Adobe Photoshop"
                # blank screen w/ word tablets on the top
                e "On tablets"
                # ibis paint logo on left
                e "You can use ibisPaint, if you can ignore the ads"
                # autodesk/medibang logos in the center 
                e "Alternatively, autodesk sketchbook and medibang all have free options"
                # procreate on the left
                e "Procreate is a great one time purchase for iPad, and is very user friendly"
                # csp somewhere sad face
                e "CSP on ipad is a recurring subscription which is very sad"

                e "I personally use Procreate now, and when I drew on my computer, I used Krita"
                e "Remember that drawing software is just a matter of preference"
                # excited sprite
                show e excited
                e "Great artists can draw with any software"
                e "(Though a disagreeable software can cause much suffering)"

                e "Now go out in the world"
                e "And create something"
                # normal sprite
                show e normal
                e "Or don't"
                e "I don't really care haha"
    
            "I'm all done":
                jump end
    
    jump end

    label end:
        e "Seems like you've read everything you wanted to"
        e "Hopefully you learned something from these ramblings"
        # excited sprite
        show e excited
        e "I wish you good luck on your art journey"
        # normal sprite
        show e normal
        e "Let's see the masterpiece you made this time..."
        $ ending = renpy.random.randint(1, 5)
        if ending == 1:
            jump ending_1
        elif ending == 2:
            jump ending_2
        elif ending == 3:
            jump ending_3
        elif ending == 4:
            jump ending_4
        else:
            jump ending_5
    
    label ending_1:
        # good ending
        e "That's a beautiful creation"
        e "I'm sure your parents will be proud"
    
    label ending_2:
        # good ending
        # excited sprite
        show e excited
        e "Aww what a cute kitty"
    
    label ending_3:
        # mid ending
        # amogus
        # thinking sprite
        show e thinking
        e "An interesting choice of drawing"
        e "But the shading is quite nice"

    label ending_4:
        # just a sad smiley face
        # angry sprite
        show e angry
        e "Did you really need my advice to produce this???"
        e "Well at least he's smiley (unlike the Kumon guy)"

    label ending_5:
        # just a bunch of lines
        e "This reminds me of the old drawing practice my art teacher made me do..."
        e "Practice well!"

    return
