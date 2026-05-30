define mc = Character("[povname]")
define prof = Character("Professor")
define kai = Character("Kai")
define luna = Character("Luna")
define r = Character("Rashim")

image bg class = "class.png"
image bg downtown = "Downtown 1 Day.png"
image bg park = "Park 1 Day.png"
image bg room = "room.png"
image bg sky_day = "Sky Day.png"
image bg sky_afternoon = "Sky Afternoon Day.png"
image bg sky_night = "Sky Night Day.png"

image kai_img = "kai.png"
image luna_img = "luna.png"

default unimarks = 0
default nasatest = 0

label splashscreen:
    scene black
    with Pause(1)

    show text "Valerian Crow Presents" with dissolve 
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

label start:

    scene bg class

    $ povname = renpy.input("What's your name?", length=32)
    $ povname = povname.strip()

    if not povname:
        $ povname = "Thaddeus Mahi"

    mc "Hi my name is [povname], And I love mathematics"
    mc "I love maths so much that I'm currently studying math's in University"
    mc "I love maths so much, I'm thinkng about it while writing my final exams"
    mc "Ohh"
    mc "My final exams"
    mc "I should finish this exam before time runs out"
    "Only 30 minutes remaining"

    menu:
        "Find the sum of 15 and 23"
        "23":
            $ unimarks += 0
        "36":
            $ unimarks += 0
        "38":
            $ unimarks += 1
        
    menu:
        "Find the product of 7 and 9"
        "62":
            $ unimarks += 0
        "63":
            $ unimarks += 1
        "60":
            $ unimarks += 0

    menu:
        "Find the area of a rectangle with length 8 cm and width 5 cm"
        "30":
            $ unimarks += 0
        "40":
            $ unimarks += 1
        "35":
            $ unimarks += 0
        
    menu:
        "Add the fractions 2/3 and 1/4"
        "11/12":
            $ unimarks += 1
        "8/10":
            $ unimarks += 0
        "3/7":
            $ unimarks += 0

    menu:
        "In a right triangle, if the opposite side is 3 and hypotenuse is 5, find sin(θ)"
        "0.3":
            $ unimarks += 0
        "0.5":
            $ unimarks += 0
        "0.6":
            $ unimarks += 1

    menu:
        "What is the probability of rolling a 4 on a fair six-sided die?"
        "1/4":
            $ unimarks += 0
        "1/6":
            $ unimarks += 1
        "1/8":
            $ unimarks += 0

    menu:
        "Find the area of a triangle with base 10 cm and height 6 cm"
        "30":
            $ unimarks += 1
        "60":
            $ unimarks += 0
        "12":
            $ unimarks += 0

    menu:
        "Find the difference between 100 and 47"
        "53":
            $ unimarks += 1
        "57":
            $ unimarks += 0
        "63":
            $ unimarks += 0

    menu:
        "Solve for x: 2x + 5 = 13"
        "4":
            $ unimarks += 1
        "6":
            $ unimarks += 0
        "9":
            $ unimarks += 0

    menu:
        "What is the perimeter of a square with side length 7 cm?"
        "28 cm":
            $ unimarks += 1
        "49 cm":
            $ unimarks += 0
        "14 cm":
            $ unimarks += 0
        
    "Time is up"
    prof "Ok time is up, drop your pens and hand in your exams"
    mc "Luckily, I have finished all the questions and I can relax now"
    prof "Ok everyone, please leave results will be announced tomorrow morning on the class group"
    mc "Now what should I do? I have nothing to do now"

    menu:
        "Go out of class":
            pass

    scene bg downtown
    show kai_img at left
    show luna_img at right

    "As I step out of the class, I see my friends waiting for me outside"
    "Honestly, I do not know what I'd be without them"

    kai "Hey [povname], how did the exam go?"
    mc "Hey Kai, I think it went well, I finished all the questions and I think I did well"
    kai "That's great to hear, I'm sure you did well"
    luna "Obviously I'm not suprised, he treats math's like his God after all"
    luna "Anyways I don't wanna speak about a exam I clearly failed so let's go somewhere"

    menu:
        kai "So, Where should we go"
        "Library":
            jump library
        "Casino":
            jump casino
        "I'm sorry I have to go home":
            jump home 

label library:
    scene bg downtown
    show kai_img at left
    show luna_img at right
    mc "I have a suggestion, why don't we head to the the public library and study"
    kai "Yeah no that sounds boring, bye"
    luna "I agree with you Kai, I don't wanna go to the library, let's go somewhere else"
    luna "Bye [povname], I hope you enjoy yourself"
    mc "No way you both are just leaving me here"

    menu:
        "Go to library":
            pass

    hide kai_img
    hide luna_img
    scene bg park

    mc "Well I guess I can go and practice with the new set of maths questions from the Weekly Math's Jump"
    "You begin walking to the library with a pen and paper in hand, trying to solve an equation"
    "You are so invested in your problem that you completly disregard your surroundings"
    "Until you hear something"
    "Something loud"
    "You look up and see......"
    "A truck"
    scene black

    show text "You Died" with dissolve
    with Pause(3)

    jump xeno

label xeno:
    "You wake up in a strange place, you have no idea where you are"
    menu:
        "WHAT DO YOU WISH TO DO?"
        "Quit":
            return
        "Wake up":
            jump chapter1


label casino:
    scene bg downtown
    show kai_img at left
    show luna_img at right
    mc "Why not the casino?"
    kai "Now we talking"
    luna "Is it not just probability to you [povname]"
    mc "It's good to just have fun sometimes"
    kai "WOOAH, I hope I'm hearing right"
    kai "[povname] know's what fun is?"
    luna "I'm also suprised"
    mc "You two are just mean, I'm also human"
    kai "Right, Right now let's get moving people"

    "They all began walking and talking about stuff university student's speak about"
    "I would'nt know I just turned 18 on the 24th of April this year, and I'm in my last year of highschool"
    "Hopefully I'll know but just not know"
    "Well enough of me and back to the story"
    "They arrived at the House Of Blacklash"
    "A royal blackjack only casino"
    "And by the entranced was Rashim"

    r "Welcome to the House Of Blacklash how may I help you"

    menu:
        "We simply looking around":
            jump m
        "We wish to play":
            jump n

label m:
    r "This casino is reserved for only the wealtheist, I will not allow you to site-see"
    r "Leave immediately"
    jump home

label n:
    r "Welcome in"
    r "Please follow me to the gaming area"
    "You follow Rashim to the gaming area and you see a lot of people playing blackjack"
    r "Please take a seat and I will deal you in"
    "You take a seat and start playing blackjack"
    "You play a round of black jack and decide to return home"

label home:

    scene bg downtown
    show kai_img at left
    show luna_img at right

    mc "Sorry guys but I have to go home and prepare for my internship tomorrow"
    kai "Ok bye"
    luna "Goodluck, bye [povname]"
    mc "Thank you both"

    hide kai_img
    hide luna_img
    scene bg room

    "You return to your small apartment"

    menu:
        "sleep":
            scene bg sky_night
            "You decide to fall asleep"
            "And wake up the next day"
            scene bg sky_day

    mc "I'm guessing I slept the whole night"
    mc "I should go to school the proffesor is announcing our marks today"

    scene bg class

    "You decide to quickly run to school and sit down right before the professor starts to speak"

    prof "Welcome in [povname], late as usual"

    "The whole class laughs"

    prof "Ok, since your'e the only one left I find it fitting to announce you mark in front of the whole class"
    prof "[povname]........"
    prof "You got"
    prof "[unimarks]/10"

    if unimarks >= 8:
        jump congrats
    else:
        jump fail

label congrats:

    scene bg class

    prof "Congratulations [povname], you did an amazing job, you got [unimarks] out of 10, that's a great mark"
    mc "Thank you professor, I'm really happy with my mark"
    prof "You should be, you worked really hard for this mark, I'm really proud of you"
    mc "Thank you professor, that means a lot to me"
    prof "Also, NASA came here looking through the results and have picked you as a candidate for an internship, you should be really proud of yourself"
    prof "You will be working with some of the best scientists in the world, and you will be doing some really cool stuff, I'm really excited for you"
    mc "Wow, that's amazing news, I'm really excited for this opportunity, thank you professor"
    prof "You're welcome, I'm really happy for you, you deserve this opportunity, I'm sure you will do great things in the future, I'm really proud of you"

    show kai_img at left
    show luna_img at center

    "Luna and Kai walk in"

    luna "Hi [povname], we heard the news, congratulations on your internship, that's amazing news!"
    kai "Now you can do math's at a higher level"
    mc "Thank's everyone, I'm really grateful for this"
    prof "What are you waitng for they are waiting for you in the other room, run"
    mc "Yes proffessor"

    "You quickly run to the other room and see 2 men wearing NASA uniform holding a ple of papers"
    "They prompt you to sit down and start asking you questions about your background and your experience with math's"
    "And have also set 50 maths problems for you to solve"

    menu:
        "start solving":
            "You open the questions and you begin to answer"
        "I don't wanna do this":
            jump fail2

    menu:
        "Find the sum of 15 and 23"
        "23":
            $ nasatest += 0
        "36":
            $ nasatest += 0
        "38":
            $ nasatest += 1

    menu:
        "Find the product of 7 and 9"
        "62":
            $ nasatest += 0
        "63":
            $ nasatest += 1
        "60":
            $ nasatest += 0

    menu:
        "Find the area of a rectangle with length 8 cm and width 5 cm"
        "30":
            $ nasatest += 0
        "40":
            $ nasatest += 1
        "35":
            $ nasatest += 0

    menu:
        "Add the fractions 2/3 and 1/4"
        "11/12":
            $ nasatest += 1
        "8/10":
            $ nasatest += 0
        "3/7":
            $ nasatest += 0

    menu:
        "In a right triangle, if the opposite side is 3 and hypotenuse is 5, find sin(θ)"
        "0.3":
            $ nasatest += 0
        "0.5":
            $ nasatest += 0
        "0.6":
            $ nasatest += 1

    menu:
        "What is the probability of rolling a 4 on a fair six-sided die?"
        "1/4":
            $ nasatest += 0
        "1/6":
            $ nasatest += 1
        "1/8":
            $ nasatest += 0

    menu:
        "Find the area of a triangle with base 10 cm and height 6 cm"
        "30":
            $ nasatest += 1
        "60":
            $ nasatest += 0
        "12":
            $ nasatest += 0

    menu:
        "Solve for x: 2x + 5 = 13"
        "4":
            $ nasatest += 1
        "6":
            $ nasatest += 0
        "9":
            $ nasatest += 0

    menu:
        "What is the perimeter of a square with side length 7 cm?"
        "28 cm":
            $ nasatest += 1
        "49 cm":
            $ nasatest += 0
        "14 cm":
            $ nasatest += 0

    menu:
        "Simplify: 3(x + 4) - 2x"
        "x + 12":
            $ nasatest += 1
        "5x + 12":
            $ nasatest += 0
        "x + 4":
            $ nasatest += 0

    menu:
        "What is the slope of the line y = 4x - 7?"
        "-7":
            $ nasatest += 0
        "4":
            $ nasatest += 1
        "0":
            $ nasatest += 0

    menu:
        "Factor completely: x² - 9"
        "(x - 3)(x - 3)":
            $ nasatest += 0
        "(x + 3)(x - 3)":
            $ nasatest += 1
        "(x + 9)(x - 1)":
            $ nasatest += 0

    menu:
        "Evaluate 5² - 3 × 2"
        "4":
            $ nasatest += 0
        "19":
            $ nasatest += 1
        "8":
            $ nasatest += 0

    menu:
        "If a = 3 and b = -2, find a² - b"
        "11":
            $ nasatest += 1
        "7":
            $ nasatest += 0
        "9":
            $ nasatest += 0

    menu:
        "What is the value of π rounded to two decimal places?"
        "3.14":
            $ nasatest += 1
        "3.16":
            $ nasatest += 0
        "3.12":
            $ nasatest += 0

    menu:
        "Find the median of: 5, 8, 12, 15, 20"
        "12":
            $ nasatest += 1
        "8":
            $ nasatest += 0
        "15":
            $ nasatest += 0

    menu:
        "A car travels 150 km in 3 hours. What is its average speed?"
        "50 km/h":
            $ nasatest += 1
        "45 km/h":
            $ nasatest += 0
        "60 km/h":
            $ nasatest += 0

    menu:
        "Solve the inequality: 2x - 5 > 7"
        "x > 6":
            $ nasatest += 1
        "x > 1":
            $ nasatest += 0
        "x < 6":
            $ nasatest += 0

    menu:
        "What is 15% of 200?"
        "30":
            $ nasatest += 1
        "20":
            $ nasatest += 0
        "25":
            $ nasatest += 0

    menu:
        "If the diameter of a circle is 10 cm, what is its radius?"
        "5 cm":
            $ nasatest += 1
        "20 cm":
            $ nasatest += 0
        "10 cm":
            $ nasatest += 0

    menu:
        "Simplify: √16 + √9"
        "7":
            $ nasatest += 1
        "5":
            $ nasatest += 0
        "25":
            $ nasatest += 0

    menu:
        "What is the y-intercept of the line y = -3x + 6?"
        "-3":
            $ nasatest += 0
        "6":
            $ nasatest += 1
        "0":
            $ nasatest += 0

    menu:
        "Solve for y: 4y - 7 = 2y + 5"
        "y = 6":
            $ nasatest += 1
        "y = 12":
            $ nasatest += 0
        "y = 3":
            $ nasatest += 0

    menu:
        "A bag has 4 red, 5 blue, and 1 green marble. What is P(blue)?"
        "1/2":
            $ nasatest += 1
        "5/10":
            $ nasatest += 0
        "1/5":
            $ nasatest += 0

    menu:
        "What is the volume of a cube with side length 3 cm?"
        "27 cm³":
            $ nasatest += 1
        "9 cm³":
            $ nasatest += 0
        "18 cm³":
            $ nasatest += 0

    menu:
        "Simplify: (2x³)(4x²)"
        "8x⁵":
            $ nasatest += 1
        "6x⁶":
            $ nasatest += 0
        "8x⁶":
            $ nasatest += 0

    menu:
        "If cosθ = 0.8, what is sin²θ?"
        "0.36":
            $ nasatest += 1
        "0.64":
            $ nasatest += 0
        "0.2":
            $ nasatest += 0

    menu:
        "What is the next term in the sequence: 3, 6, 12, 24, ..."
        "36":
            $ nasatest += 0
        "48":
            $ nasatest += 1
        "30":
            $ nasatest += 0

    menu:
        "Find the value of 2³ × 2⁴"
        "2⁷":
            $ nasatest += 1
        "2¹²":
            $ nasatest += 0
        "2⁷?":
            $ nasatest += 0

    menu:
        "A ladder 13 m long reaches a window 12 m high. How far is the foot from the wall?"
        "5 m":
            $ nasatest += 1
        "10 m":
            $ nasatest += 0
        "3 m":
            $ nasatest += 0

    menu:
        "What is the reciprocal of 2/5?"
        "5/2":
            $ nasatest += 1
        "2/5":
            $ nasatest += 0
        "1/5":
            $ nasatest += 0

    menu:
        "Simplify: (3a²b)²"
        "9a⁴b²":
            $ nasatest += 1
        "6a⁴b²":
            $ nasatest += 0
        "9a²b²":
            $ nasatest += 0

    menu:
        "If f(x) = x² + 3, find f(-2)"
        "7":
            $ nasatest += 1
        "1":
            $ nasatest += 0
        "-1":
            $ nasatest += 0

    menu:
        "What is the mode of: 2, 4, 4, 6, 7, 7, 7, 9"
        "4":
            $ nasatest += 0
        "7":
            $ nasatest += 1
        "6":
            $ nasatest += 0

    menu:
        "Solve the system: x + y = 10, x - y = 2"
        "x=6, y=4":
            $ nasatest += 1
        "x=5, y=5":
            $ nasatest += 0
        "x=8, y=2":
            $ nasatest += 0

    menu:
        "What is the sum of interior angles of a pentagon?"
        "540°":
            $ nasatest += 1
        "360°":
            $ nasatest += 0
        "720°":
            $ nasatest += 0

    menu:
        "Write 0.75 as a percent"
        "75%":
            $ nasatest += 1
        "7.5%":
            $ nasatest += 0
        "0.75%":
            $ nasatest += 0

    menu:
        "If 3x = 81, what is x?"
        "4":
            $ nasatest += 1
        "5":
            $ nasatest += 0
        "3":
            $ nasatest += 0

    menu:
        "Simplify: (x²)³ / x⁴"
        "x²":
            $ nasatest += 1
        "x⁶":
            $ nasatest += 0
        "x⁵":
            $ nasatest += 0

    menu:
        "What is the compound interest on $1000 at 10% per annum for 2 years?"
        "$210":
            $ nasatest += 1
        "$200":
            $ nasatest += 0
        "$1210":
            $ nasatest += 0

    menu:
        "Find the distance between points (1,2) and (4,6)"
        "5":
            $ nasatest += 1
        "7":
            $ nasatest += 0
        "4":
            $ nasatest += 0

    menu:
        "What is the value of tan45°?"
        "1":
            $ nasatest += 1
        "0":
            $ nasatest += 0
        "√2/2":
            $ nasatest += 0

    menu:
        "The quadratic equation x² - 5x + 6 = 0 has roots:"
        "2 and 3":
            $ nasatest += 1
        "-2 and -3":
            $ nasatest += 0
        "1 and 6":
            $ nasatest += 0

    menu:
        "Convert 3/8 to a decimal"
        "0.375":
            $ nasatest += 1
        "0.3":
            $ nasatest += 0
        "0.38":
            $ nasatest += 0

    menu:
        "If 60% of a number is 48, what is the number?"
        "80":
            $ nasatest += 1
        "28.8":
            $ nasatest += 0
        "100":
            $ nasatest += 0

    menu:
        "What is the circumference of a circle with radius 7 cm? (use π=22/7)"
        "44 cm":
            $ nasatest += 1
        "154 cm":
            $ nasatest += 0
        "22 cm":
            $ nasatest += 0

    menu:
        "Solve: |x - 3| = 5"
        "x = 8 or x = -2":
            $ nasatest += 1
        "x = 8 only":
            $ nasatest += 0
        "x = 2 or x = -8":
            $ nasatest += 0

    menu:
        "A die is rolled twice. Probability of getting a sum 7?"
        "1/6":
            $ nasatest += 1
        "1/12":
            $ nasatest += 0
        "5/36":
            $ nasatest += 0

    menu:
        "Factor: 2x² + 5x + 2"
        "(2x + 1)(x + 2)":
            $ nasatest += 1
        "(2x + 2)(x + 1)":
            $ nasatest += 0
        "(x + 2)(x + 1)":
            $ nasatest += 0

    menu:
        "What is the derivative of x² with respect to x?"
        "2x":
            $ nasatest += 1
        "x":
            $ nasatest += 0
        "2":
            $ nasatest += 0

    return

label fail:
    scene bg class

    prof "Unfortunately, you didn't pass. Better luck next time."
    return

label fail2:
    "You decided not to take the NASA test, and as a result, you missed out on a great opportunity. You feel regretful about your decision."
    "You realize that sometimes, taking risks and stepping out of your comfort zone can lead to amazing opportunities. You vow to be more open to new experiences in the future."
    "But this is unfortunately where your journey ends"
    "You realse what you just did and stormed out the university onto the main road"
    "You did not realise the truck approaching you and you got hit by it"


label chapter1:

    scene bg room

    "You wake up from the strange dream..."

    show text "Coming Soon" with dissolve 
    with Pause(2)

