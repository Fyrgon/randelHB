default eveTalked = 0

label evelynGuildTalk:
if eveknow == 1 and evesex == 0:
    show blushsadtalke
    show worriedmc
    e "I-I'm sorry, little one. It's better if we stopped seeing each other for a while."
    hide blushsadtalke with easeoutright
    mc "Eve, wait!"
    mc "{i}Urgh, Eve's ignoring me. I have to talk to her somehow."
    mc "{i}I'll talk to her at the Guild Quarters. She won't be able to run away from me then..."
    mc "{i}Right?"
    jump guild
if evelosttimer < 3 and evelost == 1:
    mc "Eve isn't here."
    jump guild
if evelosttimer < 7 and evelost == 1:
    show sadtalke
    show worriedmc
    show talksadhappymc
    mc "How... are you doing, Eve?"
    e "...I'm doing fine, little one. Thank you for asking."
    mc "Remember, we're always here for you, ok?"
    show sadhtalke
    e "I know, little one. Thank you."
    jump guild
hide screen hud
if time < 3:
    scene agblr with dissolve
else:
    scene agblrevening with dissolve
show talkhappymc
show smilee
mc "Hello!"
hide talkhappymc
show smilemc
show talkhe
e "Oh, hello, little one! What brings you here?"
menu:
    #"Talk" if evequest > 0:
        #mc "Just wanted to talk."
        #e "Oh alright, come in then."
        #scene everoomin with fade
        #if eveTalked == 0:
        #    ""
        #    $ eveTalked += 1
        #    jump guild
        #if eveTalked == 1:
        #    ""
        #    $ eveTalked += 1
        #    jump guild
        #if eveTalked > 2:
        #    ""
        #    $ eveTalked += 1
        #    jump guild
    "Guess who'll be joining your party soon?" if askeve == 1:
        jump swta1
    "Ok, I did it." if alphafalcon >= 3 and greenarrow ==1 and evequest == 0:
        jump swta3
    "I'm ready, let's go." if level >= 10 and sequest1 == 0:
        if swordlvl < 6:
            mc "{i}Wait, if I'm gonna go on a quest with these guys, {b}I better train a bit more.{/b}"
            mc "{i}I've gotta show that I have what it takes to be in their party."
            jump guild
        jump cavetresureq
    "Nothing!":
        hide talkhe
        show talkhappymc
        mc "Just came by the Guild, thought I would come see you."
        show talkhe
        hide talkhappymc
        e "How nice of you!"
        hide talkhe
        show talksadhappymc
        mc "Talk to you later then! Bye!"
        jump guild





label evelynGuildQuarters:
scene everoom
if aerinlost > 0:
    play sound doorknock
    "...{p}..."
    "You still can't believe she's gone beacause of you."
    jump gquarters
elif evelosttimer < 3 and evelost == 1:
    mc "{i}I should give her some time."
    jump gquarters
elif evesex == 1:
    play sound doorknock
    e "Come in, little one."
    show everoomin with fade
    show smilee
    show smilemc
    e "What brings you here?"
    menu:
        "Wanna sleep together?":
            show talkwamc
            mc "I thought we could spend the night together?"
            show blushtalke
            e "Ohh... did anyone see you come in?"
            mc "I don't think so."
            e "Good. Let's get to bed then."
            if loveeve == 1:
                show evesex movie with fade
                e "Aaahhh..."
                mc "I love you, Eve."
                window hide
                pause
                e "Aaahh... Aaahhh..."
                mc "I'm going to cum!"
                scene evesexcum with flash
                pause 0.1
                scene evesexcum with flash
                pause 0.1
                scene evesexcum with flash
                scene evesleep2 with fade
                e "I'm so lucky to have you, little one."
                scene black with fade
                "You wake up the next day and leave the room without waking Eve."
                $ time = 0
                call sleepvars from _call_sleepvars_15
                jump guild
            show evesex movie with fade
            e "Aaaahhh... Fuck me harder, little one!"
            window hide
            pause
            mc "Your pussy is the best!"
            e "Aahhhh... aaahhhh... so... good!"
            mc "You're addicted to my cock, aren't you?"
            e "...Yeeeesss...!!!"
            mc "I'm going to cum... take it, slut!"
            e "Cum inside meeeeeeeee!!!"
            scene evesexcum with flash
            pause 0.1
            scene evesexcum with flash
            pause 0.1
            scene evesexcum with flash
            scene evesleep1 with fade
            e "Aaaaahhhh... cooooooock..."
            scene black with fade
            "You wake up the next day and leave the room without waking Eve."
            $ time = 0
            call sleepvars from _call_sleepvars_16
            jump guild
        "About us..." if thcynthconfess >= 3 and toldEve == False:
            $ toldEve = True
            mc "Eve? I think we need to talk about the two of us for a second..."
            e "What's wrong, [mc]?"
            mc "Well..."
            mc "I have been sleeping with Cynthia and Thea as well besides you."
            e "Oh."
            mc "I'm so sorry for cheating on you, I know it's bad and I-"
            e "[mc]."
            mc "...Yes?"
            e "You... don't know, do you?"
            mc "Know what?"
            e "Us elves... We're polyamorous."
            mc "Poly-what?"
            e "It's normal for elves to have multiple partners, it's not really seen as something bad in our culture..."
            mc "Wait what?"
            e "Yeah, so... Uh... I don't really mind, little one."
            mc "...Thanks, Eve."
            e "It's alright, little one. I thought you already knew honestly."
            mc "Heh, it's good to know then."
            jump guild
        "Nothing":
            mc "Just wanted to check how you're doing."
            e "I'm doing just fine, little one."
            mc "Good to know. Bye, then."
            e "Hehehe. Bye."
            jump guild

##### EVENTS
if savedaerin == 1 and evemillyquest == 0:
    jump EveQ1pre
if evemillyquest == 1 and ledricquest == 0:
    jump EveQ1transition
if evekiss == 1 and eveknow == 0:
    jump EveQ3
if eveknow == 1 and evesex == 0:
    jump EveQ4


##### Pre Quests
play sound doorknock
"...{p}..."
mc "{i}Huh... It seems she's not home."
jump gquarters


##################################
#####  Eve's Village House   #####
##################################

label evelynHouseTalk:
menu:
    "Your empty house":
        show talkwamc
        mc "Why does your house look kinda empty? There's almost nothing here except for those beds and that table."
        hide talkwamc
        show talkwae
        e "What did you expect, [mc]? I don't really spend much time here and neither does Milly. So, this place was kinda abandoned."
        mc "Oh yeah, right, that makes sense. Totally forgot about that."
        jump eveHouse

    "You and Sander":
        show talksadhappymc
        mc "Something's been bugging me for a while."
        show sadhtalke
        e "What is it, little one?"
        mc "You and Sander... are you guys..."
        e "What?"
        mc "Like dating or something?"
        e "Dating?"
        mc "{i}Of course. She doesn't know what dating is. How do I make this make sense to her...?"
        mc "Uhh... I guess \"In love\"?"
        show blushtalke
        e "What? Nooo way! Hahahaha! What made you think that we were?"
        mc "Well, it's just that since the two of you are, well, always together and do almost everything together, I just thought it made sense that you two were dating..."
        e "It's nothing like that, little one. We're partners and that's all there is to it. And besides, I don't think Sander has a romantic side to him at all. He's just a pervert most of the time."
        mc "Oh, I see. Hahaha."
        show blushtalke
        e "Don't worry, little one.  I'm still a maiden and I don't plan on changing that anytime soon."
        jump eveHouse

    "About Milly":
        mc "So Eve, can you tell me a bit about your sister?"
        show talkhe
        hide blushtalke
        e "What do you want to know?"
        mc "Well, for starters, what is she like?"
        show talkwae
        hide talkhe
        e "Hmm, let's see... Well, she's really smart, that's for sure. And she is very curious too. She really likes hearing about all of my adventures and the outside world."
        e "I guess it's fascinating for her since she can't leave this Village."
        mc "Why can't she leave the Village?"
        e "You see, [mc], a priestess is magically bound to her Village. Therefore, she can never leave it, or else the spell bounding her to it would be broken."
        mc "And what would happen if it did get broken?"
        e "That's something you'll find out another day, little one."
        mc "Alright, I won't ask again. But I don't get why she became one then."
        e "Well, it's not exactly her choice. See, a priestess is chosen at birth from each generation. And it's always the last born that becomes the priestess or priest, so Milly had no choice."
        mc "So she's the last in the generation?"
        e "Yeah."
        mc "So... Uhm, what happens next? If there are no men left in the Village, I mean, will it just eventually die out?"
        e "Yeah..."
        mc "That's really sad... and unfair."
        e "It's nature, little one, everything has to come to an end one day."
        mc "Hmm... you're right."
        mc "I guess Milly must be really lonely then, being the last born of the whole generation..."
        show sadtalke
        e "Yeah, the few born of the last generation are a bit too young to be her friends. I try to come here every day but sometimes I can't make it when I'm on quests and I feel very selfish most of the time."
        e "You know, for leaving her alone here and all, while I explore the beauties of the outside world and have fun on quests."
        mc "But you try your best to come here every day, right?"
        e "I do."
        mc "And that means you care about her and I think that's what matters the most."
        e "Thank you, [mc]. Look at you giving this 300-year-old elf lessons about life."
        mc "Heh, I guess I'm pretty wise, aren't I?"
        show talkhe
        e "You sure are."
        mc "But why \"Milly\"? ...It doesn't exactly sound like an elf name."
        e "You noticed, didn't you?  I was the one that named her. It's not exactly an elvish name. You see, Milly was a very dear friend of mine that I met in Dermis. And out of respect for her, I named my sister Milly."
        mc "That's nice, she must've been a really good friend."
        e "She really was."
        jump eveHouse

    "About the Priestess":
        show talkwamc
        mc "What can you tell me about the hag?"
        hide talkwamc
        show talkwae
        e "...The Elder Priest, Zenelith, you mean?"
        hide talkwae
        show talkwamc
        mc "Oh yeah, right, that's her name."
        hide talkwamc
        show talkwae
        e "Sigh... Well, little one, she's the oldest elf in the Village and the only elf alive of the sixth generation."
        e "She directs all of our ceremonies and oversees all the events that happen in the Village... Which includes the duel. She's also in charge of keeping records of the Village history... She's just as important as the elder."
        mc "What about her personality?"
        e "Well, little one, let's say she is... Strict."
        e "She doesn't really have any friends in the Village. She's the last living member of the sixth generation and the only one who didn't give birth to any of us of the seventh generation."
        mc "She was the only one of her generation who didn't generate offspring?"
        e "Yes and after all the men died, she accepted her clan duty to become the priestess."
        e "Nobody really knows how she was before becoming priestess but she was probably just as \"strict\" before becoming the priestess."
        e "But after all being strict is the job of the priestess. She needs to keep our traditions alive, so it's not really bad that she's this way."
        mc "I see. Thanks Eve!"
        e "No problem, little one."
        jump eveHouse

    "Leave":
        mc "That's all, I'll be leaving now. Make sure to get some rest."
        e "Okay, [mc]. Thank you for the visit!"
        jump elfvillage
