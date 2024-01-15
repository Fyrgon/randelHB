label gabehouse:
    stop music
    if time == 4:
        scene villagen
        mc "She's probably asleep."
        jump maplimbo
    if gabee1 == 0:
        scene villageback
        mc "I have no reason to go there."
        jump maplimbo
    if time < 2:
        scene villageback
        mc "She's not home yet. I should come after noon."
        jump maplimbo
    if gabee1 >= 1 and readgabe1 == 0:
        scene villageback
        mc "{i}I should study about the History of Randel. She said we will be having a study session."
        mc "{i}I should get a book."
        jump maplimbo
    scene gaberoomd
    hide screen screenmap
    if gabee1 >= 1 and readgabe1 >= 1 and studygabe1 == 0 and gabeintro == 0:
        jump gabeStudyingPt1
    if gabee1 >= 1 and studygabe1 == 0 and gabeintro == 1:
        hide screen hud
        mc "Hi, Gabe."
        g "Hey, [mc]."
        g "Let's get started, I hope you studied."
        mc "I'm ready."
        "The both of you go to your normal positions."
        jump gabeQuestions1
    if gabee1 >= 1 and studygabe1 == 1 and gabeintro == 1 and studygabe2 == 0:
        jump gabeStudyingPt3
    if gabee1 >= 1 and studygabe1 == 1 and gabeintro == 1 and studygabe2 == 1:
        show talkg
        show smilemc
        g "Hi, [mc]."
        show talkhappymc
        mc "Hey."
        g "What's up?"
        $ GabeAcademy = False
        $ GabeHome = True
        call gabrialTalk
