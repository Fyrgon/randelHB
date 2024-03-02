label ZenelithEncounter:
    hide screen hud with fade
    play music lake
    mc "I'm starting to get accustomed to the sights of the Outer Valley. It feels so weird that I hadn't been in them that often when I was a kid, they're honestly not even that much of a problem to traverse without encountering monsters..."
    "And just as you say that, you hear the rustling of some leaves on your right. You stop and turn around."
    scene direwolf with vpunch
    play music battlemusic1
    mc "OH FUCK-"
    "The lone wolf growls at you and starts getting closer. You can feel its bloodlust just by the air around you: it's going to attack."
    "You have two choices: Either run and hope you are faster than a 4-legged monster, or fight and hope you are stronger than a Direwolf."
    menu:
        mc "{i}Damn it... What do I do?"
        "Fight":
            $ ForestSaved = True
            mc "{i}C'mon [mc]! You're a Bronze-Rank Adventurer! A single Direwolf won't be a problem!"
            "You ready your sword, putting it between you and the direwolf. You're not going down without a fight."
            "Suddenly, the Direwolf jumps towards you. It's way faster than you imagined, but, more importantly, it's way more agile."
            "The wolf dodges your sword and with a quick motion it bites into your neck. You feel the air leaving your lungs as your vision slowly goes black."
            stop music fadeout 2
            scene black with fade
            mc "{i}Guh..."
            mc "{i}Is this it...?"
            "You feel the blood flowing out of your neck. The time it's taking to pass out and die is surprisingly long."
            if metFGirl == False:
                    "Then the wolf wails, and everything goes quiet."
                    "You feel a hand on your neck, and before you pass out, you manage to hear one last thing."
                    "{color=#fff}???" "You town folks..."
                    pause 2
                    play music night
                    scene forrestn with fade
                    "You slowly wake up. It's night and your neck still kinda hurts."
                    mc "I'm... alive?"
                    mc "...I'm alive! Hahah!"
                    mc "I have no idea how, but I'm alive!"
                    "You look around yourself and you see nobody, yet when you touch your neck you feel some bandaging that wasn't there before."
                    "You get up, and ponder for a second calling for whoever helped you, but after the encounter with the Direwolf, you decide it's better to stay quiet."
                    mc "{i}Guess I'll have to find my way back..."
                    "You being walking through the woods."
        "Run":
            mc "{i}...I think I might be able to outrun it. Maybe it'll even leave me alone if I get out of its territory..."
            if cynthtrain >= 6:
                mc "{i}Cynthia trained me well enough for this."
            scene forrest
            "Then, you start running."
            "As you're discovering while traversing the forest, running in the woods isn't exactly the easiest thing to do, especially if half of the trees have branches at the height of your face."
            "And especially so if there's a direwolf right behind you."
            "Yet, somehow, you are still alive."
            mc "{i}I want to call this a success, but I still need to get out of here-"
            "Suddenly, the trees end."
            "Actually, not just the trees. The ground below you has disappeared as well."
            "The direwolf stays still on the edge of the cliff as you fall to what seems like a very likely death."
            pause 1
            mc "AAAAHHHHHHHHHHHHHH!!!"
            stop music fadeout 2
            "You fall for what seems like an eternity, but was most likely just three stories. The tress are nice enough to soften your fall by hitting you with their branches in the stomach a few times before you hit the ground."
            mc "Ugh... Damn it..."
            scene black with fade
            pause 3
            play music night
            scene forrestn with fade
            "You slowly wake up. It's night and your head hurts like crazy, just like the rest of your body."
            mc "—Fuck... That hurt."
            "You get up and look around yourself. The dark isn't helping you in your attempt at finding a way back home."
            mc "{i}Guess I'll have to find my way back some other way..."
            "And with that, you quietly start walking through the forest, hoping to at least find a better place to put down camp."
    "After a few minutes you see something in the distance. It seems like there's a campfire up ahead."
    play sound campfire
    scene zenelithfire3 with fade
    mc "What the-"
    zn "Wh- YOU!"
    scene zenelithfire3blr
    "The elf priestess quickly gets up, the rags she's using as clothes barely covering her body almost falling off because of the sudden movement."
    play sound magic
    "She points her hand at you and shoots a magic spell, yet when it reaches you, the remains of Scarlet's shield seem to be enough to deflect it back at her."
    $ gameover = "zenelithchoice"
    label zenelithchoice:
        scene zenelithdown with vpunch
        "Zenelith falls back on the ground, and despite her attempts at getting back up, it seems like she's too weak to even lift her own weight."
        mc "...How the mighty have fallen."
        zn "You ape... You're lucky I am weak, or else you'd be dead..."
        "The two of you stand silent for a moment. You open your mouth, but Zenelith is quicker to talk."
        if RapeZen == True:
            zn "What are you going to do now? Are you going to violate me again?"
            mc "...Hah, no, not exactly."
        zn "...A-Are you going to kill me then?"
        mc "{i}Am I?"
        mc "{i}She's an awful person, but is that enough to kill her? She hasn't killed anyone herself... Maybe there's another way?"
        mc "{i}Killing is wrong, I know that, she's not a demon, but..."
        label zenencountermenu:
        menu:
            "Save her" if bothpath >= 4:
                jump ZenelithWholesome
            "Kill her":
                jump ZenelithMurder
            "Punish her":
                jump ZenelithSlave
    return





label ZenelithMurder:
    play music dark
    $ killZen = True
    $ evil += 1
    mc "{i}Think straight, [mc]! She's evil, if I let her go like this she will just keep doing what she's been doing all this time!"
    mc "Yes, I am."
    zn "..."
    #scene zenelithcamp_resigned
    "You raise your sword above her head. For a moment you hesitate."
    zn "I'm sor-"
    "And then you strike."
    scene forrestn with vpunch
    #scene zenelithcamp_death
    ### maybe a scene that's all red and then there's the characters silhouettes drawn all black. Maybe there's like the MC with his sword in front of him and a headless body in front of him.
    mc "..."
    mc "Ngh-"
    #scene zenelithcamp_corpse
    ### Just Zenelith's corpse
    "You put a hand in front of your mouth, trying to stop yourself from puking. You quickly turn around and start walking away without turning back."
    scene black with fade
    "And you keep walking."
    scene adventurersguild_day with fade
    "You arrive at the Guild in the early morning, there's barely anyone around. July waves at you, but you ignore her."
    mc "{i}I need to talk with Eve..."
    "You go up to the Guild Quarters."
    scene everoom
    "{i}Knock knock"
    mc "..."
    mc "Maybe she's not here..."
    #scene morningeve
    ### It could be nice to have a scene with Eve opening the door here, but it's fine if it's not here.
    "Eve opens the door."
    show eve
    show prot sad
    e @skeptict "[mc]? What are you doing here this early?"
    mc "..."
    mc @sadt "I found Zenelith."
    e @angryt "What?! When? Where?"
    show eve angry
    mc @sadt "Tonight, in the forest... I..."
    e @angryt "What?"
    mc @sadt "I... killed her."
    e @smilet "That's gr-"
    show eve
    scene everoom
    show eve
    show prot sad
    pause 2
    e @sadt "...Are you ok?"
    mc @sadt "I've never... I've never killed someone like that."
    mc @sadt "She looked so... helpless..."
    #scene evehug
    ### This scene is a bit more important. We need Eve comforting the MC for this.
    e @hopet "You did the right thing."
    mc @sadt "But..."
    e @smilet "No buts."
    e @angryt "She was evil. Maybe you didn't know Aerin's brother, but I did, and he was the sweetest person in the village, the least deserving of being enslaved for 160 years."
    e @angryt "She made the village suffer."
    e @sadt "...Did you get any sleep?"
    mc @sadt "No..."
    show eve smile
    e @smilet "Come inside, you can sleep in my room, it's alright."
    stop music fadeout 3
    mc @sadt "Thanks Eve, I'm... so tired... of everything."
    "Eve caresses your hair."
    e @hopet "Go in and rest, you'll feel better afterwards."
    scene everoomnight with fade
    "Eve lets go of you and you sluggishly walk to the bed."
    "You immediately fall asleep."
    scene black with fade
    play music lake
    e "Hey, [mc]"
    show everoomin with fade
    "After a few hours, you wake up. Eve is sitting on the bed with a gentle smile on her face. She seems worried."
    show everoomblr
    mc "Good morning, Eve..."
    e "It's already evening."
    mc "What- How long did I sleep?"
    e "Just the entire day, I've seen worse."
    mc "{i}Sigh..."
    e "How are you feeling?"
    mc "I don't know... I'm still confused."
    mc "But I think you're right, it was the right thing to do."
    e "Heh, good to know you're feeling a bit better."
    e "Sander was worried sick."
    mc "That feels very out of character from his part."
    e "You don't know him as well as you think. He can be more than the goofy guy... He was really worried."
    mc "Tell him I'm sorry for worrying him."
    e "Oh, no, I can't. I wasn't supposed to tell you he was actually worried."
    mc "Hah, alright then."
    e "Well, now it's time to go home, [mc], I kinda need that bed."
    mc "{i}Ah, right, I'm in her bed."
    menu:
        "Alright":
            mc "Alright. Good night, Eve."
            e "Goodnight, [mc]."
            g "And remember: you did the right thing."
            mc "I will."
        "It's not like I'd mind having you here next to me":
            mc "It's not like I'd mind having you her-"
            e "Get out before I decide to kick you out myself, [mc]"
            mc "Alright, alright! I'm going."
            e "...Take care."
    $ zenRouteEnd = True
    $ day += 1
    $ time = 2
    jump home
    return
