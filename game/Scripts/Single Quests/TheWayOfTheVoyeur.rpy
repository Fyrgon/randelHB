label wotv1:
    mc "Is that Sander?"
    mc "I guess I should talk to him. He looks like a cool-enough guy. We didn't properly get introduced last time I saw him."
    show normals
    show talkhappymc
    mc "Hey!"
    hide talkhappymc
    show smilemc
    show talkwas
    sa "Oh, hey, uh... random stranger?"
    hide talkwas
    show talksadhappymc
    mc "Oh, sorry. I'm [mc], we've met... kinda..."
    hide talksadhappymc
    show talkwas
    sa "Whaaaaaaa... really? I don't seem to remember... Oh shit, are you that kid I owe 200 silver?"
    show talkwanmc
    hide talkwas
    mc "What? No! Wait... you owe a kid 200 silver?"
    hide talkwanmc
    show talkns
    sa "None of your business, kid..."
    sa "...Thank god, it's not him..."
    hide talkns
    show talkwanmc
    mc "We met when I came to join the Academy, Evelyn was, umm... carrying yo-"
    hide talkwanmc
    show talkwas
    sa "Ohhh, you're the new kid Eve's been prattling on about! Man, I've been waiting to meet our new young Adventurer!"
    sa "So, how's it going?"
    mc "I'm doing ok, I guess."
    sa "Huh... So have you reached Bronze yet?"
    hide talkwas
    show talkhappymc
    mc "Naah, not yet."
    show talkns
    sa "Hmm..."
    "Sander smirks as if an idea just popped into his head"
    sa "You can join our party when you reach Bronze, if you'd like."
    hide talkns
    show talkhappymc
    mc "Really?!"
    hide talkhappymc
    show talkns
    sa "Totally. Eve and I always need someone to carry our gear around!"
    show thinkmc
    mc "......"
    hide thinkmc
    show angry
    mc "...Not funny..."
    hide angry
    show thinkmc
    show talksecs
    sa "Hahahahaha!"
    hide talksecs
    sa "Just joking, kid! We'd love to have you in our party!"
    show talkwas
    sa "But I'll need you to do something for me..."
    show talkmc
    mc "......"
    mc "Ok, what?"
    sa "You can't tell this to anyone... it will be our secret..."
    mc "Yeah? Fine."
    sa "Do you know what an Eye Orb is?"
    mc " Uhmm... it's that orb mages use to see things, right?"
    sa "Yeah... but do you know what it's really used for?"
    mc "...Uhmm..."
    show suprised
    hide talkmc
    sa "To spy on people!"
    hide talkwas
    show smirks
    show talkwanmc
    mc "What?"
    hide suprised
    show thinkmc
    show talkwas
    sa "Ok, kid. It's time I shared some of my wisdom, so listen up."
    sa "Through my years of adulthood, I have learned many things."
    sa "As you can tell, I'm rather popular with the ladies..."
    show talkwas
    mc "I don't thin-"
    hide talkwas
    show talkwas
    sa "Shut up and listen! As I was saying, as I am an attractive man. It's quite obvious that I've slept with {i}countless{/i} women from all over Astylla!"
    sa "Elf, human, dwarf, orc, lizard... you name it, I've laid it!"
    mc "Wait, lizard?"
    sa "What, I'm a man of culture!"
    sa "Anyways, back to my story. After some time, I began to get bored. It started to get too predictable. It lacked suspense, it lacked danger and thrill! That's when I discovered the virtues of voyeurism!"
    sa "One day, as I was traveling through the woods, I heard splashing in the nearby river."
    sa "I slowly moved towards the sound to discover a girl bathing! Well, it was nothing new. I've seen {i}plenty{/i} of girls naked."
    mc "......"
    sa "So, I was standing there looking at her bathe. That's when I realized... she was unaware of me. I got to see her in her natural state; being herself and totally unaware of my presence. "
    sa "I felt like a benevolent god looking from above at one of nature's most beautiful creations..."
    sa "It was... magnificent... art in its finest form!"
    show talksecs
    hide talkwas
    sa "That's was the story of my enlightenment!"
    hide talksecs
    mc "......"
    show talkwanmc
    mc "You know... I thought you were a cool guy but you've turned out to be one creepy dude."
    hide talkwanmc
    show talkwas
    sa "Are you going to do it or not?"
    show talkwanmc
    hide talkwas
    mc "Do what exactly?"
    sa "I want you to find an Eye Orb and spy on the girls at the Academy!"
    show suprised
    pause 3
    show angry with dissolve
    hide suprised
    mc "WHAT?! Are you fucking insane?!"
    sa "What? You want to join the party, right? You gotta do this... as... initiation... yeah."
    mc "But how do I even find an Eye Orb?"
    sa "Buy one. Mervin outside has them... I think?"
    mc "Ok, then how am I supposed to spy on girls without them noticing me?"
    sa "I don't know. You'll figure it out, you seem like a smart kid!"
    mc "B-But... I-"
    sa "Well, Eve's calling me. I gotta go! You'd better do what I say if you wanna join the gang, kiddo... Bye!"
    hide talkwas
return


label wotv2:
    show normalm
    show talksadhappymc
    mc "Uhm... Hey, Scarlet..."
    show normalmc
    show talksadhappymc
    mc "...Is there something like an invisibility spell?"
    hide talksadhappymc
    show uhm
    s "An invisibility spell?"
    hide uhm
    show talkwam
    s "Yeah... why?"
    hide talkwam
    show talksadhappymc
    mc "I was wondering if you could teach me... that spell."
    hide talksadhappymc
    show wacm
    s "Why that spell in particular?"
    hide wacm
    show talksadhappymc
    menu:
        "Lie":
            mc "Uhm... I thought... Since I'm an Adventurer, now it would be useful... for... uhm... stealth missions!"
            hide talksadhappymc
            show anythingm
            s "......"
            show surprisedblushmc
            s "You wanna peep on girls, don't you?"
            hide surprisedblushmc
            show blushtalkhappymc
            mc "Whaa- How?! I mean, no, why would I do that???"
            mc "I'm not some sick perv..."
            hide blushtalkhappymc
            show talkwam
            s "Sure, sure... well, I don't care anyway."
            s "So I'll teach you!"
            show talkhappymc
            hide talkwam
            mc "What? Really?"
            hide talkhappymc
            show talkwam
            s "I am a teacher, after all. Teaching is what I do."
            s "I don't care what you do with what I teach..."
            s "Wait... should I care?"
            s "Ah... Nah. On second thought, I don't care."
            scene black with fade
            show text "{color=#fff}Scarlet teaches you the invisibility spell." at truecenter with dissolve
            pause
            hide text with dissolve
            scene lecturemage1
            show talkwanmc
            mc "So I have to say HOLMAN and that's it?"
            hide talkwanmc
            show normalmc
            show talkm
            s "It's called chanting. And yes, you chant HOLMAN but you have to be familiar with the language of spells. How good is your Astyllian?"
            show talkmc
            if chartrait == 1:
                mc "I've studied a fair amount."
                s "Good. Make sure you are {b}fluent in Astyllian{/b}. That spell won't work if it's not pronounced correctly."
            else:
                mc "Not the best..."
                s "Make sure you are at least basically {b}fluent in Astyllian{/b}. That spell won't work if it's not pronounced correctly."
            mc "Ok, got it."
            s "Oh and another thing, the spell only lasts for a few minutes... don't get caught doing whatever you're doing, ok?"
            mc "I'm not doing anything... stealth missions, remember!?"
            s "Sure. Don't get caught on your \"Stealth Mission\". "
            mc "Thanks Scar."
            hide talkhappymc
            hide normalmc
            show sadsmilem
            $ invisibilityspell += 1
            scene academytalkblr with fade
            show normalmc
            mc "So I learned the spell. Now I just have to use the Eye Orb."
            $ q1 += 1
            jump academy


label wotv3:
    scene academytalkblr with fade
    show normalmc
    mc "Ok... now's the time."
    if magiclvl > 0:
        $ persistent.peekingTime = True
        hide screen hud
        show talkmc
        mc "HOLMAN!"
        hide talkmc
        show holmann
        mc "{i}It worked! Wow, this looks cool... Now I gotta sneak into the girl's locker room."
        scene black with fade
        show text "You slowly sneak into the girl's locker room unnoticed." at truecenter
        hide text
        scene bathescene1 with fade
        mc "{i}Oh shit... someone's actually in here... Now I gotta take out the orb."
        "You take out the orb and hold it in front of you."
        mc "{i}It's a good thing the orb's invisible too. Otherwise, people would freak out seeing a floating Eye Orb."
        "Girl" "Come out already, Gabe. You don't have to change in there. We're all girls here!"
        mc "{i}GABE!?"
        scene bathescene2 with dissolve
        g "I'm just using the bathroom, be out in a moment!"
        mc "{i}Shit, it's Gabe. Fuck!"
        "Girl" "Whatever, come in here! The water is getting cold!"
        g "Yeah, I'm coming!"
        scene bathescene3 with dissolve
        mc "{i}Oh my god... I'm about to see my childhood friend naked in front of me."
        scene bathescene4 with dissolve
        pause
        scene bathescene5 with dissolve
        $ sawgabebathnude += 1
        menu:
            "Wow, Gabe...":
                mc "{i}It's really been 6 years... Her body's really grown a lot..."
                mc "{i}I hate to admit it but Sander was right."
                scene bathescene6 with dissolve
                pause
                mc "{i}Oh, yes... Gabe..."
                scene bathescene7 with dissolve
                pause
                mc "{i}...This is both super weird and super hot at the same time."
                scene bathescene8 with dissolve
                pause
                scene bathescene7 with dissolve
                mc "{i}Ok Gabe, just do a little spin for me."
                scene bathescene7 with vpunch
                mc "{i}Fuck! The spell is starting to wear off... Why now? Nooooooo...!"
                mc "{i}I've got to go. I don't want to get caught."
            "This is wrong.":
                mc "{i}This is so wrong... But I have to do this if I want to join Eve and Sander's party. Curse you Sander!"
                scene bathescene6
                mc "{i}I guess this is enough. Time to leave."
                mc "{i}...Sorry Gabe."
        scene academytalkblr with fade
        show normalmc with dissolve
        mc "{i}Now I should {b}give this to Sander{/b}."
        $ q1 += 1
        $ peekingdone += 1
        jump academy
    show talkmc
    mc "HOLMAN!"
    hide talkmc
    show thinkmc
    mc "{i}Shit, it didn't work... I guess I didn't pronounce it right. I better {b}study some Astyllian at the library then{/b}."
    jump academy

label wotv4:
    show angry
    show normals
    mc "Here, I did it. Take the Eye Orb."
    show talkwas
    hide angry
    show normalmc
    sa "Nice work, little man. Give it here... Oooh yeah!"
    hide talkwas
    hide normals
    show smirks
    show angry
    $ goteyeorb -= 1
    mc "So, this means I'm in, right?"
    hide angry
    show talkwas
    sa "Totally! You're in... but what's with the long face? Don't act like you didn't enjoy it!"
    menu:
        "I did not":
            show angry
            mc "What, no?! I'm not a sick pervert like you."
            hide angry
            sa "Hehe... yeah, right! Anyway, thanks, kid."
            $ renpy.notify("{color=#fff}Quest completed: The Way of the Voyeur")
            $ askeve += 1
            $ sanderquest += 1
            $ q1 += 1
            jump guild
        "Yeah, I did":
            show talkhappymc
            mc "Yeah, I did... turns out, you were kinda right."
            hide talkhappymc
            sa "Hahaha! See, I told you, kid! Welcome, my young apprentice!"
            play sound chime
            $ renpy.notify("{color=#fff}Sander trusts you more now.")
            hide talkwas
            show talkhappymc
            mc "Apprentice?"
            hide talkhappymc
            show talkwas
            sa "Yes! You are my disciple now."
            hide talkwas
            show talkwamc
            mc "Hehe, fine. Thank you for accepting me as your disciple, Voyeur-sensei."
            hide talkwamc
            show talkwaecs
            sa "Hahahahaha!"
            show screen notice
            pause 2
            hide screen notice
            $ sanderrel += 5
            hide talkwaecs
            show talkwas
            sa "You're alright, little man! I'm looking forward to working with you. See ya."
            show talkhappymc
            mc "Me too."
            sa "Wait, how much was the Eye Orb?"
            show talkwanmc
            mc "30 silver. Why?"
            "Sander takes some money from his pocket."
            sa "Here, take it."
            mc "What?"
            sa "Take it. It's 30 silver."
            menu:
                "Thanks":
                    show talksadhappymc
                    mc "Thanks."
                    $ money += 30
                    $ renpy.notify("{color=#fff}You gained 30 silver.")
                    sa "See you later, kid."
                "No thanks":
                    show talkwamc
                    mc "Thanks but I don't need it."
                    sa "What the hell is wrong with you, kid? I'm giving you free money."
                    mc "It's fine."
                    show screen notice
                    pause
                    hide screen notice
                    $ sanderrel += 5
                    hide talkwaecs
                    sa "......"
                    "Sander drops the coin purse on the floor."
                    sa "Oops! I appear to have dropped my purse!"
                    scene agblr
                    show talkwanmc
                    mc "Hey!"
                    mc "Hey, don't leave... your purse..."
                    mc "..."
                    mc "......"
                    mc "What an idiot."
                    $ renpy.notify("{color=#fff}Quest completed: The Way of the Voyeur")
                    mc "Guess I'll have to take it then."
                    $ money += 30
                    play sound ("chime.mp3")
                    $ renpy.notify("{color=#fff}You gained 30 silver.")
            $ q1 += 1
            $ askeve += 1
            $ sanderquest += 1
            jump guild
