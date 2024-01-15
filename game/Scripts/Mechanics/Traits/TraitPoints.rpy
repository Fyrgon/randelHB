label bookworm:
    $ chartrait = 1
    $ renpy.notify("{color=fff}Character trait:{/color} {color=#0094FF}Bookworm")
    ## Trait Variables
    $ magiclvl = 1
    if skippedIntro == True:
        jump skippingBack
    jump out1

label hothead:
    $ chartrait = 2
    $ renpy.notify("{color=fff}Character trait:{/color} {color=#FF6600}Hothead")
    ## Trait Variables
    $ swordlvl = 1
    if skippedIntro == True:
        jump skippingBack
    jump out1

label playful:
    $ chartrait = 3
    $ renpy.notify("{color=fff}Character trait:{/color} {color=#3AC400}Playful")
    ## Trait Variables
    $ bowlvl = 1
    if skippedIntro == True:
        jump skippingBack
    jump out1
