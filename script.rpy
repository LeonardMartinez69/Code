# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# The game starts here.

label start:
    call variables  

    menu choice_menu:
        "Right choice":
            $ variables.points += 5
#            variables.correct_choice(True) ---> if wrapper
            pass
#            jump rightchoice (not finished)
            

        "Wrong choice":
            $ variables.points -= 1
#            jump choice_menu (no choice menu yet)
#            variables.correct_choice(False)  ---> if wrapper
            pass

    e "You're correct. You have [variables.points] points."
    e "In total, you made [variables.mistakes] wrong choices so far."

    return

label rightchoice:
    e "This is the right choice"

    return

label variables:
    python:
        variables = Variables()  
    return
