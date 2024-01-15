screen WaterSports():
    tag menu
    style_prefix "game_menu"
    add "images/fetishWS.png" xalign 0.5 yalign 0.5

    imagebutton:
        idle "yesIdle.png"
        hover "yesHover.png"
        action Jump("WaterSportsYes")
        xalign 0.583
        yalign 0.495

    imagebutton:
        idle "noIdle.png"
        hover "noHover.png"
        action Jump("WaterSportsNo")
        xalign 0.417
        yalign 0.495
