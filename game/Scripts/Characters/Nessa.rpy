label nessatalk:

    menu:
        "Leave":
            jump elfvillage

        "Sex?" if sexnessa == 1 :
            scene jail
            show normaln
            show smilemc
            mc "Sex?"
            show sedtalkn
            n "Yes, please!"
            show nessasex movie with fade
            window hide
            pause
            n "Ahn... This dick is the best!"
            pause
            mc "Uurrgh..."
            n "Ahh...! You better come here ever day!"
            mc "Ha... O-Ok."
            pause
            mc "I'm going to cum!"
            n "Cum... Cum for me, [mc]!"
            scene nessacum with flash
            pause 0.05
            scene nessacum with flash
            scene jail with fade
            show sedtalkn
            show smilemc
            n "Hahh... Just what I needed. Thanks, [mc]!"
            mc "Happy to help... and thank you for letting me walk out of the prison."
            n "I could go for another round if you want?"
            menu:
                "Why not?":
                    show talkwamc
                    mc "Let's do it."
                    n "Hehehe. Look who's all grown up now?"
                    show nessasex movie with fade
                    pause
                    "The two of you keep on having sex. Time goes on and Nessa shows no signs of stopping."
                    pause
                    "You lose count of the number of times you came."
                    pause
                    "Your body is unable to keep up with Nessa. You pass out."
                    scene black with fade
                    "You wake up and crawl out of the prison as usual."
                    jump elfvillage
                "Hell no!":
                    show suprised
                    mc "Hell no!"
                    n "Pfft, hehehehe. Fine."
                    jump elfvillage

        "Is the task done?" if nessaquest == 1:
            scene jail
            show normaln
            show smilemc
            show talksadhappymc
            mc "Is the task done?"
            if nessaquesttimer >= 4:
                show hornn
                n "YES!"
                mc "YES!"
                show sedtalkn
                $ sexnessa += 1
                $ persistent.sexNessa = True
                n "Here's your 200 silver. Now take off your clothes!"
                scene black
                "The both of you get undressed."
                n "I can't believe I finally get to do it!"
                pause
                n "I'm going to put it in now."
                scene nessasexstart with fade
                pause
                n "Ahhh... This is the b-b-b-b-BEST!"
                pause
                show nessasex movie
                mc "{i}These elves are so tight!"
                pause
                n "AAAAHHHHH... THIS IS... AMAZING!"
                pause
                n "I-I can't stop!"
                pause
                mc "I'm going to cum!"
                pause
                n "Do it! Do it inside me!"
                pause
                mc "Uuuurghhh!"
                scene nessacum with flash
                pause 0.05
                scene nessacum with flash
                mc "Ohhh... man... that was go-"
                show nessasex2 movie
                pause
                mc "Ahn- I-I j-just came!"
                pause
                n "I can't... stop!"
                pause
                mc "{i}My dick!"
                pause
                n "Need more!"
                pause
                mc "I think... I'm going to cum again!"
                pause
                n "Cum as much as you want! I don't care!"
                pause
                mc "Nngh!"
                scene nessacum with flash
                pause 0.05
                scene nessacum with flash
                mc "{i}huff... huff...{/i} you... made... me... cum... twice."
                pause
                scene nessasexstart with dissolve
                n "{i}huff... huff...{/i} Hehehe."
                n "Your dick is still hard."
                play music horror
                pause
                mc "No...{p}Oh no...{p}Oh no-no-No-No-NO-NO-{b}NOOOOO!!!!!{/b}"
                scene black
                "Nessa continues to violate you for another hour. You pass out in the process... When you wake up, Nessa's gone."
                "With an inch of your life left, you crawl out of the prison..."
                $ nessaquest += 1
                jump elfvillage
            show hornn
            n "Almost there... I can't wait to see that dick of yours again."
            jump nessatalk

        "Ask about Zenelith's house" if bothpath == 2:
            scene jail
            show normaln
            show smilemc
            show talksadhappymc
            mc "Uhm... so Nessa, you're in charge of the village's protection, right?"
            show talkwan
            n "Uh, yeah? I think I told you earlier."
            mc "Do robberies happen here in the village?"
            n "Robberies?!"
            mc "Yeah, like do people steal stuff from other people by breaking into their houses?"
            n "No! Why would anyone do that? We always share what we have!"
            mc "I see but I found that the doors can be locked right. Why is that?"
            n "W-Well, people need privacy, don't they?"
            mc "They're locked by keys, right?"
            n "Yeah, they are."
            mc "So since you're in charge of the village security, don't you know have some kind of... Master Key?"
            n "I do- ...Now what's this? What do you want?"
            mc "I just want to get into a particular house? And it's not for a robbery or anything."
            show talkangryn
            n "What?!"
            mc "I swear it's nothing bad, it's for something very important."
            n "Are you crazy? How could I compromise the village security like that?"
            mc "I'm telling you, it's for something very important! It concerns Eve and Aerin."
            n "Huh?"
            mc "If you give me that key, I can stop the duel from happening. No one will get banished."
            n "Lies!"
            mc "It's true!"
            n "......"
            n "Who's house is it?"
            mc "The... elf priestess' house."
            n "You've got to be kidding me."
            mc "You have to believe me, it's for something very important!"
            n "Like what? Getting into her dressing room while she's changing? Or how about stealing some panties?"
            mc "What- No! It's not like that."
            mc "{i}I can't get her involved in this until I have proof. Zenelith looks like a dangerous person, she might do anything to cover her tracks."
            mc "{i}I know Nessa, I think I have something I can use against her."
            mc "What if I let you touch my dick?"
            show sedtalkn
            n "WH-WHAAAAAAA... I..."
            mc "If you give me the key, I'll let you stroke my dick."
            n "S-S-S-S-S-Stroke your d-dick?!"
            mc "Yes! And I promise you, I won't do anything that would harm the village."
            n "...H-How dare you! How could you, how can you have the GALL... to bring the captain of the guard to her knees?!"
            mc "I just want the keys."
            show talkangryn with vpunch
            hide sedtalkn
            n "Ngggh... NO!!! IT'S MY SOLEMN DUTY TO PROTECT THIS VILLAGE, EVEN IF IT KILLS ME!!! I WILL NOT LET SOME DIRTY HUMAN MAKE ME DO HIS BIDDING!!!"
            show talkwamc
            mc "I'll let you suck it."
            show hornn
            n "{b}DEAL!!!!!!!!!{/b}"
            mc "{i}Hehehehe! I knew this would work!"
            show sedtalkn
            n "Ok, now take your pants off!"
            mc "Whoa, whoa, wait a minute. The keys first."
            n "Ok, fine. Take it but please don't do anything stupid."
            mc "I promise you, nothing's going to happen."
            scene jail with fade
            "Both of you get undressed."
            n "I can't believe it, I'm finally going to taste a d-dick!"
            mc "Come on, get to it, will ya? My dick feels like it's about to burst."
            n "Shut up, I'm trying to savor this moment!"
            mc "Ugh."
            n "So big, so juicy... I-I-I can't resist!"
            show nessabj movie
            mc "W-Wow, at least give a heads-up."
            pause
            window hide
            n "Can't"
            pause
            n "Talk"
            pause
            n "Must"
            pause
            n "Suck"
            pause
            mc "How... are you... so good at this?"
            pause
            mc "Slow down!"
            mc "I'm gonna cum!"
            pause
            scene nessabjcum with flash
            pause 0.5
            scene nessabjcum with flash
            scene jail with fade
            $ persistent.nessaBlowjob = True
            show sedtalkn
            show smilemc
            n "That was... amazing."
            show talksadhappymc
            mc "It was. You really looked like you knew what you were doing."
            n "Hehehe. I was born for dicks."
            mc "No kidding."
            mc "{i}That cute face really doesn't fit her."
            mc "I have to go now."
            n "[mc]?"
            show normaln
            mc "Hmm?"
            show talknn
            n "Can you at least tell me what you're up to?"
            mc "I can't, not yet."
            n "...Whatever you do, don't get yourself into trouble. And I want the key as soon as you're done with your \"investigation\"."
            mc "I promise."
            n "I can't believe I'm doing this..."
            mc "It's for Eve and Aerin. Trust me!"
            n "Whatever. Now get out of here already before I suck you off again."
            mc "{i}Gods no! My dick can't take anymore!"
            scene elfvillage with fade
            mc "Ok, I got the key!"
            $ bothpath += 1
            jump elfvillage

        "About Aerin" if sawaerin >= 1:
            show normaln
            show smilemc
            show talkhn
            show talkmc
            mc "How much do you know about Aerin?"
            n "We were very close when we were little. Me, Eve and Aerin did everything together."
            mc "So the three of you were pretty close friends?"
            n "Yeah but after her mother got banished, we saw less and less of her. She didn't show it but we knew she blamed the village for abandoning her mother."
            n "Things got worse when her brother disappeared soon after. The whole village tried to find him but we couldn't. They searched for weeks and months but all attempts went in vain."
            n "She was a totally different person after that day. She wouldn't even talk to anyone, she'd just lock herself home, isolated from everything and everyone."
            mc "She must have gone through some really hard times. Did you guys even try to talk to her?"
            show talkangryn
            n "We did but she didn't want to talk to us, or anyone. So we gave up as well."
            mc "But isn't she your friend?"
            n "What do you suggest I do, then? break down her door, tie her up and force her to talk? If she wants to be left alone, it's better to respect her wishes."
            mc "...So, what happens if she becomes the Elder?"
            n "We'll have to follow her whether we like it or not. But I know she'd make a great leader, even though she hates the village."
            mc "How so?"
            n "Because she's been reading and training hard. Since she was a little kid, she always wanted to be the Elder. I think her motivation grew even more after her mother left."
            mc "Who do you think will win then?"
            n "The duel? Well, it's a close call but I'd put my silver on Eve. She's got more experience in fighting real enemies, you know? Aerin has trained a lot but, she hasn't put it to much use."
            mc "That makes sense, I'd go for Eve too!"
            jump nessatalk

        "About Eve":
            show normaln
            show smilemc
            show talkhn
            show talkhappymc
            mc "Tell me about Eve."
            n "Well, what do you want to know?"
            mc "What was she like when she was little?"
            n "She was really kind and mature for her age. She treated us almost like we were her kids or something, even though we were only like 50 years apart."
            mc "{i}50 years apart does make you a kid compared to her but these are elves we're talking about."
            n "She really liked going outside and seeing things, she was always very curious about the outside world."
            mc "I guess that's why she left."
            n "Yeah. After her mother became the Elder, she begged her for permission to go out to the world. Surprisingly enough, the Elder approved."
            mc "Really?"
            n "Yeah. Eve's mother was very kind, just like Eve."
            n "So she came back after a few years and brought us all sorts of cool stuff from the outside world; relics we'd never seen before, even weapons far better than our own."
            n "She talked about her Guild a lot too and the different monsters she fought and defeated in battle. She then stayed a few years in the village and left again, she's been coming and going ever since."
            mc "What about you? Don't you want to go outside?"
            show talkblushn
            n "I do but I'm not as lucky as Eve. I'm a Taran. Protection of the village is my first priority. So I have to stay here."
            n "But it's not as bad here as Eve says it is..."
            show sedtalkn
            n "And I think it got a lot better."
            mc "Huh?"
            jump nessatalk

        "About the Priestess Zenelith" if bothpath <= 4:
            $ nessaInfo = True
            show talkwanmc
            mc "What is the Elder Priestess like?"
            n "Just the way you think she'd be like."
            menu:
                "A bitch?":
                    mc "A bitch?"
                    n "Hahahaha, sort of."
                "Strict":
                    mc "Strict?"
                    n "You could say that."
            n "She doesn't really have any friends in the village... I don't think she ever had any besides her brothers."
            mc "She had brothers?"
            n "Two but they both died in the war against the Demon King centuries ago."
            mc "Oh... How old is she?"
            show suprised
            n "456."
            mc "Wow..."
            hide suprised
            n "Hehe, she is pretty old."
            show talkwanmc
            mc "So what exactly does she do?"
            n "She takes care of all the ceremonies and oversees all the events that happen in the village, including the duel. She's also in charge of keeping records of the village history. Pretty much the most important stuff."
            mc "I see."
            jump nessatalk
