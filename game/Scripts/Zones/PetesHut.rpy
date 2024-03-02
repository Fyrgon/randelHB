label fishhut:
if Taliya6Talk == True:
    if time >= 4:
        scene villagen
    else:
        scene villageback
    menu:
        "Go ask Uncle Pete about The Sword":
            show text "{color=#fff}This is a point of no return. If you keep going you'll arrive at the current ending of the game." at truecenter
            pause 4
            hide text
            show text "{color=#fff}Do you want to proceed?"
            pause 3
            hide text
            menu:
                "No":
                    jump maplimbo
                "Yes":
                    jump Chapter1End
        "Just go to the Fish Hut":
            if time > 3:
                mc "It's too late to visit Uncle Pete."
                jump maplimbo
play sound lake
play music runclepete fadein 1
if party == 1 and showpetebadge == 0 and time < 4:
        jump petebadge
jump talkingpete
