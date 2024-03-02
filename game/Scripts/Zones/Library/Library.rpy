default loritea = 0
default loriFunValue = 0
default loriNightSex = False
default justStraightUpAskedHer = False

label library:
    if loriEventValue == 10 and loriDropped == False:
        jump lori10
    if time >= 4:
        scene villagen
        mc "The Library is closed."
        jump maplimbo
    hide screen screenmap
    show screen hud
    stop music
    scene library
    "You arrive at the library."
    menu:
        "Lori":
            if loriEventValue == 4:
                jump loriApologizing
            if loriEventValue == 8 and loriDropped == False:
                call lori8
                jump home
            jump loriTalk
        "Study Astyllian":
            if loriEventValue == 4:
                jump loriApologizing
            hide screen hud
            call loriTea
            l "I'll go get the book, alright?"
            mc "Alright."
            show animationreadl
            "After a while, Lori comes back with a huge book and slumps it on the desk. She opens it and thus begins the lesson."
            window hide
            pause 2
            if loriEventValue == 8 and loriDropped == False:
                "Once the lesson is over, lori looks at you and blushes lightly."
                call lori8
                call magicLevel
                jump home
            if magic + ( magiclvl * 2 ) > 2 and loriEvent == True and level > 4 and loriDone == False:
                if loriFunValue < 1:
                    $ loriFunValue = 1
                if loriEventValue < 6:
                    jump expression "lori" + str(loriEventValue)
            else:
                "The two of you spend some time studying."
                call loriFunTimes
            mc "Thanks, Lori."
            if loriFunValue >= 7 and loriDone == True:
                l "Y-You're welcome... But please stop teasing me while we're studying."
                mc "I can't promise anything."
                l "Sigh."
            if loriDropped == True:
                l "Anytime..."
            else:
                l "Anytime."
            if magiclvl % 2 == 0:
                l "Was the tea good?"
                if magiclvl > 0:
                    mc "Yeah, as always."
                else:
                    mc "Yeah, it's great."
                if loriDropped:
                    l "...I'm glad."
                else:
                    l "I'm glad you like it."
            hide animationreadl
            call magicLevel
            $ time += 1
            jump library
        "Book of Monsters":
            if time >= 3:
                "The Library is closing soon. I don't have time to read anything."
                jump library
            if loriEventValue == 4:
                jump loriApologizing
            jump monsterindex


        "Convince Lori to go adventuring" if loriEventValue == 5 and level > 4:
            $ justStraightUpAskedHer = True
            jump lori5
        "Time for adventure" if loriEventValue == 7 and time < 1:
            jump lori7
    return
