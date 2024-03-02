label nessa1:
    scene jail
    show normaln
    show smilemc
    show talkhn
    n "Hello, [mc]."
    show talksadhappymc
    mc "Hey."
    show talkwan
    n "Say, [mc], has your stay here been pleasant so far?"
    show talkwanmc
    mc "Yeah, sure. Why do you ask?"
    n "The Village people haven't bothered you in any way, have they?"
    mc "No... Matter of fact, I think they're trying their hardest to ignore me."
    n "Hahahaha... That is exactly what I wanted to hear."
    mc "What do you mean?"
    n "Oh, it's just that I've ordered the Village folk to keep their distance from you."
    mc "Why the hell would you do that?!"
    n "I said that you have a sexually transmittable disease."
    show angry
    show wan
    mc "WHAT?!"
    hide wan
    n "Look, I know you're angry at me, but I did it for your own good."
    mc "Can you please explain how this is for my own good?"
    n "Alright, alright, you see, most of the women here are horny lunatic nymphos that'd go wild at the sight of a man."
    n "And if you walk in here with that dick hanging around like that, do you have any idea what would happen?"
    mc "{i}I'd be in heaven?"
    n "You'd die. They'll fuck you until your dick fell off."
    show suprised
    mc "...C'mon, t-they aren't that desperate..."
    n "They haven't seen a dick in 200 years, [mc]."
    hide suprised
    mc "I guess you do have a point."
    show thinkmc
    n "See, you should listen to what I say, I'm always right."
    show sedtalkn
    n "Besides, we have to protect that dick at all costs!"
    show talkwanmc
    mc "Huh?"
    show talkblushn
    n "Hehehehe."
    hide sedtalkn
    $ metnessajail += 1
    jump nessatalk


label nessa2:
    scene jail
    show normaln
    show smilemc
    show talkhn
    n "Oh, yes! You're here!"
    mc "Uhm... H-Hi."
    show sedtalkn
    n "[mc], there's something I've been craving since you got here."
    show talkwanmc
    mc "My dick?"
    n "...Is it that obvious?"
    mc "Uhm... yeah."
    show talkwamc
    mc "So, let's fuck."
    n "Ohhh... No, I can't."
    hide talkwamc
    mc "{i}Of course, it isn't that easy. There always has to be some sort of grind."
    n "Not like this. I could do it right now, but that would ruin the experience. I need to savor it more. Like, I need to work my way to it, you know?"
    mc "Huh?"
    n "It's no fun when you get things without earning them."
    mc "Ok, so what do you want me to do?"
    n "Not you, me!"
    mc "{i}This girl is making no sense."
    n "Give me some sort of task... and for my reward... you can fuck me."
    show suprised
    mc "{i}Wait a minute, this is a reverse grind! What the fuck?!"
    hide suprised
    mc "So you do something for me and I get to fuck you as well?"
    show hornn
    n "YES! YES!"
    show talkwamc
    mc "{i}Makes no sense, but I like it."
    mc "Ok, so why not suck my cock and I'll reward you with a good fucking?"
    n "Not something like that, idiot. Hehehe. Something that doesn't involve... sex stuff."
    mc "Ok."
    mc "{i}So it's my time to choose a grind. Oh, how the tables have turned."
    menu:
        "Bring me 200 gold":
            mc "Bring me 200 gold."
            n "Yes, that's it! Consider it done."
            n "Ohhh... I'm so excited, just thinking about it makes me wet!"
    mc "O-Ok... good luck then."
    $ nessaquest += 1
    jump elfVillage

label nessa3:
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
        n "Here's your 200 gold. Now take off your clothes!"
        scene black
        "The both of you get undressed."
        n "I can't believe I finally get to do it!"
        pause
        n "I'm going to put it in now."
        scene nessasexstart with fade
        pause
        n "Ahhh... This is the B-B-BEST!"
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
