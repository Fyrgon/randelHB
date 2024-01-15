label updateinfo:
    call screen updateinfo


screen updateinfo():
    tag menu
    style_prefix "game_menu"
    add im.Blur(gui.main_menu_background, 1.5)
    add "images/updateinfo.png" xalign 0.5 yalign 0.5

    imagebutton:
        idle "updateinfoexit"
        hover "updateinfoexit1"
        action Return()
        xalign 0.8
        yalign 0.99
