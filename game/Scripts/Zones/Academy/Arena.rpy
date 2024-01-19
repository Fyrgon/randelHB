default taliatrain1 = False

label arenar:
    show screen hud
    play music trainig
    scene arena with fade
    if time >= 4:
        "It's too late and the school closes."
        jump home
    if TaliyaQ == 3 and time == 0 and penepisellosessoomosessuale == False:
        jump TaliyaQ3
    if TaliyaQ == 6 and Taliya6Talk == False and time < 2 and TimerT6 <= day:
        jump TaliyaQ6Pre

    menu:
        "Melee training":
            hide screen hud
            if time > 2 and TaliyaQ < 1 and TaliyaQ > 1:
                mc "I can't train right now, General Taliya is gone..."
                jump arenar
            elif TaliyaQ == 1:
                mc "Time to train with Taliya."
            elif time > 2:
                mc "I can't train right now, it's too late."
                jump arenar
            $ time += 1
            if TaliyaQ < 7:
                show animationsword
                "You train with your sword. You practice basic strikes. You feel more comfortable with the sword now."
                hide animationsword
            else:
                show animationswordnotaliya
                "You train with your sword. You practice basic strikes. You feel more comfortable with the sword now."
                hide animationswordnotaliya
            $ sword += 1
            if chartrait == 2:
                $ sword += 1
            if sword == 2:
                play sound chime
                $ renpy.notify ("{color=#00C413}Your Sword stat has increased.")
                $ swordlvl += 1
                $ sword = 0
            if swordlvl >= 3 and taliatrain1 == False:
                t "Hey recruit, come here."
                mc "Me?"
                t "Is there anyone else here?"
                mc "Ok..."
                scene tt2
                t "What is your name, recruit?"
                mc "[mc]."
                t "I see you've been training a lot."
                scene tt1
                mc "Yes, ma'am."
                scene tt2
                t "Good. I like hard-working soldiers."
                scene tt1
                mc "Thank you, ma'am."
                scene tt2
                t "Ok, let's see how much you've learned. Prepare to duel."
                mc "What?!"
                t "Come at me, soldier."
                mc "B-But I'm still a recruit... I can't possibly win against you."
                t "You think I don't know that? Just show me what you've got."
                t "I'll go easy on you."
                mc "{i}Show-off..."
                mc "Uhm... Ok then."
                pause 1.5
                scene taliaduel
                "You draw your sword."
                mc "{i}Taliya seems to be on the defensive. I guess I'll charge at her and show her what I'm capable of."
                "You decide to charge at her."
                mc "Yaaaah!"
                "As soon as you reach her, Taliya dodges your swing and quickly pushes you off balance. You fall to the ground hard."
                scene taliyaq1b
                mc "Oww..."
                t "Weak. Get up, recruit."
                scene tt2
                t "You still have much to learn. Fighting isn't about swinging your sword like a maniac. You must use your head as well."
                t "I'll teach you an important lesson. When you're against an enemy who is faster and more agile than you, you mustn't strike first."
                t "Like you did now."
                mc "......"
                t "The secret is to wait for your opponent to attack and counter it."
                t "While you counter you must try to damage your opponent. Once they are injured, they should not be as fast. That is the time to strike. Go in full force and end your opponent swiftly."
                t "That's how you use your head when fighting."
                t "You got that?"
                mc "Y-Yes, ma'am."
                t "Good. Now keep training. The next time we duel, things better be different."
                mc "Next time?... Yes, ma'am! I'll train harder."
                $ taliatrain1 += 1
                $ renpy.notify ("{color=#00C413}Your Sword stat has increased.")
                $ swordlvl += 1
            if TaliyaQ == 1:
                jump TaliyaQ1
            jump arenar

        # "Duel with Talia" if taliatrain1 == 1:
            # show talkt
            # hide screen hud
            # show normalmc
            # t "Back for more, recruit?"
            # show normalt
            # show talkmc
            # mc "Yes, ma'am."
            # hide talkt
            # hide talkmc
            # t "Let's begin then."
            # scene taliaduel with fade
            # t "Begin!"
            # "You take her advice and stay on the defensive until she attacks. Then without warning, she darts towards you."
            # "You have no time to react, she strikes your sword. It goes flying off your hand and falls on the ground."
            # t "Still weak. Train harder, recruit."
            # mc "Y-Yes, ma'am."
            # "You pick up your sword and leave."
            # "Bunis" "You can't progress any further in this version of the game."
            # "{color=#FF8EF5}Rin the Other Dev" "Taliya's route will be available in the next update!"
            # jump arenar


        "Archery Training":
            hide screen hud
            if time > 2 and magic_lamp < 1:
                mc "I can't train right now, it's too late."
                jump arenar
            elif magic_lamp > 0:
                mc "{i}Thanks to the lamp I can see the target even this late and train."
            if bowlvl < 2:
                if TaliyaQ < 7:
                    show animationbow
                else:
                    show animationbownotaliya
                "You train with the bow. You start shooting arrows but none hit the target."
                mc "Shit... I need to train more."
            else:
                if TaliyaQ < 7:
                    show animationbowgood
                else:
                    show animationbowgoodnotaliya
                if bowlvl < 5:
                    "You train with the bow. You start shooting arrows, one arrow manages to hit the target."
                    mc "Yes I hit it! Looks like I am making progress at least."
                else:
                    "You train with the bow. You've finally started hitting the target consistently."
            $ bow += 1
            if chartrait == 3:
                $ bow += 1
            if bow == 2:
                play sound chime
                $ renpy.notify ("{color=#00C413}Your Bow stat has increased.")
                $ bowlvl += 1
                $ bow -= 2
            $ time += 1
            jump arenar
        "Talk to Taliya" if TaliyaQ < 7:
            if TaliyaQ == 4 and t4qt < day+3 and Q4Pre == False:
                jump TaliyaQ4Pre
            hide screen hud
            show talkmc
            show tarm normal
            "Hey, General Taliya."
            t "What is it, recruit?"
            menu:
                "Nothing.":
                    show talksadhappymc
                    mc "Uhm... nothing, ma'am."
                    show lookdownsupmc
                    t "Then why are you here? Get back to training, recruit!"
                    jump arenar
        "Go back":
            jump academy
