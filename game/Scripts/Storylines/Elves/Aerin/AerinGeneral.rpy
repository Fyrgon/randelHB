default aerinQ = 0

label aerin1:
    hide screen hud
    scene elfgravesaerin with fade
    mc "{i}Is that Aerin?"
    mc "......"
    mc "{i}Is she's crying?"
    mc "{i}Shit, she's coming this way."
    scene elfgravesblrs
    show sada
    show normalmc
    show talkhappymc
    mc "Uhm... hey there, Aerin. My na-"
    a "......"
    show talkna
    hide talkhappymc
    a "S-Sorry, human, I can't talk now. I'm in a hurry."
    hide talkna
    mc "Oh, okay then."
    hide talksadhappymc
    hide sada with easeoutright
    mc "{i}She was crying. I guess I caught her in a bad time."
    mc "{i}I wonder what she's like, I should ask Milly about that."
    $ aerinQ += 1
    jump elfVillage
    ### MC needs to talk to Milly about Aerin

label aerin2:
    show worriedmc
    mc "Hope this goes well."
    play sound doorknock
    "{i}Knock knock"
    "You hear someone run to the door."
    a "Who is it?"
    show talksadhappymc
    mc "It's [mc]."
    a "Who?"
    mc "Uhm... the human."
    show normala
    show angrya
    pause
    show talkwaa
    a "What do you want?"
    hide talkwaa
    mc "I-I thought it'd be a good idea to talk to everyone in the Village, I want to get to know them better."
    hide angrya
    show talkwaa
    hide talksadhappymc
    a "Why?"
    show talksadhappymc
    mc "I guess I just... like talking to people."
    show thinka
    a "......"
    show smilemc
    mc "......"
    show talksada
    hide talkwaa
    a "Wanna come inside then?"
    hide talksada
    show talkhappymc
    mc "Sure."
    scene aerinhouse with fade
    pause 0.5
    mc "Wow, your house looks beautiful."
    a "Th-Thank you!"
    mc "Did you do all this by yourself?"
    a "Uhmm, yeah, most of it."
    mc "Awesome!"
    scene aerinhouseblr
    show smilemc
    show shytalka
    a "So, do you drink tea?"
    mc "Yeah, b-but you don't have to make it. I just came for a small chat."
    a "But it's better if we— I mean, {b}you{/b} had some."
    mc "...Okay then."
    show talksada
    a "Take a seat. I'll bring the tea."
    mc "Thank you."
    hide talksada
    hide shytalka with easeoutleft
    pause 0.5
    show aerinhouse with dissolve
    "You take a seat at a small wooden bench. In front of you is the table where you assume you'll be drinking the tea. The house is small but comfy."
    "Looking behind, you can see the beautiful sunset coming from the small makeshift window. The whole place gives you a warm and welcome vibe."
    "You feel safe in this house, and you like that."
    "Aerin returns holding a tray, with the cup of tea and a small muffin inside, she gently places them on the table."
    scene teaaerin with fade
    mc "Thank you, is this muffin homemade?"
    a "Y-Yes... I bake these kinds of things often."
    "You take a bite."
    scene teaaerin2 with dissolve
    $ persistent.aerinTea = True
    mc "Wow... This is the best thing I've ever tasted!"
    a "There's no need for flattery."
    mc "No, I'm serious, these muffins taste amazing. Do you have some more? Can I take some home?"
    a "Wh-What... Are they really that good?"
    mc "You're joking? Of course they are."
    a "I do have some left. I guess I could give you some, if you like them that much."
    mc "Thank you... thank you so much!!"
    a "N-No problem."
    scene aerinhouseblr
    show smilemc
    show normala
    show talkwamc
    mc "So... care to tell me about yourself?"
    show talkwaa
    a "Huh?"
    mc "Well, you said we could talk, right?"
    a "But, why do you even care? I'm entirely unrelated to you."
    show talkwamc
    mc "So what? I like meeting new people. Don't you?"
    show talksada
    a "...I guess so."
    mc "See? Okay then, let's start."
    a "Alright... Uhm... I am Aerin of Loren. I'm 324 years old-"
    mc "Stop, stop. You can't just give me your autobiography on the spot."
    show talkangrya
    a "Then what do you want?"
    show angrya
    mc "I think it's better if I asked the questions."
    show talkwaa
    a "Go on, then."
    mc "Let's see..."
    mc "So you're 324, right? Which means you're the same age as Eve."
    e "Yes."
    mc "The two of you were friends, right? When you were little?"
    e "...Y-Yeah... I-I don't want to talk about it."
    mc "O-Ok, Uhm..."
    mc "Why don't you tell me about you and Milly? I heard you two are close."
    show talkha
    a "Yeah, we are."
    show thinkmc
    mc "......"
    hide talkha
    hide angrya
    show talkangrya
    a "What?"
    mc "No, I thought I saw you smile..."
    a "Huh? I did smile... What kind of person do you think I am?"
    mc "No... no, it's nothing like that."
    a "You've seen me one time and you're already judging me?"
    mc "No... it's just from what I heard... I thought you were..."
    a "What did they say?"
    show talksadhappymc
    mc "Huh? ...It's just some stuff. Look, I'm sorry I judged you, okay?"
    a "No, just tell me what they said!"
    mc "......"
    mc "They... said that you've been ignoring the Village people ever since your... mother... got banished."
    show sada
    a "......"
    show talksada
    hide sada
    hide talkangrya
    a "They still see me that way..."
    show talkwanmc
    hide talksadhappymc
    mc "Huh?"
    a "It's ju—"
    show talkangrya
    a "You know, I shouldn't have to explain myself to you. I don't even know you!"
    mc "Well, you don't have to, but I'm not part of the Village, am I? Who else can you talk about this with?"
    a "......"
    show talksadhappymc
    mc "Come on, I could be your inside man! I'm really good at giving advice."
    a "Why? Why are you trying to help me?"
    mc "I don't know. It's how I am, I guess."
    show sada
    a "......"
    show talksada
    hide sada
    hide talkangrya
    a "...So you won't talk to anyone about this?"
    mc "Cross my heart."
    show shytalka
    a "Not even with Evelyn?"
    mc "Not a single soul."
    show normalmc
    hide talksadhappymc
    a "{i}Sigh...{/i} It's true what they said. After my mother got banished, I grew to hate the Village. I hated Evelyn's mother, I hated Evelyn, I hated everyone. And then, my brother disappeared."
    a "The Village tried to find him, but they couldn't. I also blamed them for not looking hard enough and for giving up. But as time went on, I realized I was being childish."
    a "I realized that the Village people aren't the ones to blame for my mother's banishment, and that they did their best to find my brother."
    a "But when that happened, it was too late. The Village has already given up on me. And I don't blame them for that it was my fault. I treated them too harshly."
    mc "So you're saying that you don't hate the Village?"
    a " I don't."
    mc "Then why don't you just go and tell them?"
    a "Th-They wouldn't listen."
    mc "They will, trust me. Or at least tell Milly."
    a "I... I can't, I don't know how to talk to people anymore."
    mc "You talk to Milly, don't you?"
    a "I just play games with her, she's just a child."
    mc "{i}Well, she sure doesn't sound like any child I've ever met."
    show talkwamc
    hide talkwanmc
    hide normalmc
    hide thinkmc
    mc "Okay, I know exactly what you need."
    a "What's that?"
    show talksada
    hide shytalka
    mc "We need to work on your... Uhh... What word am I looking for...?"
    mc "Ah! Got it! Your approachability."
    a "My what?"
    mc "Let's start with your appearance."
    a "Wh-What's wrong with my appearance?"
    mc "It's perfect, but it's missing an important detail!"
    a "Like what?"
    mc "A smile."
    a "I do smile."
    mc "Okay, let's see it."
    scene aerinhouseblr
    show thinkmc
    show normala
    a "......"
    show talkwanmc
    mc "So... where is it?"
    show talkwaa
    a "I {b}am{/b} smiling."
    hide talkwaa
    a "......"
    mc "You think you are, but I don't see it. How about you try a little harder."
    a "......"
    show happya with dissolve
    a "......"
    show talkwamc
    mc "There we go, that's better. "
    show talksada
    a "I doubt it'll make a difference."
    mc "Are you kidding me?! You look like a totally different person now!"
    show blushtalka
    a "Pft, stop messing around."
    mc "{i}She's really pretty when she smiles, her eyes totally light up."
    mc "{i}I better leave now though, I've taken up enough of her time. I bet she has a lot of training to do."
    show talksadhappymc
    mc "I guess I'll take my leave now. I bet you have more training to do. It was a lot of fun hanging out with you."
    show shytalkha
    a "Oh, okay."
    mc "Bye then."
    show shytalka
    a "W-Wait, don't you want the muffins?"
    mc "Oh yeah, I forgot about them."
    a "I'll go get them."
    $ aerinmuff += 1
    scene aerinhouseblr
    show thinkmc
    show shytalkha
    hide shytalkha with easeoutleft
    mc "{i}It looks like Aerin is a very good and kind person. I think she's been very lonely for a really long amount of time. I feel bad for her."
    mc "{i}Should I continue helping her, or should I just stop it here and leave? She is Eve's opponent after all."
    menu:
        "Help her":
            mc "{i}I should help her. She's been alone for too long."
            show shytalkha with easeinleft
            a "I'm back. Here you go."
            show talkhappymc
            mc "Wow, that's a lot. Thanks!"
            a "No problem."
            mc "Looks like we made a lot of progress on the first day."
            a "First day?"
            mc "Yeah, are you free tomorrow? We can continue this, if you want to."
            show blushtalka
            a "I-I am free, so y-you want to help me?"
            mc "Yes!"
            show shytalka
            a "But you're on Eve's side. Why are you helping me?"
            mc "This has nothing to do with the duel, I'm just helping you with... your personal issues."
            a "Oh, I see."
            mc "So, am I allowed to assist you?"
            show talkha
            a "Yes!"
            mc "Good, I'll come back tomorrow!"
            show blushtalka
            hide shytalka
            hide talkha
            a "Okay... and [mc], I just wanted to say... thank you... for... helping me."
            a "I didn't know if there was anyone that cared about me, except for Milly, let alone a complete stranger."
            mc "It's nothing. We're not strangers anymore, right?"
            a "I guess not."
            mc "I'm glad to hear that. See you tomorrow!"
            a "Bye... and s-stay safe."
            mc "I will."
            scene elfvillage with fade
            mc "{i}I think I did the right thing!"
            $ aerinQ = 3
            $ time = 4
            jump elfVillage
        "Leave her":
            mc "I should stop this. I've done enough. Besides, I came here to help Eve, that's what I should do."
            show shytalkha with easeinleft
            a "I'm back. Here you go."
            show talkhappymc
            mc "Wow, that's a lot. Thanks!"
            a "No problem."
            mc "Well, goodbye then."
            a "Goodbye."
            a "I-It was nice talking to you."
            mc "Thanks."
            $ dumpaerin += 1
            $ time = 4
            jump elfVillage


label aerin3:
    hide screen hud
    show normalmc
    play sound doorknock
    "{i}Knock knock"
    show happya
    show talkha
    a "Hello [mc]."
    if aerinmeettimer == 2:
        show shytalka
        a "I thought you were supposed to come visit yesterday?"
        show talksadhappymc
        mc "Oh, I'm really sorry, I had this emergency quest!"
        show blushtalka
        a "It's ok, your here now."
    if aerinmeettimer > 2:
        show shytalka
        a "I thought you wouldn't come. You said you'd be here the next day."
        show talksadhappymc
        mc "Oh, I'm really sorry, I had this emergency quest and I just got back today."
        show blushtalka
        a "It's ok, you're here now."
    mc "Looks like you're happy to see me."
    a "I am."
    show surprisedblushmc
    show happya
    pause
    show talkwamc
    show shytalka
    a "What is it?"
    mc "I thought you would be like, \"Eh, whatever\"."
    a "But I am happy to see you."
    mc "Uh-huh. Ok, I appreciate your honesty."
    show blushtalka
    a "Thank you. You are coming in... right?"
    mc "Oh yeah, let's get started."
    scene aerinhouseblr with fade
    show smilemc
    show talkha
    a "I'll bring you some tea."
    mc "Sounds good!"
    hide talkha with easeoutright
    scene teaaerin with fade
    a "Here you go."
    mc "More muffins!"
    a "Yes, I-I baked some more since you... liked them."
    mc "Wow, thanks!"
    a "I'm glad you haven't grown tired of them..."
    mc "Never!"
    a "Hehehe."
    mc "Let's start our lesson then."
    a "I didn't realize this was a lesson! Should I take notes?!"
    show aerinhouseblr
    show talksadhappymc
    mc "Uhh... I don't think taking notes is necessary."
    show blushtalka
    a "That's a relief."
    show happya
    mc "{i}She's taking this more seriously than I thought. Maybe I should lighten up a little bit, this isn't that serious after all."
    mc "Aaaah, I see you've taken that first lesson into consideration."
    show talkha
    a "Huh? ...Oh, yes... I've been practicing my smile... a little bit."
    mc "Hahaha, that's good to hear!"
    a "I thought you wouldn't be able to recognize me."
    mc "I didn't, I thought I was in the wrong house for a moment!"
    show blushtalka
    hide talkha
    hide happya
    a "Hahahaha."
    mc "{i}It's so easy to make her laugh, I should try doing that more often."
    mc "Now to the lesson. Today we'll be talking about your communication skills, or lack thereof."
    "Aerin nods."
    mc "So your problem here is that you're not really honest with your feelings. You have to open up to people more."
    a "O-Okay, I'll try. "
    mc "Let's try it out then. Say something honest about me and don't be embarrassed."
    show shytalka
    a "Uhh..."
    a "Yesterday, when we were talking, it was..."
    mc "Go on..."
    a "It was... disgusting, the way you talked while eating the muffin, made me want to puke."
    show suprised
    mc "......"
    hide suprised
    mc "Uhh, haha, I think we're being a little too honest here."
    a "But you said I should be totally honest and open about my feelings."
    mc "Yeah, but how about we try to lean on to the more... positive things?"
    a "Oh, okay."
    mc "A-And I'm sorry for talking while eating, I-I didn't realize I did that."
    a "It's okay, I avoided looking at your mouth anyway."
    mc "Haah... is that so?"
    mc "{i}Well, that was embarrassing."
    a "Let me try again then."
    mc "Okay."
    mc "{i}Please, let it be something nice."
    show blushtalka
    hide shytalka
    a "I think you're a very nice person."
    show surprisedblushmc
    mc "Th-Thanks!"
    show talkha
    a "Are you blushing?"
    mc "Whaaat?? No..."
    a "Yes you are! Hahaha!"
    mc "I'm not used to getting complimented, okay?"
    a "Hahaha, this is fun. Okay, do me now."
    mc "Huh?"
    a "It's your turn now, go on."
    show talkmc
    hide surprisedblushmc
    mc "Hmm... I think you are the..."
    menu:
        "Prettiest girl":
            show talksadhappymc
            hide talkmc
            mc "Hmm... I think you are the... the prettiest girl I've ever seen!"
            $ aerinrel += 5
            show blushtalka
            hide talkha
            a "You're trying to make me blush..."
            mc "Looks like it worked."
            show shytalkha
            a "Hahah, you're right. It seems like I'm not really used to getting compliments either."
        "Nicest girl":
            show talksadhappymc
            hide talkmc
            mc "Hmm... I think you are the... the nicest girl I've ever met."
            show blushtalka
            hide talkha
            a "Th-Thank you!"
            mc "Look who's blushing now."
            a "Hahah, you're right. It seems like I'm not really used to getting compliments either."
        "Best baker":
            show talkwamc
            hide talkmc
            mc "Hmm... I think you are the... the best baker in Astylla."
            show blushtalka
            show talkha
            a "Oh... Th-Thank you."
            mc "{i}That made her blush? I guess she's not used to getting compliments either."
    mc "I think you understood the lesson, right?"
    a "Yeah."
    mc "Don't be afraid to tell anyone how you feel. And don't be scared to apologize; everyone makes mistakes sometimes."
    mc "Just go tell the Village people you're sorry, and tell them how you really feel."
    a "I-I'll try."
    mc "Sounds good."
    a "So is that all for the lesson?"
    mc "Yeah, I think that's it."
    a "Really? Thank you then."
    mc "No problem. I won't be bothering you anymore then, Aerin. You should really focus on your training."
    a "You're right."
    a " And, [mc]. I just wanted to say that..."
    a "I-I'm really glad that I met you."
    mc "Same here."
    mc "{i}She's so sweet. It's sad that she's in this situation. What would happen if she lost the duel? She'd have to leave and she'd end up all alone."
    mc "{i}Eve has me, Sander and the whole town with her if she loses. Sure, she'll have to lose her sister, but still! I feel bad for Aerin."
    menu:
        "Help Aerin win the duel":
            mc "Aerin, listen. What I'm about to say might sound stupid... but I... I want to help you win the duel!"
            a "Huh? ...Wh-What did you say?!"
            mc "I'll help you to win the duel against Eve."
            a "What?! H-How?"
            mc "I don't know. I'll find a way, I-I'll find some way you could beat her."
            a "But... That would mean you'd be betraying your friend."
            mc "No— ...Yeah, sort of."
            mc "Look, even if Eve loses, she'll still have a lot of people with her. But you... You would be all alone..."
            a "...Why do you care about me so much?"
            mc "B-Because I like you, Aerin."
            a "Like?"
            mc "I want to save you!"
            a "[mc]..."
            a "Th-This is crazy! What if you get caught? Eve would never trust you again! And she'd be furious enough to kill you!"
            mc "I'll make sure I don't get caught!"
            a "......"
            a "I know Eve is stronger than me, and I know I would probably lose the duel. But I-I can't cheat, it would be betraying the very principles of my ancestors."
            a "I'm sorry, [mc]. Words cannot describe how much I appreciate your help, but I can't do it."
            mc "Come on now, Aerin..."
            a "I'm sorry, [mc]. Being the Village Elder was something I swore to my mother I'd do. I can't let that oath be broken."
            mc "{i}Sigh..."
            mc "If that's what you want."
            a "Thank you for understanding."
            mc "I'll go then."
            a "[mc], please feel free to come and visit, okay? It won't bother me at all."
            mc "Okay."
            scene elfvillage with fade
            mc "{i}She refused my help. But I could see it in her eyes, she knew she'd lose the duel without my help."
            mc "{i}I should find a way to help. One without anyone noticing. Not Eve, not Aerin, and most certainly not anyone else in the Village."
            mc "{i}Hmmm... I don't think I can convince Eve to lose on purpose."
            mc "{i}So I got no choice but to make her loose. How do I do it? Eve has to have somekind of weakness, I could use it against her."
            mc "{i}Finding it is the problem. Maybe I can look through Eve's room at the Guild? her house here is prety much empty, so looking there would be pointless."
            mc "{i}Hope July has some spare keys to Eve's room."
            $ aerinpath += 1
            $ aerinQ += 1
            ### AerinOnlyQuestline.rpy
            jump elfVillage
        "Help Eve win the duel":
            mc "{i}I know it's sad, but I can't betray Eve. She's my friend, and she trusts me a lot. I can't betray her trust. I've helped Aerin enough already."
            mc "Goodbye then."
            a "Goodbye, [mc]."
            $ evepath += 1
            jump elfVillage
        "Try to find another way":
            mc "{i}I just can't choose! ...I'll have to find a way where everyone gets to be happy!"
            mc "Goodbye then, Aerin. And good luck with the duel."
            a "Th-Thank you. Please feel free to come and visit, okay? It won't bother me at all."
            mc "Okay."
            scene elfvillage with fade
            mc "This whole banishment thing seems to be the main problem here! I should go and speak to Zenelith and solve this once and for all."
            $ bothpath += 1
            $ aerinQ += 1
            ### AerinTrueQuestline.rpy
            jump elfVillage









label romanceaerin:
    scene aerinhouseblr with fade
    pause
    scene teaaerin with fade
    "You two have a chat while you have your normal cup of tea and Aerin's delicious muffin."
    if evelost == 2:
        $ aerinconfes += 1
        scene aerinhouseblr
        show blushtalka
        show smilemc
        a "Uhm... about that night, I-I really meant it!"
        a "I do love you. Sorry if I don't show it that much. I'm just not used to it, you know?"
        show talksadhappymc
        mc "I know, let's take our time."
        a "Thank you for understanding, [mc]."
        mc "You take care now. I'll come back to help you with your work."
        show shytalkha
        a "Ok. Bye, [mc]."
        $ time += 1
        jump elfVillage
    $ aerinrel += 5
    if aerinrel > 20:
        scene aerinhouseblr
        show shytalka
        show smilemc
        a "So [mc], are you leaving today?"
        menu:
            "Sleep at Aerin's place":
                mc "Yeah, sure, we could have some fun."
                show shytalkha
                a "I was thinking the same thing!"
                scene black with fade
                label aerin_sex_repeat:
                if aerin_one_hour_stand > 0:
                    scene aerinhouseblr with fade
                "The two of you undress and jump on the bed."
                scene aerinsex1 with fade
                pause 0.6
                scene aerinsex2
                pause
                show aerinsexfinal movie
                pause
                a "Aaahhh... why does your dick always feel... this good?"
                pause
                mc "I'm cumming!"
                scene aerinsexcum with flash
                pause 0.5
                scene aerinsexcum with flash
                scene aerinasslick1 with fade
                a "I love you, [mc]."
                mc "I love you too."
                scene black with fade
                if aerin_one_hour_stand == 0:
                    "The two of you cuddle up and fall asleep."
                    call sleepvars from _call_sleepvars_2
                    scene black with fade
                    "When you wake up, Aerin's already gone. You sit on the bed and take a look around. She might have gone off to work but you think about how satisfied you feel after that eventful night."
                else:
                    $ aerin_one_hour_stand = 0
                    mc "{i}What a break... Aerin is possaionate when riding me."
                    $ time += 1
                jump elfVillage
            "Go home":
                mc "Sorry Aerin, I won't be able to stay with you today."
                show shytalkha
                a "Oh, it's ok. Take care then."
                mc "You too."
                $ time = 4
                jump elfVillage



    if aerinrel == 20:
        label aerin_sex_first:
        scene aerinhouseblr
        show shytalka
        show smilemc
        a "[mc]... I... want to have sex with you."
        show surprisedblushmc
        mc "{i}She's really direct with these kinds of stuff."
        mc "Are you sure about this?"
        show shytalkha
        a "Yes, I think it's time I finally make you feel good."
        mc "{i}I can't believe it's finally happening!"
        a "Follow me."
        scene black with fade
        "You go with Aerin to her room. The both of you remove your clothes."
        a "Lie down on the bed."
        mc "O-Ok."
        a "Wow, your sexual organ is so big. I'm supposed to put this whole thing in me... right?"
        mc "Y-Yeah, and it's called a dick."
        scene aerinsex1 with fade
        a "Right, your dick. I'm going to put it in me now."
        scene aerinsex2 with hpunch
        a "Ahhhh... this is amazing!"
        mc "{i}So tight!"
        show aerinsexfinal movie
        pause
        a "I can't stop moving my hips... Aaahhhh!"
        a "Does it feel good?"
        window hide
        pause
        mc "Y... Yes...!"
        a "Your dick feels sooooo good!"
        mc "Ahhh... slow down... Aerin! I think I'm going to cum!"
        pause
        a "Do it! Cum inside me, give me your seed!"
        pause
        mc "Agh!!!"
        scene aerinsexcum with flash
        pause 0.05
        scene aerinsexcum with flash
        pause
        scene aerinasslick1 with fade
        a "That... was... amazing... Sex is amazing!"
        mc "It really was."
        a "Did I make you feel good?"
        mc "Yes... you were amazing..."
        a "Hehehe... thanks!"
        a "Umm... [mc]. I know, you being in the outside world and all. You might do this with a lot of women...."
        mc "Aerin, I-"
        a "It's okay, I understand. You are a human, after all... but all I ask is to remember me... To remember the time we had together."
        mc "I will, I promise!"
        a "I'm glad."
        scene black with dissolve
        if aerin_one_hour_stand == 0:
            scene black with dissolve
            "The two of you cuddle up and fall asleep."
            call sleepvars from _call_sleepvars_3
            scene aerinhouseblr with fade
            "When you wake up, Aerin's already gone. You sit on the bed and take a look around. She might have gone of to work but you think about how satisfied you feel after spending the night with her."
        else:
            $ aerin_one_hour_stand = 0
            mc "She is always so wild. I can't get enough of her."
            $ time += 1
        jump elfVillage

    if aerinrel == 15:
        scene aerinhouseblr
        show shytalkha
        show talksadhappymc
        a "Uhm, [mc], do you want to... continue from where we left off last night?"
        mc "Y-Yes!"
        scene black with fade
        label aerin_sex_licking:
        "You go to Aerin's room. Aerin undresses. She lies on her bed fully naked. You take a moment to admire her shape and curves and beautiful body, down from the supple skin to the details of her buttocks."
        scene aerinasslick1 with fade
        a "What are we going to do today?"
        scene aerinasslicka5 with vpunch
        a "Hey! At least give me a warning!"
        show animationaerinlick
        mc "Sorry, I couldn't resist that juicy ass."
        a "Aaahhh... don't say that..."
        pause
        a "Aaahhhhh... I think I'm going to cum again!"
        pause
        scene aerinasslicka7 with flash
        pause 0.05
        scene aerinasslicka7 with flash
        a "I'm cumming!!!!!!!!!"
        scene aerinasslick1 with fade
        a "I didn't even return the favor and make you feel good today. I'm such a terrible lover..."
        mc "Hey! It felt good licking your ass."
        a "Don't say that... It sounds... dirty..."
        mc "Hahahaha. But I know you like it."
        a "I... kinda do!"
        mc "It's getting dark, time for me to go then... Take care, ok?"
        a "You'll come back tomorrow, right?"
        mc "Yeah, I will. Can't live without me, huh?"
        a "YES!!!"
        mc "Hehehe..."
        $ time = 4
        jump elfVillage



    if aerinrel == 10:
        scene aerinhouseblr
        show shytalka
        show smilemc
        a "So [mc], about us... I was thinking... since... now we are together, I thought we could do... stuff?"
        mc "Like what?"
        a "You know... the things lovers do..."
        show talksadhappymc
        mc "Like go on dates? Yeah sure, I would love to-"
        a "No... I mean things like..."
        show blushtalka
        a "Things like... seeing each other naked."
        show thinkmc
        mc "{i}Did I hear that right?"
        hide thinkmc
        mc "Wh-What- I think I-I misheard y-you-"
        a "I said we... should... see each other naked."
        show surprisedblushmc
        mc "{i}Oh Astylla, I think I'm going to faint!"
        mc "Oh, hahahahaha! ...I-I thought you wanted to take things s-slow, right?"
        show shytalkha
        a "Well, it was you who said that. And you told me to be honest with my feelings. So I feel like we shouldn't stall. If we love each other, there's no reason to wait."
        mc "{i}gulp{/i} You're right, but are you sure about this?"
        a "Yes. So... what do you say?"
        show talksadhappymc
        mc "If that's what you want, I'm fine with it."
        label aerin_sex_fingering:
        a "Let's go to my room then."
        scene black with fade
        "You go to Aerin's room. Aerin undresses. She lies on her bed fully naked. You take a moment to admire her shape and curves and beautiful body, down from the supple skin to the details of her buttocks."
        scene aerinasslick1 with fade
        pause
        mc "Wow... you... look beautiful!"
        a "Th-Thank you."
        scene aerinasslick1 with fade
        a "I really have no experience with these kinds of things. [mc], I leave the rest to you."
        mc "{i}gulp. Who does she think I am? I've got no experience either!"
        mc "O-Ok."
        a "I know I said we shouldn't stall but I-I... don't want to rush things either."
        mc "I-I understand."
        menu:
            "Finger her":
                scene aerinasslicka1 with dissolve
                a "Th-That's my... W-What are you doing?"
                mc "Just, relax I'm going to make you feel good."
                a "But... I want to make you feel good too-"
                show animationaerinfinger
                a "Aaaahhhh...!"
                pause
                window hide
                mc "Do you like it?"
                a "Yes! It feels good... Ahhh!"
                mc "{i}She's getting really wet."
                a "Aaaahhhh... wait... I feel something...!"
                pause
                mc "You're going to cum."
                a "I'm going... to... what?"
                a "You're going faster... my pussy... Aaaahhhhhh... I'm cumming!!!!!"
                hide animationaerinfinger
                scene aerinasslicka4 with flash
                pause 0.05
                scene aerinasslicka4 with flash
                a "Aaaahhhhhhhhhh!!!!!!!"
                a "{i}huff... huff... huff..."
                scene aerinasslick1 with fade
                a "That felt amazing, [mc]!"
                mc "I'm glad you liked it."
                a "I feel sleepy..."
                mc "I think we've done enough for today then..."
                a "But I didn't make you feel good."
                mc "It's ok, we'll do this again tomorrow."
                a "O-Ok... see you tomorrow."
                scene elfvillagen
                mc "{i}That was amazing! I didn't get much action though. Still, I think Aerin had a good time!"
                $ time = 4
                jump elfVillage
    mc "Thanks for the tea, Aerin."
    a "You're welcome!"
    mc "I'll see you tomorrow then."
    a "Ok, bye [mc]."
    mc "Bye, Aerin!"
    $ time = 4
    jump elfVillage
