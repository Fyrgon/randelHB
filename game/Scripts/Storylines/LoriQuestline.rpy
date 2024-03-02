default loriEventValue = 0
default loriEvent = True
default loriBest = False
default toldLoriWallcrawler = False
default toldLoriYokel = False
default toldLoriDelivery = False
default toldLoriLedric = False
default toldLoriMore = 0
default askedAboutLori = False
default loriInsisting = False
default loriLooksCuteLikeThat = False
default loriNotReally = False
default loriDateDate = 9999
default loriDone = False
default loriDropped = False

label loriTea:
    if loritea == 0:
        scene black with fade
        l "Oh, [mc]. Would you, uhm... like some tea to drink while you read?"
        mc "Yeah, sure! That would be great."
        l "I'll bring you a cup right away... You're ok with Kahata tea, right?"
        "Lori quickly walks away."
        mc "Yeah!"
        l "Ok, awesome!"
        "After a few moments, Lori brings you a cup of tea."
        mc "That was quick."
        l "Hahah, yeah. I made some tea a while ago... I made extra... {size=-3}just in case you came over today."
        mc "......"
        mc "...Thanks."
        l "You're welcome!"
    else:
        scene black with fade
        "Lori puts a cup next to you. You see some steam coming from it. It's kahata tea."
        l "Here's some tea for you, [mc]."
        mc "Thanks."
        l "You're welcome."
    $ loritea += 1
    return



label loriFunTimes:
    if loriDone == False:
        if loriFunValue == 1:
            "You notice her glasses are a bit dirty today."
            mc "...Lori, can you pass me your glasses?"
            l "H-Huh? Why?"
            "Even though you haven't replied yet, she hands them to you,"
            mc "Oh, I noticed they were a bit dirty."
            "As you clean them, you notice Lori blushing lightly."
            l "Thanks."
            "You hand them back to her and you return to the studying."
        elif loriFunValue == 2:
            "As the two of you are studying, you notice that every once in a while — when she thinks you're not looking — she plays with the frame of her glasses while blushing lightly each time."
            mc "{i}She's cute."
            "After some time, you're finally done with the studying, and you smile at her."
    if loriDone:
        if loriFunValue == 2:
            "Lori seems a bit nervous today. You're not sure what it is, but she seems more tense than other times."
            "When the two of you accidentally touch after you both reach for the pen at the same time, she flinches."
            mc "...Are you okay?"
            l "M-Me? Y-Yeah! How c-come you're asking?"
            "You grab her hand and she winces."
            mc "You can tell me."
            l "It's nothing, I'm just... A bit worried."
            mc "For what?"
            l "You won't leave me, will you?"
            mc "...What are you talking about?"
            l "I-I told you it's nothing! L-Let's just keep studying..."
            "You grab her other hand."
            mc "Lori. You know I would never."
            l "...But what if you died?"
            mc "I won't."
            l "..."
            l "Alright."
            "You let her hands go."
            mc "Now we can keep studying, you dummy."
            l "Heh."
        #elif loriFunValue == 4:
        #    "After half an hour of studying, Lori pokes you."
        #    mc "What is it?"
        #    "Lori smirks"
        #    l "Are you... busy tonight?"
        #    mc "Uhm, I'm... not?"
        #    mc "{i}Where is she going with this?"
        #    l "Well, y'know... My bed has got space for two."
        #    mc "{i}Oh, so that's where she's going."
        #    menu:
        #        "Accept her offer":
        #            mc "Sounds very interesting. I'll have to come and make sure that's true tonight, then."
        #            "Lori blushes lightly."
        #            l "I-I'll wait for you."
        #            $ loriNightSex = True
        #        "Turn her down":
        #            mc "Ah... I'm sorry I can't tonight. I need to get up early tomorrow."
        #            l "O-Oh, u-uhm, i-it's fine then! Don't worry..."
        #            "You can see all her confidence draining in an instant."
        #            mc "{i}I feel kind of bad, now..."
        #    mc "...Let's get back to studying now, though."
        #    l "Y-Yeah..."
        #    "The two of you get back to studying Astyllian. Once you're done, you stretch your arms behind your back."
        elif loriFunValue >= 7:
            "The two of you study. Or at least, Lori does her best to teach you more Astyllian as you tease her throughout."
    else:
        "She's a great teacher. When the studying is over you feel like you've learned a lot."
        if loriDropped:
            "It does feel weird to keep learning from the girl you indirectly turned down... But she hasn't really said anything about it, so why should you?"
    $ loriFunValue += 1
    return



label lori0:
    hide screen hud
    "The two of you start studying like usual. Astyllian is a very weird language, yet you somehow grasp most of it with ease."
    scene readtalk1 with Fade(0.5, 1.5, 1.0)
    l "I'm surprised, [mc], you're really talented."
    mc "Am I? It really isn't that hard..."
    l "Well, considering you told me you never studied Astyllian before, your pace is really impressive."
    mc "Now you're making me blush."
    l "I-I'm just being honest. If we keep going at this pace you'll know in a few weeks what some people take years to learn."
    mc "I guess I really am just that good."
    l "Heh, yeah."
    "Lori takes a step back from the table and then looks at you."
    l "Since you're so gifted, today's lesson is suspended."
    mc "H-Huh? Wait why-"
    l "Because..."
    "Lori looks down."
    l "...I th-thought we could talk a bit."
    mc "Huh... That's it? Sure, then. Was there anything you wanted to talk about?"
    l "Well, you said you've joined the Adventurers' Guild, haven't you? Tell me about some of your adventures!"
    if corbanDone == True and aquest2 >= 2 and (quest1 >= 5 or mineQuest == True):
        mc "Some of my adventuers? Sure, let's see..."
        label tellingLoriAboutYourAdventures:
        menu:
            "Tell her about the Wallcrawler Quest" if (quest1 >= 5 or mineQuest == True) and toldLoriWallcrawler == False:
                mc "Well, I could tell you about the one time I helped solving a wallcrawler infestation."
                l "Please do tell me about it!"
                mc "Okay, okay. Let's see..."
                mc "It was some time ago, it was one only quests I could take part in considering my rank so I decided to take it."
                mc "I didn't know what wallcrawlers were exactly... They're not the kind of monster you'd see in the forest."
                l "Oh yeah, wallcrawlers like closed spaces a lot more... There actually was infestation here once as well."
                mc "There was?"
                l "Yeah... Some merchant hadn't checked his cargo and had accidentally brough a few in town. They started going from house to house and the adventurers in town had to get together to exterminate them all."
                l "They're easy to kill, but they're kind of a nuisance."
                mc "Oh you're definitely right. If I hadn't looked up what they were and their weak point, I would have probably not been able to do much."
                mc "As I was saying, I looked them up in the Book of Monsters and then I followed the route to the cave they were infesting. Apparently it was a dwarf settlement, and they were the ones to call for help."
                l "Oh, you mean Rongan?"
                mc "Huh?"
                l "The cave, was it called Rongan?"
                mc "I'm... Uh... Don't remember."
                l "...Oh, I see."
                mc "Why?"
                l "Oh, nothing. I have some relatives from my mother side that live there. I'm not close with them or anything... They don't really come here at all."
                mc "Ah, I see. Is there a grumpy old dwarf with a scar on his face between your relatives?"
                l "Uhm, no... At least not that I remember."
                l "The last time I saw any of them it was when my mother got sick a few years ago... Pure Dwarves age a lot faster than I do, so maybe one of them now matches that description perfectly well."
                l "Anyone who I remember as being a little child now could be a grown dwarf. I'm sure little Agnia and Nadia aren't that little anymore..."
                if hadNadiaBlowYou == True:
                    mc "N-Nadia?"
                    l "You know her, [mc]?"
                    mc "Ahh, n-no it's nothing."
                    l "You sure? You're acting weird."
                    mc "Oh no no, it's nothing I swear."
                    mc "I-I'll get back to the story now."
                    l "...Alright. What were you saying about that old dwarf?"
                else:
                    mc "Let's not think about that now, shall we?"
                    l "Y-You're right... What were you saying about an old dwarf?"
                mc "Right, the grumpy old dwarf."
                mc "Well, that dwarf is who I found when I arrived at the cave. He told me where the wallcrawlers were, not before insulting how young and meek I look."
                l "Well, you're definitely short for human standards, and thin for dwarven standards... Can you really blame him?"
                mc "Just because you're correct doesn't mean you're right. I'm still an adventurer."
                l "True."
                mc "But that definitely made me want to prove him wrong, so I immediately went looking for the wallcrawlers."
                mc "That cave was really dark... Unluckily for wallcrawlers, their spikes glow, so it was easy to spot them."
                mc "They're definitely uglier than they're described in the Book of Monsters."
                l "I can imagine."
                mc "But, well, even though I had to withstand their ugliness, I killed every single one of them."
                mc "I think I was way more nervous than I had to be... I had trained hard enough to know it wasn't going to be a problem to get rid of them."
                mc "When I finished I came back and told them I was done they almost didn't believe me."
                l "What did they give you?"
                mc "Ah, the grumpy dwarf offered me a diamond."
                if hadNadiaBlowYou == True:
                    mc "{i}Let's not mention that I turned that down to get a blowie from her cousin, though..."
                l "Wow, but that's so much!"
                mc "I guess I impressed them."
                l "Heheh, well [mc], you can definitely be impressing."
                mc "I can?"
                l "Y-Yeah! Maybe you don't realize because it feels normal to you, but most people cannot learn Astyllian as quickly as you, nor can they be adventurers at the same time, while {b}also{/b} studying at the Academy."
                mc "...I guess you're right."
                l "And since you're a cool adventurer, tell me about other quests you've been on!"
                mc "Okay, okay..."
                $ toldLoriWallcrawler = True
                $ toldLoriMore += 1
                jump tellingLoriAboutYourAdventures
            "Tell her about Yokel" if aquest2 >= 2 and toldLoriYokel == False:
                mc "I'm not sure how fun this was but... Have you heard that Yokel burned down?"
                l "Oh, yeah I did... A tragedy, really."
                mc "Well, I was supposed to deliver some crystals there the same day."
                l "..."
                mc "When I got the crystals I thought it was going to be a relatively easy quest... Thank Astylla I had read about imps before embarking on it."
                mc "I walked all the way to Yokel and, once there... The town was already in flames."
                "Lori looks at you worriedly."
                if thealive == True:
                    mc "There were imps flying around... I honestly considered just running away but..."
                    mc "I saw a woman being attacked by some imps and I just couldn't do nothing."
                    "Lori's eyes light up."
                    l "You saved her?"
                    mc "Yeah. I ran towards the imps with one of the crystals I was supposed to deliver and fended them off. The woman was unconscious so I carried her all the way back to Randel... I couldn't really do much more than that."
                    l "Wow... Is she okay?"
                    mc "Yes. I've let her stay at my place since, y'know... her town burned down."
                    l "I hope she's alright now."
                    mc "She is."
                else:
                    mc "There were so many imps there... I couldn't really have done much, so I had to run away."
                    l "Oh..."
                    mc "If I was stronger maybe I could've saved some people, but..."
                    l "...imps aren't weak monsters."
                    mc "....Yeah."
                    l "Maybe if it had been one or two you could've done something... But imp packs are scary."
                    l "Did you know that Randel was attacked as well once?"
                    mc "No, I didn't. When?"
                    l "Oh, decades ago. During King Olin's reforms. Thane became unstable and Randel began taking in many citizens... All the movement around the town attracted some imps which tried to attack the city. They killed very few people fortunately since all of Randel's Gold and Diamond adventurers were in town."
                    mc "Wow... I would've loved to be there to see it."
                    l "Seeing all those adventurers fight was one of the coolest thing I had ever seen."
                    mc "I'm sure it was."
                l "On what other quests have you been?"
                $ toldLoriYokel = True
                $ toldLoriMore += 1
                jump tellingLoriAboutYourAdventures
            "Tell her about the Delivery Quest" if corbanDone == True and toldLoriDelivery == False:
                mc "Well there's this one time I went to Corban to deliver a sword."
                l "Tell me about it."
                mc "Well, the quest itself wasn't really anything worth talking about. It's what happened afterwards that's the cool part..."
                mc "...Though I'm not sure I can tell you, now that I think about it."
                l "Oh c'mon [mc]. You know I don't have anyone else to tell that to."
                mc "...You promise you won't tell?"
                l "Pinky promise."
                mc "Okay then I'll tell you what happened."
                mc "After delivering the sword, I wandered a bit around Corban... and that's when I saw General Taliya."
                l "General Taliya was in Corban? Why? Corban is a very small town..."
                mc "Indeed. She was there to track down a criminal organization who was selling drugs around the Kingdom."
                mc "She decided to have me help her, so I went in first and I talked to the boss while pretending to be someone looking to buy a shipment of drugs to make competition to some guy. I somehow convinced them and then..."
                mc "{i}Let's not say that a stranger sucked my dick."
                mc "Taliya went in and, uhm... Killed all of them in a matter of seconds."
                l "Wow."
                mc "Yeah she's the strongest person I know for sure."
                if toldLoriMore > 1:
                    l "It's weird hearing you tell me about these adventuers... In half of these you aren't even the one doing most of the cool stuff."
                    mc "What can I say? I'm still weak. There's so many people stronger than me... and one day I'll be just as strong."
                    l "Then I'll watch over your rise as a hero closely."
                    mc "Oh really? I'm glad you will."
                    "Lori blushes slightly"
                l "What else? Any other fun adventure you wanna tell me about?"
                # MC tells Lori about the Delivery Quest
                $ toldLoriDelivery = True
                $ toldLoriMore += 1
                jump tellingLoriAboutYourAdventures
            #"Tell her about the Ledric" if ledricquest > 0 and toldLoriLedric == False:
                # MC tells Lori about his encounter with the Ledric
                ########
                # I NEED TO REPLAY THAT, I DON'T REMEMBER WHAT HAPPENS THERE
                ########
            #    $ toldLoriLedric = True
            #    $ toldLoriMore += 1
            #    jump tellingLoriAboutYourAdventures
            "That's it" if toldLoriMore > 0:
                mc "...Yeah, that's pretty much it."
        l "Ahhh...! Just hearing about your adventures gets me so excited."
        mc "Really? They're not anything special..."
        l "Oh, maybe that's what you think, but I haven't done anything even remotely as exciting outside of my dreams."
        mc "Admittedly, in retrospective they're more fun than they were in the moment."
        l "You think so?"
    else:
        mc "Well... I haven't really been on any."
        l "What? Really?"
        mc "Well, not yet."
        l "Ah that's a shame..."
        mc "I'll make sure to go on some and tell you about them later."
        l "I'll gladly listen to you when you'll have some adventure to tell me about then."
    l "I know I can't speak from experience, but..."
    l "Going on adventures and seeing the world, Overcoming obstacles and fighting monsters... It all sounds so fun."
    mc "Yeah, you're right. That's why I joined the guild, after all. But as a Bronze you don't get to do too much of that... I wish I could get to Silver more quickly."
    l "I'm sure you'll get there one day, and then maybe I'll geek out about your adventures."
    mc "Hah, I'd be flattered if that were ever the case."
    l "Do you have a favorite adventurer?"
    mc "I do, but I'll admit it's kind of a basic choice."
    l "...is it Gladius Hans?"
    mc "What? No, not {b}that{/b} basic. It's Aghelos."
    l "Wait, really?"
    mc "Yup. Randel's Shiny Diamond is my favorite adventurer. Basic, but can you blame me?"
    l "I can't blame you at all, he's my favorite too!"
    scene loridaydreaming with fade
    l "Everyone always talks about him, but not many know how cool he actually was."
    l "You see, Aghelos didn't just fight monsters and demons. He saved Randel during the Great Breach and killed a Demon General, but that's not all that there is to him. Aghelos was strong just as much as he was kind."
    l "You probably know that he came from a poor family in Randel, right?"
    mc "Yeah, and when he went to the Academy his instructor noticed his talent and told him to sign up at the Adventurers' Guild."
    l "And you probably don't know much of what happened between his signing up and his life as a Diamond adventurer, do you?"
    mc "...Not really, no."
    l "That's the part that fascinates me the most. He was talented and destined to achieve great things, yet... he had to go through the same steps any other adventurer had to go through. It took him years to reach Diamond-Rank."
    l "And he did lots of things during those years."
    l "When he reached gold he realized he was making way more money than he needed for himself. Most people in his situation would've used all that wealth for themselves."
    l "Buying land, and securing a luxurious future... yet he started giving most of his money back to the people."
    l "You know the square around which the market distric is built?"
    mc "Yeah? What about it?"
    l "It used to be a grass field before he funded what's there now."
    mc "Wow. All by himself?"
    l "Yup."
    mc "That's amazing... I didn't know any of that."
    l "Did you know he had a companion for most of his days as a Silver adventurer?"
    mc "He did? I always thought he was a solo adventurer..."
    l "Oh no, not at all. Even during his diamond days he often collaborated with other adventurers... They're just not as famous."
    l "But he only had one stable partner, and that was Ellie."
    l "They reached Silver at the same time and began adventuring together. And even though Ellie was never going to be as good as Aghelos, they stuck together."
    l "Ellie was weak even for her own rank. She wasn't good at using weapons or magic, you could say she wasn't fit for anything more than Bronze, but she was good at everything else."
    l "She knew how to read maps and had a great sense of orientation, she knew how to avoid traps and was very, very smart. Some say that she knew the Book of Monsters like the inside of her pockets... "
    l "She did everything she could to compensate for her lack of strength, and she was rewarded by being the only adventurer to form a party with Aghelos."
    l "I know I'll never be strong, so even if I admire Aghelos, I aspire to be like Ellie."
    mc "You really should just sign up at the guild. Even if it was just one quest, I'm sure you'd enjoy it."
    scene readtalk1 with fade
    l "Mh... I'll pass. I like daydreaming about these things, but good ol' me has to take care of this library, I can't just leave and do whatever."
    mc "I'm pretty sure you can, but you do you."
    l "Well, since you insist, I'll think about it. Now I have to go reorder some books, it's already pretty late."
    mc "Have fun with that. See ya."
    l "See ya!"
    "You leave the library and go back home."
    call magicLevel
    $ loriEventValue += 1
    $ time += 1
    $ persistent.loriDayDreaming = True
    jump home



label lori1:
    hide screen hud
    "Studying with Lori is really fun. Even though the topic at hand is Astyllian, she still manages to make it fun. It's really true that a good teacher makes the difference."
    "After you're done studying, you close the book and lean back, stretching yourself."
    scene readtalk1 with Fade(0.5, 1.5, 1.0)
    mc "Ahh... Thanks, Lori."
    l "It's nothing. I told you I like helping out."
    mc "I know, but you're such a good teacher that I need to thank you regardless."
    "Lori blushes."
    l "Th-Thanks."
    "The two of you sit in silence for a while. You're not sure why you're not just leaving."
    l "So... How's the academy?"
    mc "Ah it's... It's okay."
    l "Is it fun? I've... never gone to the Academy."
    mc "You... didn't go to the academy?"
    scene readtalksad with dissolve
    "Lori looks down for a moment."
    l "No, I... You see, my mother was a slave."
    mc "...A slave?"
    l "Yeah, she was a slave... and so was I. When I was born, King Olin still hadn't outlawed slavery among those born on Astyllian soil, and throughout all of my adolescence I was, well, a slave."
    mc "Wait, wait- How old are you? I'm pretty sure slavery has been outlawed since I was born."
    l "I-It's rude to ask a lady her age, y'know?"
    mc "Oh, I-I'm sorry..."
    l "...I'm 52."
    mc "Oh, wow."
    l "Surprised?"
    mc "I'll admit I thought we were peers."
    l "Heh... But even if I'm so much older, I really haven't lived much more than you."
    mc "What's that mean?"
    l "Well... Slaves don't really get to do much, and librarians stay in the library all day long."
    "You see Lori looking up at the ceiling of the library."
    l "I've probably seen and done much less in my 52 years of life than you have in just 19. I haven't had many friends either..."
    mc "Oh, I... I'm sorry."
    l "Hey, it's fine."
    "She glances at you."
    l "You don't have to be sorry — we are friends after all, aren't we?"
    mc "...We are, but are you sure that's enough?"
    l "Of course. When you haven't had many friends, one more friend means a lot."
    menu:
        "I'll do my best then":
            scene readtalk1 with fade
            $ loriBest = True
            mc "Then I'll make sure to make it mean even more."
            "You see Lori blush slightly."
            l "A-Aw, there's no need to do that..."
            mc "What do you mean there isn't? You just told me you haven't experienced much of the world! If we're friends, I must help you make many more experiences!"
            "You can see Lori's cheeks flush even more with each and every one of your words."
            l "I-I get it, I get it! P-Please stop saying all those embarassing things..."
            mc "What are you talking about? It's not embarassing. I'm just being earnest."
            l "Y-Yeah... You are."
            "Lori smiles at you and then sighs."
            l "Alright, I've kept you here long enough. I need to go order some returned books, see you next time."
            mc "See you, Lori."
        "Thanks":
            scene readtalk1 with fade
            mc "Oh, well, thanks,"
            l "Thank you, as well, for being my friend."
            "Lori sighs."
            l "Well, I won't hold you any longer. I need to go order some returned books, so I'll see you next time."
            mc "Alright, see ya."
    scene black with dissolve
    "You wave at her as she leaves your side. Then you get up and leave the library."
    call magicLevel
    $ loriEventValue += 1
    $ time += 1
    jump home



label lori2:
    hide screen hud
    "As the two of you are studying, you notice she's got a book with her today that you didn't see her before with."
    scene readtalk2 with Fade(0.5, 1.5, 1.0)
    pause 2
    "When you ask her what it is, she blushes and puts it behind herself as if to hide it from you."
    scene loripanic with fade
    l "I-It's nothing, just something I'm r-reading..."
    mc "...Huh. Okay."
    scene animationreadl with fade
    "The lesson continues like normal from there forward, but she keeps the book away from you during the entirety of it."
    "When you're done studying, you say goodbye and leave."
    scene villageback with fade
    mc "{i}I wonder what that was about..."
    call magicLevel
    $ loriEventValue += 1
    $ time += 1
    $ persistent.loriEmbarassedPanic = True
    jump home



label lori3:
    hide screen hud
    "As usual, the lesson goes by like nothing. You're honestly impressed by Lori's teaching skills. From the way she talks one would assume she has rarely ever taught before, and yet she's very good at explaining."
    "Still, the weirdest thing is how well she knows Astyllian. Common folks don't really study Astyllian if not at the Academy, which she already said she hasn't gone to."
    scene readtalk1 with Fade(0.5, 1.5, 1.0)
    mc "You know Lori, I was wondering... how do you know Astyllian so well?"
    "You see Lori immediately tense up at the question."
    scene readtalksad with fade
    l "Ah, it's.. a long story."
    mc "Well, I have time."
    l "..."
    mc "...So?"
    l "It's kind of personal, and not really a fun story, so..."
    menu:
        "I still want to know":
            $ loriInsisting = True
            mc "I would still like to know... It can't be that bad, it's just Astyllian."
            "Lori doesn't reply, for a moment you think she's ignoring you on purpose, but that's unlike her. No, you understand what she's actually doing when you hear her sob."
            mc "H-Huh?"
            scene loricry with fade
            mc "Wow, okay, sorry, I didn't mean to-"
            l "I-It's fine, It's not your fault I'm j-just..."
            mc "C-Can I do some-"
            l "I-I've got something to do, S-See you tomorrow."
            "Before you can say anything more, she walks away. You stand there dumbfounded."
            scene library with fade
            mc "{i}Is it really {b}this{/b} bad? Wow..."
            $ persistent.loriMadeCry = True
        "Let her be":
            mc "Okay, if you don't want to tell me it's fine. I didn't mean to hit a sour spot..."
            scene loridistant with fade
            l "It's... fine."
            mc "{i}I wonder what must have happened if she feels so bad from even just asking about it... And it's not like she teaches me Astyllia unwillingly. In fact, she pretty much volunteered."
            mc "I'm still sorry, I won't ask again."
            l "Thanks... I-I have to go and do something now, see you."
            "Before you can say anything she runs away. Seeing her like this makes you feel really bad."
            scene library with fade
            mc "{i}How should've I have known this would be her reaction? Damn it."
            $ persistent.loriDistant = True
    mc "{i}Maybe I should ask around...? It can't be just the language itself, and if I don't want this to happen again I should probably find out what it is to avoid the subject..."
    mc "{i}...Who am I kidding, I just really want to know, now."
    "You leave the library and go home."
    call magicLevel
    $ loriEventValue += 1
    $ time += 1
    jump home



###################
## ALL RESPONSES ##
###################
label borisInfoDump:
    mc "{i}Mh... Scarlet and Taliya probably won't know anything being new in town and all... Maybe I should ask Boris?"
    "A chill runs through your spine."
    mc "{i}Yeah... he's probably the only one who'd know anything about it."
    scene lecture with fade
    "You sheepishly walk into the history class. You see Boris cleaning his blackboard."
    mc "Uhm, excuse me?"
    scene lecturetalk with fade
    b "Yes?"
    mc "I know this might be unproper but... Do you mind if I ask you about Lori?"
    b "Lori? The librarian, you mean?"
    mc "Yes, her."
    b "Well, I haven't seen her in a while for sure... I don't go often to the library these days."
    b "I used to go to the library every single day when I was younger. Lori's mother is such a sweetheart. She's actually the one who taught me how to read when I was a kid."
    mc "Really?"
    b "Yeah. She caught me sneaking into the library once and decided to teach me something useful."
    "Boris looks at the blackboard, then back at you."
    b "I'm extremely grateful to her."
    b "...What did you want to know abot Lori?"
    mc "Well... She's been teaching me Astyllian, so the other day I asked her why she knows Astyllian so well and..."
    b "Oh, yeah... You see, Lori's father was an elf noble. He got Martha pregnant and then never showed up again."
    mc "Oh."
    b "As much as I respect her... I can't say she's not delusional. She still thinks he'll come back for them... and because of that she's taught Lori Astyllian, to prepare her for that day."
    mc "Oh that's... sad."
    b "It is."
    mc "Well... Thank you, Mr. Boris."
    b "You're welcome. Say hi to her on my behalf."
    mc "I will. See you."
    "You leave the classroom."
    $ askedAboutLori = True
    return
label gabeInfoDump:
    mc "Gabe... You know Lori?"
    g "Yeah?"
    mc "What can you tell me about her?"
    g "Besides the fact that she's great?"
    mc "Well, uhm, yes."
    g "I can tell you that she's precious. And smart. And a bit of a goof."
    mc "Yeah, sounds about right."
    g "She always helps me out when I need something..."
    mc "...Do you know why she knows Astyllian so well?"
    g "Uh... I think it's because of her father? I don't know much about it, but he's supposed to be where she got her elf half from."
    mc "I guess that makes sense..."
    g "I've heard she has never met her father though, so there's probably some issue there..."
    mc "Oh, I see."
    g "Like I said, I don't know much about it. I'd tell you to ask Lori, but I don't think she's too keen on talking about that kind of stuff."
    mc "That makes sense. Thank you anyways."
    g "You're welcome!"
    $ askedAboutLori = True
    if GabeHome == True:
        jump gabehouse
    else:
        jump academy
label julyInfoDump:
    mc "Yeah, uhm... Do you know anything about Lori?"
    j "The librarian?"
    mc "Yeah, her."
    if sawjuly >= 4:
        j "I know lots about her."
        mc "You do?"
        j "I can still remember when she used to sneak out from her duties to come beg adventurers to take her with them to Thane."
        mc "Thane? Why Thane?"
        j "Her father is supposed to be an elven noble from there. She has never met him and her mother was so convinced he'd come back for them that she managed to convince her daughter too for a short while..."
        mc "Oh, that's... awful."
        j "Yeah, though that's why she's so well educated. Her mother wanted to make her into the best daughter a noble could desire... I believe Lori can speak Astyllian fluently."
        mc "...Because it's the elven language."
        j "Exactly."
        j "She's grown to be a far more reserved woman... I'm glad that she stopped pursuing her mother's delusions, at least. Her brains are wasted on something like that. She's easily one of the smartest people I've ever met."
        mc "Wow, really?"
        j "Indeed. And I commend her futher for being like that despite being born a slave."
        mc "I guess some people are simply gifted in some ways."
        j "Yeah, that's true... But for each gift there's a curse. She's a genius trapped by her situation into being a simple librarian."
        mc "..."
        j "I hope she'll find her own way."
    else:
        j "Well, I don't know too much about her... I don't really leave this place too much, and she doesn't leave the library too often either. Everything I know is by hearsay."
        mc "Like what?"
        j "Like the fact that she's smart, or that she used to come around the guild when she was younger... Or, I guess, the fact that she's never met her father."
        mc "Wait, really?"
        j "Apparently he was some sort of noble elf who came by once and never came again. She's only had her mother her whole life."
        mc "{i}An elf... that would explain the Astyllian."
        mc "I see. Well, thank you regardless."
        j "You're welcome."
    $ askedAboutLori = True
    return



label loriLoreDump:
    scene loridistant with fade
    $ persistent.loriDistant = True
    l "You've probably already guessed I'm a half-elf... Well, that elf half is from my father side."
    "You stay silent, letting her continue her story."
    l "My mother fell in love with him while he was visiting. He was a minor noble, accompanying some other nobles who came here on a visit. My ex-master's family was trying to build connections with Thane and solidify their status in Randel..."
    l "...They failed, but thanks to those attempts, that noble elf ended up taking my mother to his chamber and... well, here I am."
    l "That noble never came back after that, but my mother never stopped loving him. She was sure he'd come back for her and take us with him... But she wasn't even allowed to say his name."
    l "She made sure I studied Astyllian and brought me up as if I was ever going to be more than a slave..."
    l "Still, I love mom. She made me into the person I am today and, in a way, she was right: I'm not a slave anymore."
    l "But even if I'm a free woman... How can I leave the place I grew up in? And I certainly can't leave my mother now that she's bedridden, can I?"
    mc "..."
    l "Being half elf isn't great when your only parent left isn't an elf... Looking like a teen by the time your parents are old isn't the greatest feeling ever."
    l "And so, here I am, wasting my life in a library, where I'll probably be for the rest of its duration..."
    mc "That's... a lot."
    l "I know, don't worry..."
    return

label loriApologizing:
    mc "{i}Should I go apologize right now?"
    if askedAboutLori == False:
        mc "{i}I still don't know what made her react that bad..."
    menu:
        "Yes":
            if askedAboutLori == False:
                mc "{i}Yes let's do it. I don't need to know what happened to apologize."
            else:
                mc "{i}Yes, let's do it."
        "No":
            mc "{i}...Not yet."
            jump library
    jump lori4
label lori4:
    hide screen hud
    scene library with fade
    "It takes some walking before you find Lori in the library. When you do find her, she's puttin some books on a shelf. She doesn't seem to notice you as you walk up to her."
    mc "Hey... Lori."
    "She jumps and turns around."
    l "O-Oh! Hi, I didn't hear you walk in..."
    mc "Well, it's a library, I didn't want to make too much noise..."
    l "Yeah, that's true..."
    "The two of you look at each other in silence for a while, both of you have something to say to each other."
    "[mc] & {color=#8C79C6}Lori{/color}" "I'm sorry."
    "Turns out it was the same thing."
    if loriInsisting == True:
        mc "What? Why are you sorry? I was the one who insisted."
        l "I... didn't want to make a scene in front of you, I'm sorry."
        if askedAboutLori == True:
            mc "That wasn't even slightly your fault. Even if I didn't know about your father I shouldn't have insisted."
            l "W-Wait, m-my father? How did you know?"
            "You look down for a moment, feeling guilty for having invaded her privacy, but then you look up at her again."
            mc "I asked around. I wanted to know what made you feel so bad so that I would make sure it didn't happen again."
            l "...Sigh."
            l "Thank you, [mc]. For being considerated."
            mc "I wasn't the other day. I'm sorry."
            "Lori smiles."
            l "You're forgiven."
        else:
            mc "That wasn't even slightly your fault. Whatever it is that made you cry, it was my fault that it was brought up. I'm sorry."
            l "I'm... No, it's my fault, I could've just told you what it was. It's not really a secret."
            mc "Do you want to tell me what it was now?"
            l "..."
            l "I do."
            mc "Then I will listen and, hey, if you feel like crying again... My arms are free for a hug."
            l "Heh, thank you, [mc]."
            call loriLoreDump
            scene library with fade
    else:
        l "W-Why are you sorry? I was the one who treated you coldly out of nowhere."
        if askedAboutLori == True:
            mc "I didn't take offense, even less now that I've asked around about it."
            l "...You what?"
            mc "Ah... I was worried. I want to treat you right and since I didn't know what it was that made you feel so bad, I went around and asked about you..."
            mc "...I'm sorry about your father."
            l "..."
            l "...It's fine."
            mc "Is it?"
            l "It's not your fault. And I can't really do much about it if not move on."
            mc "You... could look for him."
            l "And then what?"
            "Lori paused for a moment."
            l "...I don't wanna end up disappointed."
            "Even though you were an orphan, you really couldn't understand what she felt like. Ever since you were a child you knew that you only had Uncle Pete. You didn't have anyone to actually look for like she did."
            "You nodded lightly."
            mc "I see."
        else:
            mc "I don't care. I'm sure you had your reasons to feel bad even though I don't know them."
            l "B-But I-"
            mc "Nuh-uh, no but's. If you want to make up for it you can give me a hug instead."
            l "..."
            l "I-I'll tell you what it was, if you don't mind."
            mc "That's fine as well. I'll happily listen."
            l "Alright... It's not really a happy story though."
            mc "I assumed as much."
            call loriLoreDump
            scene library with fade
    l "But, hey, it's not all bad. If it weren't for him, I would've never learned Astyllian. We wouldn't be friends."
    mc "...I guess that's true."
    l "And thanks to learning Astyllian and living in the town's biggest library, I've learned a lot about how magic works and stuff. And by a lot I mean {b}a lot."
    mc "How much is a lot?"
    l "...Wanna see?"
    mc "See? You're gonna cast a spell here?"
    l "Oh no, no. Let me show you."
    scene black with fade
    "Lori starts walking away and you follow her through the library up until you reach a door you've never seen before. She opens it. The other side isn't lit so you can hardly make out what that room is supposed to be."
    scene lorireveal with fade
    l "It took a lot of begging for them to allow me to use this room."
    mc "Use it? for what?"
    l "Experiments."
    "Lori flicks some device next to the entrance and suddenly the room lights up."
    scene lorilab with fade
    l "This is my laboratory. I experiment with magic crystals here."
    mc "Wow that's... unexpected. You never told me about it before."
    l "Hehe... It's kind of my secret little passion project."
    mc "Passion project?"
    "You point at her collection of magic crystals, probably worth a lifetime of work."
    mc "You call that a passion project?"
    l "Well, I've told you I'm old... Plus, I don't really have anything else I need to spend money on."
    mc "Huh... I guess you've got a point."
    "Lori begins wandering around the lab as you also do the same, inspecting every single thing you see. Lots of these crystals laying around seem to have weird contraptions around them which purpose you don't know. You decide to ask about them."
    mc "Are these... Your experiments?"
    l "Oh, yeah!"
    mc "What... do they do?"
    l "Most of them do nothing."
    mc "Oh."
    l "That's why they're experiments."
    mc "And what are you trying to do exactly?"
    l "Do you know how crystals work?"
    mc "Uh... not exactly."
    l "Well, they're basically a way to store mana that can be reused later. They're pretty handy if you don't want to wait to gather mana for spells. It doesn't make much of a difference with low-level spells, but when it comes to stronger ones, they're very useful."
    if TaliyaQ > 3:
        mc "{i}So that's why Taliya uses that crystal..."
    l "The main problem with them is the time it takes to recharge them... And the fact that they need to be attuned with you before you can use them."
    l "So what I've been trying to experiment with are machines capable of casting set spells independently of their caster."
    mc "How? Don't you still need to cast them?"
    l "That's the thing! You don't have to if you use runes!"
    mc "Runes? But don't runes keep casting a spall until they run out of mana?"
    l "That's exactly what I'm trying to solve."
    mc "How?"
    l "That's... the tricky part."
    mc "So you haven't made much progress, huh?"
    l "Well, that's incorrect. I've made a lot of progress... Just not enough."
    "Lori points at some of the machines in the laboratory."
    l "Those ones, I never managed to make them work."
    "Lori then points at some other machines."
    l "Those ones worked once, then broke down and I haven't been able to fix them."
    "Finally, Lori points at another group of machines."
    l "...and those need the crystal to be fully charged to cast the spell once, which makes them useless."
    "Lori sighs."
    l "This is already a lot of progress, but I'm still far from obtaining my goal. Now my biggest obstacle is calibrating the runes and the wait time of the mechanisms so that the same spell can be cast multiple times using the same crystal core, but that's-"
    "Lori blushes lightly and looks at you."
    l "Sorry, I'm probably boring you with all of this, am I not?"
    mc "You're definitely not."
    "She blushes more."
    l "I am not?"
    mc "No, you aren't. I might not understand what exactly you're talking about, but that's exactly why this isn't boring. It sounds like you're doing something amazing to me."
    mc "You're a half-elf, you've got plenty of time to keep researching this, don't you? You'll get there at some point."
    l "...Thanks [mc]."
    mc "You're welcome."
    "The two of you stand in silence for a few moments, then Lori speaks up."
    l "Th-There's not much else to show you here. Let's go back."
    mc "Okay."
    scene library with fade
    "The two of you go back to the library and after some more chit chat you decide it's time to go home."
    mc "Well... Once again, sorry for making you think about that... stuff."
    l "It's fine, [mc]. Don't worry. Thank you for being my friend."
    mc "There's no need to thank me, I enjoy being your friend."
    l "Heh. Me too."
    mc "Alright then. Now it's time for me to go. See ya!"
    l "See you, [mc]."
    $ loriEventValue += 1
    $ time += 1
    $ persistent.loriReveal = True
    jump home



label lori5:
    hide screen hud
    scene readtalk1 with Fade(0.5, 1.5, 1.0)
    if justStraightUpAskedHer == False:
        "The two of you study together like always."
        "While you do, you think to yourself..."
        mc "{i}Let's invite Lori on a quest with me."
    mc "Hey Lori."
    l "Mh? What's up?"
    mc "How about I take you out adventuring?"
    l "H-Huh?"
    mc "You said you would've liked to go adventuring, so I thought... why not? Let's go on an adventure together."
    l "But I- A-Are you joking with me?"
    mc "What? No, I'm serious. Many low-level quests are easy, and I'm sure you would have fun."
    l "But I've never been on a quest! What if I hold you back or something..."
    if flirtingWithLori == True:
        mc "You won't. Plus, it's not like I mind having a cute girl like you come on a quest with me."
    else:
        mc "You won't. Plus, it's not like I mind having people accompany me on quests."
    "Lori blushes."
    l "W-Well, I wouldn't mind either, but... I can't just leave the library unattended."
    mc "Then I'll find someone and ask them to take care of the library for a day."
    l "I'm not sure that's a good idea, [mc]."
    mc "I'll find someone trustworthy, I promise."
    l "Sigh... Fine, I'll allow it."
    mc "Hah! Good, I'll go now, then. See you soon!"
    l "S-See you..."
    "You leave the library"
    scene villageback with fade
    mc "{i}I wonder who could take care of the place for a day..."
    mc "{i}A friend who would be willing to help me and Lori out... Who is trustworthy and knows their way around the library... Who-"
    mc "{i}Gabe! That's who I can ask that to!"
    mc "{i}I'll go ask her as soon as I can..."
    if justStraightUpAskedHer == False:
        call magicLevel
    $ time += 1
    $ loriEventValue += 1
    jump home



label lori7:
    hide screen hud
    show prot normal with fade
    mc "{i}I should probably tell Gabe I'm planning to go today..."
    g "Hey there, [mc]."
    mc "{i}Huh?"
    show gabrial hoodie smile
    g "Good day, bozo."
    show prot smile
    mc "Oh, hi there Gabe! I was just about to come look for you."
    g "Let me guess, needed me to take care of the library?"
    mc "Uhm, yeah. How did you know?"
    g "First of all, you asked me to. Second of all, I saw you going towards the library and figured that maybe you were going to the library to pick up Lori and just forgot to come to me first."
    mc "...Yeah I did forget."
    g "See? You should be thankful you've got such a good friend."
    mc "Oh, I consider myself very lucky, don't worry."
    l "Oh, hello you two."
    show gabrial hoodie smile at flip
    show smilel
    with fade
    l "What are you doing here?"
    mc "I'm here to take you on a quest... And she's here to take care of the library."
    g "Hi."
    l "Oh, you'd really do that, Gabe?"
    g "Of course I would. I'm your friend, and this goofball here is my friend too. You guys are there when I need y'all, so I'm here now that you need me."
    l "W-Wow... Uhm, thank you."
    g "You're welcome... But are you sure you're going to go on a quest dressed like that?"
    l "Wha- No, I just wasn't expecting this so I-"
    l "Ahhh! I'm gonna go change right now!"
    hide smilel with easeoutleft
    "Lori storms off in a rush."
    g "Lori's livelier than usual. She must be really excited."
    mc "I was that excited too when I joined the guild, honestly."
    g "I bet you were."
    g "Well, I'll be at the counter there. I doubt I'll have much trouble taking care of the place for a day, anyways."
    mc "You think so?"
    g "Well, most people don't know how to read, and most of those who can don't really have time to read books."
    mc "You do have a point. I hope you won't get too bored."
    g "I'll entertain myself with some books since I'm already here."
    mc "Hah, smart."
    g "See you later, then."
    mc "Bye bye."
    hide gabrial with easeoutleft
    scene library with fade
    "After Gabe leaves your side, you sit down and wait for Lori to come back. She's taking a while."
    mc "{i}How much time does she need to change? What is she even putting on?"
    l "I'm done!"
    "You hear Lori's voice and turn around just to see her there in front of you. You immediately understand why it took her so long."
    show prot surprised
    show lori adv smile with easeinleft
    pause 1.5
    l "..."
    mc "{i}She..."
    menu:
        "looks cute":
            mc "{i}...She looks cute."
            $ loriLooksCuteLikeThat = True
        "looks weird":
            mc "{i}...She looks weird."
        "looks dumb":
            mc "{i}...She looks dumb."
    window hide
    pause 1
    hide lori adv smile
    show lori adv normal
    l "S-Stop staring so much..."
    show prot smile
    mc "Oh, sorry, I'm just..."
    if loriLooksCuteLikeThat == True:
        mc "...You look very cute."
        show lori adv blush
        l "O-Oh, th-thanks..."
    show lori adv normal
    mc "Why do you have that giant backpack with you?"
    l "I-I thought I'd bring some of my inventions along, you never know then they could come in handy..."
    mc "...Aren't most of them useless or broken?"
    l "Y-Yeah... I brought the ones th-that aren't."
    mc "..."
    mc "Makes sense. Shall we go then?"
    show lori adv smile
    l "Lead the way!"
    scene villageback with fade
    "The two of you bid Gabrial farewell and then leave the library."
    "You walk alongside Lori, attracting the attention of the onlookers. Lori definitely stands out, being so small while carrying such a huge bag."
    scene adventurersguild_day with fade
    mc "{i}I haven't exactly thought this through... Can I legally take Lori with me on a quest?"
    mc "{i}Let's just... not think about it."
    "You walk up to the quest board and see the different quests that have been put up on it."
    "You see lots of quests for Bronze adventurers and above, but you feel like they could be too dangerous for Lori."
    "Then, your sight places itself upon a quest for Recruits."
    show black with dissolve:
        alpha 0.5
    show text "{color=#fff}{b}{u}Investigate Demon Deer Sightings{/u}{/b}\n{i}Some merchants and locals have spotted a horned red-deer south of Randel. Investigate and kill if possible.{/i}\n{b}Rank{/b} — Recruit\n{b}Reward{/b} — 25 gold" with dissolve
    pause 10
    hide text
    hide black
    with dissolve
    mc "{i}A Demon Deer... This should be fairly simple."
    "You grab the quest from the board and then walk up to the counter."
    scene adgc2 with fade
    j "Greetings, [mc]. How can I help you?"
    scene adgc1
    mc "I'd like to take this quest."
    if level >= 10:
        scene adgc2
        j "...You're taking a quest below your rank?"
        scene adgc1
        mc "Y-Yeah..."
    "July peeks behind you and sees Lori. She smiles."
    scene adgc2
    j "Are you perhaps taking someone with you on a quest?"
    scene adgc1
    mc "W-What? Me? No, not at all!"
    mc "...Is it not allowed?"
    scene adgc2
    j "As long as you're there doing your part, the guild can't say anything."
    scene adgc1
    mc "Oh, thank Astylla."
    scene adgc2
    if sawjuly >= 4:
        j "It really makes me nostalgic to see her like this..."
    j "...She looks excited."
    scene adgc1
    mc "She is. Unfortunately this isn't exactly an exciting quest, but... I don't want to put her into danger."
    scene adgc2
    j "As you should."
    j "Well, the quest is yours. Have fun you two."
    scene adgc1
    mc "Thanks July."
    "July replies back with a smile. You leave and go back to Lori."
    scene adventurersguild_day with fade
    show prot smile
    show lori adv normal
    mc "Alright we can go now."
    l "She didn't say anything about me?"
    mc "She said it's fine as long as I don't leave you to do all the work."
    l "Really?"
    show lori adv smile
    mc "Yup. Let's go now."
    "The two of you leave the guild and head towards the forest."
    play music forest
    scene forest with fade
    if level >= 10:
        "Once there, you begin looking for any sign of the Demon Deer. You aren't usually this methodic when going on quests — especially if they're for a rank below yours — but you want to impress Lori."
    else:
        "Once there, you begin looking for any sign of the Demon Deer with extreme attention. You wouldn't usually be this careful while going on a quest like this one, but you want to impress Lori."
    scene loriquesttrap1 with fade
    "When you think you've found the area where the deer is, you begin setting up the trap."
    "Uncle Pete used to be a hunter before being a merchant, so he's taught you lots about the different ways to trap animals and beasts."
    "Demon Deers are remarkably simple to catch. You just need to set up a bait and find a way to trap their horns while they eat the bait. You can get the job done with just a few ropes."
    "The harder part would normally be finding the bait: Hollyflowers. Despite them not growing in all of Astylla, they're pretty common around Randel."
    scene loriquesttrap2 with fade
    "Considering all of this, it's more than reasonable for this quest to be ranked for Recruits. Demon Deers can be dangerous in packs, but a single one could be handled by almost anyone."
    "You and Lori spend some time setting up the trap, chit chatting as you do so. She's unreasonably excited despite how mundane this feels to you... But seeing her smile definitely makes up for it."
    scene loriquesttrap3 with fade
    "When you finish setting up the trap, you and Lori hide behind some bushes in silence, waiting for the deer to approach."
    "This is the boring part. Sitting in silence is all but exciting."
    "For one of you, at least. Lori seems to be on top of the world right now."
    "You don't know what it is, but seeing her so happy really makes you want to fill her face with kisses."
    "You sigh, hoping that at least it won't take long for the deer to appear."
    window hide
    pause 3
    "..."
    window hide
    pause 4
    mc "{i}Now I get why Uncle Pete changed profession."
    scene forest
    "You lay back and wait. There's no need to stare at the trap anyways. You just need to watch out for any noise."
    window hide
    pause 2
    show black:
        alpha 0.5
    show text "{color=#fff}30 minutes later..."
    with dissolve
    pause 2
    hide black
    hide text
    with dissolve
    "You feel Lori thugging your shirt."
    mc "Huh?"
    l "{size=-3}Shh! It's here."
    "You immediately sit up and peek with Lori."
    scene loriquestdeer with fade
    mc "{i}I hadn't heard it getting close... I guess staring half an hour at the trap wasn't useless."
    mc "{size=-3}Now we just wait for it to fall into the trap."
    l "{size=-3}And then we kill it."
    mc "{size=-3}Yup."
    "The deer looks towards your direction."
    mc "{size=-3}Shi-"
    scene forest with vpunch
    "The two of you quickly hide behind the bushes, hoping the deer didn't notice you."
    mc "..."
    l "..."
    "You stay there for what feels like an eternity, when suddenly..."
    window hide
    play sound rustle
    pause 1.5
    mc "{i}It worked!"
    "When the two of you look back up, the Demon Deer's horns are caught between the trap you set up."
    mc "Ah-hah!"
    l "We did it!"
    mc "Of course we did. Now let's kill it."
    "You walk up to the Demon Deer, paying attention not to step behind it. You wouldn't want to get kicked by it's hind legs."
    mc "Wanna do the honor?"
    l "C-Can I?"
    mc "Of course."
    "You hand Lori your sword."
    mc "Just cut its throat and it'll die quickly. It's easy."
    l "A-Alright!"
    "Lori carefully positions the sword below the deer's neck, then she cuts. Her movements are sloppy, and the cut just barely deep enough to do its job, but you don't say any of that to her face."
    play sound stab
    pause 0.5
    play sound fall
    "The deer falls dead to the ground."
    scene loriquestdeerdead with fade
    mc "That was easy wasn't it?"
    "Lori hands you back the sword."
    l "It was fun."
    mc "I'm glad."
    mc "Well, time to pack this up and go back to the guild."
    l "Wait, let me check something."
    mc "What is it?"
    "Lori kneels down in front of the deer, and begins inspecting the gem."
    scene loriquestgem with fade
    mc "What's up?"
    l "This gem... Do all Demon Deer have gems like these?"
    mc "I think so? I had never seen a Demon Deer face to face before honestly... I did hear that their gems were supposed to be blue though."
    l "And this is purple, isn't it?"
    mc "Yeah, I see that. What's your point?"
    l "This is... a magic crystal."
    mc "What? How?"
    l "I don't know how, but someone put a magic crystal into this deer's forehead."
    mc "Should we take it out?"
    l "Considering the size, it could be worth thousands. I don't see a reason to leave it here."
    mc "Fair point."
    l "Though I do wonder why someone would do something like this..."
    "You take out your knife and begin pulling out the crystal."
    l "It has to be for a good reason, nobody would waste this kind of resource for a random deer..."
    l "Unless..."
    "As you begin pulling the crystal out, Lori notices something."
    l "...There's runes carved on this crystal."
    mc "For what?"
    l "If you take it out I can try and reading the carving in full, but I think it's some sort of... communication device..."
    "You keep pulling."
    l "Meant to signal when..."
    l "[mc]! Wait don't-"
    "You finally pull it all out."
    scene lorigembeam with flash
    "As soon as the crystal leaves the deer's body, a beam of light shoots out of it and reaches for the sky."
    "The two of you sit in silence."
    window hide
    pause 2
    mc "What the..."
    l "I think we should leave."
    mc "I agree."
    window hide
    play sound rustle
    pause 1.3
    mc "...But I think it's too late for that."
    "You turn around."
    scene loriquestdrake with fade
    pause 2
    mc "Fuck."
    play sound drakeroar
    scene loriquestdrake
    pause 1
    mc "RUN!"
    play sound roarloud
    pause 0.3
    scene lorirun with vpunch
    pause 4
    "The two of you begin running away at full speed."
    "You could probably manage to escape on your own, but Lori is with you right now, and she's not really the athletic kind."
    "There's only one way Lori gets out of here alive. You need to buy her time."
    mc "{i}But how?"
    scene forest with fade
    "You keep running, the monster is very quickly catching up. Maybe if you turned around... No, you need a better place if you want to have any chances against that beast."
    mc "{i}There's a river that goes through the forest... If we found a bridge maybe..."
    mc "LORI!"
    l "Y-YEAH?"
    mc "FOLLOW ME!"
    l "THAT'S WHAT I'M DOING!"
    mc "I'VE GOT A PLAN!"
    l "WHAT IS IT?"
    mc "WE'LL REACH A BRIDGE AND I'LL HOLD IT OFF LONG ENOUGH TO LET YOU ESCAPE!"
    l "A-ARE YOU CRAZY?! HAVE YOU SEEN HOW BIG THAT MONSTER IS?"
    mc "I AM CRAZY ENOUGH TO WANT TO TRY THIS TO SAVE YOUR LIFE."
    l "H-HUH?!"
    mc "JUST DO WHAT I SAY!"
    l "O-OKAY!"
    "The two of you keep running. You're not sure where to find a bridge, but you know the forest well enough to find the Yill River."
    play voice [ river ] loop
    mc "{i}There it is!"
    "Once you've reached the river, it doesn't take you long to find a bridge across it."
    mc "Alright Lori. Don't stop running, alright?!"
    l "B-But-"
    mc "No but's! Go!"
    "Lori groans as you stop, but she does as you told her to."
    mc "{i}Alright... What do I do now..."
    "You turn around to face the monster with..."
    menu:
        "Your sword":
            play sound roarloud
            scene loriquestchasesword with flash
            "You hold out your sword, facing the monster, ready to fight it."
        "Your bow":
            play sound roarloud
            scene loriquestchasebow with flash
            "You draw your bow, facing the monster, ready to fight it."
        "Your magic":
            play sound roarloud
            scene loriquestchasemagic with flash
            "You hold out your hand and focus. You've learned a few spells while learning Astyllian... You're not sure if they're strong enough to take the monster down, but this is a good time to find that out."
    #scene loriblast1
    mc "{i}Alright, [mc]. Time to show this monster who's the boss."
    "You take a deep breath, trying to calm yourself before a fight you're not sure you'll be able to win."
    stop voice fadeout 3
    "But then..."
    play sound magic
    #scene loriblast2 with Fade(0.1, 2.5, 1, color="#fff")
    scene forest with Fade(0.1, 2.5, 1, color="#fff")
    "A magic beam blasts next to you towards the monster. With a single hit, the beast is lifeless on the ground."
    "You're left without words."
    mc "What the..."
    scene lorishoot with fade
    pause 2
    "You turn around and see lori on the ground with one of her inventions in her hand."
    mc "What did you..."
    scene lorihug with Fade(0.5, 0.5, 2)
    pause 2
    l "We did it!"
    mc "Y-Yeah!"
    l "I was so scared..."
    "The two of you stay like that for a few moments before Lori lets go of you."
    scene forest with fade
    show prot smile
    show lori adv blush
    l "..."
    mc "You alright?"
    l "Y-Yeah, I am."
    mc "Thanks for saving me."
    l "I couldn't just leave you."
    mc "Well, it's what I asked you to do."
    mc "But I'm glad you didn't. I wasn't really sure I could fend that monster off."
    l "You're an idiot."
    mc "An idiot who was trying to save you, cut me some slack."
    l "{cps=100}{size=-4}...I wouldn't want to be saved if you had to die.{/cps}{w=0.2}{nw}"
    show prot questiont
    mc "...Huh? What did you say?"
    l "N-Nothing! J-Just... Don't do something that reckless again."
    show prot smile
    mc "I'll try not to."
    l "...Thanks."
    mc "So anyways..."
    show prot normal
    "You look over at the monster on the ground."
    mc "...What the fuck was that?"
    show lori adv normal
    l "That's a Drake."
    mc "I wasn't really asking for its name... That kind of monster shouldn't be this close to Randel. And the magic crystal too..."
    mc "It's all just very weird. I can't say someone set this up intentionally, but this definitely isn't normal. I'll have to report it to July."
    l "The Guild Manager?"
    mc "Yeah, she needs to know about this. If we were some regular Recruits we would've died right there..."
    l "Thank Astylla that crystal had enough mana to power a shot."
    mc "Thank Astylla indeed."
    mc "Let's head back, now."
    l "Yeah let's go."
    scene adventurersguild_evening with Fade(0.5,3,2.0)
    "You arrive at the guild that's it's already evening. You tell July about everything that happened. She seems very worried and assures she'll have some Golds look into it."
    $ money += 25
    $ exp += 50
    call levellingUp
    show prot normal
    show lori adv normal
    mc "Alright, we can go home now."
    l "What did she say?"
    mc "She'll get someone to look into it... Apprently there's a lot of weird stuff happening around town recently."
    l "...That doesn't sound too good."
    show prot smile
    mc "It doesn't, but it's fine. Us adventurers will take care of it."
    show lori adv smile
    l "Not without me you won't."
    mc "There's no need to rub that in."
    l "Let me feel proud of my inventions the one time they prove themselves useful."
    mc "Okay, okay. Let's go back to the library now. Gabe's waiting for us."
    l "Alright."
    scene black with fade
    "The two of you walk together to the library. You accompany her up until the library's door and then stop."
    l "[mc]?"
    mc "Yeah?"
    l "Can you lean forward?"
    mc "Uh... Sure?"
    scene lorikiss with Fade(0.1,0.5,3)
    pause 3
    mc "..."
    scene black with flash
    "You see Lori's face become the reddest you've ever seen it become."
    "She lets go of your cheek and quickly dashes inside before you can say anything."
    "You stand there shocked for some time, then you see Gabe walk out of the library."
    g "Lori looked pretty embarassed. What did you do?"
    mc "Me? I didn't do anything."
    g "What happened then?"
    mc "...She kissed me."
    g "Hah! I didn't expect her to do that so soon."
    "Gabe pats you on the back."
    g "I'm going home. You better treat her right, lucky guy."
    mc "Wait, you knew?"
    g "It was obvious!"
    "Gabe waves as she walks away. You stand there for some more time, even more confused than before. Then, you decide to go home."
    $ time = 3
    $ loriEventValue = 8
    $ persistent.loriQuesting = True
    jump home



label lori8:
    hide screen hud
    scene library
    show blushl
    show prot smile
    l "Hey, [mc]..."
    mc "What's up?"
    l "I, uhm, was wondering if..."
    mc "{i}Is she... tryin to ask me out?"
    mc "{i}It would only make sense... Even Gabe said it: she likes me."
    mc "{i}Do I like her too...?"
    menu:
        "Of course":
            mc "{i}...of course I do, she's just {b}so{/b} cute!"
        "Not really":
            $ loriNotReally = True
            mc "{i}She fun, but I wouldn't really say I {b}like{/b} her..."
    l "{cps=90}...Th-There's this nice little cafe n-near the market d-district that I always w-wanted to go to a-and I was wondering if you'd come with me!{/cps}{w=0.7}{nw}"
    mc "Woah, woah, slow down."
    mc "{i}Yup. She just asked me out."
    l "S-Sorry..."
    "Lori looks down."
    if loriNotReally == True:
        mc "{i}Should I turn her down?"
        menu:
            "Yes":
                mc "{i}I'd rather turn her down while she's still too shy to ask me out on a date directly... I wouldn't want to break her heart later."
                hide blushl
                scene normall
                mc "It's fine, don't worry, it's just that... I'm very busy."
                l "Oh."
                mc "Y'know, between the adventuring and the academy, and all the other stuff..."
                l "Y-Yeah, no, I-I get it..."
                mc "I take some time to come over every now and then because we're friends, but I really can't spare any more time."
                l "..."
                mc "Sorry."
                l "{cps=60}{size=-4}I guess I got my hopes up for no reason..."
                mc "..."
                mc "...I'll see you around, then. I've got to go now."
                l "B-Bye..."
                $ loriDropped = True
                jump home
            "No":
                mc "{i}I'm not so cruel to do something like this to her."
                mc "{i}It's just a date anyways, she's not asking me to marry her."
    else:
        mc "{i}Astylla be blessed, she's so cute."
    mc "It's fine don't worry. I'll gladly come with you to the cafe."
    hide blushl
    show smilel
    l "Really?"
    mc "Just tell me when and I'll be there."
    l "...H-How about tomorrow?"
    mc "Yeah sure! I don't have anything to do."
    mc "Should we meet up here and then go to the Cafe or..."
    l "W-We can meet at the Market, i-if it doesn't bother you."
    mc "Oh, it doesn't. When?"
    l "Maybe... 5pm?"
    mc "Gotcha, I'll be there tomorrow afternoon then."
    "You can tell from Lori's expression that she just suppresed her urge to say \"Yay!\"."
    mc "Well then, I'll see you tomorrow."
    l "Yeah! See you tomorrow!"
    "You leave the library."
    scene villageback with fade
    mc "A date with Lori, huh?"
    mc "She's so shy she had to find an excuse not to call it a date, heh."
    mc "I guess I better get ready then."
    $ loriDateDate = day+1
    $ loriEventValue = 9
    jump home



label lori9:
    hide screen hud
    mc "{i}Alright, I'm in time... Now I just need to find Lori."
    "You begin looking around for Lori. Being short doesn't help her stand out in a crowd."
    "...Not like you're that much taller."
    l "[mc]!"
    "You hear Lori calling your name and you turn around towards the direction of her voice."
    scene loridatedress with Fade(0.1,0.8,2)
    pause 3
    mc "Oh wow you look... really cute."
    scene villageback with fade
    show prot smile
    show lori date blush
    l "Y-You think so?"
    mc "You always look cute."
    l "...D-Don't make me blush."
    mc "I think it's too late for that."
    "Lori mumbles something out of embarassment."
    mc "Well then, shall we go?"
    "You extend your hand towards her."
    l "W-We shall."
    scene villageback
    show black:
        alpha 0.5
    "She takes your hand, and the two of you begin walking towards the cafe she talked about."
    "You can feel how nervous she is just by the way she grips your hand. Every now and then she holds it tighter for a few seconds, as if she wanted to make sure you were still real, or that you wouldn't slip away from her grasp."
    scene cafe with fade
    play music lentorasgueado_heartbeater fadein 8
    if cynthdate > 0:
        "You quickly arrive at the cafe and realize this is the same place Cynthia took you out for your date."
        mc "{i}What a coincidence..."
    else:
        "You quickly arrive at the cafe she mentioned. It's a neat place for sure, though you haven't really ever been to a place like this before."
    l "Oh, look! There's some bards playing today!"
    mc "Wow, this place must've got lots of money if they can hire two musicians."
    l "I did hear it's a very neat place. Let's go sit down somewhere."
    mc "How about there? Next to the window."
    l "Oh, sure."
    scene loridate3 with fade
    "You sit down first, and then Lori sits in front of you."
    scene loridate1 with fade # smile
    mc "What should we eat?"
    l "Mhh... Let's see the menu."
    "Lori reaches for the menu and begins reading it."
    scene loridate2 with fade # menu
    pause 2
    mc "Is there anything that sounds tasty?"
    l "Well, I've heard that they make some really good cakes. Like this plum cake here on the menu... Should we order it?"
    mc "You mean that kind of sweet, soft bread with sugar on top?"
    l "Apparently they make it with chocolate here."
    mc "That definitely sounds tasty. Let's get one each."
    scene loridate1 with fade
    l "Alright!"
    scene black with dissolve
    "When the waiter arrives, the two of you make your order and then start waiting for it to arrive."
    scene loridate1 with fade
    pause 4
    mc "So..."
    l "Yeah?"
    mc "The other day I forgot to ask you if you liked going on a quest."
    mc "...Ignoring the fact that we almost died, I mean."
    l "Well... It was fun."
    scene loridate5 with dissolve
    l "I never thought I'd face a monster head on in my life, it was exciting."
    scene loridate1 with dissolve
    l "But also very, very scary."
    mc "Yeah, that's how it is most of the time. It's a lucky day when everything goes accordingly."
    l "I did end up gaining a magic crystal from things not going accordingly, though. I had never had one so big before."
    l "Maybe with it I'll manage to make some progress in my research..."
    mc "Really? That's great!"
    l "It is, though I'm still aiming to obtain something that can be used with smaller crystals... Otherwise it would be unpractical to manufacture."
    mc "I suppose that's true... Have you ever thought of going to the Capital?"
    l "Huh? Why?"
    mc "If you showed your work to the King he would be so impressed that I'm sure he'd fund your research."
    scene loridate4
    pause 2.5
    scene loridate1
    l "That would be incredible... But I doubt it's gonna happen."
    mc "Why not?"
    "Before Lori can answer, the waiter finally arrives with your two chocolate plum cakes."
    "Waiter" "Enjoy your meal."
    "[mc] & {color=#8C79C6}Lori{/color}" "Thank you."
    mc "Wow this sure does look good."
    l "Let's dig in, then."
    "The two of you begin eating the plum cake. You wouldn't say you're surprised that it tastes good, but it does taste really good."
    mc "We should definitely come here again."
    scene loridate4
    l "W-We should?"
    mc "Yeah! Food's great."
    scene loridate5
    l "...Yeah, let's come again some time."
    "The two of you keep eating in silence. Surprisingly being in silence with Lori doesn't make you feel awkward. She really looks like she's enjoying herself."
    "After she's eaten half of the cake, she seems to think of something and quickly gets up."
    l "Wait I'll be right back."
    scene loridate3 with fade # empty bg
    mc "Uh, alright."
    stop music fadeout 4
    "You wait there at the table while you watch her walk up to the bards. She says something to them and they respond by nodding. When she comes back she's smiling."
    play music mysunmymoonmysky fadein 5
    "As she sits back at the table, she giggles."
    scene loridate1 with fade
    mc "What was that?"
    l "I asked them if they could play a song."
    mc "What song?"
    l "My mom's and my favorite song."
    mc "Oh? What's it called?"
    l "I don't think it has a name, but my mom used to sing along with it making up her own lyrics, so I've always just called it \"Our\" song."
    mc "That's really cute."
    scene loridate4
    mc "I don't think I have a favorite song... But I like this one for sure."
    l "..."
    l "...You know, [mc]."
    mc "Mh?"
    l "I, uhm, really wanted to thank you. For everything, I mean."
    if loriBest == True:
        mc "I told you I'd do my best for you, don't you remember?"
        l "Y-Yeah, you did..."
    else:
        mc "You don't have to thank me. I did \"Everything\" because I care about you, after all."
        l "..."
    "You can see Lori struggling to find the words to say to you."
    mc "{i}Is she going to declare?"
    l "I..."
    l "I think I..."
    "You can see her ears twitching."
    l "...L-Like you...{p}...I l-like your shirt!"
    mc "..."
    mc "{i}Wow she really messed this one up."
    mc "{i}Let's prevent any more embarassment by pretending to believe her."
    menu:
        "I like my shirt too":
            mc "...I like my shirt too."
            l "..."
            mc "I always wear my best clothes to impress the ladies."
            l "...Do I count as a lady?"
            mc "Why wouldn't you?"
            l "..."
        "I like your shirt too":
            mc "Well, your shirt looks really nice too. I've already told you, but you look super cute in it."
            l "Th-Thanks..."
        "Thank you":
            mc "Well... Thank you."
            l "...Y-Your welcome."
    mc "So... Anyways..."
    "After that, you quickly change subject."
    scene loridate1 with fade
    "The two of you end up ordering another dish and talking for some more time. The situation has clearly gotten a bit awkward, but Lori doesn't try to declare herself again, so you decide to let her be."
    "After all, she probably wants to be the one to tell you how she feels first. She's inexperienced and shy, but she definitely has the determination."
    mc "{i}Plus, I really want to see what kind of cute face she makes when she finally spills the tea."
    l "Well... I'm full."
    mc "Yeah, me too. I think we can go."
    "You call the waiter who hands you the bill. It's 10 gold."
    mc "{i}Oh yeah, it's definitely expensive."
    l "Let's split the bill."
    if money < 10:
        mc "Actually... I don't really have the money on me."
        l "...Really?"
        mc "Sorry."
        l "How much you got?"
        if money == 0:
            mc "None."
            l "..."
            l "I'll pay for the two of us then. Consider it a payback for the crystal."
        elif money == 1:
            mc "...I've only got a single coin with me."
            l "Sigh..."
            l "Alright, I'll just pay for the two of us. Consider it a payback for the crystal."
        else:
            mc "Just [money]."
            l "..."
            l "Alright, I'll pay the difference then. Consider it a payback for the crystal."
            $ money = 0
        mc "Thank you very much."
    elif money < 20:
        mc "Alright, let's split."
        $ money -= 10
    else:
        menu:
            "I'll pay for you":
                mc "Let me pay for you as well."
                l "H-Huh? But I'm the one who decided to go to such an expensive place..."
                mc "And I enjoyed the food and the company a lot, so I want to pay for both of us."
                l "...Fine."
                $ money -= 20
            "Alright":
                "Alright, let's split."
                $ money -= 10
    stop music fadeout 5
    scene villageback with fade
    "Once the bill is paid, you leave the cafe and begin walking back home. You walk alongside Lori until you reach the crossroad."
    show prot smile
    show lori date smile
    l "You go south, right?"
    mc "I can walk you home if you want me to."
    l "N-No there's no need to do that."
    mc "You sure?"
    l "One hundred percent."
    mc "Okay, then I'll bid you farewell, m'lady."
    l "S-See you too."
    hide lori easeoutleft
    "You wave at her as she walks away. Once she's not in sight anymore, you leave and go home."
    mc "{i}...She's such a dork."
    mc "{i}Not that I'm any better, but she's a way cuter dork."
    mc "{i}I really wonder what will happen the next time I go and see her. Will she manage to tell me how she feels?"
    $ time = 3
    $ persistent.loriDate = True
    $ loriEventValue = 10
    jump home



label lori10:
    hide screen hud
    stop music
    scene villageback
    mc "{i}I wonder... How am I going to approach her when I'll see her now?"
    mc "{i}I'm not sure she bought my act during the \"date\"... I don't want things to be awkward between us."
    mc "{i}Should I just go and say hi like nothing?"
    mc "{i}No, maybe..."
    mc "Hello, m'lady."
    mc "..."
    mc "{i}No, that's awful. Let's stick with \"hi.\""
    scene library
    "When you arrive at the library, you find it deserted once again."
    "At first you think that Lori might be somewhere in the library ordering books, but you cannot seem to find her anywhere."
    mc "{i}This is weird... She never leaves this place alone."
    mc "{i}Where could she be...?"
    mc "..."
    mc "{i}The Lab!"
    "Quickly you make your way towards the lab. If she's not there you'll probably just give up and go home for the day."
    "Just as you reach the door and are ready to enter the lab, Lori comes out of it. The two of you crash into each other."
    play sound bang
    scene library with vpunch
    play sound fall
    pause 1
    scene lorispill1 with Fade(0.5,0.5,3)
    pause 1
    l "What the-"
    "Your body feels hot."
    l "Uh-oh."
    "You don't know why, but you're feeling extremely horny. Lori has probably noticed your raging boner by this point."
    scene lorispill2 with vpunch
    l "U-Uhm, [mc]?"
    mc "..."
    l "Y-You should probably get off me b-before-"
    l "...Oh."
    "You see Lori smile deviously for the first time ever."
    scene black with dissolve
    "She gets up and pushes you towards the library behind you. Her little hands begin unbuckling your belt."
    mc "...Lori?"
    l "I-I'll take care of this."
    "Once your dick is out, you see Lori flinch. The face she's making is unreasonably cute."
    mc "{i}Astylla, I want to fuck her so bad right now."
    "And almost as if answering your prayers, Lori puts her lips around the tip of your cock and slowly begins shoving it down her throat."
    scene loriblowjob1 with vpunch
    mc "Wh-"
    l "Ngh..."
    window hide
    pause 3
    mc "Bless Astylla this feels great..."
    scene loriblowjob2 with vpunch
    pause 2
    mc "Fuck!"
    scene loriblowjob1 with hpunch
    pause 1
    scene loriblowjob2 with vpunch
    pause 1
    mc "{i}Her mouth feels so good... My dick can barely fit in there."
    scene loriblowjob1 with hpunch
    pause 1
    l "Ngh... Mh... Nh-"
    window hide
    pause 1
    scene loriblowjob2 with vpunch
    l "Guh-"
    window hide
    pause 1
    mc "You're... Amazing."
    scene loriblowjob1 with vpunch
    pause 1
    mc "{i}I feel so hot... Is it because of that substance...?"
    window hide
    pause 1
    scene loriblowjob2 with hpunch
    pause 0.3
    scene loriblowjob1 with vpunch
    mc "{i}Shit- I don't know what it is, but I think I'm..."
    window hide
    scene loriblowjob1 with hpunch
    pause 1
    scene loriblowjob2 with vpunch
    pause 1
    scene loriblowjob1 with hpunch
    mc "Fuck- I'm gonna cum!"
    pause 2
    scene loriblowjob2 with vpunch
    pause 1
    scene loriblowjob3 with vpunch
    scene loriblowjob3 with flash
    scene loriblowjob3 with flash
    scene loriblowjob3 with flash
    l "Ngh-"
    window hide
    pause 2
    mc "Ahh..."
    window hide
    pause 1
    "Slowly, you feel your vision go blurry."
    scene loriblowjob3 with dissolve:
        blur 5
    scene loriblowjob3 with dissolve:
        blur 2
    scene loriblowjob3 with dissolve:
        blur 10
    "Then, you pass out."
    scene black with flash
    play music leitmotif_bass fadein 3
    pause 3
    "When you wake up, you find yourself in a bed you don't recognize."
    scene loribedroom
    mc "{i}What...?"
    "You try to remember how you ended up there, but the last thing you can remember is..."
    mc "{i}...Oh Astylla don't tell me we had sex."
    "You look around yourself. You had never been in Lori's room before now that you think about it."
    "The room itself is incredibly tidy. Books are scattered around the room, but they're all piled up neatly, purposefully. The only book sitting alone, separate from all the other ones, is next to the bed you're sitting it."
    "On the chair next to the bed sits a familiar book."
    mc "{i}Where have I seen it before..."
    "You try your best to remember where you've seen the book before, and then..."
    show loripanic with flash:
        blur 0.5
        alpha 0.7
    pause 1
    mc "{i}Right! It was the book she was reading!"
    mc "{i}...I wonder what's inside this book to be so embarassing for her."
    hide loripanic with dissolve
    "You start reading the back cover."
    mc "{i}This is it? It's just a romance novel! What a dummy."
    "But as you keep on reading, you start noticing something weird."
    "The book is about a shut-in girl who befriends an adventurer. The protagonist then ends up going on an adventure with said adventurer, then they go on a date, and then..."
    mc "{i}...She uses an aphrodisiac on the love interest."
    "For a moment you think this could be all a big coincidence, but quickly enough the truth seems plainly obvious."
    mc "Was she... trying to turn this book into a reality?"
    mc "{i}...Was she using me?"
    menu:
        "It can't be":
            mc "{i}...No she'd never do something like this."
        "It must be":
            mc "{i}...I guess I judged her wrongly."
    scene library
    show prot angry
    with fade
    show blushl with easeinleft
    "You get out of her bed and make your way outside. As soon as you step into the library you see Lori happily ordering books in one of the bookshelves. When she sees you she blushes and looks down, trying to smile."
    "You walk up to her with the book still in your hand. When she notices it, she takes a step back."
    l "Uhm..."
    mc "Why does this book sound so close to what happened between us?"
    l "I..."
    mc "I'm listening."
    l "..."
    l "...I didn't know how to do it."
    show prot question
    mc "Do what?"
    l "I..."
    stop music fadeout 1
    scene loriconfess with flash
    pause 1
    l "...I wanted to go out with you."
    mc "..."
    l "I've never liked anyone the way I like you and I didn't want to mess up, so..."
    l "...I used that book to help me."
    mc "..."
    mc "You used a... Fictional book...?"
    l "..."
    mc "You know these things don't work in real life, right?"
    l "What else should've I done?"
    if loriNotReally:
        mc "..."
        mc "I..."
        "{i}Do you like Lori?"
        menu:
            "I do":
                mc "{i}After everything that's happened... I think I like her now."
            "I don't":
                mc "{i}...I just can't get myself to like her."
                mc "I don't know."
                scene library
                show prot normal
                show normall
                with fade
                mc "...But I don't really like you that way."
                l "...Oh."
                mc "Don't get me wrong, I think you're neat, but... Can't we just stay friends?"
                l "..."
                scene loridistant with fade
                l "Y-Yeah, w-we can..."
                mc "..."
                l "S-Sorry I-"
                scene loricry with flash
                mc "..."
                l "I'm sorry I-"
                "You see Lori struggling to form a full sentence."
                l "...I think I'll go now."
                scene library
                show prot normal
                show normall
                with fade
                hide normall with easeoutright
                mc "..."
                mc "I think it's better if I go home now."
                scene villageback with fade
                mc "{i}...It's not my fault I don't like her."
                mc "{i}It's not hers either, she's just not my type. Ahh... I feel so bad. Maybe there was a better way to say that."
                jump home
                $ loriDropped = True
    mc "...You could've just told me."
    l "H-Huh?"
    "Without hesitation, you pull her into a kiss."
    scene lorifinalkiss with flash
    l "!!!"
    window hide
    pause 2
    "She kisses you back, even more intensely than you."
    "She pushes herself onto you, trying to kiss you even deeper, unable to contain her eagerness."
    "The two of you keep kissing, but you can feel Lori yearning for more as she moves her hands onto your belt again."
    "This time you decide to repay her favor by slowly taking off all of her clothes."
    "Once she's fully naked, you push her against one of the libraries."
    #scene black with dissolve
    #scene lorisexanimated
    #show black
    #hide black with dissolve
    #pause 5
    scene lorisex0 with vpunch
    l "[mc]..."
    window hide
    pause 1
    mc "...Are you ready?"
    l "R-Readier than ever."
    scene lorisex2 with vpunch
    l "AH!"
    "Lori shivers."
    window hide
    scene lorisex1 with vpunch
    l "...Do it again."
    scene lorisex2 with vpunch
    l "Ah~!"
    mc "You like it?"
    l "Fuck, yes I do."
    mc "Then I'll keep going."
    scene lorisex1 with vpunch
    pause 1
    scene lorisex2 with vpunch
    l "Fuck~!"
    window hide
    pause 1
    scene lorisex1 with hpunch
    mc "Hah..."
    window hide
    pause 1
    scene lorisex2 with vpunch
    l "Mh~"
    pause 1
    scene lorisex1 with hpunch
    pause 1
    scene lorisex2 with vpunch
    mc "{i}She's so fucking tight!"
    pause 1
    scene lorisex1 with hpunch
    l "G-Go faster~!"
    mc "Well, if you ask me like that..."
    window hide
    pause 0.5
    scene lorisex2 with vpunch
    pause 0.5
    scene lorisex1 with vpunch
    pause 0.5
    scene lorisex2 with vpunch
    l "Y-Yes~!"
    pause 0.5
    scene lorisex1 with vpunch
    pause 0.5
    scene lorisex2 with vpunch
    pause 0.5
    scene lorisex1 with vpunch
    pause 0.5
    scene lorisex2 with vpunch
    pause 0.5
    l "FUCK!"
    scene lorisex1 with vpunch
    pause 0.5
    scene lorisex2 with vpunch
    pause 0.5
    mc "Lori..."
    scene lorisex1 with vpunch
    l "[mc]~!"
    scene lorisex2 with vpunch
    pause 0.3
    scene lorisex1 with vpunch
    l "It feels so good...!"
    pause 0.3
    scene lorisex2 with vpunch
    l "D-Don't stop!"
    pause 0.3
    scene lorisex1 with vpunch
    pause 0.3
    scene lorisex2 with vpunch
    pause 0.3
    scene lorisex1 with vpunch
    pause 0.3
    scene lorisex2 with vpunch
    pause 0.3
    scene lorisex1 with vpunch
    mc "{i}Oh, fuck, I'm..."
    scene lorisex2 with vpunch
    l "I-I'm gonna...!"
    scene lorisex1 with vpunch
    pause 0.1
    scene lorisex2 with vpunch
    pause 0.1
    scene lorisex4 with vpunch
    l "...cum!"
    scene lorisex4 with flash
    pause 0.3
    scene lorisex4 with flash
    pause 0.2
    scene lorisex4 with flash
    scene lorisex4 with flash
    scene lorisexcum with Fade(0,1.5,5)
    pause 3
    mc "...Fuck."
    l "Yes you did...{p}...Fuck me, I mean."
    mc "..."
    l "...And you also came inside."
    mc "I'm... sorry."
    l "Heheh... It's fine~"
    scene library
    show black:
        alpha 0.35
    with fade
    "Suddenly, you hear the door of the library squeaking. Someone opened it."
    l "{size=-3}Fuck!"
    "Lori grabs your hand."
    "Then the two of you quickly scrambled to run away into her bedroom."
    play music "after-effects.mp3" fadein 1.5
    scene loribedroom with fade
    l "...We're safe."
    mc "Phew."
    l "..."
    mc "..."
    l "I-I'll dress up."
    mc "O-Oh. Yeah, I'll just... turn around."
    scene black with dissolve
    l "...You need to turn around after what we just did?"
    mc "Shut up."
    l "Heheh..."
    pause 1
    scene loribedroom
    show black:
        alpha 0.4
    show prot smile
    show smilel
    with fade
    l "..."
    mc "..."
    l "So, uhm...{p}...That was something."
    mc "It, uh, definitely was."
    l "Was it... something good?"
    mc "Absolutely."
    hide smilel
    show blushl
    l "..."
    l "[mc]... I think I love you."
    mc "I... think the same thing."
    mc "...Even though we haven't known each other for that long I... I really like you."
    mc "You're a great teacher, you know how to make lessons fun..."
    mc "You're smart and passionate about the things you like...{p}...You're also a goof who messes up her declaration."
    l "...Shut."
    mc "You're just so precious. Even the most boring of quests can become fun with you. The wonder in your eyes for the world is so charming, just like the way you smile."
    mc "I love all of that. I love you."
    l "..."
    l "You can't just say all of that, it's unfair."
    mc "It's not unfair, it's just true."
    l "..."
    l "...I like your voice. I like the way you smile and I like how focused you look when I talk to you. It makes me feel appreciated."
    l "and I love how much you give yourself to others — to me. You don't know how happy I was when you offered to take me on a quest with you. Nobody had ever done something like that before."
    hide blushl
    show smilel
    l "...I love you, [mc]. I'm sure of it."
    mc "Yeah... I'm sure of it too."
    #scene lorisecondkiss
    scene loribedroom with dissolve
    "Lori hugs you. She feels so small."
    l "Thank you for being my friend... and something more."
    mc "You're more than welcome."
    "The two of you stay like that for some time, enjoying the other's embrace."
    window hide
    pause 1
    scene black
    show text "{color=#fff}3 hours later." at truecenter
    with fade
    pause 3
    hide text with dissolve
    scene library
    show smilel
    show prot smile
    with dissolve
    mc "Well, I'll head back home now."
    l "Alright. See you soon."
    mc "See you, Lori."
    "You leave the Library and make your way back home."
    scene villageback with fade
    mc "{i}That... definitely didn't go like I expected it to."
    $ time += 1
    $ persistent.loriFirstTime = True
    $ loriEventValue = 11
    $ loriFunValue = 0
    $ loriDone = True
    jump home
