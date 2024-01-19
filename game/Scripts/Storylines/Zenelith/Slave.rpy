default zenS = 0
default scarlettaughtthatonespell = False
default scarletCharge = False
default zd1 = False
default zd2 = False
default zd3 = False
default zd4 = False
default zg1 = False
default asked4gift = False
default zenbag = False
default zenbooks = False
default zenmattress = False
default gaveZBag = False
default zentimer = 7

label ZenelithSlave:
$ zenSlave = True
$ zenBegun = True
$ evil += 2
mc "{i}She deserves what she got...{p}No, actually... she deserves worse than this."
mc "{i}She tortured Aerin's brother for almost two centuries and then she ran away. She's not getting away with a quick death or a life in the wild... Yeah, no. She is going to get punished for what she has done."
mc "{i}Afterall it's \"eye for an eye\", isn't it?"
mc "Get up."
zn "...Huh?"
mc "C'mon, get up before I change my mind."
zn "Wh-Why? T-Too afraid to dirty your hands with the blood of an elf?"
mc "{i}Oh, no. I just want to lure you somewhere to lock you in for another century."
mc "No, you don't deserve to live like this because of what you did. I want to make it right. I'll help you."
"Zenelith looks at you in anger but slowly, she gets up."
zn "Don't think I trust you, ape."
mc "You have no reason to."
zn "Tsk."
"She's so weak she almost falls again but she manages to stay upright."
mc "Let's get going. I'm as lost as you are but we shouldn't be too far from the road."
show forrestn
"She reluctantly starts following you."
scene forrestn
mc "{i}Alright, there's still a problem with all of this..."
mc "{i}I can't just take her to Randel, my home doesn't have anywhere to keep her."
if thealive == True:
    mc "{i}And I've already got Thea at home..."
mc "{i}Obviously the Elf Village isn't an option either."
mc "{i}Even if her house is empty now, they'd get suspicious of me going there often.{p}What a shame! Her basement would've been perfect."
mc "{i}I'm starting to think It'd be better to just kill her and be done with her..."
"The two of you walk for what seems an eternity before Zenelith speaks up."
zn "I'm not sure why I'm trusting you."
mc "And I'm not sure why I'm helping you."
zn "..."
zn "How can I know you're not just taking me somewhere to kill me?"
mc "Because simply killing you would give you less chances to run away."
zn "..."
mc "Listen, I'm already helping you here. Let's make a deal."
zn "What deal?"
mc "I'll keep helping you so long you stop questioning me."
zn "How could I not question the actions of an ape like you?."
mc "It's easy. You just have to not open your mouth."
"Zenelith doesn't reply."
mc "Exactly like that."
zn "..."
mc "Good, you're starting to get it-{p}...Wait, I think I see something."
scene zenelithshackn with fade
mc "{i}What the-?"
zn "...What is this?"
mc "{i}...Perfect! A shack in the middle of nowhere! Now I just have to figure out how to lock her in there."
mc "A cabin in the middle of the woods."
zn "I could see that already."
mc "Good. Let's get inside."
"As you walk inside, Zenelith angrily follows you."
scene shackinteriorbasedirtyn with fade
show prot normal
show znrag angry
znr @angryt "This place is awful."
mc @smirkt "Oh, I think it's perfect."
znr @angryt "Of course, it's the standard for you apes."
mc @smilet "Ah yes, that's exactly what I meant."
mc @smilet "Let's sleep here for tonight. Tomorrow morning we'll find another solution."
znr @angryt "I'm not going to sleep with an ape."
mc @hopet "I'l sleep outside if that makes you feel better."
znr @angryt "It doesn't."
mc @talk "Well, can't do much about that. Have a good night."
znr @angryt "...What stops me from killing you while you're asleep?"
mc @smirkt "They're gonna come look for me if I suddenly disappear. \"They\" includes Eve, by the way, so it really wouldn't be in your best interest to kill me."
hide prot normal with easeoutleft
"And as Zenelith glares at you one last time, you leave the shack."
scene zenelithshackn with fade
"Once outside you turn around and look at the door. How can you lock her in? You don't have chains nor a seal to-"
mc "{i}Wait! What did Scarlet say about the rune? The spell could turn off that kind of seals... but it can also turn them on!"
mc "{i}Maybe if I carve the seal onto the door and use the rune I could imprison her. Her magic is too weak to even hurt me, she definitely won't be able to undo the seal."
mc "{i}Let's hope I didn't throw the rune at some point."
"You decide to go to bed for now. It's going to be easier to check your bag when the sun comes out."
"Thus you use your camping gear and set up a tent for yourself. You slowly fall asleep."
stop music fadeout 1
scene black with fade
pause 2
play music forest
scene zenelithshack with dissolve
pause 2
"The next day you wake up early and find yourself still alive. She either decided not to kill you or she simply sleeps more than you do."
"You decide to go inside the house to check on her."
scene znsleep
"She's still sleeping, a faint smile on her face."
mc "{i}Smiling even after all the things she's done... Tsk."
scene zenelithshack with fade
"You get your bag and start checking every pocket hoping to find the rune. You almost end up taking everything out of the bag before you can find it at the bottom of one of the main pockets."
mc "{i}I knew I hadn't thrown it away! Now let's start carving the symbol."
"You take out your knife and begin carving the seal on the door hoping she doesn't wake up."
"Fortunately, she doesn't."
"Once you're done you use the rune to try and activate the seal.{p}...{p}......"
show zenss1 with dissolve
"The carving suddenly glows yellow and when you try to open the door it doesn't even flinch slightly. The seal works."
mc "{i}Good job, [mc]. Now I've just got to repeat this... two more times for the windows."
show zenss with dissolve
"You manage to finish all the seals before she wakes up but right after using the rune on the last window you notice that the rune feels a lot lighter."
mc "{i}Huh? Why is it...?"
mc "{i}Wait. Could it be that the spell can only be cast a certain amount of times?"
mc "{i}If that's the case then I need to have Scarlet cast magic on the rune every now and then or else I won't be able to get in and out of the house... God damn it."
mc "{i}I don't want to risk undoing the seal just to get in the house now... I guess I'll wake her up from here."
play sound doorknock
mc "Zenelith! Wake up!"
play sound doorknock
"You loudly knock on the door a few times until you hear her angrily moan."
zn "What the hell is wrong with you, ape?! I am trying to sleep!"
mc "You know how yesterday I told you that you had no reason to trust me?"
zn "...Huh?"
mc "Well, I wasn' being sarcastic."
zn "What the hell do you-"
"You hear Zenelith rushing over the door and trying to open it to no avail."
zn "No... You couldn't have-"
mc "I have. Thank you very much for teaching me about seals."
zn "You piece of-!"
mc "Nuh-uh. Don't be like that, that will only make it worse for you."
zn "As soon as I get out of here you're dead!"
mc "See, that's the thing. You won't get out of here. How long do elves live again?"
zn "W-What are you trying to say?"
mc "You kept Morgan in your dungeon for 160 years. I was wondering if you even had that many years left before your death considering you were the oldest in the village."
zn "You can't leave me here that long! You won't even live for that much!"
mc "You're right, I won't live 160 years and most likely I won't live another 80 either. But that doesn't matter. I can make it much, much worse for you in this shorter time together to keep it fair."
zn "Please! Don't! I'm sorry for what I've done!"
mc "Hah! ...It's too late to apologize. I've already decided what to do with you."
mc "At first I thought I could kill you, but then I thought... \"Why not punish her?\"{p}You're horrible, Zenelith, you deserve this."
mc "Plus, I also get to enjoy using you as much as I want~ You're lucky your looks are right up my alley."
zn "As if I'd ever let you, disgusting ape!"
mc "You're weak and frail. You can't use your magic against me... And if you were to venture out alone I think you'd quickly die. Honestly, I'm impressed you didn't die before I found you."
mc "You can't do anything to stop this, Zenelith."
zn "I won't become a slave of an ape!"
mc "You already have."
"Zenelith bangs on the door, you can almost hear her grinding her teeth."
zn "FUCK YOU!"
mc "That's a really bad start. You need to learn some manners."
zn "I won't treat you as anything other than a dumb ape, you little-"
mc "Yeah, yeah. That's enough. I'm going to go. If by next time you've calmed down, I'll give you something to eat, alright?"
zn "If you step inside you're dead!"
mc "I'll take that as a yes."
scene ambush1 with fade
"You leave as the sound of Zenelith slamming her fists on the door and calling out slowly fades away. You end up finding your way back to the main road and leave a small mark on a tree to remind yourself where to head for the shack."
#call screen WaterSports with fade
#pause
#label WaterSportsYes:
#$ watersports = True
#hide screen WaterSports
#jump slaveIntroEnd
#label WaterSportsNo:
#hide screen WaterSports
#jump slaveIntroEnd
#label slaveIntroEnd:
$ zenS = 1
$ persistent.zenIntro = True
$ day += 1
$ time += 1
jump home


label foodShenanigans:
scene ambush1 with fade
hide screen hud with dissolve
"You leave Randel with a basket full of fruit. You don't exactly know what people from the elf village usually eat but you figured that if they live in trees they likely enjoy fruit."
"You walk for a while until you reach the tree you had left a mark on. From there you walk inside the forest until arriving at the cabin you left Zenelith in."
scene zenss with fade
if chargedRune < 1 and scarletCharge == False:
    "You take out the rune from your bag and remember that you still haven't asked Scarlet to repair it."
    mc "{i}Right. I better go before doing anything with Zenelith."
    jump home
elif chargedRune < 1:
    "You take out the rune from your bag and realize it's really light. You probably need Scarlet to charge it up again."
    mc "{i}Let's go see Scarlet, I wouldn't want to end up letting the door unlocked."
    jump home

if lastAte == 1:
    jump day1
elif lastAte == 2:
    jump day2
elif lastAte == 3 and RapeZen == True:
    jump day3
elif lastAte == 4 and RapeZen == True:
    jump day4
elif lastAte < 10 and RapeZen == True:
    jump day5
elif lastAte < 10:
    jump day3f
elif lastAte >= 10:
    $ evil += 1
    jump starvedZen


label day1:
play sound doorknock
mc "Goodmorning, Zen."
"At first you hear nothing, then the shack's floorboards creak."
zn "What do you want, ape?"
mc "I wanted to know if you had calmed down, have you?"
zn "Calmed down? Yes, I'm calm enough to know exactly what I will do the moment you step inside."
mc "I see, you still haven't understood your position then."
zn "My position? You're the ape here."
mc "And you're a slave."
zn "Not for long."
mc "Sure thing.{p}Well, Zen, I guess I'll go again. I hope next time you'll have changed idea."
"And thus you leave."
$ zd1 = True
$ time += 1
jump home


label day2:
if zd1 == True:
    play sound doorknock
    mc "Goodmorning again, Zenelith."
    zn "..."
    "She stays quiet. For a second you believe she might have decided to calm down, then you hear her punching the door."
    zn "LET ME OUT!"
    mc "Oh, no no no. You got this wrong Zen. You aren't getting out."
    zn "You apes are all the same... Deceitful and cruel."
    mc "It's funny to hear that from you, Elder Priestess. I wonder if Morgan would agree with you."
    zn "SHUT UP!"
    mc "I see you haven't calmed down yet. It's alright, I can come another day."
    if RapeZen == True:
        zn "Tsk. Yeah, come another day. You will still be a disgusting ape."
    else:
        zn "...Y-Yeah! Come another day! I'm n-not going to give up!"
    mc "The more you resist the worse it'll be for you in the end. It would've been much easier to be obedient...{p}...Now though, that won't be enough."
    zn "Wh-What?"
    mc "You'll see.{p}Have a nice day."
    zn "You-!"
    "And then you leave."
    $ zd2 = True
    $ time += 1
    jump home
else:
    play sound doorknock
    mc "Good day, Zenelith."
    zn "..."
    "Zenelith doesn't answer."
    mc "Have you decided to ignore me or have you resigned yourself?"
    zn "I-I'm not giving you any satisfactions, ape."
    mc "Oh but you've already satisfied me by letting yourself get trapped so easily."
    zn "...I trusted you."
    mc "Too bad."
    zn "As soon as you lower your guard I-I'll show you how that feels."
    mc "That won't happen. I won't lower my guard around a bitch like you."
    zn "How {b}dare{/b} you call me that!?"
    mc "Is \"toy\" better? That's how you called Aerin's brother, right?"
    zn "SHUT UP!"
    mc "...I see you haven't calmed down yet. It's alright, I can come another day."
    if RapeZen == True:
        zn "Yeah, come another day. You will still be a disgusting ape."
    else:
        zn "...Y-Yeah! Come another day! I'm n-not going to give up!"
    mc "The more you resist the worse it'll be for you in the end. It would be much easier for you to be obedient...{p}...But I guess that if you won't behave, I have no reason to behave either."
    zn "Wh-What do you mean?"
    mc "You'll see.{p}Have a nice day."
    zn "You-!"
    "And then you leave."
    $ zd2 = True
    $ time += 1
    jump home


label day3:
if (zd1 == True) or (zd2 == True):
    play sound doorknock
    mc "Good day, Zenelith."
    zn "{size=-2}I'm not... giving up... I'm not... giving up..."
    mc "Zenelith? Have you already lost your mind?"
    zn "Huh? O-Oh... You're back, ape."
    mc "Hungry?"
    zn "Not enough to have lost my spirit."
    mc "I noticed."
    zn "It's being harder than you expected isn't it?"
    mc "Maybe you're just angrier because I raped you back there in your basement."
    zn "{b}Don't{/b} bring that up."
    mc "Why not? sore spot? I could've done much worse honestly."
    zn "You defiled me, ape. And I won't forgive that easily. Come back however many times you want, I am not giving up."
    mc "We're just on the third day, Zen. We still got a long time ahead of us."
    zn "I'm an elf, a human day for me is nothing."
    mc "We'll see about that next time around. See you."
    "And then you leave Zenelith once again."
    mc "{i}What a pain in the ass..."
    $ zd3 = True
    $ time += 1
    jump home
else:
    play sound doorknock
    mc "Good day, Zenelith."
    zn "You've decided to show up, ape. I almost thought you had become a chicken of sorts."
    mc "Really funny."
    zn "Not as funny as your attempt at breaking me. You've already defiled me once, I won't let you take advantage of me a second time."
    mc "Oh, won't you?"
    zn "I will not."
    mc "Well, at first I thought I'd just feed you as soon as you calmed down but... you know what? I've changed my mind."
    zn "What?"
    mc "I'll give you food when you take off your top."
    zn "WHAT?!"
    mc "You heard me right."
    zn "You... I'll kill you!"
    mc "You can try."
    mc "Anyways, I hope next time you'll be calmer. Have a nice day."
    "And then you turn around and leave. You hear Zenelith protesting but you ignore her."
    $ zd3 = True
    $ time += 1
    jump home


label day4:
play sound doorknock
mc "Zenelith~? How are you?"
zn "R-Ready to kill you."
mc "Oh, c'mon. There's no need to be so aggressive."
zn "You're the one who asked."
mc "I guess you're right."
zn "Of course I am."
mc "Am I to suppose then that you're still not willing to behave?"
zn "...Y-Yes."
mc "Oh, what a shame... Guess I'll eat this fruit all by myself."
zn "Ngh..."
mc "Heh. Bye, Zen."
"You leave her there and return home. She's definitely lost most of her spirit... Maybe tomorrow she'll finally give in."
$ zd4 = True
$ time += 1
jump home


label day3f:
play sound doorknock
mc "Zenelith~?"
play sound doorknock
mc "I've got you a basket full of fruit~"
zn "Ngh..."
mc "C'mon... Why do you have to be like this? I just want you to behave and then I'll give you all the food you want~"
zn "...I can't let you win..."
mc "I think that getting to eat counts as a win on your side as well, you know?"
zn "..."
mc "And, after all, how are you planning to escape if you don't even have the energy to stand up?"
zn "..."
zn "W-Will you really let me eat if I behave?"
mc "Of course I will. I've already got you where I wanted, there's no reason to let you die."
zn "F-Fine then..."
mc "Ahhh... Good! Then let's start with something easy, aye?"
zn "W-What is it?"
mc "From now on, call me {b}master{/b}."
zn "I am not-!{p}I-I'm...{p}...Yes, master."
mc "{i}Hah! She's actually doing it!"
mc "That's good. Now I'm going to come in. If you try to jump me when I get in, you're dead."
zn "Y-Yes..."
mc "I don't think I've heard that right."
zn "{size=-4}Y-Yes, master."
mc "What?"
zn "Yes, m-master!"
mc "That's more like it."
"You walk over to the door and use the rune on it. The glow of the seal disappears and then you walk inside."
scene shackinteriorb
"As soon as you get in you see Zenelith sitting with her back on a wall trying to get up."
mc "There's no need to stand up. I'll come over there."
scene znboobcloths
show znboobworried
"You make your way to her and sit in front of her. You put the basket to the side and when Zenelith tries to reach for it you push it just far enough that she can't grab it."
show znboobangry
zn "What are you-"
mc "Take off your top."
zn "W-What?!"
mc "I'll give you 10 seconds, then I'll leave."
zn "Y-You can't-"
mc "10...{p}9..."
zn "W-Wait!"
mc "8...{p}7...{p}6..."
show znboobshy
hide znboobangry
zn "W-Why do you have to-"
mc "5...{p}4...{p}3..."
zn "F-Fine!"
"As your count approaches zero, she hastily removes her top. She clearly doesn't like it but she doesn't have the energy to protest anymore."
scene black with dissolve
pause 0.2
scene znboobnude
show znboobfing
show znboobeyeside
pause 3
zn "A-Are you happy now?"
mc "Almost. You forgot to say my name."
zn "..."
show znboobangry
hide znboobfing
hide znboobeyeside
zn "{size=-5}Y-You piece of..."
mc "What?"
zn "..."
show znboobshy
zn "A-Are you happy now... m-master?"
scene znboobnude
show znboobshy
pause 3
mc "I am."
"You move the basket until she can easily reach inside of it."
show znboobshy
show znboobeyeside
hide znboobangry
"The moment her hand manages to reach the first fruit she completely forgets about her missing top and starts to eat eagerly."
mc "{i}I'd say it's enough for now. If I try to push it some more she might go back to how she was before."
mc "Alright Zen, I'm going to go now. Enjoy your meal."
"She barely pays you any attention as you leave the shack. Once outside you close the door and apply the seal again."
mc "{i}I wonder how many things I can get her to do without forcing her... Maybe she will actually become like a slave if I train her the right way... Hm..."
"And while you think about that, you return home."
$ chargedRune -= 1
$ persistent.zenGrope1 = True
$ zenS = 2
$ lastAte = 0
$ time += 1
jump home

label day5:
play sound doorknock
mc "Zenelith~?"
play sound doorknock
mc "I've got you a basket full of fruit~"
zn "Ngh..."
mc "C'mon... Why do you have to be like this?"
zn "Y-You're scum..."
mc "And yet I'm here offering you food in exchange of very little."
zn "..."
mc "And, after all, how are you planning to escape if you don't even have the energy to stand up?"
zn "..."
if zd3 == True and (zd1 == False or zd2 == False):
    zn "I-I won't take off my top."
    mc "I think you will."
    zn "..."
    mc "As a matter of fact, now I'll come inside and you'll do it spontaneously."
    zn "I-I-"
    scene shackinteriorb
    "You use the rune on the door and you enter the room. As soon as she sees the fruit in the basket her mouth opens."
    mc "So?"
    "She looks at you with hate, yet desperation is clearly the stronger emotion inside of her as she quickly undoes the knot that kept her top up."
    scene black with dissolve
    pause 0.2
    scene znboobnude
    show znboobfing
    show znboobeyeside
    pause 3
    zn "A-Are you happy now?"
    mc "Mh... Almost."
    show znboobangry
    hide znboobeyeside
    hide znboobfing
    zn "W-What else do you want?!"
    mc "Stop calling me ape. From now on I'm your {b}master{/b}."
    zn "I-I'm not going to-"
    "You suddenly put your hand on the hilt of your sword."
    mc "Sorry, could you repeat that?"
    show znboobshy
    hide znboobangry
    zn "...{p}I-I...{p}...Yes, master."
    mc "Good."
else:
    zn "W-What do you want me to do?"
    mc "You know what I want you to do."
    zn "A-And you'll let me eat afterwards...?"
    mc "Of course I will. I've already got you where I wanted, there's no reason to let you die."
    zn "F-Fine then..."
    mc "Ahhh... Good! Then let's start with something easy, aye?"
    zn "W-What is it?"
    mc "From now on, call me {b}master{/b}."
    zn "I am not-!{p}I-I'm...{p}...Yes, master."
    mc "{i}Hah! She's actually doing it!"
    mc "That's good. Now I'm going to come in. If you try to jump me when I get in, you're dead."
    zn "Y-Yes..."
    mc "I don't think I've heard that right."
    zn "{size=-4}Y-Yes, master."
    mc "What?"
    zn "Yes, m-master!"
    mc "That's more like it."
    "You walk over to the door and use the rune on it. The glow of the seal disappears and then you walk inside."
    scene shackinteriorb
    "As soon as you get in you see Zenelith sitting with her back on a wall trying to get up."
    mc "There's no need to stand up. I'll come over there."
    scene znboobcloths
    show znboobworried
    "You make your way to her and sit in front of her. You put the basket to the side and when Zenelith tries to reach for it you push it just far enough that she can't grab it."
    show znboobangry
    zn "What are you-"
    mc "Take off your top."
    zn "W-What?!"
    mc "I'll give you 10 seconds, then I'll leave."
    zn "Y-You can't-"
    mc "10...{p}9..."
    zn "W-Wait!"
    mc "8...{p}7...{p}6..."
    show znboobshy
    hide znboobangry
    zn "W-Why do you have to-"
    mc "5...{p}4...{p}3..."
    zn "F-Fine!"
    "As your count approaches zero, she hastily removes her top. She clearly doesn't like it but she doesn't have the energy to protest anymore."
    scene black with dissolve
    pause 0.2
    scene znboobnude
    show znboobfing
    show znboobeyeside
    pause 3
    zn "A-Are you happy now?"
    mc "Almost. You forgot to say my name."
    zn "..."
    show znboobangry
    hide znboobfing
    hide znboobeyeside
    zn "{size=-5}Y-You piece of..."
    mc "What?"
    zn "..."
    show znboobshy
    zn "A-Are you happy now... m-master?"
    scene znboobnude
    show znboobshy
    pause 3
    mc "I am."
"You move the basket until she can easily reach inside of it."
show znboobshy
show znboobeyeside
hide znboobangry
"The moment her hand manages to reach the first fruit she completely forgets about her missing top and starts to eagerly eat."
mc "{i}I'd say it's enough for now. If I try to push it some more she might go back to how she was before."
mc "Alright Zen, I'm going to go now. Enjoy your meal."
"She barely pays you any attention as you leave the shack. Once outside you close the door and apply the seal again."
mc "{i}I wonder how many things I can get her to do without forcing her... Maybe she will actually become like a slave if I train her the right way... Hm..."
"And while you think about that, you return home."
$ chargedRune -= 1
$ persistent.zenGrope = True
$ zenS = 2
$ lastAte = 0
$ time += 1
jump home


label starvedZen:
scene zenss with fade
"You knock on the door of the shack."
mc "Good morning, Zen."
scene zenss
pause 1
"...Silence."
mc "Zen?"
"Still no answer."
mc "I'm getting angry, Zen. If you don't answer I'll get in and teach you a lesson."
"Again, she doesn't answer. You can't even hear the creaks of the floorboards."
mc "Alright, that's it."
scene shackinteriorb
"You undo the seal and storm inside, ready to throw hands at her, yet when you get in she's on the floor. Motionless."
mc "Zen?"
"You tap her lightly with the foot. She doesn't flinch."
mc "Uh..."
"You get down on your knees and put a finger in front of her mouth. She isn't breathing.{p}You nervously touch her neck. She's cold and you can't feel her heartbeat."
mc "God damn it."
scene zenelithshack
"You quickly get up and walk outside. You know it's your fault she's dead."
menu:
    "She deserved it.":
        "But after all, she deserved to suffer. She's probably lucky she managed to die before you could do anything worse to her."
        mc "...Tsk. I guess I've got something less to worry about at least."
        "You leave her there and go home. You decide you won't come back."
    "She didn't deserve it.":
        mc "Even for what she's done... She didn't deserve a death like this. It's too cruel even for me."
        mc "Sigh... Well, whatever. I guess she managed to avoid what I wanted to do with her."
        "You decide to leave her there and go home. There's no reason to stay or come back."
$ zenRouteEnd = True
$ chargedRune -= 1
jump home


label zenGrope01:
hide screen hud
show prot normal
$ chargedRune -= 1
if zg1 == False:
    mc @smirkt "Hungry?"
    znr @angryt "...No."
    mc @smirkt "We both know that's a lie."
    zn "..."
    mc @talk "Oh, c'mon, what's gotten into you? You were doing so well."
    znr @angryt "I-I won't let you humiliate me further."
    mc @talk "Too bad then. We'll see if you still think like this next time I come."
    $ zg1 = True
    $ time += 1
    jump home
else:
    mc @smirkt "So, have you made up your mind?"
    znr @angryt "...Yes."
    mc @smilet "That's nice to hear."
    znr @angryt "I won't do a-anything you want me to again!"
    mc @talk "Oh, c'mon. That's just counter-productive."
    znr @angryt "I-I don't care!"
    mc @talk "Sigh. Well, see you then."
    $ time += 1
    jump home


label zenGrope1:
$ chargedRune -= 1
hide screen hud
show prot normal
if zg1 == True:
    mc @smirkt "Changed idea yet?"
    "Her expression is enough to tell you that if she could she would stab you right without hesitation."
    zn @angryt "...Y-Yes, master."
    mc @smilet "I knew you'd come to your senses."
else:
    mc @smirkt "Hungry?"
    znr @angryt "...{p}Y-Yes."
    mc "Good, I've got some food with me."
znr @angryt "...D-Do I have to-"
mc @talk "Yes."
mc "{i}...She keeps forgetting how she has to call me."
zn "..."
scene black with dissolve
pause 0.2
scene znboobnude
show znboobfing
show znboobeyeside
pause 2
mc "You're learning quickly. Here, have some food."
"You give her some food to eat. She grabs it without saying a word and starts eating."
if zg1 == True:
    mc "{i}Even so... It took her some time to get she has to do what I say... Has she really understood what her place is?"
else:
    mc "{i}Yet, I wonder... Has she understood what her place is?"
menu:
    "She probably hasn't. Let's teach her a small lesson.":
        mc "{i}Yeah, let's show her that resisting won't benefit her even when she gives in."
        "Just as Zenelith goes to take some more food, you grab it all and push it aside. She looks at you shocked."
        scene shackinteriorb with fade
        show znrag angry
        znr @angryt "W-What-!?"
        mc @talk "That's all you get."
        znr @angryt "What? W-Why?"
        if zg1 == True:
            mc @talk "You resisted. You don't deserve to eat all the food I brought you."
            znr @angryt "But I-"
            mc @talk "I don't care. You should've done it the first time I came back, not now."
            zn "..."
            mc "Goodbye now."
            "You grab the food you pushed aside and leave the shack. She looks angry but doesn't try anything."
        else:
            mc @talk "I want to make sure you understand your place."
            zn @angryt "B-But I've done what you asked me to!"
            mc @talk "Then why have you not been referring to me as master?"
            zn "..."
            mc @talk "Exactly. See you Zenelith."
            "You grab the food you pushed aside and leave the shack. She looks angry but doesn't try anything."
    "After not eating for 3 days again she probably got it.":
        mc "Alright Zen, I'm going to go. I'll bring more food next time, so I hope you'll keep doing what I say."
        "Zenelith doesn't reply and keeps eating instead."
        mc "{i}What a pain she is..."
$ zenS = 3
$ lastAte = 0
$ submission = 1
$ time += 1
jump home

label zenGrope02:
hide screen hud
show prot normal
$ chargedRune -= 1
mc @smilet "Good day. I've brought you something to eat."
"Zenelith glares at you then tries reaching for the food but you immediately step back."
mc @talk "I think you still haven't understood how this works, slave."
zn "..."
mc @talk "First of all, I want to hear you calling me master from now on. Always."
zn "..."
mc @talk "C'mon. I'm waiting."
znr @angryt "...Yes, master."
mc @talk "Second of all, you only get to eat {b}when I say so{/b}. You don't reach to the food before I'm satisfied with you, got it?"
znr @angryt "Yes..."
mc @talk "Try that again."
znr @angryt "Yes... master..."
mc @talk "Better. Now take off your top."
zn "..."
scene black with dissolve
pause 0.2
scene znboobnude
show znboobangry
pause 2
mc "I see you're starting to get it. But you know that your disobedience can't go unpunished, right?"
zn "W-What?"
mc "No food today. Have a nice day."
zn "B-But I just did what you asked me to!"
mc "I asked you to do it the other day and the day before too. I don't want a slave who does what I say whenever they want to. I want a slave who does what I want when I want."
"You start heading towards the door."
scene shackinteriorb with fade
show znrag angry
show prot normal
znr @angryt "Y-You..."
mc @talk "I'd recommend you to not try your luck further."
zn "..."
$ time += 1
jump home

label zenGrope2:
hide screen hud
show prot normal
mc @talk "Goodmorning, slave."
zn "..."
mc @talk "I hope you're hungry, because I got some food for you."
znr @angryt "...I am, master."
mc @smilet "Good. Let's get started then."
"Zenelith stays still for a moment, then she takes off her top without saying a word."
scene black with dissolve
pause 0.2
scene znboobnude
show znboobworried
pause 2
mc "You know... I think I got bored of that."
"A spark of hope appears in Zenelith's eyes. Maybe you'll stop asking her to undress every time she has to eat."
mc "Just looking at them... It's not doing much for me."
show znboobangry
hide znboobworried
zn "W-Wait, what do you-?"
scene znboobgrope
show znboobangrysurprised with vpunch
pause 1
zn "What the hell?!"
mc "Oh yes, this is much better."
zn "S-Stop right now."
mc "Hm... I don't think I will. Actually, how about I squeeze them a bit?"
zn "W-Wait-"
scene znboobgrope
show znboobfing with hpunch
pause 1
zn "Ahn~!"
mc "Heh, I see you like it too."
show znboobangrysurprised
hide znboobfing
zn "N-No, I don't!"
mc "That's why you were moaning?"
zn "I was not!"
scene znboobgrope
show znboobfing with hpunch
zn "Ah~!"
mc "So how do you call that?"
show znboobangrysurprised
hide znboobfing
zn "Y-You piece of..."
mc "Ah-ah. Watch your mouth."
zn "...Yes, master."
mc "Good. You can eat now."
scene znboobnude
show znboobshy
show znboobeyeside
"You let her breast go and hand her the food, she immediately starts eating. You decide to leave for the day."
$ lastAte = 0
$ zenS = 4
$ time += 1
jump home

label zenGropeEnd:
hide screen hud
show prot normal
mc @smilet "Hey there, how are you doing today?"
znr @angryt "Bored. You know, I stay all day inside a shack all by myself."
mc @talk "That makes sense, I guess."
mc @smirkt "Hungry?"
znr @angryt "Yes."
mc @smilet "That's nice to hear. I brought lots of tasty stuff with me. Let's get started, shall we?"
"Zenelith looks down with a grimace. Then she takes a deep breath."
scene black with dissolve
pause 0.2
scene znboobnude
show znboobworried
pause 2
zn "Pleased?"
mc "Oh, you know I'm not."
zn "..."
scene znboobgrope
show znboobfing with hpunch
pause 2
zn "Mnh..."
mc "You're holding in, huh?"
zn "W-What?"
mc "Open your mouth and stick your tongue out."
zn "Huh?"
mc "It's an order."
scene znboobgrab
show znboobmouth with vpunch
zn "Whath awe you-"
scene znboobgrab
show znboobmouth
pause 1
show znboobmouth with vpunch
zn "Ah~!"
mc "That's more like it."
show znboobmouth with vpunch
zn "Shtoph- Ah~"
menu:
    "Continue":
        show znboobmouth with hpunch
        zn "Hah~! Pleash...~"
        show znboobmouth with hpunch
        zn "S-Shthop~! Ah~!"
        show znboobmouth with vpunch
        zn "N-Not like th- AH~!"
        scene znboobgrope
        show znboobfing with vpunch
        mc "Heheh... That's enough, I'm satisfied. You can eat."
        scene znboobnude
        show znboobshy
        show znboobeyeside
        "Unlike the other times, she doesn't immediately start eating. She has one of her hands between her legs as if to stop something from leaking."
    "Stop":
        mc "{i}That's enough teasing for now."
        mc "Alright, I'm satisfied. You can eat."
        scene znboobnude
        show znboobshy
        show znboobeyeside
        "Unlike the other times, she doesn't immediately start eating. Her breath is heavy and when you look down at her legs..."
mc "{i}Heh, so sensitive."
scene shackinteriorb with fade
"As soon as she regains composure she starts eating and once again you leave."
mc "Goodbye, toy."
zn "G-Goodbye, master."
mc "{i}Oh, I like the sound of that. She's definitely improved..."
$ lastAte = 0
$ zenS = 5
$ time += 1
jump home



label zen5Menu:
show prot normal
if lastAte >= 3:
    zn @talk "I-I'm really hungry master..."
menu:
    "Give her the gifts" if zenbag == True and zenbooks == True and zenmattress == True and gaveZBag == False:
        hide screen hud
        jump zen5C
    "Talk":
        if asked4gift == False:
            jump zen5A
        elif gaveZBag == True:
            znr @smilet "Thank you for the gifts, master, you're very kind."
            mc @smilet "You deserved them for being obedient. Didn't I tell you that's how you'd get on my good side?"
            znr @smilet "You're right, master. I'm sorry for not understanding earlier."
            mc @smilet "It's alright."
            jump zen5Menu
        else:
            mc @smilet "How are you?"
            if lastAte >= 3:
                znr @angryt "I'm hungry."
                mc @talk "Ah, I see."
                jump zen5Menu
            znr @talk "Still bored."
            mc @angryt "...I'm working on it."
            jump zen5Menu
    "Feed":
        hide screen hud
        mc @talk "Goodmorning, toy. Hungry?"
        znr @talk "Yes, master."
        mc @smilet "That's nice to hear. I brought lots of tasty food just for you."
        "Zenelith looks down and takes a deep breath, then she takes off her top."
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
                "Once you let her be she doesn't immediately start eating. One of her hands is between her legs to stop something from leaking."
            "Stop":
                mc "{i}That's enough teasing for now."
                mc "Alright, I'm satisfied. You can eat."
                scene znboobnude
                show znboobshy
                show znboobeyeside
                "Once you let her be she doesn't immediately start eating. Her breath is heavy and when you look down at her legs..."
        mc "{i}Heh, so sensitive."
        scene shackinteriorb with fade
        "As soon as she regains composure she starts eating and once again you leave."
        mc "Goodbye, toy."
        zn "G-Goodbye, master."
        $ lastAte = 0
        $ time += 1
        jump home


label zen5A:
mc @smilet "Hey there, Zen. How are you?"
znr @talk "Are you really interested in that, master?"
mc @talk "I was trying to be nice."
znr @talk "Sigh. Well, I'm bored. I spend all day here doing nothing waiting for you to come for anything to happen."
mc @smirkt "We can have more fun together if you insist."
znr @angryt "I... appreciate the offer, master but I was talking about when I'm alone."
mc @talk "I see."
mc "{i}Hm... I guess she's not totally wrong. She might die from boredom if she just spends all her day by herself in a cabin that has nothing outside rubble..."
mc @smilet "Would you like something in particular?"
znr @talk "Huh?"
mc @normal "I'm asking if you want me to bring you something."
znr @smilet "R-Really? I'd appreciate that so much..."
mc @normal "Yes, yes but what would you like?"
znr @talk "Uhm..."
"Zenelith looks up at the ceiling and for a second you see her smile satisfied but it quickly fades away as she looks back at you."
znr @talk "Maybe a book or two... And, you know the camp where you found me? Well, when we left I forgot to take with me my bag."
mc @questiont "Your bag?"
znr @talk "Yes, I had a bag full of gems... I, uhm, kept them for... personal reasons. Memorabilia, yes."
mc @questiont "Memorabilia, huh?{p}...Alright, I'll see what I can do."
znr @smilet "Thank you very much master."
mc "{i}Mh... Maybe I should get her a bed as well. That way when she finally gives in to sex we'll have a place to do it."
$ asked4gift = True
jump zen5Menu

label zen5B:
scene forrest
hide screen hud
"You walk through the forest for a few hours trying to find Zenelith's old camp but it's proving to be real difficult."
mc "{i}Is this really worth it? It's literally just a bunch of rocks..."
"But as you question what you're doing, you stumble right in the camp where Zenelith was."
mc "{i}Oh well, I'm here now anyways."
"It takes you very little to find the bag. You check inside and there's indeed just pieces of gems and some random wood pieces as well. It doesn't weight too much so you decide to carry it all back with you."
if zenbooks == True:
    mc "{i}Alright, I've got everything. Let's hope that by doing this she'll become more compliant..."
else:
    mc "{i}Alright, now I just have to get her some books... Hopefully by being nice she will become more compliant."
$ time += 1
$ zenbag = True
jump home

label zen5C:
mc @smirkt "Guess what I've got for you?"
znr @talk "...No way."
mc @smilet "Yup."
"You take the books and zenelith's gems from your backpack and show them to her. She smiles but for a brief moment more than a happy smile it looks like a mischevious smile."
znr @smilet "Thank you very much, master."
"Zenelith goes to take the gifts from you hands but you move them closer to you."
mc @talk "I didn't say I am going to give them to you."
znr @angryt "Huh?"
mc @smirkt "I am being extra generous to you, so I want something more than the usual from you."
show znrag angry
znr @angryt "...What do you mean?"
mc @smirkt "Get all naked."
znr @angryt "Wh-What?!"
mc @angryt "It's an order."
zn "..."
znr @angryt "F-Fine."
stop music
scene znfingerbase1 with fade
zn "H-Happy now?"
mc "Not yet."
zn "W-What? What else do you want?"
scene znfingerbase1
show znfinger0 with dissolve
pause 1
mc "This."
zn "W-Wait! What are you-"
scene znfingerbase2
show znfinger2 with vpunch
zn "AH~!"
hide znfinger0
hide znfinger2
show znfinger1
mc "Heh. Look how wet you are."
zn "P-Please stop."
mc "No, I don't think I will."
"You don't give her time to reply as you start moving your fingers again."
show zenfingering1
zn "Mnh~ S-Stop!"
"You don't pay attention to her plead and instead smile as each little moan escapes her mouth with another movement of your hand."
zn "Ahmn~... Ngh..."
mc "{i}Let's make this a bit better for her~"
hide znfinger1
hide znfingering1
show zenfingering2 with vpunch
zn "Wha- ANH~! Ah~!"
mc "Better, isn't it?"
zn "I- mnh~! I'm gonna-"
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
mc "Wow, you really came a lot."
zn "Mnh... Y-You b-bastard..."
mc "I'd normally punish you for calling me that but I'll let it pass just because I love the look on your face right now."
zn "You..."
mc "And since you didn't resist at all while I did all that, you've deserved to have your gifts as well. Here."
scene shackinteriorb with dissolve
"You leave the books and the bag on the floor next to her. It takes her a while to recover but she manages to regain her composure and look inside the bag. She stares at the content for a few seconds and then smiles."
"You then go outside and take the mattress inside. She looks at you in awe while you put the mattress on the floor. It really is quite big."
zn "Master... Thanks."
mc "You're welcome."
$ gaveZBag = True
$ persistent.fingerZen = True
scene shackinteriors with dissolve
show screen hud
show znrag normal
jump zen5Menu

label zen5F:
scene zenelithshack
hide screen hud with dissolve
show zenss1 with fade
mc "{i}I wonder... What could I have her do today? She already let me finger her... I wonder if she's already willing to blow me off."
"As you get closer to the shack, though, something feels off. You can't quite put your hand on it but..."
mc "{i}Wait. Why are two of the seals turned off?!"
"Without a second thought you rush inside the shack. Could it be that her magic finally started working again?"
stop music
scene shackinteriors with flash
show prot angry
"And there you find her. On the floor with the stones from the bag arranged in a very familiar shape in front of her."
mc "{i}Wait a second-"
show znrag satis with dissolve
znr @angryt "Hah. Look who showed up."
mc @angryt "So those were actually the pieces of your staff, huh?"
znr @angryt "Yes. And now I can finally use my magic again."
mc @smirkt "Then you shouldn't have wasted time talking."
znr @angryt "What-"
hide znrag satis
show znrag angry with hpunch
hide znrag angry with easeoutleft
"You jump towards Zenelith. She doesn't have enough time to cast a spell that you've already pushed her aside and took her makeshift staff away from her."
mc @talk "Pathetic."
zn "Y-You!"
mc @talk "I guess having a slave for 160 years hasn't taught you what happens when a slave tries to run away."
"With your foot you crush her staff, rendering it useless once again. She tries to protest but you don't listen to her."
mc @smilet "And now I'm going to teach you a lesson."
zn "H-Huh?"
"You walk over to Zenelith and she steps back, unfortunately the wall blocks her from going further."
mc @angryt "Take those off and turn around."
zn "W-What?"
mc @angryt "You heard me."
zn "..."
"At first you think she isn't going to undress but surprisingly she starts stripping and once she's naked she turns around."
scene zenspankpre1 with fade
pause 1.5
zn "P-Please be gentle..."
mc "Would you've been gentle to Morgan if he did the same?"
zn "..."
mc "You know maybe I won't be satisfied regardless of what I do to you.{p}...Maybe I should kill you for trying to trick me."
scene zenspankpre2 with dissolve
zn "N-No! Please I don't want to die!"
mc "Tsk."
scene zenspanking with hpunch
pause 0.4
scene zenspank1
zn "Ngh!"
mc "You don't want to die, huh?"
scene zenspanking with hpunch
pause 0.4
scene zenspank2
zn "I don't! I'm sorry!"
mc "I don't think you are."
scene zenspanking with hpunch
pause 0.4
scene zenspank3
zn "P-Please!"
mc "Keep begging, slut."
scene zenspanking with hpunch
pause 0.4
scene zenspank4
zn "I-I'm sorry... M-Master, please stop..."
scene zenspanking with hpunch
pause 0.4
scene zenspank5
mc "No."
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
zn "Ahn~"
mc "...You're moaning? This turns you on? Disgusting."
zn "M-Master please, I-I'll do anything..."
mc "Anything?"
zn "Y-Yes, please..."
mc "..."
mc "Goodbye, toy."
zn "N-No wait!"
scene zenelithshack with fade
mc "{i}Time to re-apply all the seals..."
scene zenss with dissolve
zn "M-Master please... Don't leave me..."
mc "{i}Oh, I'm not leaving forever... I'll leave her alone for only a week. When I'll be back she'll have definitely learned the lesson if she's still alive."
zn "M-Master! Come back please!"
mc "{i}God, she's annoying."
zn "W-What do you want me to do? H-How can I convince you?"
mc "{i}Let's just leave..."
$ chargedRune -= 1
$ persistent.zenSpank = True
$ zenS = 6
jump home

label zenLateturn:
scene zenss with fade
"You knock on the door of the shack."
mc "I'm back toy."
scene zenss
pause 1
"...Silence."
mc "Toy?"
"Still no answer."
mc "I'm getting angry, Zen. If you don't answer I'll get in and teach you another lesson."
"Again, she doesn't answer. You can't even hear the creaks of the floorboards."
mc "Alright, that's it."
scene shackinteriors
"You undo the seal and storm inside, ready to teach her a lesson, yet when you get in she's on the floor. Motionless."
mc "Zen?"
"You tap her lightly with the foot. She doesn't flinch."
mc "Uh..."
"You get down on your knees and put a finger in front of her mouth. She isn't breathing.{p}You nervously touch her neck. She's cold and you can't feel her heartbeat."
mc "God damn it."
scene zenelithshack
"You quickly get up and walk outside. You know it's your fault she's dead."
menu:
    "She deserved it.":
        "But after all, she deserved to suffer. She's probably lucky she managed to die before you could do anything worse to her."
        mc "...Tsk. I guess I've got something less to worry about at least."
        "You leave her there and go home. You decide you won't come back."
    "She didn't deserve it.":
        mc "Even for what she's done... She didn't deserve a death like this. It's too cruel even for me."
        mc "Sigh... Well, whatever. I guess she managed to avoid what I wanted to do with her."
        "You decide to leave her there and go home. There's no reason to stay or come back."
$ zenRouteEnd = True
$ chargedRune -= 1
$ time += 1
jump home

label zenReturn:
hide screen hud
mc "{i}It's time."
"Before you leave to the shack you take with you food for Zenelith. If she does everything you ask her maybe she'll deserve to eat it."
scene zenss with fade
mc "{size=-3}...I'm back."
"..."
mc "{i}I don't know why I expected someone to answer after whispering that."
"You decide to start getting closer to the cabin."
zn "{size=-7}Master...{/size}{p}{size=-5}Master come back...{/size}{p}{size=-3}come back...{/size}{p}{size=-2}master...{/size}{p}"
mc "{i}Oh, I see, she's gone insane, great."
mc "I'm here."
scene zenss with vpunch
zn "{size=+5}Master!"
mc "Stop shouting. If you attract any monster I won't hesitate to use you as meat shield."
zn "{size=-3}Y-Yes master."
mc "Good. I'm coming in then."
scene shackinteriors with fade
"You get inside and there she is, kneeling still on the bed, she looks at you uncertain of what's going to happen."
mc "So, toy, have you understood the lesson?"
zn "Y-Yes, master."
mc "I hope something like this won't happen again."
zn "I-It won't, master."
mc "{i}She at least sounds more complacent... Let's see how obedient she is now."
mc "Are you hungry?"
zn "...Yes, master."
mc "Good, I've got just the thing for you then. Sit down.{p}...Naked."
zn "Y-Yes."
scene bjanimstart with fade
pause 2
mc "{i}Just how I like 'em."
mc "I don't think I need to tell you but... Don't try biting."
zn "Y-Yes..."
mc "Perfect. Now open your mouth wide."
"She opens her mouth as you slowly lower your pants. She doesn't flinch when you take your dick out."
scene zenbj with dissolve
pause 1
mc "{i}H-Holy fuck, this feels amazing... I guess her mouth is good for more stuff other than talking shit."
mc "You're doing a great job taking it, toy. Keep going like this.."
mc "{i}Sure, she still looks like she wouldn't mind killing me but... Heh, she has clearly understood who's the boss."
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
zn "..."
mc "{i}That wasn't bad but I haven't heard her squel like she usually does..."
mc "{i}I want something more, like..."
mc "...Get on the bed."
zn "...?"
mc "Now."
"She gets on the bed and then, without hesitation, you push her down."
scene zenpress with fade
pause 1
zn "W-Wait~!"
mc "Shut up and take it, slut."
scene zenpress with dissolve
pause 3
zn "M-Master...~"
mc "What?"
zn "Pl-Please... u-use me as much as you w-want~!"
mc "I'm already doing that."
zn "Mnh~!"
scene zenpress with dissolve
pause 2
zn "Ahh~!"
mc "{i}God- She's so tight! How is she over 400 years old?!"
scene zenpress with dissolve
pause 1.7
zn "Ngh~! M-Master I-I'm...!"
scene zenpress with hpunch
mc "Well, I'm not."
zn "Y-Yes! K-Keep going~!"
scene zenpress with dissolve
pause 4
zn "Mnh~"
mc "You're so tight--"
mc "I-I'm almost there..."
scene zenpress with dissolve
pause 0.7
mc "I'm cumming!"
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
mc "Ah... Much, {b}much{/b} better."
zn "M-Master..."
mc "...You're forgiven, toy."
zn "Th-thanks~"
scene shackinteriors with fade
"Not soon after Zenelith passes out. She probably used too much energy."
"You sigh and get up. You leave her there with some food next to her and leave. From now on you'll be back and you know she'll listen to all your requests."
mc "{i}Heh, I really am the luckiest. I get to fuck her whenever I feel like so."
$ zenS = 7
$ chargedRune -= 1
$ persistent.zenReturn = True
$ time += 1
jump home




label zFirstAnal:
hide screen hud
mc @talk "Alright, get on the ground. Now"
znr @talk "Yes, master."
"She gets on all fours on the ground. This is new but she thinks she knows what's going to happen. She takes off her clothes and waits."
scene znanalbase with fade
zn "C'mon master, I can't wait for it any longer~"
mc "...Let's try something new."
zn "Oh?"
scene znanalbasemc with dissolve
mc "Let's try this hole today."
zn "Mh?-"
scene znanalanim with dissolve
"You give her no time to say anything that you're already inside of her ass, thrusting in and out of her."
zn "OH GOD~! YES!"
"You can feel her shiver with pleasure with each thrust, her lewd pants and, every once in a while, you hear her let out a satisfied giggle."
scene znanalanim with vpunch
zn "Fuck... me... Harder~!"
mc "{i}Look at her... To think just some weeks ago she wanted to leave."
zn "Mess my insides master~!"
scene znanalanim with hpunch
zn "OH~!"
scene znanalanim with hpunch
zn "AHN~!"
mc "{i}Oh god... I'm going to cum..."
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
mc "Hah, you really are a slut."
$ persistent.zenAnal = True
$ analDone = True
call ItsFoodOrNothing from _call_ItsFoodOrNothing_first
jump zenMenuC
