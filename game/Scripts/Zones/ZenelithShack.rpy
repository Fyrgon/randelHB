label zenShack:
if zenQ >= 1:
    jump zenRomChecks
elif zenS >= 1:
    jump zenSlaveHouse



label zenSlaveHouse:
if zenS == 1:
    jump foodShenanigans
if zenS == 6 and zentimer > 0:
    mc "{i}Still to early..."
    jump home
$ chargedRune -= 1
if zenS == 6:
    if zentimer <= -3:
        jump zenLateturn
    jump zenReturn
if zenS == 7:
    jump zenMenu
if zenS >= 2:
    jump slaveMenu






label slaveMenu:
"You decide to go visit Zenelith. You take something to eat for her with you."
if zenS == 5 and gaveZBag == True:
    jump zen5F
scene zenss with fade
pause 1.2
if gaveZBag == True:
    scene shackinteriors with fade
else:
    scene shackinteriorb with fade
if submission < 1:
    show znrag angry
    znr "Oh, you're back."
elif zenS < 5:
    show znrag angry
    znr "You're back... Master."
else:
    show znrag normal
    znr @talk "Welcome, master."

if zenS == 2:
    if lastAte >= 3:
        jump zenGrope1
    else:
        jump zenGrope01
if zenS == 3:
    if submission < 1:
        jump zenGrope02
    else:
        jump zenGrope2
if zenS == 4:
    jump zenGropeEnd

if zenS == 5:
    jump zen5Menu


label zenRomChecks:
if time == 0 and zenQ == 6:
    hide screen hud
    jump zenelith7
elif zenQ == 6:
    if time > 2:
        $ time = 4
    mc "{i}It's too late, we wouldn't be able to come back before it's dark... Let's go back home."
    jump home

$ time += 1

if zenQ == 4:
    hide screen hud
    jump zenelith5

if time < 4:
    scene zenelithshack with fade
else:
    $ time = 4
    scene zenelithshackn with fade

if zenLeft == True:
    mc "{i}There's no point in coming back here again."
    $ zenRouteEnd = True
    jump forest

if zenQ == 1 and toolz == 0:
    hide screen hud
    mc "{i}Wait, what am I doing here? I still need to get the tools to repair this place."
    if dayZ >= 4:
        mc "{i}I told myself I'd have come back the day after it, yet I'm extremely late..."
        mc "{i}Let's go in and apologize."
        mc "Zenelith?"
        scene shackinteriorb
        "You walk inside the shack and find it emptier than how you left it."
        "She seems to have left."
        mc "Agh, I'm an idiot!"
        $ zenLeft = True
        mc "...Let's head back home."
        $ time += 1
    jump home
if zenQ == 1 and toolz == 1:
    hide screen hud
    if dayZ >= 4:
        mc "{i}I told myself I'd have come back the day after it, yet I'm extremely late..."
        mc "{i}Let's go in and apologize."
        mc "Zenelith?"
        scene shackinteriorb
        "You walk inside the shack and find it emptier than how you left it."
        "She seems to have left."
        mc "Agh, I'm an idiot!"
        $ zenLeft = True
        mc "...Let's head back home."
        $ time += 1
        jump home
    jump zenelith2

if zenQ == 2 and furnitureZ == False and Zdress == False:
    hide screen hud
    mc "{i}Why am I here? I still haven't bought the things I said I would."
    jump home

if zenQ == 2 and furnitureZ == True and Zdress == False:
    hide screen hud
    mc "{i}Why am I here? I still have to buy her a better dress..."
    jump home

if zenQ == 2 and furnitureZ == False and Zdress == True:
    hide screen hud
    mc "{i}Why am I here? I haven't bought the table and chairs yet."
    jump home

if zenQ == 2 and furnitureZ == True and Zdress == True:
    hide screen hud
    mc "{i}Alright, let's go inside."
    jump zenelith3

if zenQ == 3:
    hide screen hud
    jump zenelith4

if zenQ == 5:
    hide screen hud
    jump zenelith6

"You carefully walk through the outer valley until you find the path to the shack. It takes you sometime but you finally arrive after a few hours."

play music lake
menu:
    "Spend some time with Zenelith":
        hide screen hud
        jump zenTalk
    "Fuck her" if zenPlay == True and zenSexDone == False:
        jump zenSexing
    "Have sex" if zenFuck == True and zenSexDone == False:
        jump zenSexing
    "Make love" if zenLove == True and zenSexDone == False:
        jump zenSexing
    "Go back":
        jump forest
