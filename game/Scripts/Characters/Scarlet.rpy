default ScarletTalked = 0
default scoldedYouForSkippingClass = False
default classesParticipatedInWhenFirstTalked = 0
default dayWhenClassScold = 200

label Scarlet:
    if findtheaclothes == 1:
        hide screen hud
        mc "Scarlet seems like a safe bet. She taught me that invisibility spell without a second thought."
        mc "Ok... Let's do this."
        scene lecturemage2 with fade
        "You find Scarlet in her classroom reading a book, and making notes for a study plan. She notices you walk in and looks up at you with a smile."
        show smilemc
        scene lecturemage3
        s "[mc]! I was just thinking about you. Are you wanting to learn any extracurricular spells for your \"stealth missions\"?"
        "She giggles and looks back down to her notes."
        s "I actually found this interesting spell that will make you-"
        mc "Uhm... no, I actually had a favor to ask of you Ms... I mean Scarlet."
        "Scarlet looks up again and closes her book. She leans forward on her desk."
        s "What can I do for you, sweetie?"
        mc "{i}Ahh... I can almost see right down her shirt... is she doing this on purpose?"
        mc "Uhm... well... I... "
        "Scarlet's smile widens as she watches you."
        mc "I need some of your clothes..."
        "Scarlet's smile doesn't move an inch. She looks at you coyly."
        scene lecturemage1
        show smilemc
        show normalm
        show talkwam
        s "Hrm... I have to admit, I wasn't expecting that one. Why do you need them?"
        mc "{i}She took that... well? I'm not sure what I was expecting... Now, how should I handle this?"
        menu:
            "Be honest":
                mc "To be honest Scar, I went on an adventure to Yorkel and saved a girl. The town was destroyed and she has nothing left. She needs a few change of clothes."
                show sadtalkm
                s "...Wow... That poor girl..."
                s "{i}Why am I both disappointed and delighted? He's so sweet."
                s "Of course [mc], I'll leave some clothes in your desk tomorrow. Give that poor girl my regards, ok?"
                mc "{i}That was remarkably painless..."
                mc "Thank you, Scar. I'll be leaving now, I gu-"
                show anythingm
                s "Oh, but you'll owe me a favor someday."
                hide smilemc
                show talkwanmc
                mc "What?"
                s "You'll owe me one. My clothes are really nice, and I'm not going to force a girl down on her luck to owe me anything."
                mc "What do you want?"
                s "Oh... I haven't decided yet. I'll get back to you on that."
                "Scarlet winks."
                s "Go on now! I think class is starting soon!"
                mc "Ok then... Bye, Scarlet..."
                s "Bye, [mc]..."
                s "I love making that boy squirm..."
                "You leave the room with a sense of dread. Wondering what \"favor\" lies ahead in your future."
                $ theaclothestimer += 1
                $ findtheaclothes +=1
                jump academy
            "Lie about it":
                mc "Well... you see... I..."
                show normalm
                "Scarlet stares through you."
                show wasmilem
                show talksadhappymc
                mc "I mean... I'm learning how to be a tailor, just in case adventuring doesn't work out, so..."
                "Scarlet continues to stare. Somehow smiling even wider than before."
                mc "So I need some clothes...to hem... for practice... just in case..."
                "Scarlet stares at you. The silence is deafening. You think you are about to crack under the pressure, when she suddenly bursts into laughter."
                show lolm
                s "Hahaha!!! [mc], you are a monumentally bad liar, you dolt!"
                "She continues to laugh as you feel your pride slowly disintegrate."
                s "Oh wow... haha... I needed that. Okay, [mc]. Just for the good laugh, I'll give you some clothes to \"hem\". But if you are considering an alternate career path. May suggest becoming a jester. You are hilarious!"
                mc "Thanks, Scarlet..."
                "Scarlet laughs again while you consider leaving."
                hide lolm
                show talkwam
                show thinkmc
                s "I'll drop them off in your desk tomorrow, sweetie. They won't be anything fancy, so don't get too... excited... about them."
                mc "No, it isn't for anything like that..."
                s "Sure, sure [mc], I {b}totally{/b} believe you."
                "Scarlet winks at you."
                s "You should get going, class is going to start soon, I believe."
                mc "Thanks, Scar."
                s "Don't do anything I wouldn't do with them!"
                "Scarlet begins to laugh again as you exit the classroom. "
                mc "Wow... that could have gone better... at least I have the clothes for Thea..."
                $ theaclothestimer += 1
                $ findtheaclothes +=1
                jump academy
    hide screen hud
    scene lecturemage1
    show talkhappymc
    show normalm
    mc "Hello."
    hide talkhappymc
    show smilemc
    show talkwam
    s "Hey there, ki-... I mean, [mc], what's up?"
    menu:
        "Talk":
            mc "Just came for a chat."
            if time < 3:
                s "Sorry, [mc], I've got another class right now, come back later."
                mc "Alright, see ya."
                jump academy
            if ScarletTalked == 0:
                $ classesParticipatedInWhenFirstTalked = wentToClassEver
                $ dayWhenClassScold = day
                s "Aw, how nice. You {i}are{/i} warming up to me, then."
                mc "Yeah, yeah, I am."
                s "Then tell me, how's it all going? Are you having fun at the Academy?"
                menu:
                    "It's going well":
                        if wentToClassEver == 0:
                            s "Oh, I bet it is. You've been skipping my class since forever."
                            mc "Oh, uhm..."
                            s "It's fine, [mc], it's fine. I get that you're too shy to come to my classes, being friends with the teacher might be embarassing."
                            mc "Wh- That's not the reason!"
                            s "Hahaha, I know, I know. Look how red you are~"
                            mc "Oh, shut up."
                            s "Fine, fine."
                            $ scoldedYouForSkippingClass = True
                        elif wentToClassEver < 3:
                            s "I'm glad... Though you could come to class more often."
                            mc "O-Oh, yeah, sure, I... should."
                            s "...You seemed much more excited on your first day than you are now, what happened?"
                            mc "I don't know I guess I just... focused more on adventuring."
                            s "Sigh, I can't blame you. When I was young, I also skipped school to go on adventuring, just be careful at least."
                            mc "I will, I will."
                            s "Wouldn't want you to get beaten up by a boar."
                            mc "Yeah, yea- Hey! How bad do you think I am?"
                            s "I mean... You're pretty small, [mc], and slim... You don't exactly {b}look{/b} strong."
                            mc "Well, appearance deceives."
                            "Scarlet smirks and gets closer to you, putting a hand on your chest."
                            s "Sure... I can sense all your tough manly muscles with my fingers."
                            mc "S-Shut up."
                            $ scoldedYouForSkippingClass = True
                        else:
                            s "That makes sense, you've been coming to my class pretty often."
                            mc "Yup, I really am a model student."
                            s "...Though I've seen you paying more attention to the girls in class than the actual lesson."
                            mc "Huh?"
                            s "Don't lie to me, [mc], I've only seen you talking to girls here at the Academy. You're a full-on womanizer."
                            mc "What the hell?!"
                            s "Pfft- Hahaha! I'm just messing with you. Look how red you are~"
                            mc "Sh-Shut up."
                    "It's not going too well":
                        if wentToClassEver == 0:
                            s "Well that makes a lot of sense. You've been skipping classes since forever."
                            mc "Oh, uhm..."
                            s "It's fine, [mc], it's fine. I get that you're too shy to come to my classes, being friends with the teacher might be embarassing."
                            mc "Wh- That's not why I-"
                            s "Heh, I know, I know, I was just messing with you. Look how red you are~"
                            mc "S-Shut up."
                            s "Fine..."
                            $ scoldedYouForSkippingClass == True
                        elif wentToClassEver < 3:
                            s "Oh well... Maybe you should come to school more often."
                            mc "O-Oh, yeah, I probably should."
                            s "...You seemed much more excited on your first day than you are now, what happened?"
                            mc "I don't know I guess I just... focused more on adventuring."
                            s "Sigh, I can't blame you. When I was young, I also skipped school to go on adventuring, just be careful at least."
                            mc "I will, I will."
                            s "Wouldn't want you to get beaten up by a boar."
                            mc "Yeah, yea- Hey! How bad do you think I am?"
                            s "I mean... You're pretty small, [mc], and slim... You don't exactly {b}look{/b} strong."
                            mc "Well, appearance deceives."
                            "Scarlet smirks and gets closer to you, putting a hand on your chest."
                            s "Sure... I can sense all your tough manly muscles with my fingers."
                            mc "S-Shut up."
                            $ scoldedYouForSkippingClass == True
                        else:
                            s "That's weird, you've come to my class often enough..."
                            mc "Yeah, I guess..."
                            s "...Unless you've been zoning out in every class looking at pretty girls."
                            mc "Huh?"
                            s "Don't lie to me, [mc], I've only seen you talking to girls here at the Academy. You're a full-on womanizer."
                            mc "What the hell?!"
                            s "Pfft- Hahaha! I'm just messing with you. Look how red you are~"
                            mc "Sh-Shut up."
                s "...It's fun teasing you though."
                mc "Just because you used a spell to rejuvenate yourself doesn't mean you can act like a teenage girl."
                s "What do you mean? Old ladies tease the young all the time."
                mc "Sure thing, mom."
                s "Heh..."
                "..."
                mc "{i}Uhm... She's got quiet all of a sudden."
                mc "So..."
                s "Huh? Oh! Sorry, my mind wandered off for a second."
                mc "..."
                s "Well, that's enough talking, you little brat. I need to go back to work."
                mc "Alright, see ya."
                s "See ya."
                "She ruffles your hair, you protest and walk away from her grasp, but your hair has already been messed up."
                jump academy
            if ScarletTalked == 1:
                if scoldedYouForSkippingClass == True and wentToClassEver > (dayWhenClassScold-day)/4+classesParticipatedInWhenFirstTalked:
                    s "Well, well, let me say then that I'm very proud of you."
                    mc "You are?"
                    s "Yeah, you've actually started coming a bit more often to class. I'm glad."
                    mc "Well what else am I supposed to do? Just drop out?"
                    s "You'd be surprised how many students don't show up to classes anymore."
                    mc "Really? That many?"
                    s "Yeah, apparently since the Demon King was slain people started taking the whole war less seriously... Which is a problem considering that the Demon Army seems to be building up strength again."
                    mc "Well, I spend my time outside of school doing adventuring stuff. So even if I dropped out, I'd still be prepared to fight the Demon army."
                    s "Yeah, I guess you're right, but not everyone stops coming to be an Adventurer."
                    mc "Mh."
                elif scoldedYouForSkippingClass == True and wentToClassEver < (dayWhenClassScold-day)/4+classesParticipatedInWhenFirstTalked:
                    s "You know, it's a shame you haven't started coming often to school, I feel like you'd be a really good student."
                    mc "Would I?"
                    s "Your uncle says so."
                    mc "W-Wait, you spoke with my uncle?"
                    s "I'm your teacher and you have been skipping a lot of classes, of course I have."
                    mc "Oh no... He's definitely angry now."
                    s "Don't worry, [mc], he's not angry."
                    mc "He's not?"
                    s "C'mon, kid, at least you skip class to be an Adventurer. I can't fault you for that. I was an Adventurer for most of my life and look how I ended up."
                    mc "...in a school teaching teens?"
                    s "W-Well, yes..."
                    mc "..."
                    s "B-But what I mean is that I still ended up fine. As long as you apply yourself in something you're going to end up fine."
                    s "Also, don't tell your uncle I told you this, but going on quests is much more fun than being in a school."
                    mc "Hah, I won't tell him, don't worry."
                    s "Good, good."
                s "So, what has my favorite student been doing recently?"
                if bronzebadge == True:
                    mc "Nothing much, I don't think I've told you but I've recently become a Bronze-Rank Adventurer."
                    s "Really? That's great [mc]! How long have you been an Adventurer for?"
                    mc "Since I started the Academy."
                    if day < 21 or dayWhenBronze < 20:
                        s "It's not even been three weeks! Guess we got a prodigy here."
                        mc "Oh c'mon, don't make me blush. Anyone could've done it, it was pretty easy."
                        s "Well, you're not wrong. It {b}is{/b} the easiest rank to achieve, but it's still something to be proud of."
                        mc "Thanks."
                        s "...Though it {b}did{/b} only take me 5 days when I got it."
                        mc "What?! How?!"
                        s "Heheh."
                    elif day < 21 or dayWhenBronze == 500:
                        s "Well, it took you some time didn't it?"
                        mc "Well, it's not like I got the badge yesterday."
                        s "Have you, now?"
                        mc "Yes! I've had it for a while!"
                        s "Alright, alright, I believe you."
                    else:
                        s "Oh, I see. That's really cool."
                        mc "Yeah I've been having lots of fun."
                        s "What level are you now?"
                        mc "I'm level [level]."
                        s "Nice. I'm proud of you."
                        mc "Uhm, thanks."
                else:
                    mc "I've been training."
                    s "Training?"
                    mc "Yeah, I am trying to get to Bronze-Rank so that I can join a party."
                    s "Oh, that sounds neat. You already know who's going to join you?"
                    mc "Well, not exactly. It's me who's going to join {b}them{/b}."
                    s "You say that as if it changed much. It's normal for parties to grow over time."
                    mc "I guess you're right."
                    s "I know I am. I was the last one to join the party I was in when I was an Adventurer."
                    mc "So... you were the newbie."
                    s "...Don't call me that."
                    mc "Sure thing, newbie."
                    s "You know I can turn you into a frog if I wanted to, right?"
                    mc "I'm sorry, I'm sorry."
                    s "Good."
                s "Alright, that's enough talking. I gotta go now."
                mc "See ya then."
                s "See ya."
                jump academy
            if ScarletTalked > 1:
                s "Sure, I've got some time to spare."
                mc "There's one thing I was meaning to ask."
                s "What is it?"
                mc "You're single, aren't you?"
                s "..."
                s "Am I supposed to take that as a hint for something?"
                mc "What- No. Don't- I didn't mean it like that."
                s "Did you?"
                mc "I didn't!"
                s "Sure."
                mc "..."
                mc "I asked because I haven't seen anyone with you and it's weird a 53-year-old mage would be single."
                s "...I liked my interpretation more."
                mc "You're avoiding my question."
                s "I'm not."
                mc "You are."
                s "Nuh-huh."
                mc "So, you {b}are{/b} single."
                s "...I am."
                mc "So... Is that why you de-aged yourself?"
                s "Wh- No! I'm not that desperate."
                mc "You did try to flirt with me when we met, though."
                mc "{i}And sometimes I think you still are..."
                s "No, I wasn't! I was just being nice."
                mc "Yeah... \"nice.\""
                s "You'll get it when you're my age."
                mc "I don't think I will."
                s "Get out of here before I turn you into a frog, you brat."
                mc "Byeee."
                s "Bye-bye."
                jump academy
        "Ask Scarlet about the rune" if zenS == 1 and scarletCharge == False:
            hide screen hud
            show prot smile
            show normalm
            mc @smilet "Remember the rune you gave me?"
            show talkwam
            s "Yeah?"
            hide talkwam
            mc @questiont "When it gets lighter... Does it mean its magic faded?"
            show talkm
            s "Well, sort of. It means that the mana it was infused with has been used up."
            hide talkm
            mc @smilet "I see. Then... Could you recharge my rune?"
            show talkwam
            s "...You encountering that one seal a lot?"
            hide talkwam
            mc @hopet "Well... yeah. There's this elven priestess that's been doing lots of bad things and she uses this seal a lot to protect her stuff."
            show talkm
            s "I see... Well then, sure. I'll recharge it for you, and if it depletes again, just come pay a visit again."
            hide talkm
            mc @smilet "Really? Thanks, Scar!"
            show talkm
            s "Heheh."
            hide talkm
            scene black with dissolve
            show text "{color=#fff}Scarlet recharges the rune." at truecenter
            pause 1
            hide text with dissolve
            scene lecturemage1 with dissolve
            show prot smilet
            show normalm
            mc @smilet "Wow, it's heavy again."
            show talkm
            s "I know, right?"
            hide talkm
            mc @smilet "Anyway... I'll go now. See ya."
            show talkwam
            s "Huh? Oh- Okay, see ya."
            hide talkm
            hide prot smile with easeoutright
            "You quickly make your way out of the academy."
            $ chargedRune = 8
            $ scarletCharge = True
            show screen hud
            jump home
        "Ask Scarlet to recharge the rune" if zenS >= 1 and chargedRune < 1 and scarletCharge == True:
            hide screen hud
            show prot smile
            show normalm
            mc @smilet "Hey there Scarlet. Can you recharge the rune?"
            show talkwam
            s "Again?"
            hide talkwam
            mc @smilet "Yup."
            show talkm
            s "Alright."
            hide talkm
            scene black with dissolve
            show text "{color=#fff}Scarlet recharges the rune." at truecenter
            pause 1
            hide text with dissolve
            show text "{color=#fff}...She then forces you to talk with her for 15 minutes." at truecenter
            pause 1
            hide text with dissolve
            scene lecturemage1 with dissolve
            show prot smilet
            show normalm
            mc @smilet "I gotta go now, Scar. Thanks again for recharging the rune."
            show talkm
            s "It's nothing, it's a good excuse to chit chat."
            "You wave at Scarlet and leave the classroom."
            $ chargedRune = 8
            show screen hud
            jump home
        "Ask for help with the priestess" if bothpath >= 4 and protectionspell < 2:
            if protectionspell == 0:
                show normalm
                show smilemc
                show talkmc
                mc "Scarlet, I-"
                s "Hold it right there. Are you asking for some favor again?"
                show talksadhappymc
                mc "Uhm, yeah."
                s "I knew it! man, I should start charging you for these types of stuff. I feel like I'm spoiling you."
                mc "Please, Scarlet, I really need your help this time."
                s "......"
                s "Geez, fine. I can't say no to that face."
                mc "Heheh, thanks."
                s "So, what do you want this time, sir?"
                mc "Do you know protection magic I could use?"
                s "Yeah."
                mc "Could you teach me?"
                s "Hmm, what kind of protection spell do you need?"
                mc "What do you mean?"
                s "I mean, what kind of magic do you need protection from? Low class magic, medium class magic, high class magic?"
                mc "Umm, something like... elf magic."
                s "Elf magic! You've been dealing with quite a lot of elves recently."
                mc "{i}I should tell her. She' helped me a lot, she deserves to know."
                mc "If I tell you something, can you keep it a secret?"
                s "Oh, yes! I love secrets."
                mc "Ok."
                "You tell Scarlet the whole story."
                show uhm
                s "I can't believe a priestess would do that. [mc], this sounds serious. Let me go there, I can stop her."
                mc "No! I promised Eve that I wouldn't tell anyone about their village."
                s "Hmm. I see, you have to do it alone then?"
                mc "Yeah."
                s "I understand."
                s "So, [mc], there's some good news and some bad news."
                mc "Ok."
                s "The bad news is, elf magic is really powerful. And I think at your level, it would take at least years until you learn a protection spell to counter elf magic."
                mc "Oh."
                hide uhm
                s "Hold on, I haven't said the good news yet. The good news is, you got yourself a master mage who can put a powerful protection spell on you."
                mc "Really! That's great! Let's get started then, I have no time to lose."
                s "Hold on, mister. I need at least two days to put the spell on you."
                mc "What?! Really?"
                s "Come here."
                "Scarlet touches your forehead with her palm."
                s "Your mana level is too low."
                s "I can't put the spell on you at once."
                mc "Huh, why? I thought my mana had nothing to do with the spell."
                s "It does. Think of it as this way; A scrawny soldier needs to go through an army of orcs. So he's given a very strong armor, but it's heavy. Now, what happens when he wears it?"
                mc "He gets crushed, because the armor is too heavy for him?"
                s "It's the same here. You're the scrawny soldier and the heavy armor is the protection spell."
                mc "Oh, I get it. But why take two days then?"
                s "I need to make the armor as light as possible so you can wear it. That takes time."
                mc "Ah, ok."
                s "I'll start the first phase now, but you'll have to come again if you want the spell to work properly."
                mc "Got it."
                show black with fade
                "Scarlet takes out her staff and chants a spell. She waves her staff and zaps you with a red beam of light. Your body starts to get heavy to the point where you feel like it would sink into the ground."
                hide black
                show worriedmc  with flash
                s "Ok, we're done for today."
                mc "{i}Urgh, my head."
                s "[mc]?"
                mc "I'm fine, just a bit dizzy."
                s "Hahaha. Imagine if I did the whole thing right now."
                mc "Yeah... now I kind get what you said earlier."
                s "Now go home and get some rest."
                mc "Right, I'll be back for the second phase of the spell."
                s "Ok."
                scene academytalkblr
                show worriedmc
                show lookdownsupmc
                mc "{i}Urk... I don't feel so good."
                show normalg with easeinleft
                pause 0.5
                hide normalg
                show talkwagabe
                hide lookdownsupmc
                show sadg
                g "Whoa, [mc]? What's up? You don't look so good."
                mc "Gabe? Y-Yeah, I'm just having a headache."
                g "Is it bad?"
                mc "N-No, I'll manage."
                g "You better go home straight away, [mc]. I'll cover for ya."
                mc "Oh, th-thanks. Yeah, I should go home."
                g "You want me to walk you home?"
                mc "No, no, I'm fine. Thanks."
                g "Ok, be careful now."
                mc "I will."
                scene villageback with fade
                mc "{i}Must get home... must... not... faint..."
                "You somehow manage to get home."
                scene mcroomblur with fade
                show worriedmc
                show talksadhappymc
                mc "{i}sigh{/i} I made it."
                if thealives == 1:
                    show normalth
                    show talknth
                    th "[mc]! You're early today."
                    mc "Oh, hey Thea. Yeah, I wasn't feeling well so I came home."
                    show worriedth
                    th "Oh no, are you sick?"
                    mc "Nah, I'm just tired, that's all."
                    show talksth
                    hide worriedth
                    hide talknth
                    th "You have... been away from home a lot recently."
                    mc "You're right, I've been on this important quest for a while now. I'm sorry, I didn't get a chance to tell you."
                    th "It's ok, I'm sure you've been very busy."
                    mc "Yeah."
                    show gambaruth
                    th "Then I suggest you go to bed straight away!"
                    show normalth
                    mc "Hahaha, I will."
                scene roomnew
                "You fall onto the bed and instantly fall asleep."
                $ time = 4
                $ protectionspell += 1
                jump home

            if protectionspell == 1:
                show normalm
                show smilemc
                show talkmc
                s "So, are we ready for the next phase?"
                mc "Yeah, I hope I'll be able to walk home today."
                s "Hahaha. Don't worry, it won't be that hard today."
                mc "I'll take your word for it."
                show black with dissolve
                "Scarlet zaps you with the red beam again. You somewhat feel less discomfort than the last time."
                hide black
                show thinkmc with flash
                s "Ok! We're done here. How do you feel?"
                mc "Uhm... nothing special."
                s "That means it worked. Now be careful. And remember, the effects of the spell will wear off after some time."
                mc "Got it. Thank you, Scarlet. None of this would've been possible if it wasn't for you."
                s "Awww. Don't mention it [mc], it's been a pleasure."
                mc "See you then."
                $ time += 1
                s "Good luck kid"
                $ protectionspell += 1
                $ bothpath += 1
                jump academy

        "Ask about the seal" if bothpath >= 2 and rightsealspell == 0:
            if spellintroscarlet == 0:
                show normalm
                show smilemc
                show talkmc
                mc "Scarlet, do you know about seals?"
                show talkwam
                s "Uh... yeah."
                mc "See, I found this door while I was on a quest. When I tried to open it, some kind mark appeared and pushed my hands back."
                s "Ah, yes, a doorway seal."
                mc "Yeah, something like that. What are they?"
                s "To put it into simple terms; They're basically magical locks. They can't be broken down by force."
                mc "Oh... so is there no way to break it?"
                s "There is. You can break it with magic, but that takes a lot of mana. The easiest way is to find the right spell and unlock it."
                mc "How do I do that?"
                s "You identify the type of seal by its mark."
                mc "Like the one that appeared when I tried to open the door?"
                s "Exactly."
                mc "Then... can you teach me how to open that door?"
                s "Sure can!"
                mc "Alright. What do I gotta do?"
                s "First, do you remember the mark you saw on the seal?"
                mc "Uhm..."
                s "What kind of door was it? In what region did you find it?"
                mc "It... was an Elven door."
                s "An Elven door, huh? Well, you're in luck. Elves only have 8 seals, so I think you might be able to find it. Wait a minute."
                "Scarlet casts a spell and opens one of her drawers. She takes a book and shows it to you."
                scene sealspellbook with fade
                pause
                s "Here are the 8 signs, can you remember which one it was?"
                pause
                window hide
                menu:
                    "1":
                        mc "The first one."
                        s "Ok."
                        $ wrongsealspell = 1
                        "Scarlet pulls out a small rock and saps it with her staff."
                        jump sealtalk
                    "2":
                        mc "The second one."
                        s "Ok."
                        $ wrongsealspell = 1
                        "Scarlet pulls out a small rock and saps it with her staff."
                        jump sealtalk
                    "3":
                        mc "The third one."
                        s "Ok."
                        $ rightsealspell += 1
                        "Scarlet pulls out a small rock and saps it with her staff."
                        jump sealtalk
                    "4":
                        mc "The fourth one."
                        s "Ok."
                        $ wrongsealspell = 1
                        "Scarlet pulls out a small rock and saps it with her staff."
                        jump sealtalk
                    "5":
                        mc "The fifth one."
                        s "Ok."
                        $ wrongsealspell = 1
                        "Scarlet pulls out a small rock and saps it with her staff."
                        jump sealtalk
                    "6":
                        mc "The sixth one."
                        s "Ok."
                        $ wrongsealspell = 1
                        "Scarlet pulls out a small rock and saps it with her staff."
                        jump sealtalk
                    "7":
                        mc "The seventh one."
                        s "Ok."
                        $ wrongsealspell = 1
                        "Scarlet pulls out a small rock and saps it with her staff."
                        jump sealtalk
                    "8":
                        mc "The eighth one."
                        s "Ok."
                        $ wrongsealspell = 1
                        "Scarlet pulls out a small rock and saps it with her staff."
                        jump sealtalk
                    "Don't remember":
                        $ dontrememberseal += 1
                        mc "Damn it, I can't remember."
                        s "Hmmm... I can't help you then, [mc]. Sorry."
                        mc "Urr..."
                        s "Come back if you remember it."
                        mc "Yeah, I'll try."
                        mc "{i}Damn it, I have to memorize that symbol!"
                        jump academy
            if dontrememberseal >= 1:
                mc "I remember the symbol now."
                s "Wait, let me get the book."
                jump SealBook
            mc "Um, Scarlet? ...That rune you gave me didn't work."
            s "What! No way."
            mc "Yeah, I think I showed you the wrong symbol."
            s "That has to be the reason. So do you remember the correct one?"
            mc "Yeah."
            s "Good, let me get the book."
            jump SealBook


        "Ask about an invisibility spell" if saq == 1 and invisibilityspell == 0 and peekingdone == 0:
            jump wotv2

        "Nothing":
            show talksadhappymc
            hide talkwam
            mc "Nothing really."
            show talkm
            s "What?"
            s "Weirdo."
            jump academy
    return


label SealBook:
 scene sealspellbook with fade
 pause
 menu:
    "1":
        mc "The first one."
        s "Ok."
        $ wrongsealspell = 1
        "Scarlet pulls out a small rock and saps it with her staff."
        s "Here you go."
        mc "Thanks."
        jump academy

    "2":
        mc "The second one."
        s "Ok."
        $ wrongsealspell = 1
        "Scarlet pulls out a small rock and saps it with her staff."
        s "Here you go."
        mc "Thanks."
        jump academy

    "3":
        mc "The third one."
        s "Ok."
        $ rightsealspell = 1
        $ wrongsealspell = 0
        "Scarlet pulls out a small rock and saps it with her staff."
        s "Here you go."
        mc "Thanks."
        jump academy

    "4":
        mc "The fourth one."
        s "Ok."
        $ wrongsealspell = 1
        "Scarlet pulls out a small rock and saps it with her staff."
        s "Here you go."
        mc "Thanks."
        jump academy

    "5":
        mc "The fifth one."
        s "Ok."
        $ wrongsealspell = 1
        "Scarlet pulls out a small rock and saps it with her staff."
        s "Here you go."
        mc "Thanks."
        jump academy

    "6":
        mc "The sixth one."
        s "Ok."
        $ wrongsealspell = 1
        "Scarlet pulls out a small rock and saps it with her staff."
        s "Here you go."
        mc "Thanks."
        jump academy

    "7":
        mc "The seventh one."
        s "Ok."
        $ wrongsealspell = 1
        "Scarlet pulls out a small rock and saps it with her staff."
        s "Here you go."
        mc "Thanks."
        jump academy

    "8":
        mc "The eighth one."
        s "Ok."
        $ wrongsealspell = 1
        "Scarlet pulls out a small rock and saps it with her staff."
        s "Here you go."
        mc "Thanks."
        jump academy
 return


label sealtalk:
    scene lecturemage1
    show talkwanmc
    show normalm
    mc "What's this?"
    show talkwam
    s "A rune."
    mc "What's it for?"
    s "Runes are rather useful, you see. They're how us mages can store a spell for later use. In your case that spell is the one to turn on or off that specific seal you showed me."
    show talkwamc
    mc "Woah, really? I thought I would have to learn a spell or something!"
    s "Normally you do, but... these are elven seals, even some royal mages have a hard time with this sort of stuff."
    mc "So what's special about this rune?"
    s "Well, I already did the hard part so you don't have to. The rune is already enchanted, you just have to hold it in your hand. Easy-peasy."
    mc "Wow. Thanks, Scarlet."
    show teethecm
    s "No problemo, kid. That's what teachers are for. Hahaha."
    show thinkmc
    mc "{i}I thought teachers are supposed to {b}teach{/b} students, not do stuff for them..."
    mc "Say, Scarlet. That book, doesn't it existing make the seals kinda useless? Anyone can open a seal if they've got a copy."
    show teethm
    s "Heh. Good point."
    s "Here's a little secret...{p}This book is one of a kind, the only book in Astylla with all that information."
    mc "What?! And how did you get it?!"
    show talksleepm
    s "Ehhh... Maybe I wrote it myself, who knows."
    mc "No way."
    show talkwam
    hide talksleepm
    hide teethm
    hide teethecm
    s "Now, now. Don't go blabbering this to everyone you meet. It's a secret, ok?"
    mc "Fine."
    s "Good."
    mc "Thank you for this, Scarlet. I'll be going then."
    s "Ok."
    scene academytalkblr with fade
    mc "{i}Ok, I got the spell! Hope it's the right one."
    $ spellintroscarlet += 1
    jump academy
    return
