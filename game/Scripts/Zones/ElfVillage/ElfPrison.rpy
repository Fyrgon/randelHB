label elfPrison:
            if time == 4:
                mc "I can't get in there now."
                jump elfvillage
            stop music
            hide screen hud
            if metnessajail == 0:
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
                n "The village people haven't bothered you in any way, have they?"
                mc"No... Matter of fact, I think they're trying their hardest to ignore me."
                n "Hahahaha... That is exactly what I wanted to hear."
                mc "What do you mean?"
                n "Oh, it's just that I've ordered the village folk to keep their distance from you."
                mc "Why the hell would you do that?!"
                n "I said that you have a sexually transmittable disease."
                show angry
                show wan
                mc "WHAT?!"
                hide wan
                n "Look, I know you're angry at me but I did it for your own good."
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

            if savedaerin == 1 and nessaquest == 0:
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
                n "Not like this. I could do it right now but that would ruin the experience. I need to savor it more. Like, I need to work my way to it, you know?"
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
                mc "{i}Makes no sense but I like it."
                mc "Ok, so why not suck my cock and I'll reward you with a good fucking?"
                n "Not something like that, idiot. Hehehe. Something that doesn't involve... sex stuff."
                mc "Ok."
                mc "{i}So it's my time to choose a grind. Oh how the tables have turned."
                menu:
                    "Bring me 200 silver.":
                        mc "Bring me 200 silver."
                        n "Yes, that's it! Consider it done."
                        n "Ohhh... I'm so excited, just thinking about it makes me wet!"
                mc "O-Ok... good luck then."
                $ nessaquest += 1
                jump elfvillage
            scene jail
            show normaln
            show smilemc
            show talkhn
            n "Hello, [mc]."
            hide talkhn
            show talksadhappymc
            mc "Hey."
            hide talksadhappymc
            show talkhn
            n "What brings you to this dark prison today?"
            jump nessatalk
