screen playerstatistics():
    modal True
    add "images/playerstatistics.webp"

    vbox xalign 0.35 yalign 0.11:
        text "{size=+12}{color=#000}{i}[mcn]"

    vbox xalign 0.35 yalign 0.195:
        if mcBold == True:
            text "{size=+10}{color=#000}{i}Bold"
        elif mcNormal == True:
            text "{size=+10}{color=#000}{i}Average"
        else:
            text "{size=+10}{color=#000}{i}Timid"

    vbox xalign 0.26 yalign 0.26:
        if chartrait == 1:
            text "{size=+9}{color=#000080}{i}Bookworm"
        elif chartrait == 2:
            text "{size=+9}{color=#800000}{i}Hothead"
        else:
            text "{size=+9}{color=#008000}{i}Playful"

    vbox xalign 0.308 yalign 0.5:
        text "{size=+9}{color=#800000}[swordlvl]"
    vbox xalign 0.306 yalign 0.645:
        text "{size=+9}{color=#008000}[bowlvl]"
    vbox xalign 0.304 yalign 0.765:
        text "{size=+9}{color=#000080}[magiclvl]"

    vbox xalign 0.76 yalign 0.37:
        if level < 10:
            text "{color=#800000}{size=+15}{b}Recruit{/color}"
        elif level < 20:
            text "{color=#7A4F00}{size=+15}{b}Bronze{/color}"
        elif level < 30:
            text "{color=#7A7A7A}{size=+15}{b}Silver{/color}"
        elif level < 40:
            text "{color=#D39B00}{size=+15}{b}Gold{/color}"
        else:
            text "{color=#61B6CE}{size=+15}{b}Diamond{/color}"

    vbox xalign 0.74 yalign 0.48:
        text "{size=+9}{b}{color=#000}[level]"
    vbox xalign 0.75 yalign 0.56:
        text "{size=+5}{b}{color=#000}[exp]/[expLvl]"

    if level > 10 and level < 20:
        add "images/bronzeicon.webp" xalign 0.776 yalign 0.2

    imagebutton:
        xpos -0.81
        ypos 0.03
        idle "journalbackscrn"
        hover "journalbackscrn1"
        action Hide("playerstatistics"), Show("hud")
