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
        jump july3
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
            mc "{i}Sigh."
            mc "Ok."
            mc "And Eve was wrong, alright?!"
            j "Hehehehe. Ok, whatever you say."
            $ theaguildjob += 1
            jump guild

        "Ask about Lori" if loriEventValue == 4:
            call julyInfoDump
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
