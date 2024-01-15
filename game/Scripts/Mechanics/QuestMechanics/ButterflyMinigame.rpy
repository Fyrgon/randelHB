default BFMGtries = 0
default repeatBFMG = 1

label randomNumberGeneratorBF:
    $ roll10 = renpy.random.randint(1, 10)
    $ randomX = roll10/10
    $ roll10 = renpy.random.randint(1, 10)
    $ randomY = roll10/10
    if BFMGtries < 20:
        $ randomT = renpy.random.randint(2, 4) / 2
    elif BFMGtries < 50:
        $ randomT = renpy.random.randint(2, 3) / 2
    elif BFMGtries < 100:
        $ randomT = renpy.random.randint(1, 3) / 2
    else:
        $ randomT = renpy.random.randint(1, 2) / 2
    $ BFMGtries += 1
    return

label butterflyMinigameStart:
    $ BFMGtries = 0
    $ repeatBFMG = 1
    $ bfly = 0
    scene forestfloor
    mc "Alright, time to catch some butterflies."
    show text "{color=#fff}Click on the butterflies to catch them!"
    pause 2.5
    hide text with dissolve
    label butterflyMinigameStart2:
    scene forestfloor
    call randomNumberGeneratorBF
    show screen butterflyCounter
    show screen butterflyMiniGame
    pause

label butterflySuccess:
    hide screen butterflyMiniGame
    $ bfly += 1
    if repeatBFMG < 5:
        if BFMGtries >= repeatBFMG*10:
            jump BFMGCheck
    else:
        if BFMGtries >= (repeatBFMG - 5) * 25 + 50:
            jump BFMGCheck
    jump butterflyMinigameStart2

label butterflyMiss:
    hide screen butterflyMiniGame
    if repeatBFMG < 5:
        if BFMGtries >= repeatBFMG*10:
            jump BFMGCheck
    else:
        if BFMGtries >= (repeatBFMG - 5) * 25 + 50:
            jump BFMGCheck
    jump butterflyMinigameStart2

label BFMGCheck:
    hide screen butterflyCounter
    hide screen butterflyMiniGame
    $ repeatBFMG += 1
    if bfly == 1:
        mc "{i}Let's see... I've got... [bfly] butterfly."
    else:
        mc "{i}Let's see... I've I got... [bfly] butterflies."
    if bfly < 2:
        mc "{i}...Yeah no, this isn't enough. I should probably catch more if I want to beat her."
        jump butterflyMinigameStart2
    else:
        mc "{i}Will this be enough?"
        menu:
            "It's enough":
                jump butterflyEnough
            "Catch more":
                if bfly < 10:
                    mc "{i}I probably need more to beat her..."
                else:
                    mc "{i}Let's catch some more just to be sure."
                jump butterflyMinigameStart2



screen butterflyCounter():
    if repeatBFMG < 7:
        text "{color=#FFF}Butterflies Caught: [bfly]" at transform:
            anchor (-0.3, -0.5)
    else:
        text "{color=#FFF}{size=+1}Butterflies Caught: [bfly]" at transform:
            anchor (-0.3, -0.5)

screen butterflyMiniGame():
    modal True
    imagebutton:
        xalign randomX
        yalign randomY
        idle "images/butterfly.webp"
        hover "images/butterflyH.webp"
        action Play("music", "audio/chime.mp3"), Jump("butterflySuccess")
    timer randomT action Jump("butterflyMiss")
