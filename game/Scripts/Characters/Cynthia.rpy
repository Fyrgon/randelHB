label cynthiaAcademyTalk:
    hide screen hud
    if sawcynth == 3:
        show normalmc
        show talksadhappymc
        show normalc
        mc "Uhm... Hi, Cynthia..."
        hide talksadhappymc
        show talkshc
        c "Hello... Do I know you?"
        show talksadhappymc
        mc "We, uhm... We sort of bumped into each other-"
        hide talksadhappymc
        show talkshc
        c "Oh, hah! Silly me! I remember now."
        mc "Hehehe..."
        hide talkshc
        "Cynthia glances around to see if anyone is paying attention."
        show angryc
        show suprised
        c "Ok, listen here, dipshit. I don't want you to start stalking me, you hear?"
        c "Don't think for even a second that I haven't noticed you staring at me all the time. Or that you \"bumped\" into me by accident."
        hide angryc
        show normalcb
        show worriedmc
        show talkwanmc
        mc "B-But... What? I thought-"
        hide talkwanmc
        show angryc
        c "Oh, I know. You thought Cynthia was a cute, friendly lovey-dovey little girl, right? Guess what? You're wrong. I'll fuck you up."
        c "I don't want to be seen with a loser like you, so do me a huge favor and scram."
        scene academytalkblr
        show worriedmc
        mc "{i}I can't believe it. Cynthia is secretly a super bitch..."
        mc "{i}All that friendly, cute girl attitude is just an act."
        show angry
        mc "That bitch!"
        $ sawcynth += 1
        jump academy
    if sawcynth == 6 and findtheaclothes == 1 and cynthquest2 == 0:
        mc "Why am I asking Cynthia? I suppose it's safer than asking a teacher or my childhood friend..."
        mc "In reality, I'm probably just looking for an excuse to talk to her..."
        "Cynthia sees you coming from down the hall and glares at you."
        mc "Ahh... man... she really doesn't want to be seen with me..."
        "Cynthia then quietly gestures down the hall and excuses herself from her \"friends\"."
        mc "Wait... does she want me to follow her?"
        "You follow her down the hall and see her enter the janitor's closet."
        mc "Ok... so?"
        "As soon as you open the door, Cynthia grabs you by the scruff of your collar and pulls you in."
        scene storeroomblr with vpunch
        show normalcb
        show talkwancb
        show normalmc
        c "Ok [mc], I am actively trying to be less of an asshole towards you. I've got this thing going on here. You know it's bullshit, but it's important to me. So please, don't break my cover here."
        hide talkwancb
        show talksadhappymc
        mc "I just-"
        show talkwancb
        hide talksadhappymc
        c "Look... we went on an adventure, you managed to not molest me in a tent, it was fun and you are a good guy. I just can't risk my persona being... compromised..."
        mc "......"
        c " Hey, I'm just being honest and nobody else here besides you is getting that. Nobody here is my friend. The guys are present dispensers, and the girls are annoying fuckwits. I can't risk losing social status by getting figured out."
        mc "......"
        c "It's nothing personal. It's just school politics."
        show talkwanmc
        mc "...Alright then."
        mc "{i}Should I really ask her for the clothes after all that?"
        menu:
            "Go ahead and ask":
                show talksadhappymc
                mc "I just need one thing from you, then I'll leave you alone at school."
                "Cynthia looks like she is about to yell at you, then she calms herself down and begins to speak through clenched teeth."
                show angryc
                c "I rreeeaally am trying here, [mc]. What the fuck do you want?"
                hide angryc
                mc "I need some of your clothes."
                show wac
                c "......"
                mc "...It isn't for anything weird."
                hide wac
                show angryc
                c"...What the fuck?"
                mc "No really, it's for-"
                c "Nope. I don't wanna know. I don't care. You know what? I actually don't care what you want them for if it means you'll stop bothering me at school."
                mc "Wait, I mean it. It's for this g-"
                c "No! Don't care! I'll leave some clothes in the locker in here tomorrow. Feel free to do whatever you are going to do with them. I wash my hands off this. Don't ever bring it up again!"
                mc "How am I supposed to bring it up again if I'm not supposed to talk to you?"
                c "UGH! Only at school, you nitwit!"
                scene storeroomblr
                show normalmc
                show normalcb
                "Cynthia marches out of the janitor's closet in a huff."
                hide normalcb with easeoutright
                mc "Well... that was interesting... wait... so she does want me to talk to her? Cynthia is... Confusing."
                $ theaclothestimer += 1
                $ findtheaclothes +=1
                $ girlclothes += 1
                jump academy
            "Don't ask her":
                mc "It's fine Cynthia. I get it."
                c "Look, for what it's worth, I think you are a really nice guy. I have an act to upkeep, and something about you..."
                mc "Me?"
                c "Ugh... nevermind. Just avoid me at school, ok?"
                mc "Just at school?"
                c "UGH! See you later!"
                mc "...Ok?"
                "Cynthia glares at you. She looks like she wants to say something. Before she gathers the will to say anything, she abruptly leaves the janitor's closet."
                scene storeroomblr
                show thinkmc
                mc "That was weird... Ah shit, I guess I'll have to go ask somebody else for the clothes then."
                jump academy
    if cynthquest4 > 0 and cynthiaPelt == False:
        c "Oh, [mc], have this."
        $ renpy.notify("{color=#fff}You gained 15 silver")
        $ money += 15
        "She hands you a pouch with money."
        mc "Huh?"
        c "For the pelt."
        mc "Oh, right. Thank you."
        c "No problem, it's yours anyway."
        $  cynthiaPelt = True
        jump academy
    if sawcynth == 6:
        if cynthtrain >= 6:
            show talknc
            c "Hey [mc]."
            show normalcg
            show talknc
            show smilemc
            c "It's better if we don't talk at the Academy."
            c "You know... For your own safety."
            "You notice a few suspicious faces pointed towards your direction."
            show talksadhappymc
            mc "Yeah, ok. I get it."
            mc "Bye."
            show smilenc
            "Cynthia nods."
            jump academy
        show talkwancb
        show smilemc
        c "What do you want, [mc]?"
        menu:
            "Nothing":
                mc "Nothing."
                c "...Seriously?"
                show talkhappymc
                mc "Heh... Yeah."
                jump academy
    show worriedmc
    show normalcb
    show talkwancb
    c "Are you fucking retarded or something? Just in case you are in need of a reminder, I said \"don't talk to me\", got it?"
    jump academy



label cynthiaGuildTalk:
    scene cynthiaroom with fade
    show smilemc
    show talknc
    c "Hey, [mc]."
    if cynthquest4 > 0 and cynthiaPelt == False:
        c "Oh, [mc], have this."
        $ renpy.notify("{color=#fff}You gained 15 silver")
        $ money += 15
        "She hands you a pouch with money."
        mc "Huh?"
        c "For the pelt."
        mc "Oh, right, thank you."
        c "No problem, it's yours anyway."
        $ cynthiaPelt = True
        jump guild
    menu:
        "Talk":
            show talkwamc
            mc "Hey. Just came for a quick visit."
            c "I was wondering when you would show up."
            scene cynthiaroom with fade
            "You spend some time with Cynthia and leave."
            jump guild
        "Call Thea" if thcynthconfess > 4:
            mc "Uhm, I was thinking about calling Thea up here."
            c "Oh... For what exactly?"
            mc "You know...{p}To have some fun."
            c "Threesome?"
            mc "Yes, a threesome."
            c "Wait right here, I'll bring her up."
            show cynthea movie with fade
            th "Ahhh... Ahhhhh...!"
            pause
            c "Mmh...! Yes!"
            th "Keep going, [mc]!"
            pause
            mc "I'm at my limit-"
            pause
            mc "Fuck!!!"
            scene theacynthbase4 with flash
            pause
            scene thecynthsleep1 with fade
            show thecynthsleep3
            c "Hah... That was great."
            th "Yup, I could get used to this. Hehe."
            c "Looks like [mc] is still alive."
            mc "Keeping up with you girls ain't easy."
            c "Eheh, you asked for it."
            mc "Yeah, and I don't regret it."
            "The three of you fall asleep."
            call sleepvars from _call_sleepvars_13
            jump guild
        "Sex":
            show smirkc
            c "Ohhh...... I know that face."
            show cynthsexanimf movie with fade
            pause 6
            c "Ahhh... Ahhhh......"
            window hide
            pause
            c "Harder!"
            pause
            c "Fuck"
            c "Ahhh...... Ahhhh..."
            mc "I'm cumming!"
            menu:
                "Cum inside":
                    mc "Arrhhhh!"
                    scene cynthsexcumin with flash
                    c "Fuuuck!"
                    show cynthsex5
                    c "You came inside."
                    mc "Sorry I-I didn't have time to..."
                    c "It's fine."
                    c "I have a contraception spell on me."
                    mc "Really?"
                    c "Of course. It's essential for pretty girl like me."
                    mc "Right."
                "Cum outside":
                    scene cynthsexcumout with flash
                    mc "Arrhhhh!"
                    c "Jeez, you came all over me."
                    mc "......"
                    show cynthsex5
                    c "I like it."
            scene cynthiaroomn with fade
            c "Ahhh... Perfect way to end the day, don't you think?"
            mc "Yup."
            c "I love you, [mc]."
            "The two of you cuddle and fall asleep."
            scene black
            show text "{color=#fff}End of day [day]." at truecenter
            with dissolve
            pause
            hide text with dissolve
            pause
            call sleepvars from _call_sleepvars_14
            scene cynthiaroom with fade
            "You wake up in the morning. You have some tea with Cynthia."
            "The two of you then go down to the Guild."
            $ time = 0
            jump guild
        "Leave":
            show prot smile
            mc @hopet "Actually, I need to do something else, sorry."
            hide talknc
            show talkwancb
            c "Really?"
            mc @hopet "Yeah, sorry. Bye."
            c "Bye."
            jump guild
