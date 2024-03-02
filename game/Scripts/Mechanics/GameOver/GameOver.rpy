label GameOver:
    stop music fadeout 1
    hide screen hud
    scene gameover with fade
    play music desolation
    show text "{color=#fff}Click on one of the buttons" at truecenter
    call screen GameOverScreen

label GameOverReturn:
    stop music fadeout 1
    jump expression gameover
