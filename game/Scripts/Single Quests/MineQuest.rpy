label minequest:
    hide screen hud
    play music forest
    scene ambush1 with fade
    mc "I think I'm on the right track..."
    "You follow the directions on the map."
    scene black with fade
    show text "{color=#fff}After some time..." with dissolve
    pause 2
    hide text with dissolve
    scene ambush1 with fade
    mc "{i}huff... huff... huff..."
    mc "So tired..."
    mc "I've been walking for hours..."
    "You walk for a while and finally reach the mine."
    mc "There it is... haha..."
    scene cave with fade
    stop music
    show normalmc
    mc "This place is really dark..."
    "{color=#fff}Dwarf" "Who goes there?"
    pause
    show dwarf with easeinleft
    "{color=#fff}Dwarf" "What are you doing here, child?"
    show talkmc
    mc "Uhm, I'm here to take care of your Night Crawler problem!"
    "{color=#fff}Dwarf" "......"
    "{color=#fff}Dwarf" "Huh? They sent a kid?! Unbelievable!"
    menu:
        "I'm tough":
            show angry
            mc "I'm tougher than I look, you know."
        "Don't worry":
            show talksadhappymc
            mc "Don't worry, appearances can fool. I'm tougher than I look."
    "{color=#fff}Dwarf" "You'd better be! Those things are in the deeper levels of the mine. They've been there for almost a month now."
    "{color=#fff}Dwarf" "They're persistent devils and won't move an inch. When we get closer, they spit fire."
    mc "...Don't you guys have bows? Why don't you just shoot them down?"
    "{color=#fff}Dwarf" "......"
    "{color=#fff}Dwarf" "Dwarves DO NOT use bows. Ever. Have you ever seen a dwarf with a bow?!"
    if chartrait == 1:
        mc "{i}It seems that stereotypes aren't in the wrong this once."
    mc "This is the first time I've ever seen a dwarf, if I'm being honest, so I thought that maybe..."
    "{color=#fff}Dwarf" "Never! Dwarves do not muck about with archery! "
    mc "Ahhh... I get it..."
    mc "I'll go deeper into the mine then."
    "{color=#fff}Dwarf" "Don't you need a torch? It's dark as cow guts down there."
    mc "{i}Dark as cow guts? Is that even a thing?"
    mc "O-Oh, yeah, thank you."
    "{color=#fff}Dwarf" "Good luck down there!"
    "{color=#fff}Dwarf" "And please don't die!"
    mc "{i}...Aww, he's actually kinda nice."
    "{color=#fff}Dwarf" "We won't be able to take your body out and you'll make the whole mine stink!"
    mc "{i}I spoke too soon..."
    "You take the torch and go deeper into the cave."
    scene cave with fade
    "You notice that all the other miners stare at you while you go deeper into the mine. One guy looks like he's about to cry."
    "A few moments later..."
    mc "This place is creepy... No sign of Wallcrawlers though."
    "{i}THUNK"
    "Something falls onto your shoulder. You touch what it appears to feels sticky..."
    "You already know what it is. You jump back without bothering to look up."
    "A fire ball lands right in front of you."
    mc "Shit! It's a Wallcrawler."
    label wallcrawler:
    $ gameover = "wallcrawler"
    scene wallcrawler with vpunch
    "Wallcrawler" "{i}SHRIEEEEKKKKK!"
    "You see the Wallcrawler on the cave ceiling. Its eyes glow bright red in the dark."
    "You take out your bow and aim."
    menu:
        "Aim for the heart":
            mc "I don't need to risk trying to save the heart. Might as well go for the kill."
            "The Wallcrawler spits another fire ball at you as you jump to the side to dodge it."
            "As soon as you regain your balance, you release an arrow."
            play sound arrow1
            "The arrow flies and hits the Wallcrawler's heart."
            "It lets out a final shriek and falls to the ground dead."
            mc "It's a shame I couldn't get the heart but still... playing it safe was a good idea. These things look nasty. Ok, one down and who knows how many more to go."
            jump endhunt
        "Aim for the head":
            mc "I need the heart. I'll have to bring it to the floor."
            "The Wallcrawler spits another fire ball at you as you jump to the side to dodge it."
            "As soon as you regain your balance, you release an arrow."
            play sound arrow1
            "The arrow flies and hits the Wallcrawler's head."
            "It lets out a shriek and falls to the ground."
            "You quickly run to it and draw your sword."
            "As soon as you reach it, the Wallcrawler jumps to its feet and swings its razor sharp-claws at you."
            if swordlvl >= 5:
                "You quickly deflect it with your sword and cut of its arm with your next blow."
                "It shrieks and falls to the ground in pain."
                "You keep one foot on its head and plunge your sword right next to its heart. You keep stabbing around its heart as it screams."
                "And finally, you reach down and rip its heart out. The shrieks stop and the creatures lies motionless."
                $ wcheart += 1
                play sound chime
                $ renpy.notify ("{color=#fff}You obtained a Wallcrawler Heart.")
                mc "{i}Huff...{/i} I did it...{p}I DID IT!"
                mc "I got the heart!"
                mc "That was intense. I don't think I have the energy left to do that again."
                mc "I know it's valuable but I just can't do it again. I'll just kill of the next ones outright."
                jump endhunt
            "You try to deflect it but you're too late!"
            mc "Fuck...!"
            "Its claws tear right through your face. Your head is completely ripped off."
            scene black with fade
            "Not a pretty way to go. You should've trained a bit more before trying to be a badass."
            scene black with fade
            jump GameOver

label endhunt:
    scene black with fade
    "For the next few hours, you find the remaining Wallcrawler and kill them with your bow."
    mc "Oof... I guess that's all of them. There were more than I expected."
    scene cave with fade
    mc "Time to go and tell the boss his Wallcrawler problem is taken care of."
    "You go out of the deep mine."
    "As you come out, you see the faces of the other miners. You can clearly tell they're more than surprised to see you."
    show dwarf
    show normalmc
    show talkwamc
    mc "Ok, it's done."
    hide talkwamc
    "{color=#fff}Dwarf" "What?! You mean the Wallcrawler are dead?"
    show talkwamc
    mc "Yeah, they're dead, every single one of em'."
    hide talkwamc
    "{color=#fff}Dwarf" "I can't believe it... Thank you, young Adventurer! Thank you so much!"
    mc "{i}Well, that was a sudden change in character..."
    "{color=#fff}Dwarf" "You have really saved us a lot of trouble. We would've lost the mine if not for you."
    show talkwamc
    mc "I'm just doing my duty, sir."
    hide normalmc
    show smilemc
    "{color=#fff}Dwarf" "As a token of our gratitude, please have this."
    "The dwarf shows you a big diamond."
    mc "Is that a diamond?!"
    "{color=#fff}Dwarf" "I found this while I was mining one day. It's valuable. You can sell it for at least 200 silver."
    mc "{i}200 silver?! Wow, that's a lot... Dwarves are known to be generous. I guess that's true then."
    menu:
        "Take the diamond":
            show talkhappymc
            $ diamond += 1
            mc "Thank you very much!"
            "{color=#fff}Dwarf" "You earned it, young Adventurer. I wish you a safe journey back to your town."
            "{color=#fff}Dwarf" "And may we meet again!"
            mc "I hope so too."
            "You say your goodbyes and leave the mine."
            play music forest
            scene ambush1 with fade
            mc "It's not dark yet, I better keep moving."
            "You walk for several hours. Soon, the light starts to fade."
            scene ambushn with dissolve
            play music night
            mc "It's too dark to keep going. I better make camp here."
            "You set up your camp."
            mc "Well, that was easier than I thought. It's a good thing I had this manual."
            mc "No point staying awake. This place isn't that dangerous and I should have enough cover."
            mc "Better go to sleep..."
            scene black with fade
            mc "What a day. It went really well for my first quest. I feel like I've grown stronger."
            mc "I'm so tired..."
            scene black
            show text "{color=#fff}End of day [day]." at truecenter
            with dissolve
            pause 2
            hide text with dissolve
            call sleepvars from _call_sleepvars
            play music forest
            scene ambush1 with fade
            "You wake up the next day and head back to Randel."
            $ exp += 120
            $ renpy.notify ("{color=#fff}You gained 80 silver.")
            $ money += 80
            call levellingUp from _call_levellingUp_2
            $ quest1 += 4
            jump guild

        "I was thinking of something else...":
            mc "{i}He's in the mood to offer anything. I should take this chance."
            mc "I was thinking of something other than silver."
            "{color=#fff}Dwarf" "What might that be?"
            mc "You know, I prefer women over money."
            "{color=#fff}Dwarf" "Well, I-I didn't take you for such a person."
            "{color=#fff}Dwarf" "H-Huh... don't worry I can arrange something."
            "The dwarf leaves for a while then returns."
            scene nadia with fade
            "{color=#fff}Dwarf" "This is Nadia. She'll be able to service you."
            if chartrait == 1:
                "{i}Wow, it's just like in the books. Dwarven females are taller than males."
                "{i}She's hot."
            else:
                "{i}Wow, she's hot. Is she a human? She clearly doesn't look much like a dwarf."
                mc "Huh. Is she a dwarf?"
                "{color=#fff}Dwarf" "Yeah, what's wrong?"
                mc "It's that... she's not short..."
                "{color=#fff}Dwarf" "......"
                "{color=#fff}Dwarf" "You've clearly no knowledge of dwarves!"
                mc "{i}Shit, he's back in grumpy mode."
                "{color=#fff}Dwarf" "Dwarven females aren't short like the males."
                mc "Oh, sorry, I didn't know. My knowledge of Astyllian races isn't that good."
                mc "{i}So that means all dwarven females are taller than the males. Man, guess these guys have a hard time having sex..."
                "{color=#fff}Dwarf" "Hmph..."
            "{color=#fff}Dwarf" "Ok, now do whatever you want but no joining giblets!"
            mc "What?"
            Nadia "He means no sex, honey."
            mc "Oh... ok."
            mc "{i}Still better than nothing..."
            Nadia "Come on, baby, you've been keeping me for too long."
            mc "{i}Shit, I've already got a hard on."
            if mcTimid == True:
                mc "O-Ok, I'm coming..."
                Nadia "Don't be shy, baby."
            else:
                mc "Don't worry girl, I'll be right there."
                Nadia "Ooooh, haha!"
            "She leads you to a small room."
            scene black with fade
            Nadia "Ok, go ahead and take your pants off already."
            "You clumsily take off your pants."
            scene nadiasuck1 with fade
            pause 2
            Nadia "Wooow, it's so big... can't wait to taste it!"
            scene nadiasuck2 with dissolve
            Nadia "Humpf..."
            mc "Ahh... that feels so great..."
            scene nadiasuck3 with dissolve
            pause 2
            mc "Fuck!"
            scene nadiasuck2 with dissolve
            pause 1
            scene nadiasuck3 with dissolve
            pause 1
            mc "{i}Her mouth feels so good... My dick feels like it's melting."
            scene nadiasuck2 with dissolve
            pause 1
            Nadia "Humpf... Humpf... Humpf..."
            pause
            menu:
                "Take it deeper, bitch.":
                    mc "Take it deeper, bitch."
                "Can you go a bit deeper, babe?":
                    mc "Can you go a bit deeper, babe?"
            show nadiasuck3 with hpunch
            Nadia "Urk..."
            mc "Yeah... that's perfect."
            show nadiasuck3 with hpunch
            pause 1
            mc "{i}This is so hot. She really knows what she's doing."
            pause 1
            show nadiasuck2
            pause 0.3
            show nadiasuck3 with hpunch
            mc "{i}Shit, she's so good."
            pause 5
            mc "Fuck, I'm gonna cum!"
            menu:
                "Cum outside":
                    scene nadiasuckcumout1 with flash
                    pause 0.5
                    scene nadiasuckcumout2 with flash
                    pause 0.4
                    scene nadiasuckcumout2 with flash
                    pause 0.3
                    scene nadiasuckcumout2 with flash
                    pause 0.2
                    scene nadiasuckcumout2
                    pause 1
                    Nadia "Mh~"
                "Cum inside":
                    scene nadiasuck3 with flash
                    Nadia "Guh-"
                    pause 0.5
                    scene nadiasuck3 with flash
                    pause 0.4
                    scene nadiasuck3 with flash
                    pause 0.3
                    scene nadiasuckcumin1 with flash
                    pause 0.2
                    scene nadiasuckcumin2
                    pause 1
                    Nadia "Hah~"
            Nadia "That was such a huge load~ I'm guessing you liked it?"
            mc "It was amazing..."
            Nadia "Heh...{p}The fun's not over yet, babe."
            mc "{i}Oh god, I'm in heaven."
            $ persistent.nadiaBlowjob = True
            scene black with fade
            "Nadia takes off her clothes and lies on the bed."
            scene nadialick1 with fade
            Nadia "What are you waiting for?"
            Nadia "Come here and lick my pussy."
            mc "{i}You don't need to tell me twice."
            scene nadialick2 with dissolve
            Nadia "Wow- Easy there, tiger."
            mc "{i}Her pussy looks so juicy... I can't resist."
            scene nadialick2 with flash
            Nadia "Oh... Yes baby, that's the spot."
            scene nadialick2
            Nadia "Mh~! You're really good- Ahn~!"
            scene nadialick2
            pause 2
            Nadia "Ahh...~ I'm so wet...!"
            mc "{i}Really? It's my first time. Guess it's a natural born talent."
            scene nadialick2
            pause 3
            mc "{i}Let's see if she likes it a little rougher..."
            scene nadialick2 with vpunch
            Nadia "AH! This feels so good...!"
            scene nadialick2 with vpunch
            Nadia "K-Keep going~!"
            scene nadialick2 with vpunch
            pause 2
            scene nadialick2 with vpunch
            pause 1
            Nadia "Ahm~ You're gonna make me cum!"
            scene nadialick2 with vpunch
            pause 3
            Nadia "C-CUMMING~!"
            scene nadialick3 with vpunch
            pause 0.3
            scene nadialick3 with vpunch
            pause 2
            Nadia "{i}Huff... huff... huff..."
            scene black with fade
            "You both get dressed."
            scene nadia with fade
            pause
            Nadia "That was amazing, baby."
            Nadia "Hope we'll get to do it again."
            mc "Haha, me too!"
            $ persistent.nadiaLick = True
            menu:
                "Say thank you":
                    mc "Thank you, I really had a good time. Goodbye!"
                    show screen notice
                    pause
                    hide screen notice
                    $ renpy.notify ("{color=#fff}Nadia is happy.")
                    Nadia "Oh ho... you are such a cutie. Bye-bye!"
                "Just leave":
                    mc "Well, I'll be going then."
                    Nadia "...Bye-bye."
                    pause 3
            scene cave with fade
            show dwarf
            show smilemc
            "{color=#fff}Dwarf" "I won't ask for details but I hope you got what you wanted."
            show talksadhappymc
            mc "Yeah... Uhh, it was great..."
            mc "{i}This is so awkward."
            mc "Thank you."
            hide talksadhappymc
            "{color=#fff}Dwarf" "You earned it, young Adventurer. I wish you a safe journey back to your town."
            "{color=#fff}Dwarf" "And may we meet again!"
            mc "I hope so too!"
            "You say your goodbyes and leave the mine."
            play music forest
            scene ambush1 with fade
            mc "It's not dark yet, I better keep moving."
            "You walk for several hours. Soon, the light starts to fade."
            scene ambushn with dissolve
            play music night
            mc "It's too dark to keep going. I better make camp here."
            "You set up your camp."
            mc "Well, that was easier than I thought. It's a good thing I had this manual."
            mc "No point staying awake.This place isn't that dangerous and I should have enough cover."
            mc "Better go to sleep..."
            scene black with fade
            mc "What a day. It went really well for my first quest. I feel like I've grown stronger."
            mc "I can't believe what happened with Nadia. It was so hot!"
            mc "I'm so tired..."
            scene black
            show text "{color=#fff}End of day [day]." at truecenter
            with dissolve
            pause 2
            hide text with dissolve
            call sleepvars from _call_sleepvars_1
            play music forest
            scene ambush1 with fade
            "You wake up the next day and head back to Randel."
            $ exp += 120
            call levellingUp from _call_levellingUp_3
            pause 1
            $ renpy.notify ("{color=#fff}You gained 80 silver.")
            $ money += 80
            $ quest1 += 4
            jump guild
