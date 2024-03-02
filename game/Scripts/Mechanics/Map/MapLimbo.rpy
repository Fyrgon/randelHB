label maplimbo:
$ atHome = False
stop music fadeout 0.5
stop sound fadeout 0.5
hide screen interactivehome
play music maplimbo
if time < 3:
    scene mapbaseday
if time == 3:
    scene mapbaseevening
if time > 3:
    scene mapbasenight
call screen screenmap
pause
