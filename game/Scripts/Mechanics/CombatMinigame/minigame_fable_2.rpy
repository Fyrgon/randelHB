default fable_minigame_max_attempts = 0
default fable_minigame_fails = 0
default fable_minigame_score = 0
default fable_minigame_score_to_win = 5
default fable_minigame_difficulty = "normal"
default fable_target_speed = 1
default fable_minigame_bar = 90


init:
    transform fable_point_move(frp):
        subpixel True
        rotate_pad True
        align(0.5,-0.53)
        rotate frp


screen fable_2_minigame:
    $ attempts = fable_minigame_max_attempts - fable_minigame_fails
    add "Scripts/Mechanics/CombatMinigame/Fable_bar.png" align(0.5,1.92)
    add "Scripts/Mechanics/CombatMinigame/Fable_point.png" at fable_point_move(fable_minigame_bar)
    text "{color=#fff}Hits:[fable_minigame_score]/[fable_minigame_score_to_win] Attempts:[attempts]" align(0.5,0.1)

    if fable_minigame_bar >= -15 and fable_minigame_bar <= 15:
        key "dismiss":
            if fable_minigame_score + 1 < fable_minigame_score_to_win:
                action [SetVariable("fable_minigame_score", fable_minigame_score + 1), Show("you_press_button_good")]
            else:
                action [SetVariable("fable_minigame_score", fable_minigame_score + 1), Jump("end_fightMiniGame")]
    else:
        key "dismiss":
            if attempts > 1:
                action [SetVariable("fable_minigame_score", 0), SetVariable("fable_minigame_fails", fable_minigame_fails+1), Show("you_press_button_bad1")]
            else:
                action [SetVariable("fable_minigame_score", 0), Show("you_press_button_bad_last"), Jump("end_fightMiniGame")]


screen fable_timer_left:
    timer 0.0001 repeat True action [
        If(fable_minigame_bar <  -90, SetVariable("fable_minigame_bar", int(-90))),
        If(fable_minigame_bar >= -90, SetVariable("fable_minigame_bar", fable_minigame_bar - int(fable_target_speed))),
        If(fable_minigame_bar == -90, Hide("fable_timer_left"), Show("fable_timer_right")),
    ]


screen fable_timer_right:
    timer 0.0001 repeat True action [
    If(fable_minigame_bar > 90, SetVariable("fable_minigame_bar", int(90))),
    If(fable_minigame_bar <= 90, SetVariable("fable_minigame_bar", fable_minigame_bar + int(fable_target_speed))),
    If(fable_minigame_bar == 90, Hide("fable_timer_right"), Show("fable_timer_left")),
    ]


screen you_press_button_good:
    text "{size=-1}{color=#1e8e00}Nice move!{/color}{/size}" at fable_move_good
    timer 2.0 action Hide("you_press_button_good")

screen you_press_button_bad1:
    text "{size=-1}{color=#950000}-- Agh! --{/color}{/size}" at fable_move_bad1
    timer 0.5 action [Hide("you_press_button_bad1"), Show("you_press_button_bad2")]

screen you_press_button_bad2:
    text "{size=-1}{color=#950000}Don't lose focus!{/color}{/size}" at fable_move_bad2
    timer 1.0 action [Hide("you_press_button_bad2")]

screen you_press_button_bad_last:
    text "{size=-1}{color=#950000}That was the last hit{/color}{/size}" at fable_move_bad_last
    timer 2.0 action [Hide("you_press_button_bad_last")]


transform fable_move_good:
    align(0.5,0.5)
    linear 0.7 zoom 3.0
    linear 0.3 alpha 0.0
transform fable_move_bad1:
    align(0.5,0.5)
    linear 0.6 zoom 2.5
    linear 0.4 zoom 0.5 alpha 0.0
transform fable_move_bad2:
    align(0.5,0.5)
    linear 0.6 zoom 2.5
    linear 0.2 zoom 0.5 alpha 0.0
transform fable_move_bad_last:
    align(0.5,0.4)
    linear 1.0 zoom 3
    linear 1.0 zoom 1 alpha 0.0


label start_fightMiniGame:
    if fable_minigame_difficulty == "extreme":
        $ fable_target_speed = 150 / swordlvl
    if fable_minigame_difficulty == "hard":
        $ fable_target_speed = 110 / swordlvl
    if fable_minigame_difficulty == "norma":
        $ fable_target_speed = 60 / swordlvl
    if fable_minigame_difficulty == "easy":
        $ fable_target_speed = 20 / swordlvl
    if fable_target_speed < 1:
        $ fable_target_speed = 1
    $ fable_minigame_fails = 0
    $ fable_minigame_score = 0
    show screen fable_timer_left
    call screen fable_2_minigame


label end_fightMiniGame:
    hide screen fable_2_minigame
    hide screen fable_timer_left
    hide screen fable_timer_right
    $ renpy.pause(0.3)
    jump expression fightMiniGame
