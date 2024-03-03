label OuterForest:
    if sanderquest == 0:
        mc "{i}I better complete Sander's quest first. There's no point in leveling up if I don't have a party to join when I reach Bronze."
        jump forest

    menu:
        mc "{i}Anything here can easily kill me... There should be Royal Eagles the size of a strong man good for experience or I could hunt Dire Wolves for their pelts to sell..."
        "Dire Wolf":
            hide screen hud
            "You search the valley for a while and finally stumble upon a lone dire wolf."
            show direwolf
            "It sees you and starts charging at you. You unsheathe your sword."
            mc "Ok, focus... I've trained enough to do this. Maybe..."
            if swordlvl >= 10:
                "You strike the big wolf on the head just as it gets within range. It falls to the ground."
                mc "Whew, that was scary. Now I got to give this to the Guild and get some money!"
                scene black with fade
                $ exp += 15
                call levellingUp from _call_levellingUp_11
                show text "{color=#fff}You head to the Guild and hand over the pelt. You get your reward.{/color}" at truecenter with dissolve
                pause 1.3
                hide text with dissolve
                play sound chime
                $ renpy.notify("{color=#fff}You gained 50 silver.")
                $ money += 50
                $ time += 1
                jump guild
            $ renpy.notify ("{color=#fff}Sword skill check: {color=#A50000}Fail. ([swordlvl] < 10)")
            scene huntfg3
            "Dire wolf runs around and pounces on you few times, it overwhelms you with it's attacks"
            mc "Shit, it's too fast and too strong for me alone!"
            mc "I have to run"
            if cynthtrain >= 6:
                mc "{i}Thank all gods I trained with Cynthia or I would be teared apart by now."
                jump forest
            $ renpy.notify ("{color=#fff}You don't run fast enough: {color=#A50000}Fail. ([cynthtrain] < 6)")
            "You are trying to run away but the dire wolf is fast and relentless. Soon enough its fangs and claws find their target and you can feel them sinking through your flesh."
            scene black with fade
            "Not a pretty way to go. You should've trained a bit more before trying to be a badass."
            scene black with fade
            jump GameOver

        "Royal Eagle":
            hide screen hud
            scene huntf1 with fade
            "You spot a Royal Eagle after searching the valley for a while. You draw your bow and shoot."
            play sound arrow1
            if bowlvl >= 10:
                scene huntf3 with dissolve
                "The arrow hits the Royal Eagle and it falls to the ground."
                scene huntf4 with vpunch
                if chartrait == 3:
                    mc "Bullseye! Playing skittles actually paid off, I guess."
                else:
                    mc "Bullseye! All that training paid off, I guess."
                $ time += 1
                $ exp += 40
                call levellingUp from _call_levellingUp_12
                jump forest
            $ renpy.notify ("{color=#fff}Bow skill check: {color=#A50000}Fail. ([bowlvl] < 10)")
            scene huntf2 with dissolve
            mc "Shit, it dodged it!"
            scene huntf22
            "Eagle spotted you and it started chasing you, it's talons like small swords pointed at you as it swoops down."
            mc "Fuck...!"
            if cynthtrain >= 4:
                mc "{i}Thank all gods I trained with Cynthia or I would be goner by now."
                jump forest
            $ renpy.notify ("{color=#fff}You don't run fast enough: {color=#A50000}Fail. ([cynthtrain] < 4)")
            "Its claws tear right through your back. Your continuousness fade quickly away as you feel ripping pain."
            scene black with fade
            "Not a pretty way to go. You should've trained a bit more before trying to be a badass."
            scene black with fade
            jump GameOver