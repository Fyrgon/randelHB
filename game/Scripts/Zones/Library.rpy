label library:
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
            jump loriTalk
        "Book of Monsters":
            if time >= 3:
                "The Library is closing soon. I don't have time to read anything."
                jump library
            jump monsterindex
        "Study Astyllian with Lori":
            hide screen hud
            if loritea == 0:
                scene black with fade
                l "Oh, [mc]. Would you, uhm, would you like some tea to drink while you read?"
                mc "Oh, that would be great! Thanks."
                l "I'll bring you a cup right away... You're ok with Kahata tea, right?"
                mc "Yeah."
                l "Ok, awesome!"
                $ loritea += 1
            show animationreadl
            "Lori brings a huge book and slumps it on the desk. She opens it and thus begins the lesson."
            mc "Thanks, Lori."
            l "Anytime... was the tea good?"
            if magiclvl == 1:
                mc "Yeah, as always."
            else:
                mc "Yeah, it's great."
            l "Thanks!"
            hide animationreadl
            $ magic += 1
            if chartrait == 1:
                $ magic = 2
            if magic == 2:
                play sound chime
                $ renpy.notify ("{color=#00C413}Your Sorcery stat has increased.")
                $ magiclvl += 1
                $ magic -= 2
            $ time += 1
            jump library
