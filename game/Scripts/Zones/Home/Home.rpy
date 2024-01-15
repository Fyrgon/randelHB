default atHome = False

label home:
    jump versionCheck
    label home2:
    $ atHome = True
    play music home
    if time < 3:
        scene homeday
    if time == 3:
        scene homeevening
    if time > 3:
        $ time = 4
        play music night
        scene homenight
    hide screen hud

    call homeEvents

    if time < 3:
        $ timeName = "day"
    elif time == 3:
        $ timeName = "evening"
    else:
        $ timeName = "night"
    show screen interactivehome
    show screen hud
    pause

screen interactivehome():
    modal True

    imagebutton:
        xalign 0.563
        yalign 0.3941
        idle "home/home[timeName]door.webp"
        hover "home/home[timeName]doorh.webp"
        activate_sound "hover.mp3"
        if thealive == True:
            action Jump("theaStuff")
            if livingWithThea == True or knowThea == True:
                tooltip _("{color=#fff}Thea")
            else:
                tooltip _("{color=#fff}Rescued Stranger")
        else:
            action Call("noOneHome")
            tooltip _("{color=#fff}Door")
    imagebutton:
        xalign 0.765
        yalign 0.403
        idle "home/home[timeName]closet.webp"
        hover "home/home[timeName]closeth.webp"
        activate_sound "hover.mp3"
        if petefish == 1:
            action Jump("eatingFishe")
            tooltip _("{color=#fff}Eat Uncle Pete's fish")
        else:
            action Jump("inventoryHome")
            tooltip _("{color=#fff}Empty")
    imagebutton:
        xalign 0.99999999999999999
        yalign 0.99999999999999999
        idle "home/home[timeName]bed.webp"
        hover "home/home[timeName]bedh.webp"
        activate_sound "hover.mp3"
        action Jump("skippingTime")
        if time < 4:
            tooltip _("{color=#fff}Pass time")
        else:
            tooltip _("{color=#fff}Sleep")
    imagebutton:
        xalign 0.1785
        yalign 0.4799
        idle "home/home[timeName]ink.webp"
        hover "home/home[timeName]inkh.webp"
        activate_sound "hover.mp3"
        action Jump("nameChange")
        tooltip _("{color=#fff}Change your Name")
    if time < 4 and gabee1 == 3:
        imagebutton:
            xalign 0.055
            yalign 0.505
            idle "home/home[timeName]book.webp"
            hover "home/home[timeName]bookh.webp"
            activate_sound "hover.mp3"
            action Jump("readingAtHome")
            tooltip _("{color=#fff}Study")

    $ tooltip = GetTooltip()

    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True
            frame:
                xalign 0.5
                text tooltip





label skippingTime:
    hide screen interactivehome
    if time > 3:
        jump sleeping
    else:
        hide screen hud
        show black with fade
        pause 2
        $ time += 1
        jump home

label nameChange:
    hide screen interactivehome
    $ mcn = renpy.input("Change name to")
    "You name is now [mc]"
    jump home

label eatingFishe:
    hide screen interactivehome
    mc "Mmh, salmon! My favorite."
    mc "Thanks, Uncle Pete."
    $ petefish = 0
    jump home

label theaStuff:
    hide screen interactivehome
    if theagotjob == 1 and theadogfood == 0 and time < 4:
        jump theadoge
    elif livingWithThea == True:
        jump theaMenu
    elif thealive == 1:
        jump theaintr
    else:
        "If you're seeing this, either something went wrong or you're playing on an old save."
        jump theaMenu

label noOneHome:
    hide screen interactivehome
    show text "{color=#000}No one else is home.":
        align (.41, .39)
    pause 1
    hide text with dissolve
    jump home

label inventoryHome:
    hide screen interactivehome
    "You don't have anything in your closet."
    jump home
