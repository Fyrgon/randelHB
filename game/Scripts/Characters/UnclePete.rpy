default peteTalking = 0

label talkingpete:
    hide screen hud
    scene fishhut with fade
    mc "Hey, Uncle Pete."
    show uncletalk
    hide talkhappymc
    if askfishpete == 0 and day >= 2:
        u "Hey, [mc]!"
        u "How was the fish I gave you?"
        mc "Oh, that..."
        menu:
            "\"Yeah, it was great!\"":
                mc "Yeah, it was great!"
                u "Hah, I'm glad you liked it."
            "Lie" if throwfishout == True:
                mc "Y-Yeah, it was great..."
                u "......"
                u "Well, I'm glad you liked it."
            "\"...I didn't eat it.\"" if throwfishout == True:
                mc "Sorry, Uncle Pete. I forgot to eat it and... it got spoiled. I had to throw it out."
                show saduncle
                pause
                show sadtalkuncle
                u "Ah... it's fine."
        $ askfishpete += 1
        u "So, what brings you here?"
        jump talku
    u "[mc]! What brings you here?"

label talku:
    show screen hud with dissolve
    menu:
        "Just came for a visit":
            hide screen hud
            hide uncletalk
            show unclenormal
            show talkhappymc
            mc "Oh, nothing. I just came for a quick visit."
            hide talkhappymc
            show smilemc
            hide unclenormal
            show uncletalk
            u "Then get in, c'mon!"
            show black with fade
            "You spend some time with Uncle Pete."
            pause 2
            $ peteTalking += 1
            if peteTalking == 1:
                scene fishhut
                show unclenormal
                show prot smile
                u "So, [mc], has the sword I gave you been helpful?"
                mc "Oh yeah, definitely. It's a great sword, I'm lucky that you hadn't sold it back in the day."
                u "Heh, yeah."
                mc "Have you finished the painting?"
                u "No, no, I'm far from finished. Art takes time."
                mc "You're right."
                u "But not just art, [mc]. Never forget to give things the time they need. I know you've always wanted to be an Adventurer but don't rush things too much... many Adventurers don't get to live to be old."
                mc "Don't worry Uncle Pete, you taught me well."
                u "Hah, I hope I did. I only learned to take things slowly when I took you in. It'd have been useful to know earlier, though..."
                u "...you know, to deal with a little pest like you."
                mc "Hey!"
                u "Hahah! I'm just kidding around. From what I heard about other kids, you were an angel and you definitely still are. I'm really happy that turned out to be the case."
                mc "Well, I'm really glad I have had you all this time."
                u "Alright it's getting late, it's better if you go."
                mc "Alright, Uncle. See ya!"
                u "See ya."
            if peteTalking == 3:
                scene fishhut
                show unclenormal
                show prot smile
                u "You know kid, there's something I was meaning to tell you."
                mc "What is it?"
                u "Do you like someone?"
                mc "Huh?! Uncle Pete!"
                u "Oh c'mon, you're 19 years old, don't get all flustered."
                menu:
                    "I do":
                        mc "I do."
                        u "What are they like?"
                        menu:
                            "Strong, brave, a bit bad mouthed but good in her heart." if savecynth > 0:
                                mc "Strong, brave, a bit bad mouthed but good in her heart."
                                u "She sounds fun."
                                mc "She definitely is."
                                u "Now, I asked because I want you to know something."
                                mc "What?"
                            "Direct, lovely, determined and a hard-working leader who makes great muffins." if bothpath >= 4:
                                mc "Direct, lovely, determined and a great leader- Oh and she makes great muffins."
                                u "She sounds like someone who gets more stuff done than you."
                                mc "Uncle!"
                                u "Hahah! I still get you this easy, [mc]. When are you going to learn?"
                                mc "When you stop!"
                                u "The only thing that will stop me from teasing my kid is death, so you'll have to endure this a lot longer."
                                mc "Sigh..."
                                u "I'm getting side-tracked, I actually asked because I want you to know something."
                                mc "What is it?"
                            "Independent but lonely, knowledgeable and a formidable mage." if zenQ > 4:
                                mc "Independent but lonely, knowledgeable and a formidable mage."
                                u "I hope you can make her less lonely."
                                mc "I do my best."
                                u "I'm glad."
                                mc "Why'd you ask?"
                            "Pure, cute, strong-willed and definitely a magnificent cook" if theagotjob > 0:
                                mc "Pure, cute, strong-willed and definitely a magnificent cook."
                                u "She sounds like the sweetest person."
                                mc "Oh, she really is."
                                u "I'm glad."
                                mc "Why you asking?"
                            "A bit shy, smart, hard-working and a great friend.":
                                mc "A bit shy, smart, hard-working and agreat friend."
                                u "...Heh."
                                mc "What?"
                                u "Heheheh."
                                mc "What are you laughing for?!"
                                u "Oh, nothing. I have no idea who this smart and hard-working great friend is that you're talking about and I'm not laughing because of that."
                                mc "Uncle!"
                                u "Alright, alright, sorry. I'm happy you like Gabe, I know she's a good kid too."
                                mc "Y-Yeah..."
                                u "Now though, let's not get sidetracked, I wanted to tell you something."
                                mc "What is it?"
                            "Strong but with a soft side. Reliable and experienced." if TaliyaQ > 3:
                                mc "Strong but with a soft side. She's reliable and experienced... and maybe a bit older than me."
                                u "Just \"a bit\" older?"
                                mc "..."
                                u "Oh... I see, I see. Definitely sounds like a great choice."
                                mc "Y-Yeah... Why did you ask?"
                            "A formidable archer, motherly and way taller than me." if ledricquest > 0:
                                mc "A formidable archer, motherly and way taller than me."
                                u "Oh? I see, I've raised you well."
                                mc "...What?"
                                u "Oh, nothing."
                                mc "..."
                                u "Anyways..."
                                mc "So... Why did you ask?"
                            "Don't wanna tell.":
                                mc "I won't tell you. You might guess who it is."
                                u "Ahah, you got me."
                                u "But no, that's not why I asked."
                                mc "Then why?"
                        u "I want you to know that... there's still much I'd like to teach you, there's still many experiences that I can share with you. You're the closest I've ever had to a son and I want you to be the best person you can be. You've made me proud all these years and I want you to make me proud till the end."
                        mc "O-Oh, th-thanks Uncle."
                        u "And I want to tell you one thing about love. This person you like... treasure her. Spend as much time as you can with her and use your time well. I told you to take things slowly and that's true for love too. Things do take time but use that time the right way. Don't let it slip."
                        mc "I won't."
                        u "Good."
                        u "I fell in love once and I didn't use the time we had together for ourselves, we spent time doing other things and in the end she... she left me."
                        u "Be a better man than me, [mc]. I know you can be — you already are."
                        mc "Thanks, Uncle. I'll do my best not to disappoint you."
                    "I don't":
                        mc "I don't have anyone I like"
                        u "I see."
                        mc "Why?"
                        u "It's just that... I've thought about it a lot. I lived a lot already. I'm not old, sure but I've had my fair share of experiences."
                        u "I fell in love only once in my life. Sure, I did have other experiences before that but... Only once was it really special."
                        u "I thought I could take my time, [mc], I thought she'd live much longer than I would but in the end she didn't... and we could never have the life we wanted to."
                        u "It's true, kid, things do take time. But use that time the right way. Don't let it slip."
                        mc "Wow, uhm... I won't. Thanks Uncle."
                        u "Sorry if this came out of nowhere but you're an adult now and... There's things I haven't told you that I want you to know, because I want you to be the best person you can be, because you've made me proud all these years and I want you to make me proud till the end."
                        mc "I'll do my best not to disappoint you."
                u "Just do your best to be a good person, you won't disappoint me."
                mc "Thanks, Uncle."
                u "You're welcome. Now go, it's getting late."
            #if peteTalking == 5:
            #    scene fishut
            #    show unclenormal
            #    show prot smile
            scene fishhut with fade
            show screen hud
            call screen screenmap
        "May I borrow some paint?" if afq ==1 and readalphafalcon == 1:
            hide screen hud
            jump swta2
        "Tools for repairing the Shack" if zenQ == 1 and dayZ >= 1 and toolz == False and zenLeft == False:
            hide screen hud
            hide uncletalk
            show unclenormal
            show prot smile
            mc @smilet "Could I borrow your tools? I need to repair some stuff."
            hide unclenormal
            show uncletalk
            u "Oh? Did something break at home?"
            hide uncletalk
            show unclenormal
            mc @hopet "Oh, no, no. It's for some of my stuff"
            hide unclenormal
            show uncletalk
            u "If you need any help, I can give you a hand. Just because I'm old doesn't mean I can't, you know?"
            hide uncletalk
            show unclenormal
            mc @smilet "Yeah, I know but if I don't do it myself, I'll never learn how to do it."
            hide unclenormal
            show uncletalk
            u "Hah! Seems like leaving you the house was a good idea, eh? You almost sound like an adult."
            hide uncletalk
            show unclenormal
            mc @smirkt "Oh shut up. I {b}am{/b} an adult."
            hide unclenormal
            show uncletalk
            u "Yes, I guess you are... I still remember when I found you fourteen years ago, you were a little pest. Yet here you are, a grown man... You know I'm proud of you, right?"
            hide uncletalk
            show unclenormal
            mc @hopet "I do."
            hide unclenormal
            show uncletalk
            u "Good. Now don't let me hold you any further. Get what you need but please bring them back soon."
            hide uncletalk
            show unclenormal
            mc @smilet "I will! Thank you, Uncle."
            hide unclenormal
            show uncletalk
            u "Take care."
            "You leave and go back home."
            $ toolz = True
            jump home
        "Your tools" if toolz == True and zenQ >= 2 or toolz == True and zenLeft == True:
            hide screen hud
            hide uncletalk
            show unclenormal
            show talkhappymc
            mc "Here's your stuff, Uncle Pete."
            hide talkhappymc
            show smilemc
            hide unclenormal
            show uncletalk
            u "Thanks kid, hope it was useful."
            hide uncletalk
            hide smilemc
            show unclenormal
            if zenLeft == True:
                show talksadmc
                mc "Yeah..."
            else:
                show talkhappymc
                mc "Yeah. Thanks, Uncle."
            $ toolz = False
            jump home



label petebadge:
        hide screen hud
        scene villageback
        show smilemc with easeinright
        mc "I hope Uncle Pete is home."
        "You see someone coming out of Uncle Pete's fishing hut."
        show thinkmc
        mc "{i}Scarlet?"
        show normalm with easeinleft
        s "Oh. Hey, [mc]."
        mc "Hey."
        s "Your uncle's fish is really good, I just bought some from him."
        show talksadhappymc
        mc "Ah."
        s "He's a nice guy, your uncle."
        mc "Heh, yeah he is."
        s "I'm guessing you're here to pay him a visit?"
        mc "Yeah, I just became a Bronze-Rank Adventurer. I wanted to tell Uncle Pete."
        show teethm
        s "Really? Wow, congratulations!"
        mc "Thanks, Scarlet."
        show sadtalkm
        $ showpetebadge += 1
        s "Your uncle will be very proud. He's always talking about you, you know?"
        mc "I hope he hasn't said anything embarrassing."
        s "Heheh. Nothing like that."
        mc "It sounds like you come here often."
        show talkwam
        s "Yeah, where else do you think I should get my fish from?"
        mc "Hm... You got a point."
        menu:
            "You know, my uncle is still single.":
                show talkwamc
                mc "You know, my uncle is still single, by the way."
                s "......"
                hide talkwamc
                show uhm
                s "Do you want me to turn you into a frog?"
                mc "Hey, hey! I'm just joking!"
                hide uhm
                s "Eheheh."
            "Say nothing":
                mc "......"

        s "Alright, now I got to go. Go give your uncle the good news."
        mc "Alright. Bye, Scarlet."
        scene villageback
        show smilemc
        show sadtalkm
        s "Bye."
        hide sadtalkm with easeoutright
        pause
        hide smilemc with easeoutleft

        scene black with fade
        "You arrive at Uncle Pete's fishing hut."
        play sound doorknock
        "{i}knock knock"
        mc "Uncle Pete? It's me, [mc]."
        "......"
        "......"
        mc "Uncle P-"
        "The door opens."
        u "[mc]. Hey, kiddo."
        mc "Hey, Uncle Pete. What's up?"
        u "Just... painting."
        mc "Oh."
        u "So, what brings you?"
        "You show Uncle Pete your Bronze badge."
        mc "I became a Bronze-Rank Adventurer."
        u "[mc]... That's amazing! Hahahah!"
        u "Congratulations, Adventurer!"
        mc "Heheh, thanks!"
        u "Come in, come in! We need to celebrate!"
        "You go in."
        scene fishhut with fade
        u "Take a seat."
        "Uncle Pete opens a cupboard and takes out a bottle."
        u "You're nineteen now, right?"
        mc "Yes."
        u "Hahah, great! Let's have a drink!"
        mc "A drink?"
        u "Yeah. Come on, have a drink with your old man! It's about time!"
        mc "{i}Whoah, it's my first time having drink with Uncle Pete."
        mc "Ehhh, why not?"
        u "Hehehe. But hold on to your pants, this is some strong stuff."
        mc "Bring it on!"
        u "Here we go!"
        scene black with fade
        "Uncle Pete pours you a glass and you both start drinking. The two of you talk for a long while as you tell Uncle Pete about your adventures."
        "Uncle Pete wasn't kidding: the drink packs one hell of a punch. A few sips and your head already starts to spin. Uncle Pete on the other hand has no problem. He's gulping it down like water."
        u "This Sander seems to be an interesting fellow, isn't he?"
        mc "Y-Yeah, he's kinda weird though."
        u "Hahaha. Weird people are always the interesting ones."
        mc "I guess you're right."
        u "And what about this elf woman? Eve, was it?"
        mc "Oh yeah, she's really kind. The total opposite of Sander."
        u "Hehe, I would like to meet your friends one day."
        mc "Yeah, I think you'd like them. Maybe one of these days."
        "Time passes and you keep chatting."
        play music night
        mc "Ugh... is it already night or am I just drunk?"
        u "Hahahahah, it's both."
        mc "What..."
        u "Let's go outside, looks like you need some air."
        mc "Nooo... {i}hic{/i}, it's fine, Uncle Pete... let's just stay here."
        u "Come on, it's really nice outside at this time."
        mc "{i}...hic."
        u "And I don't want you throwing up inside my house."
        mc "Ugh... fine... fine."
        "The two of you go outside."
        play music nurture
        $ persistent.peteStargazing = True
        scene petestargaze with fade
        pause
        window hide
        mc "...Wow."
        u "Pretty, isn't it?"
        mc "The sky is so beautiful... {i}hic{/i}"
        u "Hmmm, it is."
        pause
        mc "Why are the stars... so... big?"
        u "Heh. Mainly because you're drunk, kid."
        mc "I'm not... drunk."
        u "Hahah."
        u "......"
        u "I'm really proud of you, [mc]."
        mc "......"
        mc "Thanks, Uncle Pete."
        u "I'm glad that I settled down here with you, [mc]. My life before this, as a merchant, it was always about... selling this, selling that."
        u "I really didn't know why I didn't stop before, maybe because people told I was good at it. Still, I felt like my life had no meaning, like it had no real destination."
        u "But after I took you in, taking care of you, seeing you grow up... That was and still is, everything to me. I realized I had finally found a meaning in my life."
        u "I just want to keep watching you and see you go on many journeys. That's all I want."
        u "Be sure not to disappoint, you hear me?"
        mc "Heheh, I'll try my best."
        u "Remember kid, your old man is always here to back you up."
        mc "Thank you for everything, Uncle Pete."
        u "......"
        "Uncle Pete rubs his eyes."
        "You see tears falling from his face but you pretend not to notice."
        "The two of you stare at the beautiful sky."
        scene black with fade
        stop music fadeout 3.0
        scene mcroomn with fade
        $ time = 4
        jump home
