define readFQ = False

label QuestBoard:
    $ checkboard += 1
    mc "Let's see..."
    scene questboard with fade
    menu:
        ##### GABEQUEST 2
        "Investigate goblin camp" if testDone == True and level >= 10 and gabequest2 == 0:
            if swordlvl < 2 and bowlvl < 2:
                mc "I don't think I'm ready for this yet. I should go train a bit more."
                jump guild
            show black with dissolve:
                alpha 0.5
            show text "{color=#fff}{b}{u}Investigate Goblin Camp{/u}{/b}\n{i}There have been reports of a small tribe of goblins occupying the abandoned castle in the forest. You have to scout the location and report back to the Guild.{/i}\n{b}Rank{/b} — Bronze\n{b}Reward{/b} — 100 gold" with dissolve
            pause 10
            hide text
            hide black
            with dissolve
            menu:
                "Start quest":
                    mc "Let's start then."
                    jump gabequest2
                "Later":
                    mc "I'll still need time."
                    jump guild
        ##### MINE QUEST
        "Wallcrawler infestation" if mineQuest == False:
            show black with dissolve:
                alpha 0.5
            show text "{color=#fff}{b}{u}Wallcrawler infestation{/u}{/b}\n{i}Rongan's Mine is infested with Wallcrawlers. The dwarves require help in exterminating these creatures. Please provide your assistance.{/i}\n{b}Rank{/b} — Recruit\n{b}Reward{/b} — 40 gold" with dissolve
            pause 10
            hide text
            hide black
            with dissolve
            mc "This looks like something I can handle... I think."
            if readwallcrawler == False:
                mc "But what are Wallcrawlers? I should {b}look into them at the Library.{/b}"
                jump guild
            menu:
                "Start quest":
                    if icamping == 1:
                        if readwallcrawler == False:
                            mc "Wait. I still need to read about the Wallcrawlers. I better go to the Library and check it out. I need to know what I'll be running into."
                            jump guild
                        if easyMode == False and swordlvl < 2 and bowlvl < 2:
                            mc "I don't think I'm ready for this yet. I should go train a bit more."
                            jump guild
                        play sound chime
                        $ renpy.notify("{color=#fff}Quest started: Mine Quest")
                        mc "Everything's ready. Time to start my first quest!"
                        "You head out into the forest."
                        jump minequest
                    mc "Wait this mine is pretty far. I may need to spend the night somewhere."
                    mc "I should get some camping equipment."
                    jump guild
                "Not yet.":
                    mc "I still have some things to do."
                    jump guild
        ##### FIRST THEA QUEST
        "Delivery Quest" if aquest2 < 2:
            if aquest2 == 0:
                show black with dissolve:
                    alpha 0.5
                show text "{color=#fff}{b}{u}Crystal Delivery{/u}{/b}\n{i}The town of Yorkel has been having trouble with Imps. They require a shipment of Black Tourmaline Crystals. Please provide your assistance.{/i}\n{b}Rank{/b} — Recruit\n{b}Reward{/b} — 80 gold" with dissolve
                pause 10
                hide text
                hide black
                with dissolve
                mc "A delivery quest? Man, these are boring..."
                mc "I have no choice though... it's the only quest on the board I am allowed to handle."
                mc "Imps? I better look them up in the {b}Book of Monsters{/b}."
                $ aquest2 += 1
                jump guild
            menu:
                "Start Quest":
                    if readimp == 0:
                        mc "Wait. I still need to read about Imps. I better go to the Library and check it out. It's a good idea to know what I'll be running into."
                        jump guild
                    if easyMode == False and swordlvl < 3:
                        mc "I better train a bit more with my sword."
                        jump guild
                    jump impquest
                "Not yet.":
                    mc "I still have some things to do."
                    jump guild
        ##### FIRST TALIYA QUEST
        "Fetch Quest" if gabequest3 >= 1 and TaliyaQ < 1 and corbanDone == False:
            if readFQ == False:
                show black with dissolve:
                    alpha 0.5
                show text "{color=#fff}{b}{u}Go Fetch a Sword in Corban{/u}{/b}\n{i}I need someone who can go to Corban and get me the silver sword I commissioned to Philmon. For more info, ask July.{/i}\n{b}Rank{/b} — Bronze\n{b}Reward{/b} — 50 gold" with dissolve
                pause 10
                hide text
                hide black
                with dissolve
            menu:
                "Start Quest":
                    if time > 0:
                        mc "{i}Corban is too far away, I better go in the morning."
                        jump guild
                    jump TaliyaQ0
                "Maybe later":
                    mc "I still have some things to do."
                    jump guild

        "Go back":
            jump guild
    return
