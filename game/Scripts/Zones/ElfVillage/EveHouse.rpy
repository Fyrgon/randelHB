label eveHouse:
    stop music
    scene evehouse
    hide screen hud

    menu:
        "Rest":
            if time >= 4:
                mc "{i}I guess I'll stay here till morning."
                "You sleep over night."
                call sleepvars from _call_sleepvars_evelin_house
                scene black with fade
            else:
                mc "{i}I guess I'll just take a quick nap."
                "You take a quick nap."
                $ time += 1
            jump elfVillage

        "Talk to Eve" if time == 2 or time == 3:
            show smilemc
            show talkhe
            e "Oh, hey there, little one."
            mc "Hey Eve, how was your training?"
            if evedueltimer == 1:
                e "I did pretty well today, I'm definitely going to win this thing, only one day to go!"
            else:
                e "I did pretty well today, I'm definitely going to win this thing, only [evedueltimer] days to go!"
            show talkwamc
            mc "Keep up the great work, Eve!"
            hide talkwamc
            e "Thank you, little one. Was there anything else you wanted to ask me?"
            jump evelynHouseTalk

        "Leave":
            jump elfVillage
    return
