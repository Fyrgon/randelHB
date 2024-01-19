define readFQ = False

label QuestBoard:
            if level < 5:
                "I haven't reached level 5 yet. I can't go on quests yet."
                jump guild
            $ checkboard += 1
            mc "Let's see..."
            menu:
                "Investigate goblin camp" if gabe2 == 1 and level >= 10 and gabequest2 == 0:
                    if swordlvl < 2 and bowlvl < 2:
                        mc "I don't think I'm ready for this yet. I should go train a bit more."
                        jump guild
                    "There have been reports of a small tribe of goblins occupying the abandoned castle in the forest. You have to scout the location and report back to the Guild."
                    "Rank — Bronze"
                    "Reward — 100 silver"
                    menu:
                        "Start quest":
                            mc "Let's start then."
                            jump gabequest2
                        "Later":
                            mc "I'll still need time."
                            jump guild

                "Wallcrawler infestation" if quest1 < 3:
                    if quest1== 1:
                        menu:
                            "Start quest":
                                if icamping == 1:
                                    if swordlvl < 2 and bowlvl < 2:
                                        mc "I don't think I'm ready for this yet. I should go train a bit more."
                                        jump guild
                                    if readwallcrawler == 0:
                                        mc "Wait. I still need to read about the Wallcrawlers. I better go to the Library and check it out. I need to know what I'll be running into."
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
                    mc "Let's see."
                    "The coal mine nearby is infested with Wallcrawlers. The miners require help in exterminating these creatures. Please provide your assistance."
                    "Rank — Recruit"
                    "Reward — 40 silver"
                    mc "This looks like something I can handle... I think."
                    mc "But what are Wallcrawlers? I should {b}look into them at the Library.{/b}"
                    $ quest1 += 1
                    jump guild

                "Delivery Quest" if aquest2 < 2:
                    if aquest2 == 0:
                        "The town of Yorkel has been having trouble with Imps. They require a shipment of Black Tourmaline Crystals. Please provide your assistance."
                        "Rank — Recruit"
                        "Reward — 80 silver"
                        mc "A delivery quest? Man, these are boring..."
                        mc "I have no choice though... it's the only quest on the board I am allowed to handle."
                        mc "Imps? I better look them up in the {b}Book of Monsters{/b}."
                        $ aquest2 += 1
                        jump guild
                    menu:
                        "Start Quest":
                            if swordlvl < 3:
                                mc "I better train a bit more with my sword."
                                jump guild
                            if readimp == 0:
                                mc "Wait. I still need to read about Imps. I better go to the Library and check it out. It's a good idea to know what I'll be running into."
                                jump guild
                            hide screen hud
                            mc "{i}I should grab the crystals from July."
                            play sound chime
                            $ renpy.notify("{color=#fff}Quest started: Delivery quest")
                            scene adgc1
                            mc "Hey, July. I accepted the Yorkel delivery quest. May I get those crystals?"
                            j "Oh, yes, of course! They're right here."
                            "July goes in and brings a big bag."
                            j "Here you go! It's a bit heavy. I hope you can carry this all the way to Yorkel!"
                            mc "I'll manage, thanks."
                            "You look in the bag. It's filled with beautiful black crystals."
                            mc "What are these things anyway?"
                            j "Oh, those are the Black Tourmaline Crystals mentioned in the flyer."
                            mc "Yeah, I know that but why do they need these? Wouldn't they need like swords and shields if they have an Imp problem?"
                            j "Well, these are cleansing crystals. Imps won't even come near if you have these arround you!"
                            mc "I see... if they don't come to you, you won't need the weapons?"
                            j "Exactly! Hehe... you better leave soon now. The notice has been there for a few days. They'll be needing this delivery more than ever."
                            mc "Yeah, ok. Bye!"
                            j "Good luck!"
                            j "Oh and bring me some cheese if you can, please."
                            mc "What?"
                            j "Cheese! Yorkel has the best dairy farms in all of Astylla. Their cheese is the best."
                            mc "Uh... Alright, I'll see what I can do."
                            j "Yay!!"
                            "You leave the Guild."
                            jump impquest
                        "Not yet.":
                            mc "I still have some things to do."
                            jump guild

                "Fetch Quest" if gabequest3 >= 1 and TaliyaQ < 1:
                    if readFQ == False:
                        "\"I need someone who can go to Corban and get me the silver sword I commissioned to Philmon. For more info, ask July.\""
                        "Rank — Bronze"
                        "Reward — 50 silver"
                    menu:
                        "Start Quest":
                            if time > 0:
                                mc "{i}Corban is too far away, I better go in the morning."
                                jump guild
                            hide screen hud
                            mc "{i}Alright let's grab this and go talk with July"
                            scene adgc1 with dissolve
                            j "Hey there, [mc]."
                            mc "Hi July, can I take this quest?"
                            "July looks at the quest note and then reaches behind the counter. When she gets back up she puts a small letter on top of the counter, you can see something written on the envelope."
                            j "Of course you can. This has the address you need to go to and inside there's a letter that confirms you're there to take the sword back to Randel."
                            mc "Alright, thank you."
                            "You grab the note and say bye to July as you leave the guild."
                            scene villageback with fade
                            mc "{i}Alright this here says that I need to go to Shay's Forge on Hern Street... Hopefully it doesn't take much to find it so that I can get back before it's too dark."
                            "You put the letter inside a pocket of your backpack and then decide to set off."
                            jump TaliyaQ0
                        "Maybe later":
                            mc "I still have some things to do."
                            jump guild

                "Go back":
                    jump guild
