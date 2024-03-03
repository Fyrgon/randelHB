label elfTemple:
    stop music
    if time == 4:
        "{color=#fff}Elf guard 1" "S-Stop right there!"
        "{color=#fff}Elf guard 2" "Y-You c-c-cannot go to the t-temple at the moment. P-Please leave!"
        mc "Uhm, ok."
        mc "{i}What's up with those two??"
        jump elfVillage
    scene elftemple
    hide screen hud
    menu:
        "Talk to Aerin" if savedaerin == 1:
            if time > 0:
                mc "Aerin must have already started work, I shouldn't bother her now."
                jump elfVillage
            scene highelfroom with fade
            if sawaerinelder == 0:
                $ persistent.helpAerin = True
                scene highelfroom
                show smilemc
                pause
                scene highelfroomblr
                show happya
                show talkha
                a "You came!"
                show talkwamc
                mc "Of course I did! This place looks really great. It kinda suites you."
                a "Really!"
                mc "Yeah."
                a "Can you believe it? All the elders before me sat on that exact place!"
                mc "It's pretty amazing."
                mc "So you said you had a lot of work."
                show talksada
                a "Yeah, it keeps piling up. Since... Zenelith is gone, I've got more work."
                mc "Don't worry, I'm here to help!"
                a "Really?"
                mc "{i}Now I have to argue my way to help her."
                hide talksada
                a "That's great!"
                mc "......"
                mc "{i}Ok, I was wrong."
                mc "Thank Astylla, I thought I would have to force you to let me help."
                show shytalka
                a "Oh, sorry! That's so rude of me. Hehehe... But I do need some help."
                show shytalkha
                mc "I'm glad to help. Let's get started then!"
                scene aerinworkhelp with fade
                "You help Aerin with her work. As expected, there was a lot of signing of papers, making records and reviewing records."
                "You get bored and mess around a bit."
                scene highelfroomblr with fade
                show smilemc
                show happya
                show talkha
                a "That's enough for today, [mc]."
                mc "Yeah, I'm tired too."
                a "From goofing around. Hehehehe."
                mc "Hey! I worked too, ok?"
                a "You did, you did. So [mc], would you... like to have a cup of tea at my house?"
                show shytalkha
                mc "Yeah, sure, that sounds good."
                scene aerinhouse with fade
                pause
                show smilemc
                show talkha
                a "I'll make some tea real quick."
                mc "Ok."
                hide talkha with easeoutright
                mc "{i}Morgan must still be asleep, I shouldn't bother him."
                mc "{i}That guy's got a bright future ahead of him. And a lot more years while I'm gone. Hehehe."
                "Aerin returns with the usual muffin and tea."
                scene teaaerin
                "You finish your cup of tea and eat the muffin."
                mc "Thanks, Aerin."
                a "You're welcome."
                scene aerinhouseblr
                show blushtalka
                show smilemc
                a "Uh... about that night, I-I really meant it!"
                a "I do love you, sorry if I don't show it that much. I'm just not used to it, you know?"
                show talksadhappymc
                mc "I know, let's take our time."
                a "Thank you for understanding, [mc]."
                mc "You take care now. I'll come back to help you with your work."
                show shytalkha
                a "Ok. Bye, [mc]."
                $ sawaerinelder += 1
                $ time = 4
                jump elfVillage
            scene highelfroomblr with fade
            show talkwamc
            show happya
            mc "I'm here for work, boss."
            a "You came!"
            scene aerinworkhelp with fade
            "You \"help\" Aerin with her work."
            scene highelfroomblr with fade
            show smilemc
            show talkha
            a "Foof, I'm beat. Wanna head to my place?"
            show shytalka
            a "Or not, it's totally up to you. Hehehe."
            menu:
                "Ok":
                    mc "Sure!"
                    show shytalkha
                    a "Great! Let's go then."
                    jump romanceaerin
                "Leave":
                    mc "Sorry Aerin, not today."
                    a "Oh, it's ok. See you tomorrow then."
                    mc "Ok, bye."
                    $ time += 1
                    jump elfVillage

        "Let's just play with Aerin" if aerinrel > 20:
                scene highelfroomblr with fade
                show talkwamc
                show happya
                a "You are here, [mc]... I'm always happy to see you."
                mc "Hello babe, how about a break? We can do all sorts of stuff..."
                a "Mhhh, what sort of stuff do you mean? I wouldn't mind a small break."
                show blushtalka
                menu:
                        "Lets have a quick one":
                                show shytalkha
                                a "Ah... ok... oh god, now I'm getting wet already."
                                $ aerin_one_hour_stand = 1
                                jump aerin_sex_repeat
                        "Lets do it lovingly":
                                show shytalkha
                                a "Oh [mc], I would love to experience that again."
                                $ aerin_one_hour_stand = 1
                                jump aerin_sex_first
                        "I would love to eat you out again":
                                show shytalkha
                                a "Am... Am I that tasty down... there? Em, ok... if you like it that much... I love it too."
                                $ aerin_one_hour_stand = 1
                                jump aerin_sex_licking
                        "How about I gave you a massage":
                                a "Mh. Ok, my shoulders are little stiff..."
                                mc "I will also massage your pussy with my fingers."
                                show shytalkha
                                a "Oh-? Oh! ... You naughty... ok."
                                $ aerin_one_hour_stand = 1
                                jump aerin_sex_fingering

        "Talk to Milly" if millyangry == 0:
            if evelost:
                show worriedmc
                show talksmi
                mc "How are you holding up Milly?"
                mi "...I'm doing fine. [mc]. Thanks for asking."
                mc "If there's anything I ca-"
                show angrymi
                hide talksmi
                mi "I know why you did it."
                mc "Huh?"
                mi "I know you helped Aerin win."
                show suprised
                mc "Wh-What?"
                mi "My sister was not at her best at the time of the duel. She looked like she was having a hard time standing up. I know she got enough rest the day before, so I knew someone had done something to her."
                mi "Eve showed typical symptoms of her Rosa Flower allergy; red eyes, dizziness, it had to be it."
                mc "{i}She knows!"
                mi "Finding the culprit was easy. I was the only person who knew about her allergy in the Village. And even if Aerin somehow found about it, I know she wouldn't use it. So it had to be an outsider."
                mc "That's it? So you think I did it?"
                mi "Yes, you're close to Eve, so you surely would've found out about her allergy."
                mc "S-Still, why would I... I have no reason to do it..."
                mi "...I know why you did it, and I can't say what you... did was wrong, it was partly my fault as well."
                mi "I sent you to Aerin."
                mc "Milly..."
                mi "If Eve lost, she'd have a lot of people to back her up. And if Aerin lost, she would be alone forever. That's what you thought, right?"
                mc "......"
                mi "I've thought about it many times as well."
                mc "Milly, I-I'm sorry."
                mi "......"
                mi "It's ok, I forgive you."
                mi "But [mc]...{p}We're not friends anymore."
                mc "...I understand."
                $ millyangry += 1
                jump elfVillage
            if savedaerin == 1:
                show smilemc
                show normalmi
                show talkhmi
                mi "[mc]! Our hero! Heheh."
                mc "Oh stop, I've had enough of it."
                mi "Hero~ Hero~"
                mc "At times, you do act like a child."
                mi "C'mon [mc]-ayya, what you did is more than admirable. You helped everyone. Who knows how it could've turned out otherwise?"
                mc "Well, you were the one who told me to talk to Aerin. This wouldn't have happened if it wasn't for you."
                mi "I know. Obviously I'm the mastermind behind it all."
                mc "Of course you are."
                mi "Hehehe."
                jump talkmilly
            if metmilly == 0:
                show smilemc
                show normalmi
                show talkhmi
                $ metmilly += 1
                mi "Hey, [mc]-ayya!"
                if chartrait == 1:
                    mc "{i}Hmm she called me her ayya, which is brother in Astyllian, I guess that's how they call each other here."
                    mc "{i}Ok, let's see. What's the word for sister... I think it's... nangi?"
                    show talkhappymc
                    mc "Hey, Milly-nangi"
                    show talkwami
                    mi "Looks like you know your Astyllian, [mc]!"
                    mc "I used to read a lot of books when I was little."
                    mi "That's good to hear. Most humans have a very poor understanding of Astyllian. They just learn the spells and that's it. They don't even understand that Astyllian is a whole language."
                    mc "Yeah."
                else:
                    show talkhappymc
                    mc "Oh, hey... Milly... ayyaa???"
                    show talkwami
                    mi "Hehehe. You don't know what ayya means, right?"
                    mc "Nope, no idea."
                    mi "It means \"brother\", and you are supposed to say Milly-nangi, which means \"sister\"."
                    mc "Oh, I see."
                    mi "You humans have a very poor understanding of Astyllian, you just learn the spells and that's it. You guys don't even understand that Astyllian is a whole other language."
                    mc "Yeah, I guess you're right..."

            show talkhmi
            show smilemc
            mi "So what brings you here, [mc]-ayya?"
            jump talkmilly
        "Leave":
            jump elfVillage
    return
