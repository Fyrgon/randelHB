default failHistory = False
default copyGabe = 0
default testDone = False

label test:
    hide screen hud
    show animation2
    pause 2
    mc "{i}Yawn..."
    mc "Nice... I didn't sleep in."
    mc "Better get ready soon or I'll miss the test."
    "You quickly get ready and head to the Academy."
    label testHangover:
    scene academytalkblr with fade
    show  normalg
    show smilemc with easeinright
    mc "Hey."
    show talkg
    g "You came!"
    $ didtest = True
    show talksadhappymc
    mc "Yup, I see you're getting more comfortable without the hoodie."
    show talkshg
    g "Uhm... yeah, I thought I could try."
    mc "That's great."
    g "Good luck then, give it your best!"
    mc "Yes, ma'am!"
    g "Hehehe."
    show talkwamc
    mc "Just make sure you don't cover your paper."
    show talksg
    g "Huh? Why?"
    mc "I... might need some... support."
    show cuteg
    g "Hey! No copying!"
    mc "I was just kidding."
    hide cuteg
    g "It's for your own good. If we get caught, we both get expelled, then and there."
    mc "Alright, alright, I get it."
    scene black with fade
    "The both of you go in and get seated."
    "You sit closer to Gabe."
    "To your surprise, a lot of students haven't shown up."
    scene lecturetalk with fade
    b "Ok, everyone is here. I'll now be handing out the papers. You have thirty minutes. No talking and no copying! Get a 5/10 and you'll pass."
    "Boris walks around the class handing out the papers."
    "You get your paper."
    scene testgabe1 with fade
    b "You can start now. I do not need to remind you that if you fail this test, you will have to repeat this class. Good luck."
    mc "{i}Whew... Ok, let's do this."
    $ correct = 0
    "1. How old is Randel?"
    $ testAnswer = "340 years"
    menu:
        "100 years":
            "100 years."
        "130 years":
            "130 years."
        "320 years":
            "320 years."
        "340 years":
            "340 years."
            $ correct += 1
        "Copy from Gabe":
            call copyingGabe
    "2. Who founded Randel?"
    $ testAnswer = "James Randel"
    menu:
        "John Randel":
            mc "Jhon Randel."
        "James Randel":
            mc "James Randel."
            $ correct += 1
        "Mark Randel":
            mc "Mark Randel."
        "Jack Randel":
            mc "Jack Randel."
        "Copy from Gabe":
            call copyingGabe
    "3. What was Randel famous for?"
    $ testAnswer = "Its rich soil"
    menu:
        "Its rich soil":
            mc " Its rich soil."
            $ correct += 1
        "Its wheat":
            mc "Its wheat."
        "Its beauty":
            mc "It's beauty."
        "Its Adventurers' Guild":
            mc "Its Adventurers' Guild."
        "Copy from Gabe":
            call copyingGabe
    "4. What was one of Randel's old names?"
    $ testAnswer = "Randelton"
    menu:
        "Randelia":
            "Randelia."
        "Randelburg":
            "Randelburg."
        "Randelton":
            "Randelton."
            $ correct += 1
        "Randella":
            "Randella."
        "Copy from Gabe":
            call copyingGabe
    "5. Who became the king after King Woren?"
    $ testAnswer = "Ron"
    menu:
        "Rem":
            "Rem."
        "Rei":
            "Rei."
        "Ron":
            "Ron."
            $ correct += 1
        "Reg":
            "Reg."
        "Copy from Gabe":
            call copyingGabe
    "6. Who summoned the Demon King?"
    $ testAnswer = "Rem"
    menu:
        "Rem":
            "Rem."
            $ correct += 1
        "Rei":
            "Rei."
        "Ron":
            "Ron."
        "Reg":
            "Reg."
        "Copy from Gabe":
            call copyingGabe
    "7. What mountains did King Ron have to cross during the Great Displacement?"
    $ testAnswer = "Mountains of Arp"
    menu:
        "Central Atoll":
            "Central Atoll."
        "Red Mountains":
            "Red Mountains."
        "Mountains of Arp":
            "Mountains of Arp."
            $ correct += 1
        "Misty Mounts":
            "Misty Mounts."
        "Look at Gabe's paper":
            call copyingGabe
        "Copy from Gabe":
            call copyingGabe
    "7. Who killed the Demon King?"
    $ testAnswer = "Sir Gladius Hans"
    menu:
        "Sir Jhon Albert":
            "Sir Jhon Albert."
        "Sir Gregory Hans":
            "Sir Gregory Hans."
        "Sir Jamie Hans":
            "Sir Jamie Hans."
        "Sir Gladius Hans":
            "Sir Gladius Hans."
            $ correct += 1
        "Copy from Gabe":
            call copyingGabe
    "8. In which battle was the Demon King slain?"
    $ testAnswer = "the Final Hern Siege"
    menu:
        "The Battle of Dermis":
            "Battle of Dermis."
        "The Final Hern Siege":
            "The Final Hern Siege."
            $ correct += 1
        "The Last Westian Seige":
            "The Last Westian Siege."
        "The Battle in the Darklands":
            "The Battle in the Darklands."
        "Copy from Gabe":
            call copyingGabe
    "10. Which race built the modern Astyllian Walls?"
    $ testAnswer = "Dwarves"
    menu:
        "Elves":
            "Elves."
        "Humans":
            "Humans."
        "Dwarves":
            "Dwarves."
            $ correct += 1
        "Demons":
            "Demons."
        "Copy from Gabe":
            call copyingGabe
    b "Ok, times up! Please hand over your papers."
    mc "{i}Thank Astylla, I finished it in time!"
    "You hand over your paper."
    g "How was it?"
    menu:
        "Bad":
            mc "Not very happy about it."
            g "Let's try to be positive..."
        "Good":
            mc "Better than I thought."
            g "That's a relief."
        "Not sure":
            mc "Not very sure."
            g "I'm sure you did well."
    if copyGabe > 0:
        mc "Uhm... Thanks..."
        g "...Don't mention it."
    "Boris starts marking the test. Some time passes and he finally sets them down."
    scene lecturetalk with fade
    b "Ok, I have the results. First, I'll be calling out the names of the students who failed the test."
    if correct < 5:
        $ failHistory = True
        b "Deacon... Saul... Chicco... Pat... {p}...and [mc]."
        b "This means you will have to repeat this class before moving onto the next grade. I wish you all the best of luck."
        "Boris hands out the other papers."
        b "{size=-3}Oh, by the way, Cody, I need to talk with you..."
        "You leave the class."
        scene academytalkblr with fade
        show talksg
        show worriedmc
        g "[mc], I'm sorry."
        mc "It's ok, you tried your best. Thanks, Gabe."
        g "Yeah but-"
        mc "It's fine. I'll just have to make it big as an adventurer."
        g "...I hope you do, honestly."
        mc "Well, I'm heading home now, see you."
        g "Bye-bye."
        jump home
    b "Deacon,{p}Saul,{p}Chicco,{p}...and Pat."
    b "This means you will not continue your studies in this Academy. I wish you all the best of luck."
    scene academytalkblr with fade
    "Boris hands out the other papers. You get yours."
    b "Well done."
    mc "Th-Thank you sir."
    "Everyone, except one student, leave the class."
    b "{size=-3}So, Cody, about that scolarship..."
    scene academytalkblr with fade
    if correct == 10:
        show suprised
        mc "I got [correct] out of 10!"
        show smilemc
        show talkwag
        g "10 out of 10! That's amazing, [mc]!"
        mc "Thanks!"
    else:
        show talkhappymc
        mc "I got [correct] out of 10."
        show talkshg
        g "Thats great! You made it."
        mc "Yeah, thanks."
    show talkwag
    mc "How did you do?"
    show talkshg
    g "I got a 10."
    mc "Of course."
    g "Hehehe."
    show talksadhappymc
    mc "So, this means I'm safe?"
    g "Yeah, you did good. I'm proud of you."
    mc "Thanks."
    g "..."
    g "...See you later then."
    mc "Okay, bye."
    scene academytalkblr
    show prot smile
    show talkshg
    show blushtalkg with dissolve
    pause 1
    g "You... can still visit, even if we... don't have studying to do."
    mc @smilet "Y-Yeah! Alright."
    $ testDone = True
    $ time = 3
    jump academy




label copyingGabe:
    $ copyGabe += 1
    if copyGabe == 1:
        $ correct += 1
        mc "{i}Better look slowly."
        "You slowly take a peek at Gabe's paper."
        "She notices and covers her paper."
        mc "{i}Come on."
        mc "{i}Guess I'll have to write one myself."
        mc "...{p}..."
        g "{size=-5}Psst."
        "You turn to Gabe. She moves the paper for you to see."
        mc "..."
        "You look at her paper and see that the answer is [testAnswer]."
        mc "{size=-5}Thanks."
        "She blushes as she takes the paper back and starts to write as you write down the correct answer."
        return
    if copyGabe == 2:
        $ correct += 1
        "You peek Gabe's paper once again."
        mc "{i}Ahh... I knew it was [testAnswer]."
        "You write the answer down on your test, but you notice that Boris is looking at you suspisciously."
        mc "{i}I think it's better if I don't copy again..."
        return
    if copyGabe == 3:
        "You try to peek once again and not get seen, but suddenly your hear a hand slam on your desk."
        "When you turn around Boris is right in front of you."
        b "I am very disappointed in you."
        "He takes your paper away and sits at his desk. You sigh."
        mc "{i}I knew I shouldn't have..."
        "You wait in silence until the class is done. Boris says your name while listing everyone who failed, and you sadly leave the classroom."
        scene academytalkblr with fade
        show talksg
        show worriedmc
        g "[mc]..."
        mc "I know, I know, I'm an idiot."
        g "Sigh... You are."
        g "Well... see you tomorrow."
        mc "Yeah, uh, see you."
        jump home
    $ correct += 1
    return
