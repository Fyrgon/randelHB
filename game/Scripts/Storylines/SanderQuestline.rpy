label sanderHigh:
                hide screen hud
                mc "{i}Oh, it's Sander."
                mc "{i}Wonder what he's doing?"
                show normals
                show talkhappymc with easeinright
                $ sanderhigh += 1
                mc "Hey, Sander."
                show talkwas
                sa "Oh hey there little man."
                mc "What you doing?"
                sa "I just came here looking for some herbs."
                show talkwamc
                hide talkhappymc
                mc "Ah, for what?"
                sa "Just some... Potions."
                menu:
                    "Don't have time":
                        show talksadhappymc
                        mc "cool-cool. I'll leave you to it then."
                        s "Alright, see you around kid."
                        jump forest
                    "Offer to help":
                        mc "Oh, ok. Mind if I help?"
                        show talkns
                        sa "Really? Man, that would be great."
                        mc "Alright then, what kind of herb are we looking for."
                        sa "It's like this."
                        "Sander shows you a stranger herb you've never seen before. It's peculiar enough to spot easily."
                        mc "Got it."
                        scene forrest with fade
                        "The two of you start looking for the herb. You search for hours and barely manage to find any."
                        show talkwamc
                        show normals
                        mc "How many did we get?"
                        sa "Uhm... Nine."
                        show thinkmc
                        mc "Seriously? After searching so much..."
                        show talkwas
                        sa "It's ok man, this is a good haul."
                        mc "Are they that rare?"
                        sa "Yup."
                        mc "So what kind of potion are you making with these anyway?"
                        show seriouss
                        sa "......"
                        if sanderrel >= 5:
                            play sound chime
                            $ renpy.notify("{color=#fff}Sander Relationship check:{/color} {color=#00C413}Success!")
                            sa "Listen [mc]... This isn't really for a potion."
                            show talkwanmc
                            mc "Then what is it?"
                            sa "Promise me you won't tell anyone. If you do, it'll get me in serious trouble."
                            mc "I promise."
                            sa "Alright."
                            sa "See this?"
                            "Sander holds up a leaf."
                            sa "This is called a Marow leaf."
                            mc "A Marow leaf... Never herd of it."
                            sa "That's because it's illegal."
                            mc "Illegal? Wh-why is it illegal?"
                            sa "It's a psychedelic."
                            mc "What's a Sikedelees?"
                            sa "Psychedelic. It... It makes you have a great time."
                            mc "A great time? What do you mean? It's a leaf."
                            sa "I don't fucking know man, it just does."
                            menu:
                                "Try it.":
                                    mc "Well... How good are we talking about?"
                                    sa "I-I can't put it into words man, it just... like, takes you out of it."
                                    mc "Out of what?"
                                    sa "I told you, I can't put it into words."
                                    mc "Hmm... So do you, like, eat it?"
                                    sa "No, you smoke it."
                                    mc "......"
                                    show talkwamc
                                    mc "Can I try?"
                                    sa "What?"
                                    mc "I'd like to try, sounds interesting."
                                    show talkangrys
                                    sa "Nah. Sorry little man, I can't."
                                    show angry
                                    mc "What, why not?"
                                    sa "Because... It's like... Bad for you or something..."
                                    mc "Why is it bad?"
                                    sa "I don't know, people say it is."
                                    mc "Why is it bad?"
                                    sa "T-They say it's addicive and stuff..."
                                    mc "Is it?"
                                    sa "...No."
                                    mc "So why is it bad then!?"
                                    sa "I-I don't- it's what I heard."
                                    mc "I just want to see what you are talking about, man."
                                    sa "Nope. No."
                                    mc "Come on."
                                    sa "......"
                                    scene forest
                                    show talksads
                                    sa "God... It's my fault for telling you all this..."
                                    show talkwamc
                                    mc "Yeah, your fault."
                                    sa "{i}Sigh"
                                    sa "How old are you again?"
                                    mc "19"
                                    sa "......{p}Alright then."
                                    mc "Yes!"
                                    scene forest with fade
                                    "Sander takes the leaf and tears it to pieces, he then takes out a smoking pipe out of his satchel."
                                    "He puts the pieces into the pipe and lights it up."
                                    sa "He you go, just take in one whiff."
                                    mc "Alright..."
                                    "You take the pipe, you hold it in you hands inspecting it."
                                    mc "{i}I don't know why Sander is making such a big deal out of this... It's probably kinda like getting drunk."
                                    "You take a whiff."
                                    "Sander takes the pipe from your hands."
                                    sa "How do you feel?"
                                    mc "...Like before."
                                    mc "Maybe just... a bit dizzy."
                                    scene black with fade
                                    pause 0.1
                                    scene forest with fade
                                    show trip with dissolve
                                    mc "......"
                                    scene black with fade
                                    pause 0.1
                                    scene forest with fade
                                    show trip
                                    mc "This ain't that bad."
                                    mc "..."
                                    mc "Things look a bit... Fuzzy."
                                    "......"
                                    "Unknown" "Psst"
                                    mc "Hmm..."
                                    "Unknown" "Psst!"
                                    mc "Mhh..."
                                    mc "...Huh?"
                                    scene scarsex1 with flash
                                    mc "Wow... That tree..."
                                    mc "Looks kinda.....hot."
                                    "Tree" "Hmm... Hey there cutie..."
                                    mc "Is she talking to me?"
                                    "Hot talking tree" "Yeah you."
                                    mc "Man, she is talking to me."
                                    mc "Wait a minute, that's not a hot talking tree..."
                                    show scarsex2 with flash
                                    pause 0.1
                                    show scarsex1 with dissolve
                                    pause 0.1
                                    show scarsex2 with dissolve
                                    mc "It's... S-scarlet."
                                    s "Come on, [mc]. I know you want it."
                                    mc "W-wait... You mean I-I can."
                                    s "Yes... Yes."
                                    mc "{i}Gulp"
                                    mc "Oh god, I'm about have sex with scarlet."
                                    mc "Wait, wasn't I with someone...?"
                                    scene forest
                                    show trip
                                    mc "Hmm... Well, there no one there."
                                    mc "Except for that laughing tomato."
                                    show tomato
                                    "laughing tomato" "Hey [mc]"
                                    "laughing tomato" "Fuck that bitch!"
                                    mc "{i}I will, creepy tomato."
                                    mc "Oh boy..."
                                    mc "Here I go."
                                    scene scarsex2
                                    s "Come on kid, fuck me."
                                    scene scarsex3
                                    pause
                                    mc "Yoo! My dick's huge!"
                                    s "Hmm..."
                                    hide window
                                    show scarsex4 with dissolve
                                    s "Ahh yes... Just like that."
                                    $ persistent.acidTrip = True
                                    pause
                                    s "Harder."
                                    s "Harder!"
                                    s "HARDER!!"
                                    scene lecturetalk
                                    show trip
                                    "Boris" "Mr.[mc]!"
                                    "Boris" "What do you think you're doing?"
                                    mc "Uhm... Uhh..."
                                    mc "Wait, I'm in class."
                                    scene class
                                    show trip
                                    g "Hi, [mc]."
                                    "Boris" "Stop copulating with Miss Scarlet."
                                    mc "Scarlet? Wh-where did she go?"
                                    "Boris" "Now sit down Mr. [mc]."
                                    mc "...What was I doing earlier?"
                                    "Boris" "Ah there you are. What took you so long?"
                                    mc "Huh?"
                                    scene ledric
                                    show trip
                                    "Monster" "I'm very sorry, sir. I had to eat three children on my way here."
                                    "Boris" "Enough with the excuses now sit down."
                                    mc "What the fuck is going on."
                                    scene lecture
                                    show trip
                                    "Student" "Excuse me Mr.boris, I have grave news."
                                    "Student" "The wild boars have started an uprising, They're attacking the village!"
                                    scene lecturetalk
                                    show trip
                                    "Student" "Oh lord, everyone RUN!!!!!!!!!!!"
                                    mc "Wh-What?? The wild boars??? An uprising?"
                                    mc "Fuck, they're here to kill me and avenge their comrades!!"
                                    g "Get out of here [mc]!"
                                    show trainingcynth2 with easeinright
                                    mc "{i}Huff... Huff... Huff..."
                                    hide trainingcynth2 with easeoutleft
                                    show glob5 with  moveinbottom
                                    mc "Shit they're coming!!!!"
                                    scene black with blinds
                                    show glob5
                                    mc "Wait what's happening-"
                                    hide glob5 with moveoutbottom
                                    mc "AHHHHHHHHH"
                                    scene abyss1 with flash
                                    show trip
                                    pause
                                    scene abyss2
                                    show trip
                                    mc "What is happening?!"
                                    scene black with flash
                                    mc "...Did I die?"
                                    mc "{i}Gasp"
                                    mc "{i}Huff... Huff..."
                                    scene forest with flash
                                    show trip with dissolve
                                    mc "{i}I'm alive{i}"
                                    hide trip with dissolve
                                    sa "Hey, you're up."
                                    sa "How was the trip, little man?"
                                    mc "I..."
                                    mc "...I don't know what the fuck happened, man."
                                    sa "Hahaha!"
                                    sa "I'll tell ya what happened."
                                    sa "First you were talking to a tomato."
                                    mc "A tomato."
                                    sa "And then... Hahaha... And then you started humping that tree... Hahaha!"
                                    mc "What!?"
                                    sa "Oh-hahaha- Yeah! Damn, I wish I brought the eye orb."
                                    mc "Oh my god... what else did I do?"
                                    sa "Well, then you started running around like a maniac yelling something about a wild boar revolution or something."
                                    mc "......"
                                    mc "{i}What the hell was I doing..."
                                    mc "{i}My mind... it's all foggy..."
                                    sa "Now you get what I was saying?"
                                    mc "Yeah, that was like..."
                                    sa "Like nothing you ever experienced before."
                                    mc "Yeah."
                                    mc "Man, how often do you take this stuff?"
                                    sa "I don't know, whenever I feel like it."
                                    mc "Does it always get this crazy?"
                                    sa "Yup."
                                    mc "Lord Astylla, now I understand why you're so weird."
                                    sa "hehehe"
                                    sa "So did you like it?"
                                    mc "Y-Yeah it was... something."
                                    sa "Hehehe"
                                    sa "Lets head on back to Randel then. It's getting dark."
                                    mc "It's already dark?"
                                    mc "How long was I out?"
                                    sa "Five, six hours."
                                    mc "What!?"
                                    mc "What were you doing all that time?"
                                    sa "I got high too."
                                    mc "{i}He seems completely fine."
                                    sa "Everything's fine with you, right?"
                                    mc "Yeah, yeah."
                                    sa "Good, lets go."
                                    scene ambush1 with fade
                                    "The two of you walk back to Randel. Throughtout your journey Sander talks about all of his weird experiences, you can't help but laugh at his ridiculous stories."
                                    mc "Hahaha... No way."
                                    sa "Yup, that's exactly what I saw."
                                    mc "That's crazy."
                                    sa "It was, I kid you not, I laid there crying the whole day."
                                    mc "Hahahaha"
                                    sa "......"
                                    sa "Gosh, you remind me of my brother, so much."
                                    mc "Huh."
                                    mc "Wait, you have a brother?"
                                    sa "Yeah..."
                                    mc "How come I've never seen him? is he not living in Randel?"
                                    sa "......"
                                    sa "He's... Not living anywhere. Not anymore at least..."
                                    mc "Oh..."
                                    mc "I'm sorry."
                                    sa "Nah, it's ok."
                                    mc "How did he...?"
                                    sa "I killed him."
                                    mc "What?"
                                    sa "He didn't leave me a choice."
                                    mc "...Would you mind me asking you what happened?"
                                    sa "{i}Sigh{/i}... The place we grew up in wasn't really the best place to grow up."
                                    sa "My dad, he... Wasn't a very good guy. He used to beat us all the time."
                                    sa "My mother died when my brother was born. I guess... My dad blamed him for it."
                                    sa "When he grew older, my brother, he hanged around with some bad people. They... He changed."
                                    sa "And one day, he decided he wasn't going to get abused anymore."
                                    sa "He tried to kill our farther."
                                    sa "I... I couldn't just stand there and watch, I-I had to stop it."
                                    sa "But he wouldn't stop, no matter ho much I held him back."
                                    sa "...I ended up killing my only brother."
                                    mc "{i}My god, Sander, I... He never seemed the one to have such a dark past."
                                    mc "{i}His cheery attitude... It's probably how he copes."
                                    mc "...Sander ...I'm sorry."
                                    sa "......"
                                    sa "Pfttttt!"
                                    sa "HAHAHAHAHAHAH!"
                                    sa "You bought it, you really bought it!"
                                    mc "You- YOU MOTHERFUCKER!"
                                    sa "HAHAHAHA!!!"
                                    sa "You thought I had the most cliché tragic backstory? hahahaha!"
                                    mc "Yeah! It wasn't funny, man!"
                                    sa "HAHAHAHA! Oh man, you're killing me here."
                                    mc "...So that was all a lie."
                                    sa "Yeah, haha... That's the story I use when I want to pick up some chicks."
                                    sa "Ladies love the sad broken type."
                                    mc "{i}Sigh"
                                    sa "Hehehe."
                                    mc "So you never had a brother?"
                                    sa "Oh no, I do have a brother. Pim works at the bank in the Capital."
                                    sa "The guy's always busy and has barely any time to see his loving brother."
                                    mc "And your parents?"
                                    sa "They live in the capital as well."
                                    "Sander shows you a photo."
                                    sa "Papa and Mama were the best parents a child could wish for."
                                    "{i}Hmm....they look really wealthy."
                                    mc "What does your father do."
                                    sa "Papa owns a bank in the capital."
                                    mc "......"
                                    mc "You're serious this time, right?"
                                    sa "Yeah, yeah."
                                    mc "Your dad owns a bank!"
                                    sa "Yeah, that's what I said."
                                    mc "Them why are you, uh, so..."
                                    mc "Coarse?"
                                    sa "Huh... I guess that's the impression I give."
                                    "You take another look at the photo"
                                    "{i}Sander seems to have been a pampered kid. No wonder Eve has to take care of him now."
                                    sa "Man, didn't think you would've fallen for that."
                                    mc "Yeah, yeah. It's my fault for thinking that you had some sense of depth."
                                    sa "Hahah! Nope, I'm just the comic relief guy."
                                    sa "And that's fine with me. You don't need to be deep and tragic to be interesting. At least that's what I think."
                                    mc "Yeah?"
                                    sa "Yeah, there's no shame in being a one-note character."
                                    sa "As long as you're true to yourself and beleive it in you heart, I think that makes you an interesting person."
                                    mc "Huh..."
                                    mc "You saying that actually gave you a bit of depth."
                                    sa "Really?"
                                    sa "Guess I wasn't as shallow as thought."
                                    sa "Anyway, try spreading my tragic backstory as much as possible, ok."
                                    mc "Your fake tragic backstory?"
                                    sa "Yeah."
                                    mc "But I thought you said you were fine being the comic-relief guy."
                                    sa "But I need to think about the ladies."
                                    mc "...Fine."
                                    sa "Hehehe great."
                                    sa "Looks like we're almost there."
                                    "The two of you are back at the guild."
                                    scene agblr with fade
                                    show talkns
                                    show smilemc
                                    sa "Then, I'm off little man."
                                    sa "Had a great time today, hope we'll do it again."
                                    mc "Oh no. We're not doing that again."
                                    sa "Good just what I wanted to hear. See ya."
                                    mc "Bye! Oh, and... Thanks."
                                    mc "As weird as it was, I had a great time."
                                    sa "No problem kiddo, but remeber, drugs are bad."
                                    mc "Ok papa."
                                    j "Drugs?"
                                    sa "Alright, got to go, bye!"
                                    mc "Heheh."
                                    $ sanderhigh += 1
                                    jump guild
                        sa "It's some... healing elixr."
                        mc "Oh."
                        if trissq1 > 1:
                            mc "Don't you use blood butterflies for healing elixrs?"
                            sa "Uhm... Yeah, you can do that, but this is a stronger elxir. "
                            mc "Hmm... Ok."
                        sa "Thanks for the help, kid."
                        sa "I better get back to the guild."
                        mc "alright, see you later then."
                        sa "Yup, bye."
                        mc "{i}That guy's definetly making something shady."
                        $ sanderhigh += 1
                        jump home
