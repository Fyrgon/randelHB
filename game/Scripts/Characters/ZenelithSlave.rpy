default firstZBath = True
default chargedRune = 0
default lastAte = 0
default submission = 0
default addiction = 0
default degradation = 0
default analDone = False
default endZenFeed = False
default endZenUse = False
default endZenPusnih = False
default endZenBathe = False


label zenMenu:
hide screen hud
"You decide to go visit Zenelith. You take something to eat for Zenelith with you."
scene zenss with fade
pause 1.2
scene shackinteriors with fade
show prot normal
if addiction < 5 and degradation < 5 and submission < 5:
    show znrag normal
    znr @talk "Welcome, master."
else:
    show znrag smile
    znr @talk "Master! You're back!"
if lastAte >= 3:
    zn @talk "...I-I'm really hungry, master."
label zenMenuC:
show screen hud
scene shackinteriors
show prot normal
if addiction < 5 and degradation < 5 and submission < 5:
    show znrag normal
else:
    show znrag smile
menu:
    #"Talk":
    #    ""
    "Feed" if lastAte > 0:
        $ endZenFeed = True
        mc @smirkt "Hungry?"
        zn @talk "Yes, master."
        menu:
            "Don't have her do anything":
                mc "Here, take some."
                zn "..."
                mc "C'mon. I'm being generous. If you don't take it, I'll have you do something instead."
                zn "Y-Yes! S-Sorry master."
                $ addiction += 1
                $ lastAte = 0
                jump zenMenuC
            "Grope":
                call zGrope from _call_zGrope
                call ItsFoodOrNothing from _call_ItsFoodOrNothing
                jump zenMenuC
            "Fingering":
                call zFinger from _call_zFinger
                call ItsFoodOrNothing from _call_ItsFoodOrNothing_1
                jump zenMenuC
            "Blowjob":
                call zBJ from _call_zBJ
                call ItsFoodOrNothing from _call_ItsFoodOrNothing_2
                jump zenMenuC
            "Sex":
                call zSex from _call_zSex
                call ItsFoodOrNothing from _call_ItsFoodOrNothing_3
                jump zenMenuC
            "Anal" if (if endZenFeed = True and endZenUse = True and endZenPunish = True and endZenBathe = True) or  analDone == True:
                if analDone == False:
                    jump zenFirstAnal
                call zAnal from _call_zAnal
                call ItsFoodOrNothing from _call_ItsFoodOrNothing_4
                jump zenMenuC
    "Use":
        $ endZenUse = True
        menu:
            "Grope":
                call zGrope from _call_zGrope_1
                jump zenMenuC
            "Fingering":
                call zFinger from _call_zFinger_1
                jump zenMenuC
            "Blowjob":
                call zBJ from _call_zBJ_1
                jump zenMenuC
            "Sex":
                call zSex from _call_zSex_1
                jump zenMenuC
            "Anal" if analDone == True:
                call zAnal from _call_zAnal_1
                jump zenMenuC
    "Punish":
        $ endZenPunish = True
        call zSpanking from _call_zSpanking
        $ addiction -= 1
        jump zenMenuC
    "Let her bathe":
        $ endZenBathe = True
        mc @smirkt "You up for a bath?"
        zn @smilet "A-A bath?"
        mc @smirkt "Yes."
        if firstZBath == True:
            mc @smirkt "There's a lake nearby. I'll take you there and you'll be able to bathe yourself."
            zn @angryt "...And you're coming with me?"
            mc @talk "Of course."
            $ firstZBath = False
        mc @talk "Now let's go, then."
        jump zBathing
    #"Toilet" if watersports == True:
    #    ""















label zGrope:
mc @smirkt "Good. Take off your top."
"Zenelith stays still for a second, then she takes off her top."
scene black with dissolve
pause 0.2
scene znboobnude
show znboobworried
pause 2
zn "..."
mc "Time to have some fun."
scene znboobgrope
show znboobfing with hpunch
pause 2
zn "Mnh..."
mc "Open your mouth wide."
zn "Y-Yes..."
scene znboobgrab
show znboobmouth with vpunch
pause 2
show znboobmouth with vpunch
zn "Ah~!"
mc "Enjoying it like the slut that you are."
show znboobmouth with vpunch
zn "Mnh~ Ahn!"
menu:
    "Continue":
        show znboobmouth with hpunch
        zn "Hah~! Pleash...~"
        show znboobmouth with hpunch
        zn "S-Shthop~! Ah~!"
        show znboobmouth with vpunch
        zn "N-Not like th- AH~!"
        mc "Heheh... You're all red.{p}Fine, this is all for today."
        scene znboobnude
        show znboobshy
        show znboobeyeside
    "Stop":
        mc "{i}That's enough teasing for now."
        mc "Alright, I'm satisfied..."
        scene znboobnude
        show znboobshy
        show znboobeyeside
return

label zFinger:
mc @smirkt "Alright, get all naked."
zn "..."
"Zenelith quietly strips down."
stop music
scene znfingerbase1 with fade
zn "...?"
mc "Time to have fun."
scene znfingerbase1
show znfinger0 with dissolve
pause 1
zn "Nh..."
scene znfingerbase2
show znfinger2 with vpunch
zn "AH~!"
hide znfinger0
hide znfinger2
show znfinger1
mc "Would you look at that? Already wet."
zn "M-Master..."
mc "Yes, slut?"
"You don't give her time to reply that you start moving your fingers again."
show zenfingering1
zn "Mnh~ K-Keep going!"
mc "I shall."
show zenfingering1 with dissolve
pause 2
zn "Ahmn~... Ngh..."
mc "{i}Let's make this a bit better for her~"
hide znfinger1
hide znfingering1
show zenfingering2 with vpunch
zn "Wha- ANH~! Ah~!"
mc "Better isn't it?"
zn "I- Mnh~! I'm gonna—"
scene znfingerbase3
show zenfingering2 with flash
zn "CUM~!"
scene znfingerbase3
show znfinger1 with flash
show znfinger2 with flash
pause 0.1
show znfinger1 with flash
pause 0.2
show znfinger5 with flash
pause 1.3
mc "You always come a lot from this, don't you?"
return

label zBJ:
mc @smirkt "Good, I've got just the thing for you then. Sit down, naked."
znr @talk "Y-Yes, master."
scene bjanimstart with fade
pause 2
mc "{i}Always a great view, even with that look of hers."
"You pull down your pants and take out your cock. You smile satisfied when she manages to not change expression when you do so."
mc "Now open your mouth wide..."
scene zenbj with dissolve
pause 1
mc "{i}Ahh... This feels amazing... So wet and hot..."
mc "You're doing a great job taking it, toy. Keep going just like this..."
mc "{i}Sure, she still looks like she wouldn't mind killing me, but... Right now, she's taking my dick and she's not complaining, so it's all good."
scene zenbj with dissolve
pause 5
mc "{i}God, this is so good..."
scene zenbj with dissolve
pause 1
mc "{i}I-I might..."
scene zenbj with flash
mc "C-Cum!"
scene zenbj with flash
pause 0.1
zn "Mnh-!"
scene zenbj with flash
pause 0.1
scene bjanimcum with flash
mc "Ahh... Much better."
return

label zSex:
hide screen hud
mc @talk "Alright, get on the bed. Now"
znr @talk "...Yes, master."
"She gets on the bed and lays down, know very well what's coming."
scene zenpress with fade
pause 1
zn "AH~!"
mc "Yes, moan just like that, slut."
scene zenpress with dissolve
pause 3
zn "M-Master...~"
mc "Yes~?"
zn "Use me~!"
mc "I don't need you to tell me that."
zn "Mnh~!"
scene zenpress with dissolve
pause 2
zn "Ahh~!"
mc "{i}God— She's so tight!"
scene zenpress with dissolve
pause 1.7
zn "Ngh~! M-Master I-I'm...!"
scene zenpress with hpunch
mc "Came already? Too bad, I still haven't cum."
zn "Y-Yes! K-Keep going~!"
scene zenpress with dissolve
pause 4
zn "Mnh~"
mc "You're so tight--"
mc "I-I'm almost there..."
scene zenpress with dissolve
pause 0.7
mc "I'm cumming!"
zn "M-Me too~!"
scene zenpress with flash
pause 0.2
scene zenpress with flash
pause 0.1
scene zenpress with flash
pause 0.1
scene zenpress with flash
pause 0.05
scene zenpress with flash
pause 0.05
scene znsexanimecum with flash
pause 3
mc "Ahh... That was marvelous..."
zn "Y-Yes..."
return


label zAnal:
hide screen hud
mc @talk "Alright, get on the ground. Now"
znr @talk "Yes, master."
"She gets on all fours on the ground. After the first time she knows what this is for. She takes off her clothes and eagerly shakes her ass."
scene znanalbase with fade
zn "C'mon master, take me~"
scene znanalbasemc with dissolve
mc "I will."
show znanalanim with vpunch
"You slip your manhood inside of her ass, immediately starting to thrust."
zn "OH GOD~! YES!"
"You can feel her shiver with pleasure with each thrust, her lewd pants and, every once in a while, you hear her let out a satisfied giggle."
scene znanalanim with vpunch
zn "Fuck... me... Harder~!"
mc "{i}Look at her... My own personal toy."
zn "Mess my insides master~!"
scene znanalanim with hpunch
zn "OH~!"
scene znanalanim with hpunch
zn "AHN~!"
mc "{i}Mhh... I'm going to cum..."
scene znanalanim with hpunch
zn "Use me~!"
mc "{i}I'm... so close..."
menu:
    "Cum outside":
        scene znanalanim with vpunch
        zn "I'M-"
        mc "-Cumming!"
        scene znanalanim with flash
        pause 0.2
        scene znanalanim with flash
        pause 0.1
        scene znanalanim with flash
        pause 0.1
        scene znanalanim with flash
        pause 0.05
        scene znanalbasemc with flash
        pause 0.05
        scene znanalcumout with flash
        pause 2
        mc "Ah..."
        pause 1
    "Cum inside":
        scene znanalanim with vpunch
        zn "I'M-"
        mc "-Cumming!"
        scene znanalanim with flash
        pause 0.2
        scene znanalanim with flash
        pause 0.1
        scene znanalanim with flash
        pause 0.1
        scene znanalanim with flash
        pause 0.05
        scene znanalanim with flash
        pause 0.05
        scene znanalanimcum with flash
        pause 2
        scene znanalcumin with dissolve
        mc "Ah..."
        pause 1
mc "You're so fucking tight, you know?"
zn "I-I always am for my master~"
mc "Hah, what a fucking slut."
return



label zSpanking:
hide screen hud
mc @talk "You know, I haven't liked the way you've behaved recently... I haven't punished you enough."
znr @angryt "W-What?"
mc @talk "Get on the wall. Naked."
zn "..."
"Zenelith strips down, you can almost sense her shame as she approaches the wall"
scene zenspankpre1 with fade
pause 1.5
zn "P-Please be gentle..."
mc "It wouldn't be a punishment if I were."
zn "..."
scene zenspanking with hpunch
pause 0.4
scene zenspank1
zn "Ngh!"
mc "This is what you get!"
scene zenspanking with hpunch
pause 0.4
scene zenspank2
mc "For being a naughty little slut!"
scene zenspanking with hpunch
pause 0.4
scene zenspank3
mc "That doesn't know her place!"
scene zenspanking with hpunch
pause 0.4
scene zenspank4
zn "I-I'm sorry... M-Master, please stop..."
scene zenspanking with hpunch
pause 0.4
scene zenspank5
mc "Not yet."
scene zenspanking with hpunch
pause 0.3
scene zenspank5
pause 0.1
scene zenspanking with hpunch
pause 0.3
scene zenspank5
pause 0.1
scene zenspanking with hpunch
pause 0.4
scene zenspank6
zn "Ahn..."
mc "...A moan? Tsk. I really hope it was for the pain and not something else. We're done for today."
show screen hud
return



label ItsFoodOrNothing:
scene shackinteriors
show prot normal
mc "Now then..."
menu:
    "Give her the food":
        mc @talk "Here's the food. You did a good job today."
        zn "T-Thanks master..."
        $ submission += 1
        $ lastAte = 0
    "Don't give her food":
        mc @talk "You know... I've changed idea."
        zn "...?"
        mc @smilet "I don't feel like feeding you right now, sorry."
        zn "W-What?"
        mc @talk "Sorry, toy. Live with it."
        mc @smirkt "Though I do have to say: your performance when food motivates it is a lot better than when it doesn't."
        zn "..."
        $ degradation += 1
$ time += 1
if time > 3:
    mc "{i}It's late... Let's go home for now."
    jump home
jump zenMenuC





label zBathing:
scene zenelithshack with fade
"The two of you get out of the house and you take Zenelith to the lake. Her eyes sparkle when she sees the water, but as soon as she remembers she needs to undress in front of you she sulks."
mc "Have a nice bath."
zn "..."
"Zenelith strips and gets into the water."
scene znbath1
menu:
    "Say nothing":
        "Zenelith washes herself thoroughly and, when she's done, she gets out of the water. You order her to wait until she's dry before putting back her clothes. At first, she wants to protest, but seems to decide not to."
        "Then when she's finally dry and dressed again you decide to go back."
        $ addiction += 1
    "Degrade her":
        mc "I love it when you willingly undress for me."
        scene znbath2
        zn "..."
        mc "If I ever decide to sell you, that will definitely be a selling point."
        zn "..."
        mc "\"An elf made for sex\", \"She'll obey all your orders\", that kind of thing, y'know?"
        zn "..."
        "Zenelith finishes bathing in silence. When she gets out you tell her to wait before dressing up again since she's all wet. You ogle at her body the entire wait."
        "Then when she's finally dry and dressed again you decide to go back."
$ time += 1
if time > 3:
    "You take Zenelith back to the shack, then you realize how late it already is."
    mc "{i}Oh god, better get home before it's dark."
    jump home
jump zenMenuC
