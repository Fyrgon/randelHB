default zenPlay2 = False
default zenFuckDone = False
default zenBlush = 0
default zenAdventuring = False
default zenSexDone = False

label zenTalk:
if zenrel < 0 and zenPlay2 == True:
    zn "..."
    mc "Zen?"
    zn "I don't want to hear anything from you. Leave."
    mc "What?"
    zn "You just used me to satisfy your needs. I believed you when you said you'd stop and I hoped you would at some point... But you didn't. So, leave."
    mc "Tsk. Whatever you want."
    "As you leave, Zenelith looks down. For a moment you think you saw a tear but you don't think much of it."
    mc "{i}Guess I'm not welcome here anymore then."
    $ zenRouteEnd == True
    jump home
play music happy
"You go inside the cabin and find Zenelith there."
scene shackinteriorbase
show shacktable
show zndress smile
show prot smile
if zenFuckDone == True:
    jump postsexzen
$ zenrel += 10
#if zenrel > 140:
#    jump zenelith6
mc @smilet "Hey there, Zen."
znd @smilet "Oh, hey, [mc]. How are you?"
mc @smilet "I'm doing fine, how about you?"
znd @smilet "I'm good. I've just finished taking care of the garden. As a matter of fact, would you like something to eat?"
menu:
    "Yes":
        mc @smilet "Sure."
        znd @smilet "Let me get you something done then."
        $ roll3 = renpy.random.randint(1, 3)
        if roll3 == 1:
            "Zenelith leaves and comes back with some pears."
            znd @smilet "Here, they're really sweet."
            mc @smilet "Of course, they are."
            znd @blusht "Yeah."
            "You take a pear and begin eating it."
        if roll3 == 2:
            "Zenelith goes outside and returns with some grapes."
            mc @smilet "You've got grapes in the garden?"
            znd @smilet "I've got everything I like there... Well, except you."
            show zndress blush
            mc @smirkt "That was a bad one."
            znd @blusht "Sorry, sorry."
            "She takes a glass and uses magic to make you some grape juice."
            show zndress smile
            show prot smile
            mc @questiont "Grape juice... Are you able to make wine?"
            znd @smilet "That would require a bit more mana."
            mc @smilet "I see."
            "You take your glass and begin drinking."
        if roll3 == 3:
            "Zenelith goes outside and returns with some fruits, she smiles as she takes a loaf of bread and once again prepares some bread with jam."
            znd @smilet "I hope it's not too sweet."
            "You give it a bite and to your surprise the jam is just as sweet as you like it."
            mc @smilet "It's perfect."
            znd @smilet "I'm glad."
            "You keep eating as the two of you talk some more."
    "No, thanks":
        mc @smilet "No, thanks."
        znd @smilet "Alright then."
"The two of you talk for a while. When the sun is almost down, you tell Zenelith you need to go and you say goodbye to each other."
jump home

label postsexzen:
mc @smilet "Hey there, Zen"
znd @smilet "Oh, hey, [mc]."
"The two of you chit chat for a while. When the sun is almost down, you tell Zenelith you need to go and you say goodbye to each other."
jump home

label zenSexing:
hide screen hud
stop music fadeout 1
mc "Hey, Zen~"
if zenrel < 0:
    if zenPlay2 == True:
        zn "..."
        mc "Zen?"
        zn "I don't want to hear anything from you. Leave."
        mc "What?"
        zn "You just used me to satisfy your needs. I believed you when you said you'd stop and I hoped you would at some point... But you didn't. So, leave."
        mc "Tsk. Whatever you want."
        "As you leave, Zenelith looks down. For a moment you think you saw a tear but you don't think much of it."
        mc "{i}Guess I'm not welcome here anymore then."
        $ zenRouteEnd == True
        jump home
    zn "No."
    mc "Huh?"
    zn "I'm not your plaything, [mc]. When you make love to me you need to... make love to me."
    mc "..."
    zn "So? Nothing to say?"
    mc "I'm sorry, I didn't know it made you feel so bad."
    zn "Do you promise me you won't treat me like that anymore?"
    $ zenrel = 50
    $ zenBlush = 0
    menu:
        "Yes (lie)":
            $ zenPlay2 == True
            mc "Yes, I promise."
            zn "Sigh... You're forgiven."
            pause 1
            zn "Now come here..."
            "Zenelith kisses you and the two of you slowly make your way into the house."
            mc "{i}Let's be nice just this once so she'll let me keep fucking her..."
            "The two of you begin to undress each other as you kiss. You feel her body with your hands as she hugs you tightly, then you slowly move to the bed."
            mc "I love you."
            zn "I love you too, [mc]."
            jump zenSex2L
        "Yes (truth)":
            $ zenPlay == False
            $ zenFuck == True
            mc "I promise, I'm sorry."
            zn "You're forgiven."
            pause 1
            zn "Now come here..."
            "Zenelith kisses you and the two of you slowly make your way into the house."
            "The two of you begin to undress each other as you kiss. You feel her body with your hands as she hugs you tightly, then you slowly move to the bed."
            mc "I love you."
            zn "I love you too, [mc]."
            jump zenSex2L
zn "Oh, hey, [mc]!"
if zenBlush < 3:
    "You give Zenelith a kiss and she blushes."
    zn "U-Uhm..."
elif zenBlush > 3 and zenPlay == True:
    "You kiss Zenelith but she doesn't return the kiss, she seems to be a bit sour."
elif zenBlush > 3 and zenBlush < 6:
    "You give Zenelith a kiss and she kisses you back."
    zn "Oh?"
else:
    "Zenelith kisses you and smile."
    zn "I think I know what you want, you naughty boy~"
    jump zenSex1
if zenFuck == True:
    mc "I've been holding off too long, let's get in."
if zenLove == True:
    mc "Zen, I can't resist you..."
    zn "My, you're so eager... Fine, let's go inside~"
label zenSex1:
"You go inside the shack, a smile on your face."
if zenLove == True:
    $ zenrel += 10
    "The two of you begin to undress each other as you kiss. You feel her body with your hands as she hugs you tightly, then you slowly move to the bed."
    mc "I love you."
    zn "I love you too, [mc]."
elif zenBlush > 5:
    "Zenelith seems to want you more than you want her. She quickly begins to strip you and pushes down on the bed, then she gets naked."
    "She tries to get on top of you but you smirk and push her over to the side."
    mc "Getting cocky, huh? How about you take my cock instead?"
    jump zenSex2
elif zenPlay == True:
    $ zenrel -= 20
    "You undress her and push her over on the bed, almost throwing her. She gives you a disapproving look but you don't care about it. She only has you, whatever you do to her she won't mind."
    "You get naked and get on the bed. She hesitantly opens her legs and you smile. Then you thrust inside of her."
elif zenFuck == True:
    "You quickly undress her. She's already wet so there's no need for foreplay. You push her on the bed, she looks at you eagerly. When you take out your cock, her expression melts."
    mc "Turn over."
    "She obediently turns around, then you go down on her."


label zenSex2:
$ zenBlush += 1
if zenFuck == True:
    jump zenSex2F
if zenLove == True:
    jump zenSex2L
if zenPlay == True:
    jump zenSex2P


label zenSex2P:
scene zenelith movie with fade
pause 2
zn "God...!"
scene zenelith movie with vpunch
pause 1
zn "[mc]... Y-You're too-"
scene zenelith movie with vpunch
pause 1
zn "T-Too rough~!"
scene zenelith movie with vpunch
pause 1.5
mc "You know you like it~"
zn "Y-Yes! I l-like it!"
scene zenelith movie with vpunch
pause 1
mc "Take my cock, you slut...!"
scene zenelith movie with vpunch
zn "Ngh~!"
scene zenelith movie with vpunch
zn "Gh-!"
scene zenelith movie with vpunch
zn "Yes!"
scene zenelith movie with vpunch
mc "I'm gonna fill you up!"
scene zenelith movie with vpunch
zn "Mh...!"
scene zenelith movie with vpunch
mc "Th-There!"
scene zenelith movie with flash
zn "Aahn~!"
scene zenelithsexrani
show zenelithsexc1 with vpunch
pause 0.2
show zenelithsexc2 with flash
pause 0.2
show zenelithsexc3 with flash
pause 0.4
show zenelithsexc4 with dissolve
pause 1
show zenelithsexc6 with dissolve
zn "..."
mc "That was great."
zn "You're too rough."
mc "But you like it."
zn "..."
"She doesn't say anything else and when you try to touch her again, she gets up and dresses up."
mc "{i}Can't even take a good fuck, tsk."
"You follow her example and dress up as well, ogling at her body until she's done. She makes a grimace and leaves the house."
$ zenSexDone = True
jump zenShack


label zenSex2F:
scene zenelith movie with fade
pause 2
zn "Ngh...!"
scene zenelith movie with dissolve
pause 1
mc "Zen, you're so hot..."
scene zenelith movie with dissolve
pause 1
zn "You're so rough~!"
scene zenelith movie with dissolve
pause 1.5
zn "[mc]~! Keep going!"
mc "Mh~"
scene zenelith movie with vpunch
pause 0.1
zn "Oh yes...!"
scene zenelith movie with vpunch
zn "Yes~!"
scene zenelith movie with vpunch
zn "Yes!!"
scene zenelith movie with vpunch
zn "YES~!"
scene zenelith movie with vpunch
mc "Zen...!"
scene zenelith movie with vpunch
zn "Fill me...!"
scene zenelith movie with vpunch
mc "I'm-"
scene zenelith movie with flash
zn "C-Cumming~!"
scene zenelithsexrani
show zenelithsexc1 with vpunch
pause 0.2
show zenelithsexc2 with flash
pause 0.2
show zenelithsexc3 with flash
pause 0.4
show zenelithsexc4 with dissolve
zn "You're so rough..."
show zenelithsexc7 with dissolve
mc "You know you like it."
zn "You're right."
mc "Heh."
zn "Come back whenever you want."
mc "That's what I already do."
"She kisses you one more time and then you two dress up again."
$ zenSexDone = True
jump zenShack

label zenSex2L:
scene zenelith movie with fade
pause 2
zn "[mc]...!"
scene zenelith movie with dissolve
pause 1
mc "Zen..."
scene zenelith movie with dissolve
pause 1
zn "Keep going~!"
scene zenelith movie with dissolve
pause 1.5
zn "Ngh~! I love you!"
mc "Mh~"
scene zenelith movie with dissolve
pause 1
zn "Deeper...!"
scene zenelith movie with vpunch
zn "Yes~!"
scene zenelith movie with vpunch
zn "Yes!!"
scene zenelith movie with vpunch
zn "YES~!"
scene zenelith movie with vpunch
mc "Zen-! I'm gonna...!"
scene zenelith movie with vpunch
zn "C-Cum inside of me...!"
scene zenelith movie with vpunch
mc "I'm-"
scene zenelith movie with flash
zn "Ahn~!"
scene zenelithsexrani
show zenelithsexc1 with vpunch
pause 0.2
show zenelithsexc2 with flash
pause 0.2
show zenelithsexc3 with flash
pause 0.4
show zenelithsexc4 with dissolve
zn "That was amazing..."
mc "Yeah..."
zn "I can feel your seed inside of me, eheh..."
show zenelithsexc7 with dissolve
mc "Eheh..."
zn "I love you."
mc "I love you too."
zn "Come back whenever you want."
mc "That's what I already do~"
"You kiss each other for a while and then dress up again."
$ zenSexDone = True
jump zenShack
