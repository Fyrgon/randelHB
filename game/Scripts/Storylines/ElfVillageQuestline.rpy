label evequeststart:
    hide screen hud
    play sound doorknock
    "{i}Knock knock"
    scene homedayblur
    show thinkmc
    mc "Huh?"
    e "It's me, little one."
    mc "{i}Oh, it's Eve."
    mc "Hey Eve, come on in."
    show normale with easeinleft
    show normalmc
    show talkwanmc
    mc "What brings you by, Eve?"
    show sadtalke
    hide normalmc
    e "Little one, I came to tell you that I'll be leaving Randel..."
    mc "You're going on a quest alone? It sounds dangerous. If you're going, just to tell me. Give me a few minutes to get ready, I'll come with you."
    e "...Little one, I mean \'really\' leaving Randel... for good."
    show suprised
    pause 0.5
    show talkwanmc
    hide suprised
    mc "Wait, what!? ...Why?"
    e "I'm sorry, it's complicated."
    mc "What do you mean? Tell me! We're partners, and I'd like to think we're friends too. I think an explanation is fair!"
    e "You don't need to worry about it, take care of yourself, Little one."
    scene homedayblur
    show worriedmc
    mc "Wait, Eve!"
    mc "{i}What the hell, why is she leaving all of a sudden?"
    mc "{i}I have to see if Sanders knows about this."
    play sound doorknock
    "{i}Knock knock"
    sa "Kid! Open up, quick!"
    mc "{i}Sander, right on time!"
    show thinkmc
    show talksads
    sa "Kid, I've got some bad news."
    mc "Eve's leaving town."
    sa "Yeah! Wait, how did you know?"
    mc "She dropped by, and told me just a few minutes ago."
    sa "Really? Well, that's good, that means she isn't far off."
    mc "What do you mean?"
    sa "Come on, Kid, we're going to follow her."
    mc "Follow her? Where?"
    sa "I'll explain on the way, just hurry and get ready. "
    scene forest with fade
    "The two of you leave. After tracking her for some time, you see Eve heading into the forest, in plain sight even as she delves deeper into the greenery."
    mc "Hey Sander, there she is."
    sa "Yeah, I see her."
    "You both follow her."
    "{i}It feels like we've been following Eve for a long time, even if the sun hasn't gone down much. Honestly... it feels like we're just hunting a woodland creature."
    "{i}It's a pretty nice day out. The sun is warm, but not overbearing. A few clouds patterned in the sky. The trees and grass are clear, vibrant shades of green from the radiance of the sunlight."
    "{i}This would feel like a great day to go for a hike through the forest... if we weren't stalking another Guild member and all."
    mc "So, can you please tell me what exactly is going on?"
    sa "I don't know, she said she had urgent business in her village."
    mc "Something urgent? It has to be pretty serious if it would make her leave Randel forever. I wonder why she didn't tell us."
    sa "I'm not completely making sense of this either, man."
    sa "Eve normally visits her village almost every day, but this seems different."
    mc "Why does she visit her village every day? I thought she hated that place."
    sa "As far as I'm aware, she does. But she has family; a sister there."
    mc "WHAT?!"
    sa "Yeah. if I were to guess, I'd say it has to do something with her."
    mc "{i}Eve has a sister? Who would've thought?"
    sa "Alright, enough talking, we should stay quiet."
    mc "Right."
    "You keep following Eve, the path she takes is one you've never seen."
    mc "We're still in the outer forest, right?"
    sa "I-I don't know, I've never been down this path before."
    mc "Hmm... that's a comforting thought."
    "{i}I've been in the forest a lot, and I've never come across this path. I know that the deeper we go, the more dangerous it'll get. And if a fight breaks out, our cover is blown."
    "{i}I'm having my fingers crossed that things don't go south."
    "She finally stops."
    scene evestalk
    pause
    window hide
    sa "{size=-5}She stopped."
    "Eve glances from left to right to see if anyone is around."
    pause
    mc "What is she doing?"
    sa "{size=-5}Shh... don't get us caught... like last time. "
    mc "Last time? That was your fau-"
    sa "SHH!!!"
    mc "{size=-5}Ok, ok, enough with the shushing."
    scene evestalk2
    $ persistent.followedEve = True
    mc "{size=-5}What? She went inside the tree!"
    sa "{size=-5}Hehe, nice. Well, little man, I think we just discovered the passage to the elf village."
    "You scout the area for a bit. You slowly head into the tree."
    scene black with fade
    stop music
    mc "{i}Man, it's really dark in here."
    "......"
    "........."
    mc "Is something supposed to happen now?"
    sa "Just wait... I think this is some sort of portal, we'll be teleported any time soon."
    mc "..."
    mc "......"
    mc "........."
    mc "{i}Yawn"
    sa "I-It must be charging up mana... or something"
    mc "Oh... you don't say?"
    sa "Relax, give it a minute!"
    mc "Fine."
    mc "{i}Yawn"
    sa "And can you stop with your damn yawning?!"
    menu:
        "{i}Yawn":
            mc "{i}Yawn"
            sa "Alright, that's it!"
            sa "Damn this isn't working. Let's get out, come back in and see what happens."
            mc "Finally."
            jump elfvillageintro
        "Sorry":
            mc "Ok, ok, sorry. I was bored, that's all."
            sa "I'm bored too, you know!"
            menu:
                "Ask about Eve's sister":
                    mc "So... Eve's sister... Have you've seen her?"
                    sa "Huh... who?"
                    mc "Eve's sister."
                    sa "Ohhh... someone's interested, I see."
                    mc "Yeah, I am... But not in the way you're thinking."
                    sa "Hehehe, yeah, yeah, I get ya."
                    sa "But sorry, little man, I haven't seen her either."
                    mc "Oh."
                    sa "But I bet she's as hot as Eve... eh?"
                    mc "She is her sister, after all."
                    sa "Wait, you admitted Eve's hot? Hahahaha!"
                    mc "{i}Why is he acting like a 9-year-old?"
                    mc "I mean, y-yeah, she is hot... I-I mean pr-pretty."
                    sa "Oh, come on! Haha... admit it... don't hide it, little one. Not from your Master Sander."
                    mc "Alright fine, Eve is hot. Happy?"
                    sa "Hahaha. See, we're making progress, my pupil. You've begun to accept your feelings."
                    mc "Yeah, yeah, whatever, sensei."
                    sa "Hehe. Ok, this doesn't seem to be working."
                    sa "Why don't we get out and come back in and see what happens?"
                    mc "Yeah, that sounds good."
                    jump elfvillageintro
label elfvillageintro:
    "The both of you climb out of the tree."
    scene elfvillage with flash
    play music home
    mc "Wait, what happened?"
    sa "I guess we already teleported. Huh, how about that?"
    scene elfvillageblr with vpunch
    show talkangryn
    show serioussop
    show suprised
    pause 0.5
    show worriedmc
    hide suprised
    "Elf Girl" "Ohama nawathinawa!"
    mc "{i}Shit!"
    "{color=#8DE549}Elf girl" "Ayuda bima danawa!"
    mc "What the hell is she saying?"
    sa "I don't fucking know! Must be Astyllian or some shit!"
    "{color=#8DE549}Elf Girl" "......"
    "{color=#8DE549}Elf Girl" "Ugh, stupid humans! I said drop your weapons, assholes!"
    sa "Ahhh..."
    "{color=#8DE549}Elf Girl" "Do it!"
    sa "Ok, ok, calm down."
    "The two of you drop your weapons to the floor."
    "{color=#8DE549}Elf Girl" "How did you humans even find this place?"
    sa "W-We just went into that tree. And when we came out, we were here."
    "{color=#8DE549}Elf Girl" "And why did you guys randomly get into a tree?"
    sa "Ehm..."
    sa "For privacy!"
    "{color=#8DE549}Elf Girl" "What?!"
    mc "What?! No...  we were just following our friend, we wanted to know if she was fine."
    "{color=#8DE549}Elf Girl" "Stalkers, eh...?"
    "{color=#8DE549}Elf Girl" "Ok, time for inspection. Take of your clothes, a-all of them."
    mc "We're not stalkers we- WHAT?!"
    "{color=#8DE549}Elf Girl" "It's... standard procedure."
    sa "If that's what the lady wants."
    sa "{size=-5}This isn't going to end well."
    mc "{size=-5}Really? I figured you'd enjoy the stripping down part, sensei."
    sa "{size=-5}Ha-ha, funny. Listen, here's the plan."
    sa "{size=-5}On my signal, pounce on her. I'll take care of the rest."
    mc "{i}Sigh...{/i} {size=-5}Ok."
    "{color=#8DE549}Elf Girl" "Come on maggots, what's taking you so long? Do you need mommy to take off your clothes?"
    sa "{size=-5}NOW!"
    scene elfvillageblr with hpunch
    "You pounce on the elf girl and grab her tight."
    "{color=#8DE549}Elf Girl" "Mona huthakkda! Get off me, you...!"
    mc "I did it, Sander!"
    mc "......"
    scene sanderrun with vpunch
    play sound runfunny
    mc "SANDER!"
    sa "Your sacrifice will not be forgotten, little man! I will avenge yooouuuu!!!"
    mc "SANDER, YOU MOTHERFU-!!!"
    play sound punch
    stop music
    scene black with vpunch
    "You feel a hit on the back of your head, and everything goes black."
    scene black
    pause
    scene elfjail with fade
    pause 0.3
    scene black with fade
    pause 0.5
    scene elfjail with fade
    pause 0.3
    show thinkmc
    mc "{i}Ugh, where am I? What happened...?"
    show talkangryn with easeinleft
    "{color=#8DE549}Elf Girl" "Finally, you're up"
    mc "{i}Oh yeah, now I remember."
    "{color=#8DE549}Elf Girl" "Well, how about we start with your name?"
    mc "Huh...?"
    "{color=#8DE549}Elf Girl" "I-I'm interrogating you, idiot!"
    mc "Ah... I'm [mc]."
    n "Ok [mc], My name is Nessa. I'm the commander of the village guard, and I'm very curious as to how you managed to find us."
    mc "I told you, we were following our friend."
    n "Hah! Okay, stalker, following a fr-"
    n "Wait, was it Evelyn?"
    mc "Uhh... Will she get into trouble if I say yes?"
    n "Ugh, she's in enough trouble already!"
    mc "What do you mean? What's going on?!"
    n "It's none of your concern what goes on in our village."
    mc "Yeah, well she's my friend. So her well-being does concern me!"
    n "Ugh... This is why we told Evelyn not to get involved with the outside world."
    mc "Tell me what's going on. Is she in big trouble or something?"
    show talkwann
    hide talkangryn
    n "What? Nooooooo, it's nothing life-threatening..."
    n "Oh wait, is it not a bit life-threatening? ...Hmmm, it is life-threatening when you think about it."
    mc "Tell me what's going on!"
    n "Sigh... She's competing for the village chief. That's all you need to know."
    mc "What?!"
    n "Hey, I told you that's all you need to know."
    n "......"
    n "Wait... did I just sell our village information to a prisoner?"
    hide talkwann
    show sedtalkn
    n "Oh no... his seductive powers, they are far greater than I imagined!"
    mc "{i}What's up with her suddenly?"
    mc "What the hell are you talking about?"
    n "We haven't come against you men in centuries! We never thought you would be this powerful!"
    mc "Huh? I didn't even do anything."
    n "It's your seducing powers!"
    mc "Right... Well, like I said, I didn't do anything."
    n "You wouldn't know! Your power is too much for you to even notice it!"
    mc "{i}This girl is crazy!"
    show talkwanmc
    mc "What the hell is wrong with you?"
    n "Huh?"
    show talkhn
    n "Oh, you must be wondering why the sudden change in character. That earlier was me being the commander of the guard. We have to keep up appearances, you know what I mean?"
    mc "Hmm, yeah, you were kinda... intimidating, on account of how ridiculous you were acting."
    n "Heheh. Sorry if I scared you or anything. If you're a friend of Eve, I guess you're a good guy."
    mc "Thanks, I guess."
    "Quietness falls in the room."
    mc "So, you've never seen a human male before?"
    hide talkhn
    n "We haven't seen a male in over 150 years."
    mc "Ahh..."
    show suprised
    mc "What?!"
    n "Heheheh... yeah."
    mc "...S-So the whole village is..."
    n "Only elf women."
    show surprisedblushmc with dissolve
    mc "......"
    mc "{i}I've finally found Heaven, aside from being a prisoner!"
    mc "Ahem, s-so when was the last time you saw a male?"
    n "Hmm... about 200 years ago."
    mc "{i}Holy shit!"
    n "But I have to say, I'm a little disappointed."
    mc "What do you mean?"
    n "The male sexual organ is smaller than I expected. I'm not sure if I'll be able to feel pleasure as described in old text."
    show talkwanmc
    hide surprisedblushmc
    hide suprised
    hide thinkmc
    mc "How do you kn- Wait, did you!?"
    n "What? I had to do an inspection, right? Hehehehe."
    menu:
        "There's something called privacy?!":
            mc "Don't you know there's something called privacy?!"
            show talkangryn
            n "Ok, ok. Sheesh, my bad. You don't have to be a bitch about it."
            mc "......"
            n "Oh, someone's coming!"

        "Well, it can get bigger.":
            show talkwamc
            mc "Well, it can get bigger."
            n "It can! How?! ...Tell me, tell me now!"
            mc "I just have to get aroused... then it gets bigger."
            n "Ehhhhh? Really?"
            mc "Yeah."
            n "Wow, that's really cool! So you guys can get your sexual organ ready when it's time for intercouse?"
            mc "{i}Why is she talking about it like she's reading out of a book?"
            mc "...It's called a dick. And yeah."
            n "Wow... DICK..."
            n "DICK... DICK... DICK..."
            mc "SHHHHH, shut up! What if someone hears you?!"
            n "Naaaaa! No one will come down here... I still didn't report you in."
            mc "What?!"
            n "No one knows we're down here, so we've got plenty of time."
            mc "Time for what?"
            n "To make your DICK big!"
            show surprisedblushmc
            mc "{i}gulp{/i} Uh-oh."
            n "So if I take this hood off, will it make your dick big!"
            hide surprisedblushmc
            mc "Urh, no, I'm not as sexually frustrated as you guys."
            mc "{i}Am I?"
            n "Well..."
            scene nessahot1 with vpunch
            n "What if I did this?"
            window hide
            pause
            mc "{i}Shit!"
            scene nessahot2 with dissolve
            pause
            n "It got bigger!..."
            "You hear footsteps."
            n "Fuck! Someone's coming!"
            scene elfjail
            "Nessa quickly puts her hood on."
            $ persistent.nessaPantyless = True

    show normaln
    show worriedmc
    show sadtalke with easeinleft
    e "[mc]! Are you alright?"
    mc "Yeah, I'm fine, Eve."
    mc "{i}Damn it, Eve! Things were getting good!"
    e "Why didn't you report him in, Nessa?"
    n "Oh, I was... interrogating him."
    e "...?"
    e "......Whatever! Let's go, little one."
    "The two of you head out of the prison."
    play music home
    scene elfvillageblr with fade
    show talkwanmc
    show normale
    mc "How did you know I was there, Eve?"
    e "Sander. He somehow managed to sneak into the village. He found me and told me you got captured."
    e "It's a miracle he managed to sneak past the elf guards and get into the village. Seriously... he might even be able to sneak through the dark lands and get to the Demon King's castle with that sort of skill."
    mc "{i}Huh... so that was Sander's plan. He didn't run away after all. Still, he did leave me to fend for myself."
    show talkwamc
    mc "Well, he's the Master Voyeur, after all."
    show talkwae
    e "Yeah, he is..."
    e "...Uhm, [mc]? What's a voyeur?"
    show talksadhappymc
    mc "What? ...Hehe, I'll explain it to you later."
    e "Oh, ok."
    mc "So, where are we going now?"
    e "Let's go to my house. Sander's waiting there, he's been worried sick."
    mc "Oh, has he now?"
    scene elfvillage
    "You head to Eve's house. The whole village is surrounded by big trees. All the houses and shops are built into the trees."
    "{i}I'm not an architectural buff, but even I can see the ingenuity in these structures. Seeing buildings constructed around the trees is nothing short of awe-inspiring."
    "{i}I feel like a child going to a festival for the first time."
    mc "What are these trees?"
    e "These are Mara trees."
    mc "\"Mara\" ...That's Astyllian, right?"
    e "Yeah... It means \"great.\""
    mc "Great trees... Ohhh... I've never seen them."
    e "They're really rare. These are elven trees. Most of them were cut down by the Demon King's army."
    mc "Seriously, why?"
    e "Because he hated all things elf."
    mc "Really? Why did he hate the elves so much?"
    e "I don't know, little one. I'm not that much of a historian myself. But you should ask my sister. She knows all about these things."
    mc "Ah, about that, why didn't you tell me you have a sister?"
    e "Oh, sorry. You never asked, little one."
    mc "Sigh... I guess you're right, but it's still..."
    e "Don't worry, little one. You'll get to meet her soon."
    "You finally arrive at Eve's house. It doesn't really seem any different to the other houses."
    mc "{i}These houses all look the same. I wonder if they get mixed up sometimes?"
    show evehouse with fade
    show talkwaecs
    show smilemc
    stop music
    sa "Oh, [mc]! You're alive!"
    "Sander runs and grabs you."
    sa "Did they torture you?! I'm sorry I wasn't there sooner!"
    mc "I'm fine now Sander, seriously."
    sa "Thank Astylla!"
    mc "So, that was your plan?"
    show talkwas
    sa "Yeah, I escape and came back to save you. It worked perfectly if you ask me."
    mc "Yeah, it did. But what if the elf girl pulled out a knife and stabbed me when I pounced on her? A heads-up would've been nice!"
    sa "Uhh... Well, I didn't think about that! Hahaha!"
    show talkwae with easeinright
    show talksr
    hide talkwas
    hide talkwaecs
    e "When were you good at making plans, Sander?"
    sa "Well, it worked! That's what matters!"
    play sound doorknock
    "{i}Knock knock"
    e "Oh, that might be Milly!"
    mc "Who?"
    e "My sister."
    mc "Oh."
    hide talkwae with easeoutright
    "Eve heads to the door."
    sa "Oh, here she comes, little man. What type do you think she'll be? Thick ass or big boobs? "
    mc "Uhm..."
    menu:
        "Thick ass.":
            show talkwamc
            mc "Thick ass."
            sa "Right on."
            sa "Please let her have a thick Eve ass!"
        "Big boobs.":
            show talkwamc
            mc "Big boobs."
            sa "Nahh, I bet 1000 silver she's gonna have a thick Eve ass."
            mc "I guess we'll see."
    "Eve opens the door."
    scene evemilly with vpunch
    mi "Eve! You're finally back!"
    scene evemilly2 with dissolve
    pause
    "{color=#FFD747}Sander and {color=#96C7FF}[mc]" "......"
    mc "That's..."
    sa "Eve's sister."
    $ persistent.millyEve = True
    pause
    window hide
    mc "S-She's a loli."
    sa "We have sinned, little man."
    sa "{size=-5}Small boobs and no ass."
    e "It's nice to see you too, Milly! Heheh."
    e "I'm sorry I couldn't visit the last few days. We were on a quest."
    mi "I was waiting for you, but it's ok! Please tell me about your adventure. What did you see? Did you fight monsters? ...Tell meeeeee!"
    e "Hahaha, I'll get to it soon."
    mi "Who are these gu- wait..."
    scene evehouse
    show normalsop
    show smilemc
    show smilee
    show talkhmi
    mi "It's Sander and [mc], right?"
    e "Yeah."
    mi "Ammata udu... I've heard about you guys. The creepy man must be Sander-"
    show talkangrysop
    sa "What... who told you I was creepy?!"
    mi "You've been with my sister for a long time, right? I've heard a lot of stories about your adventures."
    show talkwaecsop
    sa "You might have heard how skilled I am as a warrior and the many beasts I've sla-"
    hide talkwaecsop
    mi "She said you always get caught peeping on her."
    sa "What?! Lies!"
    e "Hahahaha!"
    show normalsop
    hide talkangrysop
    mi "And the small human must be [mc]. Eve's been talking a lot about you recently. Always rambling on and on about how cute you wer-"
    show blushtalke
    e "Oh-Wait, is that the temple bell?"
    mi "What?"
    e "It is... Milly you better hurry on now hehehe... Priestess Zenelith might be waiting for you."
    mi "Was that really the bell? Oh no, I better get going! Bye guys, it was nice meeting you!"
    hide talkhmi with easeoutleft
    e "Hehehe. That's Milly, doesn't like to close her mouth once she opens it."
    mc "She seems nice. What does she do at the temple?"
    e "She's a priestess."
    mc "A priestess?"
    e "Yes."
    show talkwae
    hide blushtalke
    e "Sander, hands of my sister, ok?!"
    show talkangrysop
    sa "M-Me, why n-not him?"
    e "Don't drag him into this. I know [mc] still doesn't understand those sort of things yet."
    mc "{i}Wow... how old does she think I am?"
    sa "Whatever, I'm not a damn pedophile."
    e "A what?"
    sa "It means I'm not into small girls, so your sister's safe. Happy?!"
    mc "How old is she anyway? ...If you don't mind my asking."
    e "She's 179, she'll be turning 180 soon."
    mc "{i}Oh."
    mc "{i}How the hell does aging work for elves?!"
    sa "{i}cough{/i} {size=-5}Elves..."
    play sound doorknock
    "{i}knock knock"
    sa "Who the hell is it this time?"
    sa "Another sister?"
    show angrytalke
    hide blushtalke
    e "Shut up, I don't have another sister."
    a "Evelyn, open up. It's me, Aerin."
    e "Ugh..."
    hide smilee
    hide talkwae
    hide angrytalke with easeoutright
    sa "I bet it's gonna be a baby this time."
    show normala with easeinright
    show normale with easeinright
    show talkwasop
    hide talkangrysop
    sa "{i}whistle{/i} {size=-5}She's not a baby, but you can call her a babe. You know what I mean? Hehehe."
    show talkmc
    mc "{size=-5}Shut up, Sander!"
    show talkwaa
    a "So it's true, you did bring humans. The elder priestess isn't going to be happy. You'll be disqualified for sure."
    show angrytalke
    e "To what do I owe the pleasure of your presence?"
    a "We've been summoned by priestess Zenelith, I suggest you don't keep her waiting."
    hide talkwaa
    hide normala with easeoutright
    sa "Eve, seriously, what's going on here? You have to tell us."
    show watalkeve
    e "It's a long story."
    sa "We don't care."
    mc "Yeah. Just tell us, Eve."
    e "Fine. From where do I start...? Alright, in this village there are four families, you see. Each family has their own role and duty in the village."
    e "The Tara family is in charge of protection, the Shogo family is in charge of gathering resources and keeping the village fed. And the other two clans Lorel and Meril... The latter is mine. For the last two generations, my clan has been in charge of leading the village."
    e "But though there are two families, there can only be one elder. So each time when an elder is needed, both families will present their candidate. And the one who wins in a duel will be made the elder."
    sa "Duel as in...."
    e "We fight."
    sa "Huh... that doesn't sound very elvish."
    e "All elves are equally matched in knowledge and almost every other skill. But what is not the same is their fighting ability."
    sa "Ok... that makes sense."
    mc "So, you're one candidate, right?"
    e "I am."
    mc "Then who's the other one?"
    e "Its Aerin."
    mc "Oh..."
    sa "So you just have to beat her, right? You've got this Eve, you're one of the best fighters I know."
    e "Thanks Sander, but the same can be said for Aerin. She's been training for this day since she was little."
    mc "Who was the previous elder?"
    e "It was my mother."
    mc "So did she pass away?"
    e "Yeah... It's been a while though. It was like 60, 70 years back."
    mc "...These elf years are really confusing my brain."
    e "Don't worry, little one. You'll get used to it."
    sa "So the village didn't have an elder for 60 years?"
    e "It may sound long to you, but yeah. I didn't want to compete."
    sa "Why?"
    e "Because I would lose both ways."
    mc "What do you mean?"
    e "See, if I won, I would have to leave the outside world and stay here forever. And if I lose-"
    sa "You'll be dead."
    e "Noooooo! We don't fight to the death. We're aren't that barbaric."
    mc "So what happens when you lose?"
    e "You're banished from the village."
    mc "What?"
    e "Those are the ancient traditions."
    mc "So if you lose, you won't be able to see your sister?"
    e "Correct."
    sa "It's really is a lose-lose situation, ain't it?"
    e "Yes."
    mc "So, this Aerin, have you known her for a while?"
    e "Well she is... was my friend."
    mc "Was?"
    e "After her mother got banished, she... changed. Maybe she thought it was all our fault."
    mc "Oh, I understand."
    mc "So, is she living alone?"
    e "Yes, she had a brother, but he disappeared."
    mc "Disappeared?"
    e "It happened when we were little. Most of them say he just left."
    mc "I thought there were no males here."
    sa "What, no males?!"
    e "Wait, who told you that?"
    mc "Ne- I mean the elf guard."
    sa "Yeah... I didn't see any guys, now that you mention it."
    e "[mc] is right. There are only elf women in our village."
    mc "How is that possible?"
    e "I'll explain later, little one. Now's not the time for a history lesson. I better head to the temple."
    sa "Ok, let's go."
    e "Huh?"
    sa "We're coming too."
    mc "Yeah."
    e "...Fine, they'll ask about you anyway. Let's go."
    sa "Lead the way, Madame."
    scene elfvillage with fade
    "All three of you come out of Eve's house and head to the temple."
    "{i}The temple is a big hollow tree without leaves or any branches. When I say big, it seems like an under-statement. I don't think I've ever seen something as massive as this."
    "{i}This singular tree could be considered a forest in its own right. The man-hours or should I say elf-hours that would be needed to carve out something this size makes my head spin."
    "You head into the temple."
    scene elftemple
    e "Ok, we're here. Just... don't talk, ok Sander? I'll handle this?"
    sa "Yes, ma'am."
    zn "Athiyanthan awa, Evelyn."
    scene elfpriestshow with fade
    $ persistent.priestShow = True
    pause 0.5
    mc "{i}Wow... hot priestess."
    sa "Checking the body on her, huh?"
    scene elftemple
    show znpr r talk
    show watalkeve
    show angrya
    e "Paraku wunata samawenna, Zenelith."
    sa "{size=-5}Great, are we not supposed to understand anything?"
    zn "It seems like you brought the \"waduro\" with you..."
    e "Yes, I did."
    "Eve and priestess Zenelith continue to speak in Astyllian."
    mc "{size=-5}What's a \"waduro\"?"
    sa "{size=-5}I don't know, probably \"humans\" or something."
    mc "{size=-5}Aren't you supposed to be a Gold level adventurer?"
    sa "{size=-5}Yeah, so what? I don't need Astyllian, magic is for losers."
    mc "{size=-5}Hmph. Ok, tough guy."
    zn "I cannot believe you brought these \"creatures\" into our sacred village."
    e "These are my friends, they're my responsibility."
    zn "I shall deal with this later. Now, let's get back to the reason you are here."
    zn "Evelyn of Meril, you have no choice but to accept the duel. After your mother's passing, when you pleaded to me to give you more time to think, out of the generosity of my heart, I gave you 50 years of time."
    zn "It's been more than 60 years now, you've had enough time. If you do not participate now, you will be banished from this village forever. Do you understand?"
    e "Yes."
    zn "So, will you accept the duel?"
    e "..."
    e "I accept."
    e "On one condition."
    zn "What?"
    e "You'll let my friends stay in the village."
    zn "You must be joking. How are we supposed to share the same land we live in with these foul beasts?"
    sa "Hey! Who are you calling beasts, lady?!"
    zn "Silence, \"wadura\"! You humans were mere beasts when we arrived, playing with sticks and stones! Now look at you, after leeching off everything from our kind, you think you can talk back to me?"
    sa "I don't know what the fuck you're saying, bitch! But I swear I'll teach yo-"
    show sadtalke
    e "Sander, shut up!"
    zn "You still think I can let these beasts stay here?"
    e "Please, that's all I'm asking."
    zn "......"
    zn "...I'll let the small one stay, at least he has some discipline. But the other one has to leave."
    e "No, that wasn't the deal."
    zn "Either only the little one stays or the both of them leave."
    e "No there has to be a-"
    sa "Eve! It's ok, I'll leave."
    e "What?"
    sa "It's fine, I don't want to share the same place as this arrogant loudmouth cow either."
    scene elftemple
    show worriedmc
    show talks
    sa "Little man, I leave the rest to you then. Take care of her."
    mc "Sander... I won't let you down!"
    show talkwasop
    hide talks
    show sadtalke with easeinleft
    e "I'm sorry, Sander."
    sa "Ah, don't worry. It's not like we're not gonna see each other again, you become the elf elder and kick this bitch out of the village."
    e "I'll find a way to get you here Sander, somehow."
    sa "Ok then, see you guys. Good luck, Eve. I know you got this."
    e "Thanks, Sander. See you soon."
    mc "Bye, Sander."
    sa "Hey cow, I'm leaving! {i}mwah{/i} See you around! Haha!"
    zn "Ugh! Guards, escort this \"wadura\" out of the village!"
    hide talkwasop with easeoutright
    "Two guards take Sander out of the village."
    mc "{i}I hope he'll be fine. Eve looks really sad."
    mc "Hey Eve, what does \"wadura\" mean?"
    e "Oh... uhh, it means..."
    e "Ape."
    mc "...Huh. Good to know."
    scene elftemple
    show znpr r talk
    show angrya
    zn "Back to us. Evelyn, do you accept the duel?"
    show watalkeve
    e "I do."
    zn "And you, Aerin of Loren, do you accept the duel? "
    show talkangrya
    a "In the name of my family, I accept the duel."
    zn "It's settled then. The duel will be held after a moon cycle is over. Use this time to ready yourselves. May the Four Mothers bless you."
    scene elfvillage with fade
    "All of you head out of the temple."
    show talkna
    show normale
    show normalmc
    a "I-I wish you good luck Evelyn."
    e "Good luck to you, too."
    hide talkna with easeoutright
    mc "I bet you have some training to do."
    e "Yes, little one. I will be taking my leave. Feel free to explore the village. If you have any problems, speak to my sister. She'll be at the temple. I'll be able to get home in the evening after training."
    mc "Sounds good. Thank you for getting the priestess to let me stay."
    show talkwae
    e "You're welcome, little one. Oh, and [mc], don't get into any trouble."
    show talksadhappymc
    mc "Don't worry, I'll be at my best behavior."
    e "Ok. See you, little one."
    mc "See you soon, Eve."
    $ eveduel += 1
    $ evedueltimer = 8
    $ sawelfvillage = True
    scene elfvillageblr with fade
    show text "{color=#fff}Hints are disabled for this quest.{/color}"
    pause
    show text "{color=#fff}This quest line has multiple endings. The duel will be held after a full moon cycle, in 8 days. Make sure you explore the elf village at diffrent times of the day and speak to all the NPCs if you want to get the best possible ending.{/color}"
    pause
    jump elfvillage

################################################################################
################################################################################
#########################         QUEST STUFF         ##########################
################################################################################
################################################################################

label meetZenelith:
        hide screen hud
        "You see Zenelith go up to her house. You quickly run to see if you can catch her before she gets inside."
        show thinkmc
        mc "Damn it! I missed her."
        mc "Should I knock?"
        menu:
            "Knock":
                mc"I better knock."
                "{i}Knock Knock"
                mc "No one's answering."
                mc "This is weird."
                mc "I really need to talk to her."
                "You try to force the door open. It should be easy; the door seems weak, maybe even too weak. You reach to push from the handle and as soon as you touch it. But for some reason, the door just opens."
                mc "{i}It wasn't locked."

            "Sneak in":
                mc "{i}There's no way this bitch would listen to what I have to say."
                mc "{i}I should just sneak in and see what I can do. Maybe find some dirt on her or something."
                mc "{i}Time for some lock picking."
                mc "......"
                mc "{i}Uhhhh... I don't even know how to lock pick."
                mc "Well, when stealth fails, brute force is the way to go!"
                if sawmegan >= 3:
                    mc "Wait, why did that sound so familiar?"
                    "You try to force the door open. It should be easy, the door seems weak, maybe even too weak. You reach to push from the handle. But as soon as you touch it the door just opens."
                    mc "{i}It's not locked! Great! I'm still in stealth mode."
        "You slowly open the wooden door and carefully take a look inside."
        scene priesthouse with fade
        mc "{i}Why is it so dark in here? This place is creeping me out."
        "You slowly start heading inside"
        mc "{i}Where the hell is she?"
        zn "Wake up, toy!"
        scene doorpriest1
        mc "Shit! Where is she?!"
        play music creepymusic
        zn "Get up already! I've had a long day."
        mc "{i}I think it's coming from inside the floor."
        zn "Ugh, I've had enough of those stupid humans... How dare they?!"
        mc "{i}I think there's some kind of basement down there."
        zn "I'll deal with them soon, once this stupid duel is over!"
        mc "{i}I think this is the door that leads to the basement."
        zn "WAKE UP ALREADY! {i}WHIP"
        "Unknown voice" "...SEX? ...SEX? ...SEEEEEXX?"
        mc "{i}What the fuck is going on down there?"
        mc "{i}I should try to get in there."
        menu:
            "Try to open the door":
                "{i}Okay let's see, please don't be locked..."
                "You gently push  the door."
                scene doorpriest2 with flash
                "Suddenly, a bright light shines and forcefully throws your hands back."
                mc "{i}What the hell?! It almost blew my hands off!"
                mc "{i}Is that some kind of magical seal?"
                mc "{i}She went as far as to seal the door with magic. What the hell is she hiding down there?"
                zn "Fuck! I forgot to lock the front door! You better be ready when I'm back, slave!"
                "You hear footsteps coming up."
                mc "{i}SHIT! I better get the fuck out of here."
                "You quickly run out of the house, making as little noise as possible."
                scene elfvillagen with fade
                mc "{i}huff... huff... huff"
                mc "What the hell even was that? There was someone down there with her. There's something really weird going on with Zenelith. I need to learn more about this."
                mc "I need to find a way to get into her house while it's still daytime and see what's going on down there."
                mc "And that sealed door, how do I even get past that?!"
                mc "...All of this is crazy. Should I tell anyone about this whole thing? Would they even believe me if I did? I don't even have any proof."
                mc "I could tell Eve... but I don't want anything bad to happen to her!"
                mc "Ughh... calm down [mc], think straight!"
                mc "I'll have to do this on my own. I'll tell someone once I have enough proof."
                mc "So think, what do I need to do?"
                mc "I need to find a way to get into the Zenelith's house when she's not home."
                mc "And I need to find a way to break that seal. Hmmm... I think I could get help from Scarlet, she definitely knows something about seals!"
                if faila == 1:
                    mc "Shit! I can't go to the Academy now, I'm expelled. Damn it!"
                mc "There are only [evedueltimer] days before the duel. I've got to do all this before that happens."
                mc "...Let's see if I can do this!"
                $ bothpath += 1
                $ metpriest += 1
                jump elfvillage





#######################################################
#######################################################
#######################################################
##                   ENDINGS
#######################################################
#######################################################
#######################################################





label elfduel:
    scene homeday with fade
    $ eveduel -= 1
    $ evedueltimer += 1
    $ dueldone += 1
    stop music
    mc "Today's the duel. I better head to the elf village"
    "You get ready and go to the elfvillage"
    scene elfvillage with fade
    show normalmc with easeinright
    mc "{i}I wonder where the duel is happening?"
    mc "{i}Oh, there's Nessa. I should ask her."
    show talknn
    mc "Hey, Nessa!"
    n "Oh, hey there, [mc]. Here to see the duel?"
    mc "Yeah! Where is it happening?"
    n "In the temple grounds, it's right behind the temple."
    mc "Ok, thanks. Aren't you coming?"
    n "Naaah, I'll just wait here. I'll be there if something happens."
    mc "I understand."
    scene duelarena with fade
    "You go to the temple grounds. The duel hasn't started yet. The place doesn't look much like an arena, it's just a plain field. All the villagers are starting to gather around the two contestants."
    "Eve and Aerin both look serious. You've never seen Eve like this before."
    if rosa == 4:
        mc "{i}Ok, Eve's right there. I just need her to smell the flower"
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
        e "Thank you little one."
        mc "......"
        scene duelarena with vpunch
        "You hug Eve tight."
        mc "{i}Sorry, Eve."
        e "[mc]?"
        mc "You got this, Eve!"
        "You head back to the village people who have now all gathered and ready to witness the duel."
        "You see Aerin eyeing you suspiciously."
    "The both of them are now ready for battle. Zenelith stands in the center."
    zn "May the great four mothers bless the both of you. Let the duel begin!"
    if rosa == 4:
        scene elfduel with fade
        play music battlemusic1
        "You see Eve standing on her side of the arena, she looks like she can barely hold her balance, yet she still stands proud and ready."
        "The duel commences, the two girls go back and forth at each other, but swing after swing, Eve gets more and more tired. Aerin sees this and decides to take advantage of her opponent's weakness. She steps back."
        "And with one final swing of her sword, she manages to strike Eve directly, knocking her to the ground."
        stop music
        mc "{i}Aerin won!"
        mc "{i}I'm sorry, Eve..."
        "Eve and Aerin are taken to the temple."
        "You leave the elf village. You head to the Guild to tell Sander the news."
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
    scene elfduel with fade
    play music battlemusic1
    "Both Eve and Aerin are standing at their sides of the arena, waiting for the duel to start. The gong hits and both opponents start furiously running at each other, strike after strike."
    "Eve as expected has the upper hand, but Aerin does not fall much behind, she still has hope, hope that she can win. However, Eve is not going to let that happen. With one last menacing look at her opponent, she strikes."
    "The only thing you can hear is the thud of Aerin's unconscious body hitting the ground."
    scene black
    "Aerin is taken to the temple."
    stop music
    mc "{i}Eve won!"
    scene elfvillage
    show normale
    show worriedmc
    $ aerinlost += 1
    mc "Eve, congratulations! You were awesome!"
    e "Thank you, little one..."
    mc "{i}She doesn't look that happy."
    mc "So... Aerin... what's going to happen to her?"
    e "Sh-She... will have to leave."
    show sadtalke
    hide normale
    e "I'm sorry, [mc], but I've got to go. I'm very tired."
    hide sadtalke with easeoutright
    mc "Oh, yeah, sorry."
    mc "{i}She looks really sad. I think the fact that Aerin is getting banished still hurts her. They were friends after all."
    if aerinpath == 1 or bothpath < 3:
        mc "{i}I couldn't help her in the end."
        mc "I should go see her."
        scene aerinhouseblr
        "As you go into Aerin's house, you see her packing up her things. The house already feels empty."
        show sada
        show worriedmc
        mc "Aerin, I-I..."
        show shytalkha
        a "It's ok, [mc]. I'm ok."
        mc "I tried my best, Aerin. I tried to find a way to help you, but... I just needed more time."
        a "[mc], I never really understood why you were so kind to me, but thank you. You were a friend to me, one of very few I have."
        mc "Where are you going to go?"
        a "There's a whole world out there. There must be a place where I'll be accepted."
        mc "Come, live with me."
        a "Huh?"
        mc "You can stay in my house, I'm sure you'll like it there!"
        show shytalka
        a "I-I can't."
        mc "Please, it's ok."
        a "......"
        mc "Please, at least consider it."
        a "...Ok."
        a "You should go now, the village guards might come here for me."
        mc "Ok."
        mc "But remember... my house is always open for you."
        a "Thank you [mc], I'm really happy that I met you."
        scene elfvillage with fade
        mc "{i}Damn it! Why couldn't I save her?!"
        mc "{i}I hope she accepts my offer, she doesn't have to be alone!"
        scene black with fade
        "You go back to Randel. When you reach home, it's already dark."
        $ time = 4
        jump home
    if aerinpath == 1 or bothpath >= 3:
        mc "{i}I couldn't help her in the end!"
        mc "{i}But I have to tell her about her brother!"
        mc "{i}I have to go see her."
        scene aerinhouseblr
        "As you go into Aerin's house, you see her packing up her things. The house already feels empty."
        show sada
        show worriedmc
        mc "Aerin! There's something I want to tell you."
        a "[mc]?"
        mc "Your brother! He's alive. Zenelith has him locked up."
        a "WH-WHAT?!"
        "You hear the front door open."
        mc "YOU! How did you..."
        a "Priestess Zenelith! What have you done with my brother?"
        zn "So, you told her. I knew it was you, that day. I can sense it, that dirty scent you carry."
        mc "Y-You wont get away with this!"
        zn "We'll see about that."
        a "Is my brother al-"
        "In a split second, Aerin is sent flying across the room."
        mc "AERIN!"
        "Before you have time to react, blue orbs comes and hit you. The pain is excruciating as every orb tears through your flesh and bones. Everything goes black."
        scene black
        pause 0.5
        scene gameover with fade
        pause
        return
    mc "{i}It's sad that Aerin has to leave."
    "You go back to Randel. When you reach home, it's alreay dark."
    $ time = 4
    jump home


label ElfGoodEnding:
        hide screen hud
        show smilemc
        show normale
        show talkhe
        e "[mc], you're back."
        show talkhappymc
        mc "Hey Eve, what happened while I was gone?"
        e "A lot! Everyone's at the temple now."
        mc "I don't know what that means... What's happening at the temple?"
        e "Aerin's being made the elder, the ceremony is being held as we speak."
        mc "Really? So they decided to make Aerin the elder."
        e "I refused to become the elder, so they gave her the job."
        mc "That's great news! But I have a question. Last night, did you guys talk?"
        show talkwae
        e "We did, after Aerin stopped crying. She cried for almost another hour after she saw her brother... I had to listen to her weeping before I could talk to her."
        mc "Hehehehe, she must've been pretty shocked."
        e "She certainly was."
        mc "So what exactly did you guys talk about?"
        show sadhtalke
        e "We talked a lot, actually. She said she was sorry for the way she acted and that she has now changed. It was a pleasant surprise."
        mc "That's great! So the both of you are friends now?"
        e "I suppose we are."
        mc "Why aren't you at the ceremony?"
        e "Oh, I almost forgot. We should go to Aerin's house, Nessa must be waiting for us."
        show talkwamc
        mc "What's going on?"
        e "We're going to give Aerin a surprise party."
        mc "Really? That's awesome! Let's go then."
        scene aerinhouseblr with fade
        show smilemc
        show smileeop
        pause
        show normaln with easeinleft
        pause
        show talkwan
        n "Everything is a-go, Eve. We're ready to rock! Oh, hey [mc]."
        show talksadhappymc
        mc "Hey, you guys changed the place a lot."
        n "Oooh, so you've been here before. I can only wonder why."
        show talkwanmc
        mc "It's not even like that. I just came for a visit, that's all!"
        n "\"A visit\", right, I gotcha."
        n "Yeah, well anyways, we added some decorations here and there. Nothing too fancy."
        hide talkwanmc
        mc "You guys did a great job."
        n "Thanks, we sure do appreciate it. "
        show talkheop
        e "So Nessa, you invited everyone right?"
        n "Yup."
        mc "I'm really happy that the three of you are together now."
        n "Hahaha, me too. It's all thanks to you [mc], our hero!"
        e "I can't thank you enough, little one. You've helped us all."
        mc "I'm glad I was able to help, I just wanted everyone to be happy."
        n "It was a good thing you came to our village, [mc]. Now, since everything is ready, all that is left is to surprise Aerin, right?"
        e "Yeah. We'll give her a surprise she will not forget."
        "{color=#8DE549}Nessa and {color=#96C7FF}[mc]" "YEAH!"
        n "I'll go grab her then, the ceremony must be almost over."
        e "Understood."
        hide normaln
        hide talkwan with easeoutright
        scene aerinhouseblr
        show talkhappymc
        show smilee
        mc "Oh, Eve, how's Morgan doing?"
        e "He is doing well, all things considered. You should go meet him. He's been asking for you since he awoke."
        mc "I guess I should, huh? Where is he?"
        e "He's in that room at the corner."
        mc "Thanks, Eve."
        "You go to Morgan's room."
        scene aerinbrother with fade
        morg "Oh, you're back! [mc], right?"
        mc "Yeah. How are you doing?"
        morg "Never been better! I never thought I'll be able to sleep in a bed like this again. My body is still weak, the village doctor said I should at least rest for two years."
        mc "For 2 years?! That long?"
        morg "Long! I was chained to a wall and tortured for 160 years. What did you expect? Heh..."
        mc "I'm sorry, I didn't mean to bring that up. Are you ok with talking about it?"
        morg "Yeah, it's fine, I owe you that much at least."
        menu:
            "Ask him what happened":
                mc "Can you tell me what happened?"
                morg "My memory is... a bit lacking. I only remember bits and pieces. I remember going out hunting, and then suddenly Elder Zenelith came out of nowhere and used some sort of spell on me."
                morg "When I woke up, I was in her prison, chained."
                mc "What did Zenelith do to you?"
                morg "She... used me... for her pleasure."
                morg "She didn't seem to enjoy it much either, she was always so frustrated, as if there was something wrong with me... maybe with her. When she was especially angry she would whip me..."
                morg "While I was in there, I slowly started to lose track of time. After a certain point, I didn't even feel like I existed anymore..."
                morg "But that night, when I heard Aerin's name, I regained myself. It was like waking up of from a deep sleep."
                mc "That's... I'm really sorry."
                morg "You saved me from that never ending nightmare, [mc]. You gave me my sister back. I'm sorry that this weak elf will never be able to repay you."
                mc "It's all right, seeing the two of you together is more than enough for me."
            "Let him rest":
                mc "No, it's alright. You get some rest."
        morg "Th-Thank you, [mc]. I heard what happened to my sister, after I disappeared."
        mc "Yeah, she was... lonely."
        morg "Yes... but Aerin told me that you talked to her and helped her to become a better person."
        mc "I didn't do that much, she did it on her own."
        morg "No, it's because of you. I know that I have no right to ask more of you, but please continue helping my sister. I'm still weak, I won't be able to give the support she needs."
        mc "I'll help her."
        morg "Thank you."
        mc "You get some rest now. Don't think you're useless. You've been through a lot and endured for this long. You did it for her. You being here is all the support she needs."
        morg "Thank you, [mc]."
        jump aerinparty
