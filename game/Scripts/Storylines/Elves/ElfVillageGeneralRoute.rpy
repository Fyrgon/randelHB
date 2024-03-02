label elfqueststart:
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
    mc "What brings you here, Eve?"
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
    e "You don't need to worry about it, take care of yourself, little one."
    scene homedayblur
    show worriedmc
    mc "Wait, Eve!"
    mc "{i}What the hell, why is she leaving all of a sudden?"
    mc "{i}I have to see if Sanders knows about this."
    play sound doorknock
    "{i}Knock knock."
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
    sa "Come on, kid. We're going to follow her."
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
    sa "I don't know, she said she had urgent business in her Village."
    mc "Something urgent? It has to be pretty serious if it would make her leave Randel forever. I wonder why she didn't tell us?"
    sa "I'm not completely making sense of this either, man."
    sa "Eve normally visits her Village almost every day, but this seems different."
    mc "Why does she visit her Village every day? I thought she hated that place."
    sa "As far as I'm aware, she does. But she has family; a sister there."
    mc "WHAT?!"
    sa "Yeah. if I were to guess, I'd say it has to do something with her."
    mc "{i}Eve has a sister? Who would've thought?"
    sa "Alright, enough talking, we should stay quiet."
    mc "Right."
    "You keep following Eve, the path she takes is one you've never seen."
    mc "We're still in the Outer Forest, right?"
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
    sa "{size=-5}Hehe, nice. Well, little man, I think we just discovered the passage to the Elf Village."
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
    sa "I-It must be charging up mana... or something."
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
        "Sorry":
            mc "Ok, ok, sorry. I was bored, that's all."
            sa "I'm bored too, you know!"
            mc "..."
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
            mc "I mean, y-yeah, she is hot... I-I mean p-pretty."
            sa "Oh, come on! Haha... admit it... don't hide it, little one. Not from your Master Sander."
            mc "Alright fine, Eve is hot. Happy?"
            sa "Hahaha. See? We're making progress, my pupil. You've begun to accept your feelings."
            mc "Yeah, yeah, whatever, sensei."
            sa "Hehe. Ok, this doesn't seem to be working."
            sa "Why don't we get out and come back in and see what happens?"
            mc "Yeah, that sounds good."
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
    mc "We're not stalkers, we- WHAT?!"
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
    "{color=#8DE549}Elf Girl" "Finally, you're up."
    mc "{i}Oh yeah, now I remember."
    "{color=#8DE549}Elf Girl" "Well, how about we start with your name?"
    mc "Huh...?"
    "{color=#8DE549}Elf Girl" "I-I'm interrogating you, idiot!"
    mc "Ah... I'm [mc]."
    n "Ok [mc], My name is Nessa. I'm the commander of the Village guard, and I'm very curious as to how you managed to find us."
    mc "I told you. We were following our friend."
    n "Hah! Okay, stalker, following a fr-"
    n "Wait, was it Evelyn?"
    mc "Uhh... Will she get into trouble if I say yes?"
    n "Ugh, she's in enough trouble already!"
    mc "What do you mean? What's going on?!"
    n "It's none of your concern what goes on in our Village."
    mc "Yeah, well she's my friend. So her well-being does concern me!"
    n "Ugh... This is why we told Evelyn not to get involved with the outside world."
    mc "Tell me what's going on. Is she in big trouble or something?"
    show talkwann
    hide talkangryn
    n "What? Nooooooo, it's nothing life-threatening..."
    n "Oh wait, is it not a bit life-threatening? ...Hmmm, it is life-threatening when you think about it."
    mc "Tell me what's going on!"
    n "Sigh... She's competing for the role of Village Elder. That's all you need to know."
    mc "What?!"
    n "Hey, I told you that's all you need to know."
    n "......"
    n "Wait... did I just sell our Village information to a prisoner?"
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
    mc "...S-So the whole Village is..."
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
        "Ever heard of privacy?!":
            mc "Don't you know there's something called privacy?!"
            show talkangryn
            n "Ok, ok. Sheesh, my bad. You don't have to be a bitch about it."
            mc "......"
            n "Oh, someone's coming!"
        "It can get bigger":
            show talkwamc
            mc "Well, it can get bigger."
            n "It can! How?! ...Tell me, tell me now!"
            mc "I just have to get aroused... then it gets bigger."
            n "Ehhhhh? Really?"
            mc "Yeah."
            n "Wow, that's really cool! So you guys can get your sexual organ ready when it's time for intercourse?"
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
            n "It got bigger...!"
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
    e "Huh...?"
    e "...Whatever! Let's go, little one."
    "The two of you head out of the prison."
    play music home
    scene elfvillageblr with fade
    show talkwanmc
    show normale
    mc "How did you know I was there, Eve?"
    e "Sander. He somehow managed to sneak into the Village. He found me and told me you got captured."
    e "It's a miracle he managed to sneak past the elf guards and get into the Village. Seriously... he might even be able to sneak through the dark lands and get to the Demon King's castle with that sort of skill."
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
    "You head to Eve's house. The whole Village is surrounded by big trees. All the houses and shops are built into the trees."
    "{i}I'm not an architectural buff, but even I can see the ingenuity in these structures. Seeing buildings constructed around the trees is nothing short of awe-inspiring."
    "{i}I feel like a child going to a festival for the first time."
    mc "What are these trees?"
    e "These are Mara trees."
    mc "\"Mara\" ...That's Astyllian, right?"
    e "Yeah... It means \"great.\""
    mc "Great trees... Ohhh... I've never seen them."
    e "They're really rare. These are elven trees. Most of them were cut down by the Demon King's army."
    mc "Seriously, why?"
    e "Because he hated anything that had to do with elves."
    mc "Really? Why did he hate the elves so much?"
    e "I don't know, little one. I'm not that much of a historian myself. But you should ask my sister. She knows all about these things."
    mc "Ah, about that... Why didn't you tell me you have a sister?"
    e "Oh, sorry. You never asked, little one."
    mc "{i}Sigh...{/i} I guess you're right, but it's still..."
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
    sa "Yeah, I escaped and came back to save you. It worked perfectly if you ask me."
    mc "Yeah, it did. But what if the elf girl pulled out a knife and stabbed me when I pounced on her? A heads-up would've been nice!"
    sa "Uhh... Haha, I didn't think about that!"
    show talkwae with easeinright
    show talksr
    hide talkwas
    hide talkwaecs
    e "When were you good at making plans, Sander?"
    sa "Well, it worked! That's what matters!"
    play sound doorknock
    "{i}Knock knock."
    e "Oh, that might be Milly!"
    mc "Who?"
    e "My sister."
    mc "Oh."
    hide talkwae with easeoutright
    "Eve heads to the door."
    sa "Oh, here she comes, little man. What type do you think she'll be? Thick ass or big boobs? "
    mc "Uhm..."
    menu:
        "Thick ass":
            show talkwamc
            mc "Thick ass."
            sa "Right on."
            sa "Please let her have a thick Eve ass!"
        "Big boobs":
            show talkwamc
            mc "Big boobs."
            sa "Nahh, I bet 1000 gold she's gonna have a thick Eve ass."
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
    mc "S-She's a little girl."
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
    e "It is... Milly, you better hurry on now, heh... Priestess Zenelith might be waiting for you."
    mi "Was that really the bell? Oh no, I better get going! Bye, guys! It was nice meeting you!"
    hide talkhmi with easeoutleft
    e "Hehehe. That's Milly, doesn't like to close her mouth once she opens it."
    mc "She seems nice. What does she do at the temple?"
    e "She's a priestess."
    mc "A priestess?"
    e "Yes."
    show talkwae
    hide blushtalke
    e "Sander, hands off my sister, ok?!"
    show talkangrysop
    sa "M-Me, why n-not him?"
    e "Don't drag him into this. I know [mc] still doesn't understand those sorts of things yet."
    mc "{i}Wow... how old does she think I am?"
    sa "Whatever, I'm not a damn pedophile."
    e "A what?"
    sa "It means I'm not into small girls, so your sister's safe. Happy?!"
    mc "How old is she anyway? ...If you don't mind my asking."
    e "She's 179, she'll be turning 180 soon."
    mc "{i}Oh."
    mc "{i}How the hell does aging work for elves?!"
    sa "{i}Cough...{/i} {size=-5}Elves..."
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
    sa "{i}Whistle...{/i} {size=-5}She's not a baby, but you can call her a babe. You know what I mean? Hehehe."
    show talkmc
    mc "{size=-5}Shut up, Sander!"
    show talkwaa
    a "So it's true, you did bring humans. The Elder Priestess isn't going to be happy. You'll be disqualified for sure."
    show angrytalke
    e "To what do I owe the pleasure of your presence?"
    a "We've been summoned by Priestess Zenelith, I suggest you don't keep her waiting."
    hide talkwaa
    hide normala with easeoutright
    sa "Eve, seriously, what's going on here? You have to tell us."
    show watalkeve
    e "It's a long story."
    sa "We don't care."
    mc "Yeah. Just tell us, Eve."
    e "Fine. From where do I start...? Alright. In this Village there are four families, you see. Each family has their own role and duty in the Village."
    e "The Tara family is in charge of protection, the Shogo family is in charge of gathering resources and keeping the Village fed. And the other two clans Lorel and Meril... The latter is mine. For the last two generations, my clan has been in charge of leading the Village."
    e "But though there are two families, there can only be one Elder. So when a new Elder is needed, both families will present their candidate. And the one who wins in a duel will be made the Elder."
    sa "Duel as in...."
    e "We fight."
    sa "Huh... that doesn't sound very elfish."
    e "All elves are equally matched in knowledge and almost every other skill. But what is not the same is their fighting ability."
    sa "Ok... that makes sense."
    mc "So, you're one candidate, right?"
    e "I am."
    mc "Then who's the other one?"
    e "It's Aerin."
    mc "Oh..."
    sa "So you just have to beat her, right? You've got this Eve, you're one of the best fighters I know."
    e "Thanks Sander, but the same can be said for Aerin. She's been training for this day since she was little."
    mc "Who was the previous Elder?"
    e "It was my mother."
    mc "So did she pass away?"
    e "Yeah... It's been a while though. It was like 60, 70 years back."
    mc "...These elf years are really confusing my brain."
    e "Don't worry, little one. You'll get used to it."
    sa "So the Village hasn't had an Elder for 60 years?"
    e "To you it probably sounds like a much longer time, but yeah. I didn't want to compete."
    sa "Why?"
    e "Because I would lose both ways."
    mc "What do you mean?"
    e "See, if I won, I would have to leave the outside world and stay here forever. And if I lose—"
    sa "You'll be dead."
    e "No, no! We don't fight to the death. We're aren't that barbaric."
    mc "So, what happens when you lose?"
    e "You're banished from the Village."
    mc "What?"
    e "Those are the ancient traditions."
    mc "So, if you lose, you won't be able to see your sister?"
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
    mc "I thought there were no guys here."
    sa "What, no guys at all?!"
    e "Wait, who told you that?"
    mc "Ne- I mean... The elf guard."
    sa "...Yeah, now that you mention it, I haven't seen any male elves."
    e "[mc] is right. There are only elf women in our Village."
    mc "How is that possible?"
    e "I'll explain later, little one. Now's not the time for a history lesson. I better head to the temple."
    sa "Ok, let's go."
    e "Huh?"
    sa "We're coming too."
    mc "Yeah."
    e "...Fine, they'll ask about you anyway. Let's go."
    sa "Lead the way, ma'am."
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
    mc "{size=-5}Aren't you supposed to be a Gold-Rank adventurer?"
    sa "{size=-5}Yeah, so what? I don't need Astyllian, magic is for losers."
    mc "{size=-5}Hmph. Ok, tough guy."
    zn "I cannot believe you brought these \"creatures\" into our sacred Village."
    e "These are my friends, they're my responsibility."
    zn "I shall deal with this later. Now, let's get back to the reason you are here."
    zn "Evelyn of Meril, you have no choice but to accept the duel. After your mother's passing, when you pleaded me to give you more time to think, out of the generosity of my heart, I gave you 50 years of time."
    zn "It's been more than 60 years now. You've had enough time. If you do not participate now, you will be banished from this Village forever. Do you understand?"
    e "Yes."
    zn "So, will you accept the duel?"
    e "...I accept."
    e "...On one condition."
    zn "What?"
    e "You'll let my friends stay in the Village."
    zn "You must be joking. You us to share the same land we live in with these foul beasts?"
    sa "Hey! Who are you calling beasts, lady?!"
    zn "Silence, \"wadura\"! You humans were mere beasts when we arrived, playing with sticks and stones! Now look at you, after leeching off everything from our kind, you think you can talk back to me?"
    sa "I don't know what the fuck you're saying, bitch! But I swear I'll teach you-"
    show sadtalke
    e "Sander, shut up!"
    zn "You still think I can let these beasts stay here?"
    e "Please, that's all I'm asking."
    zn "......"
    zn "...I'll let the small one stay, at least he has some discipline. But the other one has to leave."
    e "No, that wasn't the deal."
    zn "Either only the little one stays or the both of them leave."
    e "No, there has to be a-"
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
    sa "Ah, don't worry. It's not like we're not gonna see each other again, you become the Village Elder and kick this bitch out of the Village."
    e "I'll find a way to get you here Sander, somehow."
    sa "Ok then, see you guys. Good luck, Eve. I know you got this."
    e "Thanks, Sander. See you soon."
    mc "Bye, Sander."
    sa "Hey cow, I'm leaving! {i}Mwah!{/i} See you around! Haha!"
    zn "Ugh! Guards, escort this \"wadura\" out of the Village!"
    hide talkwasop with easeoutright
    "Two guards take Sander out of the Village."
    mc "{i}I hope he'll be fine. Eve looks really sad."
    mc "Hey Eve, what does \"wadura\" mean?"
    e "Oh... uhh, it means...{p}...Ape."
    mc "...Huh. Good to know."
    scene elftemple
    show znpr r talk
    show angrya
    zn "Now, back to the matter at hand. Evelyn, do you accept the duel?"
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
    a "I-I wish you good luck, Evelyn."
    e "Good luck to you, too."
    hide talkna with easeoutright
    mc "I bet you have some training to do."
    e "Yes, little one. I will be taking my leave. Feel free to explore the Village. If you have any problems, speak to my sister. She'll be at the temple. I'll be able to get home in the evening after training."
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
    show black:
        alpha 0.5
    show text "{color=#fff}Hints are disabled for this quest.{/color}" with dissolve
    pause 4
    hide text with dissolve
    show text "{color=#fff}This quest line has multiple endings.\nThe duel will be held after a full moon cycle, in 8 days.\nMake sure you explore the Elf Village at diffrent times of the day and speak to all the characters to obtain the True Ending.{/color}" with dissolve
    pause 10
    hide text with dissolve
    jump elfVillage


     #############################
 ######################################
#####         DUEL ENDINGS         #####
 ######################################
     ##############################

label elfduel:
    scene homeday with fade
    $ eveduel -= 1
    $ evedueltimer += 1
    $ dueldone += 1
    stop music
    mc "Today's the duel. I better head to the Elf Village."
    "You get ready and go to the Elf Village."
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
        ### Aerin-Only Ending
        jump aerinWinsDuel
    else:
        # Not-Aerin endings
        jump eveWinsDuel
