default ledricquest = 0
default sequest1 = 0



label cavetresureq:
    show normalmc
    show talkhappymc
    show normale
    mc "I'm ready, let's go!"
    hide normale
    hide talkhappymc
    show talkhe
    e "Alright then, you sure everything's good to go?"
    menu:
        "Yeah!":
            mc "Yeah!"
        "On second thought...":
            mc "On second thought... I gotta check out something."
            e "No problem! Take your time, little one."
            jump guild
    e "Then I'll get Sander. Let's go!"
    scene adventurersguild_day with fade
    "Evelyn goes off and gets Sander."
    sa "You ready, kid?"
    mc "Yep."
    sa "And you've got all your stuff?"
    mc "Yeah, everything's right here."
    sa "Sounds good! Let's get going then."
    "Eve and Sander pick up their bags and the three of you leave the guild to go into the forest."
    play music forest
    scene ambush1 with fade
    sa "I believe this is the way."
    e "You sure?"
    sa "Yeah, according to the map if we follow this path we'll get to the cave just a little bit before noon."
    e "Then let's move."
    "The three of you walk in silence for a while."
    mc "Uhm... how long have you guys known July?"
    e "Ever since the day we joined the Academy."
    sa "Why, [mc]? Got a crush? Haha!"
    mc "No! It's nothing like that... it's just..."
    mc "Have you guys noticed anything strange about her?"
    sa "Strange? ...Urm, nothing particular."
    sa "The only thing that's strange about her is her eyes, if you ask me."
    sa "How can she see anything with eyes that small?"
    e "That's rude, Sander! Why are you asking, [mc]? Did you notice something strange about her?"
    if sawjulyvampire == 1:
        "{i}So they don't know, huh?"
        "{i}Better keep quiet. I promised July I wouldn't tell anyone."
        mc "Nah... It's nothing..."
    else:
        mc "Well... it's just one night I saw her-"
    "You hear a twig break nearby."
    sa "LOOK OUT!"
    show animationspearthrow
    pause
    hide animationspearthrow
    "Sander pushes you away. A spear zooms by your head and misses by an inch."
    sa "Are you alright?!"
    mc "Yeah, I'm ok!"
    play music battlemusic1
    e "Goblins!"
    $ gameover = "goblinfight"
    label goblinfight:
    scene ambush4 with dissolve
    e "They've surrounded us!"
    sa "We can't go through... We have no choice but to fight."
    sa "You up for this, kid?"
    menu:
        "Yeah!":
            mc "Heck yeah!"
        "I'll kill every single one of these little green fuckers!":
            mc "I'll kill every single one of these little green fuckers!"
            sa "Hell yeah! That's the spirit!"
    e "Here they come, get ready!"
    scene ambush5 with hpunch
    sa "[mc], you take that one! Eve and I'll take care of the ones on the right."
    mc "Got it."

label fightgoblin:
    mc "Time to take you down!"
    show animationgoblin
    menu:
        "Strike first":
            "You charge at the goblin."
            "You swing your sword down on the goblin with all your force."
            "The goblin ducks and rolls between your legs. In a flash, it's behind you."
            mc "Fuck!"
            "You close your eyes, preparing for the worst... Then you here a whoosh and when you turn around the goblins is dead. An arrow sticks out of its head as it slumps to the ground."
            e "Come on, [mc]! watch out there's another one!"
            mc "{i}Damn it, I almost died!"
            $ savedbyeve1 += 1
            scene goblin6 with vpunch
            "Another goblin jumps out of the underbrush."
            mc "You're next. Come at me! "
            scene goblin7 with dissolve
        "Wait for it to attack first":
            "You remember Taliya's training. You wait for the goblin to attack."
            "The goblin charges at you."
            "It thrusts it's spear at your gut. You side step away and close the distance between you two and strike."
            "You manage to land a glancing blow. The goblin quickly jumps back, bloodied."
            menu:
                "Charge!":
                    " It's injured! Time to charge!"
                    "You charge at the goblin and slash it with your sword."
                    "The goblin tries to dodge but it's too injured to move."
                    play sound slash1
                    scene goblin4 with vpunch
                    mc "Yaargh!!!"
                    "The goblin drops to the ground."
            scene goblin6 with vpunch
            "Another goblin jumps out of the underbrush."
            mc "You're next! come at me!"
            scene goblin7 with dissolve
    "The goblin throws a bottle at you."
    menu:
        "Catch it":
            "You reach out to catch it but it slams into your hands and shatters."
            scene goblin8 with vpunch
            "The bottle was filled with... Goblin piss?! It splattered all over your hands."
            "In mere moments you begin to feel dizzy."
            mc "Urgh..."
            "You fall to the ground."
            scene black with fade
            "You hear Sander yell."
            sa "KID!"
            "All the voices and sounds of fighting start to fade away."
            sa "KIIIIIIIIDDDDDDD!!!!!"
            "Fun fact; Goblin piss is extremely toxic."
            jump GameOver
        "Slash it":
            "You swing your sword at the small bottle."
            show goblin9 with vpunch
            "You hit it but its contents spray all over you."
            mc "Ugh! What is this?!"
            "To your horror you realize what it is. It's goblin piss!"
            "In mere moments you begin to feel dizzy."
            mc "Urgh..."
            "You fall to the ground."
            scene black with fade
            "You hear Sander yell."
            sa "KID!"
            "All the voices and sounds of fighting start to fade away."
            sa "KIIIIIIIIDDDDDDD!!!!!"
            "Fun fact; Goblin piss is extremely toxic."
            jump GameOver
        "Dodge it":
            "You duck swiftly."
            scene goblin8 with dissolve
            pause
            scene goblin8 with vpunch
            "The bottle misses you as it smashes against the ground behind you."
            "You look back. Looks like you were right to avoid it. The horrid stench coming from behind you tells you that the bottle was filled with goblin piss."
            "You quickly charge and cut the goblin down."
            play sound slash1
            scene goblin10 with hpunch
    play music forest
    mc "Whew... that was intense..."
    mc "Hey guys! Need a..."
    scene goblinkill1
    mc "-hand?"
    scene goblinkill2 with vpunch
    mc "{i}Holy shit... They took out the entire group. These guys are good."
    pause
    sa "Nice work, [mc]!"
    sa "We just wrapped up here as well."
    e "There were a lot more than we expected."
    sa "Yeah."
    scene ambush1 with fade
    show sadtalke
    show normalmc
    e "Are you ok, [mc]?"
    hide sadtalke
    show smilee
    show talkmc
    mc "I'm fine."
    if savedbyeve1 ==1:
        show talksadhappymc
        mc "Uhm... thank you for saving me back there."
        show sadhtalke
        e "Don't worry about it. It's your first time after all."
    else:
        show sadhtalke
        e "You did realy well little one. I clearly underestimated you."
        show talksadhappymc
        mc "Thanks."
    sa "Well guys, we better get a move on. It's going to get dark soon."
    scene ambush1 with fade
    "You guys walk for a while before finally reaching the cave."
    sa "I think this is it."
    e "Let's go in, shall we?"
    stop music
    "You go in. Evelyn uses a spell to light a torch."
    scene black with fade
    mc "Ewwww... What's that smell?"
    sa "Trust me kid, you don't wanna know."
    "You proceed further into the cave. As you walk along, you see piles of bones, small beds made out of animal skins and spears leaning against the walls of the cave."
    mc "It looks like the goblins have been living here."
    e "That explains the smell..."
    "A few moments later."
    e "How deep is this cave? Are you sure we aren't lost?"
    sa "No, no, I'm sure."
    sa "We're on the right track. I can feel it!"
    "After traveling further into the cave, you begin to see a light."
    mc "Is that?"
    sa "The treasure!"
    scene chest1 with fade
    sa "There it is!"
    e "We finally found it."
    e "Ok Sander, now open it."
    sa "Why me? You do it."
    sa "It might be booby trapped or something..."
    e "Ugh... come on Sander, they're goblins. They lack the ingenuity and patience to make booby traps."
    sa "Ok, fine. But it's your fault if I die!"
    "Sander opens the chest."
    scene chest2 with flash
    mc "Wow..."
    sa "Jackpot."
    e "See? You're still alive."
    sa "Whatever... let's take the chest and go. I can't stand this smell anymore."
    "You help Sander carry the chest out of the cave. By the time you get out, it's already dark."
    scene ambushn with fade
    play music night
    sa "It's too dark to travel. I guess we'll have to make camp here."
    e "Is it safe here? We're pretty deep in goblin territory."
    sa "Yeah, it should be. We took care of the goblins, I don't think there's any more left in this area."
    sa "We'll take turns keeping watch just in case then."
    e "Uhm... That'll work."
    "You guys set up camp. Eve goes out to collect firewood."
    show normalsr
    show talksr
    show smilemc
    sa "Ok, everything's ready."
    show normale with easeinleft
    show talkhe
    e "I'm back... it's not much but this is all I could find nearby."
    hide talkhe
    hide talksr
    sa "That'll do."
    show watalkeve
    e "Oh and I also found a lake nearby, I think I'll take a dip. I need to wash this filthy goblin blood off me."
    e "I'll be right back."
    hide normale
    hide watalke with easeoutleft
    scene ambushn
    show smilemc
    show smirks
    pause
    sa "So kid, do you wa-"
    show angrytalke with easeinleft
    e "Sander, if I catch you peeking again, I swear to god I'll rip you in half!"
    show suprised
    hide smirks
    show talksr
    sa "Ok, Eve! Fine, fine, I promise! No peeking."
    hide suprised
    hide angrytalke with easeoutleft
    pause
    hide talksr
    show smirks
    sa "...So kid as I was saying..."
    sa "Wanna go peek on Eve?"
    show talkwanmc
    mc "What?! Are you crazy?! Didn't you hear what she just said?"
    sa "Ahh, don't mind her! Besides, don't worry, you'll be with me."
    sa "I'm the Master Voyeur remember? I'll make sure we won't get caught."
    sa "So, what do you say?"
    mc "......"
    sa "Come on, it's Eve!"
    mc "......"
    sa "Think of that white plump yet toned body..."
    mc "......"
    sa "That juicy-"
    mc "Ok."
    sa "What??? I didn't quite hear you there."
    mc "OK, FINE!"
    sa "Hehe... I knew you would come around. Let's go!"
    scene black with fade
    "You follow Sander."
    "Sander surprisingly manages to track Eve easily."
    mc "{i}I guess he has a lot of experience in stalking people."
    sa "I think this is the spot. Now slowly follow my lead."
    "You slowly creep your way towards the lake and hide behind a boulder."
    "You hear water splashing nearby."
    sa "That should be her. Ok, now slowly peek."
    mc "What about you?"
    sa "You go first. I-I'll watch your back..."
    mc "If you say so."
    mc "We are gonna so get murdered."
    sa "That's just it... The suspense, that's what we want. That's what enriches the experience! Which motivates people in the thrill of endangerment!"
    mc "You're fucking weird, man."
    sa "Ok, ok! ...Let's get to it then."
    "You slowly peek over the boulder."
    scene evebathe1 with fade
    pause
    mc "{i}Damn... Eve's packing such a great body..."
    scene evebathe1
    pause
    mc "{i}I mean look at that ass..."
    scene evebathe1
    pause
    mc "{i}I could stare at her all day."
    sa "Hey! Come on, it's my turn."
    mc "Just wait, I-"
    scene evebathe2 with vpunch
    $ persistent.eveBath = True
    mc "Fuck."
    show black with moveinbottom
    "You quickly duck."
    sa "What?!"
    mc "I think she saw me."
    "You see Sander's face fill with horror."
    sa "OH NO!!!"
    "You look behind and see Eve..."
    show everage1
    e "YOU LITTLE PRICKS! I'M GONNA KILL YOU!!!"
    sa "Sorry, little man. It's been an honor serving with you."
    e "Come here!!!"
    play sound punch
    scene everage2 with vpunch
    mc "GAHHH!"
    play sound punch
    scene everage3 with hpunch
    sa "AHHHH!!"
    scene ambushn
    show normalsr
    show normale
    show normalmc
    show angrytalke
    e "I can't believe you, Sander! Every time!"
    e "A-And why did you bring [mc]?!"
    show talksr
    sa "Come on Eve, we're just having some light-hearted fun!"
    e "Fun?! Spying on people when they bathe?!"
    sa "Ok, ok... we're sorry."
    show talksadhappymc
    mc "Yeah, I'm really sorry Evelyn."
    e "I can't believe you brought [mc] into this..."
    e "......"
    e "Ughh... fine! But only this one time."
    mc "{i}That settled down fast."
    sa "Yeah, yeah, ok. You bashed our heads anyway."
    e "You guys are lucky you are just getting that!"
    sa "Since that's over, why don't we make a fire?"
    e "{i}Sigh...{/i} fine."
    scene black with fade
    "Sander piles up the fire wood as Eve casts a spell. The wood quickly starts to burn."
    sa "Come, sit here."
    play sound campfire
    play music happy
    scene camp with fade
    sa "Haah, what a day, huh?"
    e "Yeah... how was it, [mc]? Your first adventure with us?"
    menu:
        "It was great.":
            mc "It was great."
        "It was awesome!":
            mc "It was awesome!"
        "It was the best!!":
            mc "It was the best!!"
            e "Wow, I'm glad you enjoyed it."
    sa "Why wouldn't it be, he got to see you naked!"
    e "Not funny, Sander."
    sa "Hehehe..."
    e "Sooo, why don't we get to know each other more? What do you say, little one?"
    e "I think you certainly would like to know about us as well."
    mc "Oh, yeah."
label campq:
    menu:
        "How old are you guys?":
            mc "How old are you guys?"
            sa "Oh... well I am 46... and Eve here is... wait, how old are you exactly? I lost count at like 310."
            e "...I'm 324."
            mc "Wow."
            sa "That's Elves for ya. They barely age."
            sa "I wish I was an Elf. Man, think of all the things I could do. All the girls I could-"
            e "Yeah, yeah, we get it."
            e "But it's not that easy...."
            e "...I mean seeing everyone around you age and die... it's hard."
            e "I guess that's why Elves keep their distance from other races."
            mc "Have you lost a lot of friends?"
            e "Yeah... I try to remember them all but it's too much. Their faces just fade away after some time."
            e "As time goes on when you age, everyone you know dies... and then, your forget who your best friends are."
            e "That's a fate of a living-being with a long lifespan, like me..."
            mc "I'm sorry, Evelyn."
            sa "Yeah, Eve, that sucks."
            e "No, it's ok, you start to get used to it after a while."
            sa "I guess we don't have to worry about having maids when we get old, huh [mc]? Eve can take care of us."
            e "Taking care of you two old farts? No thanks!"
            mc "Hehehehehe.."
            jump campq
        "How did you guys meet?":
            mc "How did the two of you meet?"
            e "Hmm... we met... in the forest, right?"
            sa "Yeah, it was my early days of being an adventurer. I was, like, 21 or something."
            sa "I was on a quest in the forest. I think it was to hunt and bring back a white deer."
            sa "So I was tracking this thing for days, until I finally found it."
            sa "Then just as I was ready to take the shot, an arrow comes out of nowhere and hits the deer."
            sa "When I looked back, it was Eve."
            sa "So she says she wants the deer and I refuse because I tracked that damn thing for days."
            mc "Were you an adventurer too?"
            e "No, I was just hunting. I wasn't even living in Randel at that time. I lived in a small elf town in the forest."
            mc "So then, what happened?"
            sa "So we finally decide to both bring in the deer and split the reward."
            sa "Then after a few days, Eve comes out of nowhere and joins the Guild."
            mc "Really? Why?"
            e "I liked the feel of the Guild after I got to visit it. Plus, I was bored living in my home town for so long. I needed a little bit of... adventure."
            sa "So then, we decided to party up and started going on quests."
            mc "Wow, I didn't know there was an elf town in the forest."
            e "It's well hidden. Many people don't know about it."
            sa "Yeah, Eve won't even tell me where it is."
            e "It's for the towns own safety. Elves really like to keep to themselves. They don't want to be interfered with by the outside world."
            mc "Hmm..."
            jump campq
        "What rank are you?":
            mc "What rank are you in the Guild?"
            sa "We both are Gold level adventurers."
            mc "Gold?!"
            sa "Yep."
            mc "Wow, how long have you guys been adventurers?"
            sa "I've been an adventurer for about 27 years and Eve's been around for 24 years."
            mc "That's a long time."
            sa "Hmmm... it is, now that I think about it. But it doesn't feel like it."
            e "Yeah, it all feels like yesterday."
        "That's all.":
            mc "Well, that's all."
    e "Now that you know about us, why don't you tell us about yourself?"
    mc "Ok... ask away then."
    sa "Ok, let's go with some random questions."
    sa "What's your... favorite color?"
    mc "What?"
    sa "Just answer."
    menu:
        "Red.":
            mc "Red."
            sa "Mm-Hm."
        "Blue.":
            mc "Blue."
            sa "Mm-Hm."
        "Green.":
            mc "Green."
            e "I like green too. It reminds me of the forest and nature."
            sa "Boring!"
        "Black":
            mc "Black."
            sa "Mm-Hm."
        "White.":
            mc "White."
            sa "Mm-Hm."
        "Gold.":
            mc "Gold."
            sa "Me too! Nothing's prettier than the color of money."
            e "Pfft..."
    sa "Ok, on to the next."
    sa "Would you prefer to be a Swordsman or an Archer?"
    menu:
        "Swordsman.":
            mc "Swordsman."
            e "Ow."
            sa "Hahaha! Nothing beats a good sword and shield!"
        "Archer.":
            mc "Archer."
            e "Hehe, good answer, little one!"
            sa "Ugh... archers are lame."
            e "He's just jealous he can't shoot straight."
    sa "Hmmm... what's your favorite food?"
    menu:
        "Chicken.":
            $ mcfood = "chicken"
            mc "Chicken."
            sa "Good choice."
        "Salad.":
            $ mcfood = "salad"
            mc "Salad."
            sa "WHAT?! Your favorite thing to eat is Salad?!"
            mc "Uh, yeah? What of it?"
            sa "...Pfft... Who the hell would eat salad by choice?!"
            e "I think it's a good thing. Salad is good for you."
            sa "Look who's talking?! I've seen you goble up an entire whole turkey like an ogre!"
            e "Hey! I never said I was a vegetarian."
        "Bread with apple jam.":
            $ mcfood = "bread with apple jam"
            mc "Bread with apple jam."
            sa "Sounds tasty. Simple breakfast meal, I like it."
        "Fish.":
            $ mcfood = "fish"
            mc "Fish."
            sa "Good choice."
        "Porkchops.":
            $ mcfood = "boar porkchops"
            mc "Porkchops, especially the ones of wild boars."
            sa "Ahhh, nice! If there's one thing Eve and I agree on, it's how good wild boar tastes."
            e "Yeah, it's amazing."
            mc "{i}Huh, I didn't really think Eve was the kind of person who likes meat."
            mc "{i}Elves eating meat seems kinda weird to me. I dont know, it could only be me."
    sa "Ok now, for the most important question... Are you ready?"
    mc "Yeah."
    sa "Are you a Boob man or Ass man?"
    e "Uggh."
    sa "Come on!"
    mc "......"
    menu:
        "Boob man.":
            mc "Boob man."
            sa "NNOOOOOOOOOOOOOOOO!!!!!!!!!!!!!!"
            mc "Hehe..."
            sa "WHY?!?! Why would you betray me?!"
            e "Let the little one choose what he likes. You can't expect everyone liking your tastes."
        "Ass man.":
            mc "Ass man."
            sa "Yes! A fellow gentleman with good taste!"
            mc "Hehe, I know, right?"
            e "Ugh, men..."
        "Both man.":
            mc "Both man."
            sa "Both man?! Well, that's a commonly boring answer."
            mc "I really can't choose, man."
            sa "...Hmm. Ok, at least you were honest. But remember little man, one day you'll have to choose. The fate of Astylla may depend on it."
            e "Oh, enough of your nonsense, Sander."
            mc "Hahaha!"
    e "Ok, enough with the pointless questions, ask something more personal."
    sa "Hmm... Ok, let's see..."
    sa "Who's the most important person to you in Randel?"
    e "Yeah, that's a good one!"
    mc "Hmm..."
    mc "It's Uncle Pete."
    sa "Why?"
    mc "Well, I wouldn't be here if it wasn't for him. He brought me to Randel and raised me on his own."
    sa "Wait, so you weren't born in Randel?"
    mc "No, I was born in Hern."
    e "Hern?"
    mc "Yeah but my memory of my time in Hern is very foggy."
    e "How did you end up with your uncle?"
    mc "He's not my real uncle. When the Demon King attacked Hern, my house was burned down. The soldiers managed to rescue me but my parents didn't make it..."
    mc "Then the soldiers brought me back to Fort Hern after the battle. Uncle Pete used to be a traveling merchant and he happened to be there at the time."
    mc "He volunteered to take care of me."
    mc "Then he brought me to Randel."
    sa "Man, that's a tragic backstory. I'm sorry, kid."
    mc "It's fine."
    e "You must really love your uncle."
    mc "Yes, I do."
    e "That's sweet."
    "Some time passes."
    "Sander starts to tell some stories of his adventures."
    sa "So, I see this super ripped chick while I was in this tavern in Burdock."
    sa "You see, I was super-into ripped chicks at that time. So, I went to her."
    sa "We had a few drinks and I could tell this chick was totally into me. So we decide to take a room and have some fun..."
    sa "Then we got to our room and I take off my clothes. Then, she tells me to rip her clothes off! It was kinky as fuck."
    sa "So, I savagely strip her down and when I pulled down her panties... guess what I saw?"
    menu:
        "A dick.":
            mc "A dick."
            sa "Close but no!"
            sa "It was two dicks!"
            mc "What?!"
            e "Hahahah! Look at [mc]'s face!"
        "What?":
            mc "What?"
            sa "Two dicks. Side by side at full mast like dueling cobras!"
            mc "What?!"
            e "Hahahah! Look at [mc]'s face!"
    sa "So she then goes, \"You can fit two, right?\""
    "Eve and [mc]" "Hahahahaha!!!"
    mc "So, what did you do?"
    sa "Well... What any man would do. I let her have her way with me."
    mc "......"
    sa "......"
    e "......"
    e "...Pfft-"
    e "...Pfft-Hahahahahahahahahaha!"
    sa "Hahahahaha! I'm just kidding kid. I fucking grabbed my sword and ran buck naked back to Randel!"
    e "Hahahaha!"
    mc "Oh! Hahaha! You almost got me there."
    sa "Hehehe..."
    e "It's getting late, guys. I guess we should go to sleep."
    e "We'll leaving tomorrow morning."
    sa "Ok, I'm sleepy as hell too."
    sa "Goodnight, guys."
    e "Goodnight!"
    mc "Goodnight."
    "Sander goes into his tent."
    e "Little one, you should go to sleep. I'll keep first watch."
    mc "Thanks. Goodnight, Evelyn."
    e "Goodnight, [mc]. And please, just call me Eve."
    mc "Ok... Eve."
    "You go into your tent. It's surprisingly cozy. You fall asleep in almost as soon as your head hits the pillow."
    scene black
    show text "{color=#fff}End of day [day]." at truecenter
    with dissolve
    pause
    hide text with dissolve
    call sleepvars from _call_sleepvars_4
    stop sound
    play music forest
    "You wake up in the morning. Eve and Sander have already packed up most of the camp."
    scene ambush1
    show normals
    show animation2
    sa "You're up. Come on, let's go. Wash your face from the lake if you want to."
    show talkmc
    mc "Ok."
    "You go to the lake, splash some water on your face, then return."
    scene ambush1
    show smilee
    show normalsr
    show talkhappymc
    mc "Ready? Let's go."
    scene ambush1 with fade
    "You begin to travel back to Randel."
    mc "Are we there yet?"
    sa "Almost, we'll make it just in time for sunset."
    mc "Huh?"
    sa "You'll see."
    "A few minutes later."
    sa "We're here."
    sa "Hey little man, check this out."
    "Sander steps back and lets you see the view."
    play music bunispiano
    $ persistent.scenery = True
    scene end with fade
    pause
    mc "Wow..."
    pause
    mc "It's beautiful."
    e "Never get tired of this view, huh Sander?"
    sa "It never fails to blow my mind."
    "You enjoy the scenery for a while with your new friends."
    sa "I think it's time to go on down."
    pause
    mc "{i}So, this is the end of my first adventure... and it was epic. Eve and Sander are really nice people."
    pause
    mc "{i}I wonder where my next adventure will take me?"
    mc "{i}Wherever it is... I just can't wait!"
    e "Hey [mc], come on!"
    mc "Coming!"
    scene end with fade
    show animationend
    pause
    mc "Huh? What was that?"
    mc "..."
    mc "......"
    mc "......"
    mc "Uhm... I guess it was the wind..."
    mc "Guys! Wait for me!"
    scene black with fade
    play music dark
    show text "In the Dark Palace..."
    pause
    hide text with fade
    pause
    "Unknown" "Your Highness, we found it, the source of the energy. It's from a small town called Randel."
    "Unknown" "From a small town? Interesting... What are their defenses?"
    "Unknown" "Pathetic, your Highness. They have one barrack with less than a dozen soldiers."
    "Unknown" "Anything else?"
    "Unknown" "They also have an Adventurer's Guild."
    "Unknown" "An Adventure's Guild? That's problematic. Those adventures are usually stronger than they look."
    "Unknown" "But it will not be a problem."
    scene yakina with fade
    $ persistent.yakina = True
    pause
    "Unknown" "I'll go see this town Randel for myself."
    pause
    scene yakina1 with dissolve
    scene black with dissolve
    pause
    stop music
    scene agblr with fade
    show smilemc
    show talksr
    show smilee
    sa "Ahhhhh, we're back... Now if you excuse me, I'll be heading to my room. I need a good nap."
    e "You go ahead then, I'll give all the gold to July."
    sa "Yeah, ok, thanks."
    show angrytalke
    e "I said I'll give \'ALL\' the gold to July."
    sa "Ok, I heard you the first time, woman..."
    e "All the gold includes the ones in your pocket as well."
    sa "Whaaaa- What do you mean?"
    e "Come on, Sander..."
    sa "......"
    sa "Ok, ok, \"Mom\", you got me."
    e "Give it here."
    sa "......"
    sa "NO! Hehehehe!"
    hide talksr with easeoutright
    show thinkmc
    "Sander runs of to his room giggling like a little girl."
    e "SANDER!!!"
    e "Ahh, that man never changes."
    hide angrytalke
    hide thinkmc
    mc "Hehehe."
    e "Ok, well, care to help me with this, little one?"
    "Eve points at the treasure chest."
    show talkhappymc
    mc "Yeah, sure, Eve."
    show talkhe
    e "Great."
    scene agblr with fade
    "The two of you carry the chest as you make your way over to July. You decide to chat with Eve along the way."
    mc "Um, Eve?"
    e "Yes?"
    mc "So, does all of this go to the guild?"
    e "Oh... you didn't know? No, not all of it but most of it goes to the Guild."
    mc "Oh, I see."
    e "Don't be sad, little one. We're paid in both gold and experience points, so it's not that much of a loss."
    mc "Really?"
    e "Yeah, since you're a bronze, you might get 2 levels of EXP."
    mc "2 levels? Isn't that a bit too low? I mean, I've done way easier quest and gotten like 3 levels of EXP."
    e "You're a bronze now, little one. The higher you're rank, the harder it is to level up."
    mc "Oh... I get it. So then, if I'm only getting 2 EXP points, you guys probably don't get any."
    e "Hahaha. Yeah, you're right... but still, we had fun. That's what matters to me the most."
    mc "Yeah, I guess you're right."
    scene adgc2 with fade
    j "Wow! You guys did it!"
    e "Yeah, it wasn't that tough, to be honest."
    j "Well, that's not a surprise. So, Evelyn, how was our new recruit?"
    scene adgc1
    if savedbyeve1 ==1:
        e "He did alright"
        j "Hmm, is that so...?"
        mc "{i}It's a good thing Eve didn't tell July that I all most got killed, July would throw a fit!"
    else:
        e "He did really well, a lot better than I expected."
        j "See, I told you he was a tough one."
        e "Oh look, we're making the little one blush..."
        mc "Wha- Oh, no... it's just the heat... Hehe..."
        e "Aww, you don't need to be embarrassed, little one... you did great..."
        mc "Thanks, Eve."
    j "Here are your shares... Um, where's Sander?"
    e "Oh, he went off to his room, said he's too tired."
    j "Oh, then can you give him his share as well?"
    e "Yeah, sure."
    j "Here you go [mc], take your share."
    $ exp += 160
    call levellingUp from _call_levellingUp_7
    $ renpy.notify("{color=#fff}You gained 100 silver")
    $ money += 100
    mc "Thanks!"
    scene agblr
    show smilee
    show talkhe
    show smilemc
    e "So then, I'll be going as well, little one. I hope you had as much fun as we did."
    show talkhappymc
    hide talkhe
    mc "I did."
    show talkwae
    e "I'm glad. I hope you're ready for more adventures."
    mc "I sure am"
    e "Hahaha. See you then, little one. Get some rest."
    mc "Ok. Bye, Eve."
    $ sequest1 += 1
    jump home
    jump guild



label EveQ1pre:
    $ evemillyquest += 1
    show normalmc
    play sound doorknock
    pause
    e "Who is it?"
    show talksadhappymc
    mc "It's me, [mc]."
    e "Oh, come in, [mc]. The door isn't locked."
    scene everoomin with fade
    pause
    scene everoomblr
    show smilee
    show smilemc
    show talkhe
    e "Hello, little one. What brings you here?"
    mc "I just wanted to see how you're doing."
    e "I'm doing fine, little one."
    #if aerindead == 1:
    #    show worriedmc
    #    mc "So, what happened at the Village after... Aerin?"
    #    show sadtalke
    #    e "The elder priestess has no authority over the Village now. What she did was... was unforgivable."
    #    mc "So you're still the elder?"
    #    e "No, Nessa is."
    #    mc "Really?"
    #    e "Yes. She's perfectly capable of leading the Village."
    #    mc "That means... you broke traditions."
    #    e "Yes. It was traditions that took everything from Aerin, in the end, her own life. Traditions like those are of no use to anyone."
    #    mc "You're right."
    #    e "{i}Sigh...{/i} No point regretting the past now, little one. It's best we forget about it."
    #    mc "Yeah."
    #    e "......"
    #    e "Oh wait, I just remembered."
    #    e "I wanted to talk to you."
    #else:
    #    e "Oh wait, it's a good thing you came."
    e "Though, now that you're here, can I ask you something?"
    mc "What is it?"
    show talkwae
    e "Are you free tomorrow?"
    mc "Y-Yeah."
    e "I'm going out on a quest, care to join me?"
    mc "Uhm, yeah, sure."
    e "Great."
    mc "What's the quest?"
    e "We're going to hunt a Ledric."
    mc "What's a Ledric?"
    e "It's a very dangerous monster. Be sure to read about it before we go on the quest."
    mc "O-Ok."
    e "It'll only be the two of us, so we better be prepared."
    show talkwanmc
    mc "Sander's not coming?"
    e "No, he's had some bad history with Ledrics. He said he won't come."
    mc "Seriously?"
    e "Yes. But don't worry, little one, I know the two of us can take it down."
    show talkwamc
    mc "I'll do my best."
    e "Come meet me here when you're ready to go."
    mc "ok"
    e "Oh and do you have camping gear?"
    if icamping == 1:
        mc "Yes."
        e "Good, make sure you bring it. We'll have to spend the night."
    else:
        mc "No."
        e "What, you're a Bronze-Rank Adventurer and you still don't have camping gear?!"
        e "Did you cheat you're way up the Guild, huh?"
        mc "Hehehe. No, I just didn't need it."
        e "Hmmm... Whatever, make sure you buy one. We'll have to spend the night."
    menu:
        "One tent would be enough for the both of us?":
            mc "Uhm... Won't one tent be enough for the both of us?"
            show sadtalke
            e "......!"
            show talkwae
            e "Hahahaha, good one! You seriously need to stop spending too much time with Sander. His weird sense of humor is starting to rub off on you."
            mc "Hehehehe, yeah."
            mc "{i}Well, I tried."
        "Ok":
            mc "Ok."
    e "Excellent! I'll see you tomorrow then, little one."
    e " Oh wait, I almost forgot. Remember to bring a mask with you."
    mc "A mask? Why?"
    e "You'll know why, when you read about the Ledric."
    mc "O-Ok, see you tomorrow."
    $ time = 4
    jump home



label EveQ1transition:
    if icamping == 0:
        mc "I need to buy some camping gear first."
        jump guild
    show normalmc
    play sound doorknock
    "..."
    "......"
    mc "Hmmm?"
    play sound doorknock
    "......"
    "......"
    mc "Eve, it's me, [mc]."
    "......"
    mc "{i}No answer."
    "You turn the door handle."
    mc "{i}It's not locked."
    "You open the door and take a peek inside."
    scene everoombook with fade
    play music bath
    mc "{i}Looks like Eve's taking a bath, I guess I'll wait until she comes out."
    e "{i}Humming"
    "You go inside and look around Eve's room."
    mc "{i}Eve's room looks dull but cozy at the same time."
    mc "{i}And look at that bed, it's so big."
    "You sit on Eve's bed."
    mc "{i}It's super soft. I wish I could sleep in this."
    "While admiring Eve's bed, you see a small red book."
    if sawevesroom == 0:
        "You take the book and open it."
        "Book" "Dururthu Day 23: Today, I got a letter from the Village. It said that I should come to the Village immediately. I'm sure this has something to do with the duel."
        "I stalled this enough. I think I should end this. I can't run away from this anymore."
        mc "{i}Wow, this is Eve's diary! She's 324 but still has a diary?"
        mc "{i}It kinda makes sense though. When you live for about 500 years, you are bound to forget things. I guess that's why she has one."
        mc "{i}Wait! I think I found what I was just looking for. Yes! This could have something about her weakness!"
        "You flip through the pages."
        "While you're going through the pages, your name catches your eye."
        mc "Huh, it's about me."
        "Diary" "Today, a young boy named [mc] joined the Guild. It was so refreshing to see a small boy in the Guild after so long. I hope he does great..."
        mc "......"
        "You keep turning the pages."
        "Diary" "[mc] came today and asked me if he could join our party. I was shocked. I'm sure Sander had something to do with this. I couldn't let the little one join our party; he's still inexperienced. What if he gets hurt?"
        "Diary" "But looking at him, I saw myself when I was little. Eager for adventure, not a care for the danger that lies ahead. He said that he would do anything to prove himself. He was so adorable."
        mc "{i}I'm not adorable! I'm 19!"
        "Diary" "So, I gave him a task of hunting three Alpha Falcons. It was the easiest thing I could think of, I just wanted to see if he was willing enough."
        "Diary" "Today, the little one completed his task; he brought three Alpha falcons. I was pretty impressed that he was able to do it so quickly, the boy has talent. So, I told him that he could join. He was really happy to hear it, I could tell."
        "Diary" "I can't wait for the adventures we'll have together."
        "Diary" "Just came back from our first quest with [mc], we had a great time."
        "Diary" "We ran into a group of goblins."
        if savedbyeve1 == 1:
            "Diary" "The little one almost got killed by a goblin. I knew bringing him along was a bad idea, he's far too young. Good thing I managed to save him. If something would have happened to him while in my care, I don't know how I would be able to live with myself."
        else:
            "Diary" "The little one took out two goblins on his own. He was really stronger than I anticipated, he must have trained a lot."
        "Diary" "We found the treasure we were looking for. Then we camped for the night. I caught Sander for the hundredth time peeping while I was bathing. And what's worst is he had brought the little one with him this time."
        "Diary" "I was so embarrassed; the little one has no knowledge of these things, not like that pervert Sander. I hope I didn't taint the little one's mind. I had to teach them a lesson, so I had to give them a good beating."
        "Diary" "We talked for a while at the fire after that. I learned a lot about [mc]. He's such an innocent child. I have this strange feeling, like I want to protect him, do what's best for him. I think it's what you call a motherly feeling. It's very strange indeed."
        mc "{i}Eve... I feel bad for doing this."
        stop music
    else:
        "You hear Eve's bathroom door open."
    scene evetowelbg
    pause
    scene evetowel1
    pause
    e "[mc]!"
    mc "Oh! S-Sorry, Eve, I shouldn't have come in."
    e "No, it's ok, little one."
    e "Just let me get my clothes."
    scene evetowelbg
    "Eve grabs her clothes and goes back into the bathroom."
    scene everoomblr
    show worriedmc
    pause
    show blushtalke
    mc "I'm really sorry, Eve. I didn't mean to-"
    e "It's ok, little one. I should really learn to lock my door from now on. Hehehe."
    mc "......"
    e "......"
    e "{i}Ahem...{/i} So, are you ready to go on the quest?"
    mc "Yeah."
    show talksadhappymc
    e "Excellent! Brought your mask?"
    mc "Yes."
    e "Then let's go."
    jump EveQ1

label EveQ1:
    "The two of you head out of the Guild and into the forest."
    "You travel for a while."
    scene ambush1 with fade
    mc "So this Ledric, you know exactly where it is?"
    e "Sort of. The report said it was giving trouble to merchants coming along this path. So it has to be around here somewhere."
    mc "Hmmm."
    e "It's getting dark. We'll set up camp here."
    mc "Ok."
    e "I better scout the surroundings first, make sure it's safe."
    e "Can you set up the camp while I'm gone?"
    mc "Sure."
    e "Thanks."
    e "But remember [mc], the Ledric could be here. If you see it, do not engage alone. Are we clear?"
    mc "Yes."
    e "Good."
    "Eve heads out into the forest. You slowly start to put up the tents."
    mc "{i}Whoa, Eve's tent is huge, just like her bed. She really like things big."
    "While you're setting up the tent, you hear a scream."
    play sound ("screamgirl.wav")
    "Unknown" "HELP!!!"
    mc "Huh!?"
    "Unknown" "Someone, please help!"
    mc "It looks like someone's in trouble!"
    "You quickly run in towards the source of the screaming."
    scene saveledric1 with fade
    mc "{i}Shit!"
    "Woman" "Wait... someone came... A-Are you real?"
    mc "Wh-What happened?"
    "Woman" "You are real! Thank you... Oh thank you... Please, get me out of here!"
    mc "Ok! Wh-What should I do?"
    "Woman" "J-Just find a bind or something, something I can grab on to. Please, this sinkhole is dragging me down!"
    mc "A bind? Ok, ok."
    scene saveledric2 with dissolve
    "Woman" "Please, quickly! M-My daughter is still out there!"
    mc "Your daughter?"
    "Woman" "Yes... ple-"
    $ gameover = "ledricgm"
    label ledricgm:
    scene saveledric3 with vpunch
    "Woman" "Argh! ...It's dragging me down, something's pulling my leg!"
    mc "Huh?!"
    "Woman" "PLEASE HELP!"
    mc "{i}I should help her!"
    mc "{i}Wait! ...This could be a trap! What if this woman is a Ledric? It's possible. I don't even know what it looks like!"
    mc "{i}But there's an equal chance that she's a normal human."
    mc "{i}Fuck, I have to choose quickly!"
    menu:
        "Grab her hand":
            mc "Hold on!"
            scene saveledric4 with hpunch
            "You grab her hand."
            "Woman" "Ha... Thank you."
            mc "I'm going to pull you out."
            "You get a good grip and pull."
            mc "Ugh!"
            "The force dragging her down is too strong. You pull harder."
            mc "Come on!"
            "You keep pulling."
            mc "Just a little more, hold on!"
            scene saveledric5
            pause 0.1
            scene black with vpunch
            "There's a sudden pull on your hand and you fall to the ground."
            mc "Ugh! Did I miss her?!"
            "You feel a sharp pain at you right arm. You try to see what's causing it but to your surprise, you right arm is missing. All you see is a pool of blood."
            mc "Huh?"
            "It takes a few seconds for you to notice that your arm has been torn off."
            mc "AAAAAAAAAHH!!!"
            mc "MY HAND!"
            "Demonic Voice" "Awww... You poor thing."
            scene ledric with flash
            mc "No... it... can't... be...!"
            "Everything starts to fade away."
            scene black with fade
            jump GameOver
        "Let her die":
            mc "{i}No... Eve said I should be cautious!"
            "Woman" "Please, help me... Help me!"
            mc "......"
            "Woman" "It's pulling me down... PLEASE!"
            menu:
                "Help her":
                    mc "Hold on!"
                    scene saveledric4 with hpunch
                    "You grab her hand."
                    "Woman" "Ha... Thank you."
                    mc "I'm going to pull you out."
                    "You get a good grip and pull."
                    mc "Urgh!"
                    "The force dragging her down is too strong. You pull harder."
                    mc "Come on!"
                    "You keep pulling"
                    mc "Just a little more, hold on!"
                    scene saveledric5
                    pause 0.1
                    scene black with vpunch
                    "There's a sudden pull on your hand and you fall to the ground."
                    mc "Urgh! Did I miss her?!"
                    "You feel a sharp pain at you right arm. You try to see what's causing it but to your surprise, you right arm is missing. All you see is a pool of blood."
                    mc "Huh?"
                    "It takes a few seconds for you to notice that your arm has been torn off."
                    mc "AAAAAAAAHH!!!"
                    mc "MY HAND!"
                    "Demonic Voice" "Awww... You poor thing."
                    scene ledric with flash
                    mc "No... it... can't... be...!"
                    "Everything starts to fade away."
                    scene black with fade
                    jump GameOver
                "Don't help her":
                    "Woman" "No... my... son...! I... need to see him!"
    mc "{i}\"Son\"? Wait... is she really telling the truth?"
    "Woman" "HELP ME, YOU SCUM!!!!!!!"
    scene saveledric6 with hpunch
    "With that last shriek, she disappears into the ground."
    mc "........"
    mc "Was... she... r-real!"
    mc "..........."
    mc "Fuck, fuck, FUCK! I should've saved her!"
    mc "!!!!!!!"
    "The ground starts to rumble."
    mc "What the hell?!"
    scene ledric with vpunch
    play music battlemusic1
    "Suddenly, a creature bursts out of the ground."
    mc "Is... that... a Ledric?!"
    "Ledric" "You're smart, human."
    mc "{i}Hehehe. I saw right through you lies, you freak!"
    "Ledric" "Your brain must taste good, then!"
    mc "{i}Shit!"
    "The Ledric lunges at you, you draw your sword and prepare to fight."
    "Just at that moment, an arrow flies past your head and hits the Ledric's chest. It lets out an unsettling shriek."
    e "[mc]! Put your mask on!"
    mc "Ah shit, I forgot!"
    "You quickly take out your mask and put it on."
    "Eve comes running towards you, she has her bow drawn and aimed at the Ledric."
    e "I told you not to engage!"
    mc "I'm sorry, i-it tricked me!"
    e "Why didn't you have your mask on?! Were you trying to get killed?!"
    mc "I'm sorry, I-I-"
    e "We'll talk about this later. Look, it got back to its senses again!"
    e "Get ready for battle."
    mc "Ok!"
    $ killledric += 1
    e "Take the right, I'll take the left. Be careful, it'll probably go for the weaker target first."
    mc "Right."
    "The Ledric starts to charge towards the both of you."
    "The two of you quickly break away. You go to right, Eve goes to the left. The both of you now surround the Ledric. The Ledric pauses for a moment and then turns to you."
    mc "{i}Eve was right."
    e "Hey, over here!"
    "The Ledric doesn't pay attention."
    "Its scorpion tail rushes at you."
    "You jump to the side and dodge it. The stinger of its tail plants itself on the ground."
    menu:
        "Cut the tail":
            "You take your sword and strike at the Ledric tail which is still impaled to the ground."
            "CLINK"
            "It's as if you've struck a brick wall. Vibrations run through your hands and up to your head."
            mc "Urgh!"
            "The Ledric pulls its tail free and swings it at you."
            "You're too slow to react. The tail hits you and you're thrown off the ground."
            e "[mc]!"
            "You're on the ground, gasping for air."
            "The Ledric crawls towards you, its demonic figure towers above you."
            mc "Urgh..."
            "It readies its tail."
            mc "{i}Eve... do something!"
    e "CHUMBAK!"
    "A yellow lightning bolt passes through the Ledric, it falls to the ground."
    "You regain your strength and get up."
    stop music
    scene evekill1 with fade
    pause
    e "Are you alright, [mc]?"
    mc "{i}Huff... huff... huff...{/i} Y-Yeah! What happened to your arm?"
    e "I'm ok, it normally happens when I charge the spell."
    mc "What was that... that yellow flash?"
    e "Oh... that was a lightning arrow."
    mc "Cool."
    e "Hehehe. You did great. My plan worked perfectly."
    mc "Huh... plan?"
    e "It takes some time for me to charge the lightning arrow, which is why I needed you to distract it."
    e "The Ledric is smart but it's not smart enough."
    mc "Oohh... so you brought me on this quest because you wanted a bait?"
    e "I needed bait that won't get himself killed! Hehehehe... And you did perfect."
    mc "Th-Thanks, I guess."
    scene evekill2 with dissolve
    pause 0.4
    scene evekill3
    mc "Look out!"
    scene evekill4
    pause 0.5
    scene evekill5 with dissolve
    "Without you even noticing, your arms move in a split second and cuts the tail before it hits Eve."
    scene evegoo with fade
    pause
    e "Urgh... Th-Thanks, [mc]."
    mc "{i}Huh, did I just cut off its tail just now? Why didn't it work earlier?"
    mc "Are you alright?!"
    e "Y-Yeah."
    mc "That... goo... can you wash it off?"
    e "......"
    mc "Eve?"
    e "Y-Yeah?"
    mc "Can you wash that off?"
    e "Y-Yeah... I mean, no... No. I don't think there's a l-lake nearby. But don't worry, I have some spare clothes... so it's fine."
    mc "Eve, are you alright?"
    e "Yes, I'm fine... I feel a bit dizzy, that's all... I probably exhausted myself."
    mc "Oh, ok... Let's go back to the camp then."
    e "W-Wait!"
    scene black
    "Eve goes towards the dead Ledric and inspects its head."
    e "There it is."
    play sound slash1
    "She stabs at some kind of red stone which is attached to its forehead. She pulls it out."
    scene heartdiamond with flash
    mc "What is that?"
    e "Milly's birthday present."
    mc "Milly's birthday present?"
    e "Hehehe, yeah. There was a reason why I picked this quest. Ledrics normally have these types of red stones on their heads. I thought this would be a perfect gift for Milly. She normally likes things like these."
    mc "{i}She likes parts of dead monsters... Welp."
    e "Isn't it pretty?"
    mc "It's weird. But I have to admit, it is pretty."
    e "Yes! Milly will love this!"
    scene forest with fade
    show talkwanmc
    show blushtalke
    mc "Hey, why didn't you tell me Milly was having her birthday?"
    e "Sorry, I forgot. We elves really don't take birthdays that seriously."
    mc "I can understand that. But still, isn't there going to be some kind of party or something?"
    e "Party?"
    e "No, that would be weird. We've never had one in our village."
    show talkwamc
    mc "So let's make this the first birthday party ever!"
    e "Mh..."
    mc "This will be special for Milly. I'll help you out with the party."
    e "Mmh... Since you guys are allowed to come into the village now, I guess it would be fine."
    e "Ok, let's do it then!"
    mc "Great!"
    show sadtalke
    e "Urgh..."
    mc "Eve... are you alright?"
    show sadtalke
    e "I'm feeling a bit dizzy all of sudden. Shall we go back to the camp?"
    mc "Yeah, let's go. You look like you need some rest."
    "The two of you head back to the camp."
    play music night
    scene ambushn with fade
    show blushtalke
    show thinkmc
    e "Can you take the first watch? I'll rest for a while and take on the next one."
    mc "Don't worry about it. You just get some sleep, I'll keep watch."
    e "The whole night?"
    show talksadhappymc
    mc "Y-Yeah."
    mc "{i}Do I have to keep watch the whole night? I can't stay up that long!"
    mc "{i}But looking at Eve, I can't say no. She looks really tired."
    e "Can... you really do it?"
    mc "Yeah, n-no problem."
    e "Th-Thank you, [mc]."
    hide blushtalke
    hide talksadhappymc
    "Eve goes into her tent."
    mc "{i}I wonder what's up with Eve? She looked really uncomfortable. I hope she's alright."
    mc "{i}Ok, I have to keep watch. I'm not really good at staying up late, I hope I'll be able to make it till the morning."
    "You feel a cold breeze pass through."
    show suprised with hpunch
    pause 0.5
    hide suprised
    mc "{i}Ah shit, I need to make a fire."
    "You see that Eve has already made a fire pit."
    mc "{i}Eve must've made it before coming to help me."
    mc "{i}Now, how do I light it? ...Eve normally uses some kind of spell. I hope she's not asleep yet."
    mc "Uhm... Eve, are you awake?"
    "..."
    "......"
    e "Yes, what is it, little one?"
    mc "Can you help me light this fire?"
    e "Ok..."
    "Eves puts her hand out of her tent and casts a spell."
    e "AGNI."
    scene ambushn with flash
    play sound campfire
    "The fire lights up in an instant. Eve takes her hand back into the tent and everything's silent again."
    mc "Uhm... Thanks, Eve."
    mc "{i}Let's keep watch now."
    scene forrestn with fade
    "You sit by the fire place and start your watch. The forest is a lot quieter than you expected. You don't hear anything, just the occasional rustling of leaves"
    "The warmth of the camp fire is really comforting."
    scene black with fade
    pause 0.2
    scene forrestn with fade
    "Your eyes slowly start to close. You fight it a couple of times. But in the end, you just give up and go to sleep."
    scene black with fade
    stop sound
    pause
    e "Ahhh..."
    window hide
    pause
    e "Ahhh... ahhh..."
    scene forrestn with fade
    mc "Huh?"
    mc "{i}Damn it, I fell asleep."
    e "Aaaahhhhh..."
    mc "Wh-What... Eve?"
    e "Ohh..."
    mc "{i}It's coming from Eve's tent."
    scene evefinger1 with fade
    pause
    window hide
    mc "{i}What?!"
    pause
    mc "{i}Is that... Eve? ...She's n-naked?!"
    e "Ahhhh... oohhh..."
    mc "{i}Is she touching herself?"
    e "So... hot..."
    scene evefinger2 with dissolve
    mc "{i}FUCK!"
    e "[mc]!"
    mc "{i}I'm screwed!"
    e "Please, help me..."
    mc "Eh?"
    mc "What's going on?"
    e "My body feels... so hot. I think I'm going to melt!"
    mc "What?"
    e "It must be because of the... Aaahh... Ledric blood. It must've had... some... kind of stimulant... Aaahhh!"
    mc "Wh-What should I do?"
    e "I don't know. Please... make it stop... my sexual organ is burning, these fluids won't stop coming out!"
    mc "{i}Gulp"
    mc "I-I-I..."
    e "Aaahhh! Quickly... please!"
    mc "{i}Did the Ledric blood really do this...? Eve looks like she's in pain!"
    mc "{i}What should I do......"
    e "Aaahhh!"
    mc "{i}Ugh... Eve's moans are making me hard!"
    mc "{i}Wait, what if..."
    mc "Eve, did you try touching yourself?"
    e "Touching... myself? Aahhh...! What do you... mean?"
    mc "Like touching your pus- I mean, sexual organs."
    e "No... why would I do that?"
    mc "{i}That's it! She needs some stimulation!"
    mc "Try doing it... It'll make you feel better."
    e "What?! ...How could that help?"
    mc "Just try it!"
    e "Ugh! ...Ok."
    scene evefinger1
    "Eve starts to touch herself."
    scene evefinger2
    e "It's not... working!"
    mc "{i}Huh, why is that?"
    mc "{i}Maybe she needs some external stimulation!"
    mc "Eve? C-Can I come in?"
    e "Huh... why?"
    mc "I can help."
    e "But I'm... Aahhh... naked!"
    mc "Just please... I know a way to help you."
    e "......"
    e "Aah! ...Ok... then... I can't stand this any longer!"
    scene evefingera1 with fade
    mc "{i}Lord Merdian... Eve looks-"
    pause
    mc "{i}No! ...You're here to help her. Focus!"
    e "What are you going to do?"
    mc "I'm going to finger you."
    e "Finger me?! Where? ...My sexual organ?"
    mc "Yes... I think you need some external stimulation."
    e "What?! ...Wait, no... I can't!"
    mc "Please Eve, let me help."
    e "Aaahhh...!"
    e "Aaahhhh... aaahhhhh... do it."
    mc "{i}Her pussy is so wet."
    show animationevefinger
    e "Aaahhh... aaahhh..."
    pause
    mc "How do you feel?"
    e "It feels... good..."
    e "Keep going..."
    pause
    e "Aahhh..."
    mc "Your pussy is so wet, Eve."
    e "My pussy? ...Aahhh..."
    mc "Your... sexual organ."
    e "Aaahhh...yes?"
    e "I forgot what it's... called..."
    pause
    e "Aaahhh... My pussy feels great!"
    e "Ahhh... Ahhhhh!"
    e "I'm going to cum!"
    scene evefingera5
    pause 0.3
    scene evefingerend
    pause 0.3
    scene evefingera5
    pause 0.3
    scene evefingerend
    e "Aaaahhhh!!!"
    pause
    scene black
    "Eve falls to the ground."
    mc "Eve!"
    e "......"
    mc "{i}She passed out."
    mc "{i}I should leave her."
    "You slowly leave Eve's tent."
    scene forrestn with fade
    mc "{i}I can't believe what just happened. M-My hand is covered with Eve's... cum."
    mc "{i}Things are going to be very awkward tomorrow."
    mc "{i}Deep breath"
    mc "{i}Well, keeping watch is pointless. I should just go and get some sleep."
    scene black with fade
    "You go into your tent and sleep."
    mc "{i}Thank you, Ledric."
    scene black with fade
    play music forest
    scene ambush1 with fade
    show talkwae
    e "[mc], wake up. We need to go."
    mc "Uhm... Ok... I'm up."
    e "We both overslept, it's almost noon."
    show smilemc
    mc "Oh... yeah."
    mc "{i}Ah... shit... I just remembered what happened last night."
    show talksadhappymc
    mc "Eve, about last night..."
    show sadhtalke
    e "Oh, yes, I'm very sorry."
    mc "No, it's fine. I was only trying to help you."
    mc "{i}She must be feeling guilty. She still thinks I'm a child, after all."
    e "It was unfair."
    mc "No."
    e "But you shouldn't have kept watch all night alone."
    mc "It's ok, I-"
    show suprised
    pause 0.3
    show talkwanmc
    mc "What?"
    e "I thought I would wake up after I rested a little but I slept the whole night. I'm really sorry, [mc]."
    mc "{i}Wait, she doesn't remember?"
    mc "Hehehehe, no problem. You didn't wake up in the middle of the night, right?"
    e "Uhm... No, why?"
    mc "No... it's nothing. I just heard some sounds coming from your tent, that's all."
    e "Oh no... did I snore? ...It must've been my snoring."
    hide talkwanmc
    hide suprised
    mc "I don't know... Hehehehe."
    mc "{i}She doesn't have a clue."
    mc "So, how are you feeling? You looked kinda tired yesterday."
    e "Yeah, I did but I feel great now."
    mc "That's good."
    e "Ok, now quick. Pack up your tent, we need to leave."
    mc "Ok."
    "You pack up your tent and the both of you leave"
    scene ambush1 with fade
    "The both of you are silent for the most part of the journey."
    mc "So... when is the party?"
    e "Huh?"
    mc "{i}Oh god, don't tell me she forgot everything!"
    mc "Milly's birthday party."
    e "Oh yes, we have it this month."
    mc "{i}Ok, she remembers."
    mc "Yeah but which day?"
    e "Oh, any day will do, as long as it's this month."
    mc "What?! We're having a birth \"day\", not a birth month!"
    e "Hahahaha! We really don't take it that seriously, remember? And besides; for elves, a day is too... how should I say this? Umm... \"specific\"?"
    mc "......"
    e "Mh. Ok, tell me this then; Do you have your birthday at the exact definitive time you were born? Like the exact minute and second?"
    mc "Uhm... no."
    e "Of course not, it's the same thing here. But for us, the time variations are a bit different."
    mc "Mmhh. Ok, I can't disagree with that logic."
    mc "So any day is ok?"
    e "Yes."
    mc "Great, we'll have to get a cake."
    e "Yes, that sounds great."
    mc "Are we going to invite everyone?"
    if aerindead == 1:
        e "I... don't think having a big celebration would be right, I mean... Aerin just passed away."
        mc "Yeah, I get that... You're right. It'll just be Sander and me then."
        e "Yes, little one, that would be better."
    else:
        e "Sure."
        mc "Great."
    "The two of you finally arrive at the Guild."
    scene agblr with fade
    show talkwae
    show talkhappymc
    mc "We're here."
    e "Yes, finally."
    show blushtalke
    e "You did great, little one."
    mc "Oh... thanks."
    hide talkwae
    e "Hehehehe. I'll go to my room now. Make sure you tell Sander about the party."
    mc "Ok."
    hide blushtalke with easeoutleft
    show thinkmc
    mc "{i}Is it really a good thing that she forgot about what happened? ...No point thinking about that."
    mc "{i}Besides, it all happened because of the Ledric blood. It's not like Eve wanted to do it, she had no choice."
    mc "{i}I better forget it as well."
    show talkwas with easeinleft
    sa "Hey little man, how was the quest?"
    show talkwamc
    mc "It was great, we took down the Ledric."
    sa "Nice."
    mc "Eve said you had... a bad history with them."
    sa "Oh, hehehehe, yeah. Let's just say I almost lost my dick to one of em."
    mc "......"
    sa "So, anything else happen?"
    mc "Hmm... N-Nothing else."
    show smirks
    sa "Didn't anything... \"interesting\" happen?"
    show talkwanmc
    mc "Uhm... What do you mean?"
    sa "Come on man, you were with Eve alone. I thought you would've gotten a piece of that ass."
    mc "What! W-We just went on a quest!"
    sa "Yeah but I thought... something might happen."
    mc "Jeez, are you serious?! Do you expect something to happen just like that? What do you think this is, some kind of romance novel?"
    sa "Hahahaha! Don't take it too seriously, kid. But I thought you really had a chance."
    mc "...Hmm?"
    sa "Ahh... I didn't tell you right."
    mc "What?"
    sa "You know, Eve normally likes younger people."
    show suprised
    pause 0.5
    hide suprised
    mc "Huh?!"
    sa "Yeah, I've been with her enough. She's normally attracted to small dudes. She says they're cute and all but I know she likes them in other ways as well."
    mc "{i}gulp{/i} in what way?"
    sa "...You know what I mean."
    mc "Really?"
    sa "Yeah kid, so I say, go for it."
    mc "...What... about you? Don't you like Eve?"
    sa "Me? Pfft, hell no, little man."
    sa "Eve's like my big sister. It would be weird if we were together."
    mc "Uhm... Yeah but you still peep on her."
    sa "Hey! That's totally different!"
    mc "Oh yeah?"
    sa "Yes! Loving someone isn't just the same as peeping on someone or... or... having sex with them!"
    sa "It's totally different. You need to feel it."
    mc "{i}Whoa, Sander. He really has a mature side to him."
    mc "You're making sense."
    mc "That's weird."
    sa "Hahahahaha! Just a tiny drop from your Sensei's Ocean of Wisdom."
    show talkhappymc
    hide talkwanmc
    mc "Thanks, I'll keep that in mind."
    mc "Oh, another thing, we're giving Milly a birthday party."
    sa "Really? That's nice. I'll bring the cake, there's this really good baker. Her cakes are the best!"
    mc "Ok, that's great."
    scene agblr
    show normals
    show smilemc
    mc "See you at the party then?"
    hide smilemc with easeoutright
    sa "Hey! When is the party?"
    mc "Don't know, ask Eve."
    sa "Huh?"
    $ time = 4
    $ ledricquest += 1
    jump home



label EveQ2:
    hide screen screenmap
    hide screen hud
    stop music
    if time < 3:
        scene agblr
    else:
        scene agblrevening
    show talkhe
    show smilemc
    e "Oh, [mc], there you are. It's time for the party."
    mc "What? Really?"
    e "Yes, Sander said he would bring the cake. Let's go."
    mc "Ok... but I didn't even get her a gift."
    e "Why, the Ledric Stone! We both took it together, right?"
    e "So, it's a gift from the both of us."
    mc "Hmm... If you say so."
    e "Let's go now."
    mc "Ok."
    scene black with fade
    "The two of you head to the Elf Village."
    play music happy
    if aerindead == 1:
        scene evehouse
        show smilemc
        show smilee
        show talkhmi
        mi "Yay! [mc], you came!"
        mc "Happy Birthday, Milly."
        mi "Thank you!"
        mi "I heard it was your idea to put a party for me."
        mc "Uhm, kinda, yeah."
        show talksmi
        mi "Thank you, [mc]! I was really sad these past few days... because... of Aerin."
        mc "I'm sorry, Milly."
        mi "It's ok, this really lightned up my mood."
        mc "I'm glad."
        "{i}Knock Knock"
        e "That must be Sander. I'll go get it."
        hide smilee with easeoutright
        pause
        show talkwae with easeinright
        show talkwasop with easeinright
        sa "Look what I brought!"
        scene millybday with flash
        mi "Whoah, is that cake for me?"
        sa "Yeah and it's not just any cake; it's a birthday cake from the greatest baker in Astylla!"
        mi "Heeeeeee~! Thank you, Uncle Sander!"
        sa "Hehehe. No worries but don't call me uncle. You're older than my great grandmama."
        mi "Hehehhehe!"
        scene heartdiamond with flash
        e "And here's a gift from [mc] and me."
        mi "Wooooow! Can this day get any better?!"
        scene heartdiamond2 with dissolve
        mi "It's so pretty!"
        e "It's a Ledric Stone."
        mi "Ledric Stone???"
        mi "Thank you, sister! Thank you, [mc]!"
        scene evehouse with fade
        "The four of you celebrate the party. The cake was good. Sander wasn't lying. All of you sing, dance and have a good time."
        show talkwasop
        show smilemc
        show talkhmi
        show smilee
        mi "Wow, this was so much fun! Thank you, everyone!"
        sa "No problem kiddo."
        mc "Yeah, we're glad you enjoyed it."
        show talksmi
        mi "I wish Aerin was here."
        show sadtalke
        e "I'm sure she's watching."
        sa "I think it's time I took my leave then."
        hide talkwasop with easeoutright
        mi "Bye, Uncle Sande!"
        sa "Stop calling me uncle, granny!"
        mi "Hihihihi!"
        mi "I'll be going too then. I can't wait to put this Ledric rock onto my collection!"
        mi "Bye! Thank you for the party, [mc], Eve!"
        hide talksmi
        hide talkhmi with easeoutright
        mc "I'm glad she liked our gift."
        e "Hehehe. Yes, me too."
        mc "I guess I'll leave too."
        show blushtalke
        e "[mc], wait. I wanted to thank you."
        e "For helping me with the Ledric and also for making Milly happy."
        show talkwamc
        mc "What? I barely did anything."
        e "You're wrong, [mc]. You're a great person. Thank you."
        show surprisedblushmc with vpunch
        "Out of nowhere, Eve gives you a kiss on the lips."
        mc "{i}EVE!"
        show talksadhappymc
        hide surprisedblushmc
        e "I-I'm sorry, [mc]. I-I just wanted to thank you. I don't know what came over me..."
        mc "{i}My head is spinning."
        mc "N-No problem, Eve."
        e "I'm really sorry, I should go."
        hide sadtalke
        hide smilee
        hide blushtalke with easeoutleft
        mc "Eve!"
        scene elfvillage with fade
        mc "{i}What was that, really? She was kissing me for like a minute. Is it an elf tradition or something?"
        "You head back to Randel thinking what just happened. You still feel the taste of Eve's lips."
        mc "{i}That was weird. I should go ask her about it."
        $ time = 4
        $ evekiss += 1
        jump home
    else:
        scene evehousebd1 with fade
        mi "Yay! [mc], you came!"
        mc "Happy Birthday, Milly."
        n "Hey there, [mc]."
        mc "Oh, hey, you guys are already here."
        n "Yup, Aerin and I were tidying up this dump until you came."
        e "Hey, don't call it a dump."
        a "It was a dump, Eve."
        mi "Yeah sis, you never clean this place."
        e "It's because I don't come here that often."
        a "Whatever, it's clean now."
        e "Hmph!"
        "{i}Knock Knock"
        e "That must be Sander. I'll go get it."
        pause
        scene evehousebd2
        sa "Look what I brought!"
        scene millybday with flash
        mi "Whoah, is that cake for me?"
        sa "Yeah and it's not just any cake; it's a birthday cake from the greatest baker in Astylla!"
        mi "Heeeeeee~! Thank you, Uncle Sander!"
        sa "Hehehe. No worries but don't call me uncle. You're older than my great grandmama."
        mi "Hehehhehe!"
        e "And here's a gift from [mc] and me."
        scene heartdiamond with flash
        mi "Wooooow! Can this day get any better?!"
        mi "It's so pretty!"
        scene heartdiamond2 with dissolve
        e "It's a Ledric Stone."
        mi "Ledric Stone???"
        mi "Thank you, sister! Thank you, [mc]!"
        "All of you celebrate the party. The cake was good. Sander wasn't lying. All of you sing, dance and have a good time."
        scene evehousebd2 with fade
        mi "Wow, this was so much fun! Thank you, everyone!"
        sa "No problem, kiddo."
        mc "Yeah, we're glad you enjoyed it."
        a "I think we'll have another one next year."
        mi "REALLY?!"
        a "Yeah, I can make the cake for that."
        a "By the way, [mc], why didn't you tell me to bake the cake? You told me that you... liked my baking, right?"
        mc "Y-Yeah but Sander said he would bring one."
        a "Hmm... it's ok. Next time you'll see, my cake will be better."
        sa "I doubt that."
        a "Huh, what did you say?"
        sa "Mary's cakes are the best."
        scene evehousebd3
        a "Hmph... You wouldn't be saying that if you had tasted one of my cakes."
        if sanderatemuff == 1:
            sa "I did eat one of your muffins. It wasn't bad but it just didn't surpass Mary's muffins."
            a "Impossible!"
            mc "{i}This cake debate is getting serious."
        else:
            sa "Still, I don't think you'll be able to surpass Mary."
            a "HUH?!?!"
            mc "{i}This cake debate is getting serious."
        a "Since when are you such a cake expert?"
        sa "Hehehehe!"
        sa "I'm one of the judges in Randel's annual cake competitions."
        "{color=#47E847}Aerin and {/color}[mc]" "WHAT?!"
        sa "Hehehe!"
        e "Ok, ok, enough with the cake debate."
        n "Yeah."
        mi "There's one solution to this problem,"
        "Aerin and Sander" "Hmmm?"
        mi "There will have to be two cakes for my next birthday."
        a "......"
        sa "......"
        a "Yeah, that's a good idea. We'll see whose cake is better then."
        sa "Challenge accepted!"
        mi "{i}Hehehe, fools."
        scene evehousebd2
        n "Ok guys, I'm heading out then. Bye!"
        a "Me too."
        mi "Bye!"
        sa "I think it's time I took my leave then."
        mi "Bye, Uncle Sander!"
        sa "Stop calling me uncle, granma!"
        mi "Hihihihi!"
        mi "I'll be going too then. I can't wait to put this Ledric rock onto my collection!"
        mi "Bye! Thank you for the party, [mc], Eve!"
        scene evehouse with fade
        show talkwamc
        show smilee
        mc "I'm glad she liked our gift."
        e "Hehehe. Yes, me too."
        mc "I guess I'll leave too."
        show blushtalke
        e "[mc], wait. I wanted to thank you."
        e "For helping me with the Ledric and also for making Milly happy."
        show talkwamc
        mc "What? I barely did anything."
        e "You're wrong, [mc]. You're a great person. Thank you."
        show surprisedblushmc with vpunch
        "Out of nowhere, Eve gives you a kiss on the lips."
        mc "{i}EVE!"
        show talksadhappymc
        hide surprisedblushmc
        e "I-I'm sorry, [mc]. I-I just wanted to thank you. I don't know what came over me..."
        mc "{i}My head is spinning."
        mc "N-No problem, Eve."
        e "I'm really sorry, I should go."
        hide sadtalke
        hide smilee
        hide blushtalke with easeoutleft
        mc "Eve!"
        scene elfvillage with fade
        mc "{i}What was that, really? She was kissing me for like a minute. Is it an elf tradition or something?"
        "You head back to Randel thinking what just happened. You still feel the taste of Eve's lips."
        mc "{i}That was weird. I should go ask her about it."
        $ evekiss += 1
        $ time = 4
        jump home



label EveQ3:
    mc "{i}I should talk to Eve about what happened in the party."
    play sound doorknock
    mc "......"
    mc "{i}No answer. Let's see if the door's locked."
    "You turn the handle and push on the door."
    "It opens"
    scene everoombook with fade
    mc "{i}Shes not here."
    mc "I'll wait here till she gets back."
    "You see Eve's diary again, just where you left it last time."
    mc "{i}Just a little peek. Let's see if she has written anything about our quest."
    "You flip through the pages."
    "Diary" "Milly's birthday is coming up. She'll be 180. My little sister is all grown up now."
    "Diary" "I saw a notice on the Quest Board today. It said there was a Ledric in the nearby forest and that it needs to be dealt with. This is perfect. Ledric Stones are really pretty, Milly would love them."
    "Diary" "Sander said he won't be coming, just as I predicted. So, I thought of taking [mc] with me. It would be a good way for us to bond."
    mc "{i}Reading diaries are amazing. It's like you're looking into a person's mind."
    "Diary" "Something truly awful happened yesterday."
    mc "{i}Hmmm?"
    "Diary" "I'm ashamed of myself. Last night, [mc] saw me naked. And what's worse, I let him touch my sexual organ. (He calls it a pussy)"
    mc "{i}What? Eve remembers!"
    "Diary" "It was all because of that Ledric blood. It acted as some kind of stimulant, which made me want to- UGH- I don't want to think about it anymore."
    "Diary" "[mc] thinks I forgot all about it, which is good. I don't know how I'm supposed to apologize."
    mc "{i}Apologize?! What the hell is wrong with her? I should be thanking her!"
    "Diary" "But ever since that day, whenever I see [mc], I see him differently. I know I said earlier that I have motherly feelings for him but now, I'm not sure if that's exactly what I'm feeling."
    "Diary" "I feel like doing things with him, things that a mother should not do with her son."
    mc "{i}Holy-"
    "The door suddenly opens."
    scene everoomblr
    show angrytalke with vpunch
    show worriedmc
    e "[mc]!"
    mc "Eve... Hey."
    e "Were you reading my log book?"
    mc "Your log book? ...Uhm..."
    menu:
        "No":
            show talkmc
            mc "No?"
            hide talkmc
            show talksadhappymc
            e "It's still on your hands."
            mc "Oh. Hehe..."
        "Yes":
            show talksadhappymc
            mc "Y-Yeah..."
    e "How could you, [mc]?! You can't invade someone's privacy like that!"
    mc "I'm sorry, Eve... I-I just wanted to talk to you."
    e "You're very bad, [mc]!"
    mc "{i}Why is she scolding me like I'm a child?! Am I going to get spanked now or something?!"
    mc "{i}Hmm... That would be great though."
    mc "Eve, I wanted to talk about what happened at the party."
    show blushsadtalke
    e "Wh-What?!"
    show talkwanmc
    mc "You kissed me..."
    e "Huh... No... I-I just... slipped."
    mc "What?!"
    e "Yes..."
    mc "Ok then, why did you act like you forgot what happened that night?"
    e "Wh-What night?"
    mc "The night you asked me to finger you."
    show supriseblushe
    e "F-F-Finger?! Nothing like that happened! Wh-What are you talking about?"
    mc "Don't lie, Eve. It's here in the diary."
    e "So you read it!"
    mc "Yeah and what about this? \"I feel like doing things with him, things that a mother should not do with her so-\""
    e "NOOOOOOO! Give it here!"
    "Eve swipes the book from your hands."
    hide supriseblushe
    e "You can't read that, [mc]!"
    mc "Eve, just tell me what's going on?"
    e "......"
    e "I'm sorry, [mc]! I shouldn't have done what I did last night. I'm ashamed of myself, I made you touch my pu- ...sexual organ."
    e "I used you for my own pleasure without thinking what kind of emotional toll it would take on you!"
    mc "{i}She's acting like she raped me."
    mc "But you didn't force me."
    e "I did! Otherwise, why would you do something so shameful?!"
    show worriedmc
    mc "I liked it."
    e "I-I... did but it was still something I should never have done!"
    mc "Eve, I said I liked it."
    show supriseblushe
    e "Wh-What?!"
    mc "You have nothing to apologize for. In fact, I should thank you."
    hide supriseblushe
    e "......"
    e "No, no, what have I done?! I've tainted your mind! You shouldn't be thinking like that!"
    mc "No, Eve-"
    e "[mc], please go... You shouldn't be here anymore."
    mc "What?"
    e "Please, leave, [mc]..."
    mc "......"
    mc "Ok."
    $ time = 4
    scene everoom with fade
    mc "{i}Damnit! Why is Eve like this?!"
    mc "{i}I need to show Eve that I'm not a little kid. And that I really like her."
    $ eveknow += 1
    jump home



label EveQ4:
        mc "OK, time to man up. I'm going to tell Eve exactly how I feel."
        play sound doorknock
        mc "......"
        mc "{i}You can't be serious. Does she ever answer the door?"
        "You turn the handle and push on the door"
        "Of course, it opens."
        mc "{i}Eve having a door is completely pointless."
        scene everoomin with fade
        play music bath
        mc "{i}Eve's in the bath again. I'll wait till she's here."
        "......"
        mc "{i}What do I say when she comes out?!"
        mc "{i}...Hmmm..."
        mc "{i}Thinking back on what Sander said, do I really love Eve or do I just want...{p}Pleasure?"
        stop music
        mc "......"
        "The door opens."
        scene evetowel1
        e "[mc], why are you here?"
        mc "I came here to confess."
        mc "I really like you and it had nothing to do with what happened that night."
        e "......"
        mc "And I'm not a little kid, these feelings are real."
        e "No, little one. You still don't understand these things."
        mc "I'm 19. I know it's little in elf years but I'm not a kid."
        e "But... why would you like this old elf anyway, little one? There are a lot of beautiful young girls out there."
        mc "I really need to get you a mirror."
        e "Huh?"
        mc "Look at yourself. you're one of the prettiest women I've ever seen!"
        e "......"
        mc "I really do love you, Eve."
        e "......"
        mc "Do you... feel... the same way?"
        e "......"
        e "...I... do..."
        mc "Then... you don't need to be afraid."
        "You move towards Eve."
        e "[mc], what are you-"
        menu:
            "Pull down her towel":
                scene evetowel with dissolve
                pause
                window hide
                e "[mc]..."
                mc "You're so beautiful, Eve."
                pause
                e "......"
                mc "You said you wanted to do things with me, right? Things a mother won't do with her son."
                e "What kind of things did you mean?"
                e "I-I-I..."
                "You start to undress."
                e "[mc]... don't..."
                mc "I want to have sex with you."
                e "E-Eh?!"
                "You grab Eve and push her to the bed."
        scene evesex1 with vpunch
        e "[mc], wh-what are you doing?!"
        pause 3
        mc "Eve, just relax."
        scene evesex2 with dissolve
        pause 7
        e "[mc]..."
        show evesex movie
        e "Aaaahhh..."
        pause
        mc "{i}Eve's skin is so soft."
        e "It feels good, [mc]."
        mc "Who's the little one now, huh?"
        pause
        e "Ahhhhhh... You're so good, [mc]..."
        menu:
            "Faster":
                show evesexfast movie
        e "Aahhhh...!"
        pause
        e "I'm going to cum..."
        mc "Me too..."
        mc "I'm going to do it inside."
        e "Ok... cum inside me!"
        scene evesexcum with flash
        pause 0.1
        scene evesexcum with flash
        pause 0.1
        scene evesexcum with flash
        pause
        scene black with fade
        e "Th-That felt amazing, [mc]..."
        mc "{i}Huff... huff...{/i} Thanks."
        e "I didn't know you could be so wild."
        mc "Hehehehe."
        e "But..."
        scene evesleep1
        e "You're still my little one."
        menu:
            "I love you, Eve.":
                scene evesleep2 with dissolve
                mc "I love you, Eve."
                e "......"
                e "I love you too, [mc]."
                $ loveeve += 1
            "Say nothing":
                mc "......"
        "Your face is gently rested on Eve's soft breasts."
        mc "{i}Haaaaah... so... soft."
        "The two of you fall asleep."
        scene black with fade
        "Next morning..."
        e "[mc]!"
        e "[mc]... wake up!"
        scene everoomblr
        show blushtalke
        pause
        show smilemc
        mc "{i}Yawn{/i} ...Morning, Eve."
        e "Good morning, little one."
        mc "{i}Ehh... still calling me little one?"
        e "You'll have to leave now... before the others wake up."
        e "If they see us together... it would be..."
        show talkwamc
        mc "Yeah, I get it, Eve. I don't like to explain myself either."
        e "Thank you for understanding."
        mc "I'll go then."
        e "Ok... and [mc]?"
        e "Last night was... amazing."
        show talksadhappymc
        mc "Thanks, I had a great time too."
        $ time = 0
        call sleepvars from _call_sleepvars_17
        $ evesex += 1
        jump guild
