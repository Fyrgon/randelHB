define firstTimeThisSpecificEventShows_YupOnlyThisOneAndNotAnotherOne = True

label homeEvents:
    if cynthtimer >= 3 and cynthquest6 == 0:
        stop sound fadeout 3
        jump cynthquest6

    if testtimer >= 3 and testDone == False:
        stop sound fadeout 3
        jump test

    if gabethea == 0 and gabeintro == 1 and theajob == 1 and time == 0:
        stop sound fadeout 3
        jump theaxgabe

    if evetimer >= 1 and sawelfvillage == False:
        stop sound fadeout 3
        jump elfqueststart

    if punchtriss == 1:
        show worriedmc
        show blackeye
        mc "{i}Ah, my eye it still hurts. Damn you, Triss!"
        hide blackeye
        hide worriedmc

    if day == 4 and time == 0 and sawcynth < 2:
        show animation2
        mc "{i}Yawn..."
        mc "Urgh. Another day of classes at the Academy."
        mc "I wish there was a day where you could just stay at home."
        show text "{color=#fff}You should go to the Academy today." at truecenter
        pause 1.5
        hide text with dissolve
        hide animation2

    if day == 3 and boris == 0 and time == 0 and firstTimeThisSpecificEventShows_YupOnlyThisOneAndNotAnotherOne == True:
        show animation2
        mc "{i}Yawn..."
        mc "Time to get ready."
        mc "I should probably go to Boris' class once in a while. I might learn something new there."
        $ firstTimeThisSpecificEventShows_YupOnlyThisOneAndNotAnotherOne = False
        hide animation2

    if day == 2 and petefish == 1:
        mc "Eww... What's that smell?"
        mc "......"
        mc "{i}Oh shit, it's Uncle Pete's fish!"
        mc "{i}I forgot to eat it, damn it. I guess I'll have to throw it out..."
        mc "Sorry, Uncle Pete."
        $ petefish = 0
        $ throwfishout = True

    if theajobtimer > 2 and theajob == 1:
        stop sound fadeout 3
        jump theaworks

    if petesawthea == 1 and time == 0:
        mc "{i}We're having dinner with Uncle Pete today."
        mc "{i}I should send a letter to him."
        "You take a piece of paper and start writing."
        "You send the letter using your messenger pigeon."
        mc "{i}Send this to Uncle Pete."
        "The bird flies away."
        $ petesawthea += 1
        jump postMusic

    if  theadogfood == 1 and petesawthea == 0 and time == 0:
        stop sound fadeout 3
        jump petemeeting

    if sanderevedinner == 1 and time == 4:
        stop sound fadeout 3
        jump sanderevedinner

    if sanderpetedinner == 1 and time == 4:
        stop sound fadeout 3
        jump sanderpetedinner

    if theadinner == 2 and time == 4:
        stop sound fadeout 3
        jump theadinner

    if petesawthea == 2 and time == 4 and petedinner == 0:
        stop sound fadeout 3
        jump petedinner
    return






label sleeping:
    "Gotta sleep..."
    hide screen hud
    stop music fadeout 1
    stop sound fadeout 1
    show sleep with fade
    pause 1
    scene black
    show text "{color=#fff}End of day [day]." at truecenter
    with dissolve
    pause 1.5
    hide text with dissolve

    if day == 2:
        stop music
        scene black with fade
        pause
        mc "{i}Where am I?"
        scene dream21 with fade
        pause
        mc "{i}Is that Uncle Pete?"
        mc "Uncle Pete!"
        mc "Uncle Pete!!!"
        mc "{i}I guess he can't hear me..."
        scene dream21a with dissolve
        mc "Hey, Uncle Pete!"
        scene dream21b with dissolve
        pause
        scene dream22
        mc "Uncle Pete, what are you doing he-"
        play sound slash1
        scene dream23
        pause
        mc "Un...cle..."
        scene dream24
        pause
        scene dream25
        pause
        scene dream23
        mc "Why Uncle...?"
        stop sound
        scene dream2e with vpunch
        mc "{b}WHYYYYYYYYYYYYYYYYY?!?!?"
        scene wakeup1 with flash
        pause 0.3
        scene wakeup2
        pause 3
        scene wakeup1
        mc "{i}Another dream! Urgh, these things get weirder and weirder..."

    if day == 10:
        play music windhowl
        scene black
        mc "{i}sob sob..."
        scene dmndrm with fade
        mc "{i}sob... sob..."
        u "[mc]? Why are you crying?"
        scene dmndrm2 with fade
        pause
        mc "{i}sob{/i}... He... He took everything."
        u "Huh? Who...? Was it some bully?"
        mc "Yeah... {i}sob{/i} ...I hate him!"
        u "Aww, don't cry, [mc]. Come, show me that bully. We'll go talk some sense into him."
        scene dmndrm3 with dissolve
        pause
        mc "He's over there..."
        stop music
        scene dmndrm4
        pause 0.8
        scene wakeup1 with flash
        pause 0.5
        scene wakeup2
        pause 3
        scene wakeup1
        mc "{i}Urgh, what was that... thing? Why won't these things just stop!?"

    ##if testdone == 1 and day == 13:
    ##    $ traitquest += 1
    ##    call traitquest
    call sleepvars

    if theagotjob == 1 and theasex == 0:
        $ payday += 1
        if payday == 7:
            scene mcroom
            show smilemc
            show talknth
            th "Here's the rent, [mc]."
            hide talknth
            show normalth
            show talkhappymc
            mc "Thanks."
            play sound chime
            $ renpy.notify("{color=#fff}You gained 20 gold.")
            $ money += 20
            $ payday -= 7
    jump home
