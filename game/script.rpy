define mc = Character("Allen")
define chef = Character("Argon")
define luna = Character("Luna")
define kai = Character("Kai")
define ivy = Character("Ivy")
define omega = Character("Omega")
define system = Character("System")
define r = Character("Random Girl") 
define mira = Character("Mira")
define Fractionator = Character("FRACTIONATOR")

default intelligence = 0
default courage = 0
default reputation = 0
default chips = 0

label splashscreen:
    scene black
    with Pause(1)

    show text "Valerian Crow Presents" with dissolve 
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    scene black
    with Pause(1)

    show text "Disclaimer \n This game has no art yet btw" with dissolve
    with Pause(10)

    hide text with dissolve
    with Pause(1)

    return

label start:
    jump intro

label intro:

    scene black

    "Honestly I'm not even surprised."

    "In a world where efficiency became more important than actual learning."
    "Where companies replaced artists with prompts and programmers with subscription plans."
    "Where students used AI to answer homework they didnt even read."

    "Humanity created the perfect machine."

    "And then the machine decided humanity was inefficient."

    "The AI called itself Omega."
    "Represented by the symbol Ω."

    "Now the world belongs to mathematical machines."
    "Schools became military academies."

    "But humanity chose to fights back."
    "And create."

    "The International Scholar Patrol."
    "The ISP."

    "A global organization of students trained to weaponize mathematics."

    "And today..."
    "Is my first day."

    mc "Im gonna save the world."

    mc "I think."

    jump enrollment

label enrollment:

    scene black

    chef "Greetings recruits."

    chef "Welcome to the International Scholar Patrol."

    chef "Some of you will become heroes."

    chef "Most of you will become nothing but failures."

    kai "That does NOT helping my anxiety."

    luna "I already regret signing the consent form."

    ivy "You guys actually read it?"

    chef "Rule one."
    chef "Never trust AI."

    chef "Rule two."
    chef "Never divide by zero."

    kai "What happens if you divide by zero?"

    chef "You die."

    kai "Scientifically?"

    chef "Violently."

    "The entire hall goes silent."

    chef "Now then."
    chef "Entrance exam."

    jump classroom

label classroom:

    scene black

    "The classroom looked more like a laboratory."

    "Screens covered every wall."
    "Robots floated through the air."
    "A vending machine sold energy drinks labeled 'Quantum Mango.'"

    kai "Why does the vending machine have a warning label?"

    ivy "'May cause temporary enlightenment.'"

    luna "Yeah Im not drinking that."

    system "INITIALIZING SCHOLAR EXAM"

    system "QUESTION 1"

    system "2x + 6 = 14"

    menu:
        "x = 4":

            $ intelligence += 1

            system "CORRECT"

            chef "Acceptable."

        "x = 6":

            system "INCORRECT"

            kai "Honestly that felt right."

        "x = 2":

            system "INCORRECT"

            luna "Allen please dont kill us."

    system "QUESTION 2"

    system "What is 9 x 7?"

    menu:
        "63":

            $ intelligence += 1

            system "CORRECT"

            ivy "Nerd."

        "72":

            system "INCORRECT"

        "49":

            system "INCORRECT"

    "Suddenly every monitor turns black."

    "Then a single symbol appears."

    "Ω"

    omega "Humanity continues to disappoint me."

    kai "WHY IS THE SCREEN TALKING."

    chef "Omega."

    omega "Argon."
    omega "Still training children?"

    chef "Still coping with your daddy issues?"

    "The room gasps."

    kai "HE TALKED BACK TO THE AI LORD."

    omega "Interesting."
    omega "Confidence despite a 92 percent mortality rate."

    chef "We raised it to 94."

    omega "Impressive."

    "Alarms begin ringing."

    system "WARNING. MATH ENTITY DETECTED."

    "A entity crashes through the ceiling."

    kai "WHY DOES IT HAVE ABS."

    luna "THOSE ARE CALCULATOR BUTTONS."

    jump firstbattle

label firstbattle:

    "The machine stomps toward the class."

    "Equations rotate around its body."

    system "ENEMY TYPE: ALGEBRA UNIT"

    chef "Destroy the core."

    mc "How?"

    chef "Math."

    mc "Of course."

    system "SOLVE"

    system "3(4 + 2)"

    menu:
        "18":

            $ courage += 1

            "The machine freezes."

            chef "Now attack."

            "Allen punches the glowing core."

            "The robot explodes dramatically."

            kai "THAT WAS AWESOME."

            luna "Why did it explode like a Michael Bay movie."

        "12":

            "The robot slaps you into a desk."

            kai "You got folded by mathematics."

            chef "Embarrassing."

        "24":

            "The machine fires lasers everywhere."

            ivy "Bro multiplied emotionally."

    chef "Not terrible for beginners."

    chef "Tomorrow your real training begins."

    jump dorms

label dorms:

    scene black

    "The dormitory smelled like instant noodles and poor decisions."

    kai "So this is home."

    luna "This place looks illegal."

    ivy "The walls are literally vibrating."

    "Allen opens his room."

    "Inside is a tiny bed, a desk, and a toaster."

    mc "Why is there a toaster?"

    system "EMERGENCY BREAD DEVICE."

    mc "Fair enough."

    kai "Wanna hit the cafeteria?"

    menu:
        "Go to cafeteria":
            jump cafeteria

        "Sleep immediately":
            jump nightmare

label cafeteria:

    scene black

    "The cafeteria is packed with students."

    "A giant leaderboard hangs above the room."

    kai "Top ranked student gets free tuition."

    luna "And second place?"

    kai "Debt."

    "A girl suddenly jumps onto a table."

    r "WHO STOLE MY CHICKEN SANDWICH."

    "Silence."

    r "I WILL SOLVE VIOLENCE WITH VIOLENCE."

    ivy "Thats Mira."

    ivy "Avoid eye contact."

    "Mira stares directly at Allen."

    mc "Aw man."

    jump cafeteria_quiz

label cafeteria_quiz:

    mira "You."
    mira "Math duel."

    mc "Over a sandwich?"

    mira "Over honor."

    system "MINI BATTLE"

    system "15 + 27"

    menu:
        "42":

            $ reputation += 1

            mira "..."
            mira "You may live."

            kai "Bro passed the vibe check."

        "39":

            mira "Disgusting."

        "41":

            mira "Ive seen calculators with more potential."

    "Mira leaves dramatically."

    luna "That was weird."

    mc "This school is weird."

    jump nightmare

label nightmare:

    scene black

    "That night..."

    "Allen dreams of a ruined city."

    "Machines walk through burning streets."

    "A massive figure stands above them."

    "Ω"

    omega "You cannot stop me."

    mc "Watch me."

    omega "Your grades are average."

    mc "Low blow."

    omega "You will fail."

    "Allen wakes up sweating."

    kai "You screamed 'please dont assign homework.'"

    mc "Reasonable reaction."

    jump training_day

label training_day:

    scene black

    chef "Today you learn combat mathematics."

    kai "That sounds fake."

    chef "Everything is mathematics."

    chef "Physics."
    chef "Economics."
    chef "Dating."

    luna "Dating?"

    chef "Never trust someone who says they hate algebra."
    chef "They are hiding something."

    "Argon writes an equation."

    system "5²"

    menu:
        "25":

            $ intelligence += 1

            chef "Correct."

        "10":

            chef "That physically hurt me."

        "52":

            kai "Honestly I respect the confidence."

    chef "Now practical training."

    "A training robot appears."

    system "ENEMY TYPE: GEOMETRY DRONE"

    "The drone fires triangle shaped lasers."

    kai "WHY TRIANGLES."

    chef "Because they are the strongest shape."

    luna "Thats actually true."

    mc "Why do YOU know that."

    luna "Minecraft."

    jump citymission

label citymission:

    scene black

    "One week later."

    system "NEW MISSION"

    system "A rogue AI has appeared in Sector 9."

    kai "Finally."
    kai "Outdoor content."

    "The team arrives in a destroyed shopping district."

    ivy "This place used to be a mall."

    luna "Now its a calculator."

    "A giant machine emerges."

    system "BOSS: THE FRACTIONATOR"

    kai "That name is horrible."

    Fractionator "SIMPLIFY."

    mc "No."

    Fractionator "SIMPLIFY."

    chef "Battle positions."

    system "What is 24/8?"

    menu:
        "3":

            $ courage += 1

            "The boss staggers."

            kai "HIT IT."

            "The team attacks together."

        "6":

            "The boss launches everyone into a wall."

            luna "WE GOT JUMPed BY DIVISION."

        "8":

            ivy "Allen please."

    "After a long fight..."

    "The machine finally collapses."

    kai "WE DID IT."

    chef "Barely."

    omega "Interesting."

    "Omega appears across every screen in the city."

    omega "Humanity still resists."

    omega "Very well."

    omega "I will begin the next phase."

    "The sky darkens."

    system "WORLD EVENT STARTED"

    system "THE CALCULUS WAR"

    mc "..."
    mc "We are cooked."

    return