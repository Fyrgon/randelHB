label gabeBeginning:
        hide screen hud
        scene academytalkblr with fade
        show smilemc
        pause 0.4
        show talkshgabe with easeinleft
        g "Hey [mc], wait up!"
        g "Are you going home?"
        hide talkshgabe
        show normalgabe
        show talkwamc
        mc "Yeah, why?"
        show talkshgabe
        g "Well, I thought we could walk home together."
        show talksadhappymc
        mc "Oh... ok, sure."
        show talkshgabe
        g "You don't mind stopping at the library on our way, do you?"
        mc "No problem."
        show talkgabe
        g "Nice! Let's go then."
        scene villageback with fade
        play music happy
        pause
        show smilemc with easeinright
        show talkwagabeop with easeinright
        pause 0.8
        g "So... what have you been up to lately?"
        scene villageback
        show talkhappymc
        show talkwagabeop
        mc "Hmm? Oh, well..."
        mc "I joined the Adventurer's Guild."
        show talkshgabeop
        g "Really! That's great."
        g "Finally, your dream came true, huh?"
        mc "Hehe, yeah."
        g "Remember how you were really into adventurers back then?"
        mc "I was. Do you remember how we used to play adventurer when we were little?"
        g "Oh yeah! ...You were the adventurer and I was the-"
        mc "Evil witch!"
        g "Hehehe, yes!"
        pause
        g "Oh look, it's Uncle Pete."
        show unclenormal with easeinleft
        show smilemc
        show normalgabeop
        show uncletalk
        u "Hey, kids."
        hide smilemc
        hide normalgabeop
        show talkshgabeop
        g "Hi, Uncle Pete."
        u "I must say, seeing the both of you together sure brings back memories."
        mc "{i}Uncle Pete, please don't say anything stupid."
        u "So where are you two heading?"
        mc "We're going back home."
        show sadtalkuncle
        u "Oh yes, it's already pass noon! I really lost track of time."
        mc "Where are you going, Uncle Pete?"
        u "Oh... just nowhere, taking a small stroll. It's something us old people do."
        g "Heheh."
        u "Alrighty... be on your way then, I won't take up your time."
        hide uncletalk
        show talkshgabeop
        g "Bye, Uncle Pete."
        u "Bye, my dear."
        hide sadtalkuncle
        hide unclenormal with easeoutright
        pause 0.4
        show petethumbsup with flash
        play sound chime
        pause
        mc "{i}Uncle Pete, what are you doing?!"
        mc "{i}Thank Astylla Gabe didn't see that."
        hide petethumbsup
        scene villageback
        show talksadhappymc
        show talkwagabeop
        g "Let's go to the library."
        mc "Yeah."
        stop music fadeout 4.9
        scene libraryblr with fade
        show smilemc
        show normalgabeop
        pause
        show talkhl with easeinleft
        l "Gabe!"
        g "Hi, Lori!"
        mc "{i}Of course, they know each other."
        l "I see you brought [mc] with you."
        show talkwagabeop
        g "You've met?"
        if loritea > 3:
            l "Oh yes, [mc] here is a regular customer."
        else:
            l "Yeah, he came the other day to ask for the Book of Monsters."
        if chartrait == 1:
            g "I guess you're finally taking books by yourself."
            mc "I told you I wasn't the lazyhead anymore."
            if loritea > 3:
                mc "Lori also helps me with my Astyllian."
        else:
            g "Really, now."
            if loritea > 3:
                mc "Lori helps me with my Astyllian."
        g "Oh, that's great."
        show talkhsl
        if loritea > 3:
            l "I had a lot of free time, so I thought I would help [mc] with his studies."
            g "Hmm, you did say you always liked teaching."
            l "Heh, yeah."
        l "Go on then, you don't need my help going through the library."
        g "Thanks, Lori."
        hide talkhl
        hide talkhsl with easeoutleft
        show talkshgabeop
        g "She's really kind, isn't she?"
        scene libraryblr
        show talksadhappymc
        show normalgabeop
        mc "Yeah, but I have to admit that the first time I came here, she almost threw me out."
        show talkwagabeop
        g "What, why?"
        mc "Ahh... She thought I came to the library to hide from the guards or something."
        g "Hahaha... Yeah, you really don't look like the reading type."
        mc "Huh? What does that mean?!"
        g "I'm just saying that you look... Dumb."
        scene libraryblr
        show angry
        show talkshgabeop
        mc "HEY!"
        g "Hahaha... I'm kidding, I'm kidding."
        mc "...I don't look dumb."
        show talkwagabeop
        g "Jeez, I said I was kidding."
        mc "......"
        show talkwanmc
        show talkgabeop
        mc "What book are you looking for anyway?"
        g "A Herbarium."
        if chartrait == 1:
            mc "Learning about plants?"
            g "Yeah."
        else:
            mc "A what?"
            g "Ugh... a book about plants."
            mc "Oh... you could've just said that."
        g "I think it should be on the right corner there."
        scene library1 with fade
        show normalmc
        show talkgabeop
        g "It should be here somewhere."
        hide talkgabeop
        show normalgabe
        "Gabe scans through the bookshelf."
        show talkshgabe
        g "It's not down here, must be on the top shelves."
        g "Hold the ladder for me, will ya?"
        show talkmc
        mc "Sure."
        show cutegabeu
        g "...And keep your eyes down, ok?!"
        show talkwanmc
        mc "Eh?"
        g "No peeking!"
        mc "Uhm... you do realize that you're wearing pants, right?"
        show cutegabe
        g "But it's still embarrassing."
        hide cutegabe
        mc "Ok, ok, fine."
        scene library1 with fade
        show normalmc
        "You hold the ladder tight. Gabe slowly climbs up and starts to look for her book."
        if chartrait == 1:
            show talkwanmc
            mc "Why are you looking for a Herbarium?"
        else:
            show talkwanmc
            mc "Why are you looking for a book about plants?"
        g "I'm studying about potions. And to make them, I need herbs. That's why."
        mc "Oh."
        mc "What kinds of potions?"
        pause
        g "Hmm?"
        mc "What kinds of potions are you making?"
        g "Different types of potions; health potions, mana potions, invisibility potions."
        show talkwamc
        mc "You make invisibility potions?"
        g "Y-Yeah... Well, I haven't made any yet, but I know how. Why?"
        mc "Nothing, it just sounded interesting."
        g "Yeah, potions are really cool."
        show smilemc
        hide talkwamc
        mc "{i}An invisibility potion does sound cool. I wonder whether it lasts longer than the spell?"
        mc "..."
        mc "......"
        hide smilemc
        mc "Did you find it yet?"
        g "Still looking."
        show normalmc
        mc "..."
        mc "......"
        mc "{i}Should I take a peek?"
        menu:
            "Yes":
                show blushsmilemc
                mc "{i}Just a small one."
                g "Whoa!"
                hide blushsmilemc
                show talkwanmc
                mc "Huh?"
            "No":
                show angrynmc
                mc "{i}Noooo. What the hell am I thinking?"
                g "Whoa!"
                hide angrynmc
                show talkwanmc
                mc "Huh?"
        play sound punch
        scene library1
        show normalmcbook with vpunch
        pause 0.5
        hide normalmcbook with hpunch
        pause 0.3
        scene black with fade
        mc "Ugh..."
        pause 3
        play sound campfire
        mc "..."
        mc "......"
        play music windhowl fadein 4.1
        "Female Voice" "Wake up!"
        show dreamg1 with fade
        pause 0.5
        hide dreamg1 with fade
        "Male Voice" "He's already dead!"
        show dreamg1 with fade
        pause 0.1
        hide dreamg1 with fade
        pause 0.03
        show dreamg1 with fade
        pause 0.1
        hide dreamg1 with fade
        "Female Voice" "No... he's still breathing."
        show dreamg1 with fade
        "Male Voice" "We were too late, he's gone."
        "Female Voice" "No!"
        show dreamg2 with dissolve
        mc "Uh... Who?"
        mc "Gabe?"
        stop music
        stop sound
        scene libraryblr with flash
        show worriedgabe
        show normall
        g "[mc]?"
        l "Is he ok?"
        g "He's waking up!"
        scene libraryblr
        show worriedmc
        show sadgabe
        show normall
        mc "Ugh... my head..."
        show talknl
        l "Are you ok?"
        show talkwanmc
        mc "Y-Yeah... what was that?"
        g "I'm so sorry [mc]! My hand slipped and the book fell."
        show talkwanmc
        mc "That was a book?!"
        mc "Felt like a brick!"
        l "Are you sure you're ok?"
        mc "My head's still ringing a bit."
        g "Sorry, [mc]..."
        mc "It's ok."
        mc "Ow..."
        mc "Did you find the book at least?"
        g "Yeah... that's... the one that fell on your head."
        mc "Oh."
        show normalgabe
        show talkhl
        l "Hehehe."
        mc "Can we go now then?"
        g "Ok, let's get you home."
        l "If your head still hurts tomorrow, come tell me. I'll fix you some herbal tea."
        show talksadhappymc
        mc "Ok. Thanks, Lori."
        g "Bye, Lori."
        mc "See you, Lori."
        l "Bye, guys."
        scene villageback with fade
        g "Are you sure you're ok? You were out for about half an hour."
        mc "Yeah, I'm fine."
        "The two of you reach Gabe's house."
        show talkhappymc
        show normalgabe
        mc "We're here."
        show talkshgabe
        g "Yup."
        mc "See you tomorrow then."
        g "Yeah..."
        g "You should visit your old friend sometime."
        show thinkmc
        mc "...?"
        show talkwamc
        mc "Uhm... I could come in now, if you want. I don't have anything planed for the evening."
        show sadgabe
        g "N-Now?"
        g "But my place is a mess now."
        mc "It can't be that bad."
        g "It kinda is."
        mc "Alright, tomorrow then."
        show worriedblushdgabe
        g "I didn't say you couldn't come. If you don't mind the mess, today's fine."
        mc "Oh, ok then, lead the way."
        scene gaberoomd with fade
        mc "{i}I guess this is what a \'mess\' looks like to her."
        show talkwanmc
        show sadgabe
        mc "You weren't kidding when you said it was a mess."
        show talksgabe
        g "I'm really sorry, I just had a lot of work piled up lately."
        show talkwamc
        mc "I'm just messing with ya. If you saw my place, you'll probably throw up."
        show talkshgabe
        g "You're telling me it can get messier than this?"
        show thinkmc
        mc "......"
        mc "You're kidding right?"
        g "What?"
        mc "Uhm... Nevermind, forget it."
        show smilemc
        show blushgabe
        mc "......"
        g "......"
        show talksadhappymc
        mc "The... place looks the same as I remember it."
        hide talksadhappymc
        hide blushgabe
        show talkshgabe
        g "Does it?"
        g "Yeah, I guess it is."
        show blushgabe
        mc "......"
        g "......"
        "There's an awkward silence in the room."
        hide blushgabe
        g "So, what do we do now?"
        show talksadhappymc
        mc "I don't know. Hehehehe."
        g "When we were little, we always used to play when we got together. But now it feels kinda weird, because we've grown up and all."
        mc "Yeah..."
        g "Well, let's do what grown-ups do then."
        show talkwamc
        mc "What?"
        g "Talk."
        mc "Ok, about what?"
        show cutegabe
        g "Uhm..."
        show cutegabeu
        g "I got nothing."
        show talkwagabe
        show talkhappymc
        "[mc] and Gabe" "Hehehehe..."
        g "Being a grown-up is damn boring."
        mc "Hmm."
        g "I wish we could play like we used to."
        show talksadhappymc
        mc "Wanna play \"Home\"?"
        show talkwagabe
        g "\"Home\"? ...Oh shit, I remember. We used to play as a family."
        g "I was the mother and you were the father."
        mc "And our son?"
        g "Uncle Pete! Hahahaha... he used to play as our son."
        mc "Little Pete."
        show talkshgabe
        hide talkwagabe
        g "It's so embarrassing when you think about it now."
        mc "Yeah."
        g "Those days were fun though."
        mc "They were."
        show talksgabe
        g "Why does life have to get so boring when you grow up?"
        show talksadhappymc
        mc "Well, I'd say it gets... more complicated."
        show talkshgabe
        g "I guess you're right. But at least you get some fun, being an adventurer."
        show talksadhappymc
        mc "I guess I do. Don't you like being an adventurer?"
        g "Uhm... not so much. Don't get me wrong. I love going on adventures, but I'd rather be a mage of Westian."
        show talkwamc
        mc "...So you chose your life to be boring?"
        hide talkwagabe
        show cutegabeu
        g "Being a mage isn't boring. Well, the process of becoming one is. It takes a lot of work."
        g "But after becoming a mage, it's super cool."
        scene gaberoomd
        show angrygabeblush
        show talkwanmc
        mc "Super cool?"
        show talkwagabe
        g "Yeah! You get to experiment with all sorts of magical arts!"
        show talkwamc
        mc "That does sound fun, but it's too much work for me."
        show talkwagabe
        g "That's why you're a lazy head."
        hide talkwamc
        mc "I'm not lazy!"
        g "Yes you are. Tell me, did you at least start studying for the test?"
        mc "...The test?"
        show talksgabe
        g "Wait, you don't know?"
        mc "Uhhh, no?"
        show yellgabe
        hide talksgabe
        g "Come on [mc]! Do you even pay attention in class?!"
        if historyClass < 2:
            g "...Nevermind you barely show up anyways."
            mc "I'm just busy with all the adventuring stuff, is all."
        else:
            mc "Ehhh, not really. I'm focusing on the whole adventurer stuff, y'know."
        show cutegabeu
        hide yellgabe
        g "You better start studying then, you wouldn't want to repeat the year, would you?"
        mc "...Repeat the year?"
        g "Yeah. You gotta pass the exam if you want to pass the class."
        show suprised
        mc "B-But the year just started? Aren't we supposed to only have a test each three months?"
        hide suprised
        g "Yeah, I know, it's a pain in the ass. But it seems the new King passed a new law and now we have to do even more tests and if you fail even just one you're out."
        show talkwamc
        hide talkwanmc
        mc "I guess I'll just be an adventurer then..."
        show talksgabe
        g "You can't be serious, [mc]! I mean no offense, but most adventurers die before they have enough money to retire. At least don't close off your other possibilities."
        show talkwanmc
        mc "You think being a soldier is better?"
        hide talksgabe
        g "Right now? Definitely."
        g "Adventurers are the only ones who constantly deal with threats to sustain themselves. A soldier might get deployed in the west, never see a demon in their life, rank up enough to never see the frontline again, and retire at 40."
        g "And since we're not poor, we don't have to stop after the first year of Academy. If we go through the whole three years we'll be immediately assigned as Captains!"
        g "Sure, Gold-Rank adventurers get a lot of money, but you know how long and how dangerous it is to get there? I mean no offense, but it's a slim chance, and I don't want to see you take it."
        menu:
            "I'll take the slim chance.":
                show prot hopet
                mc "I'll take the slim chance."
                g "Seriously?"
                mc "Yeah."
                g "You really wouldn't rather have the security of being in the Army?"
                mc "I like being an adventurer more."
                g "Why?"
                mc "You get to do whatever you want."
                g "Huh?"
                mc "You aren't bound to anything. You don't have to serve anyone, protect anyone, give advice to anyone, you just get to... go on adventures."
                g "...That's not really true, you know."
                mc "Well, you're right, but unless the Demon King comes back it'll keep being like this for a long while... And as long as I'm careful I won't die."
                g "And exactly because the Demon King is dead you'll just end up being a nobody."
                mc "I don't really care to be honest..."
                mc @angryt "... And also, it's not true!"
                mc @smilet "I knew most of our town's adventurers before joining the guild, they're not nobodies."
                g "Pft. You're weird."
                g "...But still, you can't fail [mc]!"
                g "Even if you might not want to do more than adventuring, there's lots you can learn in the more advanced classes."
                mc "{i}Sigh...{/i} I guess you're right."
                hide cutegabeu
                show talkshgabe
                g "See? Come on [mc], you have to try. Do it for me."
                mc  "..."
                mc "...Fine."
                g "Yay!"
            "You're right.":
                mc "...You're right, I better start studying."
                show talkshgabe
                g  "Good, good."
        scene gaberoomd
        show talkwagabe
        show smilemc
        g "So, do you know what the test is about?"
        if historyClass < 2:
            show worriedmc
            mc "Ahh... It's, uh, about the... y'know... Demon War...?"
            show cutegabeu
            hide talkwagabe
            g "That didn't sound too convincing."
            show talkgabe
            g "...But you're at least half right. It's about the town's beginnings as well."
            show talksadhappymc
            mc "I see."
            g "So? How much do you know?"
            mc "Uh..."
            show talkwagabe
            g "Did you even go to any of Boris' classes?"
            if historyClass > 0:
                mc "I did."
                g "You remember any of it?"
                mc "Not much. I didn't know there was going to be a test, ok?"
            else:
                mc "Uh, no."
                g "Wow."
                mc "I was b-"
                g "You were busy, I get it."
            show talkshgabe
            g "...I can help you with the studying, if you want."
        else:
            mc "...I'm assuming it's about Randel's History? And the Demon Wars."
            show cutegabeu
            hide talkwagabe
            g "I'm surprised you know that but not that there's a test."
            show talksadhappymc
            mc "Ehh..."
            g "Well it seems you know a bit about it."
            mc "Well... A bit. I will still have to study."
            show talkshgabe
            g "I can help you with that, if you want."
        mc "Really?"
        g "Yeah, we could have a group study session."
        mc "What's that?"
        g "Something we did at Westian. A group of students would get together and study... But it'll be just the two of us."
        mc "Oh, well, that sounds useful."
        g "It is. We can start tomorrow if you want. Get yourself a history book and study."
        show talkwanmc
        mc "...I thought we'd be studying together?"
        g "Yes and no. We both study on our own and then meet up and see how well we know our history! I'll be asking questions and you'll have to answer."
        hide talkwanmc
        mc "Oh, like a practice test. I get it."
        g "Yeah, let's start with the {b}History of Randel{/b}. I'll be asking questions from that section."
        mc "Yes ma'am. I could probably get a book from the library, right?"
        g "I think so. I don't know if there's many copies of it in the library, but there's not many people who can read in our year anyway."
        mc "I guess you're right."
        mc "At what time should I come?"
        g "In the evening after school."
        mc "Gotcha."
        mc "I guess I'll be going then. It's already getting dark, and you have studying to do as well."
        show talkwagabe
        hide talkshgabe
        g "\"We\" have studying to do."
        mc "Yeah, yeah, {b}\"we\"{/b}."
        g "Bye, [mc]."
        mc "Bye, bye."
        scene black with fade
        "You leave Gabrial's home and head home."
        play music night
        scene homenight with fade
        mc "{i}It was really fun spending time with Gabe after so long. She's still the same even though she's grown up."
        mc "{i}But her looks have changed... I would be lying to myself if I said she wasn't pretty."
        mc "{i}Ahhh! [mc]! She's your childhood friend, you shouldn't be thinking like this!"
        if sawgabebathnude == 1:
            mc "{i}I did see her naked though... She's hot for sure."
        "You shake your head trying to get those thoughts out of your mind."
        mc "{i}Ahh... I'm so tired."
        mc "{i}Tomorrow, I'll have to get a history book from the library. Now... I'm going to sleep."
        $ time = 4
        $ gabee1 += 1
        jump home

label gabeStudyingPt1:
    hide screen hud
    show talkg
    show smilemc
    g "Oh, hi, [mc]."
    show talkhappymc
    mc "Hey, Gabe."
    mc "You look better... without the hoodie."
    show talksg
    g "Huh? Oh, I forgot."
    hide talksg
    hide talkg
    show worriedblushgabe
    show talksadhappymc
    mc "Don't, I said it looks better."
    show talksgabe
    g "I'm not used to it."
    show talkwamc
    mc "Come on, why? Are you afraid of the sun? You a vampire or something?"
    g "No, it just feels... a bit weird, that's all."
    mc "But you had it off when I came in."
    g "Well, I was alone then. It's only weird when I'm in public."
    mc "It's just me."
    g "Uhm, yeah... but still..."
    mc "What? You can't be yourself around me? I thought we were friends."
    show cutegabeu
    g "Ugh, ok, ok, you don't need to get mushy."
    scene gaberoomd
    show smilemc
    show cuteg
    g "There, you happy?"
    show talkwamc
    mc "Now you look like the Gabe I knew."
    g "......"
    g "Sooo, you here to study?"
    $ gabeintro += 1
    mc "Yup."
    g "Did you read it?"
    mc "Yes, ma'am."
    show talkg
    g "Let's start then."
    scene gaberoomd with fade
    "Gabe takes a book and jumps on to the bed."
    g "Come."
    "You sit on the bed."
    g "Heeey! Not on... the bed."
    mc "Wh-Why not?"
    g "You... can see the book."
    mc "But I could just... not look."
    g "No, no, no... you'll have to be down here."
    mc "Come on."
    g "That's how it's going to be, boy."
    mc "Ugh."
    mc "{i}I guess she doesn't like me on her bed."
    "You sit down on the floor next to Gabe's bed."
    scene studygabe1 with fade
    mc "Fine, ask your questions then."
    g "Ok, let's see... Let's start with something easy."
    jump gabeQuestions1
label gabeQuestions1:
    scene studygabe1 with fade
    g "Here's the first one."
    g "Who founded Randel?"
    mc "......"
    menu:
        "Jhon Randel" if easyMode == False:
            mc "Jhon Randel."
        "James Randel":
            mc "James Randel."
            $ correct += 1
        "Mark Randel" if easyMode == False:
            mc "Mark Randel."
        "Jack Randel" if easyMode == False:
            mc "Jack Randel."
    g "Next question."
    g "What was Randel famous for?"
    menu:
        "Its rich soil":
            mc "Its rich soil."
            $ correct += 1
        "Its wheat" if easyMode == False:
            mc "Its wheat."
        "Its beauty" if easyMode == False:
            mc "Its beauty."
        "Its Adventurers' Guild" if easyMode == False:
            mc "It's Adventurers' Guild."
    g "Last question."
    g "How old is Randel?"
    menu:
        "100 years" if easyMode == False:
            mc "100 years."
        "130 years" if easyMode == False:
            mc "130 years."
        "320 years" if easyMode == False:
            mc "320 years."
        "340 years":
            mc "340 years."
            $ correct += 1
    jump gabeStudyingPt2
label gabeStudyingPt2:
    if correct < 3:
        g "Hmm, I think you should study a bit more, [mc]."
        mc "Sigh... Ok."
        g "Study again and come back tomorrow."
        mc "Yes, ma'am."
        $ correct = 0
        $ time = 4
        jump home
    g "Well done, [mc]. Looks like you studied well."
    mc "Foof, thanks!"
    $ correct = 0
    g "We've covered the History of Randel. We'll do the History of Astylla next."
    mc "Ok."
    g "Hmm... It still not dark yet."
    mc "We finished up quickly today."
    mc "Yeah."
    mc "I'll stay a little while longer then, if you don't mind."
    g "N-No problem."
    mc "...Boris is way different than I thought he was."
    g "Why?"
    mc "The history book, I got it from Boris. The Library didn't have one."
    mc "He just turned into a completely different person when I asked him for a book."
    g "He was nicer than you thought, right?"
    mc "Yeah."
    g "Teachers like students who are more interested in their studies. It's just a normal thing."
    mc "I guess you're right."
    g "So, you're going to the Academy more regularly?"
    mc "Y-Yeah."
    g "Good."
    g "Do you go there to study or stare at Cynthia all day long?"
    mc "What? What made you say that?"
    g "Relax [mc], I'm not judging you or anything. It's only normal; a boy looking at a pretty girl."
    mc "......"
    scene studygabe2
    $ persistent.studying = True
    g "So, what do you think about Cynthia?"
    mc "Me? I don't know."
    if sawcynth >= 4:
        mc "{i}I could tell her she's a bitch, but I doubt she'd believe me."
    mc "She is pretty, I guess."
    g "She is really pretty, isn't she?"
    mc "Uhm... y-yeah."
    g "......"
    mc "Gabe, can I ask you something personal?"
    g "Go ahead."
    mc "I've heard that some women prefer... other women... are you one of-"
    g "N-NO!"
    mc "Oh! O-Ok! ...I was just saying because, well, you seem more obsessed with Cynthia than I am."
    g "It's nothing like that. She's just my woman crush."
    mc "Woman crush?"
    g "My woman crush! A girl I think is pretty. Don't guys have those?"
    mc "What, Like a man... crush?"
    g "Yeah."
    mc "...But I'm not into men."
    g "That's not the point. It's like... finding the someone of your own gender aesthetically appealing and wishing to be more like them."
    g "The kind of person {b}you know{/b} you'd fall for if you swinged that way."
    if gabeLooksCute == True:
        mc "Well I don't find you any less \"aesthetically appealing\" than Cynthia."
        g "Hah, thanks."
    mc "But... The only men I know are... Sander and Uncle Pete."
    mc "...{p}...{p}......"
    play sound ohyeah
    scene spsexy with flash
    mc "{b}{i}GAG"
    scene studygabe2 with flash
    mc "{b}NAAAAAH{/b}, I don't think I have a man crush."
    g "Hahahahahaha!"
    scene gaberoomd
    show talkwamc
    show normalg
    mc "Ok, that's enough talking about our gender-reversed crushes for one day. I better go, it's getting dark."
    show talkwag
    g "Awww, ok then. See you tomorrow."
    mc "See you tomorrow."
    hide talkwamc with easeoutright
    g "Study the Demon War, ok?!"
    mc "OK!"
    $ time = 4
    $ studygabe1 += 1
    jump home

label gabeStudyingPt3:
    hide screen hud
    show talkhappymc
    show normalg
    mc "Hey."
    show talkg
    g "[mc]!"
    g "Want to get started right away?"
    show talkwamc
    mc "Yeah, no point wasting time."
    show talkwag
    g "Very good, [mc]."
    mc "Hehehe, thank you, ma'am."
    g "Let's start then."
    scene studygabe1 with fade
    g "Here's your first question."
    g "What was the name of King Woren's two sons?"
    menu:
        "Ron and Rim" if easyMode == False:
            mc "Ron and Rem."
        "Rem and Reg" if easyMode == False:
            mc "Rem and Reg."
        "Rem and Ron":
            mc "Rem and Ron."
            $ correct += 1
        "Rem and Rim" if easyMode == False:
            mc "Rem and Rim."
    g "The Demon King was summoned by..."
    menu:
        "Prince Rem":
            mc "Prince Rem."
            $ correct += 1
        "Prince Ron" if easyMode == False:
            mc "Prince Ron."
        "King Woren" if easyMode == False:
           mc "King Woren."
        "General Astyl" if easyMode == False:
            "General Astyl."
    g "Who killed the Demon King?"
    menu:
        "Sir Jhon Albert" if easyMode == False:
            mc "Sir Jhon Albert."
        "Sir Gregory Hans" if easyMode == False:
            mc "Sir Gregory Hans."
        "Sir Jamie Hans" if easyMode == False:
            mc "Sir Jamie Hans."
        "Sir Gladius Hans":
            mc "Sir Gladius Hans."
            $ correct += 1
    jump gabeStudyingPt4
label gabeStudyingPt4:
    if correct < 3:
        g "Hmm... I think you should study a bit more, [mc]."
        mc "{i}Sigh...{/i} Ok."
        g "Study again and come back tomorrow."
        mc "Yes, ma'am."
        $ correct = 0
        $ time = 4
        jump home
    g "Yes! Very good. I think you won't have a problem for the test."
    mc "Really? Thanks, Gabe. Wouldn't have been possible without your help."
    g "Hey, you did all the studying. I just gave you some... motivation."
    mc "Anyway, thanks for all the help."
    g "No problem."
    g "Looks like we still have time today as well."
    mc "Wanna talk about your woman crushes again?"
    scene studygabe2
    g "No, no. Haha... Let's talk about some real crushes, then?"
    mc "Why do you like this subject so much?"
    g "Nothing, I'm just curious. These are things we didn't talk about when we were kids."
    mc "...What do you want to know?"
    g "Do you have any crushes? Cynthia's an obvious one. Anyone else?"
    menu:
        "I don't have a crush on Cynthia":
            mc "I don't have a crush on Cynthia."
            g "Are you being serious?"
            mc "Yeah. Just because she looks good doesn't mean I have a crush on her."
            g "Hmm, interesting. You're more mature than I thought, [mc]."
            mc "Of course I am."
        "Say nothing":
            mc "I don't know."
            g "So you do have a crush on Cynthia?"
            mc "...Ok, I do."
            g "...See? I knew it."
    g "Anyone else?"
    mc "Mhh... no one really comes to mind."
    g "Seriously? No one? You don't find any other woman attractive?"
    mc "I do find them attractive, but I don't have a crush on them."
    g "......"
    mc "{i}Why is she staring at me? Is she trying to tell me something?"
    mc "What?"
    g "No, no, it's nothing."
    mc "...So, since I've told you about my crushes, how about you tell about yours?"
    g "My crushes?"
    mc "Yeah. And please try to talk about guys this time."
    g "Ha-ha, very funny."
    g "Surprisingly, there are quite a few guys here in Randel, now that I think about it."
    g "I don't think I have crush on anyone at the Academy."
    mc "No one?"
    g "Hmm... yeah."
    mc "What about that cool brown-haired guy?"
    g "Who?"
    mc "I think his name was... [mc] or something."
    g "Oh him, he just looks a bit dumb to me."
    mc "That's not what most girls think about him."
    g "Oh, I know what most girls think about him."
    mc "...Wait, really?"
    g "Hahaha! No! I was just kidding."
    mc "Oh."
    g "Hahaha! Got you from your own stupid joke."
    mc "Yeah, yeah."
    mc "So you don't have a crush?"
    g "Hmm... Oh wait, there was this one guy I met recently. What was his name...? I can't quite remember. You know him?"
    mc "Huh?"
    mc "{i}Who is it?"
    mc "What does he look like?"
    g "Uhm, he has brown hair and he wears a red headband."
    mc "{i}It can't be."
    g "Oh, he said he was in the Adventurer's Guild."
    mc "Sander?!"
    g "Oh yeah, Sander. That was his name."
    mc "But, he's, like, way older than you."
    g "So what? Don't you find older women attractive?"
    menu:
        "Yeah":
            mc "Uhm... yeah."
            g "It's the same thing."
        "No":
            mc "Uhm... no."
            g "What?"
            g "Ok, fine, but most guys do."
            g "It's the same thing with girls."
    mc "But Sander... how... why do you like him?"
    g "He was very charming."
    scene gaberoomd
    show talkwanmc
    show normalg
    mc "Wait, I need to make sure we're talking about the same guy here. Does he wear a yellow shirt and has a light beard?"
    show talkg
    g "Yeah."
    mc "It {b}IS{/b} Sander!"
    mc "How did you guys even meet?"
    show talkwag
    g "I went by the Adventurer's Guild thinking I would find you, then I bumped into him- or was it him who bumped into me? ...I can't really remember. He said he's seen me somewhere."
    mc "{i}Oh Astylla, I hope he didn't say where."
    mc "Have you... seen him before?"
    g "No. Then I asked if he knows about you and he said you were his... apprentice or something."
    mc "Y-Yeah, he teaches me... adventuring... stuff."
    g "Mhh... he was really nice."
    mc "So just like that, you instantly fell in love with him."
    show cuteg
    g "No! I just thought he looked cool."
    hide cuteg
    g "Why are you so surprised though?"
    mc "Uh... nothing, it's just... I didn't know you liked older guys."
    g "You really don't know much about girls, [mc]."
    mc "{i}And you don't know about Sander."
    mc "I'll tell him you said hi then."
    show cuteg
    g "Ok... but don't go tell anyone else, ok?"
    show talkwamc
    mc "Mhhh. I'll think about it, he might want to know he has a crazy fangirl."
    g "[mc]! I'm not a crazy fangirl!"
    g "I just said he looked good."
    mc "Ok, ok."
    mc "I better go now then."
    hide cuteg
    show talkshg
    g "Is it dark already?"
    show talksadhappymc
    mc "Yeah."
    g "See you tomorrow at the Academy then."
    mc "Yeah, bye."
    g "Bye."
    scene homenight with fade
    play music night
    mc "{i}Gabe met Sander. I hope he didn't say anything."
    mc "{i}I should go and ask him about it."
    $ didtest = True
    $ time = 4
    jump home



label gabequest2:
    mc "I should go see July first."
    mc "Hey July, I would like to take this quest."
    j "Let's see."
    j "Rank Bronze. Yes, you're good to go."
    j "Remember, [mc], It only says \'investigate\'. Don't get into any unwanted trouble."
    mc "I got it, don't worry."
    j "Good luck then."
    mc "Thanks."
    hide screen hud
    scene black with fade
    play music forest
    "You grab your gear and go to the forest."
    scene forest with fade
    mc "Ok, according to the map, the old castle shouldn't be far. I should be careful, this is goblin territory after all."
    "You slowly move through the forest, you keep your guard on ready for danger at any turn."
    "You hear some rustling nearby. You quickly duck and hide behind a bush."
    mc "{i}I think someone's there."
    "The rustling continues. Someone is definitely there."
    "You unsheathe your sword and slowly creep through the bush to discover..."
    scene forrest with vpunch
    show normalgabeop
    mc "Gabe?"
    show talkwanmc with easeinright
    hide normalgabeop
    show talkwagabe
    g "[mc]! You scared me."
    mc "......"
    mc "What the hell are you doing out here?"
    g "I came to pick up some herbs, you?"
    mc "You came way out here for that? Don't you know this is goblin territory?"
    show talksgabe
    g "Goblin territory? Are you serious?!"
    mc "Yeah! You didn't know?"
    g "No! I couldn't find anything in the outer valley, so I went deeper into the forest."
    mc "It's dangerous for you here, let's go."
    g "......"
    g "Yeah, ok. But wait, I found some herbs. I'll pick them up quick."
    show angry
    mc "Gabe!"
    show talkshgabe
    g "There just right there, please."
    mc "...Fine, but make it quick."
    g "I will."
    scene forrest
    show worriedmc
    hide talkshgabe
    g "I'll come as soon as I ge-"
    show suprised with vpunch
    g "AHHHHHHH!"
    play music battlemusic1 fadein 3
    mc "{i}A trap!"
    mc "Gabe! Shit!"
    g "[mc]! HELP!!!"
    show angry
    mc "SHHH! Keep it down, if the goblins might be close by, they'll hear-"
    scene forrest
    show suprised
    mc "...you."
    scene goblinfight1
    pause
    "You're surrounded by goblins."
    g "[mc]! G-Goblins!"
    mc "Gabe, stay calm!"
    mc "{i}There are four of them. If I take my time, face them one by one, I might make it."
    mc "{i}I have to do this. I have to protect Gabe!"
    g "[mc], please... don't leave me!"
    mc "I won't leave you! We're going to get out of th-"
    play sound arrow1
    scene goblinfight2
    show goblinfightwoosh
    pause 0.1
    hide goblinfightwoosh
    mc "...a... dart."
    g "[mc], what's wrong?!"
    mc "I-I feel... dizzy."
    "Everything starts to blur out"
    mc "Ngh... I can't black out now!"
    mc "Come on!"
    play sound arrow1
    show goblinfight3
    mc "Ekk!"
    play sound arrow1
    show goblinfight4
    g "[mc]!"
    mc "Urgh..."
    if chartrait == 2:
        mc "I'm tougher than this... I can still make it."
        mc "{i}If I cut down the net, Gabe might have a chance."
        mc "Gabe... as soon... as I cut this net... you run!"
        g "No... [mc]!"
        "You lift your sword to cut down the net, but another dart hits your hand."
        play sound arrow1
        show goblinfight5
        mc "Urgh..."
        mc "I... can't..."
    "You fall to the ground."
    scene black with vpunch
    stop music fadeout 1.0
    pause
    "..."
    "......"
    "......"
    "........."
    play music night
    scene castle
    pause 0.1
    scene black
    pause 0.1
    scene castle
    pause 0.1
    mc "Ugh... Where am I?"
    "You find yourself tied up in a room. It's dark; the only light source is a small torch in the corner of the room."
    "The walls are made out of stone covered in green moss. The air is cold and wet."
    mc "{i}Is this the old castle?"
    mc "{i}Gabe! ...Is she here?"
    "You hear footsteps approaching."
    "Two goblins enter the room."
    "Goblin 1" "Human... wake... up."
    mc "{i}Did it just talk?"
    "Goblin 2" "Take him... to... Leshek?"
    "Goblin 2" "Yes."
    "The two goblins carry you out."
    mc "Where the hell are you taking me!?"
    "Goblin 1" "......"
    "Goblin 2" "To... Leshek."
    "Goblin 1" "Don't... talk... to human."
    "Goblin 2" "But he ask... question."
    "Goblin 1" "Only... Leshek talk to... human."
    menu:
        "Who is Leshek?":
            "Goblin 2" "Leshek our lead-"
            "Goblin 2" "...No talk to human."
        "Keep quiet":
            mc "......"
    "The goblins take you to a large open area. You can tell that this used to be the throne room."
    "Most of the walls have broken down, revealing the night sky."
    "At the far end, you see a goblin sitting on a stone throne which is surprisingly still intact."
    "The goblins throw you to the ground."
    mc "Owww."
    "You kiss the dirty wet floor. Your eyes slowly focus on the Goblin sitting in front of you."
    le "Welcome, human."
    play music creepymusic
    scene goblinking with fade
    pause 0.1
    scene black with fade
    scene goblinking with fade
    pause 0.1
    scene black with fade
    pause 0.05
    scene goblinking with fade
    mc "Wh-What..."
    mc "What the hell are you?"
    le "Goblins! I'm sure you knew already."
    mc "......"
    le "I know it must be rather confusing, talking to a goblin. I understand."
    mc "How... can you speak?"
    le "All goblins have the ability to speak, they just don't know it."
    mc "Where's Gabe?!"
    le "Gabe?"
    mc "The girl, I know you have her."
    le "Oh, the girl. Yes, we have her. I'll bring her in."
    le "Ori... bring in the girl."
    "Goblin Ori" "Yes, Leshek!"
    mc "Did... you harm... her."
    le "Oh, no, we haven't harmed her... yet."
    mc "What do you mean \"Yet\"!"
    le "Do you know why you're both still alive? If we were normal goblins, we would've etarm angryt you by now."
    mc "......"
    mc "So why are we here?!"
    le "You are very talkative, aren't you?"
    le "I like that."
    scene gabebond1
    le "Oh, there she is. Look, not a single scratch."
    show gabebond2 with dissolve
    $ persistent.gabeBondage = True
    pause
    window hide
    mc "Gabe!"
    g "{i}sob"
    mc "You told me you didn't do anything to her, you bastard!"
    scene goblinking
    le "I said we didn't harm her, which we didn't. We just prepared her for what's to come."
    mc "What the hell does that mean?!"
    stop music  fadeout 7
    le "You want to know why you're here? I'll tell you."
    le "You're here to give us our king."
    mc "What?!"
    le "Let me explain."
    le "As you might have noticed, I'm rather different from the other goblins. I've always had more brains than brawn, you see."
    le "When I was in my tribe, I realized something. We always fought humans and we always lost, horribly."
    le "When comparing strength, goblins and humans were equally matched. \"Why do we always lose then?\" I thought."
    le "They were smarter. That's when I thought; rather than fighting them, we should learn from them. So I left my tribe."
    le "I studied humans and I learned from them, how to communicate, how to make plans, how to make weapons, how to lead."
    le "After some time, I found this castle. I gathered more goblins, I taught them what I've learned. A few years passed and we were the most powerful goblin tribe in the forest."
    play music creepymusic fadein 5
    le "It was all thanks to the human knowledge. And then I thought... What would happen if we had a human as our leader?"
    le "We would be unstoppable!"
    mc "So what? You... want me... to lead you?"
    le "Hahahaha, no! You're an adult, you would never think of us as your own. We need a human born here, surrounded by our kind."
    le "We've tried several times to capture two of humans alive and failed. Every time one of them dies. Usually the men, they try to fight back. Keeping a female alone in the castle for some time is a hard thing to do, you know what I mean."
    le "But finally, we succeed today!"
    scene gabebond1
    show gabebond2
    mc "Wh-What are you saying?"
    le "You and the girl will give us a child, who will become our king!"
    "All the goblins start to cheer."
    g "[mc]?"
    mc "Th-That doesn't make sense!"
    scene goblinking
    mc "If a human is raised with goblins, he'll be no more than a goblin himself."
    le "Correct. That's why once it's grown to a certain age, we will send it to the human world, to learn things we don't know, bring us materials we could never obtain."
    mc "Wh-Why would it listen to you? It won't betray its own kind."
    le "Well, we could come up with some lie, something that would convince it that we are the only family it has. We could tell, it was abandoned by its parents, rejected from mankind."
    mc "This is crazy!"
    mc "......"
    mc "What will... you do with us after?"
    le "This might be a bit hard on you, but I suppose you'll realize."
    mc "......"
    le "Once you've impregnated the female, you will be... killed. The girl will not be harmed in any way until the child is born. After the child is born, the girl will take care of it for a few months. And then she will be released, you have my word."
    mc "Trust the word of a goblin? Huh?"
    mc "And what if we don't do what you want. You'll kill us both?"
    le "You will be killed, after the girl is raped and killed."
    le "We might seem decent, but our sexual urges are still the same. And let me tell you, when a group of goblins get hold of a female, a pretty one like her, things get really messy."
    le "And we'll make you watch the whole thing."
    mc "You're fucking savages, after all."
    le "So human what will it be?"
    g "{i}sob"
    mc "......"
    mc "{i}SHIT! What do I do? Will he really let her go if-"
    mc "{i}Fuck, can I even trust him?! And if I don't do anything I'll have to... watch... everything."
    mc "......"
    mc "{i}I-I have... n-no... choice!"
    scene goblinking with fade
    pause 0.1
    scene black with fade
    label goblinking:
    $ gameover = "goblinking"
    scene goblinking with fade
    mc "{i}Come on, get it together!"
    menu:
        "Don't do anything, let it happen":
            mc "{i}I h-have to do this. I can't watch her getting... raped."
            mc "{i}Who knows, they might actually let h-her g-go. Yeah, th-they will."
        "Try to kill Gabe":
            $ killgabe += 1
            mc "{i}They won't let Gabe go, I know it."
            mc "{i}I shouldn't let her suffer. I-I'll end it for her... quick."
            mc "{i}Sob..."
        "Try to kill the Goblin king" if easyMode == False:
            mc "{i}I'll kill that bastard, I don't care what happens."
            scene black
            "You're only a few feet away from the goblin king. All the gaurds are behind you. "
            mc "{i}I'll strangle that motherfucker!"
            "You charge at him."
            mc "YOU FUCKER!"
            "The Goblin king jolts up, he did not expect that. You grab him."
            if chartrait == 2:
                "You're strong, and you've been in enough fights as a child. With ease, you pick him up and slam him on the floor."
                le "ARGGH!"
                "You strangle him."
                mc "DIE, BITCH!"
                "Before long, a goblin stabs you in the back."
                "But you still keep going, squeezing on the goblins king's neck as hard as you can."
                "Another goblin stabs you on the neck and pulls you off the goblin king. You fall to the ground."
                "You lie in a pool of your own blood, gushing out of your neck."
                "You look to your right."
                "The goblin king lays there motionless, his eyes bulging out of his face. All the goblins gather around him."
                "You look to your left."
                mc "G...abe."
                "Gabe is already dead. Her throat is sliced open and she lies on the floor."
                "Your vision slowly blackens... and you die."
                scene black with fade
                jump GameOver
            "You try to pull him of his throne, but he's too heavy and you're too weak. The goblin kind kicks you and you fall to the floor."
            "Before you can react, a huge blade impales your chest."
            le "Foolish human."
            le "Now look how your friend-"
            le "What?! You idiots! Why did you kill her?!"
            "You look to your left."
            mc "G...abe."
            "Gabe is already dead. Her throat is sliced open and she lies on the floor."
            "Your vision slowly blackens... and you die."
            scene black with fade
            jump GameOver
    mc "I'll... do it."
    scene gabebond1
    show gabebond2
    le "You made the right choice, human."
    le "Untie her!"
    if killgabe == 1:
        mc "{i}sob"
        mc "{i}I'll have to s-strangle her."
    mc "{i}I'm sorry, Gabe."
    "The goblins untie Gabe."
    le "Proceed, human."
    scene goblinking
    mc "......"
    g "[mc]!"
    g "[mc], CLOSE YOUR EYES, NOW!"
    mc "What!?"
    g "ALOKA!"
    stop music
    play sound magic
    scene black with flash
    "A flash of bright light hits you. You can't see anything."
    le "Ugh! ...What?!"
    mc "Gabe!"
    play music battlemusic1
    "Someone grabs hold of your hand."
    g "[mc]! It's me. Let's go."
    le "Stop them!"
    "Goblin 1" "We... not... see anything!"
    "Goblin 2" "Everything black..."
    g "We need to find our gear."
    "You run with Gabe holding on to her hand. You still can't see a thing."
    scene castle with fade
    pause 0.1
    scene black with fade
    pause 0.1
    scene castle with fade
    pause 0.1
    scene black
    g "Found it, let's go!"
    "The two of you keep running. You still can't see anything."
    scene forrestn with fade
    pause 0.1
    scene black with fade
    pause 0.1
    scene forrestn with fade
    pause 0.1
    scene black with fade
    g "I think... {i}pant{/i}... we came far... {i}pant{/i}... far enough."
    g "Sit down."
    stop music fadeout 5
    mc "I can't... {i}pant{/i}... see."
    g "I know! It'll wear off. I told you to close your eyes."
    mc "What was that?"
    g "A spell. Blinds everyone's vision for some time."
    play music night fadein 3
    mc "You... saved our asses."
    g "...I did... didn't I?"
    g "I was so scared, [mc]."
    mc "I know, I was too. Did they do anything to you?"
    g "No... they didn't."
    mc "I'm sorry, Gabe."
    g "Why?"
    mc "I couldn't do anything, I couldn't protect you."
    if killgabe == 1:
        mc "{i}I thought of killing you..."
    g "It's ok, [mc], there's nothing you could've done. And it was my fault we got in this mess anyway."
    "You hear fumbling."
    mc "What are you doing?"
    g "I'm putting on my clothes!"
    mc "Oh, sorry."
    "......"
    g "...Ok. {i}sigh"
    g "Who the hell was that, [mc]?"
    mc "I don't know. Those goblins, they're something else."
    g "We should report them!"
    mc "Yeah."
    g "How are your eyes? Still can't see anything?"
    scene forrestn with fade
    pause 0.1
    scene black with fade
    mc "A little. It's starting to get better."
    g "It'll get better soon."
    g "[mc], I have no clue where we are."
    mc "Do you still see the castle?"
    g "Yeah, a little."
    mc "Check if there's a map in my bag. You got my bag, right?"
    g "Yeah."
    g "Hmmm... there's a map of Randel, and another one of the forest."
    mc "The map with the forest, take it."
    mc "The location of the castle must be marked there. I think we can find our way using it."
    g "You're right. According to the map, we're not that deep into the forest."
    mc "Good."
    g "You knew the location of the castle?"
    mc "I was told to investigate the area, I was on a quest."
    g "Oh, that's why you were in the forest."
    mc "Yeah."
    g "Quest complete then, I guess."
    mc "Yup."
    g "...[mc], I think we should move."
    mc "Are the goblins coming?!"
    g "Not yet, but I don't feel like staying here."
    mc "You're right, let's go."
    g "Can you see?"
    mc "Still not too well."
    g "Here, take my hand then."
    "You once again grab Gabe's hand. The two of you start your journey back home."
    g "You know, this might have been the most terrifying night of my life."
    mc "Mine too."
    g "Do you run into these sorts of trouble in all your quests?"
    mc "Only if if I'm with stupid girls that get caught in traps."
    g "Hey! That stupid girl saved your ass, remember?"
    mc "Yeah, but she also got us in trouble, so it kinda cancels off."
    g "Jeez, [mc], don't be mean."
    mc "I was kidding. You did great."
    g "...Thanks."
    g "Let's just forget about all this, ok?"
    mc "You're right."
    "The two of you walk for a while."
    scene forrestn with fade
    pause 0.1
    scene black with fade
    pause 0.4
    scene ambushn with fade
    "You vision slowly comes back."
    mc "Hey, I can see again."
    g "Great, we're almost there. Look, I think I see some lights."
    "You finally arrive at Randel."
    scene villagen with fade
    show talksgabe
    show talksadhappymc
    mc "We're here. I didn't think we'd make it before dawn."
    g "Yeah."
    mc "What a day, huh?"
    show talkshgabe
    g "...Y-Yeah."
    show talkmc
    mc "We should get some rest, Gabe, it's been a rough day."
    g "...O-Ok."
    scene villagen
    show worriedmc
    show talksgabe
    g "Uhm... [mc], this might sound... a bit weird but... could you stay at my place... tonight?"
    mc "...I... don't mind. But why?"
    g "It's just..."
    show worriedgabe
    g "Ugh, just forget it."
    mc "No, it's ok. You can tell me."
    g "......"
    g "I feel kinda... scared to be alone... today, after what happened."
    mc "You don't have to be scared, we're safe now, Gabe."
    show worriedblushgabe
    g "...I... know... but..."
    show talksadhappymc
    mc "Alright then. If it makes you feel better, I'll come."
    show talkshgabe
    g "...Thanks, [mc]."
    "You go to Gabe's house."
    scene gaberoomn with fade
    stop music
    g "Take a seat, [mc], I'll bring some tea."
    mc "O-Ok."
    "You sit down. Gabe brings tea after a few minutes."
    g "Here."
    mc "Thanks."
    g "I'll go get changed. You didn't bring clothes, didn't you?"
    mc "You didn't let me."
    g "Sorry."
    mc "It's ok, I'll just take off the jacket."
    g "Ok..."
    "Gabe goes into her room."
    scene teagabe1 with fade
    mc "{i}sigh. So tired."
    mc "{i}Gabe must have gotten really scared, poor girl."
    mc "{i}I should report this to the Guild tomorrow, they need to know about those goblins."
    "You take a sip from the tea."
    pause 0.8
    mc "......"
    mc "{i}I don't think Gabe makes tea that often."
    g "How's the tea?"
    mc "Oh, Ga-"
    scene teagabe2 with hpunch
    mc "Pffft!"
    scene gabesexy1
    g "What happened?? Are you alright?"
    pause
    mc "Yeah, yeah... I just got... a bit surprised seeing you... y'know, like that."
    g "....What? This is what I normaly wear to sleep. The nights are hot here compared to Westian."
    "You take another sip of tea."
    mc "Ok."
    g "You... Already saw me naked... Stop overreacting, [mc]."
    mc "I'm sorry, I'm sorry."
    g "{i}Sigh"
    g "Where... are you going to sleep?"
    mc "I could sleep here."
    g "On the floor?"
    mc "Yeah."
    pause
    g "But why?"
    mc "Where else can I sleep?"
    g "You could sleep... in my bed if you want."
    mc "Where are you going to sleep?"
    g "No. We can both sleep in my bed, it's big enough."
    mc "Oh, Huh-"
    g "Come on, [mc], you don't need to act so weird. We're friends."
    g "It's ok if we sleep together."
    g "......"
    g "Wait! I didn't mean it like that! Ugh."
    mc "It's ok, I understand. You're right."
    g "...So, you're coming?"
    mc "Yeah, I'd rather sleep in the bed than on the floor."
    g "O-Ok."
    scene black with fade
    "Some time later..."
    scene sleepgabe1 with fade
    pause
    "......"
    "......"
    g "[mc], are you awake?"
    mc "......"
    mc "Yeah."
    g "I can't fall asleep."
    mc "Same here."
    scene sleepgabe2 with dissolve
    "......"
    scene gabesleep1
    $ persistent.gabeSleep = True
    pause
    g "Thanks for staying."
    mc "...No problem."
    g "I'm still recovering from what just happened today."
    mc "Yeah, me too."
    g "My heart was beating like crazy, I thought I was done for, [mc]."
    mc "I know."
    g "If it wasn't for you, I don't know what would have happend, those goblins would have-"
    mc "Hey! forget it, alright? Stop thinking about it."
    g "{i}Sigh...{/i} You're right... We're safe now."
    mc "Correct."
    mc "And besides, it was you who saved us. I didn't do a damn thing."
    g "No, you being there calmed my mind. It was because of that I managed to come up with a plan. If I was alone back there I would have panicked, I would have stood there and I wouldn't have accomplished anything."
    g "I'd have froze, like I always do when I'm scared."
    mc "..."
    mc "It was still thanks to you. You did well."
    g "Thanks, [mc]."
    g "..."
    mc "......"
    g "It's been a long time since we slept- I mean... spent the night together."
    mc "You can just say \"slept together\", I don't mind."
    scene gabesleep2
    g "...Feels weird when I say that though. \"Slept together\" sounds like we-"
    mc "I know what it sounds like."
    g "Don't you feel weird when you say it?"
    mc "...Not really. It's just a figure of speech; you don't really mean it."
    g "Y-Yeah."
    g "......"
    scene sleepgabe2
    pause 0.5
    scene sleepgabe1 with dissolve
    g "......"
    g "[mc]?"
    mc "Mh?"
    scene sleepgabe2
    pause 0.3
    scene gabesleep2
    g "...What... if I really asked you to sleep with me... Would it still feel... Weird to you?"
    mc "{i}What is she saying?"
    mc "Wh-What do you mean?"
    g "[mc], give me an answer."
    mc "{i}Where the hell is this going?"
    mc "W-We're friends, of course it would be weird."
    scene sleepgabe2
    pause 0.3
    scene sleepgabe1
    g "......"
    g "I... should never have asked that."
    mc "{i}Did she really mean it?"
    mc "Gabe..."
    g "Just forget it, [mc]."
    scene sleepgabe3
    show sleepgabe32
    mc "What do you mean?"
    g "[mc], just let it go. Can you pl-please t-take off your hand?"
    mc "You can't just say something like that and expect me to forget about it."
    g "P-Please, [mc], your h-hand."
    mc "Gabe-"
    hide sleepgabe32 with flash
    g "Ahhh!!!"
    scene sleepgabe4
    mc "Did you just-"
    show sleepgabe322
    g "I told you to take your damn hand of, [mc]!"
    g "J-Just go to sleep, ok?"
    scene sleepgabe4
    mc "I-I'm sorry."
    scene black with fade
    mc "{i}Just when I thought the day couldn't get any worse."
    "You go to sleep without thinking about what just happened."
    scene gaberoomd with fade
    play music home
    pause 0.9
    show animation2
    mc "{i}yawn"
    mc "...Where's Gabe?"
    show worriedmc
    mc "I have to apologize properly for last night."
    show talksg
    g "[mc], you finally woke up."
    show talksadhappymc
    mc "Yeah. Hehe. What time is it?"
    show talkshg
    g "Almost evening. We both missed Academy today."
    mc "Oh, yeah."
    g "You don't care, do you?"
    mc "Honestly, no."
    show normalg
    hide talksadhappymc
    mc "......"
    g "......"
    show blushtalkg
    show talksadhappymc
    "Gabe and [mc]" "Listen."
    mc "Oh... Uh, you go first."
    scene gaberoomd
    show worriedmc
    show talksg
    g "...I want to talk about last night. I'm really sorry."
    mc "What?! I'm the one who should be apologizing."
    g "No, no, it was me who led you on. I shouldn't have done that."
    mc "...Last night, did you really..."
    g "What?"
    mc "When I touched you... did you..."
    scene gaberoomd
    show worriedblushgabe
    show worriedmc
    "Gabe puts her hood on in embarrassment."
    g "...Yeah, I came..."
    mc "......"
    mc "Wait."
    show talkwamc
    mc "...Are my hands that good?"
    show cutegabeu
    g "Shut up, [mc], there's nothing special about your hands."
    hide cutegabeu
    g "It's just that I'm... very sensitive."
    show talkwanmc
    mc "Eh?"
    g "Ugh..."
    show cutegabeu
    g "I cum easily. There, I said it."
    hide cutegabeu
    show thinkmc
    mc "......"
    hide thinkmc
    hide talkwanmc
    show talkwamc
    mc "Pfft, hahahaha!"
    show cutegabeu
    g "Don't laugh, asshole!"
    show angrygabeblush
    show smileecmc
    mc "I can't believe you said that! Hahahaha!"
    g "This is serious, [mc], stop acting like a kid!"
    show talksadhappymc
    mc "Hahaha, ok, ok, I'm sorry..."
    show talkwamc
    mc "So your... problem, does it happen whenever someone touches you?"
    g "No! It's only... when I'm..."
    mc "Horny?"
    hide angrygabeblush
    show cutegabeu
    g "[mc]!"
    show talkwanmc
    hide cutegabeu
    mc "What, I'm helping you out. Can't stand your stuttering."
    g "...Ok, you're right."
    hide talkwanmc
    mc "Man, I can't believe I'm talking to the innocent Gabe I once knew."
    scene gaberoomd
    show talkwamc
    show worriedblushgabe
    g "I've changed a lot after leaving Astylla, [mc]. You should know I have this sort of side to me too."
    mc "A horny side?"
    show angrygabeblush
    g "{i}sigh"
    hide angrygabeblush
    g "Yeah, a horny side."
    show talksadhappymc
    mc "So last night, did you really mean it? When you said you wanted to sleep with me?"
    g "......"
    g "Yeah."
    hide talksadhappymc
    show suprised
    pause 0.4
    show talksadhappymc
    mc "{i}gulp{/i} I-I didn't know you had feelings for me."
    show cutegabeu
    g "What- Feelings?! No!"
    show talkwanmc
    mc "But you said-"
    show talksgabe
    g "I said I wanted to sleep with you, I didn't say I love you. You're a good friend, [mc]. But as a lover, you're not my type. I don't think I'll ever have a lover."
    mc "If you're not in love with me, why would you ask me to have sex with you?"
    show talkshgabe
    g "I thought we could be friends with benefits."
    mc "What does that mean?"
    hide talkshgabe
    g "...You don't know? {i}Sigh."
    g "It's like this, we're friends and we have sex."
    mc "Still doesn't make sense."
    hide talksgabe
    g "Ughh... It's like playing, we don't think of it as anything else."
    mc "So you have sex with your friend, for the fun of it?"
    show talkshgabe
    g "Yeah... pretty much."
    mc "That's weird."
    g "Well, it's a common thing in Westian."
    mc "Westian is weird."
    g "To you, I guess it is."
    mc "So in Westian, did you have any \"Friends With Benefits\"?"
    g "No, there were only girls in my Academy."
    mc "......"
    mc "Did you do anything with them?"
    hide talkshgabe
    show cutegabeu
    g "I'm not a damn lesbian, [mc]!"
    mc "{i}What's a \'lesbian\'...? I better not ask, she'll get mad again."
    mc "Oh ok, didn't want any more surprises."
    hide cutegabeu
    show worriedblushgabe
    g "Besides, even if I was, I won't be able to do anything because of my... problem."
    mc "...You tried to have sex with me though, your problem didn't stop you there."
    g "...I thought it would be different. I thought it wouldn't happen because you're my friend. And I've known you since we were kids."
    g "But it was the same in the end."
    g "I want to have sex with someone, I'm just afraid that I would end up being... disappointing."
    mc "......"
    g "I know what you're thinking, \"Gabe's such a horny slut\"."
    show talksadhappymc
    mc "No, I understand. I want to have sex and there's nothing wrong with it, same goes for you. It's just the way we are."
    scene gaberoomd
    show talksadhappymc
    show blushtalkg
    g "Oh, [mc], I knew you would understand."
    g "I wanted to tell all of this to someone, [mc]. I'm glad you understood."
    mc "...I'm your friend, Gabe, we help each other. I'm kinda starting to understand the Friends With Benefits thing now."
    g "...Hehehe."
    mc "......"
    mc "So, do you want to..."
    show talksg
    g "I don't know, [mc]. You saw what happened last night, it would be useless."
    mc "...Maybe we could start slow and build up."
    show talkwag
    g "What, you're some kind of sex trainer now?"
    show talkwamc
    mc "I have experience."
    g "Oh, really?"
    mc "Yeah, what do you say?"
    g "......"
    show talkshg
    g "Ok."
    hide talkwamc
    mc "We'll start tomorrow, I'll have to do... some research."
    g "Heheh, ok."
    g "I can't believe we're doing this."
    mc "Me neither!"
    g "You sound exited though."
    show talkwamc
    mc "I AM!"
    g "Hehehe, see you tomorrow."
    mc "Bye, horny Gabe."
    g "Bye."
    scene black with fade
    "Before going home, you go to the Guild."
    scene adgc6
    "You tell July everything."
    "July is shocked."
    j "Oh, bless Astylla, [mc]. You're lucky to be alive. I'll report this to Hern right away!"
    mc "Hmmm."
    j "How is your friend? Is she doing ok?"
    mc "Yeah."
    j "That's good. Here take your reward."
    mc "Thank you."
    j "I'm really sorry, [mc]. I didn't know it was this serious."
    mc "It's ok July."
    j "Take care then."
    $ money += 120
    "You wave July goodbye and go home."
    play music night
    scene homenight with fade
    mc "It seems like that I never really knew Gabe."
    mc "Who would've thought things would turn out this way?"
    mc "How do I train her?"
    mc "We'll have to start slow and build our way up. This is going to be great!"
    $ gabequest2 += 1
    $ time = 0
    $ day += 1
    jump home



label gabeClassFingering:
    hide screen hud
    b "Good morning, class."
    b "Take out your books."
    scene testgabe1
    "{i}Tick...{p}Tock...{p}Tick..."
    scene testgabe2 with dissolve
    pause
    mc "{i}Time for a quick assessment."
    "......"
    scene testgabe3 with dissolve
    pause 0.4
    g "H-Hey, what are you doing?"
    mc "Relax, it's part of your training."
    g "W-What the hell, [mc]? Someone might see us."
    mc "Just stay quiet and we'll be fine."
    "You start to rub Gabe's pussy."
    show testgabe4
    g "Mmmh!"
    mc "You're holding out very well."
    mc "Doesn't doing it in public turn you on?"
    g "Ngh... N-No."
    mc "Weird, it seems your body doesn't agree with you."
    g "Ahh..."
    window hide
    mc "Shh!"
    g "{size=-4}It's not my fault!"
    mc "...Well, I'll stop then."
    hide testgabe4
    g "N-No."
    g "Don't stop."
    pause
    show testgabe4 with dissolve
    g "Mmmh..."
    g "{size=-4}I-I think I'm going to cum."
    mc "Don't scream, or we're both fucked."
    g "Oh.{p}...Shit."
    scene testgabe5 with flash
    pause 0.1
    scene testgabe5 with flash
    pause 5
    scene testgabe6 with dissolve
    g "Never do that again!"
    mc "I know you liked it."
    g "Shut up!"
    mc "Well done, looks like you're ready for the next stage."
    g "R-Really?"
    mc "Yes."
    mc "{i}So if I'm going to move to the next level, I should increase the stimulus. She's ok with my fingers now, I'll have to use something else."
    mc "{i}Maybe I can buy something from Mervin. He's supposed to have everything I want, right?"
    $ gabefingerclass += 1
    $ time += 1
    jump academy



label gabetrip:
    show talkwag
    g "Here, take this."
    scene gaberoomd with fade
    "Gabe hands you a white blanket with red stripes. A classic \'picnic\' blanket."
    scene villageback with fade
    "The two of you leave."
    scene forest with fade
    play music forest
    "You follow Gabe through the forest. She's carrying a brown picnic basket. You wonder what's inside, sandwiches?"
    "It's a bright and beautiful day, perfect for a picnic."
    mc "So where's this place of yours?"
    g "Close."
    mc "Ok."
    mc "How did you find it?"
    g "When I was looking around for herbs."
    mc "You come to the forest a lot?"
    g "Yup, I need those herbs."
    mc "How come I never see you?"
    g "You don't?"
    g "Huh, guess I'm hard to spot. I've seen you a couple of times."
    mc "Really?"
    g "Yeah."
    mc "Why didn't you talk to me?"
    g "Didn't want to bother you, I usually like to mind my own business."
    mc "Hmmm."
    g "Aaaand we're here."
    scene picnic with fade
    pause
    mc "Wow..."
    g "Amazing, isn't it?"
    mc "Yeah. I can't believe I've never found this place before."
    g "The forest is bigger than you think. There are lots of places we've never seen, even in the outer valley."
    g "How about we lay down under that tree?"
    mc "Alright."
    "Gabe lays out the blanket she brought. The two of you lie down on it."
    scene picnicgabe with dissolve
    "The grass below you is soft, and there's a slight cool breeze. The shade of the tree covers you from the hot sun. You've never felt more relaxed."
    pause
    window hide
    g "Beautiful day, isn't it? Perfect for a picnic."
    mc "Yeah, I was thinking the same thing."
    g "Here, I brought some sandwiches."
    "Gabe opens the picnic basket and hands you a sandwich."
    mc "Yes!"
    "You take a bite from the sandwich."
    g "How is it?"
    if gabeSandwich == True:
        mc "Great, as usual!"
        g "Thanks."
    else:
        mc "These are great... did you make them?"
        g "Yeah."
        mc "I didn't know you were such a good cook!"
        g "Making a sandwich isn't actually considered cooking, but I'll accept the compliment."
        mc "It's way better than the ones Uncle Pete used to make..."
        g "Heheh. Thanks."
    mc "So your potions, did you manage to make one yet?"
    g "Y-Yeah a few, but not the ones I wanted to make."
    mc "And what's that?"
    g "You know like, invisibility potions, transformation potions, love potions, the cool kind."
    mc "You wanted to make a love potion?"
    g "......"
    g "Yeah."
    mc "But why? I thought you said you didn't have a crush on anyone."
    g "I don't. I wanted to use it on someone so I could... get laid."
    mc "......?"
    g "To have sex with them! Ugh, I always forget that you don't know these words."
    mc "It's all about... \"Getting laid\" to you, isn't it."
    g "Well, yeah. What else?"
    mc "I don't know, what about love?"
    g "...I'm not really into that stuff. It just makes things complicated."
    mc "You think so?"
    g "Yeah."
    g "Just take us for example. if we were \"lovers\" things would just get more frustrating."
    g "We'd have to meddle with each other's affairs. You wouldn't be able to live your own life, I wouldn't be able to live my own life."
    g "But if we don't take it seriously and stay friends, it's much easier. You can say anything, sleep with anyone and I wouldn't mind because we're friends."
    g "I still care about your problems, but we have our space."
    g "I don't know if you get me, but all I'm saying is: I like keeping things simple."
    menu:
        "I get what you're saying":
            mc "I get what you're saying. What we have is better."
            g "I knew you would understand."
            g "You know, when I saw you for the first time after I came back from Westian, I thought I was feeling the same thing too."
            g "That I instantly fell in love with you. You know, love at first sight, that cliche garbage."
            g "B-But after spending more and more time with you... I just thought being friends would be better, and it was just my urges kicking in, back at that time."
            g "......"
            g "......I'm really fed up with this love thing, [mc], after what happened with my mom."
            mc "Wait, what happened?"
            g "......"
            g "{i}Sigh"
            g "I thought I wasn't going to talk about my sob story with anyone."
            mc "What happened, Gabe?!"
            g "The reason I came back to Randel isn't only because I finished my studies at Westian."
            mc "......?"
            g "You see, I kinda ran away from home as well!"
            mc "What?!"
            g "Yeah, sorry I didn't tell you."
            mc "B-But... wh-why did you run away?"
            g "......"
            g "Apparently, my mom's a slut."
            mc "Excuse me?!"
            g "She's been sleeping with other men. And one day, my dad found out."
            g "And things started to go to hell. They got divorced and the two of them were fighting on who was taking me with them."
            g "I got tired of it, and one day I just thought, I'll just get the fuck away from the both of em. That way, no one would have me."
            g "And that is how I ended up here."
            mc "......"
            mc "......Gabe, I don't know what to say."
            g "...You don't need to. I just want to forget about that mess."
            mc "......"
            g "Hehehe. Looks like being a slut runs in the family, don't you think?"
            mc "You're not a slut, Gabe."
            g "......"
            g "I was just afraid that I would do the same thing to you. Like what my mom did to my dad."
            mc "......"
            mc "I understand, Gabe."
            g "Thanks, [mc]. You always do."

        "I don't. I love you.":
            mc "I don't. I love you, Gabe."
            g "......"
            g "I'm sorry, [mc]... I just don't feel the same way."
            mc "Will you ever?"
            g "...I'm sorry, [mc]."
            g "......"
            g "You know, when I saw you for the first time after I came back from Westian, I thought I was feeling the same thing too."
            g "That I instantly fell in love with you. You know, love at first sight, that cliche garbage."
            g "B-But after spending more and more time with you... I just thought being friends would be better, and it was just my urges kicking in, back at that time."
            g "......"
            g "......I'm really fed up with this love thing, [mc], after what happened with my mom."
            mc "Wait, what happened?"
            g "......"
            g "{i}Sigh"
            g "I thought I wasn't going to talk about my sob story with anyone."
            mc "What happened, Gabe?"
            g "The reason I came back to Randel isn't only because I finished my studies at Westian."
            mc "......?"
            g "You see, I kinda ran away from home as well..."
            mc "What?!"
            g "Yeah, sorry I didn't tell you."
            mc "B-But... wh-why did you run away?"
            g "......"
            g "Apparently, my mom's a slut."
            mc "Excuse me?!"
            g "She's been sleeping with other men. And one day, my dad found out."
            g "And things started to go to hell. They got divorced and the two of them were fighting on who was taking me with them."
            g "I got tired of it, and one day I just thought, I'll just get the fuck away from the both of em. That way, no one would have me."
            g "And that is how I ended up here."
            mc "......"
            mc "......Gabe, I don't know what to say."
            g "...You don't need to. I just want to forget about that mess."
            mc "......"
            g "Hehehe. Looks like being a slut runs in the family, don't you think?"
            mc "You're not a slut, Gabe."
            g "......"
            g "I was just afraid that I would do the same thing to you. Like what my mom did to my dad."
            mc "......"
            mc "I understand, Gabe."
            g "Thanks, [mc]. You always do."
            mc "......"
            g "Don't you think what we have is better?"
            mc "What?"
            g "Being friends with benefits rather than being married and being forever bound by love, by death do us depart nonsense."
            mc "......"
            mc "...I-I guess."
            g "Come on, [mc], don't look so down."
            g "You'll find someone better, someone better than a perv like me. Hehehe."
            mc "......"
            mc "...I understand."
            mc "{i}She sees me as a friend. I'll have to accept it."
            mc "A friend with benefits is good for me then."
            g "Exactly."

    mc "Then how about we conclude our training?"
    g "Huh?"
    mc "It's time for the last stage."
    g "You mean..."
    mc "Yeah."
    g "Here?"
    mc "I've always wanted to do it outdoors."
    g "...L-Let's do it then! I need to clear my head after all that."
    scene picnic with fade
    g "Oh, g-gos... It's finally happening! Stick it in!"
    mc "Stay still."
    scene gabesex0 with hpunch
    g "Ohhh, yes!"
    window hide
    pause
    mc "{i}She's so wet."
    mc "I'll start moving now, think you can take it?"
    g "Bring... It... On..."
    show gabesex movie
    $ persistent.gabePicnic = True
    g "Ahhhhh... this... is... amaaaaziiiiing!"
    pause
    mc "Your pussy's so wet, my dick is practically moving on it's own."
    g "Your cock..."
    g "Feels..."
    g "AMAZING!!!"
    pause
    g "Pound me harder!"
    pause
    g "Hmmmmhhhh...!"
    g "Keep going."
    mc "{i}Shit! I'm going to hit my limit."
    mc "I'm going to cum!"
    pause
    g "Do it, I already... came... twice!"
    mc "Inside!"
    g "YES!!!"
    mc "Are you sure?"
    g "Don't worry, I won't get pregnant!"
    mc "I'm cumming!"
    scene gabesexcum with flash
    pause 0.1
    scene gabesexcum with flash
    pause
    scene black with fade
    pause 0.6
    scene picnicgabe
    g "That... was... the best five minutes of my life."
    mc "I think I lasted more than five minutes."
    g "No, I kept count."
    mc "You kept count while having sex?"
    g "Yeah, I wanted to see how long I last."
    mc "...O-Ok."
    mc "You said, you won't get pregnant?"
    g "Oh yeah, I drank a contraction potion."
    mc "......?"
    g "It makes me not get pregnant."
    mc "Ohhh..."
    mc "So... you knew this was going to happen?"
    g "Heheh."
    mc "Wow, Gabe."
    mc "So you finally did it."
    g "Yeah, I finaly got laid. YAY!"
    g "Thanks again, [mc], for everything."
    mc "N-No problem."
    "The two of you lay down and relax for a while."
    g "We should do this again sometime."
    mc "For sure."
    "Several minutes pass and you almost fall asleep."
    g "Shall we head back then?"
    mc "Mh? Yeah, sure, I was falling asleep."
    g "Hehehe, me too."
    "You go back to Randel with Gabe."
    scene villageback with fade
    show talkshgabe
    show smilemc
    g "Today was great in so many ways."
    show talksadhappymc
    mc "Hehehe, yeah. I enjoyed it too."
    g "Goodnight then, [mc]."
    mc "Goodnight."
    scene homenight with fade
    mc "{i}Gabe is very... different compared to the other girls I know."
    mc "{i}She doesn't love me... but at least I have a good friend."
    mc "{i}A friend with benefits."
    $ time = 4
    $ gabetrip += 1
    jump home





label gabequest3:
    hide screen hud
    show smilemc
    show talkshg
    g "[mc]?"
    mc "Hey, Gabe, what's up?"
    g "General Taliya wants to talk with you."
    show talkwanmc
    mc "With me? Why?"
    g "I don't know. Oh, here she comes."
    scene academytalk
    show tarm talk
    show cutegop
    show talkmc
    t "Recruit [mc]."
    mc "Yes, ma'am."
    t "I got word about the goblin encampment you discovered recently. I was ordered to get rid of it."
    t "I'll be needing your help in locating their castle. Will you provide your assistance?"
    mc "Yes, ma'am!"
    t "Good. We are leaving now."
    mc "Now?"
    t "Yes. Do you have a problem with that, recruit?"
    mc "Uhm... N-No. Am I the only one you're taking with you?"
    t "Yes."
    mc "B-But their camp is quite large... I-I think we'll need more m-men."
    show tarm angryt
    t "Are you doubting my capabilities, recruit?"
    mc "N-No, ma'am... I was only... suggesting."
    show tarm normal
    t "......"
    show tarm talk
    t "I'm aware that they have the numbers, but we have no choice. There's been a breach in the wall. I've sent all the soldiers in the barracks to provide assistance."
    play sound horror
    mc "{i}The wall's been breached?!"
    stop sound fadeout 3
    g "A b-breach?"
    t "It's only a small one. Threat levels are low."
    t "I wanted to get this goblin problem out of my hair first. So the sooner we get this over with, the better."
    mc "Yes, ma'am."
    t "Good. Let's move."
    stop sound fadeout 3
    show talksgop
    g "Uhm... General Taliya? I would like to come too."
    show tarm normal
    show normalmc
    show talksgop
    t "......"
    scene academytalk
    show talksgop
    show talksadhappymc
    show tarm normal
    mc "She was with me when I found the camp."
    show tarm talk
    t "You can come, but try not to slow us down. Mages are the least reliable in my experiences."
    hide tarm talk with easeoutright
    hide talksgop
    show cuteg
    g "...Yes, ma'am."
    play music forest
    scene ambush1 with fade
    "The three of you go to the forest. General Taliya walks behind, keeping her distance. You hear the rhythmic clanking of her armor. Gabe walks next to you."
    "She looks back and then whispers to you."
    g "On Astylla, I hate her."
    mc "Shhh... she might hear you."
    g "I don't care."
    g "\"Mages are the least reliable in the battlefield\". Buh! Who does she think she is?"
    mc "...She's an experienced general, you know."
    g "Oh c'mon, [mc]. Just because she looks cool you think she's a badass general?"
    mc "I've heard stories."
    g "Stories... Heh, what kind?"
    mc "I heard she killed three minotaurs by herself."
    g "And you believed it?"
    mc "Well..."
    g "How stupid are you? Do you know how big a minotaur is? It's bigger than your house. To kill three of them? Impossible!"
    mc "It could be possible. I've seen super strong people in the Guild and they're just adventures. She must have years of military training, so I can kinda imagine what she could be capable of."
    t "Can the two of you stop your chatting and keep your eyes on the road? You might get us lost."
    mc "Sorry, ma'am."
    t "How far is the place you got ambushed?"
    mc "We're getting close."
    t "Good, keep your guard up. We could run into them."
    mc "Yes, ma'am."
    t "Mage girl, stay behind you friend."
    g "...Yes, ma'am."
    "Gabe slowly moves behind you. You can tell she's pissed."
    "The three of you walk for some time."
    scene forrest with fade
    "You finally come to the place where you met Gabe"
    show worriedgabeop
    show talkmc
    show tarm normal
    mc "It was right around here where I met Gabe."
    t "What happended here?"
    mc "We were ambushed."
    hide worriedgabeop with easeoutleft
    g "I was caught by a trap right around he-"
    show suprised with vpunch
    g "AHHHHH!"
    mc "Gabe!"
    scene forrest
    t "Pathetic, they set the trap in the same exact spot. I was told these goblins were smart."
    mc "Gabe, hold on!"
    g "I can't believe I got caught again."
    t "Recruit!"
    t "We have company."
    play music battlemusic1
    scene goblinfighttalia
    mc "{i}Shit! There's a lot more than before!"
    mc "Look out, they have poisonous darts!"
    "A dart hits Taliya's armor, it bounces away without leaving scratch."
    mc "Oh yeah... you have armor."
    mc "{i}That leaves me open."
    g "Don't worry, [mc], I've got you covered."
    g "BADAKA SHAKTHI!"
    show goblinfighttalia2 with flash
    play sound magic
    "A purple glow covers your body. The darts are repelled off you."
    mc "Whoa, thanks!"
    t "Get her down, I'll deal with them."
    mc "Y-Yes, ma'am."
    scene goblintalia with flash
    pause
    "All the goblins start to pounce at Taliya. She cuts down every one of them before they reach her. Her sword swings are elegant but deadly."
    "You see her dance with the blade, and goblin limbs fly off in each direction."
    show goblintalia1 with dissolve
    "Both of you can only watch as she massacres the entire goblin horde."
    "You cut the net and free Gabe."
    $ persistent.taliyaGoblins = True
    scene forrest with fade
    stop music fadeout 3
    show talksadhappymc
    show talkshgabe
    mc "Are you alright?"
    g "Yeah."
    mc "Thanks for covering me."
    g "No problem, couldn't be completely useless like last time."
    mc "Could've used it last time."
    g "I learned it recently, first time I used it actually. Thank Astylla it worked."
    show tarm talk with easeinleft
    t "Great work, recruit!"
    mc "Uhm... but I didn't do anything, ma'am."
    t "You followed my order to cut her down. Following orders is what a soldier is supposed to do."
    mc "Th-Thank you, ma'am."
    t "You did good too... recruit Gabe."
    t "Protecting your friend with your magic is wise, especially if he's freeing you."
    scene forrest
    show smilemc
    show talkshgabeop
    show tarm talk
    g "Thank you... ma'am."
    scene forrest with fade
    "General Taliya looks at her bloody blade. She grabs her cape and starts to wipe it."
    menu:
        "Offer her a piece of cloth":
            show tarm normal
            show talksadhappymc
            mc "Ma'am, I-I have a piece of cloth with me. Here, take it."
            "Taliya looks at you."
            show tarm talk
            t "Thank you, recruit. I appreciate the gesture, but I always wipe my blade with my cape."
            mc "Oh... ok, ma'am."
            show tarm angryt
            t "Stop calling me ma'am everytime, recruit."
            t "It's annoying."
            mc "Yes, ma- ...Ok."
            window hide
            pause 0.1
            show tarm smile with dissolve
            pause 0.5
            hide tarm smile with dissolve
            mc "{i}Was I seeing things or did she just smile?"
            $ taliarel += 1
            "You watch as she cleans her blade. The red blood stains disappear into her red cape."
            mc "{i}I'm starting to think that cape wasn't originally red."
            scene forrest with fade
            show tarm talk
            show smilemc
            show normalgabeop
            t "Where to now?"
            show tarm normal
            mc "We were kidnapped here, I-I blacked out."
            show talkshgabeop
            g "I know which way. I was awake."
            hide tarm talk
            t "Good, lead the way then."
            g "...Ok."
            scene ambush1 with fade
            "You follow Gabe. Taliya walks behind you as usual."
            g "I think she likes you."
            mc "Shut up!"
        "Don't do anything":
            "You watch as she cleans her blade. The red blood stains disappear into her red cape."
            mc "{i}I'm starting to think that cape wasn't originally red."
            scene forrest with fade
            show tarm talk
            show smilemc
            show normalgabeop
            t "Where to now?"
            show tarm normal
            mc "We were kidnapped here, I-I blacket out."
            show talkshgabeop
            g "I know which way. I was awake."
            hide tarm talk
            t "Good, lead the way then."
            g "...Ok."
            scene ambush1 with fade
            "You follow Gabe. Taliya walks behind you as usual."
    scene castle with fade
    "You arrive at the castle."
    t "Draw your swords and eyes peeled."
    "The three of you enter the castle."
    "You hear the echos of wind coming through the broken walls of the castle but nothing else. The castle is empty."
    t "Hmmm... they were smart enough to run, I'll give them that."
    t "No point in tracking them down now, they've probably gone deeper into the forest."
    t "Looks like they took everything with them. I'll search the area in case they left something behind."
    t "Keep your guard up. Who knows, they might be waiting for an ambush."
    "The two of you nod."
    scene castle with fade
    show normalmc
    show yellgabe
    g "Those bastards ran away!"
    show angry
    mc "Yeah."
    g "I wanted to get them so bad."
    mc "Yeah, me too."
    mc "{i}Fucking Leshek. I guess he got news of what's coming for him, so he scrammed. Can't blame him honestly."
    mc "{i}If I heard that woman was coming for me, I would run without second thoughts."
    scene castle with fade
    t "As I expected."
    t "The two of you spread out and look for anything they might have left behind."
    g "Yes ma'am."
    g "[mc], you search that place, I'll look around there."
    mc "Alright."
    "You head to the area Gabe pointed out to. It's a storage room."
    "You look around for awhile but you find nothing. Just some barrels and empty crates."
    "As you turn to leave you hear a thud."
    "And then a whisper."
    "Goblin 1" "Shhhh!"
    "The sound is coming from a closed barrel. You get closer."
    scene goblinkid1 with fade
    "Goblin 1" "He might've herd us."
    "Goblin 2" "He's gone now right?"
    mc "{i}There's someone inside the barrel!"
    mc "{i}Ok, be ready [mc]."
    "You draw you sword and open the barrel lid with a swift motion."
    scene goblinkid2 with vpunch
    mc "{i}GOBLINS!"
    mc "{i}These.....are......kids."
    "Goblin 1" "I-I'm scared Jark."
    mc "{i}But they're still goblins. What should I do?"
    menu:
        "Call General Taliya.":
            $ evil += 1
            $ good += 1
            "Goblin 2" "Don't worry I'll protect you."
            mc "General Taliya I found some Go-"
            "Before you can say anything one of the little goblins pounces at you. You fall to the ground."
            scene castle with vpunch
            "Despite it's size the goblin is heavy, heavy enough to pin you to the ground."
            "Goblin 2" "Run! Run gark!"
            "The other little goblin jumps out of the barrel and starts to run to the door."
            "The little goblin can get so far until it's path is interupted by a tall shadow. General taliya stands at the door blocking it's exit."
            "Without hestation she brings down her blade on the little goblins head. It falls to the ground with its head split open."
            "Goblin 2" "Noo!"
            "Taliya swiftly moves towards you and strikes the goblins thats pinning you. It falls to the ground dead."
            mc "{i}Huff... Huff..."
            show tarm talk
            t "Are you alright recruit?"
            mc "Y-yes."
            hide tarm talk
            show tarm normal
            show talkshgabeop
            g "[mc], Wh-what happened."
            mc "Those goblins..I found them in that barrel."
            hide tarm normal
            show tarm talk
            t "It's a good thing you called for me while you could. Otherwise who knows what would've happened."
            hide tarm talk
            show tarm normal
            mc "......"
            mc "Yeah."
            "You look at the two dead goblins."
            mc "{i}Would they really hurt me?"
            mc "......"
            mc "{i}No point thinking about it now."
            hide tarm normal
            show tarm talk
            t "I think we've searched the whole area."
            hide tarm talk
            show tarm normal
            hide talkshgabeop
            g "Yes."
        "Close the lid.":
            "Goblin 2" "Don't worry I'll-"
            scene goblinkid1 with vpunch
            "You slam the lid shut."
            mc "{i}I can't do it. These are just children, I just can't!"
            "You see Taliya come to the door."
            t "Anything in here?"
            mc "N-nothing."
            t "Good, come on then, we searched the whole area. theres nothing here."
            mc "I hope I made the right choice"
    scene castle with fade
    t "Let's head back. Well done, recruits."
    scene ambush1 with fade
    "The three of you walk back to Randel."
    scene villageback with fade
    show tarm talk
    show smilemc
    show normalgop
    t "Good work today, recruits. I'll be heading to Hern now... take care."
    "Gabe and [mc]" "Yes, ma'am."
    t "Recruit [mc], tell your uncle I'll be coming to see him soon."
    if taliarel == 1:
        mc "Yes."
    else:
        mc "Yes, ma'am."
    hide tarm talk with easeoutright
    pause 0.3
    scene villageback
    show talksgabe
    g "Alright. I'm going home, feel tired after all that walking."
    show talkwanmc
    mc "Yeah, me too. Bye, Gabe."
    show talkshgabe
    g "Bye, [mc]."
    scene homenight with fade
    $ gabequest3 += 1
    $ time = 4
    jump home
