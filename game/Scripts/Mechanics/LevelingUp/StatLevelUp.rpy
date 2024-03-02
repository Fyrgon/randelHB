label magicLevel:
    if easyMode:
        play sound chime
        $ renpy.notify ("{color=#00C413}Your Magic stat has increased.")
        $ magiclvl += 1
        return
    $ magic += 1
    if chartrait == 1:
        $ magic = 2
    if magic == 2:
        play sound chime
        $ renpy.notify ("{color=#00C413}Your Magic stat has increased.")
        $ magiclvl += 1
        $ magic -= 2
    return



label swordLevel:
    if easyMode:
        play sound chime
        $ renpy.notify ("{color=#00C413}Your Sword stat has increased.")
        $ swordlvl += 1
        return
    $ sword += 1
    if chartrait == 2:
        $ sword += 1
    if sword == 2:
        play sound chime
        $ renpy.notify ("{color=#00C413}Your Sword stat has increased.")
        $ swordlvl += 1
        $ sword = 0
    return
label swordLevelSuper:
    if easyMode:
        play sound chime
        $ renpy.notify ("{color=#00C413}Your Sword stat has increased.")
        $ swordlvl += 1
        return
    if chartrait == 2:
        $ swordlvl += 2
        play sound chime
        $ renpy.notify ("{color=#00C413}Your Sword stat has increased twice!")
        $ sword = 0
    else:
        $ swordlvl += 1
        play sound chime
        $ renpy.notify ("{color=#00C413}Your Sword stat has increased.")
        $ sword = 0
    return



label bowLevel:
    if easyMode:
        play sound chime
        $ renpy.notify ("{color=#00C413}Your Bow stat has increased.")
        $ bowlvl += 1
        return
    $ bow += 1
    if chartrait == 3:
        $ bow += 1
    if bow == 2:
        play sound chime
        $ renpy.notify ("{color=#00C413}Your Bow stat has increased.")
        $ bowlvl += 1
        $ bow -= 2
    return
