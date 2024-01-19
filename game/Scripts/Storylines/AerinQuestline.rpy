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
        "Book" "{i}Dururthu{/i} Day 23: Today I got a letter from the village. It said that I should come to the village immediately. I'm sure this has something to do with the duel."
        "I stalled this enough. I think I should end this. I can't run away from this anymore."
        mc "{i}Woah, this is Eve's diary! She's 324 but still has a diary?"
        mc "{i}It kinda makes sense though. When you live for about 500 years, you are bound to forget things. I guess that's why she has one."
        mc "{i}Wait! I think I found what I was just looking for. Yes! This could have something about her weakness!"
        "You flip through the pages."
        "While you're going through the pages, your name catches your eye."
        mc "Huh, it's about me."
        "Diary" "Today, a young boy named [mc] joined the Guild. It was so refreshing to see a small boy in the Guild after so long. I hope he does great..."
        mc "......"
        "You keep turning the pages."
        "Diary" "[mc] came today and asked me if he could join our party. I was shocked. I'm sure Sander had something to do with this. I couldn't let the little one join our party; he's still inexperienced. What if he gets hurt?"
        "Diary" "But looking at him, I saw myself when I was little. Eager for adventure, not a care for the danger that lies ahead. He said that he would do anything to prove himself. He was so adorable."
        mc "{i}I'm not adorable! I'm 19!"
        "Diary" "So I gave him a task of hunting three alpha falcons. It was the easiest thing I could think of, I just wanted to see if he was willing enough."
        "Diary" "Today the little one completed his task; he brought three Alpha falcons. I was pretty impressed that he was able to do it so quickly, the boy has talent. So I told him that he could join. He was really happy to hear it, I could tell."
        "Diary" "I can't wait for the adventures we'll have together."
        "Diary" "Just came back from our first quest with [mc], we had a great time."
        "Diary" "We ran into a group of goblins."
        if savedbyeve1 == 1:
                "Diary" "The little one almost got attacked, I had to save him. We should have chosen a less dangerous quest."
        else:
                "Diary" "The little one took out two goblins on his own. He was really stronger than I anticipated, he must have trained a lot."
        "Diary" "We found the treasure we were looking for. Then we camped for the night. I caught Sander for the hundredth time peeping while I was bathing. And what's worst is he had brought the little one with him this time."
        "Diary" "I was so embarrassed; the little one has no knowledge of these things, not like that pervert Sander. I hope I didn't taint the little one's mind. I had to teach them a lesson, so I had to give them a good beating."
        "Diary" "We talked for a while at the fire after that. I learned a lot about [mc]. He's such an innocent child. I have this strange feeling, like I want to protect him, do what's best for him. I think it's what you call a motherly feeling. It's very strange indeed."
        mc "{i}Eve... I feel bad for doing this."
        mc "{i}Ok, enough of this. I must find something about Eve's weakness."
        "You keep turning pages and reading through them."
        "Diary" "Went on a quest with Sander..."
        "Diary" "Bought new boots for Sander's birthday..."
        "Diary" "Made Milly a small bow..."
        "Diary" "Helped July with work..."
        "Diary" "Caught Sander peeping..."
        "Diary" "Went to the Library. Drank tea with Lori..."
        "Diary" "Caught Sander peeping... Accidentally  broke his jaw..."
        "Diary" "Went to the village and played with Milly..."
        "Diary" "Hunted a night owl..."
        "Diary" "Sander blew Rosa Flower pollen at me... felt dizzy..."
        "Diary" "Sander brought a big boar today, it was delicious!"
        mc "{i}Wait!"
        "You turn back the pages"
        "Diary" "Sander blew Rosa Flower pollen at me. He knows I'm allergic to it. Whenever those things reach my nose, I feel dizzy. That Sanders always messing around, I wonder when that man would grow up. But to be honest, having a childish companion is fun."
        mc "{i}Bingo! I could use this. She's allergic to Rosa Flower pollen."
        if chartrait == 1:
                mc "{i}Rosa Flower are those pink flowers. I read about them in the Plants of Astylla book. I think I might find them in the outer valley."
                mc "{i}So, what I have to do is find the flower and get the pollen. Then I'll use it on Eve just before the duel."
                scene black
                "You lock the door and give the key to July."
                $ time += 1
                $ aerinpath += 1
                $ knowrosa += 1
                jump guild
        mc "{i}What's a Rosa Flower?"
        mc "{i}Shit!"
        mc "{i}Wait... I could ask Lori. She reads a lot of books, she has to know."
        mc "{i}So, what I have to do is find the flower and get the pollen. Then I'll use it on eve just before the duel."
        scene black
        "You lock the door and give the key to July."
        $ time += 1
        $ aerinpath += 1
        $ askloriaboutrosa += 1
        jump guild


label aerinbadend:
        $ aerindead += 1
        hide screen hud
        show thinkmc
        mc "{i}I wonder how Eve's doing?"
        show talkangryn with easeinright
        mc "Hey, Nessa where you goi-"
        n "[mc], it's Aerin!"
        mc "What!"
        n "Come quick!"
        scene black with fade
        "You follow Nessa, you can tell that she's in a hurry."
        mc "{i}What's going on?"
        scene elfgraves with fade
        play music windhowl
        "You reach the elf graves."
        "The graveyard is quieter than usual. You see Zenelith standing in the distance, you can make out another figure on the ground in front of her."
        "The both of you run to the scene."
        scene aerindead with fade
        $ persistent.aerinDead = True
        $ aerinDead = True
        if bothpath >= 1 or aerinpath == 1:
                mc "No..."
                mc "No... this can't be happening!"
                mc "{i}Sh-She said... she would come with me!"
                "You are soon joined by Eve."
        else:
                mc "{i}Oh no..."
                mc "{i}Oh no... Oh god no! It's Aerin!"
                "You are soon joined by Eve."
        e "Wh... What happened?!"
        zn "I caught her trespassing. I asked her to leave but she refused. She drew her weapon at me, so I had... no choice."
        e "No... Aerin... {i}sob{/i} ...How could you?!"
        n "{i}sob"
        e "How could you?! How could you do this to her?!"
        zn "She was trespassing."
        e "She must have come here to... see her brother's grave..."
        zn "That doesn't justify her actions."
        e "You.... YOU BITCH! {i}sob"
        e "GET OUT OF MY SIGHT!!!"
        zn "How dare you insult me!"
        e "I don't care, I'm the elder! Upon my orders as leader of this village, you will no longer have authority over this village!"
        zn "That's just preposterous!"
        if bothpath >= 1 or aerinpath == 1:
                "You're unable to process what's happening around you. You're unable to utter a single word."
                mc "{i}She said... she said..."
                mc "{i}She would be ok..."
                scene black with fade
                "You don't feel anything, everything went silent. You head back to Randel without looking back, leaving the grim tragedy behind. You fall to bed as soon as you're home."
                show text " {color=#fff}I could have saved her...{/color}"
                with dissolve
                pause
                hide text with dissolve
                $ time = 4
                jump home
        mc "{i}Eve... Why did Aerin's death hit her this hard... Maybe deep down, she still saw Aerin as her friend..."
        mc "{i}I should probably leave, give Eve some space..."
        "You leave the elf village and head home."
        $ time = 4
        jump home


label aerinparty:
scene aerinhouseparty
play music happy
"When you go out of the room, you see the house is filled with elves getting ready for the party."
"{i}I don't think I've ever seen that many Elves gathered in one place like this. It almost reminds me being in the Guild back home. The air's filled to the brim with energy. I know Nessa said she and the others didn't do anything too fancy but nonetheless, the place looks great."
"{i}I really hope that Aerin enjoys the redecorating and surprise."
show smilemc
show smilee with easeinright
pause
show talkhe
e "Little one, get ready. Aerin's almost here."
show talkwamc
mc "Right!"
scene black with fade
"All of you, get ready to surprise Aerin."
scene aerinhouseblr with fade
show normaln
n "Come on, Aerin!"
a "Yeah, I'm coming, I'm coming!"
show normala
a "Now, what did you say my bro-"
hide normaln with easeoutleft
menu:
        "Surprise!!!":
                play sound ("suprisegirl.wav")
                show wtfa with vpunch
                pause 0.1
                show shytalkha
                "Everyone" "SURPRISE!!!"
                a "Wh-What's this?!"
hide wtfa
show normaln
show talkheop
e "A surprise party...?"
a "F-For me?"
show talkwan
n "Of course, it's for you! Everyone's been getting this ready since morning!"
a "Th-Thank you everyone."
a "You were a bit too lou-"
show thinkmc with easeinright
mc "{size=-5}Too honest, too honest!"
hide thinkmc with easeoutleft
a "I mean- You guys were too looovely. Yes, too lovely! Hehehehe..."
n "AAAALRIGHT! Let's get on with the party now, shall we?! "
a "Yeah!"
scene aerinhouseblr with fade
"The party starts. Everyone starts talking to Aerin."
"{i}I know that this isn't really Aerin's style but she's adapting quickly and looks dangerously close to having fun."
scene aerinhouseblr
show smilemc
mc "{i}Ahh... this looks great. Everyone's having a good time. I wish Sander was here to see this."
"Woman" "Yoo-hoo!"
show girlsander with easeinleft
show thinkmc
mc "Oh... H-Hi?"
mc "{i}Jeez, wha- Who is this?"
"Woman" "Hey handsome, I'm Mary. You must be the great hero I've been hearing about."
mc "Oh... Hehehe, they must be exaggerating. I really didn't do much."
"Woman" "Of course you did! You got rid of that fat cow all by yourself they say!"
mc "Well, I didn't do it alone. I had some help- wait... Sander?"
sa "Hahahahaha! Took you long enough!"
show talkwamc
mc "Haha! What the hell are you doing, Sander?"
sa "I'm in disguise."
mc "I see that but why? You know you aren't banished anymore, right?"
sa "I know... b-b-but these women. They're animals! Last night I came to meet Eve, these things suddenly jumped out from the darkness and they... They just didn't stop!!! {i}sob"
mc "......"
sa "I barely got out alive. So, this time, I came prepared."
mc "Where did you even get those clothes from?"
sa "I found them."
mc "\"Found them\" or stole them, on one of your peeping missions?"
sa "A good adventure sometimes has to skip the little details. Hey but tell me. How the hell are you still walking on two legs?"
mc "What do you mean?"
sa "These women, didn't they..."
mc "Oh, Nessa covered for me. She told everyone in the village that... I have a sexually transmittable disease."
sa "What?! Hahahahahaha! Why didn't I think of that?"
show talkheop with easeinright
e "Oh, Sander, you're back. Nice to see you."
mc "Wait, you recognized him?"
e "It's not the first time I've seen him like this."
sa "Hehehehe..."
sa "Eve, would you be so kind as to lead me to the rum?"
e "Right this way."
hide talkheop with easeoutright
hide girlsander with easeoutright
show smilemc
mc "{i}Hehehe, they realy know each other well."
show happya
a "[mc]!"
show talksadhappymc
mc "Aerin, finally got the time to talk to me, huh?"
a "You... you..."
"Aerin hugs you."
show blushtalka
a "Thank you so much [mc], I don't know how I could-"
mc "Awww, you're just like your brother! It's over, I'm glad I could help. Now just enjoy the party."
a "{i}sob{/i} Ok."
mc "Come on then!"
a "Ok- Oh, wait. Please give me a moment."
scene aerinbroyell1
pause 0.5
scene aerinbroyell2 with vpunch
pause 0.5
a "Keep your hands off him! He's still supposed to be resting!"
scene aerinbroyell3
mc "{i}She's already getting into the elder role, I see."
scene partyaerin with flash
"Everyone starts to dance and have a good time."
pause
"{i}I guess I'm not that used to parties either but I'd be lying if I didn't say I was having a ball. The room is warm with the heat of people dancing like lunatics. It seems like after a few drinks, no one here cares about how they look. It really is a sight to behold."
scene sandercaught1
pause 0.3
scene sandercaught2
pause 0.3
scene sandercaught1
pause 0.3
scene sandercaught2
pause 0.3
scene sandercaught1
pause 0.3
play sound horror
scene sandercaught3
pause 0.5
scene sandercaught4 with vpunch
pause 0.9
play sound runfunny
scene sandercaught5 with hpunch
pause
scene sanderchase
sa "HELP MEEEEEEEE!!!!!!!"
"Eve and [mc]" "Run, Sander, RUN!!!"
scene aerinhouseparty with fade
"After some time, the party dies down. Aerin thanks everyone for coming."
mc "{i}Even with everyone leaving, no one seems sad about it. In fact, they all seem happy. It's a pretty safe bet, even one Sander would win, that the night isn't ending for some of them. I guess it goes to show even if you live for hundreds of years, everyone likes to cut loose and have fun at times."
stop music fadeout 1.0
scene aerinhouseparty with fade
show smilemc
show talkhe
e "What a party that was."
show talkwamc
mc "Yeah, it was awesome!"
e "Are you heading out as well?"
mc "Yeah, after I talk to Aerin. "
show blushtalke
hide talkhe
e "Oh... ok. I'll be taking my leave then. Milly says she's exhausted."
mc "From joy, I'm sure. Milly must be happy now that everything worked out."
e "She is. Hehehe."
e "Goodbye, little one."
show smilemc
hide normale
hide blushtalke with easeoutright
pause
show happya
mc "Hey Aerin, I was just about to talk to you."
show blushtalka
a "Umm... shall we go outside then?"
mc "Huh?"
a "I-It's a bit hot in here, we could get some fresh air. I have a balcony, we could go there... if you want, that is."
mc "Yeah, ok. Where's Morgan?"
a "He's asleep."
mc "Oh good, let's go then."
scene mcatalkh with fade
mc "Wow, this place is great"
play music nurture
a "It's relaxing, isn't it?"
mc "It sure is."
a "......"
mc "......"
mc "So how's it feel to be the Elder?"
a "I-I don't know, it's great, I guess."
mc "You guess?! You've wanted this your whole life!"
scene mcatalks
a "Yeah but so many things have happened. It almost feels too good to be true."
a "I became the Elder, I got my brother back. I got my friends and village people back and..."
scene mcatalkh
a "I met you."
mc "......"
mc "{i}How do I respond to that? Come on, think of some cheesy line..."
mc "I'm glad that I met you too."
scene mcak3
a "{i}Blush"
mc "{i}Nailed it!"
a "I know you don't like being thanked a lot but I have to say it. Thank you [mc], you've given me everything. I don't know how I'm supposed to repay you."
mc "Just be happy, don't be sad anymore. That's all I want."
a "[mc], I'm getting this weird feeling. Something I haven't felt before"
mc "......"
a "I think... I..."
a "I think... I... love you."
mc "...I... feel the same way."
scene mcak1
pause 0.5
scene mcak2
pause
scene mcak3
a "......"
a "Was that what you call a \"Kiss\"?"
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
mc "Y-Yeah, sure."
a "You can come see me at the temple if you want."
mc "In the temple?"
a "Yeah, I'll be at the Elder Room. There's a lot of work for me there. It turns out being the Elder isn't as easy as I thought. Hehehehe."
mc "Haha, I'm sure you'll have your hands full. I'll see you there then."
a "Bye."
mc "Bye."
scene elfvillagen with fade
mc "{i}I can't believe she kissed me. Aerin finally got to be happy. My job here is done."
$ time = 4
"You head back home."
$ savedaerin = 1
$ elfday = day
jump home


label aerinkiss:
        hide screen hud
        mc "I wonder how's Aerin doing, where do I even find her?"
        mc "I should ask one of the guards."
        "You walk up to the guard next to the temple's entrance."
        mc "Uhm, excuse me? ...Where I can find Aerin, the... village elder?"
        "Guard" "She's in the high elf's chamber."
        mc "Can I meet her?"
        "Guard" "What does the elder want with a human?"
        mc "I-I'm a friend of hers, just tell her [mc] has come to see her."
        "Guard" "Fine."
        "The guard leaves. After a few minutes, she comes back."
        "Guard" "The elder will see you. She's in the temple, on the fifth floor."
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
        a "Can you believe it? All the elders before me sat on that exact place!"
        mc "It's pretty amazing."
        mc "So what you doing now?"
        show shytalka
        a "{i}sigh{/i} Work."
        a "It keeps piling up. Since... Zenelith is gone, I've got more work."
        mc "Don't worry, I'm here to help!"
        a "Really?"
        mc "{i}Now I have to argue my way to help her."
        show happya
        hide shytalka
        a "That's great!"
        mc "......"
        mc "{i}Ok, I was wrong."
        mc "Thank god, I thought I would have to force you to let me help."
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
        a "For caring about me. I still don't understand why you did it but I wanted to thank you."
        mc "I really didn't do anything."
        a "You're talking to me, telling me that you would help me win. That meant so much to me."
        mc "Aerin..."
        a "I don't think I would be here if you didn't show up in my house that day."
        mc "......"
        a "I'm making you uncomfortable, aren't I? Hehehe. You really don't like getting praised, don't you?"
        mc "Hehehe, I guess."
        a "Ok, I'll stop then."
        mc "So... how's it like being the elder?"
        a "It was everything I hoped for but with the amount of work is a bit overwhelming, to be honest."
        mc "I could help you out with it, like I did today."
        a "Really?"
        mc "Yeah, I can... sort papers and stuff."
        a "Hehehe, that would be helpful."
        mc "{i}Aerin looks really happy. I know I had to betray Eve but after seeing Aerin like this, I think it was worth it."
        a "[mc], there's something I should tell you."
        mc "What?"
        a "For a while, I've had this strange feeling about you..."
        a "It's something I've not felt before."
        mc "......"
        a "I think... I..."
        a "I think... I... love you."
        mc "...I... feel the same way."
        pause
        scene mcak1
        pause 0.5
        scene mcak2
        pause
        scene mcak3
        pause
        a "......"
        a "Was that what you call a \"Kiss\"?"
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


label romanceaerin:
scene aerinhouseblr with fade
pause
scene teaaerin with fade
"You two have a chat while you have your normal cup of tea and Aerin's delicious muffin."
if evelost == 2:
        $ aerinconfes += 1
        show screen notice
        pause
        hide screen notice
        scene aerinhouseblr
        show blushtalka
        show smilemc
        a "Uhm... about that night, I-I really meant it!"
        a "I do love you. Sorry if I don't show it that much. I'm just not used to it, you know?"
        show talksadhappymc
        mc "I know, let's take our time."
        a "Thank you for understanding, [mc]."
        mc "You take care now. I'll come back to help you with your work."
        show shytalkha
        a "Ok. Bye, [mc]."
        $ time += 1
        jump elfvillage
show screen notice
$ aerinrel += 5
pause
hide screen notice


if aerinrel > 20:
        scene aerinhouseblr
        show shytalka
        show smilemc
        a "So [mc], are you leaving today?"
        menu:
                "Sleep at Aerin's place":
                        mc "Nah, I would like to stay with you longer... we could have some fun."
                        show shytalkha
                        a "I was thinking the same thing!"
                        scene black with fade
                        label aerin_sex_repeat:
                        if aerin_one_hour_stand > 0:
                                scene aerinhouseblr with fade
                        "The two of you undress and jump on the bed."
                        scene aerinsex1 with fade
                        pause 0.6
                        scene aerinsex2
                        pause
                        show aerinsexfinal movie
                        pause
                        a "Aaahhh... why does your dick always feel... this good?"
                        pause
                        mc "I'm cumming!"
                        scene aerinsexcum with flash
                        pause 0.5
                        scene aerinsexcum with flash
                        scene aerinasslick1 with fade
                        a "I love you, [mc]."
                        mc "I love you too."
                        scene black with fade
                        if aerin_one_hour_stand == 0:
                                "The two of you cuddle up and fall asleep."
                                call sleepvars from _call_sleepvars_2
                                scene black with fade
                                "When you wake up, Aerin's already gone. You sit on the bed and take a look around. She might have gone off to work but you think about how satisfied you feel after that eventful night."
                        else:
                                $ aerin_one_hour_stand = 0
                                mc "{i}What a break... Aerin is possaionate when riding me."
                                $ time += 1
                        jump elfvillage
                "Go home":
                        mc "Sorry Aerin, I won't be able to stay with you today."
                        show shytalkha
                        a "Oh, it's ok. Take care then."
                        mc "You too."
                        $ time = 4
                        jump elfvillage


if aerinrel == 20:
        label aerin_sex_first:
        scene aerinhouseblr
        show shytalka
        show smilemc
        a "[mc]... I... want to have sex with you."
        show surprisedblushmc
        mc "{i}She's really direct with these kinds of stuff."
        mc "Are you sure about this?"
        show shytalkha
        a "Yes, I think it's time I finally make you feel good."
        mc "{i}I can't believe it's finally happening!"
        a "Follow me."
        scene black with fade
        "You go with Aerin to her room. Both of you removes your clothes."
        a "Lie down on the bed. Today I'll provide for you."
        mc "O-Ok."
        a "Wow, your sexual organ is so big. I'm supposed to put this whole thing in me... right?"
        $ member_name = "penis" # timid
        if mcBold == True:
                $ member_name = "cock"
        if mcNormal == True:
                $ member_name = "dick"
        mc "Y-Yeah and it's called a [member_name]."
        scene aerinsex1 with fade
        a "Right, your [member_name]. I'm going to put it in me now."
        scene aerinsex2 with hpunch
        a "Ahhhh... this is amazing!"
        mc "{i}So tight!"
        show aerinsexfinal movie
        pause
        a "I can't stop moving my hips... Aaahhhh!"
        a "Does it feel good?"
        window hide
        pause
        mc "Y... Yes...!"
        a "Your [member_name] feels sooooo good!"
        mc "Ahhh... slow down... Aerin! I think I'm going to cum!"
        pause
        a "Do it! Cum inside me, give me your seed!"
        pause
        mc "Agh!!!"
        scene aerinsexcum with flash
        pause 0.05
        scene aerinsexcum with flash
        pause
        scene aerinasslick1 with fade
        a "That... was... amazing... Sex is amazing!"
        mc "It really was."
        a "Did I make you feel good?"
        mc "Yes! You were amazing..."
        a "Hehehe... thanks!"
        a "Umm... [mc]. I know... you being from the outside world and all.. you might do this with a lot of women."
        mc "Aerin, I-"
        a "It's okay, I understand. You are a human, after all... but all I ask is to remember me. To remember the time we had together."
        mc "I will, I promise!"
        a "I'm glad."
        if aerin_one_hour_stand == 0:
                scene black with dissolve
                "The two of you cuddle up and fall asleep."
                call sleepvars from _call_sleepvars_3
                scene aerinhouseblr with fade
                "When you wake up, Aerin's already gone. You sit on the bed and take a look around. She might have gone of to work but you think about how satisfied you feel after spending the night with her."
        else:
                $ aerin_one_hour_stand = 0
                mc "She is always so wild. I can't get enough of her."
                $ time += 1
        jump elfvillage


if aerinrel ==  15:
        scene aerinhouseblr
        show shytalkha
        show talksadhappymc
        a "Uhm, [mc], do you want to... continue from where we left off last night?"
        mc "Y-Yes!"
        scene black with fade
        label aerin_sex_licking:
        "You go to Aerin's room. Aerin undresses. She lies on her bed fully naked. You take a moment to admire her shape and curves and beautiful body, down from the supple skin to the details of her buttocks."
        scene aerinasslick1 with fade
        a "What are we going to do today?"
        scene aerinasslicka5 with vpunch
        a "Hey! At least give me a warning!"
        show animationaerinlick
        mc "Sorry, I couldn't resist that juicy ass."
        a "Aaahhh... don't say that..."
        pause
        a "Aaahhhhh... I think I'm going to cum again!"
        pause
        scene aerinasslicka7 with flash
        pause 0.05
        scene aerinasslicka7 with flash
        a "I'm cumming!!!!!!!!!"
        scene aerinasslick1 with fade
        a "I didn't even return the favor and make you feel good today. I'm such a terrible lover..."
        mc "Hey! It felt good licking your ass."
        a "Don't say that... It sounds... dirty..."
        mc "Hahahaha. But I know you like it."
        a "I... kinda do!"
        mc "It's getting dark, time for me to go then... Take care, ok?"
        a "You'll come back tomorrow, right?"
        mc "Yeah, I will. Can't live without me, huh?"
        a "YES!!!"
        mc "Hehehe..."
        $ time = 1
        jump elfvillage


if aerinrel == 10:
        scene aerinhouseblr
        show shytalka
        show smilemc
        a "So [mc], about us... I was thinking... since... now we are together, I thought we could do... stuff?"
        mc "Like what?"
        a "You know... the things lovers do..."
        show talksadhappymc
        mc "Like go on dates? Yeah sure, I would love to-"
        a "No... I mean things like..."
        show blushtalka
        a "Things like... seeing each other naked."
        show thinkmc
        mc "{i}Did I hear that right?"
        hide thinkmc
        mc "Wh-What- I think I-I misheard y-you-"
        a "I said we... should... see each other naked."
        show surprisedblushmc
        mc "{i}Oh god, I think I'm going to faint!"
        mc "Oh, hahahahaha! ...I-I thought you wanted to take things s-slow, right?"
        show shytalkha
        a "Well, it was you who said that. And you told me to be honest with my feelings. So I feel like we shouldn't stall. If we love each other, there's no reason to wait."
        mc "{i}gulp{/i} You're right but are you sure about this?"
        a "Yes. So... what do you say?"
        show talksadhappymc
        mc "If that's what you want, I'm fine with it."
        a "Let's go to my room then"
        scene black with fade

        label aerin_sex_fingering:
        "You go to Aerin's room. Aerin undresses. She lies on her bed fully naked. You take a moment to admire her shape and curves and beautiful body, down from the supple skin to the details of her buttocks."
        scene aerinasslick1 with fade
        pause
        mc "Wow... you... look beautiful!"
        a "Th-Thank you."

        scene aerinasslick1 with fade
        a "I really have no experience with these kinds of things. [mc], I leave the rest to you."
        mc "{i}gulp. Who does she think I am? I've got no experience either!"
        mc "O-Ok."
        a "I know I said we shouldn't stall but I-I... don't want to rush things either."
        mc "I-I understand."
        menu:
                "Finger her":
                        scene aerinasslicka1 with dissolve
                        a "Th-That's my... W-What are you doing?"
                        mc "Just, relax I'm going to make you feel good."
                        a "But... I want to make you feel good too-"
                        show animationaerinfinger
                        a "Aaaahhhh...!"
                        pause
                        window hide
                        mc "Do you like it?"
                        a "Yes! It feels good... Ahhh!"
                        mc "{i}She's getting really wet."
                        a "Aaaahhhh... wait... I feel something...!"
                        pause
                        mc "You're going to cum."
                        a "I'm going... to... what?"
                        a "You're going faster... my pussy... Aaaahhhhhh... I'm cumming!!!!!"
                        hide animationaerinfinger
                        scene aerinasslicka4 with flash
                        pause 0.05
                        scene aerinasslicka4 with flash
                        a "Aaaahhhhhhhhhh!!!!!!!"
                        a "{i}huff... huff... huff..."
                        scene aerinasslick1 with fade
                        a "That felt amazing, [mc]!"
                        mc "I'm glad you liked it."
                        a "I feel sleepy..."
                        mc "I think we've done enough for today then..."
                        a "But I didn't make you feel good."
                        mc "It's ok, we'll do this again tomorrow."
                        a "O-Ok... see you tomorrow."
                        scene elfvillagen
                        mc "{i}That was amazing! I didn't get much action though. Still, I think Aerin had a good time!"
                        $ time += 1
                        jump elfvillage

mc "Thanks for the tea, Aerin."
a "You're welcome!"
mc "I'll see you tomorrow then."
a "Ok, bye [mc]."
mc "Bye, Aerin!"
$ time = 4
jump elfvillage