define mc = Character("[povname]")

label start:

    python:   
        povname = renpy.input("What is your name?")
        povname = povname.strip()

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
            m
        "36":
            m
        "38":
            m
        
    menu:
        "Find the product of 7 and 9"
        "62":
            m
        "63":
            m
        "60":
            m

    menu:
        "Find the area of a rectangle with length 8 cm and width 5 cm"
        "30":
            m
        "40":
            m
        "35":
            m
        
    menu:
        "Add the fractions 2/3 and 1/4"
        "11/12":
            m
        "8/10":
            m
        "3/7":
            m

    menu:
        "In a right triangle, if the opposite side is 3 and hypotenuse is 5, find sin(θ)"
        "0.3":
            m
        "0.5":
            m
        "0.6":
            m

    menu:
        "What is the probability of rolling a 4 on a fair six-sided die?"
        "1/4":
            m
        "1/6":
            m
        "1/8":
            m

    menu:
        "Find the area of a triangle with base 10 cm and height 6 cm"
        "30":
            m
        "60":
            m
        "12":
            m
        
    "Time is up"
    prof "Ok time is up, drop your pens and hand in your exams"
    mc "Luckily, I have finished all the questions and I can relax now"
    prof "Ok everyone, please leave results will be announced tomorrow morning on the class group"
    mc "Now what should I do? I have nothing to do now"


    return