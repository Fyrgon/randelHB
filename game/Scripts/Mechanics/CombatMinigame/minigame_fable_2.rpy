default randel_fails = 0
default fable_minigame_bar = 90
default fable_minigame_score = 0
default fable_you_press_button = 0
default fmgd = 1

init:
    transform fable_point_move(frp):
        subpixel True
        rotate_pad True
        align(0.5,-0.53)
        rotate frp


screen fable_2_minigame:
    add "Scripts/Mechanics/CombatMinigame/Fable_bar.png" align(0.5,1.92)
    add "Scripts/Mechanics/CombatMinigame/Fable_point.png" at fable_point_move(fable_minigame_bar)
    text "{color=#fff}[fable_minigame_score]/5 Points" align(0.5,0.1)

    if fable_minigame_bar >= -15 and fable_minigame_bar <= 15:
        key "dismiss":
            if fable_you_press_button == 0:
                if fable_minigame_score < 4:
                    action [SetVariable("fable_minigame_score", fable_minigame_score + 1), SetVariable("fable_you_press_button", fable_you_press_button + 1), Show("you_press_button_good")]
                else:
                    action Jump("end_fightMiniGame")
            elif fable_you_press_button == 1:
                action SetVariable("fable_minigame_score", fable_minigame_score + 0)
    else:
        key "dismiss" action [SetVariable("fable_minigame_score", 0), Show("you_press_button_bad"), If(randel_fails > 2, Jump("end_fightMiniGame"))]


screen fable_timer_left:
    timer 0.0001 repeat True action [
    If(fable_minigame_bar < -90,
        SetVariable("fable_minigame_bar", int(-90))),
    If(fable_minigame_bar >= -90,
        SetVariable("fable_minigame_bar", fable_minigame_bar - int(fmgd))),
    If(fable_minigame_bar == -90, Hide("fable_timer_left"),
        Show("fable_timer_right")),
    If(fable_minigame_bar == -90,
        SetVariable("fable_you_press_button", 0))
    ]

screen fable_timer_right:
    timer 0.0001 repeat True action [
    If(fable_minigame_bar > 90,
        SetVariable("fable_minigame_bar", int(90))),
    If(fable_minigame_bar <= 90,
        SetVariable("fable_minigame_bar", fable_minigame_bar + int(fmgd))),
    If(fable_minigame_bar == 90,
        Hide("fable_timer_right"),
        Show("fable_timer_left")),
    If(fable_minigame_bar == 90,
        SetVariable("fable_you_press_button", 0))
    ]


screen you_press_button_good:
    text "{color=#1e8e00}Good job!{/color}" at fable_move_good
    timer 1.0 action Hide("you_press_button_good")

screen you_press_button_bad:
    #hbox at fable_move_bad:
    text "{color=#950000}Agh!\nDon't lose focus!{/color}" at fable_move_bad
    timer 1.0 action [Hide("you_press_button_bad"), SetVariable("randel_fails", randel_fails + 1)]


transform fable_move_good:
    align(0.5,0.5)
    linear 0.05 zoom 1.3
    linear 0.5 zoom 1.0 alpha 0.0
transform fable_move_bad:
    align(0.5,0.5)
    linear 0.04 xalign 0.5
    linear 0.06 xalign 0.495
    linear 0.06 xalign 0.515
    linear 0.06 xalign 0.5
    linear 0.5 alpha 0.0

################################################################################
label start_fightMiniGame:
    show screen fable_timer_left
    call screen fable_2_minigame

################################################################################
label end_fightMiniGame: #End minigame. And jump continue game
    hide screen fable_2_minigame
    hide screen fable_timer_left
    hide screen fable_timer_right
    $ lastFMGscore = fable_minigame_score
    $ fable_minigame_score = 0
    $ renpy.pause(0.3)
    jump expression fightMiniGame
