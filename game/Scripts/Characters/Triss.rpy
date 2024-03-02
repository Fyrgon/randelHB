label trissTalk:
    scene trissroom with fade
    if trissq1 <2:
        mc "I don't have a reason to visit her."
        jump gquarters
    scene trissroom with fade
    if mettrissgq == 0:
        show thinkmc
        mc "{i}I should knock."
        play sound doorknock
        pause
        scene gqroomblr
        show talktrb with dissolve
        tr "Oh! Hi, newbie!"
        tr "What brings you here?"
        show normaltrb
        show talkhappymc
        mc "I just got my own room here, {size=-3}even though it's not finished,{/size} so I thought I'd visit my neighbors."
        hide normaltrb
        tr "Aww, how nice of you."
        if trissheal:
            tr "How did you like your reward, hero?"
        else:
            mc "I'm [mc]."
            tr "Oh yeah! I didn't get your name last time, did I? Hehe..."
            tr "I'm Triss, as you already may know."
            tr "How did you like your reward, hero?"
        menu:
            "It was ok.":
                show talkwamc
                mc "It was ok."
                show talktrb
                tr "Ooh, hehe... I know what you're playing, kid."
                tr "Playing the tough guy!"
                show talkwanmc
                mc "Yeah, right!"
                tr "I bet you've been fantasizing about me ever since!"
                mc "Urhm..."
                tr "It's ok, I'll permit it since you were such a good boy and helped me out, hero."
            "I liked it!":
                show talksadhappymc
                mc "I liked it!"
                tr "See? I'm glad. I bet you've been fantasizing about me ever since!"
                mc "Urm..."
                tr "It's ok, I'll permit it since you were such a good boy and helped me out, hero."
        tr "Do you like my night outfit?"
        mc "Uhm... it sure looks cozy."
        tr "It is! I made it myself, everyone at the Guild asked me to make one for them after they saw it!"
        mc "Are they that good?"
        tr "Yeah! Want one?"
        show talkwanmc
        mc "Uh... no, I'm fine."
        tr "Why? Because it looks girly? C'mon, even Sander got one."
        mc "That doesn't surprise or convince me."
        tr "You'll want it sooner or later, you'll see."
        mc "We'll see."
        tr "Nice talking to you, [mc], but I've got a lot of beauty sleep to catch up on."
        tr "Byeeee!"
        show talkwamc
        hide talkwanmc
        mc "Byeeee!"
        tr "Don't copy me."
        mc "Hehe..."
        $ mettrissgq +=  1
        scene trissroom
        jump gquarters
    scene gqroomblr
    show talktrb
    show normalmc
    tr "Oh, hi!"
    show normaltrb
    show talkhappymc
    mc "Good evening."
    hide normaltrb
    tr "So formal, Mr. Tough guy... Hehe."
    tr "So, what can I do for you?"
    menu:
        "Nothing.":
            mc "Nothing, I just came for quick visit."
            tr "Ahh, I see you needed your daily dose of Triss! Hehe! It's ok, I totally get it!"
            show talkwanmc
            mc "Urgh... whatever. Now I think I'm overdosing."
            tr "Byeeee!"
            scene trissroom
            jump gquarters
