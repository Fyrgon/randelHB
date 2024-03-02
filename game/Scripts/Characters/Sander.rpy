default sanderStealthTraining = False
default sanderStoppedTeaching = False
default itsNotThea = False

label sanderTalk:
hide screen hud
if time < 3:
    scene agblr with dissolve
else:
    scene agblrevening with dissolve
show talkns
show smilemc
sa "Hey, little man, what's up?"
menu:
    "Give muffin" if aerinmuff == 1:
        show normals
        show smilemc
        mc "Hey, Sander, want a muffin?"
        show smirks
        sa "Oh, yeah."
        mc "Here."
        "Sander eats the muffin."
        sa "Mmm, this is good."
        sa "You baked this?"
        mc "Nope, Aerin made this."
        sa "Oh, really? That elf girl, right?"
        mc "Yeah."
        sa "She got some skills. You know Mary?"
        mc "No"
        sa "Her muffins are as good as these."
        mc "O-Ok."
        sa "Thanks anyway, kiddo."
        mc "Just a small offering to my sensei."
        sa "Hahahahaha."
        $ aerinmuff -= 1
        $ sanderatemuff += 1
        jump guild
    "Where's Eve?" if evelosttimer < 3 and evelost == 1:
        show talkwanmc
        show talksads
        c "Hey Sander, where's Eve?"
        sa "Oh, uhm, hey there... Eve... She hasn't come out of her room ever since she came back."
        mc "Really?"
        sa "Yeah, I think we should give some time."
        mc "You're right."
        jump guild
    "I need the Eye Orb." if ieyeorb >= 1 and needOrb == True:
        show normals
        show talkwanmc
        mc "Sander, I need the Eye Orb."
        show smirks
        sa "Sure, little man. I knew you would need it eventually."
        mc "Huh?"
        sa "I gotta say, those girls in the Academy have some really cute asses. It's no wonder you want to see them a second time."
        mc "Second time? No, no, it's not for that, I need it for something else."
        show talkwas
        sa "Really... What do you need it for?"
        mc "{i}I think there's no harm in telling Sander. He's not part of the village and I think he'll believe me"
        mc "You remember that elf priestess Zenelith at Eve's village?"
        sa "Oh yeah, that hot cow!"
        mc "Uhm, yeah, but it turns out that she has a sex dungeon."
        sa "A SEX DUNGEON?!"
        mc "SHHH!!! ...Yeah, it's a sex dungeon. And guess who she has locked up there."
        sa "Uhm..."
        mc "Aerin's brother!"
        sa "No way! ...Uhm, who's Aerin again?"
        mc "You forgot?! It's Eve's opponent in the duel!"
        sa "Ohhh, the depressed chick. Got it. Didn't her brother disappear?"
        mc "Yeah."
        $ goteyeorb += 1
        sa "Then how come he's in the sex dungeon?"
        mc "......"
        mc "{i}Seriously, is he this dumb?"
        mc "Zenelith must've kidnapped him!"
        sa "Oh, yeah... that could've happened."
        sa "But why?"
        mc "I don't know. The thing is, I need the Eye Orb to show the village people what she's doing."
        sa "Oooooh, nice. I knew that bitch was evil. I wish I could help you out, little man, but I'm not sure if I'll be able to sneak in again. They've probably tighten the security after last time."
        mc "Yeah, it's ok. I can do this on my own."
        sa "That's my little man! Good luck, kid."
        "Sander gives you the Eye Orb."
        if time < 3:
            scene agblr
        else:
            scene agblrevening
        show thinkmc
        mc "Ok, all that's left is to go in there and capture everything. Then the bitch is done for."
        mc "But what if I get caught while I'm down there? I nearly got caught the last time. Should I get some help?"
        mc "She's a strong mage! Fight fire with fire. I guess."
        mc "I'll have to meet Scarlet again. I hope she hasn't got tired of helping me."
        $ bothpath += 1
        $ needOrb = False
        jump guild
    "I did it..." if peekingdone == 1 and sanderquest == 0:
        jump wotv4
    "Nothing.":
        show talksadhappymc
        mc "Oh, nothing, just came to hang out."
        hide talksadhappymc
        show talkns
        sa "Cool. Wanna drink?"
        hide talkns
        show normals
        show talksadhappymc
        mc "No thanks... I don't feel like it."
        show talkns
        sa "Sheesh, ok then. Your loss!"
        jump guild
    "About Gabe" if didtest:
        show talkwanmc
        mc "Hey, Sander, did you meet Gabe recently?"
        sa "Who?"
        mc "Gabe, the girl with the purple hair."
        sa "Oh, Gabe. Yeah, yeah, I met her. She was snooping around here looking for you. She looked very familiar, that's why I talked to her."
        mc "You don't remember where you saw her before?"
        sa "No, but I swear I've seen her somewhere."
        show angry
        mc "She was in the orb, the one I gave you."
        hide angry
        sa "Oh, shit, that's where I saw her! Hahaha."
        mc "You seriously forgot?"
        sa "Yeah, little man. I'm not really good with faces, I'm only good with... bodies."
        show creeps
        sa "Oh yeah, it's all coming back to me. That girl had one golden ass on her."
        sa "If she was naked, I could recognize that ass from a mile a way."
        mc "Y-Yeah, I know."
        hide creeps
        sa "Anyway, who was she?"
        mc "My childhood friend. She went to westian when we were like 10."
        show talkwas
        sa "Westian, huh? Got that vibe from her."
        mc "What vibe?"
        sa "I guess you haven't been to Westian?"
        mc "No."
        sa "All the girls in Westian are like that, very gloomy and dull. I think they call it \'E-mo\' or something."
        mc "Gabe isn't gloomy and dull."
        sa "Well, she's trying to be. She must have tried to fit in at Westian."
        mc "{i}Must have been hard for her. Dull and gloomy, that's the exact opposite of her."
        sa "But I'll tell you one thing; those girls are sex crazed maniacs."
        mc "Really?"
        sa "Yeah, they're always fucking. It's like part of their daily routine. Your friend must have had like a thousand cocks by now, hahaha."
        show angry
        mc "I told you, Gabe's not like that!"
        sa "......"
        show talksads
        hide angry
        sa "I'm sorry, I shouldn't have said that."
        mc "It's fine."
        sa "......"
        hide talksads
        sa "Want a drink?"
        mc "Is that the only thing you do?"
        sa "Uhm, yeah, beside baking."
        show talkwamc
        mc "Baking?"
        show talks
        sa "Huh? I said \"making\", I-I'm making things; weapons and stuff."
        mc "O-Ok."
        mc "I'll see you later then."
        hide talks
        sa "Ok, bye, little man."
        jump guild
    "About you and Eve" if sequest1 >= 1:
        show talkwamc
        mc "So what's up with you and Eve?"
        sa "What do you mean?"
        mc "Are you guys dating?"
        sa "......"
        show talkwaecs
        sa "Hahahahha!"
        sa "How the hell did you come up with that?"
        mc "What? The two of you are always together, so I thought maybe-"
        sa "We were banging?"
        mc "No... I mean, kinda, yeah."
        sa "Oh, little man. Eve and I are friends, she's even like a big sister to me."
        mc "But you spy on her."
        sa "That's totally different! Little man, peeping on someone and being in an relationship with someone are totally different things, Hahah! Loving someone takes dedication and effort which I lack. So, for me it's only peeping and perving."
        mc "When you put it that way, I guess you're right."
        sa "Of course I am."
        if sanderrel >= 5:
            sa "I'm your sensei, remember?"
            mc "Hahaha, yeah."
        jump guild
    "Help with Thea" if sanderStealthTraining == 0 and theanight == True:
        jump firstStealthTraining
    "Stealth Training" if sanderStealthTraining == True and sanderStoppedTeaching == False:
        if sanderevedinner == 2:
            if itsNotThea == False:
                call isItThea
        if time == 2 or time == 3:
            show talkwamc
            mc "I'm ready for more training."
            sa "Great. Let's go!"
            play music forest
            show animationsandertraining
            if stealthlvl >= 3:
                "You slowly sneak towards Sander. You watch your step avoiding leaves and debris. Just as you almost touch the apple Sander quickly pulls it away."
                sa "Almost. Not bad, kid, keep going at it."
                if TheaMolest == True:
                    mc "{i}This is probably enough to do anything I want to Thea at night..."
            elif stealthlvl == 2:
                "You slowly sneak towards Sander. You watch your step avoiding leaves and debris. Just as you almost touch the apple Sander quickly pulls it away."
                sa "Almost. Not bad, kid, you're making progress."
            else:
                "You start training with Sander. Sander is still able to notice you."
            $ stealth += 1
            if stealth == 2:
                play sound chime
                $ renpy.notify ("{color=#00C413}Your Stealth has increased.")
                $ stealthlvl += 1
                $ stealth -= 2
            $ time += 1
            sa "That's all for today, kid. Come back tomorrow."
            "You head back home after training."
            jump home
            show talkwamc
        else:
            mc "I'm ready for more training."
            sa "Sorry, kid not now. Come back over in after noon. I'll be free then."
            mc "Oh, yeah. Sorry, I forgot."
            jump guild








label firstStealthTraining:
show blushtalkhappymc
mc "Uhh... Sander, I need some help with, uhm, some... stealth-based things."
show talkwas
sa "Oh... you are in need of sensei's assistance, I see..."
mc "Yeah..."
show creeps
sa "What do you wish to know, young apprentice?"
mc "So... this is completely hypothetical, o-okay? Uhm... let's say there's this girl and- and she's asleep, and someone wanted to-"
show suprised
sa "-Spy on her without waking her up?"
hide suprised
mc "Y-Yeah. How did you know?"
sa "You're talking to the master, child!"
if sanderevedinner == 2:
    call isItThea from _call_isItThea_1
else:
    sa " Come, I shall teach you the way."
"You leave with Sander to the forest."
scene forrest with fade
play music forest
show talkwas
show normalmc
s "Listen up, kid. The thing you need to develop is your stealth. Specifically, how silently you can move. "
"Sander picks up a fallen apple."
s "See this apple? I want you to take it from me."
show talkwanmc
mc "What does it have to do with stealth?"
sa "Well, I'll be covering my eyes. Just pretend that I am asleep and you want to take the apple."
mc "Oohh... okay."
show animationsandertraining
"Sander ties his headband around his eyes."
sa "Okay... Come on, kid!"
"You slowly move towards Sander. When you get close to him, he turns to you instantly."
sa "Come on, kid. I can hear you coming."
mc "What? I came as slow as I could..."
sa "Being slow doesn't mean you're being quiet. You have to be aware of your entire body, where you are stepping and how heavily you are breathing."
sa "Your feet and hands should be as light as a feather."
mc "{i}Why does he sound like he's teaching me something important when in reality he's just teaching me how to molest some folks...?"
mc "Yeah, ok."
sa "Enough training for today, I've got plans for the evening. Come tomorrow evening, we'll train then."
mc "Sounds good."
hide animationsandertraining
$ sanderStealthTraining = True
$ stealthlvl += 1
$ time += 1
jump guild











label isItThea:
sa "Is this girl supposed to be Thea?"
mc "Uhm..."
menu:
    "Tell the truth":
        mc "Y-Yeah."
        sa "Come on, little man. You are diverging off the true path of voyeurism."
        sa "We only observe from a distance, we do not interfere with the freedom of our specimen. We treat it with respect and appreciate its beauty \"from a distance\"."
        sa "Do not be consumed by the dark side."
        sa "Sorry, but I can't help you."
        sa "You think this through again and you will understand the path you have chosen is not the right one."
        mc "......"
        mc "Fine."
        sa "Good."
        $ sanderStoppedTeaching = True
        jump guild
    "Lie":
        mc "No, of course not."
        sa "Alright then."
        $ itsNotThea = True
