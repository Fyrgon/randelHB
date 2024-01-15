label elfGraveyard:
            stop music
            if time == 4:
                mc "I don't have a reason to go there."
                jump elfvillage

            if sawaerin == 0 and aerinlost == 0:
                hide screen hud
                scene elfgravesaerin with fade
                mc "{i}Is that Aerin?"
                mc "......"
                mc "{i}Is she's crying?"
                mc "{i}Shit, she's coming this way."
                scene elfgravesblrs
                show sada
                show normalmc
                show talkhappymc
                mc "Uhm... hey there, Aerin. My na-"
                a "......"
                show talkna
                hide talkhappymc
                a "S-Sorry human, I can't talk now, I have to hurry."
                hide talkna
                mc "Oh, okay then."
                hide talksadhappymc
                hide sada with easeoutright
                mc "{i}She was crying. I guess I caught her in a bad time."
                mc "{i}I wonder what she's like, I should ask Milly about that."
                $ sawaerin += 1
                jump elfvillage
            if sawegraveyard == 0:
                scene elfgraves with fade
                mc "Whoa, so this is the graveyard, it looks kinda empty and, well, dead. There's not even a hundred graves here... It is a pretty small village after all."
                mc "I wonder how old the village is?"
                $ sawegraveyard += 1
            scene elfgraves with fade
            menu:
                "Leave":
                    jump elfvillage
