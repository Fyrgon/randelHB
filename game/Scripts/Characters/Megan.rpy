label meganTalk:
    scene meganroom with fade
    if meganq1 < 1:
        mc "I don't have a reason to visit her."
        jump gquarters
    if metmegangq == 0:
        scene meganroom with fade
        show normalmc
        play sound doorknock
        pause
        scene gqroomblr
        show drunknmb
        show smilemc
        m "Oh. [mc], right?"
        show talkmc
        mc "Yeah."
        hide talkmc
        show talkwanmc
        mc "Wait, are you drunk?"
        show talkdrunkmb
        m "Me...? Noooo..."
        mc "You are."
        m "Ok, maybe I am... a little... or a lot..."
        m "What do you want?"
        m "You wanna talk about what happened?"
        mc "Huh... urhm... yeah, kinda, I guess."
        m "{i}Sigh...{/i} You knew, kid."
        show angry
        mc "What?"
        m "You knew I was drunk, and you took the opportunity to make me spill the beans!"
        mc "No, how could I kno-"
        show suprised
        m "Shut up! I'll tell ya. No one has talked to me in a while so I'll tell ya."
        hide suprised
        mc "Ok then, if you say so..."
        scene gqroomblr
        show thinkmc
        show talkdrunkmb
        m "I was born in a small town near Randel... {i}hic{/i} ...on a cold night, if I remember correctly..."
        mc "{i}Oh boy... this is gonna take a while."
        m "My family was small. My mother died when I was little, so I grew up with my father and my two brothers."
        m "My father was a street brawler; he used to earn money by beating people in fights... on the street... brawling."
        m "Obviously, my two brothers took after him. Before I knew it, I was living in house full of macho brawlin' types!"
        m "My brothers and I used to play... and by play, I mean we would beat the living shit out of each other... I guess growing up like that made me strong."
        m "Then I joined the Academy. I was a really cheerful person. I loved hanging out with my new friends."
        m "But all of that changed. When we had our trials, I would always come out on top by miles. I could beat up every single one in the Academy, even the seniors!"
        m "People slowly started to hate me! My friends ignored me, and in the end... they just became my enemies."
        m "You know, not having friends is ok, as long as you don't have enemies. But having enemies, that's the worst! Especially when they used to be frenemies... wait... no, they used to be friends then enemies... Anyway!"
        mc "{i}That's depressing..."
        m "So I graduated from the Academy. Then I left town, and got to Randel, and joined the Guild. That's when I thought not to stand out. If I did, everyone would hate me again."
        mc "I think you were being paranoid."
        m "Jealousy... it's always there, Monty!"
        show angry
        mc "Monty?"
        hide angry
        m "I mean... [mc]?"
        mc "Ok, go on."
        m "So I decided to reinvent myself as an assassin... No one would really care about me. I could just be ignored and no one would hate me again."
        mc "{i}That's why she's still a Silver-Rank adventurer. She could be the top adventurer in the Guild with her skills."
        mc "...But wouldn't that make you lonely?"
        m "Having no friends is better than having enemies! So, I had to be an assassin... and be invisible... and stuff."
        m "And I fucking suck at it!"
        mc "{i}Yeah, no kidding."
        m "Every time I get caught. And when I get caught, I just get this urge to just-just-"
        show talkwanmc
        mc "Go berserk?"
        m "Exactly!"
        mc "Then why don't you just stop being an assassin?"
        m "Nope... I can't."
        mc "You're thinking too much about your past."
        m "No-no, I just can't. It's better this way. I'm still new in the Guild. And if I start being serious, all the seniors would hate me just like before..."
        mc "......"
        m "Anyway! Nice talking to you, Ben! I had to get that off my chest."
        mc "{i}Ben?"
        mc "Uhm... Yeah, you too, good talk."
        m "Ok, good- {i}hic{/i} -night!"
        mc "Goodnight."
        $ metmegangq += 1
        scene meganroom
        jump gquarters
    scene gqroomblr
    show smilemc
    show talkhappymc
    mc "Hello."
    hide talkhappymc
    show talkmb
    m "Hello, [mc]."
    m "What is it?"
    menu:
        "Oh nothing.":
            m "Let me guess, \"nothing\"."
            show talkhappymc
            mc "Hehe, yeah..."
            m "Hehe. You're kinda weird, [mc]."
            m "I like it!"
            mc "Thanks, see ya."
            m "See-ya!"
            scene meganroom
            jump gquarters
        "Were you the one at the tavern?" if theaguildjob >= 1:
            mc "Hey, were you the one who punched that guy at the tavern?"
            m "Hmm... What guy?"
            mc "It was you!"
            m "Yeah, yeah, it was me."
            mc "Thank you. He would've beaten me to a pulp if you didn't show up."
            m "Naaah, you could've taken him on."
            mc "What?! You really think so?"
            m "Yup. Size doesn't always matter, you know."
            mc "Huh. You're just trying to make me feel better."
            m "Noooo."
            mc "What were you doing there anyway?"
            m "Drinking. What else?"
            mc "But that place is shit."
            m "Yeah. I tend to like shitty things."
            m "The place reminds me of my hometown."
            mc "Your hometown must have been a tough place then."
            m "Hehehe, yeah."
            mc "Well, thanks for the help, Megan."
            m "Anytime, kid. You did good standing up for that girl."
            mc "Th-Thanks, see you later."
            m "Bye."
            jump gquarters
