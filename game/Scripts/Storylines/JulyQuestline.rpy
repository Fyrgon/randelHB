default dayWhenBronze = 500

label julyFollowed:
    if greenarrow == 1 and alphafalcon < 3:
        mc "{i}I have finally reached the right level for Bronze... but I really should finish Evelyn's quest first so I can immediately into her party!"
        jump guildMenu
    elif greenarrow == 1:
        mc "{i}Eheh... Time to show Eve what I've got!"
        show normalmc
        show talkwanmc
        show normale
        mc "Ok, I did it."
        show talkwae
        e "What, really?! It would seem that I underestimated you, little one!"
        show talkwamc
        mc "And that's not all..."
        hide talkwanmc
        hide talkwamc
        "You show Eve your Exp charm"
        e "What..."
        show surprisedblushe
        e "Level [level]?! You're already bronze rank?!"
        show talkwanmc
        mc "I still haven't told July, I wanted to show you first."
        show talkwae
        hide surprisedblushe
        e "Wow... Well, go ahead and tell July, I'll go get Sander..."
        show talkhappymc
        mc "Alright!"
        $ renpy.notify("{color=#fff}Quest complete: Show Who's Alpha")
        $ greenarrow -= 1
        $ evequest +=1
        $ q2 += 1
    else:
        hide screen hud
        pause 1
        scene adgc2
        if level > 10:
            j "Wait... Level [level]? [mc], you should've come just as soon as you reached level 10!"
            j "Oh, it's fine, you reached {b}and{/b} surpassed level 10! You're officially a Randel adventurer now! No matter how many years go by, I still get excited every time."
            j "Here's your badge."
        else:
            j "Congratulations, [mc]! You reached level 10! You're officially a Randel adventurer now! Well done, I knew you could do it!"
            j "Oh, now let's not forget: here's your Bronze badge."
        show bronzebadge with dissolve
        pause 2
        hide bronzebadge with dissolve
        j "Awww! It looks good on you..."
        j "You worked hard, [mc]. You really do deserve it!"
        mc "Thanks, July. I couldn't have done it without your support."
        j "The pleasure is all mine! Now go join a party, [mc]. I know you've been wanting too!"
        mc "Sander and Evelyn told me I could join theirs."
        j "Oh really? That's great! You're lucky, being able to join such a great party."
        j "And another thing I forgot to mention in the briefing. You will get your very own room in the Guild Quarters!"
        mc "Really?!"
        j "Yeah but your room is still under construction, so it might take a while. But you can still visit the other Guild members in their quarters."
        mc "Nice!"
        j "Run along now! Go give them the news!"
        mc "Bye, July!"
        sa "Hey kid, come here."
        scene black with fade
        show text "{color=#fff}You see Sander and Evelyn coming in through the door."
        pause 2
        hide text
        sa "Yeah, we gotta new BRONZE in the house, BABY!"
        e "Keep it down, Sander! You're screaming like a maniac..."
        e "Anyway, nice work, little one... We're really proud of you!"
        sa "Same here, kid! I knew you could do it!"
        sa "This calls for a celebration! Let's drink!"
        scene bronzeparty with fade
        $ persistent.bronzeParty = True
        "Sander buys drinks and hands one to you."
        sa "You gotta drink, kid! I won't take no for an answer."
        mc "Ughh... Ok then!"
        mc "......"
        sa "Come on, drink!"
        e "Come on, drink... drink...!"
        sa "Come on, drink... drink... drink!!"
        "You take a sip from the cup."
        scene bronzeparty with vpunch
        mc "{b}Awwwaaaaak!!!{/b}"
        sa "Hahahahahahahahhahha!!"
        e "Don't laugh, Sander! He's just a kid!"
        sa "Yeah... hahahah... haha! A lame one!"
        mc "It's horrible! Why do you guys even drink this?"
        sa "You'll get the hang of it after a few drinks... come on, drink up! Don't waste the beer."
        e "It's really weird seeing him pay for drinks. This might be the last drink you'll ever get from him, so better drink up!"
        mc "Huh... Ok, here it goes..."
        "You gulp down the remaining beer."
        sa "There you go! The little kid is finally a man!"
        mc "Awwwk... still tastes horrible..."
        sa "Hahahaha! Looks like you've still a long way to go then!"
        sa "Hey! July! You want a drink?"
        j "O-Oh, no, I've still got work to do... sorry. Thank you for asking though."
        sa "Ok, fine. I guess that's one more for me!"
        e "So are you ready to go on a quest with us?"
        menu:
            "Yeah.":
                mc "Yeah."
            "Hell yeah!":
                mc "Hell yeah!"
                e "Oooh, I like the enthusiasm!"
        e "So, Sander and I heard about this cave not far from here that has a treasure."
        mc "Really?"
        s "Yes, some say that the goblins stole it from a castle and hid it there."
        e "The cave is in goblin territory anyway. So I guess it's true."
        sa "Yeah, I think so too."
        e "Ugh goblins... I hate those little devils."
        sa "Yeah, there're pretty annoying..."
        e "[mc], do you know about goblins?"
        mc "Uhm, not much... They are little green assholes from what I hear..."
        e "You'd better do some research. We will likely run into them."
        mc "Yeah, ok!"
        mc "Sooo... when are we leaving?"
        sa "Any time, little man... You just get ready and let us know. We're good to go at any time."
        mc "Oh, ok!"
        sa "Now, let's {i}paaaaarrrtaaayyy{/i}!!!"
        "Sander orders more drinks and hands them out to the other adventurers in the Guild. Sander holds up his drink."
        sa "Everyone! Here's to [mc], our new adventurer!"
        "\"Hooray for [mc]!\" the other adventurers shout."
        "After a few drinks, Sander starts singing out of nowhere. Eve joins in."
        mc "{i}Eve's voice is so beautiful. I could listen all day... Sander is surprisingly good too."
        "Some adventurers join in and starts dancing."
        "\'Hooray for [mc]!\' they shout while dancing."
        "They pull you in and start to dance around you. You have no choice but to dance with them."
        "You dance on and have a good time. After a while, the party dies down. Sander is flat on the floor as the others congratulate you and leave."
        "Eve goes and picks up Sander."
        scene agblr with fade
        show smilemc
        show talkhse
        e "Ok then, little one. The party is final over, isn't it? I had a really good time, did you as well?"
        show talkhappymc
        mc "It was awesome..."
        mc "Is Sander always like this after a party?"
        show talkwase
        e "Oh, yeah... every time. Sometimes not even at parties!"
        mc "Hahaha. It's a good thing he's got you."
        e "Yeah, otherwise he'd still be lying around somewhere."
        e "Anyway, we better leave, little one. The Guild will be closing soon."
        mc "Oh, yeah... Bye, Evelyn!"
        e "Goodbye! Let us know when you're ready to leave for that adventure."
        mc "Ok!"
        scene black with fade
        "You leave the Guild."
        stop music
        mc "I'm finally an adventurer... I can't wait to tell Uncle Pete."
        mc "This badge looks really cool too..."
        "You look at your chest but the badge isn't there."
        mc "Fuck, where is it...?"
        mc "Aghh! It must have fallen off while I was dancing!"
        mc "Damnit!"
        mc "Better go and find it before July closes the Guild."
        "You run to the Guild and open the door."
        mc "Thank god, it's not locked yet."
        scene agn with dissolve
        show thinkmc
        mc "Where is it...?"
        "You search the Guild. After some time, you finally find it lying on the floor."
        show smilemc
        scene black with fade
        mc "Yes! Here it is."
        "You put it in your pocket and leave. As you walk out the door, you see July carrying a huge bag and walk out of the Guild."
        "She didn't see you."
        mc "Is that July? Where is she going this late...? Wait...{p} I think she's going into the forest."
        "You decide to follow her as she walks silently into the forest. After a while, she stops. You quickly hide behind a bush."
        play music night
        scene julynight1 with fade
        pause
        mc "What is she doing...? It's so dark, I can't fully see what she is up to..."
        play sound horror
        scene julynight2 with vpunch
        mc "Shit!"
        scene julynight3
        mc "Did she see me?! I think she saw me... Oh shit!"
        pause
        scene julynight4
        mc "I guess she didn't... That was too close."
        pause
        mc "She's leaving."
        scene julynight5 with dissolve
        "You wait for a few minutes."
        mc "It looks like she's gone... Let's see what she was dumping there."
        "You move to the place where you saw July."
        scene deadboar with fade
        mc "What? It's a dead boar...? And it looks all shriveled up..."
        mc "What is she up to?"
        pause 3
        mc "This is creeping me out. I should get out of here."
        "You quickly leave the forest and the shriveled boar behind."
        stop sound fadeout 3
        $ time = 4
        $ dayWhenBronze = day
        $ sawjuly += 1
        $ party += 1
        jump home


label julypt2:
        hide screen hud
        hide screen screenmap
        play music creepymusic
        scene villagen
        mc "There's something shady going on with July. I think it's time to find out what's going on with her."
        scene agn with fade
        mc "This place looks pretty spooky at night."
        mc "Where is she?"
        "You look around the Guild; it's total silence seems wrong compared to how much activity goes on during the day. A mote of moonlight shines in through the window as you search for her bedroom. Besides a storage closet, you find nothing."
        mc "I wonder where she sleeps at night? I can't find her room..."
        "You feel the hair on the back of your neck stand up and goosebumps ripple down your arm."
        mc "It's that strange feeling again... like that night I saw July in the woods."
        mc "I can sense something dark. How though? It's weird."
        mc "It's coming from below me..."
        mc "Mhh..."
        "You kneel down and pull the huge bear rug. It's surprisingly heavy but you manage to pull it aside."
        "You find a trap door."
        mc "Bingo!"
        mc "It's not locked either..."
        "You open it and find a flight of stairs heading down into some sort of cellar."
        mc "She's in here, I can feel it. I've got no choice, I'm going in."
        scene black with fade
        "You descend down the stairs which lead to a pitch-black hallway. You can barely see a foot in front of you. Dread fills your mind as you press forward. You feel as if you are passing through a dark molasses; the aura of whatever is down here is dark and ominous."
        "You head along a tunnel and find a door at the end of the hallway. It's slightly ajar."
        scene julyvampire1 with fade
        "You slowly open it and find yourself in a room lit by the moonlight coming in from a small opening in the roof."
        mc "What is this place? Am I still under the Guild? How is there moonlight in here?"
        "You suddenly see someone move silently from the corner of the room."
        mc "Hey! Who's there?!"
        "You feel the dark aura coming closer."
        "You draw your sword."
        mc "Come out!"
        scene julyvampire with dissolve
        pause
        "Unknown" "Calm down..."
        mc "Wh-What are you doing here?! Where's July?"
        "Unknown" "How did you find the trap door?"
        mc "Shut up and answer me!"
        "Unknown" "How did you get past the barrier?"
        mc "What are you talking about?"
        j "[mc]... it's me, July..."
        mc "You're fucking joking."
        mc "You're not July."
        j "You have to trust me, [mc]."
        mc "Wh-Why are you covered in blood?"
        j "{i}sigh"
        j "I was feeding."
        mc "Feeding? Feeding on what?"
        j "I'll explain everything tomorrow. Please, [mc], you have to trust me."
        mc "......"
        j "I'm sorry I kept this from you but you have to promise me that you won't tell this to anyone."
        mc "What are you?"
        j "......"
        j "I'm a Vampire."
        mc "Vampire?!"
        j "[mc], please now is not the time-"
        mc "No, you have to tell me what's going on, now!"
        j "......"
        mc "I know what a vampire is. You feed on human blood."
        j "...Well, I'm supposed to."
        mc "What do you mean \"you're supposed to\"?"
        j "Listen, I'm not the monster you think I am, [mc]..."
        mc "Have you killed anyone in this town?"
        j "What, no! I would never."
        mc "Then how are you still alive?"
        j "You don't seem to be in the mindset to hear me out..."
        mc "Just tell me!"
        j "...Boars... I drink boar blood."
        mc "What?! You mean the boars that are brought to the Guild? You feed on them?"
        j "Yeah."
        mc "Why would you do that?"
        j "Because I refuse to hurt people."
        mc "Huh... and I'm supposed to believe that?"
        j "I'm telling the truth."
        mc "...Ok, tell me this; if you're actually July, how on Astylla are you able to be out in the day, in the sun?"
        j "Have you ever seen me outside in the day?"
        mc "Ehm... no but still, at the Guild, there's plenty of light."
        j "I've gotten used to minor amounts of sunlight."
        mc "Enough of your bullshit! I'm asking you again what did you do to July?!"
        j "{i}sigh{/i}... If you don't believe me, kill me."
        menu:
            "Kill her":
                $ notrustjuly += 1
                mc "Nice try."
                "You raise your sword to strike her down but as you do, July collapses to the floor."
                scene julyvampire1 with vpunch
                mc "Huh... Wh-What? Get up!"
                "She lies on the floor, unresponsive."
                mc "She's unconscious? What happened?"
                "You take a closer look."
                mc "She's out..."
                "You take a look around the room. You find a dead boar similar to the ones you hunt in the forest."
                mc "Was she actually telling the truth?"
                mc "What should I do with her then?"
                "You look to the corner she was initially hiding in and see a casket up against the wall."
                mc "I guess that's where she sleeps."
                "You lift her up."
                mc "Holy shit... she's heavier than she looks!"
                "You somehow manage to lift her into the casket. You gently lay her down and close it."
                mc "Let's see what happens tomorrow..."
                "You leave the underground area, close the trap door and put the bear rug back over the top."
                mc "I should leave now."
                $ sawjuly += 1
                jump home
            "Trust her":
                mc "I trust you."
                scene julyvampire2 with dissolve
                j "...Thank you- "
                scene julyvampire1 with vpunch
                "July's smile fades as she collapses to the floor."
                mc "July! Are you alright... July?!"
                "She lies on the floor, unresponsive."
                mc "She's unconscious? What happened?"
                "You take a look around the room. You find a dead boar similar to the ones you hunt in the forest."
                mc "She was telling the truth."
                mc "What should I do with her?"
                "You search the corner she was initially hiding in and see a casket up against the wall."
                mc "I guess that's where she sleeps."
                "You lift her up."
                mc "Holy shit... she's heavier than she looks!"
                "You somehow manage to lift her into the casket. You gently lay her down and close it."
                mc "Let's see what happens tomorrow."
                "You leave the underground area, close the trap door and put the bear rug back over the top."
                mc "I should leave now."
                $ sawjuly += 1
                jump home
