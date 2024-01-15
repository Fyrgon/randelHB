default metsandergq = 0

label gquarters:
    hide screen hud
    stop music
    menu:
        "Triss":
            jump trissTalk

        "Megan":
            jump meganTalk

        "Cynthia" if cynthdate == 1:
            jump cynthiaGuildTalk

        "Evelyn" if aerinlost == 0:
            jump evelynGuildQuarters

        "Sander":
                    if metsandergq == 0:
                        scene sanderroom
                        show thinkmc
                        mc "Something tells me I better knock."
                        play sound doorknock
                        pause
                        scene gqroomblr
                        show thinkmc
                        show smirksb
                        show talkwasb
                        pause
                        sa "Oh, hey, little man!"
                        hide talkwasb
                        mc "......"
                        show talkwasb
                        sa "What?"
                        show talkwanmc
                        mc "What are you wearing?"
                        sa "What? Oh, this? I got it from Triss, she makes these things. And man, they're so comfortable! It's like you're wearing a cloud!"
                        hide talkwasb
                        mc "O-kay..."
                        show talkwasb
                        sa "So, got your room, huh?"
                        show talkmc
                        mc "Nah, it's under construction."
                        sa "Those lazy bastards!"
                        sa "Anyway, feel free to come over for a drink once you got your room."
                        show talkhappymc
                        mc "Thanks, Sander."
                        sa "Cool... see ya later, kid!"
                        mc "Bye!"
                        scene sanderroom
                        $ metsandergq += 1
                        jump gquarters
                    scene gqroomblr
                    show smirksb
                    show talkwasb
                    show smilemc
                    mc "Hi!"
                    sa "Hey, wanna drink?"
                    show talkwamc
                    mc "Actually, yeah. I would, one or two."
                    scene black with fade
                    "The two of you have a good time."
                    jump guild

        "Go back":
                    jump guild
