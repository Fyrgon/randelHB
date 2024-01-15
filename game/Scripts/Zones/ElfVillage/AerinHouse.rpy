label aerinHouse:
            stop music
            hide screen hud
            if time == 4:
                mc "I shouldn't bother her at this time."
                jump elfvillage
            if sawaerin == 2:
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
                mc "I-I thought it'd be a good idea to talk to everyone in the village, I want to get to know them better."
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
                a "But it's better if we- I mean, you had some."
                mc "...Okay then."
                show talksada
                a "Take a seat. I'll bring the tea"
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
                mc "No, I'm serious, these taste amazing. Do you have some more? Can I take some home?"
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
                a "Alright... Uhm... I am Aerin of Loren. I'm 324 years ol-"
                mc "I'm not asking for an autobiography."
                show talkangrya
                a "Then what do you want?"
                show angrya
                mc "I think it's better if I asked the questions."
                show talkwaa
                a "Go on, then."
                mc "Let's see..."
                mc "So you're 324,  right? Which means your the same age as Eve."
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
                mc "They... said that you've been ignoring the village people ever since your... mom... got banished."
                show sada
                a "......"
                show talksada
                hide sada
                hide talkangrya
                a "They still see me that way..."
                show talkwanmc
                hide talksadhappymc
                mc "Huh?"
                a "It's ju-"
                show talkangrya
                a "You know, I shouldn't have to explain myself to you. I don't even know you!"
                mc "Well, you don't have to, but I'm not part of the village, am I? Who else can you talk about this with?"
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
                a "{i}Sigh...{/i} It's true what they said. After my mother got banished, I grew to hate the village. I hated Evelyn's mother, I hated Evelyn, I hated everyone. And then, my brother disappeared."
                a "The village tried to find him, but they couldn't. I also blamed them for not looking hard enough and for giving up. But as time went on, I realised I was being childish."
                a "I realised that the village people aren't the ones to blame for my mother's banishment, and that they did their best to find my brother."
                a "But when that happened, it was too late. The village has already given up on me. And I don't blame them for that it was my fault. I treated them too harshly."
                mc "So you're saying that you don't hate the village?"
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
                mc "We need to work on your- Uhm... what am I looking for here?"
                mc "Got it! ...Your approachability."
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
                mc "Sooo, where is it?"
                show talkwaa
                a "I am smiling."
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
                a "Hehe, stop messing around."
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
                        a "But your on Eve's side. Why are you helping me?"
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
                        $ sawaerin += 1
                        $ time = 4
                        jump elfvillage

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
                        jump elfvillage

            if sawaerin ==3:
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
                a "{i}Nods{i} Hmmm..."
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
                mc "Yeah, but, how about we try to lean on to the more... positive things?"
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
                    "Prettiest girl.":
                        show talksadhappymc
                        hide talkmc
                        mc "Hmm... I think you are the... the prettiest girl I've ever seen!"
                        show screen notice
                        pause
                        $ aerinrel += 5
                        hide screen notice
                        show blushtalka
                        hide talkha
                        a "You're trying to make me blush..."
                        mc "Looks like it worked."
                        show shytalkha
                        a "Hahah, you're right. It seems like I'm not really used to getting compliments either."
                    "Nicest girl.":
                        show talksadhappymc
                        hide talkmc
                        mc "Hmm... I think you are the... the nicest girl I've ever met."
                        show blushtalka
                        hide talkha
                        a "Th-Thank you!"
                        mc "Look who's blushing now."
                        a "Hahah, you're right. It seems like I'm not really used to getting compliments either."
                    "Best baker.":
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
                mc "Just go tell the village people you're sorry, and tell them how you really feel."
                a "I-I'll try."
                mc "Sounds good."
                a "So is that all for the lesson?"
                mc "Yeah, I think that's it."
                a "Really? Thank you then."
                mc "No problem. I won't be bothering you anymore then, Aerin. You should really focus on your training."
                a "You're right."
                a " And [mc],I just wanted to say that..."
                a "I-I'm really glad that I met you."
                mc "Same here."
                mc "{i}She's so sweet. It's sad that she's in this situation. What would happen if she lost the duel? She'd have to leave, She'd be all alone."
                mc "{i}Eve has me, Sander and the whole town with her if she loses. Sure, she'll have to lose her sister, but still! I feel bad for Aerin."
                menu:
                    "Help Aerin win the duel":
                        mc "Aerin listen, what I'm about to say might sound stupid... but I... I want to help you win the duel!"
                        a "Huh? ...Wh-What did you say?!"
                        mc "I'll help you to win the duel against Eve."
                        a "What?! H-How?"
                        mc "I don't know. I'll find a way, I-I'll find some way you could beat her."
                        a "But that would mean you'd be betraying your friend..."
                        mc "No-Yeah, sort of... Look, even if Eve loses, she'll still have a lot of people with her. But you-you would be all alone..."
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
                        a "I'm sorry, [mc]. Being the village elder was something I swore to my mother I'd do. I can't let that oath be broken."
                        mc "{i}Sigh..."
                        mc "If that's what you want."
                        a "Thank you for understanding."
                        mc "I'll go then."
                        a "[mc], please feel free to come and visit, okay? It won't bother me at all."
                        mc "Okay."
                        scene elfvillage with fade
                        mc "{i}She refused my help. But I could see it in her eyes, she knew she'd lose the duel without my help."
                        mc "{i}I should find a way to help. One without anyone noticing. Not Eve, not Aerin, and most certainly not anyone else in the village."
                        mc "{i}Hmmm... I don't think I can convince Eve to lose on purpose."
                        mc "{i}So I got no choice but to make her loose. How do I do it? Eve has to have somekind of weakness, I could use it against her."
                        mc "{i}Finding it is the problem. Maybe I can look through Eve's room at the Guild? her house here is prety much empty, so looking there would be pointless."
                        mc "{i}Hope July has some spare keys to Eve's room."
                        $ aerinpath += 1
                        $ sawaerin += 1
                        jump elfvillage
                    "Help Eve win the duel":
                        mc "{i}I know it's sad, but I can't betray Eve. She's my friend, and she trusts me a lot. I can't betray her trust . I've helped Aerin enough already."
                        mc "Goodbye then."
                        a "Goodbye, [mc]."
                        $ evepath += 1
                        jump elfvillage
                    "Try to find another way":
                        mc "{i}I just can't choose! ...I'll have to find a way where everyone gets to be happy!"
                        mc "Goodbye then, Aerin. And good luck with the duel."
                        a "Th-Thank you. Please feel free to come and visit, okay? It won't bother me at all."
                        mc "Okay."
                        scene elfvillage with fade
                        mc "This whole banishment thing seems to be the main problem here! I should go and speak to Zenelith and solve this once and for all."
                        $ bothpath += 1
                        $ sawaerin += 1
                        jump elfvillage
            scene aerinhouseblr
            show talkha
            show smilemc
            a "Oh [mc], you're back."
            mc "Hey."
            menu:
                "Talk":
                    mc "I see you quite often at the elf graveyards."
                    a "Oh, yeah."
                    mc "Why?"
                    show talksada
                    a "I'm going to my brother's grave when I feel... {p}...Lonely."
                    show worriedmc
                    mc "I thought your brother was missing."
                    a "That's what they say to make me feel better. I know he's gone. He said he would never leave me alone. He said we'd always be together until death."
                    a "The reason why he isnt here is because he's... dead."
                    mc "I'm sorry, Aerin."
                    a "It's ok, [mc]. It still comforts me thinking about him, so I visit his grave every day."
                    show shytalka
                    a "Ah, sorry. I made it depressing, didn't I?"
                    mc "Oh, no, no. Haha."
                    show shytalkha
                    a "I know, why don't we have some tea to lighten the mood?"
                    show talksadhappymc
                    mc "That's a good idea."
                    scene teaaerin
                    "You have a cup of tea and a muffin. After that, you take your leave."
                    jump elfvillage
                "Leave":
                    mc "Just came to check on you."
                    a "Is it that or do you want more cupcakes?"
                    mc "You got me."
                    a "Hahaha."
                    scene teaaerin
                    "You have a cup of tea and a muffin. After that, you take your leave."
                    jump elfvillage
