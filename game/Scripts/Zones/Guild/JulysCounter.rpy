label JulysCounter:
    if sawjuly == 3 and time < 3:
        scene adgc6
        mc "July, abou-"
        j "Not now... Let's talk in the evening. It's too crowded right now."
        mc "Ok."
        $ sawjuly += 1
        jump guild
    if sawjuly == 3 and time == 3:
        $ sawjuly += 1
        scene adgc7
        mc "So... That was you?"
        jump yesThatWasMe
    if time == 3 and sawjuly == 4:
        scene adgc7
        mc "Is it ok now?"
        scene adgc6
        j "Yeah."
        scene adgc7
        mc "So, that really was you?"
        label yesThatWasMe:
        scene adgc6
        j "Yes."
        scene adgc7
        mc "Does anyone else know?"
        scene adgc6
        j "No... it's only you."
        scene adgc7
        mc "How did you manage to keep it a secret for so long?"
        scene adgc6
        j "That trap door under the bear rug? You shouldn't be able to see that."
        mc "Huh?"
        j "I put an illusory barrier around it."
        mc "Illusion barrier?"
        j "It hides the trap door, only I can see it. I don't know how you managed to find it."
        j "The barrier must've weakened..."
        scene adgc7
        mc "What are you doing here? If you're not even going to feed on people, why would you integrate into a community like this?"
        scene adgc6
        j "Because I promised someone I'd take care of the Guild."
        mc "Who?"
        j "Why don't you take a seat, [mc]?"
        mc "{i}Oh boy, this might take a while..."
        "You pull up a chair and get seated."
        j "You know vampires are immortal, right?"
        mc "Y-Yeah?"
        scene adgc5
        j "I've been taking care of the Guild since it was first built."
        scene adgc7
        mc "What?! You mean for..."
        scene adgc5
        j "290 years."
        scene adgc7
        mc "......"
        mc "Why are you so attached to this place?"
        j "Do you know who founded the Guild?"
        mc "Uhm..."
        scene adgc5
        j "It was a man called Mark Gregory."
        mc "Oh."
        j "When I was little, I was hunting in the forest. It was a pouring that day."
        j "I was chasing this deer. And suddenly, there was a mudslide. It came at me out of nowhere, I had no time to react."
        j "I was trapped in there for... I don't know... maybe weeks?"
        j "I was slowly dying from starvation. Then one day, a man saved me. Mark dug me out of the mud with his own hands."
        j "He took me to his home and fed me, and took care of me knowing what I was."
        j "Mark was an adventurous man, he didn't like settling down and farming like other folk in Randel. He was always out there exploring."
        j "He had the idea of making an Adventurer's Guild here in Randel."
        j "While I was living with him, I knew I wouldn't have been alive if it wasn't for Mark and his adventurous spirit. If he stayed a farmer and never ventured out to the woods, I would've died under that mud."
        j "He inspired me to promise, to never harm a human being. Over time, as I was living in Randel, I began to love humans."
        j "Finally, Mark built the Guild, which was way more successful than either of us expected."
        j "A lot of young people joined the Guild, and before we knew it, we had a whole group of adventurers."
        mc "Wow."
        j "He grew up and I stayed the same. It felt like such a short time. He taught me how to blend in with humans and showed me how to run the Guild. When he became too old for adventuring, he put me in charge of the Guild. He was like a proud father that day."
        j "He knew I could run the place the way he wanted and knew I could do it... forever.{p}His... last words to me were to protect the Guild and keep the adventuring spirit alive."
        mc "And you've been here ever since?"
        j "Yeah..."
        mc "But hasn't anyone realized you have been here for... 290 years?"
        j "I can change my appearance. I'm actually pretty good at illusions despite your keen insight that night... When you saw me, that's what I really look like."
        mc "So, you change your appearance and start over as a new person?"
        scene adgc2
        j "Yeah! I put my new self in charge and the old me just \"retires\" and leaves town."
        scene adgc1
        mc "Ohhh, smart."
        j "......"
        scene adgc6
        j "Is there anything else you want to ask me, [mc]?"
        mc "What happened last night? You suddenly collapsed."
        j "Oh, I couldn't thank you enough for putting me in my casket... I normally fall asleep at that time."
        mc "Like, completely get knocked out?"
        scene adgc2
        j "Hehe, yeah. I spend a lot of energy staying up during the day. Almost as soon as it gets dark, I fall asleep."
        mc "So that's why you said you wanted to talk the next day..."
        scene adgc5
        j "Yes... which you kindly accepted."
        scene adgc1
        mc "Heh... I'm really sorry, July."
        scene adgc2
        j "I don't mind... I know it must have been shocking."
        mc "Yeah, it was..."
        if notrustjuly == 1:
            j "It was cute seeing you all serious, trying to kill me. Hehehe. You know I could've killed you with one swipe, right?"
            mc "{i}I really did try to kill her. What was I thinking?!"
        else:
            scene adgc2
            j "But you trusted me in the end, [mc]. I'm really grateful."
            mc "Hehe... It's nothing."
        j "Can you promise me you won't tell this to anyone?"
        mc "Don't worry, July. I promise."
        j "Thank you, [mc]. Please don't let this change things between us."
        scene adgc1
        $ sawjulyvampire += 1
        mc "Don't worry, it won't. July is July, human or vampire."
        scene adgc2
        j "Awww! Thank you so much, [mc]!"
        $ sawjuly += 1
        jump guild
    hide screen hud
    scene adgc2 with fade
    j "Hello there, [mc]. May I help you with something?"
    scene adgc1 with dissolve
    jump qj



label qj:


    menu:
        "A job for Thea" if theaguildjob < 2 and theasex == 1:
            mc "Hey, July, I was wondering if there were any jobs available in the Guild bar. "
            mc "Like, for a waitress."
            j "Hmm, the Guild bar doesn't really have a waitress. They just get the drinks themselves."
            j "Having a waitress does sound like a good idea. Who is it for, [mc]?"
            mc "For a friend of mine."
            j "Is it for Thea?"
            mc "Yeah."
            mc "Wait, how did you know?"
            j "Eve told me."
            mc "Oh..."
            j "Alright then, tell Thea she got the job."
            mc "......"
            mc "Aren't you going to say anything?"
            j "Hmm... about what?"
            mc "I didn't even get to tell you about Thea."
            j "Well, you didn't tell anything to me because you don't trust me enough, right? I can totally understand."
            mc "Wait! July, it's not like that, I-"
            j "Heheheh. I'm just messing with you, [mc]. Eve told me all about it."
            j "You just didn't want to deal with competition, right? I heard she's a looker."
            j "That's a very smart move, [mc]."
            mc "What?! No! That's not it either."
            j "Hehehehe. You tell your little friend that she can come in the evenings."
            mc "{i}Sigh"
            mc "Ok."
            mc "And Eve was wrong, alright?!"
            j "Hehehehe. Ok, whatever you say."
            $ theaguildjob += 1
            jump guild


        "When can I go on quests?":
            j "When you reach level 5. Until then, hunt wild boars or slay monster to gain experience. "
            jump qj
        "Can I slay other monsters?":
            j "You can. Just be careful, most of them are very dangerous. Be sure you are trained enough with your sword and bow before you do."
            j "Also, you should study about these monsters before slaying them. Go to the Library and find The Book of Monsters and study the monsters to find their weaknesses."
            jump qj
        "Where can I get new equipment?":
            j "There's a trading caravan just outside the Guild. You can buy equiment from there."
            jump qj
        "No more questions":
            mc "No more questions. Thank you!"
            j "Bye!"
            jump guild
