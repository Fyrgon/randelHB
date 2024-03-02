default trissq1 = 0
default mettrissgq = 0

label trissq:
    hide screen hud
    mc "Is that Triss? What is she doing out here?"
    menu:
        "Ignore her" if trissheal == 0:
            mc "Better ignore her, I've got the feeling that she's bad news."
            "You slowly turn around and start to walk away."
            tr "Hey, you... newbie."
            mc "{i}Shit."
            mc "Uhm, y-yeah?"
            tr "Come here, will ya?"
            mc "{i}Got no choice here."
            scene forrest with fade
            show normalmc
            show normaltr
            show talksadhappymc
            mc "Yes?"
            tr "You're an Adventurer, right? I saw you at the Guild."
            mc "Yeah."

        "Talk to her":
            if trissheal == 1:
                mc "I should talk to her. I couldn't properly thank her for saving my life."
                show talksadhappymc
                show normaltr
                mc "Uhm...hello, Triss."
                tr "Ah it's you."
                tr "[mc], right?"
                mc "Yeah."
                tr "How are you doing?"
                mc "Feeling good. I think it's completely healed."
                tr "Glad to hear."
                tr "It's a good thing you're here, actually."
            else:
                mc "I should talk to her. If the things I heard are right, I might be able to score with her."
                scene forrest with fade
                show normalmc
                show normaltr
                show talksadhappymc
                mc "Uhm... hello?"
                hide talksadhappymc
                show talkwatr
                tr "Oh, yes! Just what I was looking for!"
                show talkwanmc
                hide talkwatr
                mc "Huh?"
                show talkntr
                tr "You're an Adventurer, right? I saw you at the Guild."
                hide talkntr
                show talkmc
                mc "Yeah."
    scene forrest
    show normalmc
    show talkwatr
    tr "Would you mind helping a senior out?"
    mc "Uh..."
    tr "Oh, sorry I asked. You HAVE to help a senior out."
    mc "What's that supposed to mean?"
    tr "You have to obey the senior's orders. That's how it works in the Guild."
    show talkwanmc
    mc "Ok, fine. I'll help you out. What do you want from me?"
    show talkntr
    tr "So, I'm on this quest... I have to find some Blood Butterflies. A village nearby has been hit by a sickness and I have to deliver as much of these butterflies as possible to make an elixir."
    tr "If you would help me, I'll be able to get a lot more of the butterflies as quickly as possible. The more we catch, the more elixir they can produce. It would help the town fight the sickness."
    tr "So, what do you say?"
    hide talkntr
    show talkwanmc
    mc "Hmm..."
    tr "Why don't we make this interesting; what you need is a little motivation."
    mc "Motivation?"
    tr "You look like you haven't been getting much action in this town, huh?"
    mc "What do you mean by \"action\"?"
    tr "Don't play dumb... what are you, five?"
    tr "You know what I mean."
    mc "{i}Gulp"
    tr "Why don't we do this; if you catch more butterflies than me, I'll reward you. That way, you'll put more effort into it and catch more butterflies for... the town, and also get rewarded in the end."
    tr "And I, well, will get a certain degree of satisfaction as well."
    mc "What kinda reward are we talking about?"
    scene trisstare with fade
    pause 1
    $ persistent.trissStare = True
    tr "Ooooh. Eager, aren't we?"
    tr "You'll see."
    mc "{i}Gulp."
    window hide
    pause 2.5
    tr "But don't except too much. I'm not some third-grade whore who gives away everything for a simple favor."
    mc "{i}What does that even mean?"
    tr "Got it?"
    mc "..."
    mc "Uhm... Alright."
    tr "Hehe. As expected."
    scene forrest
    show thinkmc
    show talkwatr
    tr "Nice. You'll have to get a bug net, though."
    mc "To catch the butterflies?"
    tr "Yeah. Just get it from Mervin."
    mc "Ok."
    tr "Come back here once you got the net. I'll be here in the afternoon."
    mc "Ok, got it."
    tr "Byeee!"
    scene forrest
    show normalmc
    mc "I have to get a net from Mervin. Man, she totally played me."
    $ sawtriss += 1
    $ trissq1 += 1
    jump forest


label trissq1:
    hide screen hud
    scene forrest
    show normalmc
    show talkntr
    tr "Oh, you're back. You got the net?"
    show talkmc
    mc "Yeah."
    tr "Good, we can start. We'll split up. That way we can cover more ground."
    mc "Yeah, that makes sense."
    tr "You go that way and I'll go this way. You know what a Blood Butterfly looks like right?"
    if chartrait == 1:
        mc "Yeah, it's a red butterfly with black tipped wings, right?"
        tr "Very good! Someone's done a lot of reading."
    else:
        mc "Uhm... I assume it's red?"
        tr "Ugh... Adventurers these days. Yes, it's a red butterfly with black tipped wings."
        mc "Ok, got it. Red butterfly."
    tr "Let's start then. Remember, you'll have to catch more than me if you want your reward. We'll meet back up here. Don't take too long, ok?"
    menu:
        "I'm just doing it for the people.":
            show talkwanmc
            mc "I'm just doing it for the sick people. It's what Adventurers do."
            show talkwatr
            tr "Ohh, sure, you are hero... Hehe..."
        "Ok, got it!":
            mc "Ok. Got it!"
    "The two of you split up to search for the butterflies."
    jump butterflyMinigameStart

label butterflyEnough:
    if bfly < 20:
        mc "{i}This should be enough."
    elif bfly < 50:
        mc "{i}I might've gone a little bit overboard."
    elif bfly < 100:
        mc "{i}I got... a bit too excited."
    else:
        mc "{i}I don't think these will all fit into my backpack... But the ones I can bring back are definitely enough."
    "You go back to meet Triss."
    scene forrest
    show normaltr
    show normalmc
    show talkmc
    mc "It's done."
    hide talkmc
    show talkwatr
    tr "Yay! Now, for the moment of truth. How many did you manage to get?"
    if bfly < 3:
        mc "I got [bfly]."
        show talkwatr
        tr "Wow... you didn't even try."
        mc "Well, I mean..."
        tr "Sigh... It's a shame, because I've got..."
    elif bfly <= 5:
        mc "I got [bfly]."
        show talkwatr
        tr "You did get a few, but... Eh, I hoped you'd try harder."
        mc "I did try."
        tr "Well, what's done is done. Now for the big reveal! I got..."
    elif bfly <= 20:
        mc "I got [bfly]."
        show talkwatr
        tr "Wow... you actually gave it your all, huh?"
        tr "Ok, now let's see, I got..."
    elif bfly <= 50:
        mc "I got [bfly]."
        show talkwatr
        tr "W-Wow... That's a lot."
        mc "Eh, could've gotten more."
        tr "I see... well then, now for the big reveal! I got..."
    elif bfly <= 100:
        mc "I got [bfly]."
        show talkwatr
        tr "..."
        tr "How did you..."
        mc "Determination."
        tr "Wow. Then I hope it won't make you mad to know that I got..."
    else:
        mc "I got [bfly]."
        show talkwatr
        tr "..."
        tr "How did you..."
        mc "I actually caught more but they didn't fit in my backpack so I freed them."
        tr "You... Wow. I'm genuinely impressed. I hope it won't make you mad to know that I got..."
    tr "None."
    show suprised
    show thinktr
    pause
    show angry
    mc "WHAT?!"
    show angrynmc
    show talkwatr
    tr "Congratulations, newbie! You won!"
    show talkwanmc
    mc "What about the competition?!"
    hide talkwatr
    if bfly < 3:
        tr "That was just to make you more interested... I guess it didn't work."
        mc "Well, I thought you'd get a few considering they're for ill people."
    else:
        tr "That was just to make you more interested. It worked like a charm!"
        mc "Ugh... At least it wasn't for nothing. I don't mind as long as it goes towards saving people."
    show talkwatr
    tr "Oh... about that... I completely lied."
    tr "I just wanted some Blood Butterflies to make a few health potions. I was feeling too lazy to catch them. Thank goodness you showed up, my hero! Haha."
    tr "Thanks to you, I can make a ton of health potions, and I didn't even have to lift a finger."
    show angry
    mc "So... the whole thing was a lie?!"
    tr "Yeah, hah.. Guys do anything if I get them riled up enough."
    mc "Just take them, I'm outta here."
    tr "Oh, so you don't you want your reward?"
    mc "Huh?"
    tr "I might be a liar, but I at least to try to keep my word."
    "Triss takes off her jacket. She takes off the buttons off her shirt to reveal..."
    show animationtriss
    pause 1.5
    scene flashtrissend
    pause 5
    mc "{i}Wow... those tits..."
    mc "{i}So bouncy, yet firm..."
    menu:
        "Touch":
            mc "{i}I... can't... resist...!"
            mc "{i}Must... feel...!"
            scene black
            play sound punch
            pause
            scene forrest
            show crazytr
            show worriedmc
            show blackeye
            $ gotpunchedtriss += 1
            $ punchtriss += 1
            tr "...Did you just try to touch me?"
            tr "You're out of your mind newbie."
            scene forrest
            show worriedmc
            show blackeye
            mc "Ah shit... my eye. I guess I pushed my luck too far..."
            $ trissq1 += 1
            jump forest
        "Resist":
            mc "Must... resist...!"
            scene forrest
            show talkwatr
            show normalmc
            tr "Good! You're an obedient little dog, aren't you? Well, that's enough fun for today."
            tr "Byeeee!"
            scene forrest
            show smilemc
            mc "{i}...I guess that wasn't a total loss then."
            $ trissq1 += 1
            jump forest
