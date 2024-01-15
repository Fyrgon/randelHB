default cynthiaPelt = False

label preCynthia:
        pause
        if sawcynth == 1:
            hide screen hud
            mc "Oh... it's Cynthia!"
            scene cynthia
            mc "...She's so beautiful."
            mc "She seems really friendly too."
            mc "I wonder if she's still single?"
            mc "Should I go talk to her?"
            menu:
                "Yes":
                    mc "I gotta be a man... Ok [mc], you can do this!"
                    g "Hey, [mc]!"
                "No":
                    mc "Nooo... I can't, I'm socially awkward. I-I don't even know what to say to her!"
                    g "Hey, [mc]!"
            scene academytalkblr
            show normalmc
            show normalgabe
            show talksadhappymc
            mc "Oh... Hey, Gabe."
            hide talksadhappymc
            show talkgabe
            g "I see you're early today."
            hide talkgabe
            show talkhappymc
            mc "Haha... Yeah."
            hide talkhappymc
            show talkwagabe
            g "Watcha' doing standing here anyway?"
            hide talkwagabe
            show talksadhappymc
            mc "It's nothing, I was just... just... looking at the notice board... Yeah."
            show angrygabeblush
            "Gabe leans and looks behind you."
            mc "......"
            show cutegabe
            g "You know what? You better go and ask her out rather than stalking her all the time."
            mc "What?! No... I wasn't-"
            g "Whatever! I'm going to class. See yah later, [mc]."
            scene academytalkblr
            show talkwanmc
            mc "Gabe, wait-"
            show thinkmc
            mc "{i}What's her problem anyway...?"
            $ sawcynth += 1
            jump academy
        mc "Wait... Who's that?"
        scene cynthia
        mc "She's so beautiful... How have I never seen her before?"
        mc "Is she new in town or something?"
        g "Oh [mc], watcha' doing?"
        scene academytalkblr
        show normalmc
        show normalgabe
        show talksadhappymc
        mc "Oh! Gabe, hi."
        show talkgabe
        hide talksadhappymc
        g "Hello, you're early today."
        hide talkgabe
        show talkhappymc
        mc "Haha... Yeah... "
        hide talkhappymc
        show talkgabe
        g "Oh, it's Cynthia..."
        show talkwanmc
        mc "Who?"
        g "Cynthia, the new girl over there."
        mc "Where?"
        mc "Oh, her!"
        show angrygabeblush
        pause
        show cutegabeu
        g "...I know you were staring at her."
        show talksadhappymc
        mc "Me? Nah..."
        hide cutegabeu
        show talkgabe
        hide angrygabeblush
        g "Pfft, whatever!"
        mc "Where is she from?"
        g "She's from Thane."
        mc "In the east?"
        g "Yeah. Thane is under high alert, since it's near Fort Hern."
        g "If the fort goes down, they'll be the first to get attacked."
        mc "But why now? Hern's still holding, right?"
        g "Yeah, but for how long? They say the Demon King's army is getting stronger every day."
        mc "......"
        g "Anyway, I hear she's a really nice person. Friendly, caring and beautiful, of course."
        hide talkhappymc
        hide talkgabe
        mc "......"
        g "We better get going. Class will be starting soon."
        mc "Ok."
        $ sawcynth += 2
        jump academy




label cynthiaBeginning:
        hide screen hud
        mc "I wonder who the dude in the green shirt is? He just stands there all day like a weirdo..."
        "Suddenly, someone runs up and bumps into you."
        scene academytalkblr with vpunch
        show angryc
        show normalmc
        c "Ow! What in the hell?! {b}WATCH WHERE YOU'RE GOING, FU-{/b}"
        show wac
        show suprised
        pause
        c "-uuuuuu...riend!"
        mc "What?"
        show talkshc
        c "I mean... sorry! I didn't see you there, friend!"
        c "...Ok, bye!"
        hide wac
        hide angryc
        hide talkshc with easeoutright
        pause
        mc "{i}What was that? ...Did I just bump into Cynthia?"
        mc "{i}Did she call me a..."
        mc "{i}No, I must have heard it wrong. It's Cynthia, she wouldn't say something like that."
        $ sawcynth += 1
        jump academy



label questcynth:
    scene ambush1 with fade
    play music forest
    show normalmc
    show normalcb
    show talkwanmc
    mc "Can you please tell me where we're going? You didn't give me a chance to read about the quest before storming off."
    hide talkwanmc
    show talkwancb
    c "Ugh... Ok, listen. It's simple, there's been some news about a group of bandits nearby attacking travelers. "
    c "So I really hope you actually have your sword, because our job is to take them down."
    hide talkwancb
    show talkwanmc
    mc "For Pete's sake, I have my sword! What are we even supposed to do? Kill them or something?"
    show talkwancb
    c "Of course."
    show suprised
    mc "What! Are you serious?"
    hide suprised
    c "Yeah? Oh wait, do you think they'll leave if we asked them nicely? My god [mc], you genius! I can't believe nobody thought of that!"
    c "They are bandits, they kill people. We have to use force."
    show talkwanmc
    mc "B-But they're people... H-How are we going to kill them?"
    hide talkwamc
    c "You kill monsters, right?"
    show talkwanmc
    mc "Yeah..."
    hide talkwanmc
    c "Do you hesitate?"
    show talkwanmc
    mc "N-No, but they're-"
    hide talkwanmc
    c "Monsters? "
    c "Well let me tell you something; these \"people\" steal, murder and rape innocent people. These \"people\" are worse than monsters."
    mc "......"
    c "So do me a favor? Quit whining and do what you have to do."
    show talkwanmc
    mc "Ok..."
    c "Now shut up and follow me."
    scene ambush1 with fade
    "The two of you walk silently through the woods. Cynthia radiates an aura of general agitation. A completely opposite personality and attitude than the fake cheeriness she exhibits around everybody else."
    scene forrest with fade
    show talkwancb
    show normalmc
    c "The bandit camp should be nearby."
    c "Ok, Ehm... What was your name again?"
    mc "...[mc]."
    c "Ok [mc], we'll have to scout the area. We can cover more ground if we split up."
    c "Find the base and look around for about ten minutes. Then we'll regroup here. And for the love of god, keep quiet."
    mc "{i}Why is she bossing me around?"
    mc "{i}...And why am I ok with it?"
    show talkwamc
    mc "Sounds like a plan."
    scene ambush1 with fade
    "The two of you separate and start to scout the area, keeping mindful of traps that may have been placed around the camp."
    "After a few minutes you spot the bandit camp, but realize that the camp has apparently been attacked already. There is blood everywhere but no sign of any dead bandits."
    mc "{i}What the hell happened here? Where are the bodies? Did Cynthia do this?"
    mc "{i}No, she went in the other direction, it can't be her... and I would've heard something if there was a big brawl here while I was scouting... I better leave and regroup with Cynthia."
    "You carefully head back to where Cynthia told you to meet her. As you near the area you hear a deep gravelly voice..."
    "Unknown" "Oohh... look what we have here?"
    c "Get off me!"
    "Unknown" "Hehehe..."
    window hide
    mc "{i}Oh shit, Cynthia's in trouble!"
    scene cynthiaba1
    c "Stop!"
    pause
    "Unknown" "You've got a nice pair of tits, Missy..."
    c "Ugh! Please stop."
    mc "{i}What should I do?"
    label abandonCynthiasRoute:
    menu:
        "Watch":
            if knowAbandonCRoute == False:
                $ knowAbandonCRoute = True
                "This choices will end Cynthia's route, are you sure?"
                menu:
                    "No":
                        jump abandonCynthiasRoute
                    "Yes":
                        jump abandoningCynthiasRoute
            label abandoningCynthiasRoute:
            mc "{i}This bitch deserves this... may as well have some fun watching."
            $ persistent.abandonCynthia = True
            "Unknown" "Let's get a look down there..."
            scene cynthiaba2 with dissolve
            pause
            c "NO! {i}...sob"
            "Unknown" "Mhmm... smells nice."
            pause
            "Unknown" "I hope you're a virgin, Missy, because I lo-"
            scene cynthiaba3 with vpunch
            play sound slash1
            "Unknown" "Urk!"
            pause
            scene cynthiaba4 with vpunch
            pause 1
            c "Fucking animals!"
            mc "{i}Oh.. She just... killed that guy."
            "You sheepishly come out of the bushes"
        "Save her":
            $ persistent.saveCynthia = True
            $ savecynth += 1
            mc "{i}She might be a bitch, but I have to help her."
            "You come out of the bushes screaming."
            mc "COME GET SOME, ASSHOLE!!"
            "Unknown" "What the fu-"
            play sound slash1
            scene cynthiaba5 with vpunch
            pause 1
            mc "Huh- W-What?"
            scene cynthiaba4 with vpunch
            c "Fucking animals!"
            pause
            mc "{i}She just... killed that guy..."
    mc "Are you alright?"
    c "Yeah, yeah... this pigshit got the jump on me, came out of nowhere."
    menu:
        "Mention that you can see her tits":
            mc "Uhm... Cynthia, you're-"
            c "Huh? Wh-What is it?"
            c "......"
        "Say nothing":
            mc "{i}She has no idea her tits are out. Wow, they look amazing..."
            c "What are you staring at, loser?"
            c "......"
    scene cynthsu with vpunch
    $ persistent.cynthCovers = True
    c "Look away, you fucking pervert!"
    pause
    mc "Hehe."
    "Cythia quickly covers herself up."
    label beheading:
    $ gameover = "beheading"
    scene qtebehead1 with fade
    c "Urgh... Did you manage to find anything?"
    mc "Yeah, I found their camp."
    c "Really, how many are there?"
    mc "None."
    c "What?"
    mc "The camp's empty. There was blood everywhere. I think they were attacked."
    c "That doesn't make any sense, we were the only ones assigned to the quest."
    c "Wait... were the bodies missing?"
    mc " Uhm... yeah... How did you-?"
    scene qtebehead2
    pause 0.3
    scene qtebehead3
    if swordlvl >= 8:
        $ renpy.notify ("{color=#fff}Sword skill check: {color=#00C413}Success! ([swordlvl] >= 8)")
        jump liveqte1
    $ renpy.notify ("{color=#fff}Sword skill check: {color=#A50000}Fail. ([swordlvl] < 8)")
    c "DUCK!"
    $ qtesection = "liveqte1"
    call screen qte1

label liveqte1:
    scene qtebehead5
    pause
    scene bandit1
    play music battlemusic1
    mc "What the hell?!"
    c "......"
    mc "C'mon Cynthia, we can take him!"
    c "Run."
    mc "What!? It's two on , and he's already injured-"
    c "I SAID FUCKING RUN!"
    mc "Your bag!"
    c "Leave it!"
    "Cynthia grabs hard on your hand and runs."
    scene ciarun

    mc "Why are we running?"
    pause
    c "Those eyes... I should've noticed them earlier."
    mc "What about his eyes?"
    c "That person should be dead. I stabbed him in the heart."
    c "He had to have been possessed. That means there's a Lelluk nearby."
    mc "A what!?"
    c "A Lelluk... It's a type of demon. It can reanimate dead bodies."
    c "They're really rare. How did it even manage to get this far from the border?"
    c "I think it's responsible for what happened at the bandit camp. It made the bandits slaughter each other."
    "The two of you keep running."
    mc "I think we've lost him."
    scene ambushn with fade
    play music night
    "Both of you pause for a moment, trying to catch your breath."
    show normalcb
    show talkwancb
    show normalmc
    c "{i}Huff...{/i} You sure we lost him?"
    hide talkwansb
    show talkwanmc
    mc "{i}Huff...{/i} Yeah... {i}huff..."
    hide talkwanmc
    show angryc
    c "We have to kill it."
    hide angryc
    show talkwanmc
    mc "...Wh-What, do you mean... the Lala-"
    show talkwancb
    c "The Lelluk!"
    mc "But our job was to take out the bandits!"
    c "We can't let this thing stay here."
    c "The longer it's around, the more people it will possess. If we don't do something, this thing will get out of hand."
    mc "But I don't think we'll be able to do that right now. It's already dark, we won't stand a chance against that Lullak."
    c "It's Lelluk! ...Urgh... I hate to say this. but you're right."
    mc "Then let's camp here for the night."
    hide talkwancb
    show wac
    c "...Shiiit."
    hide wac
    mc "What?"
    show talkwancb
    c "My bag... I left it."
    show talkwamc
    mc "Well, I did mention your bag..."
    c "..."
    mc "Heheh, I guess we're down to  tent then. I don't mind sharing."
    c "Gah! Unbelievable..."
    mc "So what do you say? You wanna sleep outside or in my tent?"
    c "I don't really have a choice here..."
    mc "Hehe. Ok, I'll set the tent up"
    scene forrestn
    "You pitch in the tent."
    mc "Come in, m'lady!"
    c "Try anything, and I will kill you."
    mc "Ok, ok, sheesh."
    scene sleepcynthia5
    pause
    "..."
    "......"
    "........."
    mc "{i}Huff{/i}, What a day, huh?"
    c "......"
    mc "My legs hurt like crazy. You're a really fast runner."
    scene sleepcynthia1
    c "Can you just shut up?"
    mc "...I was just trying to break the tension. You don't have to be so mean."
    c "We're supposed to sleep."
    mc "Why are you like this? You are always being mean to me and acting like a cute princess in front of literally everyone else."
    c "......"
    c "People always believe what they see. If I just act cute and friendly, everyone then thinks I'm a cute, innocent princess who needs to be idolized and adored."
    mc "I figured as much... but why?"
    c "Because it's fucking awesome. Those stupid guys at the Academy do anything I tell them to. Do you know how many gifts I've gotten in the past few weeks?"
    mc "I can imagine."
    c "And I've yet to complete a single assignment!"
    mc "Let me guess, those \"stupid guys\" did them for you."
    c "Yes!"
    c "The stupid bitches at the Academy are annoying though, always following me around asking this and that."
    c "\"Do you think Lenius likes me?\", \"Do you think my boobs look big in this dress?\" ...Urgh, I don't give a shit! Just fucking shut up!"
    mc "......"
    mc "The way you killed that guy back there... I mean, he was already dead, but... you showed no hesitation."
    c "......"
    c "I lived in Thane. That city has been in chaos since before I was even born. Maybe because it was the closest to the border."
    c "Since the army was so preoccupied with the border, bandits would always break into houses and steal, murder... Rape."
    c "People were always on the edge, we had to be ready to defend ourselves."
    mc "So... you've killed people before?"
    c "......"
    c "Yeah... but I don't like to call them people."
    mc "I never knew it was that bad. I mean I've heard the town had some problems, but I didn't think it was that bad."
    c "The town was beyond saving in the eyes of the kingdom, so they didn't really care. They were too busy holding the border."

    mc "It must have been very tough for you, I'm sorry."
    c "......"
    mc "{i}I can kinda understand now why she's the way she is. It must've been very hard to survive in a place like that."
    c "I'm sorry if was overly mean to you, it's just that I don't really trust people."
    mc "It's ok, I get it."
    if savecynth == 1:
        c "But you're a good person..."
        show screen notice
        pause
        hide screen notice
        mc "Huh?"
        c "You tried to save me... even though I was such a bitch to you."
        mc "I just did what I had to do... No, what {b}anyone{/b} should do in that situation."
        scene sleepcynthia2
        c "...Even though you were definitely gonna get beaten up pretty bad."
        scene sleepcynthia4
        mc "Ye-"
        mc "Wait... what!? Don't underestimate me! I could've taken him on easily!"
        c "Sure, sure, Mr. Hero. Heheh."
        mc "{i}She laughed!"
        "..."
        "......"
        "........."
        c "It's so cold in here."
        mc "...Wanna cuddle?"
        scene sleepcynthia3
        c "NO!"
        scene sleepcynthia4
        mc "......"
        c "{i}Idiot."
        $ persistent.cynthiaTent = True
    else:
        c "Good."
        "The two of you remain silent. After awhile you fall asleep"
    scene black with fade
    pause
    scene ambush1 with fade
    play music forest
    "The two of you get up and get ready."
    show talkwancb

    c "C'mon [mc], pack up the tent already."
    show talkwanmc
    mc "Quit bossing me around."
    show talkc
    c "Pack up the tent, please? "
    hide talkc
    c "How's that?"
    mc "Ok... that sounds weird coming from you."
    "You pack up the tent."
    hide talkwanmc
    show talkmc
    mc "Done."
    hide talkmc
    c "Finally, we can get moving."
    scene ambush1 with fade
    mc "So, where are we going?"
    c "Let's go back to the bandit camp and see what we can find."
    mc "What if we run into more zombie bandits?"
    c "There's no point in fighting them, you can't kill 'em."
    c "We need to find the Lelluk. If we kill it, the \"zombie bandits\" will die with it."
    mc "Cool, so how do we kill it?"
    c "......"
    c "...I don't know."
    mc "You don't know?"
    c "It's a rare monster! I've only heard about it in stories."
    mc "Then what makes you think two recruit adventurers can kill it?!"
    c "We have to try! And don't put me in the same rank as you, wimp... How do you think I leveled up so fast?"
    mc "Uhm... by getting a bunch of stupid guys to kill boars for you?"
    c "No idiot! I've killed rank C and B monsters, while you were out playing in the woods hunting boars and birds."
    if quest1 >= 3:

        mc "...Hey, I killed a bunch of Wall Crawlers..."
        c "Those are still rank S monsters."
        mc "Fine then! You win... You're a badass, we get it."
    else:
        mc "Fine then! You're a badass, we get it."

    mc "But we need a plan."
    c "Let's just get to the camp and figure the rest out from there."
    mc "Fine."
    "The two of you make your way back to the bandit camp."
    "As you close in, you see several undead bandits are already there. A cloaked figure with strands of blue light emanating from its hands floats silently behind them."
    scene lelukbandits with fade
    c "Look like we found 'em."
    mc "Is that...?"
    c "It must be the Lelluk, I've heard that it looks like a ghost."
    mc "So, what do we do?"
    c "Hmm... There are only three bandits from the look of it. We won't stand a chance in a direct fight."
    c "If only we could sneak pass them and reach the Lelluk we might be able to take it out."
    mc "...Sneak past them?"
    mc "I got it!"
    c "Mh?"
    mc "I can use an invisibility spell."
    c "Invisibility spell? What? ...You know it?"
    mc "Yeah! Scar-  I mean Miss Scarlet taught me."
    c "Nice! That's perfect!"
    c "You use the invisibility spell to sneak past those guys and kill that damned thing."
    mc "Ok then... I hope this works."
    mc "HOLMAN!"
    c "......"
    mc "Can you see me?"
    c "No."
    mc "Good. It worked, I'm going in..."
    "You slowly sneak arround the bandits. Your stomach turns looking at them."
    mc "{i}Who knew I would actually be using this for a stealth mission?"
    "You sneak pass the three bandits."
    $ gameover = "leluk"
    label leluk:
    scene leluk with fade
    "You sneak ever closer to the Lelluk. But as you start to close in, it's head slowly turns."
    mc "Fuck, can it see me? No, it can't be."
    "The Lelluk's harsh red eyes stare right at you."
    mc "I think it can sense me or something. Shit!"
    "It starts to float towards you."
    mc "Shit, shit, shit!!"
    c "HEY, OVER HERE!"
    "Cynthia screams out. The Lelluk turns to her. With a silent gesture, it commands the bandits to attack her."
    mc "Shit! Cynthia won't be able to hold them off! It's distracted now, this is my chance."
    menu:
        "Stab its eyes":
            "You stab at its eyes."
            "But the sword passes right through."
            mc "What?!"
            "The Lelluk grabs you with its huge claws, you hear a deafening crack as it rips you in half."
            scene black with fade
            jump GameOver
        "Stab its heart":
            "You stab its heart."
            "But the sword passes right through."
            mc "What?!"
            "The Lelluk grabs you with its huge claws, you hear a deafening crack as it rips you in half."
            scene black with fade
            jump GameOver
        "Cut off its arms":
            "You slash your sword and cut off  of its arms. It lets out a loud shriek."
            "The bandits fall to the ground like dummies."
            mc "That's it!"
            "The Lelluk swings its huge clawed hand at you. You dodge it swiftly and cut off its other arm."
            "It shrieks again and careens away into the sky."
            scene forrest with dissolve
    scene forrest with fade
    show normalcg
    show talkwacb
    show smilemc
    c "We did it!"
    hide talkwacb
    show talksadhappymc
    mc "Yeah! Thanks for saving my ass back there."
    show talkwahcb
    c "No problem... I wanted some of the action too, you know?"
    mc "Hehehe..."
    show talkwanmc
    mc "But I didn't kill it, it just flew away."
    show talkwancb
    c "You cut off its arms, right?"
    mc "Yeah, I think it was controlling those bandits with the orbs in its hands."
    c "I thought so too. If it can't possess bodies, then its prety much harmless... creepy, but still harmless."
    mc "You're right."
    mc "So, it's over then?"
    hide talkwancb
    show talkwahcb
    c "Yeah... quest complete."
    c "You're not such a wimp after all."
    show talkwanmc
    show talkwamc
    mc "Hehe, I told you!"
    c "Ok then... let's go back."
    "Both of you go back to the Guild."
    show adgc1 with fade
    play music aguild
    "Cynthia tells July about what happened. She is shocked."
    j "Oh my goodness... are you guys ok?"
    mc "Yeah, we're fine."
    j "I never would have thought that a Lelluk could be so close to Randel."
    c "Yeah, I was pretty suprised too."
    j "It's a good thing you had Cynthia with you, [mc]. She might not look like it, but she's a tough nut to crack!"
    mc "......"
    c "Well... it was [mc] who slayed it."
    j "Really?! ...Wow [mc], well done."
    mc "Thanks, hehe."
    mc "{i}Why didn't she take all the credit? Is this just a part of her act?"
    j "Here's a little extra because of all the trouble you two went through."
    $ renpy.notify("{color=#fff}You gained 70 silver")
    $ money += 70
    "Cynthia and [mc]" "Thanks, July."
    scene agblr
    show normalc
    show smilemc
    show talkhappymc
    mc "So then, that's it."
    c "Yeah..."
    mc "It was fun right?"
    show talkwancb
    c "What was?"
    mc "Our adventure."
    c "It was ok."
    show talkwamc
    mc "C'mon."
    c "Fine. It was good! You happy now?"
    mc "Hehe... I'll see you later then."
    c "Ok... and [mc]... I'm sorry for being mean... I..."
    show talkmc
    mc "No, it's ok... I get it."
    show normalc
    pause
    show talkc
    c "Thanks..."
    $ sawcynth += 1
    play sound chime
    $ renpy.notify("{color=#fff}Quest completed")
    jump guild

label death:
    show qtebehead4 with vpunch
    play sound slash1
    pause
    scene black
    jump GameOver



label cynthquest3:
    hide screen hud
    scene agblr
    show smilemc
    show talkwahcb
    c "Ahh, there he is."
    show talkwanmc
    mc "Huh?"
    c "I was looking for you."
    mc "For what?"
    c "Wanna gain some EXP? I'm going monster hunting."
    show thinkmc
    mc "{i}Is she asking me to come with her?"
    hide talkwanmc
    show talkwamc
    mc "Uhh... O-Ok."
    show talknc
    c "Great! Grab your things, we're leaving now."
    show talkwanmc
    mc "N-Now... Wh-What are we hunting?"
    c "I'll explain on the way."
    mc "{i}Sigh"
    hide talkwahcb
    hide talknc with easeoutleft

    mc "{i}She really doesn't waste her time."
    c "Hurry up!"
    play music forest
    scene forest with fade
    "The two of you leave the Guild and enter the forest."
    show smilemc with easeinleft
    show smilenc with easeinleft
    mc "So, what are we supposed to be hunting?"
    show talkwanc
    c "A glob."
    mc "Ahhh... "
    show talksadhappymc
    mc "What's a glob?"
    show normalcg
    c "Ok, good."
    mc "What?"
    show talkwahcb
    c "It's nothing. Just do as I say and you'll be fine."
    show talkwanmc
    mc "Alright, thanks for the info."
    scene forrest with fade

    "The two of you go deeper into the forest."
    show normalmc with easeinleft
    show normalcg with easeinleft
    pause 0.3
    show talkwanmc
    mc "Hey, aren't we too deep into the forest?"
    show talkwacb
    c "Do you expect class B monsters to be hanging out in the outer valley?"
    mc "Wait, we're hunting a class B monster!?"
    c "Yeah. You're Bronze now, [mc]. You can't expect to level up only by killing boars and falcons."
    show angry
    mc "A heads-up would've been nice. I could've come better prepared."
    show talknc
    c "Relax, you'll be fine."
    mc "{i}Easy for you to say."
    scene forrest with fade
    "You keep walking for what it felt like an hour until Cynthia gives the signal to stop."
    show angryc
    show normalmc
    c "Ok, this place will do."
    show thinkmc
    mc "Hmm?"
    show talkwanc
    c "Give me your EXP charm."
    show talkwanmc
    mc "What?"
    c "Just give it."
    hide talkwanmc
    mc "......"
    show talkwancb
    c "It's for your own good. You can keep it if you don't want to."
    show normalcb
    c "......"
    "You hand Cynthia your EXP charm."
    show talkwanmc
    mc "Fine. Here take it."
    "Cynthia takes it. You can tell that she's half surprised that you actually gave it to her."
    mc "So, now what?"
    scene forrest
    show talkwanc
    show thinkmc
    c "We split up."
    mc "Are you serious?"
    c "Yeah, it'll be easier to track it this way. "
    c "You go that way and I'll go the other."
    show talkwanmc
    mc "B-But I d-don't even know what I'm supposed to be looking for!"
    c "You'll know when you see it."
    mc "WHAT?!"
    hide talkwanc
    show talknc
    c "Ok, we need to go now before it gets dark."
    c "If you're in trouble, just scream, ok?"
    hide talknc with easeoutright
    mc "Wh-?!"
    "Cynthia darts off and disappears into the bushes before you can ever have the chance to say anything."
    show angry
    mc "She's gone."
    hide angry
    mc "{i}sigh{/i} What am I supposed to do now?"
    scene ambush1 with fade
    "You wonder around the forest for a while. Nothing but the chirping of birds and occasional insects."
    scene forrest with fade
    show thinkmc
    mc "Nothing."
    mc "Where the hell is Cynthia?"
    show normalcgop
    c "Hello."
    show suprised
    mc "AAAAAAAAAHHHHHHH!!!"
    hide normalcgop
    show smilenc
    show angry
    mc "Oh, it's... you."
    mc "Don't do that. Ever."
    show talknc
    c "Sorry."
    hide angry
    show talkwanmc
    mc "So, did you find anything."

    c "Yes. Follow me."
    hide smilenc
    hide talknc with easeoutright
    "She runs off again."
    show angry
    mc "Wait..."
    mc "{i}This girl is driving me crazy!"
    "You run after Cynthia. You find her near an entrance of a cave."
    scene globmouth1 with fade
    show globc1 with easeinleft
    mc "Is it in here?"
    c "What?"
    mc "Huh? The glob or whatever we were hunting."
    c "......"
    show globc2
    c "[mc], the real reason I brought you here isn't for that."
    hide globc2
    mc "What the hell are you talking about?"
    c "I've been wanting to tell you something."
    mc "Eh?"
    show globc2
    c "I..."
    c "I... like you."
    mc "Ok, very funny."
    scene globmouth1
    show cynthstripglob with hpunch
    $ persistent.globCynth = True
    "Without warning cynthia pulls down her top."
    window hide
    mc "HAAAAAGGG!"
    pause
    c "I really do, [mc]!"
    mc "{i}What the fuck is going on here?"
    mc "{i}Is she playing with me?"
    mc "{i}Am I dreaming?"
    mc "......"
    mc "{i}Or is she being real? The whole glob thing did sound stupid!"
    mc "B-But this so sudden."
    "You move closer to her."
    mc "{i}Her tits are too good."
    c "You can touch them if you want."
    mc "Erm... I don't know if..."
    c "Don't worry [mc]"
    mc "{i}What the hell is happening!"
    mc "{i}I can't stop myself."
    mc "......"
    c "Don't you like them?"
    mc "Oh... Cynthia. Your tits look amazing."
    mc "......"
    mc "And your breath... smells like rotten flesh."
    mc "..."
    mc "{i}...Rotten flesh?"
    stop music
    mc "{i}...Rotten flesh? HANG ON A MINUTE!"
    hide cynthstripglob with dissolve
    "Cynthia disappears and you instantly come back to your senses."
    scene globmouth2 with dissolve
    "You fall to the ground from the shock of what you're seeing. The caves warped from rock into living flesh, turning into a giant..."
    play music battlemusic1
    scene glob1 with vpunch
    "MOUTH!"
    pause
    mc "AHHHHHHHHHHH!!! WHAT THE FUCK?!"
    "Saliva secretes from the walls. You can see bits of flesh, probably from those that have already been digested. The teeth are laid bare to show even more whatever meaty scraps are on."
    scene glob2 with hpunch
    pause 0.3
    scene glob3
    $ persistent.globDeath = True
    play sound stab
    "Suddenly, Cynthia leaps on to the monster from a tree. She stabs it in the eye. The monster screams out from that damage."
    c "[mc], run!!!"

    show animationglobchase
    show glob5
    pause
    "You get up and start running. You hear the monster rushing behind you."
    mc "{i}huff... huff... huff..."
    pause
    mc "{i}I'm not going to make it!"
    "You keep running as fast as you can. You can feel the monster's breath on your back."
    c "Jump to the side!"
    mc "WHAT!?"
    c "JUMP TO THE SIDE!"
    mc "It's right behind me! I won't make it!"
    c "You can make it!"
    c "Trust me!"
    mc "...URGH!"
    hide glob5 with easeoutleft
    "Without second thoughts, you jump to the side. The monster rushes pass you. It moves straight forward, and after some time it stops... by tripping over and skidding across the ground. It lies dead."
    stop music fadeout 0.9
    "Cynthia jumps down from the dead monster and walks towards you, hardly with any major damage on her, but still roughed up."
    scene forrest with fade
    show smilenc with easeinright
    play music forest
    "You're still on the ground covered with mud. She comes to you and offer you a hand. Grabbing her hand, you manage to stand up."
    show suprised
    hide smilenc
    show talkwacb
    c "Nice job, we did it. Here's your EXP charm back."
    c "400 EXP. Not bad, eh?"
    $ exp += 400
    call levellingUp from _call_levellingUp_5
    "You stare at her, still in shock as she hands you your EXP charm. "
    show talkwanc
    c "What?"
    show angry
    mc "Wh-What?!"
    mc "I was almost monster food!"
    show talknc
    c "But I saved you."
    mc "{i}I was mere seconds from being eaten! How is she so calm about this?"
    "You wipe the mud off of you."
    mc "H-How did you even find me?"
    c "I... followed you."
    mc "What do you mean?"
    c "Globs trick prey into coming into their mouth because they're too slow to like, actually move and catch prey. They use a kind of illusionary magic that tricks them into thinking they're food... or someone to fornicate."
    hide talknc
    show smilenc
    mc "......"
    show smilenc
    show suprised
    pause 0.3
    hide suprised
    mc "YOU USED ME AS BAIT?!"
    show talknc
    c "Uhm... yes."
    hide talknc
    mc "Oh my god! I could've died!"
    show talknc
    c "Relax, I wouldn't let that happen."
    hide talknc
    show normalcb
    "You look at her still mad with anger."
    show talkwancb
    c "You think I would let someone die just because I could get some EXP? What kind of person do you think I am?"
    mc "A crazy person!"
    c "Ok, I'm sorry, alright?"
    c "I didn't tell you about this is because I knew you wouldn't do it."
    c "Finding these things are impossible. Believe me, I've tried."
    mc "......"
    show sadc
    pause 0.5
    hide sadc
    show talknc
    c "You have to understand that this was an EXP gold mine. This will take us, like, up to 3 levels."
    c "It would've taken you years to get this much EXP by killing boars."
    c "I did this for the both of us."
    show thinkmc
    mc "{i}As crazy as she is, at least she's trying really hard to apologize. I did get a lot of EXP after all, she could've had it all for herself."
    mc "{i}sigh"
    mc "Fine, whatever."
    hide talknc
    show talkwahcb
    c "There, that's it. I'll buy you some candy on our way home. Ok, little baby?"
    show talkwanmc
    mc "Agh, shut up..."
    mc "Are you sure that thing is even dead?"
    show talknc
    c "Yeah. We wouldn't get the EXP if it wasn't."
    mc "Oh yeah."
    scene forrest with fade
    "The two of you start you're journey back to Randel."
    scene ambush1 with fade
    show talknc
    show thinkmc
    c "Don't worry, next time I'll tell you if you're bait, beforehand."
    mc "\"Next time\", you say?"
    c "Well, I thought we could do this again."
    mc "And what made you think I would do this again after what just happened?"
    show talkwacb
    c "Well, first of all, I thought you weren't such a pussy."
    c "And then there's all the free EXP you can get. And most importantly, you get to spend time with me."
    show talkwanmc
    show smilenc
    mc "Heh, you're really trying your hardest to be unlikable."
    hide smilenc
    c "So, are you up for it?"
    hide talknc
    show normalcg
    mc "Ugh..."
    mc "{i}I definitely don't want to. But something about her makes me want to spend more time with her."
    mc "Alright."
    show smirkc
    c "Yes! I knew you wouldn't turn down the offer!"
    hide smirk
    show talknc
    c "But you'll need to train a bit."
    mc "Why?"
    c "The way you ran earlier. If that wasn't a glob chasing you, you would've been eaten."
    c "I don't know about your sword and bow skills, but your agility needs some work."
    mc "So, you want me to be better at running away from monsters?"
    c "That's important too, you know."
    mc "For you, that would make me better bait."
    show smirkc
    c "Exactly."
    mc "You're really not trying to hide it anymore, are you."
    hide smirkc
    c "I said I'll be completely honest."
    mc "So how am I supposed to train?"
    c "Come talk to me at the Guild in the evening."
    mc "Huh?"
    c "I'll train you."
    mc "{i}Did not expect that."
    mc "Ah..."
    mc "Ok."
    c "Good."
    scene forrest with fade
    "You reach Randel."
    scene villageback with fade
    show smilenc
    show normalmc
    c "Ok, remember to come in the evening."
    show thinkmc
    mc "Alright."
    c "Bye, then."
    hide smilenc with easeoutleft
    mc "B-Bye."
    show normalcg with easeinleft
    c "Oh, and [mc], what the glob showed you back there. You better erase it from your mind."
    show suprised
    hide normalcg with easeoutleft
    mc "{i}She heard me."
    scene homeday with fade
    "You go home tired."
    mc "{i}What a day."
    mc "{i}Cynthia's method of using me as bait was uncalled for. But it could have been worse. And heck, I survived worse things up till now."
    mc "{i}She really wants me to train so I can be more effective in battle, huh? Suppose I could. That way I can train hard and not let her take advantage of me again like last time."
    mc "{i}Still, could be a good way to get closer to her. I'm making some progress making her open up. Maybe I could get further with her? Only time will tell."
    $ cynthquest3 += 1
    jump home


label cynthFirstDate:
hide screen hud
scene agblr
"You see Cynthia enter the Guild. She seems to be carrying a large box with her as she struggles."
show talkwamc
show normalcb
mc "Hey."

c "Ahh... H-Hey [mc]."
$ cynthquest2 += 1
mc "What are you doing."
c "...I'm carrying this box?"
mc "Where to?"
show talkwancb
c "Urgh... do you always put your nose into other people business like this."
show talkwanmc
mc "I was only asking. Sheesh, I thought I'd give you a hand."
show sadc
c "......"
show talksc
c "{i}Sigh{/i} I'm sorry... [mc]."
c "I'm taking these to my room at the Guild Quarters."

mc "You got promoted to a Bronze?"
c "Y-Yeah. Can we talk at my room? This thing is pretty heavy."
mc "Oh, ok... are there any more boxes?"
c "...Th-There's  more outside."
mc "Wait, I'll bring it."
hide talksc
hide sadc
c "Wh-What? ...You don't need to."
mc "It's no big deal, really."
show sadc
c "O-Ok, then."
scene agblr with fade
"You go outside and pick up Cynthia's box. The large wooden box, you thought, would be a piece of cake. But looks betrayed you as you find out how much it weighs."
mc "Got it... Ack."
scene agblr with fade
show talkwamc
show smilenc
mc "These things are pretty heavy."
show talknc
c "Yeah. That's the last of my stuff. I crammed them all into these two boxes"
scene adventurersguild_day with fade
"The two of you start to walk to the guild quarters."
c "Oh... I heard you got promoted too."
c "Congrats, sorry I missed the party. I was a bit busy."
mc "Ahh, don't worry."
mc "And congratulations to you too."
c "Thanks."
mc "Wait, when did you get promoted?"
c "Today."
mc "Really? but didn't you have a party or did I miss it."

c "Nah, I didn't. Looks like I'm not as popular as you in the Guild, as surprising as it may sound."
mc "Seriously?"
c "Hehe, yeah."
mc "Hmmm, that's hard to believe."
c "Don't you see anything different about me here?"
mc "Uhm... no."
c "I'm not acting like Miss Prefect."
mc "Oh... yeah, I forgot all about that persona."
mc "But, why? Are the men here too tough to woo?"

c "Huh! No!"
c "I just need to be myself somewhere. If keep pretending to be that princess every time, I think I would go crazy."
mc "Hm..."
mc "To be honest, I thought you'd get promoted sooner."

c "Yeah. I really was busy with some other stuff. I didn't have time for Guild work."
menu:
    "Ask what she was busy with":
        mc "What were you busy with."
        c "Ugh... just some stuff. Man, [mc], you really need to give people space, seriously."
        mc "Alright, alright, sorry."
    "Don't ask her":
        mc "{i}She really doesn't like people meddling with her business. Privacy and all that."
        mc "{i}I should probably leave it as that."
"The two of you go to Cynthia's room. "
stop music fadeout 0.3
scene cynthiaroom with fade
"The room is mostly empty, mainly because Cynthia just moved in. There's nothing else except a desk, a dresser and a cupboard to store books."
"You put down the box."
show talksadhappymc
show normalcb
mc "Whoah, nice place."
show talknc
c "...Thanks."
mc "How come I'm the only  who doesn't have a room?"
c "You don't?"
mc "They said it's still in renovation."
show talkwahcb
c "Well, it might be another way of saying we don't want you here."
mc "Yeah, very funny."
c "Alright, thanks for the help then, [mc]."
mc "Glad to help. That's everything right?"
c "Yup."
c "Wait, let me see."
hide normalcb
hide talknc
hide talkwahcb with easeoutleft
"Cynthia looks around the room to see if she's got everything."
"She then checks her pockets and her satchel."
c "Fuck!"
show talkwanmc
mc "What?"
show thinkmc
c "My knives! I thought I brought them."
"She starts to look around her room."
c "Did I bring them earlier."
hide thinkmc
mc "Should I help you check"
"Cynthia's too busy searching she doesn't hear you."
mc "I guess I'll help."
scene cynthiaroom with fade
"You start to look around."

"You open a few drawers but find nothing."
"You open  of the boxes you just brought, hoping she would find her knives. To your disappointment, it's filled with different kinds of jewels and chocolate. Gifts from her \"lovers\"."
"You went over to the big cupboard to look until you come across some jars neatly stacked together. "
"It takes a few seconds for you to process what you're just seeing..."
scene ears
pause 0.9
scene ears with vpunch
$ persistent.ears = True
"{b}IT'S A JAR FULL OF HUMAN EARS.{/b}"
mc "What the hell is this?!"
c "Oh, great. You just can't keep to yourself, can you?"
scene cynthiaroom
show angry
show normalcb
mc "Why are there glasses full of human ears in your cupboard?!"
c "{i}sigh"
hide normalcb
show talkwancb
c "They're bandit ears."
show talkwanmc
mc "B-Bandit ears?!"
c "Yes, [mc], bandit ears."
mc "Uhh, O-Ok."
mc "Why?"
c "You get paid for these."
mc "What?"
c "Yeah, if you give them to the barracks, you get paid."
mc "Then why the hell are you keep them stored in your cupboard?"
c "Well..."
c "First, I thought of handing them over to the barracks, but..."
c "I couldn't convince myself to give them away."
show talknc
c "I kinda like looking at them."
mc "WHAT?!"
show talkwacb
c "Helps me to keep count of how many I've killed."
mc "{i}This girl is messed up. Better not to push this anymore or I'll end up in  of those jars."
mc "{i}Gulp{/i} I leave it at there then."
show talkwahcb
c "Yeah... I think that would be better."
mc "So... Umm... did you find your knives?"
hide talkwacb
hide talknc
hide talkwahcb
show talkwancb
c "No. It looks like I left them at my old house."
c "I'm going to get them."
mc "I'll come with you."
hide talkwancb
show normalcb
"Cynthia looks at you. You can tell that she's trying her hardest not to say something mean."
show sadc
pause 0.5
show talkwancb

c "...Fine."
c "You sure do have a lot of free time."
scene villageback with fade
play music forest
"The two of you head out of the Guild. You pass the market and go to a really shady part of town."
play music cynthtown
scene cynthtown with fade
" You've lived here since you were a child but you've never been here."

show talkwancb
show thinkmc
c "Ok, we're here."
show talkwanmc
mc "You lived in a place like this before?"

c "Yeah, it's the cheapest place I could find."
show talknc
c "And it reminds me of home. Makes it easier to settle in."
mc "O-Ok."
hide talknc
c "No  needs to know, got it?"
mc "Yeah, yeah."
hide talkwancb with easeoutleft
"Cynthia goes into a small house built out of black wood. It almost looks like a shack, most of the wood have rotted while the ceiling had been patched up with more wood. It had seen better days."
"After a couple of minutes, Cynthia comes out."
show normalcg with easeinleft
mc "Found them?"
c "Yup."
mc "Back to the Guild then?"
c "Ye-"
show shockc
play sound stomach
"{i}grumble"
"You hear Cynthia stomach rumble."
"Her face turns bright red."
show talkwamc
mc "You're hungry, right?"
show talkwancb
c "No!"
show normalcb
c "......"
play sound stomach
c "{i}stomach grumbles"
hide normalcb
c "Ok, a little, yeah."
mc "Why don't we grab something to eat on our way back?"
c "I didn't bring any money."
mc "Come on, it'll be my treat."
mc "Think of it as a way of celebrating your promotion."
"Cynthia eyes at you suspiciously."
c "Fine."
mc "Nice. Any suggestions."
c "Wh-Why are you asking me?"
show normalcb
mc "Well, it's your treat. And I don't eat out that often, so I don't really know where to go."
"Again, her stern eyes fix on you. She analyses you, maybe trying to find whether you have an ulterior motive."
"Then she gives up and answer shyly."
hide normalcb
c "There's a small cafe close by."
mc "Great, lead the way."
"You follow Cynthia."
play music home
scene cafe with fade
"You finally come to a small cafe, another place you haven't been before. The street looks more well organized and livelier than the  you were at previously."
stop music fadeout 0.9
"You go inside and get seated."
window hide
scene cynthiadate2
play music happy
mc "It's a really nice place. I've never been here before."
scene cynthiadate1
c "It's pretty new actually. It opened just a few days before I arrived."
mc "Hmmm... when did you come to Randel... if you don't mind me asking?"
scene cynthiadate2
c "......"
c "It's been... like a month."
mc "You lived there for a month? Man, that must've been horrible."
c "What choice did I have? I was short on silver."
"A waitress comes to your table. She's dressed in a very strange outfit, something very different to a tavern wench."
"Waitress" "What will y'all be having?"
scene cynthiadate1
c "Cream cake and a coffee for me."
"Waitress" "And you, sir?"
mc "Uhm... A steak and some ale."
scene cynthiadate2
"Waitress" "Um..."
"Waitress" "I'm sorry sir but we don't serve steak... or ale."
mc "Uhh... th-then... some chic-"
scene cynthiadate1
c "He'll have the same as me."
"Waitress" "O-Ok... two cream cakes and two coffees."
c "Yes."
"Waitress" "Alright, you order will be served soon."
"The waitress leaves."
scene cynthiadate3
c "The hell, [mc]? Haven't you ever been to a cafe before?"
mc "Uhm, no."
c "{i}sigh{/i} What did I expect from a farmer's village?"
mc "So... they don't have ale or meat?"
c "No... do you see drunks dancing around in here? This isn't a tavern!"
"You take a good look around again. She's right, the atmosphere is the total opposite of that of a Tavern."
"It's... peaceful and cozy. No brawls or anything messy lying on the floor. People show proper etiquette having their meals."
mc "Hmm... Yeah, this IS different."
mc "What can you eat here?"
c "Cake, sweets, pastries, you can drink coffee as well."
scene cynthiadate2
mc "Whoa. Man, I never knew a place like this existed."
mc "Thanks."
scene cynthiadate3
c "For what?"
mc "For bringing me here."
scene cynthiadate2
c "Oh... Uh, no problem."
c "But remember, you're still paying."
mc "Ah, yeah, almost forgot."
scene cynthiadate4
"A slight smile lights up Cynthia's face."
mc "......"
mc "So... you've gone to a lot of cafes?"
c "Yeah... more than you can count."
mc "Really?"
c "It's the place most people normally go for dates... in other towns."
mc "Oh... dates, yeah."
mc "How many towns have you been to?"
c "A lot."
mc "Whoa, so you've been traveling from town to town."
c "Yup. Ever since I left Karnak, I've been on the road."

mc "That must've been fun. I mean travelling all around Astylla."
c "...Yeah... it kinda was."
mc "So you must have a lot of stories to tell, of you adventures."
c "Whoah, buster. I think I've shared more than I'm comfortable with."
mc "Urgh.. fine. At least I got this much out of you."
c "Yes."
mc "But man, you're a natural adventurer. No wonder why you're so good at what you do."
c "Heheh. I guess you're right."
"The waitress brings you your food."
show cynthiadate5 with easeinright
pause
"Waitress" "Enjoy."

"You take a bite from the piece of cake."

pause
"It's sweet, soft, and like the best cake you've ever eaten."
mc "This is... Mmmh, this is good!"
c "Oh,... I thought you wouldn't like it."
mc "Are you kidding me? It's the best cake I've ever had."
c "That good? Ok."

show cynthiadate6 with dissolve
"The two of you start to eat. You can't restrain yourself as you gobble up the cake like a hound."
pause
"Cynthia cuts a piece of the cake with a knife and eats it with a fork."
"You stare at her elegant handling while you had cream all over your face and hands."
mc "A-Ah... that's how you're supposed to eat it."
scene cynthiadate2
pause
scene cynthiadate1

"She bursts out laughing."
c "Hahaha... yeah."
"She hands you a piece of paper cloth that was placed at the table."
c "Here, wipe you're mouth with this."
mc "Th-Thanks."
"You wipe up your mouth, making sure your face is clean."
scene cynthiadate4
show cynthiadate5
c "Hehehe. Why didn't I date someone dumb like you? It's so much more fun."
mc "I couldn't help myself, ok?"
c "Hehehe."
mc "{i}She does genuinely look happy. Not like the fake smile she has in the Academy."
c "Imagine if some guy from the Academy sees us."
mc "Oh, yeah. I'll be on the hitlist of every guy at the Academy."
c "Hehehe. Yeah."
"The two of you finish your drinks."
mc "I think I'll be coming here a lot."
c "And it's all thanks to me."
mc "Yes. I'm eternally grateful."
"The waitress comes to your table."
"Waitress" "Did you guys enjoy the meal?"
mc "Yeah."
"Waitress" "We're so glad."
"Waitress" "That will be 30 silver."
mc "{i}Did she say thirty? Or was it thirteen?"
mc "Uhh, right, thirty...."
$ persistent.cynthiaFirstDate = True
if money > 30:
    "You give the money."
    $ money -= 30
    $ paycynth = True
    "Waitress" "Thank you. Please do come again."
    "The two of you leave the cafe."
    scene villageback with fade
    show talkwanmc
    show smilenc
    mc "I didn't know I was paying for a feast."
    show talkwahcb
    c "Hehehe, yeah. It's pretty expensive, hence why I go there for dates."
    mc "You're very resourceful."
    c "Yes, I am."
    show talknc
    c "Thanks for the treat, [mc]."
    show talksadhappymc
    mc "No problem."
    mc "I guess I'll have to take back what I said earlier. I won't be coming here any time soon."
    c "To the Guild then?"
    menu:
        "Go home":
            mc "I'll be going home."
            c "Oh, ok."
            c "......"
            c "Bye, then."


            mc "Bye."
            scene villageback with fade
            show thinkmc
            mc "{i}I'm slowly getting to know the real Cynthia. She doesn't seem that bad. Beneath that cold appearance, she turns out to be pretty nice."

            $ time += 1
            jump home
        "Go to the Guild":
            mc "Ok"
            "The two of you go to the Guild."
            scene agblr with fade
            show smilenc
            show smilemc
            c "That took longer than expected."
            mc "It did."
            c "......"
            c "Alright, see you later. I have to unpack my stuff."
            mc "Bye."
            hide smilenc with easeoutleft
            mc "{i}I'm slowly getting to know the real Cynthia. She doesn't seem that bad. Beneath that cold appearance, she turns out to be pretty nice."
            $ time += 1
            jump guild
$ paycynth = False
mc "{i}Shit all I have is [money]!"
scene cynthiadate2
"Cynthia notices you panicking and had to react, pulling out her satchel to draw out money."
$ paycynth = False
c "Uhh, put it on my tab."
"Waitress" "Alright. Please do come again."
"The two of you leave the cafe."
scene villageback with fade
show talkwancb
c "Thanks for the treat, [mc]."
show worriedmc
mc "Sorry, Cynthia, I'll pay you back."
c "You better."
mc "I didn't know I was paying for a feast."
show talkwahcb
c "Hehehe, yeah. It's pretty expensive hence why I go there for dates."
show talksadhappymc
mc "You're very resourceful."
c "Yes, I am."
show smilenc
c "To the Guild then."
menu:
    "Go home":
        mc "I'll be going home."
        c "Oh, ok."
        c "Bye, then."
        mc "Sorry again for earlier."
        c "Ahh, it's no problem. You paying back anyway."
        mc "I'll be sure to."
        c "..."
        c "Alright, see you later."
        mc "Bye."
        scene villageback with fade
        show thinkmc
        mc "{i}I'm slowly getting to know the real Cynthia. She doesn't seem that bad. Beneath that cold appearance, she turns out to be pretty nice."
        $ time += 1
        jump home
    "Go to the Guild":
        mc "Ok."
        "The two of you go to the Guild."
        scene agblr with fade
        show worriedmc
        show smilenc
        mc "Sorry again for earlier."
        show talkwahcb
        c "Ahh, it's no problem. You paying back anyway."
        show talksadhappymc
        mc "I'll be sure to."
        c "......"
        c "Alright, see you later. I have to unpack my stuff."
        mc "Bye."
        hide talkwahcb
        hide smilenc with easeoutleft
        mc "{i}I'm getting to know the real Cynthia. She doesn't seem that bad. Beneath that cold appearance, she turns out to be pretty nice."
        $ time += 1
        jump guild



label cynthquest4:
    show talkwamc
    mc "I'm ready to go for our monster hunt."
    c "Great. Get your camping gear, we might have to spend the night."
    mc "Oh, ok. Yeah, I have them with me."
    c "Alright. "
    c "Give me your map."
    "You hand it to her."
    "She marks a point on your map."
    show talkwanc
    c "This is the area it's been spotted. It'll probably be around here."
    mc "Ok..."
    mc "But aren't wolves normally in packs? Are we going to hunt them all?"
    c "Oh, no. That would be suicide."
    c "This  has been spotted alone. Most likely it's a lone wolf."
    if chartrait == 1 or readwolf == 1:
        mc "Ah... It's been kicked out the pack."
        hide talkwanc
        c "Correct."
        mc "That'll make things easier."
        c "Yeah."
        c "Let's get going then."
        mc "Ok."
    else:
        mc "Which means?"
        c "It means it's been kicked out of the pack."
        show talkwancb
        c "Come on, [mc]. Didn't you read the Book of Monsters?"
        show talksadhappymc
        mc "Ehhh, I forgot."
        c "Ugh... nevermind."
        c "Let's go."
    scene agblr with fade
    "While you are about to exit the Guild, you spot Sander."
    show normalcbop
    show smilemc
    show talkns with easeinleft
    sa "Hey, [mc]."
    mc "Hey."
    sa "And who's this fine lady you're with?"
    hide smilemc
    show talksadhappymc
    mc "Uhm... This is Cynthia."
    c "Hello."
    sa "Hello, I haven't seen you around the Guild much. Are you new?"
    show talkncop
    show smilemc
    c "A bit. Yeah. I don't come to the Guild that often."
    show talkwas
    sa "Oh, I see. Where are you two heading to?"
    mc "We're going to hunt a direwolf."
    sa "Ahh, you guys are looking for a better now, are ya? Be careful though, those things are no joke."
    c "Yeah, we know."
    sa "......"
    sa "Alright then, good luck."
    mc "Thanks."
    sa "I hope you don't dump our party, [mc]."
    mc "What- Of course not, this is just temporary!"
    show talkwaecs
    sa "Hehe I'm just messing with ya, kid."
    scene agblr
    show normalcbop
    show smilemc
    show angrytalke with easeinleft
    show talksr
    e "Sander, there you are. I was wondering where you disappeared to."
    sa "I was just talking to [mc]."
    e "Come on, I'm late for a delivery quest! Let's get this done quick."
    show talkhe
    e " Hey, [mc]."
    show talkwamc
    mc "Hi, what are you two doing?"
    sa "I'm getting a haircut."
    mc "From where?"
    show sadhtalke
    e "From me."
    sa "She's the best barber in town, but don't tell anyone. I like to keep her to myself."
    mc "But your hair... looks fine."
    sa "Fine! Look here."
    hide talksr
    show serioussright
    "Sander turns around and shows the back of his head."
    show talkwanmc
    mc "What am I supposed to be looking?"
    sa "I've got white hair."
    "You take a look and spot two strands of white hair."
    mc "Ahh... there it is."
    sa "I told you."
    hide serioussright
    show talksr
    hide talkwanmc
    show talkwae
    e "Ok now, come on, I'm late."
    e "Bye, [mc]... Oh, I didn't see you there... uh..."
    c "Cynthia."
    e "Oh, yes, sorry. Goodbye, you two."
    sa "Good luck, guys."
    scene agblr with fade
    "Eve grabs Sander and the two of them head towards the Guild Quarters."
    c "Glad that's finally over. Can we go now?"
    mc "Yeah, ok."
    mc "You definitely act differently in the Guild."
    c "I told you, this is the place where I can be myself."
    mc "Hmmm."
    mc "But you're nice to July."
    c "......"
    c "Of course I am. She's a good person."
    c "You think I'd just be mean to everybody for no reason?"
    mc "Uhm, yes...?"
    c "{i}sigh{/i} Come on, let's go."
    scene forest with fade
    play music forest
    "The two of you leave the Guild and enter the forest. Takes a few hours to travel deeper into the forest where it's denser."
    scene forrest with fade
    show talkwamc
    show smilenc
    mc "Make sure not to lose your camping gear this time."
    show talkwacb
    c "You'd like that, wouldn't you?"
    mc "Hehe."
    c "Don't worry, we won't be having any surprises this time. I hope."
    mc "Hm."
    scene forest with fade
    "The two of you keep walking."
    show talkwanmc
    show normalcb
    mc "How are we going to find it?"
    show talkwanc
    c "We'll have to track it, of course."
    mc "And I'm thinking you can do that."
    show talknc
    c "You thought that right!"
    c "Look."
    "She points to a carcass ahead."
    c "This is perfect."
    hide normalcb
    hide talkwanc
    hide talknc with easeoutright
    "She heads to the carcass. You follow her."
    scene forrest with fade
    show thinkmc with easeinright
    show normalcg with easeinright
    pause 0.4
    hide normalcg
    "She inspects it. You can tell she had experience over examining dead bodies and the cause of it."
    show normalcb
    c "It's fresh. Might be a couple of hours."
    hide normalcb with easeoutleft
    "She looks around the carcass. Inspecting it more, she walks around slowly."
    mc "What are you doing?"
    "She doesn't answer you. She's too focused on what she's doing."


    c "Found them."
    scene forrest
    show talkwanmc
    mc "What?"
    c "The tracks."
    hide talkwanmc with easeoutleft
    "You go and take a look. You see nothing."
    scene forest with fade
    mc "I don't see anything."
    c "You're blocking out the light, come here."
    "You move closer to Cynthia. She ushers you to lean in."
    c "Now look."
    "You look again. But this time, you see a shadow of a small dent in the ground. Still, you can't tell what it is."
    c "It has soft edges, so it's not a hoof. It has to be a paw print."
    mc "All I see is a small dent. Aren't the paw prints supposed to be like this?"
    "You draw what you think looks like a paw on the ground."
    c "Well, yeah. That's what you see in the books, but you don't find prints that perfect in the wild."
    mc "Oh... right."
    c "It's not a bad trail. It goes through those bushes."
    "She points to some bushes."
    c "Follow me. Make sure you don't step on the tracks."
    mc "But I can't see them."
    c "Just follow what I'm doing and step wherever I'm stepping... And I mean watch where I step."
    mc "Ok."
    "Cynthia crouches and starts moving, looking at the ground, then ahead of her. You follow her carefully as she leads you."
    "You go past the bushes and head deeper into the forest."
    mc "Is it close?"
    c "Must be. Keep quiet now."
    "You slowly walk throughout the forest. The anticipation of trekking must have felt like hours."
    "Finally, you hear something. You get the feeling something's moving ahead of you."
    "Cynthia puts a finger on her lips, signaling you to keep quiet."
    "The two of you move forward and peer out from the bushes."
    scene direwolf1 with fade
    "And there it is, the direwolf. Almost like it was waiting for you."
    "It could have been a bigger dog, you thought. It's much bigger than you expected."
    "You stare at its shape for a brief moment until Cynthia whispers."
    mc "It's much bigger than I expected."
    c "Yeah, it is."
    mc "So what's the plan?"
    c "......"
    "Cynthia looks around analyzing the surrounding."
    scene forrest
    show talkwanc
    show thinkmc
    c "Ok."
    c "We won't be able to take it on directly. It's too dangerous."
    c "We'll have to ambush it."
    mc "Alright."
    c "Here's how we'll do it. I'll climb up to that tree back there."
    "She directs you to a tree just right behind you."
    mc "Ok."
    c "You have to get its attention and lead it pass the tree. Once it's near, that will be the signal for me to go pounce on it. "
    show angry

    mc "SO I'M BAIT AGAIN?!"
    show talkwancb
    c "SH!"

    mc "So all that training was for this?"
    c "Well, kind of. I told you, didn't I?"
    mc "Why can't you be the bait?"
    c "What? That's crazy."

    mc "I'll be on the tree and you lead the wolf to me."
    c "No."
    mc "Why?"
    show angryc
    c "I just can't, ok?!"
    show normalcb
    mc "Tell me why then!"
    hide normalcb
    c "I can't trust you to do it!"
    mc "......"
    mc "And I'm supposed to trust someone who doesn't trust me."
    show sadc
    c "I-I..."
    label baiting:
    $ gameover = "baiting"
    scene forrest
    menu:
        "Don't be bait":
            show sadc
            show angry
            mc "I can't be bait."
            mc "You either trust me or we don't do this."
            show angryc
            c "{i}...sigh..."
            c "Whatever. Climb onto the damn tree then if you want to."
            c "I'll lead it to you. You better be ready to jump on it."
            mc "I will."
            c "......"
            c "Ok, then, go."
            scene forrest with fade
            "You head to the tree Cynthia pointed out to."
            mc "{i}Who does she think she is? Using me as bait every time."
            mc "{i}I'm not that weak, I can do something."
            "You reach the tree. It's bigger up close."
            "You scan it to the top."
            mc "{i}Gulp"
            mc "{i}I-It's huge."
            mc "{i}Can I even climb it. I was never good at climbing trees."
            mc "{i}I have to try!"
            "You grab the closest branch and start to climb. You see Cynthia watching you as you climb."
            "You carefully keep you're footing and climb higher... and higher... and higher."
            mc "{i}Alright, I'm doing it."
            mc "{i}Just a little m-"
            "SNAP"
            "The branch you were holding snaps. You lose your footing and your body is pulled downwards. You try to get hold of anything, but you grab only air."
            "Just before you could scream, everything goes black."
            scene black with hpunch
            jump GameOver
        "Be the bait":
            show sadc
            show angry
            mc "Alright, whatever."
            mc "I'll be the bait."
            c "...O-Ok."
            c "...Give me your EXP charm."
            mc "Why?"
            show talksc
            c "Because I'm the  who's going to kill it."
            c "The EXP charm only gains EXP if the person who holds it kills a monster. You may get EXP killing  by yourself, but the charm gains extra for you and stores it."
            show talkwancb
            c "Unless you don't want any EXP, I suggest it would be better if you gave it to me."
            mc "Fine, take it."
            "You give Cynthia your EXP charm."
            hide talkwancb
            hide talksc
            hide sadc with easeoutright
            "She leaves without saying another word."
            show thinkmc
            mc "{i}Alright, [mc]. Time to do this. Forget about her plans of using me as a tool, again."
            mc "Ugh"
            scene direwolf1 with fade
            "You slowly move towards the wolf."
            mc "{i}This thing is huge. It's more like a bear."
            "You draw your sword and shout."
            play music battlemusic1
            scene direwolf
            mc "Hey there, doggie!"
            mc "COME AND GET IT!"
            "The wolf growls, and without warning, it rushes towards you."
            mc "FUUUUUCK!!!"
            scene forrest
            show glob5 with easeinright
            "You turn around and make a beeline towards the tree. The wolf gnarls behind you with murderous intent of mauling you with its teeth and claws."
            mc "{i}That's the tree right there."
            "You pass by the tree."
            hide glob5 with easeoutleft
            "Cynthia jumps from the tree, onto the wolf, pining it to the ground and stabbing it with her knives thrusted onto the wolf's torso where its heart is."
            play sound stab
            scene forrest with hpunch
            "Collapsing, you manage to catch your breath."
            mc "{i}huff... huff..."
            play sound stab
            pause 0.5
            play sound stab
            pause 0.5
            play sound stab
            "You hear more stabbing behind you."
            "You turn around and see Cynthia stabbing the wolf down on the ground for good measure... The wolf is truly dead."
            stop music fadeout 0.8
            mc "...We did it?"
            c "Y-Yeah..."
            c "Good job."
            $ persistent.direWolf = True
            "Cynthia takes her knife and starts to make cuts on the wolf. "
            mc "{i}I think she's skinning it."
            if chartrait == 2:
                "You nonchalantly watch as she cuts deep into the wolf's skin, separating it from the fleshy meat with ease."
            else:
                "You're unable to keep watching as she cuts the wolf's skin apart from its meaty flesh. It's more gruesome than you expected."
                "You look away, not thinking about wanting to throw up."
                c "It needs some time getting used to."
                mc "Yeah..."
            "After she finishes skinning, Cynthia warps up the pelt and carries it under her arm."
            scene forrest with fade
            show normalcg
            show thinkmc
            c "Done."
            show angry
            mc "Great."
            show talksc
            c "Here's your EXP charm back."
            "She hands you back the EXP charm and you take it."
            $ exp += 100
            call levellingUp from _call_levellingUp_6
            show talkwanmc
            mc "Thanks."
            c "It's getting dark. We better make camp soon."
            mc "Where? Here?"
            show talkwanc
            c "Not here. We'll move out from here a bit more. We get out of the deep forest as much as we can."
            mc "Ok."
            "Cynthia puts the pelt into a bag. The two of you start to move."
            scene ambush1 with fade
            "The two of you a silent after that incident earlier. You were still thinking about that argument you had with her."
            play music night
            scene ambushn with dissolve
            c "Here will do."
            scene forrestn with fade
            "You then unpack your camping gear."
            show talkwanc
            show thinkmc
            c "I'll find some wood to set up for a fire."
            c "Can you make the tents while I'm gone?"
            show talkwanmc
            mc "Y-Yeah, sure."
            hide talkwanc with easeoutleft
            "Cynthia leaves."
            scene forrestn with fade
            "You then begin to pitch up both yours and Cynthia's tents."
            show smilemc
            "Cynthia arrives after a while, carrying a bunch of wood."
            show smilenc with easeinleft
            c "Ah, good, you've pitched them up."
            c "Took longer than I thought to find these."
            "She piles them up. She takes a match box and strikes a match. She lights the pile of wood on fire."
            "The two of you sit beside the bonfire."
            play sound campfire
            scene cynthiatalk3 with fade
            pause
            "And there's an uncomfortable silence."
            mc "{i}Why is she so quiet all of a sudden?"
            c "[mc]?"
            mc "Mh?"
            scene cynthiatalk2
            c "I just wanted to say that I'm sorry ok. About earlier."
            c "I didn't mean it."
            mc "I would be lying if I said it didn't hurt my feelings."
            c "{i}sigh{/i} I know."
            mc "It's ok."
            scene cynthiatalk3
            c "I just don't know what's wrong with me."
            c "I thought after spending all this time with you, it would be different. But I still couldn't get myself to trust you."
            mc "......"
            mc "Cynthia..."
            mc "Why did you start spending so much time with me?"
            show cynthiatalk6
            c "...Mh?"
            mc "I just find it weird that you started to spend so much time with me, like, from out of nowhere."
            mc "You brought me on your monster hunts, you could've picked anyone else from the guild."
            mc "And after that you trained me, you didn't have to do that."
            c "......"
            scene cynthiatalk4
            c "Well, I don't know. I kinda liked it, spending time with you."
            c "I really can't think of an exact reason."
            c "I mean, thinking logically, there's nothing I could benefit from you."
            c "You're not rich, you aren't that strong, and you aren't that good looking. You're no good to me at all."
            mc "{i}An arrow to the heart."
            c "But there was still something about you. I felt comfortable around you, like I could say anything to you and be my self..."
            c "......"
            c "You felt like a real person. And when I was spending time with you I felt like I was {p} really living with someone else rather than by myself."
            c "I never expected you to show up for training but you came."
            c "You still wanted to hang out with me."
            c "You knew who I really was, but you were still nice to me. You trusted me multiple times even though I was a bitch to you."
            mc "Well, that's what friends do, I guess. They put up with each other's bullshit and stick together."
            scene cynthiatalk1
            c "You thought of me as a friend?"
            mc "Uhm... yeah."
            mc "Didn't you?"
            scene cynthiatalk4
            c "I've had a lot of \"friends\", but as far as real friends go... If I had  the only person I could think of, it would be you."
            mc "{i}Guess I'm friendzoned now."
            if gabetrip >= 1:
                mc "{i}...AGAIN!"
            mc "{i}Ngh... Don't lose hope yet, [mc]."
            mc "......"
            mc "I think that's the nicest thing you've ever said."
            show cynthiatalk5
            c "Yeah, make sure you write it down somewhere."
            mc "I will."
            mc "Oh, and thanks for all the compliments earlier. I'm not rich, strong or good looking, that'll really help to boost my confidence."
            c "What? I was just saying..."
            scene cynthiatalk4
            c "Ok, you're not bad looking either. Does that make you happy?"
            mc "Compliments aren't really your thing."
            c "Nope."
            mc "I'll take what I get, I guess."
            c "Hehe, yeah."
            scene cynthiatalk1
            c "You are a really nice person, [mc]. I mean it."
            mc "Th-Thanks."
            if paycynth == False:
                c "But you're not really good at paying back debts."
                mc "Huh?"
                c "Remember? That day at the cafe. You still owe me 30 silver asshole."
                mc "Ah shit, I forgot."
                c "Hehe it's alright."
                c "......"
            show cynthiatalk6
            c "What you said earlier. That I had to trust someone, and they trust back..."
            c "I think you're right."
            mc "Of course I am."
            c "And I thought if we're friends, now I have to trust you."
            c "So from here on out, I promise I'll trust you."
            mc "And I will to."
            c "Let's shake on it."
            mc "Why not a pinky swear?"
            show cynthiatalk5
            c "Pfft, what? Are you, like, five?"
            mc "I thought it would be cute."
            c "......"
            c "{i}sigh{/i} Fine, you little baby."
            "The two of you stick out your pinkies, then lock them together and shook on it."
            c "I promise always to trust you."
            mc "There, it's done."
            c "Yeah."
            scene cynthiatalk1
            c "Thanks, [mc]. I know I don't show it often. But I'm really glad that you're my friend."
            mc "Y-Yeah... no problem."
            mc "......"
            mc "So you've never had a close friend before?"
            c "No..."
            mc "But, how- I mean, you've been to so many places. And you're basically the most popular girl at the Academy."
            show cynthiatalk6
            c "Yeah, people are normally attracted to me. But that's not the real me."
            mc "Maybe you should be yourself more."
            c "You think they'll like... this."
            c "People always want things to be sugar coated, they don't want to see the hard truth."
            mc "I stuck with you."
            c "Well that's because you're not like the rest of them."
            c "Other people always look for a way to use me. They don't care about my feelings or who I really am."
            c "They just see me as this \"beautiful girl\" and thats it, just a labeled mannequin. It won't change no matter what I did."
            c "......"
            c "So instead of being used, I just use them and just dump them when I get the chance."
            c "It's easier that way."
            mc "Mh...."
            scene cynthiatalk4
            c "My mother used to say that a girl's strongest weapon is her beauty."
            mc "I think your knives would disagree."
            c "Hehehe."
            mc "You don't really have that much faith in humanity, don't you?"
            c "Yeah, you could say that. And if you're me, you'd probably feel the same way."
            mc "Should I know why?"
            show cynthiatalk6
            c "What?"
            mc "I want to know about your past. I want to know why you feel that way."
            c "Why?"
            mc "Because I want to get to know you better."
            c "And talking about my past will help?"
            mc "Yeah, and I'll tell you about mine!"
            c "But I don't want to know."
            mc "Uh."
            mc "Well, it's something friends do, ok?!"
            c "......"
            c "{i}sigh"
            c "...So..."
            c "What do you want to know?"
            mc "From the start."
            c "You mean from the day I was born?"
            mc "Yeah."
            c "B-But that would take a hell of a long time."
            mc "Well, we've got nothing else to do here on out until we go to sleep, don't we?"
            c "......"
            c "Well, ok."
            c "I was born in Thane. I lived there with my mother for 8 years. Then I was sold to a slave trader, and th-"
            mc "Wait, what? You were sold to slave trader?!"
            c "Yeah."
            mc "{i}How is she so casual about this?"
            mc "H-How?"
            c "My house was attacked by bandits. They killed my mother and kidnapped me. Then sold me to a slave trader."
            mc "Wh- How are you so casual about this?"
            c "What? Do you want me to cry or something? What happened has happened, no amount of crying is going to make it go away."
            mc "......"
            mc "I-I didn't know. I shouldn't have asked you. I'm sorry."
            c "...I don't really mind talking about it."
            mc "You don't?"
            c "Not really. Like I said, what happened has happened. It's always there even if talk about it or don't."
            mc "......"
            c "So, do you want to know more?"
            mc "If it's ok with you, yeah I do."
            c " day, the bandits came to my house. It's normal in Thane. They come and go as they please. If you can't defend yourself, you're done."
            c "This happened after my farther left. There was no  to protect us. Mom did what she could... But it wasn't enough in the end."
            c "She told them to take anything and leave us alone. But they weren't there to rob."
            mc "......"
            scene cynthiatalk3
            "She stares deeply into the bonfire with cold dead eyes."
            c "They raped her, and killed right before my very eyes."
            mc "......"
            c "Then they caught me and sold me to a slave trader."
            c "I was taken to Karnak. It's a place where slavery is still legal."
            c "I was sold to a general there. I was bought as a gift for his daughter."
            c "She was training to become a warrior. She normally used me as a dummy for her combat practice."
            c "So, she used to beat the shit out of me for all that kick."
            c "But it helped me."
            mc "Huh?"
            scene cynthiatalk4
            c "You can learn a lot from getting beaten up. I learned almost all of the techniques she used on me. I used to practice them at night."
            c "And from taking a hell load of punishment, you can learn a lot of endurance to take a lot of hits."
            mc "......"
            scene cynthiatalk3
            c "...I was there for about six years."
            mc "How did you escape that place?"
            c "......"
            c "As I was growing more and more into a woman, it didn't take long for the general to notice me."
            c " day, he called me to his room... He was drunk."
            c "He..."
            c "He tried to rape me."
            c " I grabbed a bottle nearby and smashed it over his head. And... I stab the motherfucker right in the chest."
            mc "......"
            c "I kept stabbing until the whole bed was caked with blood. I don't know what came over me, I couldn't stop it even though he was dead. All the hate and anger, it just poured out."
            c "......"
            c "After that... I ran away."
            c "I spent some days in the streets, stealing and barely had enough food to survive."
            mc "Didn't the guards find you after you killed the general?"
            c "No, Karnak is a big city, and the major part of it are slums. There's a  in a million chance that they can find you."
            mc "How long did you live there?"
            c "A couple of years."
            mc "You survived that long alone?"
            c "Well, while I was there, I joined a Thieves Guild."
            c "I got a lot of work there and it paid well."
            mc "What did you do there?"
            c "Basically, steal from the rich."
            mc "Oh."
            c "Picked up a few tricks there. But living there was tough. As they say; there is no honor among thieves."
            c "In the slums, the thieves are always at war with each other. So you always had to have eyes at the back of your head."
            mc "{i}She really going into full detail here. I guess she's never had the chance to talk about her past to anyone close to her."
            c "Then, after I had enough money, I left that goddamn city."
            mc "Where did you go then?"
            c "Dermis, Winden, Dorn, all around Astylla."
            c "I've even been to the capital."
            mc "No way."
            scene cynthiatalk4
            c "It's awesome. Every building there is like a palace. And the cafes there are the best!"
            mc "I guess you lured a lot of capital men into your net."
            show cynthiatalk5
            c "Yeah, it was hard. But in the end, they couldn't resist my beauty."
            "Cynthia continues to talk about all her adventures. You listen to her tales in amusement and sympathy. Soon, her mood shifts to a more positive setting."
            scene cynthiatalk1
            c "And that's how I met you; the brave, young, somewhat awkward [mc] I know now."
            mc "Har-har."
            mc "Thanks for letting me get to hear about your life story. I appreciate it."
            c "Of course."
            mc "But, man, you... you've been through a lot."
            c "Yeah."
            c "......"
            c "Now it's your turn, tell me about your past."
            mc "After hearing yours, I feel like mine will bore you out."
            c "No, I want to know."
            mc "Ok then."
            "You tell Cynthia about your past. There isn't much to talk about your memories, other than the part where you've lost your parents."
            "You were more in detail as you talked about Uncle Pete, Gabe, and the simpler times, good and bad, of you spent growing up in Randel."
            "You ended on how you got into the Adventurers' Guild and got to meet Sander, Eve and Cynthia."
            c "Neat... Well, you haven't had the smoothest life either."
            mc "Nothing compared to yours, though."
            c "All lives are special in their own way."
            mc "I guess."
            mc "So you do appreciate human lives."
            show cynthiatalk6
            c "I said “special”. I didn't say they were all good."
            c "Believe me, I've been the with the highest ranking people and the lowest of scum. Most of the time, there's barely a difference between them."
            c "Good people can't really survive in this world."
            c "You either use or be used."
            mc "......"
            scene cynthiatalk3
            c "Hah, I guess I ended up being no better than the people I hate."
            c "......"
            c "...I wish I could forget all this and start again... as a normal person."
            mc "......"
            c "......"
            c "Ugh, what's wrong with me? I'm talking way too much, and I'm not even drunk."
            mc "Heh, it's ok. It's good to see that side of you."
            show cynthiatalk4
            c "......"
            c "{i}Yawn"
            c "Getting sleepy. I think we've talked enough."
            mc "Yeah, let's go to sleep."
            c "Thank you for listening, [mc]. "
            c "I've never told my story to anyone before."
            c "I didn't expect it, but I feel better after I put that out."
            mc "No problem."
            c "Goodnight."
            mc "Goodnight."
            "You go into your tent, Cynthia goes into hers."
            scene forrestn with fade
            mc "{i}All that she had to go through in her youth. It's no wonder she ended up being who she is today. I really feel bad for her."
            mc "{i}I really do feel like I'm closer to knowing her now and what her deal is. Although... wish there was some way I could help ease her life a bit."
            mc "{i}Have I slowly fallen for her though? ...I don't know. I might have to see where this leads..."
            play music forest
            scene forrest with dissolve
            "By next morning, you and Cynthia worked together to dismantle the tents. Then comes the long walk back out of the forest and back to Randel."
            scene villageback with fade
            show talkwacb
            show smilemc
            c "What a trip eh?"
            show talkwamc
            mc "Yeah, I'm still feeling tired."
            c "Yeah me too, that was a long trip"
            show smilenc
            show talknc
            c "Got to sell this pelt now."
            mc "Ah yeah."
            c "I'll give you your cut when we meet next time."
            if paycynth == False:
                mc "Nah you can keep all the silver."
                mc "Think of it as me paying off my debt."
                c "You sure?"
                mc "Yeah."
                $ paycynth = True
                $ cynthiaPelt = True
                c "ok then, I'll keep it."
            else:
                mc "Ok."
            c "......"
            c "I guess I'll see you later then. "
            show talksadhappymc
            mc "Yeah."
            c "Bye."
            mc "Bye"
            scene villageback with fade
            "After saying your goodbyes to her, you decided to head back to the comfort of your home for some R&R."
            $ persistent.cynthFireplace = True
            $ cynthquest4 += 1
            jump home


label cynthquest5:
    hide screen hud
    mc "{i}What's Cynthia doing here?"
    show talkhappymc
    mc "Hey Cynthia."
    show normalcb
    show shockc
    c "[mc]!"
    mc "You out hunting alone?"
    show talknc
    c "No, I'm on a quest."
    mc "Ah, ok."
    mc "What's on this quest?"
    show sadc
    c "......"
    hide sadc
    show talkwanc
    c "Well, it's not a Guild quest."
    show talkwanmc
    mc "Huh?"
    c "It's from the barracks. I'm going to kill some bandits."
    mc "Oh..."
    show talksc
    c "I would've called you, but since you're not... comfortable with killing... I thought I'd do this alone."
    mc "......"
    mc "I'm coming with you."
    show shockc
    c "Really?"
    mc "I can't let you go alone."
    show talkwancb
    c "Oh-ho, so you suddenly turned into my bodyguard."
    mc "I now get why you kill these people. I want to help you."
    show sadc
    c "......"
    c "You have to understand what you're getting into, [mc]. Taking a human life for the first time is hard. You can never go back once you've done it."
    mc "I know."
    c "......"
    c "Ok then."
    c "Follow me."
    scene forest with fade
    "The two of you head deeper into the forest."
    mc "I didn't know you could get quests from the barracks."
    c "They're not technically quests, there more like bounties."
    c "You don't really get these types of quests in the Guild."
    c "You don't get any EXP for killing bandits, so it's pointless."
    mc "Hmmm."
    c "The Guild doesn't really understand how dangerous people can be."
    mc "......"
    mc "So, this is what you spent most of your time doing."
    c "Yeah. Someone has to do it."
    mc "......"
    mc "That's not why you're really doing this, is it?"
    c "......"
    c "I... just can't remember the fucker's face, the  who... killed my mother."
    c "I tried so hard, even when I was a slave, I tried to remember his face every night so I could kill him  day."
    c "But the memory of that face faded away."
    c "......"
    c "So I just kill every bandit I find. Might've killed the bastard already. Who knows?"
    mc "......"
    mc "But isn't it hard? To kill all these people...?"
    c "......"
    c "Once you forget they're people, it isn't really hard."
    mc "But they're still people, they have li-"
    c "I don't want to discuss morality with you now, [mc]. I thought you said you were ok with this."
    mc "I am but I'm worried about you."
    c "......"
    c "I'm fine."
    mc "......"
    "The two of you head further into the forest. The two of you don't talk to each other to simply focus on the task at hand."
    show angryc
    show thinkmc
    c "Their camp should be nearby."
    mc "So, how are we going to do this?"
    c "......"
    c "The camp isn't that big, there'll probably be like three to four guys."
    c "My initial plan was to draw them out  by  separately and take them out."
    c "But..."
    show talkwacb
    c "Now, since you're here, I think I won't be needing to that."
    mc "Ok, what's the new plan then?"
    c "We can take them head on."
    show talkwamc
    mc "Seriously?"
    mc "Can we take on four guys head on? I mean, I can help to draw them out."
    c "Nah. If I've got a partner to watch my back, it won't be a problem."
    show talknc
    c "And besides, it's more fun this way."
    mc "......"
    c "So, are you up for it? {p}Partner?"
    mc "Yes."
    play music battlemusic1
    "Man's Voice" "Well, well. isn't that cute."
    show shockc
    show suprised
    mc "Huh?"
    scene forrest with fade
    "Man's Voice" "A man comes out of the bushes. He's muscular frame has scars all over his body. You realize it's obviously a bandit."
    "Bandit Leader" "The two of you draw your weapons"
    "Bandit Leader" "Hey, guys, did you hear that! They're here to \"Take us head on\"!"
    "Bandit Leader" "Hahaha!"
    "You hear laughing from behind you. You look around and spot 2 more bandits. They slowly walk towards the two of you."
    "Bandit 1" "{i}Whistle{/i} We've got a nice  here, boss."
    "Bandit 1" "Mmm-Mm!"
    "Bandit 2" "God, I don't know the last time I had some pussy."
    "Cynthia spits onto the ground."
    "Bandit Leader" "Hehehe. A feisty , isn't she? Yeah, she'll do just great. I'll like it when they're rough."
    "Bandit Leader" "Bill take care of this little brat for me. Gavin and I will take care of the little lady."
    c "Get ready, [mc]."
    c "I'll deal with these two, you'll have to take on the other one."
    "Your heart starts to beat like crazy. Your joints tremble upon the thought of striking these men down."
    c "[mc]!"
    label cynthMCFight:
    $ gameover = "cynthMCFight"
    scene cynthmcfight
    $ persistent.cynthMCFight = True
    window hide
    c "Got my back?"
    pause
    mc "Yeah."
    "You close your eyes and take deep breath. Your heart settles."
    mc "Lets fucking do this!"
    c "Atta boy, let's show these fuckers who their dealing with!"
    "Bandit Leader" "Let's make this quick, boy!"
    scene forrest with fade
    show banditfight with easeinright
    if swordlvl >= 10:
        $ renpy.notify ("{color=#fff}Sword skill check: {color=#00C413}Success! ([swordlvl] >= 10)")
        $ round1banditfight = 0
        jump finishfight
    $ renpy.notify ("{color=#fff}Sword skill check: {color=#A50000}Fail. ([swordlvl] < 10)")
    show text "{color=#fff}Press space, click or tap the screen while the dot is on the green to win!" at truecenter
    pause 3.5
    hide text
    $ fmgd = 2/(swordlvl/10)
    if fmgd < 1:
        $ fmgd = 1
    $ fightMiniGame = "finishfight"
    jump start_fightMiniGame
label finishfight:
    "The bandit's strikes were strong. You were quick to deflect his strikes with your blade, but even you can't keep up with his relentlessness."
    "Bandit" "Not bad."
    "Bandit" "Let's see if you can keep up."
    $ round1banditfight += 1
    if swordlvl >= 12:
        $ renpy.notify ("{color=#fff}Sword skill check: {color=#00C413}Success! ([swordlvl] >= 12)")
        jump fightover
    $ renpy.notify ("{color=#fff}Sword skill check: {color=#A50000}Fail. ([swordlvl] < 12)")
    show text "{color=#fff}Press space, click or tap the screen while the dot is on the green to win!" at truecenter
    pause 3.5
    hide text
    $ fmgd = 3.5/(swordlvl/10)
    if fmgd < 1:
        $ fmgd = 1
    $ fightMiniGame = "secondfightchecks"
    jump start_fightMiniGame
######## SECOND FIGHT CHECKS
label secondfightchecks:
    if randel_fails < 3:
        $ randel_fails = 0
        jump fightover
    else:
        $ randel_fails = 0
        jump losebandit
###############################
label losebandit:
    $ randel_fails = 0
    mc "Ahh shit!"
    "You have cuts all over your body. Blood pours out of your wounds."
    "Your energy slowly starts to drain out."
    "Bandit" "Sorry, kid."
    scene black with fade
    jump GameOver
###############################
label fightover:
    $ randel_fails = 0
    mc "{i}I can't keep doing this."
    mc "{i}I should try dodging instead of deflecting and then find an opening."
    "You leap to the side as the bandit swings his sword. Your speed is much faster now."
    "By instinct, you get the idea of slicing his legs with your blade."
    "You make a cut across the bandit's leg with your blade."
    "He yelps as his legs brought him kneeling to the ground."
    scene forrest with fade
    stop music fadeout 0.9
    "You look behind, Cynthia's already taken care of the other two bandits."
    "She looks at you and sees the bandit on the ground."
    show thinkmc
    show normalcbop with easeinleft
    play music forest
    c "I'll deal with him, [mc]."
    "Bandit Leader" "Don and Gavin... are they...?"
    c "Don't worry, you'll join them soon."
    "Bandit" "Fuck!"
    "Bandit" "Ok, just listen to me!"
    "Bandit" "I-!"
    "The man starts to cry."
    "Bandit" "Just... {i}sob{/i}... let me... live, ok?!"
    c "Ugh... this why I kill these guys right away."
    c "Seeing them grovel and sobbing makes me want to puke."
    "Bandit" "I didn't know these guys for long! I just needed some money, I'm not a bad person, not compared to them!"
    "Bandit" "Just... just please, let me go!"
    c "Yeah, you'd like that, wouldn't you?"
    "Bandit" "No, PLEASE... please!"
    "Bandit" "I-I don't want to die!"
    mc "Cynthia!"
    hide normalcbop
    show normalcb
    c "What?"
    show worriedmc
    mc "Just let him go."
    show angryc
    c "Are you crazy? Why would I let him go?"
    mc "Because he's given up."
    c "You believe this bullshit? If let him go, he'll call more of his friends."
    "Bandit" "I swear you ain't going to see me again... I swear!"
    c "......"
    c "I'm killing him."
    "Bandit" "No!"
    mc "You'll have to trust me."
    show sadc
    c "{i}sigh"
    hide sadc
    mc "You have stop all this killing, Cynthia."
    c "It's my choice, you don't get a say in it."
    mc "I do, I'm your friend."
    show sadc
    c "..."
    mc "You're not alone anymore, you don't need to keep doing this."
    c "......"
    mc "Just put the past behind you. You can start a new...  I'm here for you."
    c "..."
    c "I-"
    show suprised
    mc "LOOK OUT!"
    play sound slash1
    scene mcsavecynth with hpunch
    $ persistent.savedCynthBandit = True
    "You push Cynthia away. The blade pierces your abdomen. You feel the cold steel deep in your body. You fall to the ground."
    scene black with vpunch
    c "[mc]!"
    c "{b}YOU MOTHERFUCKER!!!{/b}"
    "Bandit" "GAAAAAHHH!"
    scene forrest with fade
    pause 0.3
    scene black with fade
    pause 0.3
    scene forrest with fade
    play sound horror
    mc "Ugh..."
    c "[mc]!"
    c "[mc]! Stay with me!"
    mc "...I-I... feel kinda dizzy."
    c "Hang on."
    "Cynthia puts you over her shoulder."
    c "Come on."
    c "We have to get to the Guild."
    "You lean on to Cynthia as she carries you forward. You feel your legs slowly losing its strength, you vision gets blurry. You can feel your sides growing in pain."
    scene forrest with fade
    pause 0.3
    scene black with fade
    mc "......"
    scene forrest with flash
    c "[mc]!"
    c "You have to stay awake, you hear me?!"
    mc "...Ugh ...Yeah."
    c "Start counting!"
    mc "Wh-What...?"
    c "Count, damnit!"
    mc "......"
    menu:
        "One":
            mc "One..."
    menu:
        "Two":
            mc "T-Two..."
    c "Keep going!"
    menu:
        "Three":
            scene forrest with fade
            pause 0.3
            scene black with fade
            pause 0.3
            scene forrest with fade
            mc "Three..."
    menu:
        "Six":
            mc "Six"

        "Five":
            mc "Five"

        "Four":
            mc "Four..."

        "Fifty":
            mc "Fifty"
    menu:
        "Six":
            mc "Six"

        "Five":
            mc "Five"

        "Four":
            mc "Four..."

        "Fifty":
            mc "Fifty"
    stop music
    stop sound
    scene black
    "......"
    c "[mc]!"
    "..."
    "......"
    c "No..."
    "..."
    "......"
    scene villageback with fade
    pause 0.3
    scene black with fade
    pause 0.3
    scene villageback with fade
    c "{i}huff... huff... huff..."
    scene black with fade
    play sound doorknock
    c "Someone help... {i}huff... huff...{/i} It's [mc]!"
    j "Oh my god!"
    scene agblr with fade
    show talksads
    pause 0.2
    scene black with fade
    sa "I'll get him!"
    j "Take him to the infirmary, quick!"
    mc "...Ugh..."
    j "Triss!"
    j "She's here. Call her!"
    sa "Hang on, little man. I got ya."
    mc "..."
    "..."
    "......"
    "......"
    play music horror
    "Demonic voice" "It hurts, doesn't it?"
    scene dream25
    pause
    scene dream24
    pause 0.2
    scene dream23
    pause
    scene dreamc2
    pause
    scene dream23
    pause 0.1
    scene dreamc2
    pause 0.1
    scene drmc1
    pause 0.2
    scene dream25
    pause 0.1
    scene dreamc2
    pause 0.1
    stop music
    scene wakeup1 with flash
    pause 0.3
    scene wakeup2
    pause
    mc "......?!"
    mc "{i}..."
    scene cynthbed2 with flash
    mc "{i}Cynthia?"
    play music nurture
    mc "{i}She's asleep."
    mc "{i}Where am I? What happened to me?"
    mc "{i}Oh, yeah."
    mc "{i}Damn it, that motherfucker."
    "You gently touch your abdomen to feel the wound."
    mc "Gh-! FFFuck!"
    c "......"
    scene cynthbed1 with dissolve
    c "...[mc]?"
    c "...You're awake."
    mc "...Hey."
    c "How are you feeling?"
    mc "Not bad... it still stings a bit."
    c "......"
    c "You've been asleep for a whole day."
    mc "Really?"
    c "Yeah."
    mc "H-How did I get here?"
    c "I carried your sorry ass."
    mc "All the way to the Guild?"
    c "Yeah."
    mc "Ah. man..."
    mc "It's all my fault. I was such an idiot!"
    c "Yeah, you were."
    c "You didn't know."
    mc "......"
    stop music fadeout 0.9
    "{i}knock knock"
    c "Looks like there are more people to see you..."
    c "I leave you to them, then."
    mc "Thank you, Cynthia... for saving me."
    c "......"
    c "You're welcome."
    $ persistent.cynthWatchingOver = True
    scene cynthbed3 with dissolve
    e "Is he awake?"
    c "Yeah."
    scene cynthbed4
    show talksadsr with easeinleft
    show sadtalke with easeinleft
    e "How are you, little one?"
    mc "I'm fine."
    sa "That was a nasty wound, [mc]. It's a good thing Triss was at the Guild."
    mc "Triss?"
    sa "She's the one who fixed you up. She one of the best doctors we have."
    mc "Oh..."
    e "We didn't know you were going on bandit hunts. That's dangerous work, you know."
    mc "Yeah... I was helping Cynthia."
    sa "That girl. I knew she's a tough one when I saw her."
    sa "She carried you all the way here, do you know that?"
    mc "Yeah."
    e "And she was in this room the whole time while you were in bed. She was up all night keeping an eye on you, seeing if you would ever wake up."
    mc "Oh..."
    sa "Are the two of you..."
    e "Sander! Now's not the time."
    e "You take some rest, little one. We'll leave."
    sa "See you kid."
    mc "Alright."
    hide talksadsr with easeoutleft
    hide sadtalke with easeoutleft
    mc "......"
    mc "{i}Cynthia was with me the whole time. I didn't know she worried about me that much."
    "{i}Knock knock"
    mc "{i}Who is it this time."
    mc "Come in."
    show talkwatr with easeinleft
    tr "Hey."
    if sawtriss >= 1:
        mc "Hey Triss, thank you for... patching me up."
    else:
        mc "Oh, hello, thank you for... patching me up."
        mc "{i}So this is Triss? She's the one Sander talked about."
    tr "No problem, kid. How's the wound?"
    mc "It still stings a bit."
    tr "Hmmm, let me see."
    "She comes over and pulls over your shirt without warning."
    mc "H-Hey."
    tr "You're all good."
    mc "Huh?"
    "You look at the area of your wound, but you don't see anything. You look as if you've been as you always were before getting the wound."
    mc "What?"
    mc "I'm completely healed?"
    $ trissheal += 1
    tr "Well of course, I used healing magic and potions on you after all."
    mc "Why does it hurt still?"
    tr "Don't worry, your brain still thinks it's hurt. Your pain receptors are still being stimulated even though there's no wound."
    mc "Uhh, ok."
    tr "It'll get better soon."
    mc "So how long should I rest?"
    tr "You don't need to anymore, you're all healed up. The best thing for you to do is go home now."
    mc "Really?"
    tr "Yeah, the pain would go away once you start to move around."
    mc "Ok then."
    tr "You're quite astonishing, I have to say."
    mc "Mh?"
    tr "You've got a very healthy body, [mc]. When that girl brought you here, it was about an hour after you were impaled by a 30-inch sword."
    tr "But you've hardly lost any blood. It's almost like your body healed itself up."
    mc "Oh, I-I don't know what to say."
    tr "Hmmm. It did surprise me quite a bit; you would've been a goner if you bled out along the way."
    mc "Maybe Cynthia used some first aid."
    tr "There was a bandage, but that's it. She didn't use any magic."
    mc "......"
    tr "Ok, enough about that."
    tr "I'll be leaving now. You're ok to go as well."
    mc "Alright. Thanks, Triss."
    tr "You're welcome."
    hide talkwatr with easeoutleft
    mc "{i}What she said is definitely interesting... My body healed itself?"
    mc "{i}Any way I better leave now."
    scene agblr with fade
    if theaguild >= 1:
        show worriedmc
        show worriedth with easeinleft
        th "[mc]!"
        mc "Thea."
        th "You shouldn't be walking."
        show talksadhappymc
        mc "No, no, Triss said I'm fine."
        show crysmileth
        th "Oh... I was so worried, you know!"
        mc "Yeah, sorry I worried you so much."
        th "Thank Astylla you're alright now."
        th "Your friend Cynthia was really nice. She was with you the whole time."
        mc "Did... Did the two of you talk"
        th "Oh yes the whole time we were with you. "
        mc "Oh, hehe... What... Did you guys talk about?"
        th "What did we talk about? I can't quite remember, we talked about whatever came to our minds."
        th "She told me about the adventures the two of you went on. Then we talked about ourselves, I told her about my past and she told me about hers."
        mc "Wait she did?"
        th "Yeah."
        mc "She opened up to you that fast?"
        th "Well, we've both been through alot. I guess we could sort of relate to one another in some way."
        mc "Hm."
        th "So are you going home now?"
        mc "Yeah."
        th "Let's go then."
        show talkwanmc
        mc "Wait, your shifts not over yet. I can go by myself, no problem."
        th "Are you sure?"
        mc "Yeah, I'm fine."
        show cryth
        th "Alright then. Please be careful, [mc]."
        mc "I will."
    scene agblr
    mc "I better talk to July before I leave."
    scene adgc6 with fade
    j "Oh my, I'm glad to see you on your feet, [mc]!"
    mc "I really worried everyone, didn't I?"
    scene adgc5
    j "Yes, you surely did. Almost gave me a heart attack."
    mc "{i}sigh{/i} I'm really sorry."
    j "You should be. I swear, worrying me like that. Hmph!"
    j "......"
    scene adgc6
    j "Triss said you're fully healed now?"
    mc "Yeah."
    j "She saved your life. Did you talk to her?"
    mc "I did."
    j "Good."
    j "You have to be more careful, [mc]."
    mc "I know."
    j "Since when did you start going on bandit hunts?"
    mc "Cynthia was on a quest from the barracks."
    mc "I just wanted to help her out."
    j "Hm, I didn't know she took on quest like that."
    mc "......"
    mc "Where is Cynthia?"
    j "She's in her room, I think she resting."
    j "That girl was as worn out as you were."
    mc "I guess I shouldn't bother her right now."
    j "I think so too."
    j "Anyway, now that that's over, try being more careful when picking which quests you can handle here after."
    mc "Alright."
    mc "Did my uncle hear about this?"
    j "I don't think so. Normally, what happens in the Guild stays in the Guild."
    j "I don't think word got out."
    mc "Oh good, I don't want to make him worry."
    j "Indeed."
    mc "I'll be going then."
    j "Alright."
    if evesex >= 1:
        scene agblr with fade
        show smilemc
        show sadtalke
        e "Hey, little one, are you leaving?"
        show talksadhappymc
        mc "Yeah."
        e "Alright."
        e "I feel really bad because I wasn't able to be with you while you were hurt."
        mc "It's alright."
        e "I was on quest out of town."
        mc "Eve, it's alright."
        e "Alright then."
        show blushtalke
        e "If you ever want to rest in my room, it's always open."
        mc "Oh... Hehe, I'll keep that in mind."
        e "Ok then, I leave you alone now."
    scene agblr with fade
    mc "{i}I sure have worried the entire Guild."
    mc "{i}Why does it make me slightly happy though?"
    mc "{i}I guess it's because I feel like I have a lot of people who care about me?"
    mc "......"
    mc "{i}I shouldn't bother Cynthia right now."
    $ time = 3
    $ day += 1
    $ cynthquest5 += 1
    jump guild



label PREcynthquest6:
        hide screen hud
        "As you enter you see cynthia waving at you"
        "You go to her."
        show talknc
        show smilemc
        c "You're looking good now."
        show talksadhappymc
        mc "Yeah, I feel much better."
        c "Good."
        c "I was just about to visit you."
        mc "Hmmm? whats up?"
        c "Come with me."
        mc "......?"
        stop music
        scene cynthiaroom with fade
        "You follow cynthia into her guild quarters"
        show talknc
        show talksadhappymc
        c "Here."
        "Cynthia hands you a box."
        mc "What is it?"
        c "Open it."
        "You open the box."
        "You find two new boots."
        mc "Wait are these for me?"
        c "Yup."
        mc "oh...b-but why."
        c "It's a gift from me for saving my life and..."
        show blushtalkhc
        c "And for being my friend."
        mc "Whoa cynthia, I don't know what to say"
        hide blushtalkhc
        c "I hope it fits you."
        mc "They look really expensive."
        show talkwahcb
        c "Uhm... A bit. But it was nothing.  You know how much money I have in my cupboard, right?"
        c "Thought I'd put them to some use."
        mc "Ahh... Yes... The ears."
        mc "But you really shouldn't have, I didn't do much."
        c "Are you kidding me. You're the only person whos ever saved my life, you deserve a reward for that."
        mc "hehehe alright then."
        c "Ok now try them on already."
        "You remove your old worn out boots and try the new ones. They fit perfectly and feel very commfortable."
        mc "They're perfect. Thanks cynthia."
        hide talkwahcb
        c "Hehe you're welcome."
        mc "......"
        c "......"
        mc "So, have any more monster hunts planned."
        c "Uhm no not really. I think it's best if we had a small break."
        mc "Hmmm yeah."
        c "But I have been hearing alot of rumours about a vampire."
        show talkwanmc
        mc "Vampire?"
        c "Yeah, and they say it's living very close by."
        mc "{i}Shit. That's July she's talking about."
        hide talkwanmc
        mc "B-but...... I've heard vampires are...... Really powerfull."
        c "Oh yeah they are. We wouldn't stand a chance."
        c "But I would really like to see one, for once in my life."
        mc "You've never seen one."
        c "No. There are very few vampires in Astylla, most of them are in the darklands."
        mc "Ah."
        c "It's just a thought."
        mc "Ok."
        mc "{i}Thank god she's not too serious about this."
        hide talknc
        show talkwanc
        c "Alright, thats it. now leave, I've got an assignment to complete."
        mc "hehe fine."
        show talknc
        c "Bye, [mc]."
        mc "Bye."
        scene agblr with fade
        mc "{i}Man these boots feel great."
        mc "{i}Damn, who would've thought I would be getting a gift from cynthia."
        mc "{i}July should be carefull. But when you think about it, She's been here for so long, I'm suprised that she some how manged to mantain her cover."
        mc "{i}I guess rumors are bound to appear."
        $ cynthboots += 1
        jump guild



label cynthquest6:
    scene homenight
    hide screen hud
    play music night
    "{i}knock knock knock"
    "......"
    mc "Nhh... "
    "......"
    scene homenight with vpunch
    "{i}KNOCK KNOCK KNOCK"
    mc "Huh...?"
    mc "...What the hell?"
    mc "Who is it?"
    c "It's me, Cynthia."
    mc "{i}What the hell is she doing this late?"
    scene kitchenn with fade
    show thinkmc
    show talkwahcb
    c "Hey."
    mc "H-Hey, what are you doing here?"
    c "Come with me."
    mc "{i}Here we go again."
    show talkwanmc
    mc "Can you tell me what I'm doing before just dragging me off?"
    c "We're going vampire hunting."
    mc "Wh-What! Now?!"
    c "Yeah."
    mc "B-But... I thought you weren't that serious with the vampire business."
    c "I am."
    c "Are you coming or not?"
    mc "{i}I have to go. What if she actually finds July?!"
    mc "Alright. Give me a few minutes."
    scene homenight with fade
    show thinkmc
    mc "{i}Shit...!"
    mc "{i}What if I run into July? What do I do?"
    mc "{i}I guess I'll have to convince Cynthia to give up the search somehow."
    show normalcgop
    c "So-"
    show suprised
    mc "AHHHHH!"
    hide normalcgop
    show normalcg
    show talkwanmc
    mc "Don't!"
    mc "Sneak up on me..."
    mc "Like that..."
    show talknc
    c "Sorry, it's a habit."
    c "So, is this your room?"
    mc "Uhh... yeah."
    c "Hm..."
    if theaguildjob >= 1:

        c "Where is your sister? I hope I didn't wake her up."
        mc "{i}Sister?"
        mc "{i}Ahh... She's talking about Thea."
        show talksadhappymc
        mc "Are you talking about Thea?"
        show talkwancb
        c "Yeah, you got more sisters?"
        c "How come you never told me about this?"
        mc "She... Isn't actually my sister."
        show talkwancb
        c "Huh?"
        mc "She's a... friend."
        c "And she lives in your house?"
        mc "Yeah, it's... it's a long story."
        mc "Can we go now? I thought you said you we're in a hurry."
        hide talknc
        show normalcb
        c "Mh..."
        show talknc
        c "Fine, whatever. Let's go."
    else:
        c "You ready?"
        mc "Yeah."
        c "Let's go then."
    scene forrestn with fade
    show talkwanmc
    show normalcg
    mc "So how are we supposed find it?"
    c "Well, I've already done the searching."
    c "I've been in a deep investigation for the past few days."
    mc "Huh, so you were serious about this?"
    c "Yeah."
    mc "So what did you find?"
    c "I went around asking people."
    c "Most of them said that it was a story that has been in the town for decades. It's an urban legend, really."
    mc "And what made you so interested in solving this kind of case?"
    c "I've got a thing for solving mysteries, the paranormal, or anything out of the ordinary, ok?"
    mc "So what did you learn about this supposed vampire?"
    c "They say it lives very close to the village."
    mc "Any proof?"
    c "One man, a woodcutter, said that he keeps finding these dead boars in the forest."
    mc "B-Boars?"
    c "Yeah."
    mc "So you think the vampire did this?"
    c "Yes."

    mc "B-But how do you know it's a vampire? I mean aren't vampires famous for feeding on human?"
    c "Yeah, but the woodcutter describes the boars being shriveled up and having bite marks."
    mc "{i}Shit, she's onto her."
    mc "But you can't be sure, right?"
    c "Vampires can survive with any type of blood, it doesn't have to be human. They prefer the taste of human blood, that's why they normally feed on humans."
    c "So I think this could be a very weak vampire, or..."
    c "It's someone who's living in town."
    mc "What?!"
    c "Just think about it; A vampire that's grown very close to humans and sees them as their own kind. So, they don't feed on humans and have to survive on alternative means for blood."
    mc "That's q-quite a stretch."
    c "Yeah, the second theory is quite a bit..."
    c "I know there's a probability that this isn't a vampire, but it's at least worth checking out."
    mc "Anyway, where are we going now?"
    c "To the place where the woodcutter saw the bodies. He marked a few places. I checked them all out except this one."
    c "I thought I'd have better luck with you around."
    mc "Oh."
    c "......"
    show smirkc
    c "You're not scared, are you?"
    mc "No!"
    show talknc
    c "You do look a bit nervous."
    mc "Of course I'm nervous, we're going to hunt a bloody vampire."
    c "Hehe."
    c "Don't worry, we won't be hunting it."
    c "I just need to get a look."
    mc "Fine... let's go."
    scene forrestn with fade
    "You follow Cynthia into the forest. You two move deeper away from town and into the deeper parts of the woods."
    mc "{i}July, please don't be there..."
    c "Almost there."
    mc "We're pretty deep into the forest."
    c "Yeah, and the fact that we're here at night makes it all the more dangerous."
    mc "You're actually excited about whether or not this vampire exists, aren't you?"
    c "No..."
    c "Ok, a bit."
    mc "So you expect we're going to bump into the vampire just like that?"
    scene julynight1 with vpunch
    mc "WUH-!"
    mc "{i}Fuck, it's July!"
    c "What?"
    "Cynthia looks towards the direction where you last saw July, confused of what you saw."
    c "What are you looking at?"
    mc "{i}You're looking straight at it, what do you mean?!"
    mc "Can't you s-see anyone there?"
    c "Huh?"
    "She takes a closer look."
    c "No."
    c "Oh wait, I know what you're trying to do."
    c "Hehehe. Nice try, [mc], but you can't scare me like that."
    mc "{i}She can't see her!"
    scene forrestn
    show talkwancb
    show worriedmc
    c "Come on, we don't have time for stupid pranks. We're almost there."
    mc "{i}She didn't see July. Why was I the only one who could see her?"
    mc "{i}Phew. Anyway, I'm glad how this turned out."
    "Grrrr..."
    mc "{i}Was that Cynthia's stomach?"
    mc "You hungry?"
    show normalcb
    c "No, why?"
    mc "Well, you're stomach's growling."
    "Grr..."
    c "That's not my stomach."
    "The both of you turn around to face whatever was the source of that growling."
    scene julysave1 with vpunch
    mc "Shit!"
    c "Direwolves! Three of them!"
    c "Don't move, [mc]..."
    play music battlemusic1
    "The three wolves slowly close in on the two of you."
    "One of it sniffs the air close to you. Then at the next second starts growling at Cynthia."
    c "Shit!"
    "One of the wolves lunges to take a bite out of Cynthia."
    show julysave2 with easeinright
    "Then out of nowhere, July swipes in and grabs the wolf before it ever lands on Cynthia."
    "She grabs the wolf by its torso and tears it in half."
    mc "{i}Oh my god."
    "She throws the brutalized carcass at the two remaining wolves, blood splatter onto them where she threw."
    "They stand on their ground, growling and snarling after what July did with such murderous intent."
    "July stands in front of you with her hands stretched apart, anticipating for the wolves to try their next move."
    "After a minute in their standoff, the wolves give up and retreat back into the forest."
    play music night
    scene julysaveblood with fade
    $ persistent.cynthVampire = True
    "July turns to the two of you with blood covered all over her. You look at Cynthia, she's definitely staring at July with her mouth open with disbelief."
    c "Y-You... a-are a vampire."
    mc "{i}Well, she's really surprised now. Frankly, I've never seen her like this."
    j "Yes, Cynthia, I am."
    c "What the fuck?! H-How do you know my name?"
    j "It seems like you don't recognize me."
    c "Huh?"
    j "I'm July."
    c "{i}gasp{/i} I knew it!"
    c "I FUCKING KNEW IT!"
    c "See, I told you, [mc]!"
    mc "Yeah, thanks for saving us, July."
    mc "And for your information, this whole idea was entirely on Cynthia's, ok? I didn't even tell her anything."
    c "Huh?"
    c "Wait, wait, YOU KNEW?!"
    mc "Uhm, yeah."
    c "B-But, how? And why didn't you tell me?"
    mc "Because I promised July I wouldn't tell anyone."
    c "......!"
    c "Ugh..."
    c "Fine. I let you pass on that one."
    c "I just can't believe I'm standing in front of a vampire, and it's July!"
    j "......"
    c "I mean... you're still July, right? You're not evil or anything?"
    c "...Wait!"
    c "You could be..."
    c "But you met [mc] and he's fine, so I guess you aren't."
    mc "Ye-"
    c "Wait!"
    c "But still you could be!"
    c "Is [mc] one of your minions? Did you kill him and turn him into a zombie?"
    c "Because that would explain why he's so dumb."
    mc "Hey, slow down! I'm not a zombie."
    j "Heh... I'm not evil, Cynthia. And [mc] isn't a zombie."
    j "I'm still the July you all know."
    c "Oh, thank Astylla!"
    c "But how did you actually find out, [mc]?"
    mc "I... well... one day, I followed her out of the Guild and saw her dumping dead boars in the forest."
    c "Lucky."
    mc "Then, the next day, I went into the Guild at night and... yeah. I, like, found her living under the Guild."
    c "Under the Guild?"
    mc "Yeah, there's a trapdoor under the bear rug."
    "You can sense July giving a pained, concerned glare at you."
    mc "...Oh, shit."
    c "......"
    c "Wait, that was too easy. Just like that?"
    mc "Well... yeah."
    mc "Earlier, when I said that someone was there, you couldn't see anyone, right?"
    c "Yeah."
    mc "But I could see. It was July."
    c "What?"
    mc "Yeah, it's weird. Do you know anything about this, July?"
    j "I don't know if you've heard, but vampires can turn invisible. Normally, when I go out at night, I turn invisible so no one from town might see me."
    c "But [mc] saw you."
    j "Yes, he did. Today and the day he found me."
    mc "How's that possible?"
    j "I don't know, [mc]. It seems like you can see me even if I turn invisible."
    c "Woah, that's cool."
    c "So that means you got like a secret power."
    mc "I-I don't know, it's weird."
    j "That night when you caught me at the Guild, I tried to erase your memory and make you unconscious."
    j "But I failed there as well."
    mc "Was that why you fainted?"
    j "Yes."
    c "You're like fully vampire-proof, a natural vampire hunter."
    c "Oh... no offence, July."
    j "......"
    mc "Do you know any reason for this?"
    j "I can't think of any."
    c "So you can erase memories as well."
    j "Yes. Normally, when someone sees me, I erase their memory."
    c "So you can't erase [mc]'s memory. Does that mean I'm going to get my memory erased."
    j "......"
    j "No. The two of you are well known members of the Guild. I have my trust in [mc]. And you are able to trust in him, then he would trust you in keeping my identity a secret."
    j "So, in short, I won't be erasing your memories."
    c "Oh... thank you."
    c "So are we the only ones who know?"

    j "No."
    mc "Wait, but you told me-"
    j "Sorry, [mc]. I lied."
    j "Everybody at the Guild knows."
    mc "What?! Even Sander and Eve?"
    j "Yes. Once someone becomes a Silver, we tell them."
    mc "We?"
    j "Me and the Diamond level adventurers. The Guild is a family. And whatever is in the Guild stays in the Guild. This secret has been passed down from generation to generation."
    j "The reason why I didn't tell you is because you're still a Bronze. If the Diamonds knew about this, I could get into a lot of trouble. Hehe."
    mc "Oh."
    j "So I trust the two of you to keep this a secret... for now."
    "[mc] and {color=#FF7F7F}Cynthia" "Yeah."
    j "The two of you should leave now. You shouldn't be this deep in the forest, especially at night."
    mc "Right."
    mc "Let's go."
    scene forrestn with fade
    "The two of you leave. As you look back, July was nowhere to be seen as she disappeared into the night."
    c "Where did she go?"
    mc "No idea."
    "The two of you walk for a while. Throughout the journey, Cynthia is silent. You can tell that she's in a deep thought about what happened earlier."
    "The two of you get back to the Guild."
    scene villagen with fade
    show talknc
    show smilemc
    c "Well, that was a wild ride, wasn't it?"
    show talksadhappymc
    mc "Y-Yeah."
    c "I mean July is a freaking vampire!"
    mc "I know."
    c "Sorry for dragging you in the middle of the night, [mc]."
    mc "Nah... I had fun too."
    show sadc
    c "......"
    c "[mc], I've been thinking."
    c "July said she can erase memories, right?"
    mc "Yeah."
    c "I'd thought I would ask you."
    c "What if..."
    c "What if she could erase my past memories?"
    show talkwanmc
    mc "What are you talking about?"
    c "I don't know..."
    c "I mean, I thought if I can forget all about my past, I wouldn't be this... fucked up person. I could live my life like a normal girl, free from all that trauma I suffered."
    c "I could be that fake princess... for real, you know?"
    mc "......"
    menu:
        "Don't say anything":
            mc "......"
            c "......"
            show talksc
            c "{i}sigh{/i} I know it sounds crazy."
            c "......"
            c "Hah... It's been a long night, I guess I'm just tired."
            c "I should go now. Goodnight, [mc]."
            mc "Goodnight."
            mc "{i}I hope she wasn't serious."
            $ cynthquest6 += 1
            $ time = 4
            jump home
        "No.":
            mc "But that wouldn't be you!"
            c "Huh?"
            mc "You are the person you are now. It doesn't matter if you are fucked up or not, you are {b}you{/b}, and I wouldn't change that for anything."
            c "......"
            show worriedmc
            mc "If erasing your past erases the you who's standing in front of me right now, I don't want that!"
            mc "I've gotten to know you so much. Why would you have to take away a part of you that makes you... you? I feel like we would end up starting all over again if you did... So, please, don't."
            show shockc
            c "......"
    $ savecynthia += 1
    scene villagen
    show talkc
    show suprised
    "Cynthia hugs you out of nowhere."
    mc "......?!"
    c "Shit, sorry."
    show talksadhappymc
    c "I don't know why I did that."
    mc "N-No, it's fine."
    show blushtalkhc
    c "I guess I'm really tired... Been a long night."
    mc "Y-Yeah."
    c "G-Goodnight, then."
    mc "Goodnight."
    c "......"
    show talkshc
    c "Thank you, [mc]."
    scene villagen
    show smilemc
    mc "{i}She hugged me. She's never done that before."
    mc "{i}I'm glad she felt better after that."
    "You went back home for the night. Though tired, you feel happy that you accomplished something. And you slept soundly after that."
    $ cynthquest6 += 1
    $ time = 4
    jump home



label preCynthDate:
hide screen hud
scene academytalk
"As you walk in you notice that there's a huge commotion coming from some students."
"Student 1" "What the hell happened?"
"Student 2" "Cynthia knocked Jamie's teeth off."
"Student 1" "Wait, what?"
"Student 2" "Yeah."
"Student 3" "She even swore at me earlier, told me to fuck off. What's wrong with her?"
"Student 1" "Did she break up with anyone?"
"Student 2" "Was she with anyone to break up with?"
"The chatter continues as you continue walking towards your class."
mc "Whoa, I guess I must have missed one hell of a show. And avoided being roughed up."
"As you're walking, your eye catches something. It's Cynthia. She's poking her head out of the storage room and is gesturing you enter into the room with her."
mc "Uh... ok?"
"You slowly go into the storge room, making sure no one spots you."
mc "Hey, what's g-"
scene cynthkiss1 with hpunch
"Cynthia kissing you before you can say another word."
mc "......!?"
scene storeroomblr
show talknc
show suprised
c "I love you, [mc]."
"You stand there with your mouth wide open."
mc "......"
show blushtalkac
c "I said I love you, asshole."
c "Say something."
mc "I-I... love you too."
c "Ugh... That's the least romantic thing you could've said."
mc "I'm just trying to process what's happening-"
show cynthkiss1 with fade
"She kisses you again, pining you to the wall. Her hands pressed against the wall with your head in-between."
hide cynthkiss1 with fade
hide blushtalkac
show talksc
show talksadhappymc
c "Thank you, [mc], for loving me."
c "The real me."
c "That night, You showed me that there are still people in this world who want me, you gave me a reason to stay in this world."
mc "Wh-what are you saying?"
c "Just forget it. It's not important anymore."
show cynthkiss1 with fade
pause
hide cynthkiss1 with fade
c "Who would've thought my first friend... would be my first lover."
mc "Wait, I'm your first lover?"
c "Yeah..."
c "And..."
hide talknc
show blushtalkhc
c "...That was my first kiss."
mc "{i}I'm Cynthia's first kiss!?"
c "......"
mc "{i}Whoah, she's blushing."
show talknc
c "Anyway, I was wondering if we could go on a date."
mc "A d-date?"
c "Yeah. I'd like to know what it's like to go on a real date, for a change."
mc "{i}This is going really fast."
mc "Th-this is going really fast."
show blushtalkac
c "What? You want us to kiss like ten times and then go on a date."
mc "N-no, I mean this all is so sudden."
c "Ok. Do you want to go on a date with me or not!"
mc "I-I do."
show angryc
c "Then why are you wining retard!"
mc "{i}Sigh{/i} alright alright."
mc " Where do you want to go?"
show smilenc
c "......"
c "How about the café?"
mc "{i}A shit, there goes my purse again."
mc "Alright, when?"
c "Anytime."
c "And you are paying, by the way."
if paycynth == 1:
    c "I don't mind paying, but I would really appreciate it if you could bring some money this time."
    mc "Yeah, yeah, don't worry."
else:
    mc "Ok. Sure."
c "Great, then I'm outta here."
mc "Now? But the Academy's still not over."
show talkwahcb
c "Well, I'm not in the Academy anymore."
mc "What do you mean you aren't in the Academy."
c "I'm dropping out."
mc "Oh... and the talk about you going crazy in the Academy has something to do with it?"
c "Yup. I always hated being in this fucking place. Besides, I got the Guild to fall back to now. And I didn't want to pretend being this fake-ass popular girl anymore."
c "Because I know there's someone who really loves me for being... well, me."
mc "......"
c "But damn, it felt so good punching Jamie."
mc "What happened there?"
c "He always keeps giving me these perverted looks. And just today, he groped my butt."
c "That's where I lost it. I punched the fucker so hard; I knocked his teeth out. Hahaha!"
mc "I guess he deserved it then."
c "Of course he did."
scene storeroomblr
show talknc
show smilemc
c "......"
c "It's kinda weird. Even though we're lovers now, I feel like nothings really changed between us."
show talkwamc
mc "Hehehe,. Yeah, me too."
c "I think it's better that way. I don't like being too mushy anyway. Hehe."
c "Alright, I'll see you later then?"
mc "Yeah."
hide talknc with easeoutright
mc "{i}Wow."
mc "{i}That really happened."
mc "{i}Ok, I need to get ready for the date. So I'll have to collect a pack ton of silver."
mc "{i}A date with Cynthia!"
mc "{i}You finally did it, [mc]!"
$ cynthkiss += 1
jump academy




label cynthdate:
    show talkwamc
    mc "Ok I'm here."
    mc "Shall we go?"
    show talkwancb
    c "Where?"
    show talkwanmc
    mc "......"
    mc "Our date."
    c "When did I agree to that?"
    mc "......!"
    show talkwacb
    c "Hehehe, got you there didn't I?"
    c "Come on, let's go, I've been waiting all day."
    mc "......?"
    "You follow Cynthia out of the guild."
    stop music
    scene villageback with fade
    if theaguildjob == 1:
        c "I talked with Thea today."

        mc "{i}Shit!"
        c "She said you saved her from Yorkel."
        mc "Y-Yeah."
        c "I still find It quite hard to believe."
        mc "Hey, I'm not as weak as you think I am."
        c "I guess you aren't."
        c "Must be nice having her at your house?"
        mc "Huh?"
        c "A beautiful girl, doing all the house work for you."
        mc "......"
        mc "Is someone jealous?"
        c "Jealous! Me? Of her?"
        c "No!"
        mc "Hahaha!"
        c "Why are you laughing?"
        mc "You are clearly jealous."
        c "Whatever asshole."
        mc "Hey come on, you don't have to get mad."
        c "I'm not."
        c "......"
        mc "Don't worry you're still my only girl."
        c "God, how are you so cheesy."
        c "......"
        c "But it did make feel a bit better"
        mc "See. Being cheesy always works."
    scene cafe with fade
    play music happy
    "The two of you arrive at the cafe."
    "You get seated."
    scene cynthiadate1 with fade

    "The waitress comes to your table."
    "Waitress" "Oh, glad to see the two of you here again."
    "Waitress" "What will you be having."
    c "A cream cake and a coffee. [mc]?"
    mc "I'll have the same."
    "Waitress" "Alright, your order will be served soon."
    "The waitress leaves"
    mc "......"
    show cynthiadate8
    c "......"
    show cynthiadate7
    c "Today's a beautiful day isn't it."
    mc "Uhm... yeah?"
    c "......"
    mc "{i}She's acting very weird now."
    mc "What's up?"
    scene cynthiadate2
    c "Huh, nothing. Why?"
    mc "You're acting a bit weird."
    c "We're on date aren't we? This how I normaly act on a date."
    mc "Well, you can just be yourself I don't mind."
    c "......"
    show cynthiadate7
    c "But we're lovers now. I feel like we should talk differently to each other."
    mc "Like how?"
    show cynthiadate8
    c "I don't know, like calling me... \"honey\", or something."
    mc "Honey?"
    c "...Y-Yeah."
    mc "Would you like being called honey?"
    hide cynthiadate8
    c "Uhm, no."
    mc "...Then why should I?"
    c "I don't know, ok. I feel like something has to change between us, now that we're together."
    mc "Nothing has to change. You can just be yourself, it's ok."
    c "...Ah."
    c "......"
    c "But you need to know that I really do love you, [mc]."
    mc "I know."
    c "......"
    scene cynthiadate1
    "The waitress comes to your table with the food."
    "Waitress" "Here you go. Enjoy!"
    c "Let's eat then, shall we?"
    mc "Yeah."
    "The two of you start eating."
    mc "So, what are we going to do afterwards?"
    c "I thought we could hang out at my place."
    mc "Your place?"
    c "Yeah, at the guild quarters."
    mc "And do what?"
    c "I don't know... stuff?"
    mc "Well...ok."
    mc "{i}I wonder what kind of stuff she wants to do."
    mc "Cynthia, I was wondering."
    mc "You said I was your first lover, right?"
    c "Yeah."
    mc "and I was your first kiss?"
    c "Yeah, where is this going?"
    mc "Are you a... virgin?"
    scene cynthiadate3
    c "Oh my god, [mc]! That's where this was going?"
    mc "Whaaat? I'm just curious."
    c "You're a damn pervert!"
    mc "Yes, yes , I am."
    c "......"
    scene cynthiadate2
    c "Yes."
    mc "Mh?"
    c "The answer to your question is yes."
    mc "Oh."
    mc "{i}She's still a virgin. I'm going to be her first."
    c "What's with the creepy grin?"
    mc "N-Nothing."
    c "Dont act so cocky, it's not like you're any better."
    mc "Well, I might have a little more experience than a virgin."
    stop music
    play sound horror
    show cynthiadate9
    "Cynthia eyes stare down into your soul"
    mc "{i}Shouldn't have said that."
    stop sound
    c "Oh... So you say you're better? Are you some kind of sex guru?"
    mc "Uhm, n-no I didn't say that. Could you lower your tone a bit? others might hear us-"
    "Cynthia stands up and grabs your hand."
    c "Come with me."
    mc "Wh-Where?"
    c "To the guild. I'll have to put you in your place."
    mc "Huh?"
    mc "But we h-haven't paid yet."
    c "Put the money on the table."
    "You put the money on the table"
    scene cafe with fade
    "Cynthia drags you out of your seat."
    mc "My cream cake! I haven't finished it!"
    "Cynthia keeps dragging you out of the cafe."
    mc "{i}My cream cake, nooooo!"
    mc "What are you going to do to me?"
    c "Oh, hohoh... You'll see."
    mc "{i}I guess this is the end."
    scene agblr
    "She drags you to the guild and into her room. She pushes you in and closes the door behind herself."
    scene cynthiaroom with fade
    show worriedmc
    show normalcb
    mc "W-What's going on!?"
    c "Take off your clothes."
    mc "W-WHAT!"
    c "Didn't you hear me?"
    mc "B-But n-now?"
    c "Yes now. I can't let you disgrace me like that."
    c "Like I said, I'm going to put you in your place."
    c "You said you're a sex expert, lets see what you got."
    mc "I didn't actually say that."
    show normalcg
    c "Oh, looks like you were lying all along. Too scared?"
    #menu:
    "No!"#:
    show angry
    mc "No!"
    mc "Ok, if you're asking for it. I have no reason to refuse."
    "You take down your pants."
    mc "I shall become the sex demon that I am."
    show talkwahcb
    c "Hehe. That's more like it."
    scene cynthstrip
    window hide
    pause
    #    "I feel like I'm using you.":
    #        mc "I mean, this soon?"
    #        mc "I feel like I'm using you."
    #        c "......"
    #        c "Oh don't worry, [mc]."
    #        c "This is totally on me."
    #        scene cynthstrip
    #        window hide
    #        c "Think of it as me using you, if that makes you feel any better."
    #        pause
    #        mc "{i}gulp"
    #        c "Now take those damn clothes off."
    #        "You take off your clothes."
    $ persistent.cynthStrip = True
    "Cynthia stares down on you."
    c "Mh... not bad, [mc]"
    c "It's not the smallest I've seen."
    mc "......"
    mc "So you've seen a dick before?"
    c "What kind of question is that? Of course I've seen a dick."
    c "Do you know what the first thing most bandits do when they see me alone?"
    c "They pull out their disgusting, stinky cocks out, thinking that they'll get a chance to put in me."
    mc "Oh."
    scene cynthiaroom
    c "Come on."
    scene cynthsex1 with fade
    pause
    "Cynthia lies down on her red fur carpet."
    c "I don't have a bed so this is all we have."
    mc "Looks comfortable enough."
    c "It is. Now come here already."
    mc "so... We're going all the way, huh?"
    c "[mc], I'm lying naked here, of course we're going all the way."
    mc "Feels like we're moving fast."
    c "Hey, the day was going to end like this anyway."
    c "I just couldn't wait any longer."
    c "Now are you going to fuck me or do you need a formal invitation?"
    mc "If you say so."
    pause
    mc "Wh-What's that on your arm? Did you get hurt?"
    show cynthsex2
    c "Mh? oh this... it's nothing, a small bruise."
    mc "You can take those off."
    c "I-its better if I keep them on."
    mc "......"

    "You remove cynthias gloves, she doesn't resist."
    scene cynthsex21 with dissolve
    mc "C-Cynthia? Wh-What happened?"
    pause
    c "Disgusting isn't it."
    c "These are from Jemeila, the generals daughter."
    mc "What did she do to you...?"
    c "She used to beat me remember?"
    c "I only had my hands to defend myself."
    mc "......"
    c "I can put them back on if it makes you feel uncomfortable."
    mc "No don't. I don't mind."
    mc "I like to see all of you."
    scene cynthsex3 with dissolve
    c "......"
    scene cynthsex4 with dissolve
    c "Ahhh... Mhhh..."
    c "I've waited so long to feel this."
    mc "I'm going to start moving."
    c "Alright."
    c "[mc], I know this is my first time."
    c "But I don't want you to hold back on me,ok."
    mc "If you say so."
    show cynthsexanim movie
    pause
    c "Ahhh... shit..."
    mc "\"It's so tight!\""
    mc "You're... so tight..."
    c "Ahhhh... I bet... I can beat you in this too."
    mc "What...?"
    c "Ahhh... Let's... See who cums first."
    mc "Alright."
    pause
    c "Ahhhh... Ahhh..."
    c "Come on, faster..."
    c "You'll have to do better than that!"
    show cynthsexanimf movie
    pause
    mc "Ugh-"
    c "Fuck..."
    pause
    mc "You don't seem to be doing so good..."
    c "Shut... the fuck up."
    pause
    mc "It's ok... You... Can cum now."
    c "F-Fuck...!"
    c "I'm cumming!!!"
    scene cynthsex3 with flash
    show cumcynth
    mc "I win."
    c "Damn it."
    mc "......"
    show cynthsexanimf movie
    pause
    c "Ahhhh....wh-what are you doing!"
    mc "I didn't cum yet...."
    c "Ahhh... But I just... d-did!"
    mc "You said... Don't hold back."
    pause
    c "Ahh... Fuck me then...! Ahh..."
    mc "I'm going to cum."
    menu:
        "Cum inside":
            mc "Ahhhh!"
            scene cynthsexcumin with flash
            c "Fuuuck!"
            show cynthsex5
            c "You came inside."
            mc "Sorry I-I didn't have time to...."
            c "It's fine."
            c "I have a contraception spell on me."
            mc "Really?"
            c "Of course. It's essential for pretty girl like me."
            mc "Right."


        "Cum outside":
            scene cynthsexcumout with flash
            mc "Ahhhh!"
            c "Jeez you came all over me."
            mc "..."
            show cynthsex5
            c "I like it."
    scene cynthsex3 with fade
    $ persistent.cynthFirstTime = True
    c "[mc], I never expected you to be so..."
    mc "Say it."
    c "..."
    c "Experienced."
    mc "Hehe what did I say."
    c "So..."
    c "...Can we keep going?"
    mc "Oh, seems like you're already addicted to my dick."
    c "N-No."
    c "Ok, maybe a little."
    mc "But you'll have to wait. I just came."
    c "W-Why?"
    mc "Do you want me to fuck you with a limp dick?"
    c "Ohhh..."
    c "Hmm..."
    c "Oh wait!"
    scene cynthiaroom with fade
    "Cynthia gets up and hurrys to one of her desks. She takes out a bottle."
    "You recognise it imidiatly. It's Cynthia's special mix!"

    c "Drink up."
    mc "Will this work?"
    c "Only one way to find out."
    "You take a few sips."
    scene cynthiaroom with flash
    play sound gulp
    "As the liquid  pours down your throught you feel your body tighten. You feel a sudden burst of energy."
    c "It worked!"
    mc "Huh?"
    "You look at your penis. It's hard and throbing like crazy."
    mc "Shit! what the hell is this?"
    c "That doesn't matter."
    c "Just fuck me already!"
    show cynthsexanimf movie
    pause
    "The two of you start to make love."
    scene cynthsexcumin with flash
    pause 0.5
    scene cynthiaroom
    "Each time you ejaculate you take another sip of Cynthia's magic elxir and keep continuing."

    show cynthiaroomsex2 with dissolve
    pause 0.8
    "Hours pass, the two of you have no idea of stoping."
    hide cynthiaroomsex2 with dissolve

    show cynthiaroomsex1 with dissolve
    pause 0.8
    c "Ahhh... Shit...!"
    c "I've never felt this fucking great!!!!"

    hide cynthiaroomsex1 with dissolve


    pause 0.3
    scene cynthiaroomn with dissolve
    show cynthiaroomsex3 with dissolve
    "You keep going until night fall."
    pause
    hide cynthiaroomsex3 with dissolve
    c "Come on drink up already."
    "After your 20th or so ejacualtion you grab the bottle. You take it to your mouth but it's empty."
    c "Whats taking so long. Come on!"
    mc "We're out!"
    c "Huh!"
    mc "It's empty."
    c "Ahh shit!"
    c "That was my last batch."

    "Cynthia walks up to her hammock and falls into it."
    c "Fuuuuck! that was crazy!"
    "You join her."
    mc "Yeah. I dont think I've ever came so much."
    c "Heh. Now do you feel bad that you underestimated me?"
    mc "Oh yes. I would've grown a few extra dicks if had know."
    c "Haha Ewwwww!"
    mc "Hehe"
    c "..."
    c "I love you, [mc]."
    mc "..."
    mc "I love you too."

    scene black with fade
    "The two of you fall asleep."
    scene cynthiaroom with fade
    "You wake up next morning."
    show smilenc

    c "Hey you're up."
    show smilemc
    show talksadhappymc
    mc "Ye-Yeah. Man my back hurts."
    c "Your back hurts? I cant feel my entire lower body."
    mc "Hehehe"
    c "Here. I brewed some of my elixr."
    c "It'll make you feel better."
    mc "Ahh thanks."
    c  "......"
    show cryc
    c "Thanks, [mc]."
    mc "Hey...."
    hide cryc
    show talknc
    c "Ahh shit sorry, this came out no where."
    c "Ignore that."
    mc "Come here."
    "You hug Cynthia."
    c "Thank you."
    "The two of you finish your drinks."
    c "Lets go down then?"
    mc "Alright."
    scene agblr with fade
    "The two of you leave the guild quarters."
    show smilenc
    show smilemc
    mc "So anymore monster hunts?"
    c "Definitely!"
    c "I'll tell you when I find one."
    mc "Can't wait!"
    c "Alright. See you soon."
    mc "Yeah."
    show angryc
    c "Make sure you visit me often, ok!"
    mc "Yeah, yeah don't worry mi'lady."
    hide angryc
    "You wave Cynthia goodbye and go home."
    if theasex == 1:
        scene homeday with fade
        th "Ah, welcome home, [mc]."
        mc "{i}Shit!"
        mc "H-Hey Thea."
        th "You weren't home last night? Were you on a quest?"
        mc "Y-Yeah."
        th "You must be tired then. I'll make you some tea."
        mc "Uhm... That won't be neccessary. I-I already had something to drink."
        th "Oh. Ok then."
        th "I'm heading out to buy some fish from Uncle pete. He said he had a lot of salmon, he said it's your favourite."
        mc "Ah y-yeah."
        th "I'll be seeing you soon then."
        mc "Bye."
        mc "{i}Thea. God what am I going to say to her."
        mc "{i}This was your choice, [mc]. You'll just have to live with it."
    $ cynthdate += 1
    jump home
