label OuterValley:
    if sanderquest == 0:
        mc "{i}I better complete Sander's quest first. There's no point in leveling up if I don't have a party to join when I reach Bronze."
        jump forest

    menu:
        mc "{i}Falcons give more experience but Wild Boars also give me money... Mh..."
        "Wild Boar":
            if swordlvl >= 1:
                hide screen hud
                "You search the valley for a while and finally stumble upon a wild boar."
                show animationboar
                "It sees you and starts charging at you. You unsheathe your sword."
                mc "Ok, focus... I've trained enough to do this."
                "You strike the boar on the head just as it gets within range. It falls to the ground."
                mc "Whew, that was easy. Now I got to give this to the Guild and get some money!"
                scene black with fade
                $ exp += 5
                call levellingUp from _call_levellingUp
                show text "{color=#fff}You head to the Guild and hand over the hunted boar. You get your reward.{/color}" at truecenter with dissolve
                pause 1.3
                hide text with dissolve
                play sound chime
                if level > 9:
                    $ renpy.notify("{color=#fff}You gained 20 silver.")
                    $ money += 20
                else:
                    $ renpy.notify("{color=#fff}You gained 5 silver.")
                    $ money += 5
                $ time += 1
                jump forest
            hide screen hud
            "You search the valley for a while and finally stumble upon a wild boar."
            show animationboar
            "It sees you and starts charging at you. You unsheathe your sword."
            "You lift your sword, but it slips away from your hands and falls to the ground."
            mc "FUCK!"
            "The boar comes and hits you like a rock."
            "You fall to the ground. You quickly pick up the sword and run."
            mc "Aaarghh! That hurts! Shit, I suck so much!"
            $ time += 1
            jump forest

        "Falcon":
            if bowlvl >= 1:
                hide screen hud
                scene huntf1 with fade
                "You spot a falcon after searching the valley for a while. You draw your bow and shoot."
                play sound arrow1
                scene huntf3 with dissolve
                "The arrow hits the falcon and it falls to the ground."
                scene huntf4 with vpunch
                if chartrait == 3:
                    mc "Bullseye! Playing skittles actually paid off, I guess."
                else:
                    mc "Bullseye! All that training paid off, I guess."
                $ time += 1
                $ exp += 15
                call levellingUp from _call_levellingUp_1
                jump forest
            hide screen hud
            scene huntf1 with fade
            "You spot a falcon after searching the valley for a while. You draw your bow and shoot."
            play sound arrow1
            scene huntf2 with dissolve
            "The arrow misses by a mile. The falcon quickly flies away."
            scene huntf22 with dissolve
            mc "Shit!"
            $ time += 1
            jump forest

        "Alpha Falcon" if greenarrow == 1 and alphafalcon < 3:
            jump swtaH
