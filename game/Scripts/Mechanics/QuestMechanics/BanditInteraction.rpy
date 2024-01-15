default stabb = 0
default round1banditfight = 0

label deflect1:
    play sound swordh2

    hide screen banditfight1
    call screen banditfight2

label deflect2:
    play sound swordh2

    hide screen banditfight2
    call screen banditfight3

label deflect3:
    play sound swordh1

    hide screen banditfight3
    call screen banditfight4

label deflect4:
    play sound swordh2

    hide screen banditfight4
    call screen banditfight5

label deflect5:
    play sound swordh3

    hide screen banditfight5
    call screen banditfight6

label deflect6:
    play sound swordh1

    hide screen banditfight6
    jump finishfight

##miss



label miss1:

    if stabb >= 3:
        jump losebandit
    $ stabb+= 1
    play sound stab
    hide screen banditfight1
    call screen banditfight2

label miss2:

    if stabb >= 3:
        jump losebandit
    $ stabb+= 1
    play sound stab
    hide screen banditfight2
    call screen banditfight3

label miss3:

    if stabb >= 3:
        jump losebandit
    $ stabb+= 1
    play sound stab
    hide screen banditfight3
    call screen banditfight4

label miss4:

    if stabb >= 3:
        jump losebandit
    $ stabb+= 1
    play sound stab
    hide screen banditfight4
    call screen banditfight5

label miss5:

    if stabb >= 3:
        jump losebandit
    $ stabb+= 1
    play sound stab
    hide screen banditfight5
    call screen banditfight6

label miss6:

    if stabb >= 3:
        jump losebandit
    $ stabb+= 1
    play sound stab
    hide screen banditfight6
    jump finishfight
