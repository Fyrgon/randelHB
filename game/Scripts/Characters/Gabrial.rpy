default timesTalkwGabe = 0
default gabeInvitation = False

label gabrialTalk:
    menu:
        "Talk with Gabe" if GabeHome == True:
            show talksadhappymc
            mc "Was walking nearby and thought of coming over."
            show talkwag
            g "Get in then! Oh and, do you want a sandwich?"
            mc "Sure do."
            scene black with fade
            "Gabe tells you to wait in her room and you do as such."
            if timesTalkwGabe == 0:
                scene gaberoomd
                show normalg
                show prot smile
                g "Y'know, it feels really strange seeing you here in my bedroom."
                mc "Huh? How come?"
                g "Well, you know, we spent six years apart and then... things are back to normal."
                mc "Well, why wouldn't they?"
                g "I'm not saying it's a bad thing, just that... It's weird. I still feel completely at ease are you."
                if boldMC == True:
                    mc "It's just my charm."
                    g "Hah, hah. Really funny."
                    mc "Thanks, I know."
                else:
                    mc "That's because we're still friends, aren't we?"
                    g "Well... Yeah. But you still couldn't recognize me when I came back."
                    mc "Listen, people change during their teenage years. You included."
                    g "You haven't."
                    mc "Is that an insult?"
                    g "Oh yeah. Definitely."
                    mc "I'll shut up."
                g "Anyways, how's it going with being an Adventurer and all?"
                if level > 10:
                    mc "It's going really well, especially since I'm a Bronze-Rank Adventurer already."
                    g "Really? I see you're on your way to become a great Adventurer already, aren't you?"
                    mc "Hah, let's not exaggerate. Getting from Bronze to Silver is being much, much more difficult than it was to go from a recruit to Bronze."
                    g "Well that sounds pretty obvious to me."
                    mc "Does it?"
                    g "Well, you know how when Adventurers get called to the army they get an army rank equivalent to their Guild one?"
                    mc "...Yeah?"
                    g "Bronze-Rank Adventurers become regular soldiers, Silver-Ranks become captains, Gold-Ranks become commanders, and diamond-Ranks get their own special rank above commanders but below major. If it were easy to become Silver-Rank we'd have more captains than soldiers in the army."
                    mc "Well yeah, that makes sense. Captains do need much more experience compared to regulars... But being a Bronze-Rank isn't as cool as anything above."
                    g "There you go again geeking about being an Adventurer."
                    mc "Hey! It's true. When a Bronze-Rank dies, people just go \"what a shame\" or even worse \"he shouldn't have taken that quest.\" Meanwhile when anyone above dies they are remembered and may even get something made for them."
                    g "Does it all have to be related to dying?"
                    mc "C'mon. You know what I'm saying."
                    g "Do I?"
                    mc "We've got two statues in Randel besides the one dedicated to King Goudeau. Basche's in front of the lake, and Aghelos' in front of the Guild. They're both legendary Adventurers and their stories have inspired so many to become Adventurers as well."
                    mc "I just... I want to become someone who can inspire others as well, y'know?"
                    g "Sigh... You really haven't changed."
                    mc "Why would I?"
                    g "Because we've been 6 years apart, dummy."
                    mc "Fair point."
                    g "I'm actually glad. It would've been awful if the kid with unreasonable dreams had become a boring farmer content with hoeing a field all day."
                    mc "Oh Astylla, that'd been horrible."
                    g "..."
                    g "...Try to not get yourself killed, though."
                    mc "I'll do my best I promise."
                    g "Good."
                    mc "Alright, it's gotten a bit late. I think I'll go now. See ya."
                    g "See ya."
                    $ time += 1
                    jump home
                else:
                    mc "Going well, still just a recruit, but hey, taking things slow has never killed anyone."
                    g "Oh definitely."
                    mc "But don't worry, I'll become a diamond-Rank soon enough."
                    g "Ah yes, a diamond Adventurer. Soon."
                    mc "Am I hearing sarcasm?"
                    g "Oh no, not at all, I'm going to be an Imperial-Rank mage in a few weeks as well."
                    mc "..."
                    g "I'm just messing. I'm glad you're still ambitious one between the two of us."
                    mc "Why? You don't want to become an Imperial mage?"
                    g "Oh, it'd definitely be great, but no one so strong started as late as I have. It'll already be hard to get to the level of a Royal mage the way I am now."
                    mc "..."
                    menu:
                        "You'll make it":
                            mc "I'm sure you'll make it. You're hard-working and smart, a mage doesn't need much more."
                            g "I haven't got enough talent."
                            mc "If the power to do hard work is not a talent, it's the best possible substitute for it... isn't that what they say?"
                            g "I guess some do say that. Let's hope they're right."
                        "You'll become the strongest":
                            mc "I believe in you. With enough willpower you'll become the strongest there is."
                            g "I'm not too sure that's how it works."
                            mc "I am."
                            g "...I won't argue, but just know I'm not convinced."
                        "You're already awesome":
                            mc "You're already awesome the way you are, though."
                            g "H-Huh?"
                            mc "You're smart, cute, hard-working, and fun. Even if you only become a high mage, who cares? You're great."
                            g "...T-Thanks."
                        "You're right":
                            mc "I guess you're right. But that still shouldn't stop you from trying your best, got it?"
                            g "Yes, yes. Don't worry I'll work my ass off to be the best I can be."
                            if surpassGabe == True:
                                g "...so that you'll never surpass me, bucko."
                                mc "Competitive, are we?"
                                g "You're the one who said you'd surpass me. Haven't seen that one happen yet."
                                mc "Heh. We'll see."
                            mc "...I believe in you."
                            g "Thanks, [mc]."
                    mc "Oh yeah, by the way, you haven't really told me a lot about your time in Westian yet. How was it?"
                    "For a second her eyes grow distant, but quickly she lightens up."
                    g "Oh, it was great! Everything there is so big! The houses, the streets, the libraries... There's even a castle!"
                    mc "Wow, the noble family of Westian must be really rich."
                    g "It really is. The Academy in Westian is even named after them because apparently they were the ones to built it before King Ron mandated Academies should be built in every city."
                    mc "Yeah, Westian is really old, isn't it?"
                    g "Yeah, but that isn't all that there is to it. Randel isn't that much younger but we started as farmers. The nobles we got only came to the town after seeing how profitable it was starting to get. They don't own most of Randel like the nobles in Westian because they werern't the ones that built Randel."
                    mc "That's true. Even though they're the most important noble family in town, the Bryways barely own anything. I think they helped with the Library and I know they own quite a few fields, but they're hardly nobles."
                    g "Yeah, the descendants of James Randel that are still in town are probably wealthier."
                    mc "Hah, yeah."
                    "Gabe looks at the window and sighs."
                    g "It's getting late, I guess it's time for you to go back home."
                    mc "Oh, yeah, you're right. See ya."
                    g "Come back soon."
                    mc "I will."
            #if timesTalkwGabe = 1:
            #    scene gaberoomd
            #    show wagabee
            #    show prot happy
            #if timesTalkwGabe > 1:
            #    scene gaberoomd
            #    show wagabee
            #    show prot happy
            else:
                "You spend some quality time with Gabe and then leave."
            $ time += 1
            jump home
        "Training" if gabequest2 == 1 and GabeHome == True:
            jump gabetrain
        "Nothing" if GabeAcademy == True:
            show talksadhappymc
            hide talkgabe
            mc "Oh, nothing much. Just wanted to see what you were up to."
            hide talksadhappymc
            show talkgabe
            g "Ah, makes sense. I've got another class coming up soon, what about you?"
            mc "Same."
            g "Ahh... I wish we had as much free time as we had when we were kids."
            mc "Remember how you used to say you wanted to grow up quickly so you could become a mage?"
            g "I didn't know I'd have to spend half of my days at the Academy..."
            mc "Hah."
            g "Well, I gotta go. See you [mc]."
            mc "See ya."
            jump academy


        "Ask about Lori" if loriEventValue == 4:
            call gabeInfoDump
            jump home

        "Ask if she can take care of the library" if loriEventValue == 6:
            g "What's up with all that hurry?"
            mc "I need to ask you a favor."
            g "Uh... Sure? What is it?"
            mc "Could you watch over the library while Lori is out?"
            g "Lori? Out? H-Huh?"
            mc "Yeah, she always talks about wanting to go on adventures, so I told her to come with me on one and she agreed... But she can't leave the library unattended, so..."
            g "...I see."
            g "Well, y'know, I'm glad you thought of me."
            mc "So, could you do it?"
            g "Yeah, I don't mind. I'm not that busy, and I'm free this whole week anyways."
            mc "Great. Thank you so much, Gabe."
            g "No probs, dude. I'm always happy to help a friend out."
            mc "Alright then, see ya! I'll come over in the morning!"
            g "Sure thing, see ya!"
            "You leave and go home."
            $ loriEventValue = 7
            jump home

        "I'm ready for our trip." if gabeInvitation == True and gabetrip == 0 and GabeHome == True:
            hide screen hud
            show talkwamc
            mc "I'm ready for our... trip."
            show talkg
            g "Great!"
            mc "Let's go then."
            jump gabetrip

        "Ask for clothes" if findtheaclothes == 1 and theaclothes == 0:
            hide talkgabe
            hide normalgabe
            $ gabesClothes = True
            show thinkmc
            show normalg
            mc "Ok then. How should I go about this...?"
            mc  "{i}I mean...{p}{i}She is definitely going to think I need these clothes for weird things...{p}{i}If I'm-"
            show talkwag
            g "[mc]?"
            hide talkwag
            show talkwanmc
            mc "Y-Yes?"
            show talkwag
            g "You've been staring at me for a solid minute, [mc]."
            hide talkwanmc
            show talksadhappymc
            mc "Oh... yeah... sorry... I need to ask you something and I'm nervous about it."
            show blushtalkg
            hide talksadhappymc
            g "Really? Well... just go ahead and ask. You weirdo."
            show talksadhappymc
            mc "May I have some of your clothes?"
            g "......"
            mc "......"
            show talkwag
            g "I'm not sure what I was expecting you to ask, but this definitely wasn't it. Why on earth do you need some of my clothes?"
            mc "{i}Should I be honest about this? I'm still not sure if I should tell folk about Thea yet..."
            menu:
                "Be honest":
                    show talkmc
                    mc "I saved a girl from Yokel. It was burned down by Imps and I barely managed to get her out of there in time. She's staying with me and needs some clothes since her old ones got destroyed."
                    show talkg
                    g "...Wow, [mc]."
                    show talkwanmc
                    mc "What?"
                    g "You are really doing the hero thing, huh?"
                    show talkhappymc
                    mc "It was just the right thing to do..."
                    if GabeHome == True:
                        scene gaberoomd
                    if GabeAcademy == True:
                        scene academytalkblr
                    show suprised
                    show normalgabe
                    "Gabe hugs you."
                    show talkgabe
                    g "I'm really proud of you. Wait I'll get some."
                    mc "Uhm... Ok... thanks, Gabe..."
                    hide surprised
                    show smilemc
                    show blushgabe
                    "Gabe goes to her room and brings some clothes."
                    g "Here, take them. I'm not sure if this might fit."
                    play sound chime
                    $ renpy.notify("{color=#fff}You got clothes for Thea.")
                    mc "Thanks, Gabe."
                    g "No problem."
                    hide normalgabe
                    hide talkgabe
                    hide blushgabe with easeoutright
                    mc "Ok, that worked out..."
                    play sound chime
                    $ renpy.notify("{color=#fff}Gabe trusts you more")
                    $ gabeKnowThea = True
                    $ theaclothes += 1
                    $ theaclothestimer += 1
                    $ findtheaclothes +=1
                    $ girlclothes += 1
                    jump home
                "Lie to her":
                    $ gabeKnowThea = False
                    mc "Uhm... the clothes are for... Uncle Pete!"
                    show wagabe
                    g "...Why?"
                    mc "He... is... trying out sewing women's clothes and needs inspiration! And you dress the best here, so I..."
                    show angrygabeblush
                    pause
                    show cutegabeu
                    "Gabe grins at you."
                    g "Well, in that case [mc], I'll drop some clothes off at Pete's shack tomorrow."
                    mc "NO! Uhm... he'd be embarrassed! That's why he asked me to get them!"
                    show yellgabe
                    g "...You realize I am not an idiot right, [mc]?"
                    mc "..."
                    g "You really think I can't tell when you are lying? I've known you since we were kids, you idiot."
                    mc "...Sorry..."
                    hide yellgabe
                    g "Ugh, it's fine. I'll drop some clothes off in your locker. Just don't do anything weird with them, ok?"
                    mc "...Thanks..."
                    if GabeHome == True:
                        scene gaberoomd
                        show worriedmc
                        show cutegabe
                        "Gabe leaves the room abruptly."
                    else:
                        scene academytalkblr
                        show worriedmc
                        show cutegabe
                        "Gabe leaves abruptly."
                    hide cutegabe with easeoutright
                    mc "Well... that could've gone better..."
                    $ gabeKnowThea = False
                    $ theaclothes += 1
                    $ theaclothestimer += 1
                    $ findtheaclothes +=1
                    $ girlclothes += 1
                    if GabeAcademy == True:
                        jump academy
                    jump home
    return





label gabetrain:
    hide screen hud
    if gabetrain1 == 0:
        show talksadhappymc
        mc "How about we start our {i}ahem{/i} \"training\"."
        show blushtalkg
        g "Ok."
        scene gaberoomd with fade
        "Gabe strips down her clothes. You stand there with your mouth open."
        g "What? We can't do anything with our clothes on."
        mc "Y-Yeah, but I thought we could start slow... because..."
        g "I know... so how do we start?"
        mc "{i}Shit! I should've really done some research. I have no idea what to do here."
        g "[mc]?"
        mc "Ok... let's start with..."
        mc "...Fingering."
        g "...A-Alright."
        scene gabefingerbase1 with fade
        show gabefingerbase0
        show gabefinger1
        mc "I'll start slow."
        hide gabefingerbase0
        g "Ahh~!"
        mc "...Gabe, I haven't started yet."
        show gabefingerbase0
        g "Oh."
        g "I-I was just getting mentally ready."
        mc "...Are you ready then?"
        g "Y-Yeah."
        hide gabefingerbase0
        hide gabefinger1
        show animationgabefinger
        g "Aahhh..."
        window hide
        pause
        g "I'm cumming!"
        scene gabefingerbase1
        show gabefinger4
        show gabecum
        show gabefingerbase2 with flash
        pause 0.2
        show gabefingerbase2 with flash
        pause 0.2
        show gabefingerbase2 with flash
        pause 0.2
        g "{i}huff... huff..."
        scene gaberoomd with fade
        mc "Looks like we have a long way to go."
        g "{i}Sigh...{/i} Yeah, I didn't even last 20 seconds."
        mc "It's alright. That's what training is for."
        g "Heheh. Ok, master [mc], if you say so."
        scene gaberoomd with fade
        show talksadhappymc
        show normalg
        mc "We'll do this again tomorrow."
        show blushtalkg
        g "Alright."
        g "Thank you, [mc]. For... helping me."
        mc "No problem."
        $ time += 1
        $ gabetrain1 += 1
        $ persistent.gabeFingering = True
        jump home
    menu:
        "Fingering":
            if gabefinger == 3:
                scene gabefingerbase1 with fade
                show gabefinger1
                g "Let's start."
                hide gabefinger1
                show animationgabefinger
                window hide
                g "Ahhh..."
                mc "You're doing well."
                pause
                g "Huff... yeeesss, I caaan do it!"
                g "Aaahhhh... aaahhh!"
                g "I think I'm going to cum."
                mc "Just a little longer."
                pause
                g "[mc]...!"
                g "I'm cumming!"
                scene gabefingerbase1
                show gabefinger4
                show gabecum
                show gabefingerbase2 with flash
                pause 0.2
                show gabefingerbase2 with flash
                pause 0.2
                show gabefingerbase2 with flash
                pause 0.2
                scene black with fade
                pause 0.5
                scene chillgabe with fade
                g "How was that?! I almost lasted 3 minutes there."
                mc "You did good."
                g "Yay! Thank you, sex master!"
                mc "Don't call me that."
                g "Hehe. Well, I guess I'm ready for a better challenge, now."
                mc "We'll see."
                "You spend some time with Gabe and go home afterwards."
                $ time += 1
                $ gabefinger += 1
                jump home
            scene gabefingerbase1 with fade
            show gabefinger1
            mc "I'm going to start now."
            g "O-Ok."
            hide gabefinger1
            show animationgabefinger
            window hide
            g "Ahhhh..."
            mc "Try to hold it in this time."
            pause
            g "...It... feels too good."
            pause
            g "Ahhhh... Ahhhhhh!"
            pause
            g "I'm going to cum."
            g "I'm cumming!"
            scene gabefingerbase1
            show gabefinger4
            show gabecum
            show gabefingerbase2 with flash
            pause 0.2
            show gabefingerbase2 with flash
            pause 0.2
            show gabefingerbase2 with flash
            pause 0.2
            if gabefinger == 0:
                scene black with fade
                pause 0.5
                scene chillgabe with fade
                mc "What are you doing?"
                g "What? Oh, this? ...I'm keeping logs."
                mc "On our training?"
                g "Yeah, see? Number of times fingered; two. Highest time lasted; 30 seconds. It'll be important to see my progress."
                mc "Uhm, ok."
                mc "You actually did better this time."
                g "You think?"
                mc "Yeah."
                g "Oh good, I've been... practicing."
                mc "...Keep it up, I guess."
                g "Hehehe. Wanna have a snack before going home?"
                mc "Ok."
                "You spend some time with Gabe."
                $ time += 1
                $ gabefinger += 1
                jump home
            scene black with fade
            pause 0.5
            scene chillgabe with fade
            g "I feel like I'm improving."
            mc "You are."
            g "When do you think I can... move to the next stage?"
            mc "{i}Gulp.{/i}{p}Soon, soon."
            g "Can't wait!"
            "You spend some time with Gabe and go home afterwards."
            $ time += 1
            $ gabefinger += 1
            jump home
        "Dildo training" if dildoi == 1:
            if gabedildo == 0:
                $ persistent.gabeDildo = True
                show talkwamc
                mc "It's time we moved to the next level."
                show talkwag
                g "Finally."
                "You show Gabe your present."
                mc "Tada!"
                show talkshg
                g "You got me a dildo?"
                mc "Yeah."
                g "Wow... I've always wanted one! Aren't these things expensive?"
                mc "A little."
                g "Thanks, [mc]!"
                mc "No problem. Let's start then."
                g "Alright."
                scene gabefingerbase1 with fade
                show gabefingerbase0
                pause
                g "Start slow, ok?"
                mc "Don't worry."
                hide gabefingerbase0
                show gabedildo1 with dissolve
                g "Ahhh... is that all of it?"
                mc "Uhm... no."
                g "Ok, ok... put it all in."
                show gabedildo2 with dissolve
                g "Oh... Astylla be blessed."
                window hide
                pause
                mc "I'm going to start moving it."
                scene gabefingerbase1
                show animationgabedildo
                g "Ahhhh~!"
                g "No... I think I'm cuming!"
                scene gabefingerbase1
                show gabefingerbase2
                show gabedildo3
                show gabecum with flash
                g "I just came."
                scene black with fade
                pause
                scene chillgabe with fade
                g "That was... AWESOME! I've never felt that good!"
                mc "Well, wait till you get to the real thing."
                g "Mhh... I don't think I'll be needing it now, since I have this."
                "Gabe dangles the dildo in front of you."
                mc "HEY!"
                g "Hehehehehe."
                mc "We'll continue tomorrow..."
                g "Ok, and I'll practice at night."
                mc "...Sure."
                "You leave Gabe's house."
                $ gabedildo = 1
                $ time += 1
                jump home
            if gabedildo == 2:
                $ persistent.gabeHandjob = True
                scene gabefingerbase1
                show gabefingerbase0
                g "Ok, I'm going to last longer this time."
                hide gabefingerbase0
                scene gabefingerbase1
                show animationgabedildo
                g "Ahhhhh..."
                g "F-Faster!"
                window hide
                pause
                g "Oh... yesssss!"
                g "Faster, [mc], faster!"
                pause
                mc "{i}She's going crazy!"
                g "Ahhh... ahhh... ahhhh..."
                mc "{i}Cum already! ...My hands are starting to ache."
                pause
                g "Aaaahhhhh!"
                g "I'm going to cum!"
                scene gabefingerbase1
                show gabefingerbase2
                show gabedildo3
                show gabecum with flash
                g "Cumming!!!"
                scene black with fade
                pause 0.5
                scene chillgabe with fade
                g "So... how did I do?"
                mc "Really good."
                g "You think I'm ready... for... the last stage?"
                mc "Mh... almost."
                g "Thanks for all the help, [mc]. I never imagined your training would work."
                mc "I told you I was a pro."
                g "It seems like you were."
                g "[mc], I'm so lucky to have a friend like you. "
                mc "...Uhm, don't mention it, Gabe."
                g "I haven't even thanked you properly."
                mc "There's no need, Gabe."
                g "No, I should."
                "Gabe scoots closer to you."
                g "Come on."
                mc "O-Ok, what do you have in mind."
                g "Well... since you've been making me feel good, I thought I should return the favor."
                mc "Oh...."
                g "And besides, I want to see how much endurance my \"master\" has."
                mc "{i}Gulp"
                "Gabe pulls your pants down."
                scene hjgabe with fade
                pause 4
                g "Wow! It's... not {b}that{/b} big."
                mc "Excuse me?!"
                g "Ahh, no offense. I just thought it would be... bigger. In all the novels I've read they're describe to be huge."
                g "...I guess they were exaggerating."
                mc "How big did you think it would be?"
                window hide
                pause 1
                g "I don't know... like, three times the size of the dildo."
                mc "WHAT!? Are you crazy- How is a person supposed to walk with a dick that big."
                g "Mh... I guess you're right. "
                g "Sorry, [mc]. It's my first time seeing one."
                mc "I'll have you know my dick size is above average."
                g "Really? You've... seen other dicks?"
                mc "...No."
                window hide
                pause 2
                g "Then how do you know?"
                mc "I just know!"
                show hjgabe1 with dissolve
                pause 1
                scene gabehjSlow
                show hjgabe
                show hjgabe1
                g "Fine, fine. I believe you, big guy. Let me make your \"big\" cock feel good."
                hide hjgabe1
                hide hjgabe with dissolve
                window hide
                pause 3
                mc "Mhhh."
                window hide
                pause 4
                g "How does it feel?"
                mc "It... feels good."
                window hide
                pause 4
                mc "{i}Her hands are soft and warm, it feels really good."
                g "You going to cum?"
                mc "...No... not yet... keep going."
                g "It seems this isn't good enough for my master. I will have to try harder then~"
                show gabehjFast with dissolve
                pause 1
                mc "Oh fuck-"
                g "Oh, did my skills impress you?"
                mc "...M-Maybe."
                window hide
                pause 7
                g "It's growing bigger... You're going to cum, aren't you?"
                mc "..."
                window hide
                pause 3
                mc "Y-Yeah."
                "Gabe lets out a small giggle."
                g "Cum on my face~"
                mc "A-Are you sure...?"
                g "Yes! do it!"
                mc "Alright th-then..."
                window hide
                pause 8
                mc "I'm cumming!"
                show gabehjCum with flash
                pause 3.5
                scene hjgabecum1 with fade
                pause 3
                g "Mmmh, you came a lot."
                "Gabe wipes her face with her fingers and licks it."
                g "......"
                g "I've always wanted to know what it tasted like."
                g "It tastes-"
                menu:
                    "Stop! I don't want to know.":
                        mc "Stop! I don't want to know."
                        g "Eh? Ok, then."
                    "Say nothing.":
                        g "It tastes... salty."
                        mc "Not sure if I wanted to know that."
                        g "Hehehe."
                scene chillgabe with fade
                mc "That was great. Thanks, Gabe."
                g "It was my pleasure."
                g "...I can't believe I finally touched a dick."
                mc "Congratulations! My little girl is finally a woman."
                g "Hehehe... Shut up, [mc]."
                g "You know, I was thinking... We should go out tomorrow."
                mc "Go out? Where?"
                g "I found a really nice place in the forest-"
                mc "In the forest?"
                g "Don't worry, it's not near goblin territory."
                g "I thought it would be a nice place for a picnic."
                g "So what do you say? Are you free tomorrow?"
                mc "Mh... I am."
                g "Great! Let's go tomorrow then."
                mc "Why go out suddenly?"
                g "I'm getting bored staying in here all day. It's time we went out."
                mc "So, is this like a date?"
                g "Huh? No. We're still friends, remember? Think of it as a small... trip together."
                mc "Oh... ok."
                g "Come to my place tomorrow evening, I'll get everything we need."
                mc "Alright, see you tomorrow then."
                g "Yeah, bye."
                scene mcroomn with fade
                pause 0.3
                stop music
                mc "{i}Gabe still thinks of me as a friend even after all that has happened?"
                mc "{i}Am I ok with that?"
                menu:
                    "Yes":
                        mc "Yeah, it's fine. No need to complicate things between us. What we have is better."
                    "No":
                        mc "No! After all this, she can't still think of me as a friend. I love her, I should tell her."
                $ time += 1
                $ gabedildo += 1
                $ gabeInvitation = True
                jump home
            scene gabefingerbase1
            show animationgabedildo
            pause 4
            g "Ahhhhh... Yes...!"
            pause 4
            g "Deeper!"
            pause 4
            g "I'm cumming!"
            scene gabefingerbase1
            show gabefingerbase2
            show gabedildo3
            show gabecum with flash
            g "Ahhhhhhhhh!"
            scene black with fade
            pause 0.5
            scene chillgabe
            g "Ahhh... That felt good. [mc], you better come every day or I might go crazy."
            mc "O-Ok."
            g "Come, let's have some tea."
            mc "Alright."
            "You spend some time with Gabe and go home afterwards."
            $ gabedildo += 1
            $ time += 1
            jump home
        "Handjob" if gabedildo > 2 :
            show talkwamc
            mc "How about you use those hands again?"
            show talkwag
            g "Sure thing, master."
            window hide
            scene hjgabe with fade
            g "I'm going to start now."
            scene gabehjSlow
            show hjgabe
            show hjgabe1 with dissolve
            pause 2
            $ handjobgabe += 1
            hide hjgabe1
            hide hjgabe with dissolve
            mc "Mmmhh, yeah."
            window hide
            pause 6
            g "So... how was your day?"
            window hide
            pause 1.7
            menu:
                "Good":
                    mc "It... was good."
                    pause
                    g "Hmmm... I'll make it better."
                "Bad":
                    mc "Not the best."
                    pause
                    g "Aww... poor [mc], let me make your day better."
            scene gabehjFast with dissolve
            window hide
            pause 6
            mc "Ahhh... Gabe, you're so good at this."
            g "Thanks. Heeheehee."
            window hide
            pause 3
            g "I wonder how long you can last~"
            window hide
            pause 8
            mc "Ugh!"
            mc "I'm-"
            g "Cumming~?"
            mc "Y-Yes!"
            show gabehjCum with flash
            pause 3.5
            scene hjgabecum1 with fade
            pause 3
            g "It's so much..."
            scene chillgabe with fade
            "After you're done, Gabe cleans herself up and gets on the bed."
            mc "Thanks again, Gabe."
            g "No problem."
            g "{i}Times given handjobs to [mc]: [handjobgabe]"
            g "Come, let's do something."
            "You spend some time with Gabe and go home."
            $ time += 1
            jump home
        "Sex" if gabetrip == 1:
            mc "Sex?"
            g "Oh yes please."
            menu:
                "Doggy":
                    $ persistent.gabeDoggy = True
                    show gabesexanime2 movie
                    window hide
                    g "Ahhh...... Ahhh..."
                    pause
                    g "Fuck me!"
                    pause
                    g "Ahn... Ahh~!"
                    mc "I'm cumming!"
                    scene gabesexcum2 with flash
                    g "AHHH!!"
                "Missionary":
                    $ persistent.gabeMissionary = True
                    scene gabemissionary1 with fade
                    pause
                    show gabesh1
                    g "Please... Put it in already..."
                    show gabesh2
                    show gabemissionary2
                    g "Ahhh~ Fuck yes!"
                    window hide
                    show gabesh3
                    g "Ahhh... Ahhh......!"
                    pause
                    show animationgabemissionary
                    g "Mh~!"
                    pause
                    mc "Fuck, you're tight!"
                    g "Harder!"
                    show gabecum
                    show gabemissionary3 with flash
                    pause 0.2
                    show gabemissionary3 with flash
                    pause 0.2
                    show gabemissionary3 with flash
                    pause 0.2
                    g "AHHH!!"
            scene chillgabe with fade
            g "That was awesome."
            mc "Hah... Yeah."
            g "We have to do this again."
            mc "I'm up for it."
            "You spend some time with Gabe and go home afterwards."
            $ time += 1
            jump home
    return
