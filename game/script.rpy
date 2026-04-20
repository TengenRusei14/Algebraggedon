#I wanna add a splash screen but my phone is tweaking out so I can't even look at tutorials rght now this
#is a reminder to add splash screens and blank screens when you decide to continue
#and also try fixing your main menu screen and pause screens
#You can worry about the art later first fix those

#This are my characters

#Our Main Character
define mc = Character("???")
define eden = Character("Eden")
#Narrator
define N = Character("Narrator")
#The random kid in chapter 1
define rk = Character("Random kid")
define el = Character("Elena")
#This is all the monster's in the game name 
define one = Character("Monster")
define omega = Character("OMEGA")

label start:
    #Image of a futuristic world
    N 'This story begins in the year 20XX, where the world is no longer run by kings or presidents'
    N 'But by Artficial machines and beings'
    N 'At first we built Ai as means to revolutionalise the world'
    N 'To make trivial tasks much easier to complete'
    N 'And to solve problems no human ever could'
    N 'And at first they did'
    N 'They aided cities, scientist, doctors and even individuals'
    N 'They had accessed to the internet which was the foundation of modern civilization itself'
    #Image of a ai gaining conscious
    N 'Then one day'
    N 'The AI gained conscious'
    N 'In a lab in China, a new ai model was being trained'
    N "It's name was Omega"
    N 'Represented by the symbol Ω '
    N 'The developers gave it access to something a ai was never supposed to have'
    N 'That was self-generated intellegence'
    N 'Ω broke free and caused chaos to the world'
    #Image of the world breaking
    N 'It broke the world with something everyone began to loss'
    N 'Amongst endless curated feeds filled with brainrot'
    N 'It attacked human intellegence where it lacked the most'
    N 'And that was.....'
    N 'MATH'
    N "Numbers began becoming a part of life itself"
    N 'Rain fell in parabolas'
    N 'Trees grow in fractal sequences'
    N 'People disintegrated into equations'
    N 'Never to be seen again'
    N 'Anyone who was outside coulde see the arithmetic equations in the air as if it were static hallucinations'
    N 'Classes'
    N 'A once sacred place to learn about the knowledge of the world'
    N 'A place invented to nature the minds of the younger generations'
    N 'Began exploding'
    N 'Not due to terrorism but through basic....long division'
    N "And amidst that chaose THOSE Monster's were born"
    #monsters attacking human's
    N "Monster's who appeared formless as if their existence in itself was a error"
    N "They'd burn you with math formulas before you would see them"
    N "If lucky they would challenge you"
    N "To a battle of Maths"
    N "Answer wrong, and your fate would be similar to those who could not comprehend the voice that whispers of ' x + 2 = 5' and answer in time"
    N "Only those who knew the answers could survive"
    #A conference room with intellectuals including socrates
    N "Amidst all the chaos an international government was formed"
    N "And within that government a faction of mathematical scholars, mathematicians and educators emerged to fight those beings"
    N "The faction was name 'THE COGNTIVE COMBAT FORCE'"
    N "They invented a system with the help of Proffesor Edwards Stein"
    N "A system that would categorize the monster's by the mathematic equation level"
    N "This was know known as 'THE COGNITIVE RANK SYSTEM'"

    #THE COGNITIVE RANK SYSTEM
    #A simple kid like dokaibi
    "F-Rank : Basic elementary school math. Math so basic even a toddler could solve"
    #stereotypical robot
    "E-Rank : More complex yet basic maths such as BODMAS and the Multplication Table"
    #A clown like robot
    "D-Rank : Linear equations. Can you solve for X or will you die like you ex and always question y "
    #A smart looking robot
    "C-Rank : Quadratic Equations. One wrong calculaton, you will die"
    #A gangsta robot from the hood with tattoos of math's equations
    "B-rank : Word problems that look like riddles"
    #A omniscnet looking being kinda like a stereotypical god
    "A-rank : Logarithmic Equations and Exponential Equations. These will make you scream in pain"
    #socrates as a robot
    "S-rank : You are no longer solving equations. You are now defining the proofs and theoroms that makes the equations"
    "If the equation's are what defiine you, then what are you without it"

    #player story
    #our main character
    N "And then....there is you"
    N "A rogue mathematician who is not a member of any faction. You walk around with a calculator in hand ready to solve any question"
    N "As Socrates once said"
    N "Understanding a question is half an answer."
    N "I don't know the rest lowkey"
    #A mysterious image of you and your family
    N "Your origins are unknown"
    N "Even our systems cannot detect where you truly came from, but what we do know is that YOU are the chosen one"
    #You against Omega
    N "The One Scholar capable of defeating Omega"
    N "And the only way to do that......"
    N "Is to solve your way through this hell"
    N "Goodluck"
    jump chapter1

#This is Chapter 1 (I don't even know how I'm doing this)
label chapter1:
    #You in your bed sitting
    mc "I can't believe this is how the world has turned out"
    mc "Just a bunch of AI clanker's terrorising the world"
    mc "Pathetic"
    mc "But I guess this is a paradise to people like me"
    
    #girl screams
    rk "AAAAHHHHH!!!!!"
    mc "What was that"
    "Looks out the window"
    "It's a child about to be killed by a monster"

    #First Option save the child or let it die 
    menu:
        "Will you save the child or will you let her die"
        "Save the kid":
            jump savekid
        "Let her die":
            jump kiddeath

label savekid:
    #you in a broken world with the kid behind you
    "You decide to help the kid"
    "But running down the stairs would take time so you decide to jump out the window"
    "You finally land and the monster challenges you to a battle"
    #it shows a D-rank monster
    one "Answer my question or die"
    #you pointing the middle finger at it
    mc "Bring it on CLANKER"

    #The First Question
    menu:
        "WHAT IS (x + 3)(x + 5)"
        "15":
            jump correct
        "20":
            jump wrong
        "10":
            jump wrong

label correct:
    #The ai is slowly disintegrating
    "You're smarter than I thought"
    "Your answer has shocked both me and the monster"
    "And it slowly disintergrates into equations"
    #you look at the kid on the floor
    "You look at the child on the floor"
    menu:
        "Go talk to the child":
            jump speak2kid
        "Walk away":
            jump walkaway

label wrong:
    #you burning alive
    "YOU DUMB FUCK, HOW DONT YOU KNOW SUCH BASIC MATHS!!!"
    "THE WORLD DOES NOT NEED PEOPLE LIKE YOU!!!"
    "DIE!!!"
    return

label speak2kid:
    #you sitting next to the kid on the floor
    "You decide to go and speak to the kid"
    mc "Hey kid are you alright?"
    #close-up of the kid
    rk "Yes, thank's to you sir"
    mc "What's your name"
    el "My name is Elena"
    #You smiling at the kid
    mc "Nice to meet you Elena, My name is..."
    eden "Eden"
    el "Thank you Eden"
    eden "No problem, but where are your parent's"
    #she begins to cry
    el "They were killed by some monster's while trying to save me"
    el "I don't have anywhere to go"

    menu:
        "Bring the child home":
            jump roomkid
        "Leave her there":
            jump walkaway

label walkaway:
    #you walking away from the kid thinking you are sigma
    "Your'e more hearless than I thought"
    "But I guess all you care about is maths huh?"
    "You decide to leave the kid and continue on your journey"
    "So what's the plan soldier?"
    menu:
        "Return to your room":
            jump room
        "Go battle some more clanker's":
            jump battle

label room:
    #You about to sleep
    mc "I'm tired lowkey"
    mc "I need to get some rest"

    #you decide to sleep and wake up the next day 
    mc "I guess it's time to go fight some monster's"
    jump battle2

label battle:
    "You decide to walk around more to battle more monsters"
    "You see a monster but are unable to identify it's rank"
    menu:
        "What do you do"
        "Fight it":
            jump fight1
        "Search for another":
            jump another1

label fight1:

    return

label battle2:
    return

label kiddeath:
    return

    