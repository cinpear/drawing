# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    e "Hey you!"
    e "So I heard you want to learn how to draw?"
    e "That's sure an ambitious goal"
    e "Regardless..."
    e "enjoy the incoherent ramblings of someone who's been trying to learn to draw for the past 6 years"
    
    # bg change into an incoherent whiteboard
    e "Chapter 1"
    e "decide what you want to learn to draw"
    e "Animals?"
    e "Food?"
    e "Landscapes?"
    e "But probably people..."
    e "And if not, well, this will probably be kinda boring for you"

    e "Chapter 2"
    e "Practice"
    e "Yep, the classic advice"
    e "But practice systematically"
    e "Learn to draw good lines, then boxes, then basic shapes"
    e "Check out drawabox.com! If you have the will to draw 100 boxes~"
    e "Practicing efficiently is hard, but if you really want to be efficient"
    e "I highly recommend oriday's system of "draw, compare, repeat""
    # https://www.youtube.com/watch?v=AB9yTNfE3go&t=649s
    
    e "Chapter 3"
    e "Observation"
    e "Learn to draw what you are seeing"
    e "Not what you think you see!"
    e "Those are two strictly different things"
    e "Learning how to draw guidelines"
    e "and using boxes/spheres/cylinders to rough out the placement of limbs will be very helpful!"

    e "Chapter 4"
    e "Anatomy"
    e "?????"
    e "Why is this here"
    e "Very important"
    e "Good foundations"
    e "You should learn if you can bear it"

    e "Chapter 5"
    e "Drawing studies"
    e "There's a lot of these"
    e "Gesture drawings"
    e "Pose studies"
    e "Composition studies"
    e "Style studies"
    e "Pay attention to things like lines of action"
    # what are lines of action?
        # line of action guide the viewer's eyes on where to look
        # they convey a sense of movement
        # if your line of action is too stiff, it can make a drawing look boring or uninteresting
        # leaving the viewer with an "offputting" feeling
            # which might be someting you are going for!
            # but oftentimes is not something you want
        # good lines of actions make for really dynamic and interesting pieces
        # so it's good to practice recognizing lines of actions in different pose studies you're doing
        # and learning how to create your own
    # for sure!
    e "Study artists that you enjoy!"
    e "Figure out what you like about their style"
    e "Break down what they do"
    e "How they use lines, how they color, their composition"
    e "The amount of detail they put in to different parts"

    e "Chapter 6"
    e "Rendering!"
    e "Learning rendering systems"
    e "or learning how to build your own"
    e "can greatly speed up the amount of time you spend rendering"
    e "I highly recommend checking out tppo on youtube"
    e "He breaks down how a lot of great artists render"
    e "I use a method similar to the chinese rendering system"
    e "Base color"
    e "Then a base shadow"
    e "Then a second, more detailed shadow to show occlusion"
    e "Adding in the lighting"
    e "And then refining with details"
    e "Remember, there's always an "ugly phase" during rendering"
    e "You just have to"
    e "trust the process~"

    e "Chapter 7"
    e "Background!"
    e "Just pray"
    e "Actually a great way to relax when I'm tired of drawing humans"
    e "It's good to note that sometimes backgrounds don't need that much detail"
    e "Random shapes + gaussian blur are goated"

    e "Some more random notes"
    e "Find references!"
    e "When you don't know how to imagine something accurately yet"
    e "It's a great idea to use references"
    e "3d models let you pose them however you like"
    e "But can be a bit finnicky or stiff"
    e "There's a lot of references online of real people posing"
    e "Or you can just take really ugly pictures of yourself"
    e "If you don't know how to draw something"
    e "Just use a reference!"
    e "Pinterest has great references"
    e "Just don't use the AI though!!!"

    e "but in the end"
    e "you should draw what you really want to draw"
    e "the best way to learn is a hyperfixation and too much time"
    e "because if you don't have a will to improve"
    e "you'll never draw a lot"
    e "so have fun!"
    e "make something that you're proud of"
    e "maybe show it off to the world"
    e "fight off the horrors of artblock"
    e "and the observation curve"
    e "it's ok pookie i believe in you"

    # choosing a drawing tablet?
    e "so maybe you're considering buying a drawing tablet"
    e "because digital art is all that"
    e "so what should you get?"

    e "First option!"
    e "A pen tablet"
    e "These come without screens, and serve to map your screen onto the tablet surface"
    e "There's a bit of a learning curve, because they have on screens"
    e "But they're cheap and easy to purchase"
    e "And are super portable because most of them aren't that big"
    e "The small wacoms are also great for playing osu..."
    e "If you're into that"
    e "THESE ARE NOT OSU TABLETS THEY ARE DRAWING TABLETS"
    e "Next"
    e "Screen/display tablets"
    e "These act as a sort of second monitor of your computer"
    e "So they're easier to use"
    e "These can get biiggggggggg though"
    e "And they are not as portable"
    e "Also, because of their size, some of them may require an external power source"
    e "Their pricing can also get very expensive quickly"
    e "Typically around $200+ range for a decent one"
    e "Lastly"
    e "Standalone tablets"
    e "The most commonly seen one is an ipad!"
    e "These are basically just tablets that you can draw on"
    e "They act as a completely separate device"
    e "You can even play your favorite video games on them"
    e "They're very easy to use and portable"
    e "But depending on the pen sensitivity, youre drawing experience may vary"
    e "It also depends on how much you like drawing on screens"
    e "Because they're tablets, good quality ones are very expensive"

    # drawing software reccs?
    e "Pen and paper can always work"
    e "But if you want to draw digitally"
    e "Then you need to pick a software"
    e "Krita is a great free option, and comes with basically anything you could want"
    e "Clip studio paint has a one time paid option on PC that goes on sale"
    e "And comes with an insane asset library"
    e "Other common options are Paint Tool SAI or Adobe Photoshop"
    e "On tablets"
    e "You can use ibisPaint, if you can ignore the ads"
    e "Alternatively, autodesk sketchbook and medibang all have free options"
    e "Procreate is a great one time purchase for iPad, and is very user friendly"
    e "CSP on ipad is a recurring subscription which is very sad"

    e "I personally use Procreate now, and when I drew on my computer, I used Krita"
    e "Remember that drawing software is just a matter of preference"
    e "Great artists can draw with any software"
    e "(Though a disagreeable software can cause much suffering)"

    e "Now go out in the world"
    e "And create something"
    e "Or don't"
    e "I don't really care haha"
    return
