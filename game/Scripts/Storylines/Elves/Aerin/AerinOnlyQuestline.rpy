label evediary:
    hide screen screenmap
    hide screen hud
    play music aguild
    scene agblr with fade
    mc "There's July. I have to get the keys from her."
    scene adgc2 with fade
    j "Oh, hello there, [mc]."
    mc "Hey, July... Erm..."
    mc "Eve sent me to get some stuff from her room, she said she lost her keys. Do you have some spare keys for her room?"
    j "Of course I do! Here you go?"
    mc "Thank you?"
    mc "{i}That was easy."
    j "[mc], you're still in contact with Eve? Didn't she leave town? She never told me why."
    mc "Yeah... she has some personal issues. She's not that far away from town though, she said that she might be able to come back."
    j "Really? That's great news! Tell her that everyone at the Guild misses her."
    mc "I will, July. Laters! I'll give the key once I get Eve's stuff."
    j "Sure."
    scene agblr with fade
    mc "{i}I got the keys. Now it's time to go into Eve's room."
    scene everoom with fade
    "You unlock Eve's door."
    scene everoombook with fade
    mc "{i}Ok, now I have to find some clues. What kind of weapons she's weak against? What kind of fighting style she uses? Something that will tell me her weakness."
    mc "{i}I doubt I'll find anything."
    "You look around Eve's room. You search for a while but you find nothing."
    mc "{i}I should've known. Of course I can't find her weakness just conveniently lying around her for me."
    mc "{i}I should... make another plan."
    "Just as you are about to leave, you see a small red book on Eve's bed."
    mc "{i}Wait... what's this?"
    scene everoomblr
    $ sawevesroom += 1
    "You take the book and open it."
    "{color=#fff}Book" "Dururthu 23rd: Today I got a letter from the Village. It said that I should come to the Village immediately. I'm sure this has something to do with the duel."
    "{color=#fff}Book" "I stalled this enough. I think I should end this. I can't run away from this anymore."
    mc "{i}Wow, this is Eve's diary! She's 324, but still has a diary?"
    mc "{i}It kinda makes sense though. When you live for about 500 years, you are bound to forget things. I guess that's why she has one."
    mc "{i}Wait! I think I found what I was just looking for. Yes! This could have something about her weakness!"
    "You flip through the pages."
    "While you're going through the pages, your name catches your eye."
    mc "Huh, it's about me."
    "{color=#fff}Diary" "Today, a young boy named [mc] joined the Guild. It was so refreshing to see a small boy in the Guild after so long. I hope he does great..."
    mc "......"
    "You keep turning the pages."
    "{color=#fff}Diary" "[mc] came today and asked me if he could join our party. I was shocked. I'm sure Sander had something to do with this. I couldn't let the little one join our party; he's still inexperienced. What if he gets hurt?"
    "{color=#fff}Diary" "But looking at him, I saw myself when I was little. Eager for adventure, not a care for the danger that lies ahead. He said that he would do anything to prove himself. He was so adorable."
    mc "{i}I'm not adorable! I'm 19!"
    "{color=#fff}Diary" "So, I gave him a task of hunting three Alpha Falcons. It was the easiest thing I could think of, I just wanted to see if he was willing enough."
    "{color=#fff}Diary" "Today, the little one completed his task; he brought three Alpha Falcons. I was pretty impressed that he was able to do it so quickly, the boy has talent. So I told him that he could join. He was really happy to hear it, I could tell."
    "{color=#fff}Diary" "I can't wait for the adventures we'll have together."
    "{color=#fff}Diary" "Just came back from our first quest with [mc], we had a great time."
    "{color=#fff}Diary" "We ran into a group of goblins."
    if savedbyeve1 == 1:
        "{color=#fff}Diary" "The little one almost got killed by a Goblin and I had to save him. I knew it was too dangerous of a quest to go with a kid like him. If something would've happened to him, I don't know how I would've been able to live with myself."
    else:
        "{color=#fff}Diary" "The little one took out two goblins on his own. He was really stronger than I anticipated, he must have trained a lot."
    "{color=#fff}Diary" "We found the treasure we were looking for. Then we camped for the night. I caught Sander for the hundredth time peeping while I was bathing. And what's worst is he had brought the little one with him this time."
    "{color=#fff}Diary" "I was so embarrassed; the little one has no knowledge of these things, not like that pervert Sander. I hope I didn't taint the little one's mind. I had to teach them a lesson, so I had to give them a good beating."
    "{color=#fff}Diary" "We talked for a while at the fire after that. I learned a lot about [mc]. He's such an innocent child. I have this strange feeling, like I want to protect him, do what's best for him. I think it's what you call a motherly feeling. It's very strange indeed."
    mc "{i}Eve... I feel bad for doing this."
    mc "{i}Ok, enough of this. I must find something about Eve's weakness."
    "You keep turning pages and reading through them."
    "{color=#fff}Diary" "Went on a quest with Sander..."
    "{color=#fff}Diary" "Bought new boots for Sander's birthday..."
    "{color=#fff}Diary" "Made Milly a small bow..."
    "{color=#fff}Diary" "Helped July with work..."
    "{color=#fff}Diary" "Caught Sander peeping..."
    "{color=#fff}Diary" "Went to the Library. Drank tea with Lori..."
    "{color=#fff}Diary" "Caught Sander peeping... Accidentally  broke his jaw..."
    "{color=#fff}Diary" "Went to the Village and played with Milly..."
    "{color=#fff}Diary" "Hunted a night owl..."
    "{color=#fff}Diary" "Sander blew Rosa Flower pollen at me. Felt dizzy."
    "{color=#fff}Diary" "Sander caught a big boar today, it was delicious!"
    mc "{i}Wait!"
    "You turn back the pages."
    "{color=#fff}Diary" "Sander blew Rosa Flower pollen at me. He knows I'm allergic to it. Whenever those things reach my nose, I feel dizzy. That Sander's always messing around, I wonder when that man would grow up. But to be honest, having a childish companion is fun."
    mc "{i}Bingo! I could use this. She's allergic to Rosa Flower pollen."
    if chartrait == 1:
        mc "{i}Rosa Flower are those pink flowers. I read about them in the Plants of Astylla book. I think I might find them in the Outer Valley."
        mc "{i}So, what I have to do is find the flower and get the pollen. Then I'll use it on Eve just before the duel."
        scene black
        "You lock the door and give the key to July."
        $ time += 1
        $ aerinpath += 1
        $ knowrosa += 1
        jump guild
    mc "{i}What's a Rosa Flower?"
    mc "{i}Shit!"
    mc "{i}Wait... I could ask Lori. She reads a lot of books — she has to know."
    mc "{i}So, what I have to do is find the flower and get the pollen. Then I'll use it on eve just before the duel."
    scene black
    "You lock the door and give the key to July."
    $ time += 1
    $ aerinpath += 1
    $ askloriaboutrosa += 1
    jump guild



label aerinWinsDuel:
    mc "{i}Ok, Eve's right there. I just need her to smell the flower."
    mc "{i}Sniff... Mhh..."
    mc "{i}Got it."
    "You take the flower and get some pollen out of it. You brush them on your shoulders."
    mc "{i}Hope this works."
    "You run up to Eve."
    show normale
    show normalmc
    mc "Eve!"
    show sadtalke
    e "Oh, little one, the duel is about to start. You should go."
    mc "Yeah, ok, I came to wish you good luck."
    e "Thank you, little one."
    mc "......"
    scene duelarena with vpunch
    "You hug Eve tight."
    mc "{i}Sorry, Eve."
    e "[mc]?"
    mc "You got this, Eve!"
    "You head back to the Village people who have now all gathered and ready to witness the duel."
    "You see Aerin eyeing you suspiciously."
    "The both of them are now ready for battle. Zenelith stands in the center."
    zn "May the great four mothers bless the both of you. Let the duel begin!"
    scene elfduel with fade
    play music battlemusic1
    "You see Eve standing on her side of the arena, she looks like she can barely hold her balance, yet she still stands proud and ready."
    "The duel commences, the two girls go back and forth at each other, but swing after swing, Eve gets more and more tired. Aerin sees this and decides to take advantage of her opponent's weakness. She steps back."
    "And with one final swing of her sword, she manages to strike Eve directly, knocking her to the ground."
    stop music
    mc "{i}Aerin won!"
    mc "{i}I'm sorry, Eve..."
    "Eve and Aerin are taken to the temple."
    "You leave the Elf Village. You head to the Guild to tell Sander the news."
    scene black with fade
    pause
    scene agblr
    show talksads
    show talkmc
    s "Little man, wh-what happened?"
    mc "Eve lost."
    show worriedmc
    s "WHAT?!"
    mc "Yes. I think we should give her some time."
    s "You're right."
    s "Ngh! Fuck!"
    mc "{i}Sander looks upset... It's weird seeing him like this."
    hide talksads with easeoutright
    mc "{i}This was my choice. I knew what would happen, I just have to live with it."
    mc "{i}I should check on Aerin tomorrow."
    $ evelost += 1
    $ time = 4
    jump home


label aerinkiss:
    hide screen hud
    mc "I wonder how's Aerin doing, where do I even find her?"
    mc "I should ask one of the guards."
    "You walk up to the guard next to the temple's entrance."
    mc "Uhm, excuse me? ...Where I can find Aerin, the... Village Elder?"
    "Guard" "She's in the high elf's chamber."
    mc "Can I meet her?"
    "Guard" "What does the Elder want with a human?"
    mc "I-I'm a friend of hers, just tell her [mc] has come to see her."
    "Guard" "Fine."
    "The guard leaves. After a few minutes, she comes back."
    "Guard" "The Elder will see you. She's in the temple, on the fifth floor."
    mc "Thank you."
    scene highelfroom with fade
    $ sawaerinelder += 1
    scene highelfroom
    show smilemc
    pause
    scene highelfroomblr
    show happya
    show talkha
    a "You came!"
    show talkwamc
    mc "Of course I did! This place looks really great. It kinda suites you."
    a "Really!"
    a "Can you believe it? All the Elders before me sat on that exact place!"
    mc "It's pretty amazing."
    mc "So... what are you doing now?"
    show shytalka
    a "{i}Sigh...{/i} Work."
    a "It keeps piling up. Since... Zenelith is gone, I've got more work."
    mc "Don't worry, I'm here to help!"
    a "Really?"
    mc "{i}Now I have to argue my way to help her."
    show happya
    hide shytalka
    a "That's great!"
    mc "......"
    mc "{i}Ok, I was wrong."
    mc "Thank Astylla, I thought I would have to force you to let me help."
    show shytalka
    a "Oh, sorry! That's so rude of me. Hehehe... But I do need some help."
    mc "I'm glad to help. Let's get started then!"
    scene aerinworkhelp with fade
    "You help Aerin with her work. As expected, there was a lot of signing of papers, making records and reviewing records."
    "You get bored and mess around a bit."
    scene highelfroomblr with fade
    show smilemc
    show happya
    show talkha
    a "That's enough for today, [mc]."
    mc "Yeah, I'm tired too."
    a "From goofing around. Hehehehe."
    mc "Hey! I worked too, ok?"
    show shytalkha
    a "You did, you did. So [mc], would you... like to have a cup of tea at my house?"
    mc "Yeah, sure, that sounds good."
    scene aerinhouse with fade
    pause
    show smilemc
    show talkha
    a "I'll make some tea real quick."
    mc "Ok."
    scene teaaerin with fade
    "You have a cup of tea and eat Aerin's delicious muffin."
    scene aerinhouse with fade
    show happya
    show smilemc
    show blushtalka
    a "Uhm... [mc], can we talk?"
    mc "Yeah sure, about what?"
    a "Sh-Shall we go outside? We could use some fresh air. I have a balcony, we could go there."
    mc "Ok."
    scene mcatalkh with fade
    play music nurture
    mc "Whoah, this place is really nice."
    a "Thanks."
    mc "So, what do you want to talk about?"
    a "I just wanted to thank you, [mc]."
    mc "Huh? What for?"
    a "For caring about me. I still don't understand why you did it, but I wanted to thank you."
    mc "I really didn't do anything."
    a "You're talking to me, telling me that you would help me win. That meant so much to me."
    mc "Aerin..."
    a "I don't think I would be here if you didn't show up in my house that day."
    mc "......"
    a "I'm making you uncomfortable, aren't I? Hehehe. You really don't like getting praised, don't you?"
    mc "Hehehe, I guess."
    a "Ok, I'll stop then."
    mc "So... how's it like being the Elder?"
    a "It was everything I hoped for, but with the amount of work is a bit overwhelming, to be honest."
    mc "I could help you out with it, like I did today."
    a "Really?"
    mc "Yeah, I can... sort papers and stuff."
    a "Hehehe, that would be helpful."
    mc "{i}Aerin looks really happy. I know I had to betray Eve, but after seeing Aerin like this, I think it was worth it."
    a "[mc], there's something I should tell you."
    mc "What?"
    a "For a while, I've had this strange feeling about you..."
    a "It's something I've not felt before."
    mc "......"
    a "I think... I...{p}I think I love you."
    mc "...I feel the same way."
    pause
    scene mcak1
    pause 0.5
    scene mcak2
    pause
    scene mcak3
    pause
    a "......"
    a "Was that what you call a \"kiss\"?"
    mc "Yes. Haha..."
    a "......"
    a "H-Have you done it before?"
    mc "N-No, it's my first time."
    a "Really! I-I'm happy I was your first kiss."
    mc "Yeah, I'm pretty happy about that too."
    a "......"
    a "It's... getting dark."
    mc "Oh yeah... I-I should go."
    mc "{i}She must be embarrassed."
    mc "I'll go then."
    a "You are coming again, right?"
    mc "Y-Yeah, I'm coming to help, remember?"
    a "Oh, yes... Hahaha..."
    mc "Bye."
    a "Bye."
    $ time = 4
    "You head back home."
    jump home
