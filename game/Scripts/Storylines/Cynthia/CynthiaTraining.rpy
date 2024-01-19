label CynthiaTraining:
    if cynthtrain == 0:
        show talkwamc
        show smilenc
        mc "I'm here for training?"
        show talkwacb
        c "Ahh, good."
        c "Let's go to the forest."
        play music forest
        scene forest with fade
        "You follow Cynthia as you two make your way to the forest. After some time, you come into a clearing."
        show talkwanmc
        show smilenc
        mc "So, what are we supposed to do?"
        show talkwacb
        c "We're going to race."
        mc "I thought you were supposed to be training me."
        c "This IS training."
        c "Trust me, this is the best way to improve your speed."
        mc "Ok then."
        hide talkwacb
        c "Great."
        scene forest with fade

        "Cynthia draws a starting line on the ground."
        c "We'll start here. There's the finish line."
        "She points to a tree far away. You nod, setting sight on the location."
        "Cynthia gets into position, stretching her legs out and her hands planted on the ground."
        c "Ready?"
        "You get into position as well, matching her posture."
        c "Try your best to beat me, alright?"
        menu:
            "Easy.":
                $ easycynth += 1
                mc "Easy."
                c "Hehe, we'll see."

            "Alright.":
                mc "Alright."
                c "Good."
        play music motivational
        c "We'll start on three."
        c "One..."
        c "Two..."
        c "THREE!!!"
        scene trainingcynth1
        "You start off running but you're not sure you can get your legs to run as fast as you can carry. More like flopping your legs wildly."
        show trainingcynth2 with easeinright
        "You can see Cynthia making a break for the tree. She runs like a real athlete compared to you, making use of her arms and legs."
        hide trainingcynth2 with easeoutright
        "As she reaches her destination, you could feel yourself let down as you quickly exhaust yourself."
        "Cynthia wins!"
        scene forrest with fade
        if easycynth == 1:
            show talkwacb
            c "That was easy, wasn't it?"
            "You're still recovering as you take deep breaths."
            c "Hehehe..."
            c "You'll need a lot of work."
        else:
            show talknc
            c "Looks like we'll have a lot of work to do."
            "You're still recovering as you take deep breaths."
        scene forrest
        show talknc
        c "Alright, get your ass up. It's time for the second lap."
        show suprised
        mc "HUH?!"
        show talkwacb
        c "Come on!"
        scene trainingcynth1 with fade
        show trainingcynth2 with easeinright
        "The two of you run more. And as if it wasn't bad enough, you've already gone past your limit."
        mc "{i}Wheeze... Wheeze... Wheeze..."
        stop music fadeout 0.9
        scene forest with fade
        show talknc
        show worriedmc
        c "{i}huff... huff...{/i} Ok, that's enough for today."
        hide worriedmc with hpunch
        play music forest
        "As soon as you hear those words, you fall to the ground."
        scene restcynthia with fade
        $ persistent.cynthiaTraining = True
        "Cynthia sits beside you."
        c "You did good today."
        mc "{i}huff... huff..."
        mc "You call repeatedly losing to you, “good”?"
        c "Well, you kept up till the end."
        c "Did you really think you could beat me? That wasn't the point."

        mc "{i}huff... huff...{/i} if you say so..."
        c "......"
        c "We'll have to keep training."
        mc "{i}huff... huff..."
        mc "Ok, just give me a few more... minutes."
        c "Hehe. I mean tomorrow."
        c "I'm not in the mood for killing a good little boy like you today. Where's the fun in torturing you if you croaked?"
        mc "Oh... thank... god!"
        c "......"
        c "Here..."
        "Cynthia hands you her bottle in earnest."
        mc "What is it?"
        c "Drink up, it'll help to get some of your energy back."

        mc "{i}She really doesn't mind about sharing her bottle with me, huh?"
        "You take the bottle. You start to take a sip of it."

        "It tastes like water but you feel a little sweetness in it as well. It also adds a refreshing feel to it being cold."
        mc "Mmmh... thanks!"

        c "Go on, take a few more sips."
        mc "......"
        "As you take a couple more sips, the cooling liquid seem to fill your already exhausted body. You start to feel refreshed."
        "After that, you hand her back her bottle."
        c "How do you feel?"
        mc "I feel good. What was that?"
        c "Hehehe. It's a special mix of mine."
        mc "What do you put in it?"
        c "Well, it won't be special if I told you now, won't it? You'll sell out my recipe."
        mc "Fine, then."
        "Cynthia takes a few sips as well."
        c "Mhh..."
        mc "So how long are you thinking about staying here?"
        c "Huh? That came out of nowhere."
        mc "Just asking."
        c "...I don't know. Until I feel like it."
        c "The Guild in Randel is really good. Do you know that there are a very few Adventuring Guilds in Astylla?"
        mc "Really?"
        c "Yeah. The only other Guild I've seen is in Dorn. But you could hardly call that a Guild."
        c "It's more like a mercenary hide-out."
        mc "So, you like it here?"
        c "Yeah, it's not bad."
        c "Why, [mc], are you scared that I might leave you?"
        mc "No!"
        c "Hahaha!"
        c "Don't worry, I won't be leaving any time soon."
        mc "......"
        c "Ahh... Ok, I think I've wasted enough time here. Why don't we head back?"
        c "Can you walk?"
        mc "Of course I can walk!"
        c "Let's go then."
        scene villageback with fade
        "The two of you head back to Randel."
        show normalcg
        show smilemc
        mc "See you tomorrow then."
        c "Hmm?"
        hide normalcg
        show talknc
        c "Oh yeah, you don't have a Guild room."
        c "Bye, then."
        c "Don't be late."
        show talkwamc
        mc "Alright."
        hide talknc with easeoutleft
        hide talknc
        mc "Urgh, my legs are killing me."
        mc "I don't think I'll be able to beat her in this lifetime."
        mc "I feel like she's starting to open up to me."
        mc "Alright, [mc]! You're hanging out with the hottest girl in the Academy! Yeah!"
        show thinkmc
        mc "......"
        show worriedmc
        mc "{i}...sigh.{/i}You're a sad man, [mc]."
        $ cynthtrain += 1
        $ time = 4
        jump home
    if cynthtrain == 1:
        show talkwamc
        show normalcg
        mc "I'm here."
        show talknc
        c "Let's go then."
        play music forest
        scene forest with fade
        "The two of you head to the forest and start that grueling training again."
        scene trainingcynth1 with fade
        show trainingcynth2 with easeinright
        "After a few rounds, you're still unable to beat Cynthia. Yet she still has that energy to beat you."
        hide trainingcynth2 with easeoutright
        pause 0.5
        scene forest with fade
        mc "{i}huff... huff... huff..."
        c "...Good work today."
        c "We'll need to keep training."
        mc "{i}huff... huff..."
        scene restcynthia
        "The two of you sit on the shade under a tree and rest. Cynthia hands you her special mix, as if she knew you needed it right now."
        c "What did you really see that day?"
        mc "What day?"
        c "The glob, what did it show you?"
        mc "I thought I was supposed to erase it from my mind."
        c "Yeah but I'm curious. Did it look real?"
        mc "Uhm... Y-Yeah."
        c "What did you see exactly? I know you saw my tits."
        c "But how were you fooled? Why did you follow it so easily?"
        mc "I-I..."
        c "......?"
        c "Ok, by the color of your face, I can tell that you aren't comfortable talking about it."
        mc "Well, yeah, obviously. Aren't you."
        c "Why would I be embarrassed?"
        mc "I'm talking about your... ti..."
        c "You can't even say it! Hahaha."

        mc "......"
        c "Well, first of all, that wasn't me to begin with. And second, you've already seen them. If I were to be embarrassed, it's probably too late. And I would probably trash your ass about it. I've lost that motivation anyway."
        mc "Yeah, yeah... But still..."
        c "Fine, I won't ask you."
        c "But why did it show you me?"
        c "You were fantasizing about me, weren't you?"
        mc "NO!"
        c "Or It might have played a past memory of yours."
        mc "Can we just stop talking about this? It's very uncomfortable."
        c "Alright, alright. It's just fascinating to me, that's all."
        c "Don't you think?"
        mc "Yeah, kind of."
        c "You can wear the toughest armor or have the strongest blade but if you can't protect your mind, you're fucked. You ought to have covered all the fields to be fully prepared, both mind and body. "
        mc "Mh..."
        if killledric >= 1:
            mc "I've fought a similar monster that uses the same technique. That almost appeared to me as human until I saw past its lies."
            c "Really, what's it called?"
            mc "Ledric."
            c "Wait, wait, you're telling me you took down a Ledric by yourself?"
            mc "Not by myself, I was with Eve."
            c "Ahhh..."
            c "Who's Eve?"
            mc "Evelyn, the elf with the creepy guy."
            c "Oh, her."
            c "......"
            c "Ledric, a class B monster. That's pretty impressive."
            mc "I barely did anything, though. I just acted as..."
            mc "Bait."
            c "Hahah. See? It's your calling."
            mc "Yeah, yeah."
        "The two of you rest in silence for a while."
        c "Time to go."
        mc "Ok."
        c "We'll continue this tomorrow."
        mc "......"
        c "You're coming right?"
        mc "Yeah, yeah."
        c "Good."
        c "See you tomorrow then."
        mc "Bye."
        c "......"
        "You watch Cynthia leave. After that, you head back home."
        $ cynthtrain += 1
        if chartrait == 3:
            $ cynthtrain = 3
        $ time += 1
        jump home
    if cynthtrain == 3:
        show talkwamc
        hide talknc
        show talkwacb
        mc "Ready for training."
        c "Good. I thought you'd given up."
        c "Come on, let's go."
        play music forest
        scene trainingcynth1 with fade
        show trainingcynth2 with easeinright
        "The two of you head to the forest and start another round of rigorous training."
        "You are still unable to beat Cynthia, again. After that, you run several rounds."
        "Despite the trials, you don't feel as tired as before. Most likely improving."
        hide trainingcynth2 with easeoutright
        pause 0.5
        scene forest with fade
        mc "{i}huff... huff... huff..."
        c "How do you feel?"
        c "...Are we making progress?"
        mc "{i}huff... huff...{/i} I guess so."
        c "You see? ...Just need to keep on going."
        mc "Ahh... Alright."
        scene restcynthia
        "The two of you sit on the shade under a tree and rest. Cynthia hands you her special mix. You feel refreshed after that."
        mc "You think anyone from the Academy has seen us together?"
        c "You scared?"
        if chartrait == 2:
            mc "No."
            c "Oh tough guy."
        else:
            mc "A bit, yeah."
            c "Hehe."
        c "I chose the forest especially because no one would see us. So, I think you're safe... for now."
        mc "Oh... good to know."
        c "Anyway, it's getting dark. We better get going."
        mc "Yeah."
        c "See you tomorrow."
        mc "Right. Bye."
        c "......"
        "Cynthia leaves waving her hand without saying anything."
        "You head back home."
        $ cynthtrain += 1
        if chartrait == 3:
            $ cynthtrain = 6
        $ time += 1
        jump home
    if cynthtrain == 6:
        show talkwamc
        show normalcg
        mc "Here for more training, ma'am."
        show talkwacb
        c "Good. I see you're starting to like this."
        play music forest
        scene forest with fade
        "The two of you head to the forest and start more training. You feel prepared for this."
        c "Ok, we've been training for about a week now. I need you to give your best."
        play music motivational
        mc "Alright."
        "The two of you get ready into position."
        c "One..."
        c "Two..."
        c "THREE!"
        scene trainingcynth1 with fade
        show trainingcynth2 with easeinright
        "You bolt forward. Cynthia sprints like an athlete while you're running as fast as you can."
        hide trainingcynth2 with easeoutright
        "You keep running at the same pace, trying you're hardest not to fall behind."
        mc "{i}Come on!"
        mc "{i}Gotta push a little more!"
        "You start to feel your chest tighten. You're losing you're breath."
        mc "{i}Ugh..."
        mc "{i}I can't!"
        c "Come on slowpoke!"
        mc "{i}Huh?"
        c "You're almost there! Keep it up!"
        c "Aren't you fed up losing to me every time? I thought I trained you to be far better than that!"
        c "Stop TRYING to beat me and actually BEAT ME!"
        mc "{i}...Yeah, just a little more!"
        mc "{i}Gotta push! I have to beat her!"
        show trainingcynth2 with easeinright
        pause 0.3
        show trainingcynth2 with hpunch
        mc "Not today!"
        c "Hehehe. Yeah, that's the spirit!"
        "You keep running as best as you can. Though you're unable to pass her but you keep running at the same pace until you reach the finish line."
        scene forrest with fade
        show talksadhappymc
        show talknc
        mc "{i}wheeze... wheeze... "
        c "{i}huff... huff... huff..."
        "Cynthia punches you on the shoulder."
        hide talknc
        show smirkc
        c "You did it!"
        mc "{i}huff... huff...{/i} thanks..."
        c "All that training finally paid off, eh?"
        mc "...Yeah... but I still couldn't beat you."
        show talkwacb
        c "Well, you can't do the impossible just yet."
        mc "{i}huff... huff..."
        show talknc
        c "But I gotta say, you pushed me quite a bit."
        mc "...I'm honored, great master."
        c "You should be, my young student!"
        hide talknc
        c "What do you say, a couple more rounds?"
        show talkwamc
        mc "You're on!"
        c "Hehehe, ok then!"
        scene trainingcynth1 with fade
        show trainingcynth2 with easeinright
        "The two of you run some more. You're still unable to beat Cynthia."
        "But somehow, you don't feel out of shape as you're used to. You feel less exhausted."
        "After running your rounds, the two of you lie on the grass."
        scene restcynthia with fade
        play music forest
        "You're definitely gasping for air."
        mc "{i}wheeze... wheeze... "
        c "{i}huff... huff... huff..."
        c "You alright there...?"
        mc "...Yeah... {i}huff{/i}... Some of your special mix would be good right about now."
        c "Huh, I forgot to bring it..."
        mc "Ahh, damn it."
        c "Just kidding."
        "She hands you the bottle. You graciously take it and gulp the liquid down."
        c "HEY! Leave some for me, you idiot!"
        mc "Sorry... I was thirsty."
        c "Give it here."
        "Cynthia takes the bottle and takes a few sips."
        c "Today was really good. You've made a lot of progress."
        mc "Th-Thanks."
        c "I think we can go on another monster hunt now."
        mc "Really?"
        c "Yeah."
        c "You've proved that you aren't useless as you used to be. So I guess you're ready."
        mc "Uh-huh, can you at least tell me what we're hunting this time?"
        c "Sure. I told you no more surprises, right?"
        c "I was thinking we could hunt a dire wolf."
        if chartrait == 1:
            play sound chime
            $ renpy.notify("{color=#fff}Bookworm check:{/color} {color=#00C413}Success!")
            mc "Oh, I've read about them."
            mc "They're like wolves but much bigger."
            c "Yup."
            mc "And their pelts are worth quite a lot."
            c "Exactly."
            c "You've read a lot about monsters I see."
            mc "Kinda. I used to read a lot of books when I was a kid."
            c "A bookworm I see."
            mc "Y-Yeah."
            c "Good for you."
        else:
            play sound chime
            $ renpy.notify("{color=#fff}Bookworm check:{/color} {color=#A50000}Fail.")
            mc "Ahhh...?"
            c "{i}Sigh{/i}... It's a wolf but much bigger."
            mc "Oh... ok."
            c "And their pelts are worth quite a lot."
            mc "Nice."
            c "Yeah."
        mc "So when are we leaving?"
        c "Tomorrow?"
        c "Or any day you can. Come talk to me in the afternoon whenever you feel ready."
        mc "Ok."
        mc "{i}That's unusually nice of her."
        c "Great."
        scene forest with fade
        c "I'll be leaving now. Got some work to do."
        mc "Alright. I should be going too."
        "The two of you get up."
        show smilemc
        show smilenc
        mc "......"
        c "......"
        show talksadhappymc
        mc "So the training is officially over?"
        show talknc
        c "Well, yeah. You can still practice on our own. You won't be needing me."
        c "Just try to maintain your speed."
        hide talknc
        mc "Alright."
        mc "......"
        mc "Thanks, Cynthia, for all of this."
        mc "I didn't expect it but you really helped me a lot."
        show sadc
        pause 0.5
        show talknc
        c "...Uhm... N-No problem."
        c "Alright... I-I should be leaving now."
        mc "Right, bye."
        c "......"
        c "Bye, [mc]."
        hide talknc
        hide smilenc
        hide sadc with easeoutright
        "You watch Cynthia leave. After that, you head back home."
        show thinkmc
        mc "{i}Why did she act so strange after I thanked her? That's so not like her."
        mc "{i}Granted, she was a cold bitch before and never liked me... Feels good now she's being nicer to me."
        mc "{i}But what is she really like though?"
        mc "{i}......"
        mc "{i}I think we've grown a lot closer now but I feel like there's still something more that she's holding back."
        mc "{i}sigh"
        mc "{i}We'll just have to wait and see where this goes."
        $ cynthtrain += 1
        $ time += 1
        jump home
    else:
        show talkwamc
        mc "Ready for training."
        show talknc
        c "Alright."
        c "Let's go."
        play music forest
        scene trainingcynth1 with fade
        show trainingcynth2 with easeinright
        "The two of you head to the forest and start training. As usual, it's a race."
        "You are still unable to beat Cynthia. You run several rounds and try to get better."
        "After a few rounds, you don't feel as tired as before."
        hide trainingcynth2 with easeoutright
        pause 0.5
        scene forest with fade
        mc "{i}huff... huff... huff..."
        c "Alright, that's enough for today."
        scene restcynthia with fade
        "The two of you sit on the shade under a tree and rest. Cynthia hands you her special mix. You feel refreshed after that."
        "After a while, the two of you bid farewell and leave. You watch her go and you then make your way back to your abode."
        $ cynthtrain += 1
        $ time += 1
        jump home
