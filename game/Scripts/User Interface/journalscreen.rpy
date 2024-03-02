screen hud():
    if time == 0:
        add "images/UI/timemorning.webp" xalign 0.01
    elif time == 1:
        add "images/UI/timenoon.webp" xalign 0.01
    elif time == 2:
        add "images/UI/timeafternoon.webp" xalign 0.01
    elif time == 3:
        add "images/UI/timeevening.webp" xalign 0.01
    elif time == 4:
        add "images/UI/timenight.webp" xalign 0.01
    else:
        add "images/UI/timemidnight.webp" xalign 0.01

    add "images/UI/balance.webp"
    vbox xalign 0.008 yalign 0.975:
        text "{size=+7}{color=#000}{b}[money]"

    vbox xalign 0.065 yalign 0.13:
        text "{color=#000}[day]"

    imagebutton:
        xalign 0.898
        yalign 0.01
        idle "UI/journal.webp"
        hover "UI/journalh.webp"
        action Hide("hud"), Show("screenjournal")
        activate_sound "map.mp3"
        tooltip _("{color=#fff}Tips & Notes")

    imagebutton:
        xalign 0.99
        yalign 0.015
        idle "UI/map.webp"
        hover "UI/maph.webp"
        action Hide("hud"), Jump("maplimbo")
        activate_sound "map.mp3"
        tooltip _("{color=#fff}Map")

    imagebutton:
        xalign 0.796
        yalign 0.03
        idle "UI/statsicon.webp"
        hover "UI/statsiconh.webp"
        if level < 10:
            action Hide("hud"), Show("playerstatistics"), SetVariable("expLvl", level*level)
        else:
            action Hide("hud"), Show("playerstatistics"), SetVariable("expLvl", level*level*2)
        activate_sound "map.mp3"
        tooltip _("{color=#fff}Stats")

    $ tooltip = GetTooltip()

    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True
            frame:
                xalign 0.5
                text tooltip
