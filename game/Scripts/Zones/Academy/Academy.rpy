label academy:
    if time > 3:
        scene villagen
        mc "The Academy is closed."
        jump maplimbo
    if faila == 1:
        scene villageback
        "...I can't go to the Academy anymore."
        jump maplimbo
    hide screen screenmap
    scene academy
    stop music
    play music academy  fadein 1

    if cynthquest6 == 1 and savecynthia == 0 and cynthmemloss == 0:
        hide screen hud
        scene cynthia
        "As you walk in you see Cynthia talking with a group of students."
        "After a while, the students leave and Cynthia is alone."
        scene academytalk
        mc "Guess I'll say hello."
        show talksadhappymc
        show normalc
        mc "Hey."
        show talkc
        c "Oh, hello."
        show thinkmc
        mc "......"
        c "......"
        mc "{i}Something doesn't feel right."
        mc "So thinking on going any quests?"
        c "Quest?"
        c "I'm very sorry but I don't think I've met you before."
        mc "......?"
        mc "Cynthia it's me, [mc]."
        show talkshc
        c "I'm really sorry, I don't seem to remember you. When did we meet?"
        show worriedmc
        mc "{i}W-Wait don't tell me."
        mc "You- ...Are you serious? I'm [mc]."
        mc "W-We went on quests together, we've slain monsters, you saved my life!"
        c "...?"
        c "Uhm... I think you've gotten me confused with someone else."
        c "I'm very sorry but I'm late for class. I should go."
        hide normalc
        hide talkc
        hide talkshc with easeoutright
        mc "Cynthia!"
        mc "{i}Fuck!"
        mc "{i}She's forgoten everything. Did she erase her memories."

        mc "......"
        mc "{i}Shit! Why didn't I stop her that night? I could've said something."
        "{i}I have to ask July!"
        $ cynthmemloss += 1
        jump academy


    if cynthquest6 == 1 and cynthkiss == 0 and savecynthia == 1:
        jump preCynthDate


    if gabequest2 >= 1 and gabequest3 == 0:
        jump gabequest3


    if day >= 5 and gabee1 == 0 and time == 2:
        jump gabeBeginning


    if day >= 4 and sawcynth < 2:
        jump preCynthia


    if day >= 7 and sawcynth == 2:
        jump cynthiaBeginning


    show screen hud
    "You arrive at the Academy."
    menu:
        "Get Thea's clothes" if theaclothestimerstart > 0 and theaclothes == 0 and theaintro == 0:
            if girlclothes == 1:
                "You go and check in your locker. In it, you find a small bag."
                mc "{i}I guess this is it."
                play sound chime
                $ renpy.notify("{color=#fff}You got clothes for Thea.")
                $ theaclothes += 1
                jump academy
            "You go into your class room. You find a small bag placed on your desk."
            mc "{i}I guess this is it."
            play sound chime
            $ renpy.notify("{color=#fff}You got clothes for Thea.")
            $ theaclothes += 1
            jump academy

        "Peeping Time!" if invisibilityspell == 1 and ieyeorb == 1 and peekingdone == 0:
            jump wotv3

        "Talk":
            menu:

                "Talk to Gabe":
                    hide screen hud
                    scene academytalkblr
                    show talkhappymc
                    show normalgabe
                    mc "Hey, Gabe!"
                    show smilemc
                    show talkgabe
                    g "Hi [mc], what's up?"
                    $ GabeAcademy = True
                    $ GabeHome = False
                    call gabrialTalk from _call_gabrialTalk

                "Talk to Cynthia" if sawcynth >= 3 and cynthmemloss == 0 and cynthkiss == 0:
                    jump cynthiaAcademyTalk

        "Meet Boris" if gabee1 == 2:
            if time < 2:
                mc "He must be in his class now. I should probably meet him after noon."
                jump academy
            hide screen hud
            mc "Hope this goes well."
            mc "{i}Who am I kidding, he's going to kill me."
            scene lecture with fade
            mc "Excuse me, Mr. Boris?"
            b "Hmmmm?"
            scene lecturetalk
            b "What is it, kid?"
            if historyClass < 2:
                mc "Sir, I was loo-"
                b "I haven't seen you before. Are you in my class?"
                mc "{i}Shit!"
                if caughtboris == 1:
                    mc "{i}He doesn't remember me? Even though I got caught day-dreaming on the first day of his class?"
                mc "I am, sir, b-but I haven't attended much of your classes."
                b "Hmm! That's why!"
                b "Why are you here?"
                mc "I was looking for a history book. The Library didn't have them, I thought if I could..."
                b "What is it, boy? Spit it out!"
                mc "I thought if could borrow one from you, sir..."
                b "......"
                b "You're studying for the test?"
                mc "Yes, sir."
                b "I'm assuming you want the \"Randel's Local History Book\", am I correct?"
                mc "Y-Yes, sir."
            else:
                mc "Sir, I was looking for the history book at the library but, uhm, you see-"
                b "What is it? Just say it already."
                mc "A-All copies had already been borrowed when I went, so I was wondering if you could lend me one..."
                b "...Was what I taught in class not enough?"
                mc "N-No, sir, It was enough! I just... would rather be safe than sorry."
                b "You know you just need 5/10 to pass the test, right?"
                mc "I do, sir."
                mc "{i}I definitely did not. That's so little..."
                b "...And you're still going to study?"
                mc "Yes, sir."
            b "Take this."
            "Boris gently places a book on his desk."
            mc "{i}Did he actually give me the book just like that?"
            mc "Th-Thank you, sir. I'll return it as soon as I can."
            b "Keep it."
            mc "Huh?"
            b "I said keep it. I have another copy."
            mc "But, sir-"
            if historyClass < 2:
                b "It's fine. If you care enough to ask I don't mind. I can understand you might be busy and the law doesn't care whether or not you show up to my class as long as you pass the tests. Keep it."
            else:
                b "Most students can either read and so they never show up to class because they can study from the book, or they can't and show up to every single class."
                b "It's not often someone is so interested to both show up and want to study more. You can keep the book, kid."
            mc "..."
            mc "Th-Thank you, sir."
            "You creep to his desk and take the book."
            b "Now, go and study."
            mc "Y-yes, sir. Thank you, sir."
            mc "{i}I don't know what the hell just happened but I got what I wanted."
            $ gabee1 += 1
            jump academy


        "Go to History Class":
            jump borisClass

        "Go to the Magical Arts Class":
            stop music
            scene lecturemage1 with fade
            jump magicalClass

        "Go to the Arena":
            if time > 3:
                mc "The Academy is closed. I can't go there now."
                jump academy
            jump arenar
