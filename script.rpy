define e = Character("Eileen")
define correct = "You got the right answer!"
define wrong = "You got the wrong answer!"

label start:
    call variables  
    show screen ScoreOverlay

    menu choice_menu1:
        "Right choice":
            $ variables.points += 5

        "Wrong choice":
            $ variables.points -= 1
    
    e  "You have [variables.points] points."
    e "In total, you made [variables.mistakes] wrong choices so far."
    
    jump question_2
    

label question_2:

    menu choice_menu2:
        "The right choice":
            $ variables.points += 5

        "The wrong choice":
            $ variables.points -= 1
    
    e  "You have [variables.points] points."
    e "In total, you made [variables.mistakes] wrong choices so far."        


    jump question_3

label question_3:

    menu choice_menu3:
        "Right choice again":
            $ variables.points += 5

        "Wrong choice again":
            $ variables.points -= 1
    
    e  "You have [variables.points] points."
    e "In total, you made [variables.mistakes] wrong choices so far."
    
    jump question_4
    
     

label question_4:
    $ variables = Variables()
    show screen ScoreOverlay

    menu choice_menu4:
        "Okay choice":
            $ variables.points += 5
    
        "Meh choice":
            $ variables.points -= 1

    call addtional_options

    menu choice_menu5:
        "Okay choice":
            $ variables.points += 5
    
        "Meh choice":
            $ variables.points -= 1

    call addtional_options

    menu choice_menu6:
        "Okay choice":
            $ variables.points += 5
    
        "Meh choice":
            $ variables.points -= 1

    call addtional_options

    menu choice_menu7:
        "Okay choice":
            $ variables.points += 5
    
        "Meh choice":
            $ variables.points -= 1

    call addtional_options

    "You have [variables.points] points."
    "In total, you made [variables.mistakes] wrong choices so far."

    python:
        player_name = renpy.input("Enter your name for the leaderboard:")
        variables.leaderboard.update({player_name: variables.points})
        variables.save_leaderboard()
        
    call screen Leaderboard(variables)

    menu leaderboard_menu:
        "Retry from the beginning":
            hide screen Leaderboard
            jump start
        "Exit":
            return
    
    hide screen ScoreOverlay

label rightchoice:
    e "This is the right choice"

    return

label variables:
    python:
        variables = Variables()  
    return

label addtional_options:
    
    if variables.retry_option and not variables.continue_anyway:
        menu too_many_mistakes_menu:
            "You made too many mistakes."
            "Continue anyway!":
                $ variables.continue_anyway = True
            "Retry from the beginning!":
                jump start
        return


#    if variables.retry_option == True and variables.continue_anyway == False:
#        menu too_many_mistakes_menu:
#            "You made too many mistakes."
#            "Continue anyway!":

#                $ variables.continue_anyway = True
#                pass
#            "Retry from the beginning!":
#                jump start
#    return
#    menu:
#        "You made too many mistakes."
#        "Continue anyway!":
#            pass
#        "Retry from the beginning":
#            return