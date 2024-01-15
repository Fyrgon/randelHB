label GuildTalk:
            menu:

                "July":
                    jump JulysCounter


                "Evelyn" if aerinlost == 0 or (evekiss == 0 and eveknow == 0) or (evekiss == 1 and eveknow == 1):
                    jump evelynGuildTalk

                "Sander":
                    jump sanderTalk


                "Cynthia" if sawcynth >= 5 and cynthmemloss == 0 and time > 0:
                    hide screen hud
                    if cynthquest2 == 1 and time == 2 and cynthquest3 == 0:
                        jump cynthquest3
                    show normalmc
                    if cynthdate == 1:
                        c "Hey."
                    if cynthtrain >= 6:
                        show talknc
                        c "Hey [mc]! What's up?"
                    else:
                        show normalcg
                        show talkwancb
                        c "What?"
                    if sawcynth >= 6:
                        menu:
                            "Confess about Thea." if thcynthconfess == 1:
                                scene cynthiaroom
                                mc "{i}Hope this goes well."
                                show worriedmc
                                show smilenc
                                mc "Cynthia, there's something I have to tell you."
                                c "Mh?"
                                show sadc
                                mc "......{p}...I-I've been cheating on you."
                                mc "I'm so sorry!"
                                c "......"
                                hide sadc
                                show angryc
                                c "Is it Thea?"
                                mc "...Yes."
                                c "So, you finally had the balls to say it."
                                c "I mean it was kinda obvious, really."
                                mc "You... You knew?"
                                c "...I had the feeling."
                                mc "...Are you mad?"
                                c "OF COURSE I'M MAD!"
                                c "You... Youuu horny asshole!"
                                c "If you had been sleeping with some other bitch I'd whoop your ass and hers too!"
                                show talksc
                                c "But Thea... She's an angel."
                                c "God this sucks!"
                                mc "I'm sorry."
                                c "So... Are you going to break up with me?"
                                mc "...Uhm, Are... you?"
                                c "I'm asking you!"
                                mc "Then, no!"
                                mc "I know you don't believe me but I love you, Cynthia! Nothing will change that!"
                                show normalcb
                                c "......"
                                c "......"
                                hide normalcb
                                hide  talksc
                                c "You don't know how much I want to kick you in the face right now."
                                mc "Do it if that pleases you. I deserve it."
                                c "Ugh... NGAH!"
                                "Cynthia punches the wall."
                                c "......"
                                show blushtalkac
                                c "...But you did confess."
                                c "And you said you still love me."
                                c "And... I, for some reason still love you."
                                c "You're... the only person who's been honest with me."
                                c "......"
                                c "{i}Sigh...{/i} Fine! You're forgiven!"
                                hide blushtalkac
                                mc "Oh thank Astylla... Thank you!"
                                c "Yeah, yeah."
                                c "Now get out, I don't want to see you for the rest of the day! No, for a week!"
                                mc "Alright..."
                                mc "But... Just know that I really do love you, Cynthia."
                                c "......"
                                c "Did you tell Thea?"
                                mc "Y-Yes..."
                                c "What did she say?"
                                mc "She said it was ok."
                                c "Just like that."
                                mc "She told me not to think of her as a shackle that prevents me from being with others."
                                c "{i}Sigh...{/i} She's too good."
                                c "You're lucky it wasn't another girl."
                                mc "I'm lucky it was you as well."
                                c "Oh, really now?"
                                c "Get out of here before I kick you out!"
                                c "...Cheesy bastard."
                                mc "Ok, ok!"
                                scene cynthiaroom
                                show sadmc
                                show angryc
                                mc "Bye..."
                                mc "...When can I see you again."
                                c "Out!!!"
                                hide sadmc with easeoutleft
                                show sadc
                                c "{i}Idiot."
                                $ thcynthconfess += 1
                                $ time += 1
                                jump home
                            "Go on a monster hunt" if cynthtrain >= 7 and cynthquest4 == 0:
                                jump cynthquest4
                            "Date" if cynthkiss >= 1 and cynthdate == 0:
                                if money < 30:
                                    mc "I should probably save up some money before going on a date with Cynthia."
                                    mc "How much was it last time?"
                                    mc "Yeah, I think it was 30 silver."
                                    jump guild
                                jump cynthdate
                            "Pay Cynthia's debt" if paycynth == False and money >= 30:
                                if cynthtrain >= 5:
                                    mc "Here's your money back."
                                    c "What money?"
                                    mc "For the cake, at the cafe."
                                    c "Ahhhh, totally forgot about that."
                                    c "It's fine, you can keep it."
                                    mc "What? Are you sure?"
                                    c "Yeah, yeah."
                                    menu:
                                        "Insist":
                                            mc "But I owe you, here take it."
                                            c "Seriously?"
                                            c "I said you can keep it."
                                            mc "It wouldn't be right."
                                            c "......"
                                            c "Well ok then."
                                            $ money -= 30
                                            "You hand her the money."
                                            c "Alright, thanks [mc]."
                                            mc "You're welcome."
                                            $ paycynth = True
                                            jump guild
                                        "Keep the money":
                                            mc "Alright, if you say so."
                                            mc "See you later then."
                                            c "Alright."
                                            $ paycynth = True
                                            jump guild
                                mc "Here's your money back."
                                c "Ahh, thanks. Wasn't hoping you would pay me back."
                                mc "Well, here it is."
                                $ money -= 30
                                "You hand her the money."
                                mc "See you later then."
                                c "Alright"
                                $ didntpaycynth -= 1
                                jump guild
                            "Nothing":
                                mc "Nothing."
                                c "Are you serious?"
                                show talkhappymc
                                mc "Hehehe."
                                jump guild
                            "Training" if cynthquest3 == 1 and time > 1 and time < 4 and cynthtrain < 7:
                                jump CynthiaTraining
                    mc "I don't want to talk to that bitch."
                    jump guild


                "Thea" if theaguild == 1 and time == 3:
                    if thdrink >= 3:
                        show blushsmilemc
                        show talksth
                        th "[mc]."
                        mc "Hi."
                        mc "I need one more drink."
                        th "You already had three, [mc]."
                        mc "B-But-"
                        show gambaruth
                        th "No more drinks for you, mister."
                        mc "Oh man."
                        jump guild
                    hide screen hud
                    show talkwamc
                    show talkhth
                    mc "Hey, Thea."
                    th "Hey, [mc], want a drink?"
                    mc "Sure. I'll have a beer."
                    th "Great. Give me a minute."
                    hide talkhth with easeoutright

                    "Thea brings you a drink after a while."
                    scene agblr with fade
                    th "Here you go, one beer."
                    mc "Thanks."
                    "You have your drink."
                    play sound gulp
                    $ thdrink += 1
                    jump guild
