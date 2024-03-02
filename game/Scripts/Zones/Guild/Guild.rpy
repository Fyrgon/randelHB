label guild:
    if time == 4 and sawjuly == 1:
        jump julypt2

    if TaliyaQ == 6 and Taliya6Talk == True and time == 3:
        jump TaliyaQ6

    if time > 3:
        scene villagen
        mc "It's too late to visit the Guild."
        jump maplimbo
    hide screen screenmap
    play music aguild
    show screen hud
    if time < 3:
        scene adventurersguild_day
    else:
        scene adventurersguild_evening
    call levellingUp from _call_levellingUp_10

    if thcynthconfess == 2 and time < 3:
        jump thcynth1
    if thcynthconfess == 3 and time == 3 and thcynthconfesstimer >= 3:
        jump thcynth2
    if thcynthconfess == 4 and time < 4:
        jump thcynth3



    if gabe2 == 1 and level >= 10 and gabequest2 == 0:
        play sound chime
        $ renpy.notify ("{color=#fff}New quest available!")

    if cynthmemloss == 1:
        hide screen hud
        mc "I should ask July about Cynthia."
        mc "July."
        j "Yes. What's the matter, [mc]."
        mc "Did you erase Cynthia's memories?!"
        scene adgc6 with fade
        j "......"
        mc "Tell me!"
        j "Yes."
        mc "Why!?"
        j "Because she forced me to."
        mc "Huh?"
        j "She told me everything about her, how she's suffered all her life."
        j "She said she couldn't take it any longer."
        j "She begged me to do it, [mc]. You have to understand."
        mc "I thought... I thought she was doing fine."
        j "She was struggling [mc], she was on the edge of giving up, I felt it."
        j "There was nothing I could do."
        mc "B-But."
        j "......"
        j "I'm sorry [mc]."
        j "But I think it was the best."
        j "She's free now. She doesn't have the dark past haunting her anymore."
        mc "......"
        "You leave without saying anything more."
        j "[mc]!"
        if time < 3:
            scene agblr with fade
        else:
            scene agblrevening with fade
        mc "{i}...She never showed it."
        mc "{i}But she was suffering. Why didn't I realize it? I could've stopped her."
        mc "......"
        mc "It's too late for regrets."
        $ cynthmemloss += 1
        jump guild

    if cynthquest5 >= 1 and cynthboots == 0 and time > 1 and sawjuly >= 5:
        jump PREcynthquest6

    if time == 4:
        scene agn
    if theasex == 1 and theaguildjob < 2:
        if time < 3:
            scene agblr
        else:
            scene agblrevening
        hide screen screenmap
        hide screen hud
        mc "I should ask July if Thea could get a job here."

    if theaguildjob == 3 and theaguild == 0 and time == 3:
        if time < 3:
            scene agblr
        else:
            scene agblrevening
        play music aguild
        hide screen screenmap
        hide screen hud
        mc "Thea must be at work now."
        mc "Let's see how she's doing."
        scene theaguild with fade
        "You spot Thea having a friendly chat with one of the Guild members while serving drinks. Her expression tells you that she likes her new job."
        "She sees you and rushes towards you."
        if time < 3:
            scene agblr with fade
        else:
            scene agblrevening with fade
        show smilemc
        show talkhth with easeinleft
        th "Hey, [mc]."
        show talkwamc
        mc "Hi. How are you liking your new job?"
        th "It's just amazing!"
        th "The people here are so nice, especially July."
        mc "I'm glad you're happy."
        "Can we get some drinks here?"
        show talksth
        th "Oh, I should get back to work."
        th "Do you want anything?"
        mc "Uhm, no, I'm good."
        th "Alright."
        "Thea gives you a kiss on the cheek."
        th "Bye, [mc]!"
        mc "B-Bye."
        "Let's go talk to July."
        scene adgc1 with fade
        j "Oh hey, [mc]. Your girlfr-"
        j "Sorry, I mean Thea is doing great."
        mc "I'm glad."
        j "Yeah, the Guild members love her. I should've hired a maid ages ago. Hehe."
        mc "It all worked out then?"
        j "Yes."
        scene adgc5
        j "Oh, and [mc], I'm keeping my eye on the Guild members. I'll steer away all of your competition away from her."
        mc "July!"
        scene adgc1
        j "Hehehe. I just can't help it. I love making you blush. Hihi."
        mc "{i}Sigh.{/i} Anyway, see you later."
        j "Buh-bye."
        $ theaguild += 1
        jump guild

    if ledricquest == 1 and evekiss == 0:
        jump EveQ2



    if aerinpath == 1 and dueldone == 0:
        jump evediary

    if level >= 10 and party == 1 and sawtriss == 0 and sawmegan == 0:
        if time > 3:
            mc "It's too late to visit the Guild."
            call screen screenmap
        hide screen screenmap
        hide screen hud
        play music aguild
        if time < 3:
            scene agblr with fade
        else:
            scene agblrevening with fade
        show smilese
        show smilemc
        show talksadhappymc
        mc "Oh. Hi, Eve. What's up? Had a party without me?"
        show talkhse
        hide talksadhappymc
        e "Oh, no, little one. Sander just had... a little drinking contest with Triss and, uhm, as you can see, he lost."
        hide talkhse
        sa "That b-bitch... I'll get her... n-next time. {i}hic"
        show talkhse
        e "You always say that, Sander. And you always lose."
        show talkwanmc
        mc "Who's Triss?"
        hide talkwanmc
        e "Oh. I think you haven't met her. She was out on a quest for about a month. She just returned yesterday."
        show talkwanmc
        mc "On a quest for a month?!"
        e "Yeah. She's a Diamond-Rank Adventurer so it's normal for her quests to take months."
        mc "A Diamond-Rank Adventurer?! Wow, never seen one before."
        e "Hehe, yeah, they're pretty rare. And they're always out on quest, so you don't see them that often."
        hide talkhse
        show talkhappymc
        mc "Hmm, I see."
        show talkow
        e "But I advise you to stay away from her, little one."
        scene trissshow with fade
        pause
        mc "Huh, why?"
        if time < 3:
            scene agblr with fade
        else:
            scene agblrevening with fade
        show talkow
        hide talkhappymc
        show talkwanmc
        e "She's, uhm, how should I say this? ...She's, uhm... inappropriate."
        mc "Inappropriate?"
        sa "She's a SLUT!!!"
        show talkow
        e "Sander! Keep it down!"
        show talkhse
        e "But yeah, he's not totally wrong. Haha."
        hide talkhse
        mc "Ah... Well, I'll keep that in mind."
        show talkmec with easeinleft
        m "Excuse me."
        show talkhse
        hide talkmec with easeoutright
        e "Oh, sorry, Megan."
        mc "What's her problem?"
        e "Oh, that's Megan. Always in a hurry."
        mc "Is she a Diamond as well?"
        e "No. She's a... Silver, I think. I really don't know much about her, honestly."
        mc "Really?"
        e "Yeah. Hehe. She doesn't talk much."
        mc "Hmm."
        e "Anyway, I'll go put Sander in his room."
        e "Hey, wait a minute... You're Bronze now, didn't you get a room at the Quarters?"
        show talksadhappymc
        mc "No... July said it's still under construction."
        e "Ohhh, I see. Anyway, you should visit us sometime."
        mc "Yeah, I should. I'll swing by sometime."
        e "That would be great. See you, little one."
        mc "Bye, Eve."
        $ sawtriss += 1
        $ sawmegan += 1
        jump guild




    if sawmegan == 2:
        if time > 3:
            mc "It's too late to visit the Guild."
            call screen screenmap
        hide screen hud
        hide screen screenmap
        jump meganq1

    if sawjuly == 2 and time <= 3:
        if time > 3:
             mc "It's too late to visit the Guild."
             call screen screenmap
        hide screen screenmap
        mc "There's July. I better talk to her."
        $ sawjuly += 1



    if askeve == 1:
        show normalmc
        mc "So I got Sander's approval. I should probably talk to Evelyn as well."

    if level >= 5 and checkboard == 0 and lvl5notif == False:
        $ lvl5notif = True
        mc "Yes! I reached level 5, finally! This means I can go on quests now. I'd better go check on the Quest Board."

    if icamping == 1 and sawcynth == 5:
        jump questcynth



    if saq < 1:
        hide screen hud
        if time < 3:
            scene agblr
        else:
            scene agblrevening
        call wotv1 from _call_wotv1_1
        if time < 3:
            scene agblr
        else:
            scene agblrevening
        show thinkmc
        mc "{i}What the hell...? How am I supposed to spy on girls without getting caught...?"
        mc "{i}{b}I could use a spell to make me invisible{/b} or something. I should ask Scarlet..."
        show worriedmc
        $ renpy.notify("{color=#fff}Quest started: The Way of the Voyeur")
        mc "{i}Ugh, I'm gonna regret this..."
        $ q1 += 1
        $ saq += 1
        jump guild

    if level >= 10 and party == 0:
        jump julyFollowed


    if day >= 5 and sawcynth == 4:
        hide screen hud
        show thinkmc
        mc "{i}Wait... is that?"
        show normalc
        show normalmc
        pause
        show normalcb
        c "Oh Astylla... it's this guy again."
        show talkwancb
        c "Can you stop following me?"
        hide talkwancb
        show talkwanmc
        mc "I wasn't following you."
        hide talkwanmc
        show talkwahcb
        c "Then why are you even here? Don't tell me you're an Adventurer."
        show thinkmc
        pause
        hide talkwahcb
        show talkwancb
        c "Oh no..."
        hide talkwancb
        show angry
        mc "Hey! I definitely joined the Guild way before you, ok!"
        show talkwahcb
        c "Oh, ok then, tough guy! What's your level?"
        mc "[level]"
        if level < 9:
            c "Pfttt! Hahaha! Still in level [level]? What a loser!"
            mc "Wh-What level are you in then?"
            c "Nine."
            show talkwanmc
            mc "Huh... B-But how?!"
            c "It's called skill, loser. Hah, bye!"
        elif level == 9:
            c "Tsk, still not impressive."
            mc "Wh-What level are you then?"
            c "The same as you."
            show talkwanmc
            mc "Huh... B-But how?! When did you even join the guild?!"
            c "Three days ago."
            mc "Wh- How?!"
            c "It's called skill, loser. Bye~!"
        else:
            $ cynthknowmcbronze += 1
            c "A Bronze, aye? Not bad for a total loser. I guess it's true that you've been here a lot longer than me."
            mc "What's your level?"
            c "9."
            mc "What?! Already? When did you join the Guild?"
            c "Three days ago."
            mc "Huh... B-But how?!"
            c "It's called skill. Hah, bye!"
        if time < 3:
            scene agblr with fade
        else:
            scene agblrevening with fade
        show angry
        mc "{i}Ugh... I hate her so much..."
        $ sawcynth += 1
        jump guild



    if sawcynth >= 6  and party == 1 and cynthquest2 == 0 and time == 2 and savecynth == 1:
        jump cynthFirstDate


    "You arrive at the guild."
label guildMenu:
    menu:
        "Talk" if time < 4:
            jump GuildTalk
        "Go to the Guild Quarters" if level >= 10 and party == 1:
            if time > 1:
                jump gquarters
            mc "I should probably visit them after noon when they aren't busy."
            jump guild
        "Check the Quest Board" if level >= 5:
            jump QuestBoard
