default lvlRep = 0
default expLvl = 0

label levellingUp:
if level < 10:
   $ expLvl = level*level
   if exp >= expLvl:
      play sound chime
      if lvlRep == 0:
            $ renpy.notify ("{color=#00AF0E}Level up!")
            pause 0.5
      if lvlRep == 1:
            $ renpy.notify ("{color=#00C40D}Double Level Up!")
            pause 0.5
      if lvlRep == 2:
            $ renpy.notify ("{color=#00D30A}TRIPLE LEVEL UP!")
            pause 0.5
      if lvlRep == 3:
            $ renpy.notify ("{color=#00FF08}QUADRUPLE LEVEL UP?!")
            pause 0.5
      if lvlRep == 4:
            $ renpy.notify ("{color=#00FF08}PENTA LEVEL UP?!")
            pause 0.5
      if lvlRep == 5:
            $ renpy.notify ("{color=#00FF08}ARE YOU OUT OF YOUR MIND?! YOU LEVELLED UP SIX TIMES!")
            pause 0.5
      $ exp -= expLvl
      $ level += 1
      if exp > 0:
            $ lvlRep += 1
            jump levellingUp
else:
   $ expLvl = level*level*2
   if exp >= expLvl:
      play sound chime
      if lvlRep == 0:
            $ renpy.notify ("{color=#00AF0E}Level up!")
            pause 0.5
      if lvlRep == 1:
            $ renpy.notify ("{color=#00C40D}Double Level Up!")
            pause 0.5
      if lvlRep == 2:
            $ renpy.notify ("{color=#00D30A}TRIPLE LEVEL UP!")
            pause 0.5
      $ exp -= expLvl
      $ level += 1
      if exp > 0:
            $ lvlRep += 1
            jump levellingUp
$ lvlRep = 0
return
