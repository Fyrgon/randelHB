default zenQ = 0
default mattressDebt = 0
default foodDebt = 0
default marketDebt = mattressDebt+foodDebt
default dayZ = 0
default toolz = False
default humanHate = False
default furnitureZ = False
default Zdress = False
default zenPeek = False
default zenNoticed = False
default lookgreatz = False
default fitsperfectly = False
default lookgorgeusz = False
default looksgreat = False
default zenPlay = False
default zenFuck = False
default zenLove = False
default zen_love_day = 0


label ZenelithWholesome:
$ evil -= 1
$ good += 1
$ zenBegun = True
show zenelithdown2
mc "Here, get up."
zn "...Huh?"
mc "C'mon, grab my hand before I change idea."
zn "Wh-Why? Don't want to get your hands dirty with the blood of an elf?"
mc "No, you have barely anything on and you probably haven't eaten in a while... Your magic is so weak you couldn't even scratch me."
mc "You seem in need of help, and I'd like to offer it to you."
mc "...Unless you'd prefer me killing you."
if RapeZen == True:
    znr "Maybe I would..."
    scene zenelithhelp
    znr "...Fine."
    mc "See? I knew you-"
    play music horror
    show forrestn with vpunch
    "Zenelith leaps on top of you, she's got something in her hand."
    scene znmcsmash with vpunch
    play sound skullsmash
    "You don't have time to react, nor to scream, that you are laying on the floor. Your life slowly going away."
    scene znmcsmash with vpunch
    play sound skullsmash2
    znr "One thing is..."
    scene znmcsmash with vpunch
    play sound skullsmash3
    znr "..To get beaten by an ape..."
    scene znmcsmash with vpunch
    play sound skullsmash
    znr "Another is to be dishonored to such an extent..."
    scene znmcsmash with vpunch
    play sound skullsmash3
    znr "By one of your kind..."
    scene znmcsmash with vpunch
    play sound skullsmash2
    znr"You repulsive scum..."
    scene black with vpunch
    play sound skullsmash4
    $ persistent.zenMurders = True
    show text "{color=#fff}Tip: Don't expect someone to forgive how you raped them." at truecenter with dissolve
    pause 3
    hide text
    jump GameOver
"Zenelith looks at you in anger, but slowly, she extends her hand."
scene zenelithhelp
znr "Don't think I trust you, ape."
mc "Alright."
"You pull Zenelith up and she almost falls again, but she manages to stay upright."
show forrestn
show znrag
show znrag angry
show normalmc
"She immediately distances herself from you, keeping a few feet of distance between you and her"
"You take a piece of wood and light it using Zenelith's campfire, then you start walking."
mc "Let's go find a better place to rest until morning."
znr "..."
"She reluctantly starts following you."
scene forrestn
mc "{i}The problem now is... Where do I take her?"
mc "{i}I can't just take her to Randel... Eve is there and so is Sander..."
if thealive == True:
    mc "{i}And I've already got Thea at home..."
mc "{i}Obviously the Elf Village isn't an option..."
mc "{i}...Aerin would kill her on sight."
mc "{i}Ugh! Why is helping so hard?!"
mc "{i}...Oh wait, it's because she's wanted."
"The two of you walk for what seems an eternity before Zenelith speaks up."
zn "I'm not sure why I'm trusting you."
mc "And I'm not sure why I'm helping you."
zn "..."
zn "How can I know you're not just taking me somewhere to kill me?"
mc "Wow, is that the idea you got of me?"
zn "That's the idea I got of you apes. Miserable, unreliable, yet full of themselves."
mc "I guess you got some of that right."
zn "Tsk."
mc "But maybe for now you could try to tone down your hatred so I get more motivated to help you out."
zn "As if I'd need your help."
mc "You don't have to pretend living in the forest is fun. Your clothes already say enough."
"Zenelith suddenly covers herself with her own hands."
zn "How dare you...!"
mc "Don't make a scene now, I'm talking about how shabby they look."
zn "It's your fault I lost my robe..."
mc "If I remember correctly you attacked me and your own spell ended up destroying your clothes, I'm not too sure that was entirely my fault."
zn "..."
mc "Wait, I think I see something..."
scene zenelithshackn with fade
mc "{i}What the-?"
znr "...Is this where you were taking me?"
mc "Uhhh... Yes, of course."
mc "{i}...Has this been here all along? How did I never see this place before?"
znr "..."
mc "Yeah, uhm... Let's go inside."
scene shackinteriorbasedirtyn with fade
show prot normal
show znrag
mc @ smilet "Oh hey, there's a patch of hay to sleep in."
znr angry "Tsk."
mc @ questiont "What?"
znr @ angryt "You expect me to degrade myself like that?"
mc @ questiont "...By sleeping on hay instead of a patch of grass in the forest?"
znr angry "...Hmpf."
mc @ talk "I'm not going to sleep there with you tonight if that's what you were thinking about. I'll sleep outside."
znr @ angryt "I don't know why accepted to come along with you, ape."
mc @ talk "Because the other option was death."
znr "..."
show prot sad
mc @ talk "Sigh... Listen, you know very well I am not getting anything out of helping you."
mc @ talk "I'm friends with both Aerin and Eve, the fact that I'm helping you is striking to me as well."
mc @ talk "But you're still a person and I'm trying to help you, because maybe there is still some good in you."
if millyInfo == True:
    mc @ hopet "Afterall, before everything happened, Milly said you weren't a bad person, and I'd like to believe her."
mc @ talk "This house, regardless of how rundown it is, is a house. There's no other place in which you'd be safe. In Randel there's people who don't like you and obviously you can't go back to your village any time soon."
znr "..."
"For a brief second her expression of contempt disappears, but you don't have time to decipher her new expression that she goes back to normal."
show znrag angry
znr @ angryt "Fine, I can't expect much more from an ape."
show prot angry
mc @ angryt "I'm not an ape. I'm a human, and my name is [mc]"
znr @ angryt "I will not stain my mouth with your monkey name... Be grateful I'm speaking your tongue."
show prot sad
mc "{i}Let's just hope she'll get better with time."
hide prot sad
show prot normal
mc @ talk "Let's just go to sleep."
mc @ talk "Goodnight."
hide prot normal with easeoutright
"You start making your way outside."
znr @ angryt "What makes you believe I won't kill you in your sleep?"
mc "The most you could get from killing me is some \"ape\" meat which I don't think is really that tasty."
"You walk out of the house."
scene zenelithshackn with fade
"You use your camping gear and set up a tent for yourself, then you finally fall asleep."
stop music fadeout 1
scene black with fade
pause 2
play music forest
scene zenelithshack with dissolve
pause 2
"The next day you wake up early and still alive. Apparently she agreed on the uselessness of killing you."
"You decide to go inside the house to check on her."
scene znsleep
"She's still sleeping, a faint smile on her face... She looks nice for once."
mc "{i}Really wish she were like that when awake as well."
scene forrest
"You then decide to leave for Randel. Despite what you had said, she wasn't totally wrong. That house is so run down that it makes little difference whether you sleep inside of it or outside."
mc "{i}First things first, I'll get her a bed and bring her some food for the day, then tomorrow we'll start cleaning that whole place up."
scene villageback with fade
mc "{i}Alright, time to buy a mattress."
"You wander around the market for some time, you haven't really ever went shopping for beds or bedding before in your life."
"After a few minutes you find someone selling a few mattresses, you go to buy one, but then you stop."
mc "{i}Wait, how am I going to take a mattress all the way through the forest?"
mc "{i}I can't just carry it over my shoulder the whole way through..."
mc "{i}I could use a mule, but... I don't have one, they're expensive, and I'm not going to buy one just for this."
stop music fadeout 2
mc "{i}Maybe Scarlet knows a spell that could be useful for this! Maybe there's a spell that can make stuff smaller or something..."
play music academy fadein 1
scene lecturemage2 with fade
"You decide to go to the academy and there you find Scarlet. She's almost done with her class so you wait outside."
pause 1
scene lecturemage1 with fade
stop music fadeout 3
"Once the class is done you walk in."
show normalm
show prot normal
mc "Hey Scarlet."
s "Hey, [mc], what's up?"
mc "Is there any spell that can make objects smaller?"
s "Not any useful for whatever you want to use it for."
mc "Wha- How can you know that?"
s "The only one I know of requires an immense amount of energy and also doesn't allow you to move the object that has been made smaller, its uses are very reduced."
mc "Damn it..."
s "Why you ask?"
mc "Uhm..."
menu:
    "Lie":
        mc "I, uhm, wanted to take more equipment with me while adventuring, and-"
        s "[mc]."
        mc "Y-Yes?"
        s "Has anyone ever told you that you're bad at lying?"
        mc "...Sigh."
        s "C'mon, what do you needed that for?"
        mc "I need to take a mattress in the middle of the forest."
        s "Oh~ For what?"
        mc "..."
        s "Alright, alright, pretend I didn't ask."
        mc "Well thanks anyways."
        s "Wait, who said I couldn't help you with that?"
        mc "Huh?"
        s "There's a spell that can make objects lighter, it's not the same but it would still be useful, wouldn't it?"
        mc "Oh, yeah! Definitely!"
        s "Alright then, let me teach it to you."
        scene black with fade
        show text "{color=#fff}Scarlet teaches you the spell." at truecenter
        pause 1
        scene lecturemage1 with fade
        hide text
        mc "Thanks a lot, Scarlet!"
        s "No problem."
    "Tell her only about the mattress":
        mc "Well, I want to buy a mattress but carrying it all the way from the market is a bit annoying."
        s "A new mattress?"
        mc "Yeah."
        s "Well, there might still be a way for me to help you."
        mc "Really? How?"
        s "There's a spell that can make objects lighter, it's not the same but it would still be useful, wouldn't it?"
        mc "Oh, yeah! Definitely!"
        s "Alright then, let me teach it to you."
        scene black with fade
        show text "{color=#fff}Scarlet teaches you the spell." at truecenter
        pause 1
        scene lecturemage1 with fade
        hide text
        mc "Thanks a lot, Scarlet!"
        s "No problem."
    "Tell her the truth":
        mc "Sigh... Listen, don't tell this to anybody, alright?"
        s "Oh? Yeah, sure."
        mc "Alright."
        mc "You see, there's this elf priestess who did some bad stuff. She got what she deserved and has been trying to survive by herself in the forest since."
        mc "I found her and despite knowing what she has done I... I don't know, I decided to help her."
        mc "We found a shack in the woods and we decided she'd stay there, but it only had rubble in it, not even a bed to sleep in..."
        mc "So I wanted to buy a mattress for her to sleep in, but carrying through the entire forest would be hard by myself..."
        s "Oh, wow."
        s "Well, that's a lot of information. You didn't have to to tell me all of that."
        s "...But I getcha."
        s "There's a spell that can make objects lighter, it's not the same but it'd still be useful, would it?"
        mc "Oh yeah, definitely."
        s "Alright then, let me teach it to you."
        scene black with fade
        show text "{color=#fff}Scarlet teaches you the spell." at truecenter
        pause 1
        scene lecturemage1 with fade
        hide text
        mc "Thanks a lot, Scarlet!"
        s "No problem."
stop music fadeout 1
scene villageback
play music tavern
"You leave and go buy the mattress, you use the spell to make it lighter and then you decide to roll it and tie it so that it's easier to carry."
if money < 20:
    $ mattressDebt = 20-money
    $ money = 0
    "You didn't have enough money, but you promise you will be back and pay for it later."
    "Somehow you convince them."
else:
    $ money -= 20
    "You pay the man the money for the mattress, then you use the spell on it to bring it along."
mc "{i}Oh, I almost forgot! I need to bring her some food too."
if money < 5:
    mc "{i}...But I'm out of money."
    mc "{i}Well, I'll just use my incredible charisma to convince people to give me stuff for free."
    "You look around and end up buying a few vegetables."
    mc "{i}I'll pay it all back I swear!"
    $ foodDebt = 5-money
    $ money = 0
    mc "{i}Damn it, I didn't have enough money..."
    mc "{i}But they said it's fine if I pay it back next time I come here."
else:
    $ money -= 5
    "You look around and end up buying a few vegetables."
$ marketDebt = mattressDebt+foodDebt
stop music fadeout 1
"Satisfied with what you got, you head to the forest."
scene forrest with fade
play music forest
"You walk slowly, trying your best to not get lost."
"Your efforts are repaid when you finally spot the cabin in the distance."
scene zenelithshack with fade
"Zenelith is standing outside as if she were waiting for you."
show znrag angry
show prot normal
znr @angryt "Oh, there you are, ape. I hoped you wouldn't come b-"
mc @angryt "I'm happy to see you too, Zenelith."
show znrag normal
znr @talk "...What's that on your shoulders?"
mc @talk "A mattress. You don't want to keep sleeping on hay, right?"
znr @talk "Correct."
mc "{i}Guess she isn't going to say thanks."
mc "{i}Maybe I {b}am{/b} expecting too much of her..."
stop music fadeout 2
mc @talk "Well, let's go inside."
scene shackinteriorbasedirty
play music lake
"Once inside, you untie the mattress and look for a spot to place it in."
"After moving some rubble, you decide to put it next to the wall."
show shackinteriorbed with dissolve
show znrag normal
show prot normal
mc @talk "There we go."
"Zenelith gets next to it and touches it lightly to check how soft the mattress is. She seems satisfied, or at least you think so."
znr @talk "Are you going to stay longer?"
mc @talk "Yes, I've also bought you something to eat."
"You take out from your bag the vegetables you got at the market, you hadn't noticed before but they look really good."
play sound stomach
show znrag angry
"...Or maybe you're just hungry. Zenelith glares at you."
mc "{i}Right, I haven't eaten for a whole day..."
menu:
    "Stay and eat with her":
        "You sit down on the floor and put your bag in front of you, then you look at Zenelith."
        mc @talk "C'mon, let's eat."
        znr @angryt "I'm not eating on the floor with an ape."
        mc @talk "You ate on the floor with ants for however-long you've been in the woods, I think you can make this sacrifice-"
        play sound stomach
        pause 1
        mc "{i}...Wait, that wasn't me."
        show znrag angryb
        "You look up and Zenelith turns her head away, yet you can still see that her face is red."
        show prot smile
        mc @smilet "C'mon, we're both hungry, let's just eat."
        "She groans, but she still ends up sitting down, doing her best to not look at you."
        show znrag angry
        "She grabs some food and you do as well. The two of you start eating."
        znr @talk "I don't understand you."
        mc @talk "I know, I'm a really mysterious guy."
        znr @angryt "Just shut up, ape."
        mc @talk "{i}Alright maybe I shouldn't act so full of myself."
        menu:
            "Have you always hated humans this much?":
                label humanHate:
                $ humanHate = True
                mc @talk "Have you always hated humans this much?"
                znr @angryt "Yes."
                if millyInfo == True or nessaInfo == True:
                    mc @talk "Even before the war?"
                    znr "..."
                    mc @questiont "You know, it was caused by an elf. But most people don't hate elves because of that."
                    znr "..."
                mc @talk "Did you ever see a human besides me?"
                znr @angryt"Yes."
                mc @talk "When?"
                znr @angryt"When you arrived to the village, there was another ape with you."
                mc "{i}Oh right, Sander. He doesn't really give the best impression of the human race..."
                mc @talk "His name is Sander, he might not have great manners, but he has been Eve's adventuring partner for years, do you really think she'd be friends with a bad person?"
                znr "She has been wandering among you apes too long, her judgement has been clouded from her time away from our village-"
                mc @angryt "We both know that's not true."
                znr @angryt"Tch, what would an ape know?"
                mc @angryt "What would an elf that enslaves other elves from her own tribe know?"
                show prot sad
                mc "{i}That came out more aggressive than I wanted it to..."
                znr @angryt"..."
                mc @talk "Sorry, didn't mean to come out like that."
                znr @talk "No, what you said is right."
                mc @talk "Huh?"
                "Zenelith gets up and turns around."
                znr @talk "You can go now."
                mc @talk "What?"
                znr @angryt "Are you deaf, ape? I told you to leave."
                mc @talk "The hell?"
                show prot surprised
                "You hear her whisper, then you see a light starting to appear in her hand."
                mc @angryt "Alright, alright! I'm leaving."
                scene zenelithshack
                mc "{i}What the hell was that? Was she going to attack me? The hell's wrong with her?."
                mc "{i}Whatever. I'm going home."
                scene forrest
                menu:
                    "Don't come back":
                        $ zenRouteEnd = True
                        mc "{i}Yeah, screw her. If she wants to treat me like this then I'm not coming back. Let's see how well she does without me."
                    "Keep trying":
                        mc "{i}...It's stronger than me."
                        mc "{i}I still feel like she is a good person underneath all that."
            "You should be nicer to the person who's helping you":
                label nicer2MC:
                mc @talk "You know, you could at least stop calling me ape now that I'm helping you."
                znr @talk "I won't."
                mc @talk "Or you could even say \"Thank you\" and stuff."
                znr @angryt "I don't intend to do that, ape."
                mc "{i}Well, that went well."
                #"The two of you eat in silence until you're both finished. You grab your bad and decide to leave."
                #mc @talk "I'm going now, see you tomorrow."
                #znr @talk "Amawa akti..."
                #mc @talk "What?"
                #znr @angryt "Goodbye."
                #scene zenelithshack
                menu:
                    "Have you always hated humans this much?":
                        jump humanHate
            "Is it good?":
                mc @talk "So... How's the food?"
                znr @talk "Decent."
                mc @talk "...I'm happy to hear that."
                znr @angryt "For ape food, that is."
                mc "{i}Oh."
                menu:
                    "You could try to be nicer to the person who's helping you":
                        jump nicer2MC
                    "Have you always hated humans this much?":
                        jump humanHate
    "Grab something to eat and leave":
        mc "Alright, see you."
        "You grab an apple and walk towards the door."
        znr "Wait."
        mc "What?"
        znr "...Nothing."
        mc "...Alright. Bye."
        "You leave and go back home."
mc "{i}Tomorrow I'll clean the whole place up... Maybe I could ask Uncle Pete to give me some tools so I can repair everything that's broken too."
$ zenQ = 1
$ persistent.zenIntro = True
$ day += 1
$ time += 2
jump home



label zenelith2:
hide screen hud
play music lake
mc "{i}Alright, let's go in."
scene shackinteriorbasedirty
show shackinteriorbed
show prot normal
show znrag normal
mc @talk "Zenelith?"
znr @talk "Oh, you're back."
mc @talk "Yes, I've brought some tools so we can get started with the reparis."
znr @angryt "We?"
mc @smilet "Yes, I'm helping you."
znr @angryt "I didn't-"
"You hand Zenelith a broom, interrupting her mid sentence."
mc @talk "Let's get to work."
znr @angryt "You really are annoying."
mc @talk "Thanks, I try my best."
znr @angryt "It wasn't a compliment."
mc @smirkt "I know."
znr "Grr..."
mc @smilet "Shall we get started?"
znr @angryt  "...Fine."
"You put the toolbox on the ground and take out a hammer and a few nails and the two of you get to work."
scene shackbuild with dissolve
"It's a tiring job, and it's definitely taking a lot of time. If you had been doing it with anyone else it'd have still been a really fun time, but Zenelith... She's not the best talker."
mc "{i}At least she hasn't called me ape yet today."
if humanHate == True:
    scene shackbuild2 with dissolve
    play music nurture fadein 5
    zn "Human."
    mc "{i}Oh, wow."
    mc  "Yes?"
    zn "I'm sorry."
    mc "You're sorry?"
    zn "Yes."
    mc "For what?"
    mc "{i}I should probably ask \"For what in particular\", but..."
    zn "..."
    zn "For yesterday, I should've not thrown you out."
    mc "Oh."
    zn "You called me out and I got angry, but you are right."
    zn "How can I say anything about Evelyn? I know her judgment hasn't become clouded, she still acts the same way she did before her mother's death. She almost hasn't changed at all."
    zn "But I did change over time and not into something better."
    zn "What I did is unforgivable, I always knew it, yet it didn't stop me. I..."
    zn "I don't know why I'm telling you this, I'm too late to do anything anyways."
    mc "{i}Wow, that's... That's new."
    menu:
        "I forgive you":
            mc @smilet "Well, I forgive you."
            znr "..."
            znr @talk "Thanks, [mc]."
            mc @smirkt "Oh, so you do know my name."
            znr @angryt "Shut up."
            stop music fadeout 2
        "You can be a better person":
            mc @talk "Yes, you did something horrible, but that doesn't mean you can't change Zenelith."
            znr "..."
            mc @hopet "I know you can be a better person, and I know you are going to try. It's why I'm giving you this chance: to show the world you're not just the mean priestess, but much more."
            znr @talk "...Thank you, [mc]."
            mc @smilet "It's weird hearing you say my name."
            znr @angryt "Should I go back to ape?"
            mc @smilet "No, I'm good."
            stop music fadeout 2
        "What's done is done":
            mc @talk "What's done is done."
            mc @hopet "You can't change the past, but you can change the present. You're not too old for that."
            mc @smilet "If Zenelith in the past wasn't a good person, make the Zenelith in the present a good person. Maybe that way people will forgive you."
            znr @talk "...If you say so."
            mc @smilet "Maybe they still won't forgive you, but maybe by then you'll have done enough good that they won't care anymore."
            mc @smilet "I believe in you."
            znr @talk "Thanks, [mc]..."
            stop music fadeout 2
            mc "{i}Oh wow, she actually said my name."
scene shackinteriorbase with fade
play music forest
"The two of you work until dawn, not speaking much after that conversation. When you're finished the place is finally looking like a real house, and a cozy one at that."
mc "See? Now it's way better."
zn "It is."
mc "Well, it's gotten late, I'm going to leave. I'm sorry I didn't bring more food, I hope what I brought yesterday was enough."
zn "It wasn't."
mc "Oh."
zn "It wasn't your fault, I don't want to depend so much on you, so I took some of what you brought and made a small garden behind the shack."
mc "Wait, really?"
zn "Yes. With magic I can make the vegetables grow faster than they'd naturally would, you don't have to bring over food anymore."
mc "Oh, alright then."
zn "..."
mc "Bye then."
zn "Bye."
scene zenelithshack
if humanHate == True:
    mc "{i}Today's been a productive day. She not only finally called me by name, but also thanked me... Maybe I {b}am{/b} making progress."
else:
    mc "{i}Welp, next time I come over it'll go even better, I'm sure of it."
mc "{i}That house is still missing a table and some chairs... I'll bring them next time around."
mc "{i}...And maybe I could buy her an actual dress too."
if evil > 2:
    mc "{i}I don't mind the view, but..."
else:
    mc "{i}She can't be going around like that forever."
$ persistent.zenRepaired = True
$ zenQ = 2
$ time += 1
jump home




label zenelith3:
play music lake
"You put down the furniture and the dress in front of the door before going in, noticing the spell wearing out."
if time < 3:
    scene shackinteriorbase
    show prot smile
    show znrag normal
    mc @smilet "Hey."
    znr @talk "Good day, human."
else:
    scene shackinteriorbasen
    show prot smile
    show znrag normal
    mc @smilet "Hey."
    znr @talk "Good evening, human."
if humanHate == True:
    mc "{i}Not my name, but not ape either, I guess it's an improvement."
    mc @smilet "Hey there, Zenelith."
    znr @talk "What is that you brought with you?"
    mc @smilet "They're gifts for you."
    znr @talk "Oh?"
    mc @smilet "Yeah, let me show you what I got you."
else:
    mc @surprisedt "Wow."
    znr @talk "What?"
    mc @smilet "You called me human."
    znr @angryt "Shut up, ape."
    mc @hopet "I'm sorry, I'm sorry, please go back to human."
    znr "..."
    znr @angryt "I see you've got stuff with you."
    mc @smilet "These? They're for you."
    znr @talk "Oh?"
    mc @smilet "Yeah. Here, I'll show you something."
"You go outside and grab the table first. You put it in the middle of the room and then put the chairs on opposite sides, leaving the dress laying next to the window outside."
if time < 3:
    scene shackinteriorbase
    show shacktable with dissolve
else:
    scene shackinteriorbasen
    show shacktablen with dissolve
pause 2
mc "Whatcha think?"
play music happy fadein 5
zn "It looks... like a real house."
mc "Heheh, I know."
"You pat the table a few times as you keep talking."
mc "I choose the nicest table to-"
with vpunch
mc "Owch-"
"You feel a sharp pain on your hand, when you look at it, you see a big splinter stuck halfway inside your finger."
"You quickly take it out, but the wound is big enough that blood starts flowing down from it."
"Then Zenelith grabs your hand."
$ persistent.zenHeal
scene zenelithmcheal2 with dissolve
mc "What the-"
zn "Are you sure you didn't get scammed? To get a splinter like that... It doesn't seem like a great table."
mc "Ha-ha. Really funny."
zn "I'm just being honest."
"The pain left in your finger slowly fades away."
mc "...Wow."
zn "Never seen healing magic before?"
mc "No, never."
zn "Guess you humans don't know everything yet."
mc "You're definitely right."
zn "Do you know how magic works?"
if magiclecture == True:
    mc "Yeah, it needs a catalyst and all that."
    zn "Well, if I still had my staff I could do more magic than this. It would also be a lot less time consuming to take care of the garden I made..."
    mc "I could get you a staff if you want."
    zn "Oh no, there's no need to do that."
    if time < 3:
        scene shackinteriorbase
        show shacktable
    else:
        scene shackinteriorbasen
        show shacktablen
    show zndress smile
    show prot smile
    znr @ smilet "All done."
    mc @ smilet "Thanks, Zen."
    znr @ talk "Don't call me Zen."
    mc @ talk "Lith?"
    znd @ talk "...Zen is better."
else:
    mc "Not really."
    zn "Well, to cast any spell you need a catalyst. For low level spells your body can work just fine, but after that you need to use something external to not injure yoursel."
    mc "I see."
    zn "If I still had my staff I could do more magic than this. It would also be a lot less time consuming to take care of the garden I made..."
    mc "I could get you a staff if you want."
    zn "Oh no, there's no need to do that."
    if time < 3:
        scene shackinteriorbase
        show shacktable
    else:
        scene shackinteriorbasen
        show shacktablen
    show znrag smile
    show prot smile
    znr @ smilet "All done."
    mc @ smilet "Thanks, Zen."
    znr @ talk "Don't call me Zen."
    mc @ talk "Lith?"
    znr @ talk "...Zen is better."
mc @smilet "Well, Zen, I've got something else for you as well."
"You grab the dress and hand it to her with a smile. Her eyes sparkle."
znr @talk "For me?"
mc @smilet  "Of course."
znr @talk "Wow..."
mc @smilet "You can put it on, it's yours."
znr @talk "Alright..."
mc "..."
znr @blusht "...Could you get out?"
mc @smilet "Huh?"
stop music fadeout 4
show prot surprised
mc @surprisedt "Oh! Yes, yes. Just call me when you're done."
if time < 3:
    scene zenelithshack
    play music forest
else:
    scene zenelithshackn
    play music night
mc "{i}Time to wait."
mc "{i}..."
mc "{i}I hope it's the right size..."
mc "{i}..."
mc "{i}She's taking a lot."
mc "{i}...Maybe I could give a peek."
menu:
    "Peek":
        $ zenPeek = True
        $ persistent.zenPeek = True
        mc "{i}Just a little peek..."
        scene znchange1 with fade
        scene znchange2 with dissolve
        mc "{i}Holy Astylla, what a sight to behold..."
        zn "{size=-10}It's such a nice dress..."
        mc "{i}What did she say?"
        "You take your ear closer to the door."
        zn "{size=-5}I can't believe he got it for me... He's such a nice person."
        zn "{size=-5}Maybe we could really be friends..."
        mc "{i}Now I feel bad. I should stop looking."
        menu:
            "keep looking":
                $ zenNoticed = True
                $ persistent.zenPeek2 = True
                scene znchange3 with dissolve
                mc "{i}She took off her bra!"
                zn "{size=-5}...Let's hope it fits."
                mc "{i}I doubt it will..."
                "Suddenly the door creeks."
                if time < 3:
                    scene zenelithshack with vpunch
                else:
                    scene zenelithshackn with vpunch
                "You jump back and hope she didn't see you peeking, your heart is racing."
                zn "Human?"
                mc "Y-YES?"
                zn "You can come in now."
                mc "{i}Thank Astylla she didn't see me.."
            "stop":
                "You turn around and lean on the door with your back."
                if time < 3:
                    scene zenelithshack
                else:
                    scene zenelithshackn
                zn "Human?"
                mc "Yeah?"
                zn "You can come in now."
                mc "Alright."
    "Don't":
        mc "{i}No! I'm not a creep."
        mc "{i}I'll just wait here outside."
        "You wait outside for a couple of minutes."
        znr "Human?"
        mc "Yes?"
        znr "You can come in."
        mc "Alright."
if time < 3:
    scene shackinteriorbase
    show shacktable
else:
    scene shackinteriorbasen
    show shacktablen
"You go inside the cabin again and find Zenelith waiting for you with her dress on."
show zndress blush with dissolve
show prot surprised
znd "..."
show prot smile
mc @ smilet "Wow..."
menu:
    "You look great":
        $ lookgreatz = True
        mc @ smilet "...You look great."
        znd @ blusht "...Thanks."
    "It fits you perfectly":
        $ fitsperfectly = True
        show zndress normal
        mc @ smilet "...It fits you perfectly."
        znd @ talk "It's a bit tight in the back."
        mc @ talk "Oh, c'mon."
        znd @ talk "I'm just being honest."
        show prot smirk
        mc @ smirkt "Want me to return it?"
        show zndress angry
        znd @ angryt "No."
        mc @ smirkt "Exactly."
    "You look gorgeus":
        $ lookgorgeusz = True
        mc @ smilet "...You look gorgeus."
        znd @ blusht "Thank you, [mc]"
        mc @smilet "Nice to hear you say my name like that."
        znd @ blusht "Nice of you that you took care of me."
    "It looks great":
        $ looksgreat = True
        show zndress normal
        mc @ smilet "It looks great."
        znd @ talk "It's weird."
        show prot question
        mc @ smilet "Is it?"
        znd @ talk "I've never worn a human dress before."
        mc @ questiont "Really?"
        znd @ talk "Yeah."
        show prot smile
        show zndress blush
        mc @ smilet "Well, it looks great on you."
        znd @ blusht "Thanks..."
"You look at Zenelith. She seems happy for once. Then you look down at your hand, there's no signs of the injury anymore, you smile."
mc @smilet "Well, it's getting a bit late, I'm going to go home now. It takes a while to get back home."
znd @smilet "Alright, see you."
mc @smilet "Bye bye."
if time < 3:
    scene zenelithshack
else:
    scene zenelithshackn
mc "{i}Today went well."
$ zenQ = 3
$ time += 1
jump home

label zenelith4:
play music lake
"As you get closer to the shack, you begin hearing something."
"The closer you get, the clearer it is that Zenelith is crying."
"You put your hand on the door, should you knock?"
menu:
    "Wait":
        mc "{i}Yeah... I should wait."
        "And you wait for what seems an eternity. Sometimes her crying tones down and for a moment you believe she is going to stop, but she doesn't."
        mc "{i}I can't take this anymore, I need to know what's up."
    "Knock":
        mc "{i}I told myself I'd help her. This is part of that."
play sound doorknock
"You take a deep breath and then you lightly knock on the door. The crying suddenly stops, and then you hear Zenelith getting up. Despite having wiped off her tears, when she opens the door it's clear as day that she has been crying."
show zndress sadc
show prot sad
znd @smilect "Hey..."
mc @sadt "Zenelith, are you ok?"
znd "..."
znd @sadct "...No."
play music reflection_l fadein 2
if time < 3:
    scene shackinteriorbase
    show shacktable
else:
    scene shackinteriorbasen
    show shacktablen
show zndress sadc
"She walks back inside the cabin. She sits with her back against the wall and looks down. She looks really sad."
show prot sad with dissolve
"You quickly follow her inside and sit beside her."
mc @sadt "What happened?"
znd @sadct "Everything."
mc @sadt "...What do you mean?"
znd @sadct "Why do you care?"
mc @hopet "Because I told myself I'd help you."
znd @sadct "Why? No matter what, I-I'll never be able to go back home..."
mc @angryt "So what?"
znd @sadct "Everything I had was in the village, every person I knew, every place I knew..."
mc @sadt "Zen... I also lost everything, once."
znd "..."
mc @sadt "When I was young my parents died and my village was burnt down. Uncle Pete took me in and brought me to Randel."
mc @hopet "I didn't know anyone, didn't have anything outside of my clothes but... I still ended up fine."
znd @sadct "It's different, [mc]. My people... They've always hated me."
znd @sadct "I was the last of my generation. I had to be taken care of while our men died against the Demon Lord."
znd @sadct "I didn't want to follow our traditions. Why did I have to become the priestess just because my mother was the previous one? I wanted to see the outside world. {b}That{/b} was my dream since I was a child. I didn't want to be bound to the village forever."
znd @smilect "And even worse... I couldn't become a mother."
znd @sadct "The people in our village were slowly decreasing, we needed as many children as possible... And I couldn't bear a single one."
znd @smilect "I was sterile."
mc "..."
znd @sadct "Not becoming a mother was my greatest sin."
znd @sadct "I was useless to the village.{p}...Who needed an elf who couldn't make other elves?"
znd @sadct "I thought accepting the role as priestess would save me, I knew that if I became the priestess they would at least... need me."
znd @sadct "But just because they needed me doesn't mean they ever liked me. They knew I accepted out of desperation.{p}...I can't remember the last time my mother smiled with me around."
znd @sadct "I did my best to fulfill my role as priestess. I made sure everyone followed the traditions... And so even those of the new generation that still liked me, stopped liking me."
znd @smilect "I became horrible, [mc]."
znd @smilect "I was scared to be tossed aside and I gave up on what I wanted to feel safe, to feel needed."
znd "...{p}...Morgan was the last man of our village. The only one who still hadn't left for the war."
znd @sadct "I... I'll n-never forgive myself."
"For a moment she seems to be going to cry again, but she manages to hold the tears back."
znd @sadct "I was desperate. For centuries nobody had spoken to me with pleasure, sometimes I even thought of...{p}...{p}But... I didn't."
znd @smilect "Instead I decided to prove to myself I was strong. That I wasn't a scared little girl anymore. That I only did it for myself and not for those ungrateful elves..."
znd @sadct "So I kidnapped Morgan. I locked him up and tortured him.{p}At first it was only to see if I could fool everyone, but then...{p}Then I became worse."
znd @sadct "He was the last male in the village... And I had him all for myself."
znd @smilect "I told myself I was doing it to degrade him, to pleasure myself..."
znd @sadct "The truth is, [mc], that I hoped I would get pregnant."
znd @smilect "Even after all these years, I still wanted their approval."
znd @sadct "...I'm so pathetic."
stop music fadeout 3
mc @sadt "...Were you happy?"
znd @sadct "What?"
mc @sadt "When you did those things, were you happy?"
play music reflection
znd @sadct "...I wasn't. Even though I hoped I would, I was miserable."
mc @hopet "Then there's still hope."
znd @sadct "What?"
mc @hopet "You aren't a bad person, Zen, you only did bad things."
znd @smilect "That doesn't make much of a difference."
mc @smilet "It does."
mc @hopet "Zen, you wouln't feel bad if you weren't a good person. You wouldn't cry when you're alone.{p}I want to prove that everyone was wrong in treating you like this. I'm giving you a chance to show the world how good you really are."
mc @hopet "You're not in the village anymore. Now you're here with me and the only thing I want you to do is be yourself. I don't want you to become a priestess, I don't want you to become a mother, I just want you to be yourself, because...{p}It's how you should be."
mc @smilet "Zen, I've never had to take care of anyone else before."
if girlclothes > 0:
    mc @hopet "Sure, there's Thea, but I barely had to do anything for her."
    mc @hopet "On the other hand for you I've been doing so many things and... Up until not too long ago I had my uncle care for me."
else:
    mc @hopet "Yet I've done lots of things for you when not too long ago I still had my uncle taking care of me."
mc @hopet "He decided to leave now that I'm 19 and let the house all for myself but even then I didn't feel so much like an adult. I was just a boy."
mc @hopet "But I've been taking care of you, I've helped you in all the ways I can. I've spent entire days just doing stuff for you and... I don't regret it."
mc @hopet "I've never had much responsibility in my life, and now I have you."
mc @smilet "I guess my uncle is right... I'm becoming an adult."
mc @smilet "You've shown me that you're not a bad person. You've shown me that you regret it and that nobody ever gave you a chance to begin with."
show zndress blush
mc @smilet"I didn't know why I was helping you at the beginning. Probably it was a sense of pity mixed with my belief that killing is bad... But now I know. I'm helping you because we're friends."
show prot smile
znd @blusht "...We are?"
mc @smilet "Of course."
show zndress normal
znd @talk "I'm..."
znd @smilect "Thanks, [mc]. Thank you for being my very first friend in almost 400 years."
mc @hopet "Thank you for showing me that sometimes I can be right about people."
if trissheal > 0:
    mc @hopet "It surely ended up better than last time when I got stabbed."
    znd @angryt "What?"
    mc @smilet "Yeah... I didn't want to kill a bandit and tried to defend him. In exchange he gave me a hole through my chest."
    znd @smilet "Well, I'm glad this time went better then."
    mc @smilet"Me too."
if time < 3:
    scene shackinteriorbase
else:
    scene shackinteriorbasen
show shacktable with vpunch
"Out of nowhere she hugs you."
zn "Thank you so, so much."
mc "You're welcome."
"The two of you stay like that for some time, enough time for her to peacefully fall asleep between your arms.{p}You decide to take her to her bed and you leave for the day."
if time < 3:
    scene zenelithshack
else:
    scene zenelithshackn
mc "{i}That went really well."
"You sigh, and only then you notice your clothes now have her sweet aroma."
$ zenQ = 4
$ time += 1
jump home

label zenelith5:
hide screen hud with dissolve
scene forrest
"As you walk towards Zenelith's hut, you notice something. Some branches on the path have been broken, higher than what you usually need to break to pass."
"At first you think it could've been Zenelith deciding to go on a walk, but then you see footprints, and they seem to point towards the cabin."
stop music fadeout 2
mc "{i}Uh-oh."
"You begin to run towards the shack."
play music dark
e "{size=-4}YOU!"
mc "{i}Oh no."
e "{size=-3}I found you."
znd "{size=-3}Stop! Please don't-"
e "{size=-2}You don't have your staff anymore, huh? Well that'll make it easier."
znd "{size=-2}I-"
e "{size=-1}How did you get that dress? Killed someone now that you can't torture Morgan anymore?"
znd "{size=-1}I didn't...!"
scene zenelithshack
show eve angry
show zndress r angry
mc "I did."
e @angryt "[mc]?!"
show prot angry
"You get between Zenelith and Eve."
e @angryt "You can't be serious."
mc @angryt "I can."
e @angryt "Do you understand who you're siding with here?"
mc @angryt "I think I do."
e @angryt "Then why?!"
menu:
    "She's not a monster":
        mc @angryt "She's not a monster, Eve."
        e @angryt "Oh, is she?"
        mc @angryt "She's a person, Eve. Like you and me."
        e @angryt "But she-"
        mc @angryt "I don't care."
        e @angryt "I can't believe you're acting like this."
        mc @angryt "I could say the same. I thought you were kind, yet here you are, filled with bloodlust. Do you think killing her will change anything? The only thing it'll bring will be death."
        e @angryt "Morgan deserves justice."
        mc @angryt "And murder is justice? She hasn't killed anyone."
        e @angryt "You wouldn't understand. You don't know Morgan."
        mc @angryt "You don't know Zen."
        e @angryt "Tsk. I've known her far longer than you have."
        mc @angryt "No. You've known the priestess for far longer than I have. You don't known Zenelith at all."
        e @angryt "Enlighten me, then."
        show zndress r normal
        mc @angryt "She was despised since birth and her family, the only people who ever gave her a chance, died centuries ago."
        mc @angryt "You all casted her aside and when she couldn't become a mother, she became the priestess because that way she would at least be respected."
        mc @angryt "What do you think would happen if someone lived like that for over four hundred years? Would you still be yourself? Would you still be kind? Because it seems to me it takes you much less to forget kindness."
        e @angryt "That doesn't excuse it."
        mc @angryt "It doesn't. She's done something terrible, but she's not an evil person. Have you never done something that you regret?"
        e @angryt "I did, but it was-"
        mc @angryt "...Completely different?"
        pause 1
        mc @angryt "That's what I thought."
        e @angryt "So what do you want me to do? Just let her be?"
        mc @angryt "No, I-"
        e @angryt "{size=-2}Shut up."
        mc @angryt "What?"
        e @angryt "{size=-2}Sh!"
        "you go quiet, then you hear it. The leaves all around you rustle and then..."
    "She regrets it":
        mc @angryt "She regrets it Eve. She knows what she did is wrong."
        e @angryt "Then let her face what she deserves."
        mc @angryt "She's not a murderer, she doesn't deserve to be murdered."
        e @smilet "Are you suggesting that I should torture her for a century and a half?"
        mc @angryt "That's not how it works Eve. Doing something just as bad as what she did won't make you a good person."
        show zndress r normal
        e @angryt "You don't understand."
        mc @angryt "I think I do."
        e @angryt "If you had known Morgan, you would understand."
        mc @angryt "Understand? I do understand. You're filled with rage and you want revenge. You aren't here for any kind of justice, you're here for revenge."
        e "..."
        mc @angryt "Eve, please, listen to me."
        mc @angryt "She has done a terrible thing, I agree. But everyone has done bad things they regret! She has simply done something worse than many of us have."
        mc @angryt "But I {b}know{/b} that she will compensate by being better than many of us."
        mc @angryt "The past days I've spent with her she has shown me many sides of herself and I believe she can be a good person- No, I {b}know{/b} she can."
        e @sadt "...So you want me to just let her be?"
        mc @angryt "No, I-"
        e @angryt "{size=-2}Wait."
        mc @angryt "What?"
        e @angryt "{size=-2}Be quiet!"
        "you go quiet, then you hear it. The leaves all around you rustle and then..."
    "She deserves a chance":
        mc @angryt "She deserves a chance, Eve."
        e @angryt "A chance? She already had one and she did what she did."
        mc @angryt "We both know that's not true."
        e @angryt "What do you mean?"
        mc @angryt "She was despised since birth and her family, the only people who ever showed her any kind of love, died centuries ago."
        mc @angryt "You all casted her aside and, when she couldn't become a mother, she became the priestess because that was the only way she would at least be respected."
        mc @angryt "She didn't even get that. Whenever she wasn't around you all talked shit about her, and you didn't know she had done anything to Morgan."
        mc @angryt "You wanna tell me she was strict? That she was a bitch? She gave you 60 years, Eve. Why didn't you become the village chief? You didn't want to let Sander go? If I wasn't around who knows what could've happened."
        mc @angryt "Now tell me: what do you think would happen if someone lived like Zenelith had to for over four hundred years? Would you still be yourself? Would you still be kind?"
        mc @angryt "She never got a chance, Evelyn. I'm giving her that chance because she has shown me she can be more than what everybody made her out to be, I'm giving her a chance because she's a good person."
        e "..."
        mc @angryt "Eve, please. I know she has done something horrible, but give her a chance. Let her at least try to redeem herself."
        e @angryt "{size=-2}Wait."
        mc @angryt "What?"
        e @angryt "{size=-2}Be quiet!"
        "you go quiet, then you hear it. The leaves all around you rustle and then..."
    "She's my friend":
        show zndress r blushn
        mc @angryt "She's my friend."
        e @angryt "What?"
        mc @angryt "I won't let you hurt any of my friends, I'm sorry Eve."
        e @angryt "How can she be your friend? She hates humans!"
        show zndress r angry
        znd @r angryt "I don't hate [mc]."
        e @angryt "Why? Because he gave you a nice dress?"
        znd @r angryt "Because he's my friend. He has helped me, he has been kind and... he's the first to do so in centuries, Evelyn."
        e @angryt "So that's it. He was the first one to help you."
        show zndress r angryt with vpunch
        znd @r angryt  "I just wanted someone!"
        scene zenelithshack
        show prot sad
        show zndress r angry
        show eve angry
        pause 2
        znd @r angryt "That was all I wanted, Eve! I wanted someone to be my friend! I've been cast aside all my life, and I couldn't even become a mother. You know how that is like, Eve."
        znd @r angryt "Torturing Morgan isn't my greatest sin for you and the others from the village, no, that is my inability to procreate, and before that it was my reluctance to follow traditions. I didn't want to be the priestess, Eve."
        znd @r angryt "I wanted to leave the village with my brothers and live in the outside world! But then they died and I had to become the priestess."
        e @angryt "That doesn't excuse you."
        znd @r angryt "It doesn't. But it doesn't excuse you either."
        znd @r angryt "I have changed. I've done it for myself, but it was thanks to [mc]. If it weren't for him I'd either be dead or still living with everyone else in the village."
        znd @r angryt "And you know what? I'd rather live here with a human than go back to the village. Nobody wanted me there to begin with."
        e "Tsk."
        mc @angryt "Eve, please."
        mc @angryt "She never got a chance to be the best she can. I'm giving her that chance because she has shown me she has a good heart. I'm giving her a chance because she {b}is{/b} a good person."
        mc @angryt "Let her redeem herself."
        stop music fadeout 3
        e @angryt "{size=-2}...Wait."
        mc @angryt "What?"
        e @angryt "{size=-2}Be quiet!"
        "you go quiet, then you hear it. The leaves all around you rustle and then..."
play music battlemusic1
scene zendirewolves with hpunch
mc "What the fuck?!"
zn "Where did they-"
e "We yelled too much... And to think I've been adventuring for decades!"
mc "Eve, there's a lot of them, what do we do?"
e "We kill them before they kill us of course."
mc "Reasonable enough."
scene zendirewolvesblr with dissolve
"You and Evelyn begin to fight. Zenelith looks helpless as she stands between you and the house. Her spells are too weak to do anything in this situation."
e "Zenelith! Why are you just standing there!?"
zn "I-"
"Zenelith runs inside the house."
e "Great! Just about what I'd expect from her."
"The direwolves keep coming. For each one you kill, two appear out of nowhere to try and jump you."
"Then you hear Evelyn yell."
mc "Eve!"
"One of the direwolves managed to knock her down, but just before it can attack her, Zenelith comes out of the house. She has something in her hand."
zn "Tiksha!"
scene zenelithpowerf with hpunch
"The direwolf falls to the ground, then Zenelith blasts another spell, and another, and another."
play sound magic
scene zenelithpowerf with hpunch
pause 0.5
play sound magic
scene zenelithpowerf with hpunch
pause 0.5
play sound magic
scene zenelithpowerf with hpunch
pause 0.5
stop music fadeout 2.5
"It doesn't take much for the direwolves to understand they're in danger and the few remaining ones flee, leaving the three of you alone once again."
scene zenelithshack
show znstaff r normal
show prot surprised
show eve angry
play music forest
mc @surprisedt "What the-"
zns @r smilet "I told you I didn't need you to make me a new staff."
mc @smilet "You put yours back together!"
e @angryt "Ahem."
mc "..."
e @angryt "I won't forgive you, Zenelith."
zns @r talk "I know."
e @angryt "But I trust [mc]."
mc @hopet "Thanks."
show prot normal
e @angryt "Don't thank me."
e @angryt "Zenelith, I'm not sure you're a good person, but I will let you prove that you're better than scum."
e @angryt "I'll let you be for now, but try something funny and I won't hesitate to kill you."
e @angryt "We'll never be friends and you will never be able to return to the village, so treasure [mc], because he might be the only friend you'll ever have."
zns @r blusht "...I already treasure him."
show znstaff r blush
e @smilet "Good."
mc @hopet "Well then-"
e @angryt "Goodbye."
hide eve with easeoutleft
show znstaff normal
mc @talk "Well, she's gone."
zns @talk "[mc]?"
mc @talk "Yeah?"
zns @talk "I'm... Tired. I know you just arrived but... If you don't mind I'd like to rest."
mc @talk "Oh, uhm, sure, don't worry, Zen."
zns @talk "Thanks."
hide znstaff with easeoutright
mc "{i}Well, time to go home."
$ persistent.zenDirewolf = True
$ zenQ = 5
$ time += 1
jump home



label zenelith6:
"You walk up to the door and knock"
mc "Zen?"
"You hear some quick footsteps and then the door opens."
show zndress smile
show prot smile
if time == 0:
    znd @smilet "Good morning, [mc]."
if time == 1:
    znd @smilet "Good afternoon, [mc]."
if time == 2:
    znd @smilet "Good evening, [mc]."
if time == 3:
    znd @smilet "Oh, [mc], it's a bit late isn't it?"
    mc @smirkt "But you're still awake, aren't you?"
    znd @smilet "You're not wrong."
mc @hopet "How are you feeling?"
znd @smilet "I'm feeling better."
mc @smilet "That's nice to hear."
znd @smilet "Want to come inside?"
mc @smilet "Yeah."
if time < 3:
    scene shackinteriorbase
    show shacktable
else:
    scene shackinteriorbasen
    show shacktablen
show zndress smile
show prot normal
mc @talk "So uhm..."
znd @determinedt "I want to prove myself."
show zndress determined
show prot question
mc @questiont "Huh?"
znd @determinedt "What you said yesterday might be true, but by standing in this hut alone all day I won't prove anything."
mc @questiont "How do you want to prove it?"
znd @determinedt "You are an adventurer, aren't you?"
mc @questiont "...Yeah?"
znd @determinedt "Helping people is your job, let me come along with you."
mc @hopet "I'm not sure that's a good-"
show prot surprised
show znstaff angry with vpunch
zns @angryt "If you won't take me, I'll will go myself."
mc @hopet "But- There's no need to do this, Zen. There's other ways to prove you're a good person."
show prot sad
zns @angryt "[mc], I wanted to leave the village when I was young. Before my brothers went to war, we dreamed of leaving and seeing the outside world."
zns @talk "The village was doing fine on its own. If we left we could help the people outside."
zns @angryt "My mother was so angry when she found out... She hated humans. I guess it's in character for a priestess."
zns @angryt "Sure, maybe I'm not fit for adventuring. After all yesterday I got really scared when the direwolves showed up... But I still managed to get my staff and help."
zns @smilet "If I see it's too much for me, I'll try something else, but first let me try being a good person by helping people the same way you do."
show znstaff smile
mc @sad "Sigh."
show prot smile
mc @smilet "Fine."
zns @smilet "Oh, thank you, [mc]! You don't know how grateful I am."
mc @smilet "Well then I'll go see what quest we could do together."
zns @talk "Wait, I wanna come with you."
show znstaff what
mc @hopet "...Well then let's go early tomorrow, otherwise you won't be able to come back home before it's dark."
zns smile "Mh."
mc @smilet "Make sure to sleep well."
zns @smilet "I will!"
mc @smilet "Bye."
zns @smilet "Bye bye."
$ zenQ = 6
$ time += 1
jump home



label zenelith7:
hide screen hud with dissolve
play music lake
scene zenelithshack with fade
"As you arrive to zenelith's cabin, you see her waiting outside. She seems to be ready to go."
show znstaff determined
show prot smile
mc @smilet "Hey there."
zns @determinedt "Good morning,"
mc @smilet "Shall we go?"
zns @determinedt "Yes!"
scene forrest with fade
pause 1
scene villageback with dissolve
"The two of you walk through the forest and then arrive at Randel. People are staring at her and she seems slightly uncomfortable, but you reassure her: There's just not that many elves around."
scene adventurersguild_day with fade
play music tavern
mc "Here we are."
zn "Wow... So this is an adventurer's guild, huh?"
mc "Yup."
j "{size=-1}[mc]!"
mc "Huh?"
"You turn around and see July waving at you gently. In front of her are standing Sander and Evelyn."
mc "Oh no."
scene adgc2 with fade
j "[mc], I was just telling Sander and Evelyn about a new quest that might need a few more people to do."
mc "What is it?"
j "It seems there have been a few sightings of a troll wandering around the area. It's decades we don't see such a strong monster so close to the town and we need someone to take care of it. Unfortunately all our diamond adventurers are out."
mc "I see, well, then count me and my friend in."
j "Oh?"
"You wave your hand at Zenelith and she walks all the way to the counter, she smiles shyly."
zn "Hi."
mc "She's Zenelith, she's quite strong and wanted to become an adventurer, so I took her here today."
j "But, [mc], even if she joined the guild she'd only be a recruit, she wouldn't be able to join you on the quest."
mc "...Can't we make an exception? The other day she saved me and Eve from a pack of direwolves almost all by herself."
j "Is that true, Eve?"
e "...Unfortunately, it is."
j "Well, if that's the case... Just this time we can make an exception."
mc "Thank you so much!"
"July hands the form to Zenelith and after she has got her briefing done, she is now finally an adventurer."
scene adventurersguild_day with fade
show sander c normal
show znstaff r normal
show eve angry
show prot normal
e @angryt "What are you doing here?"
mc @angryt "The same thing as you."
e @angryt "Tsk. Whatever, I'm going."
hide eve with easeoutleft
sa @c talk "Damn, kid. You befriended the crazy cowtits elf?"
zns @r angryt "You-"
show znstaff r angry
mc @smilet "Yeah."
show sander creepy
sa @talk "Good job."
mc @smilet "Thanks."
sa @talk "But now let's go, Eve will get angry if we lag behind."
show sander normal
mc @smilet "Alright."
hide sander with easeoutleft
show znstaff angry
zns @angryt "Does he always talk to people like that?"
mc @hopet "You'll get used to it, he's a nice person below... I think?"
show prot smile
zns @talk "Well, your friend is probably right. Let's follow them."
scene ambush1 with fade
play music lake
"The four of you all walk into the forest. Apparently the last sighting was close to the route to Yorkel."
mc "How could a troll get so close to Randel?"
sa "The Demon Lord's army has been doing more and more small raids across the border. It seems even the monsters are fleeing from the demons."
mc "Guess we'll have more work to do then."
sa "You're damn right! Lots of money is coming our way, kid."
"You keep walking. Every now and then Eve glances back at Zenelith, as if to check she isn't doing anything bad."
"Then all of you stop. You can hear in the distance the heavy footsteps of what is likely the troll you're looking for."
play music dark
sa "{size=-3}On the right."
"And there it is. From the right a giant monster appears and positions itself in the middle of the road."
scene troll
e "[mc], cover us."
stop music fadeout 3
"Sander and Eve take out their weapons and begin approaching the troll, but the monster doesn't react and waits for them."
zn "{size=-3}Why is it not-"
play music battlemusic1
"You manage to spot the goblins in the shadows just a second too late."
play sound darts
scene troll2 with vpunch
sa "What the fuck-!?"
e "Damn it...!"
mc "Sander! Eve!"
sa "It's... alright kiddo, just... do something... Ngh...!"
"You ready your sword."
mc "I don't think I can do much, but... I'll try! Zen, cover me!"
scene troll2 with hpunch
"Your rush towards the troll with your sword up in the air, but before you can strike, you hit a wall..."
scene troll3 with dissolve
"No, that's not a wall. Between you and the troll is a magic barrier."
mc "Huh?"
"When you turn around you see Zenelith holding her staff out, a yellow glow around her."
zn "Let me take care of this."
play sound darts
"The monsters have noticed something is wrong. They try to fire their darts again and the troll tries to do something as well, but nothing gets past Zeneliths' barrier"
stop music fadeout 3
zn "Reeme isha ke yon, praani ko reph rena..."
play music bunispiano fadein 3
"The air begins to cool. The grass outside the barrier slowly turns to ice and then, in the bat of an eye, the monsters in front of you are turned into ice."
scene troll4 with fade
$ persistent.zenTroll = True
mc "That was amazing!"
play sound fall
"But before you can keep praising her, she falls on the ground. You rush toward her."
mc "Zenelith!"
zn "I'm alright... I'm just not used to this kind of magic... I might've finished my reserves for the day... maybe for the week as well."
mc "You didn't have to do it, Zen, you could've at least let me handle some of the goblins."
zn "So you could get another splinter from one of their clubs?"
mc "Ha-ha. You're very funny."
zn "I didn't want you to get hurt."
mc "..."
zn "And of course I didn't want Evelyn and her friend to die either."
mc "Do you have that little faith in me?"
zn "Oh, no, I'm sure you could've done it."
mc "Sigh... Thanks."
zn "Don't thank me yet. Somebody needs to help me walk all the way back home."
mc "I think we can rest until their paralysis wears off, no need to hurry."
stop music fadeout 6
sa "If you could please turn me over so my face isn't on the ground I'd be really grateful!"
mc "Yes, yes, I'm coming."
scene ambush1 with fade
play music forest
"After an hour, everybody seems to be able to walk again. Sander staggers a bit, but that's just how he usually walks when he pretends to be sober."
show znstaff r normal
show eve
show prot smile
show sander c normal
sa @c talk "That was impressive, elf."
zns @r blusht "Thanks."
e @angryt "Yeah yeah, impressive. Who cares. We need to report to the guild that it wasn't just a troll, something here is fishy."
sa @c talk "Can we omit the part where we get saved by a recruit adventurer?"
mc @smirkt "Nope."
sa @c talk "Dang it!"
scene adventurersguild_day with fade
play music aguild
"The four of you walk back to the guild and after reporting everything to July, you get your reward and look at each other."
show sander c normal
show eve
show prot smile
show znstaff r smile
e @sadt "I hate to say it, but the only fair way to divide this is giving it all to Zenelith."
zns @r smilet "I don't want it."
sa @c talk "What?"
zns @r smilet "I don't really need it."
hide znstaff
hide prot
show znstaff r smile
show prot smile
mc @hopet "You earned it."
hide znstaff
hide prot
show prot smile
show znstaff r smile
zns @r smilet "You can have my part, [mc], you'll find better use for it than me."
hide znstaff
hide prot
show znstaff r smile
show prot smile
mc @talk "Well then..."
menu:
    "Keep it":
        $ money += 300
        mc @smilet "Thanks for coming anyways, Sander, Eve."
        sa @c talk "No problem, kid."
        mc @smilet "Well then, see ya."
        scene adventurersguild_day with dissolve
        "You grab your things and head towards the door with Zenelith, but right before you leave, Evelyn stops you."
    "Split it":
        $ money += 150
        mc @talk "Sander, Eve, let's split it in two."
        sa @c talk "That's way more than what I worked for. I'm all for that."
        e @sadt "Sigh... alright."
        scene adventurersguild_day with dissolve
        "You split the money and decide it's time to go. You grab your things and head towards the door with Zenelith, but right before you leave, Evelyn stops you."
    "Give it all to Sander and Eve":
        mc @talk "I haven't done anything either. You can have it."
        "You hand over the money to Sander and Eve."
        sa @c talk "Well kid, today you've made a wise decision. You made me get money for doing nothing."
        mc @smirkt "You did approach the monster first."
        sa @c talk "True... I should probably ask a raise."
        mc @smilet "Heh. See ya around."
        scene adventurersguild_day with dissolve
        "You grab your things and head towards the door with Zenelith, but right before you leave, Evelyn stops you."
show prot question
show znstaff r normal
show eve with easeinleft
e @sadt "...Thanks."
mc @surprisedt "Huh?"
e @sadt "I said thanks. Thank you for saving us."
show prot smile
zns @r smilet "It was the right thing to do."
e @sadt "Yes, it was."
"Eve looks down for a moment."
e @sadt "Bye."
hide eve with easeoutleft
"Then she immediately leaves."
show znstaff smile
mc @hopet "That's what I call progress."
zns @smilet "Yeah."
scene zenelithshackn with fade
play music night
"The two of you leave and head back to Zenelith's home. When you arrive it's already dark."
mc "It'll be a pain to find my way back now..."
zn "You know..."
mc "Yeah?"
zn "...You can sleep here if you want to."
mc "{i}I can?"
mc "Yeah... I'll just plant my tent here and-"
zn "I mean inside."
mc "...But there's only one bed inside."
zn "It's a big bed. You brought it here, you should know."
mc "..."
zn "So?"
menu:
    "Accept the offer":
        mc "Alright."
        scene shackinteriorbasen
        show shacktablen
        "The two of you enter the house."
    "Sleep outside":
        mc "It's fine. I don't want to bother you."
        "Zenelith raises an eyebrow."
        mc "What?"
        zn "C'mon, get in, you're not sleeping on the ground. I've done it for a week and I know it's horrible."
        mc "But I-"
        zn "No but's. There's enough space for the two of us."
        "She grabs you by your hand and takes you inside."
        scene shackinteriorbasen
        show shacktablen
mc "{i}Ending up in the same bed as Zenelith... definitely wouldn't have believed it'd happen a few weeks ago."
if mcBold == True:
    mc "I wonder if elves do kick around while they sleep..."
    zn "Would you like me to kick you?"
    mc "Mh... maybe."
    "You take off all but your long shirt and get into the bed, watching Zenelith as she joins you."
    "The two of you lay in silence for a while. You occasionally looks towards her, she looks in thought."
else:
    mc "So uhm..."
    zn "Yeah?"
    mc "Nothing."
    mc "{i}God this is so awkward..."
    "You take off what you think is appropriate to take off and get into the bed, facing towards the wall. Then soon after Zenelith joins you."
    "The two of you lay in silence for a while. You do your best to not turn towards her."
scene shackinteriorbasen
show shacktablen
pause 3
zn "[mc]?"
mc "Mh?"
zn "The other day, when Eve was here... If it wasn't for you I'd be dead. You saved me a second time."
menu:
    "It was the right thing to do":
        mc "It was the right thing to do, you deserve a chance."
        zn "Mh..."
    "You're my friend":
        mc "You're my friend, I had to do something."
        zn "Yeah..."
scene shackinteriorbasen
show shacktablen
pause 1
"A few minutes pass without a word, and as you finally fall asleep you feel something wrapping around your waist."
zn "...{size=-5}I   {size=-5}love     {size=-1}you..."
scene black with dissolve
pause 2
scene shackinteriorbase
show shacktable
play music home
"When you wake up, Zenelith has already left the bed. When you turn over you feel her side still slightly warm."
mc "Mh..."
zn "Good morning, [mc]."
"You look up and you see her on the doorstep with a basket."
show zndress smile
mc "Good morning."
znd @smilet "Slept well?"
mc "Yeah, I guess I really did buy a good mattress."
znd @smilet "I told you it's better than sleeping in a tent."
"Reluctantly, you get out of the bed. You expected to feel cold but somehow the temperature is warmer than you expected."
play music forest fadein 1
show prot smile
mc @smilet "What do you have there?"
znd @smilet "I thought I'd make some breakfast for the two of us."
mc @smilet "Elven cuisine, huh?"
znd @smilet "Our cuisine isn't that different from the humans, after all you did take it from us."
mc @smilet "Good point."
"You see her take a loaf of bread that she splits first in two. Then she opens the two slices and puts them on the table with the crumb facing upwards."
"You sit at the table and watch as she takes some fruit from the basket and holds them inside her hand. A faint green glow appears around her and then the top of the pieces of bread is filled with red jam."
mc @hopet "...You need to teach me that."
znd @smilet "Pft. Let me make something to drink."
"She takes two glasses from in front of the fireplace, they seem to have been made by hand with clay. She takes two oranges and once again she uses magic to fill the two glasses with orange juice."
mc @questiont "Did you make these?"
znd @smilet "Yeah. I can conjure water with magic, but glasses are still needed to drink it."
show prot sad
mc @talk "Sorry for forgetting to bring you any."
znd @smilet "It's fine."
znd @smilet "Let's eat now, shall we?"
show prot smile
mc @smilet "Yeah."
show prot surprised
"You grab one of the slices of bread and give it a bite. It's way sweeter than you expected, and for a second you can't contain a slight grimace."
znd @smilet "Is it too sweet?"
show prot smile
mc @hopet "No, no, it's fine, I just wasn't expecting it."
znd @smilet "Sorry, I'm too used to making it like that since I really like sweet things..."
mc @hopet "It's fine, Zen. It's really good."
"You keep eating while doing some small talk. When you're done you get up"
mc @smilet "Well, it's time to go."
znd normal "..."
hide prot with easeoutleft
show zndress r normal
"You walk towards the door, but Zenelith calls you."
znd @r talk "[mc], will you keep coming back for me?"
mc "Of course."
"She grabs your hand."
stop music fadeout 3
znd @r determinedt "Then come here, you dummy."
scene zenkiss with vpunch
"Zenelith suddenly pulls you into a kiss. At first you're shocked, but then you lean onto her."
zn "Mh..."
"Her body twitches as you wrap your hands around her."
zn "[mc]... I want you..."
mc "I want you too, Zen..."
"As the kissing continues, she slowly starts taking off your clothes. You do the same as you begin pushing her towards the wall."
zn "L-Let's get on the bed..."
"The two of you lay naked on the bed and it doesn't take long before the kissing devolves in something more."
"Your hands travel along her whole body as the kissing continues. One of her hand slowly slips on your abdomen and goes to touch your member."
zn "[mc]~"
"You look at her in the eyes and smile. Then you slip your member inside of her."
scene zenelith movie with fade
pause 2
zn "Fuck...!"
scene zenelith movie with dissolve
pause 1
mc "Zenelith..."
scene zenelith movie with dissolve
pause 1
zn "Don't stop~!"
scene zenelith movie with dissolve
pause 1.5
zn "[mc]~! I love you!"
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
zn "D-Do it inside~! n-nothing's going to happen..."
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
zn "That was amazing..."
mc "Yeah..."
$ persistent.zenGoodEnd=True
zn "I can feel your seed inside of me, eheh..."
hide zenelithsexc4
show zenelithsexc5
mc "...Are you sure nothing's going to happen?"
hide zenelithsexc5
show zenelithsexc6
zn "I'm sterile, [mc]. Even though I'd love to... I can't bear children."
mc "..."
hide zenelithsexc6
show zenelithsexc5
play music happy fadein 3
zn "But it doesn't matter right now... I never had someone make love to me like that..."
hide zenelithsexc5
show zenelithsexc7
zn "You were definitely the best."
mc "You're amazing too, Zen."
zn "I love you."
$ zenQ = 7
scene black with dissolve
pause 0.2
scene shackinteriorbase
show shacktable
"The two of you lay together for a few more minutes, then you sigh and sit up."
mc "I gotta go now."
"Zenelith smiles at you and places one hand on your back."
zn "I'll wait for you here. Come whenever you feel like it."
mc "I will."
zn "See you, [mc]."
mc "Goodbye."
"The two of you kiss one more time and then you dress up and leave."
scene forrest
mc "{i}Wow that was... something. I'm so lucky to have someone like her..."
menu:
    "To play with.":
        $ zenPlay = True
        $ evil += 1
        mc "{i}...To play with."
        mc "{i}I deserve an oscar for my performance, honestly. Sander is right, she's the cowtits elf priest, and now I can play wit her all I want~"
    "To fuck.":
        $ zenFuck = True
        mc "{i}...To fuck."
        mc "{i}Sure, she's fun, but I definitely don't love her... But I won't complain if I get to fuck her whenever I want."
    "To be with.":
        $ zenLove = True
        $ zen_love_day = day
        mc "{i}...To be with."
        mc "{i}She really is a good person. I can't believe everybody casted her aside... If I'm going to be her first, I'll do my best to be great."
$ zenrel += 100
$time += 1
jump home
