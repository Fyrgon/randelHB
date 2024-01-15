label GameOver:
    hide screen hud
    scene gameover with fade
    show text "{color=#fff}Click on one of the buttons" at truecenter
    call screen GameOverScreen

label GameOverReturn:
    jump expression gameover
