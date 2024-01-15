label maplimbo:
$ atHome = False
stop music fadeout 0.5
stop sound fadeout 0.5
hide screen interactivehome
play music maplimbo
if time < 3:
    scene mapbaseTEST
if time == 3:
    scene mapbasee
if time > 3:
    scene mapbasenightTEST
call screen screenmap
pause
