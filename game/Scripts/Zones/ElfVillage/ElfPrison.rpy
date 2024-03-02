label elfPrison:
    if time == 4:
        mc "I can't get in there now."
        jump elfVillage
    stop music
    hide screen hud
    if metnessajail == 0:
        jump nessa1
    if savedaerin == 1 and nessaquest == 0:
        jump nessa2
    scene jail
    show normaln
    show smilemc
    show talkhn
    n "Hello, [mc]."
    hide talkhn
    show talksadhappymc
    mc "Hey."
    hide talksadhappymc
    show talkhn
    n "What brings you to this dark prison today?"
    jump nessatalk
    return
