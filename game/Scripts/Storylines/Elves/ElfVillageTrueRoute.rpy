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
    "You slowly start heading inside."
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
    zn "WAKE UP ALREADY!"
    "{i}Whip!"
    "Unknown voice" "...SEX? ...SEX? ...SEEEEEXX?"
    mc "{i}What the fuck is going on down there?"
    mc "{i}I should try to get in there."
    menu:
        "Try to open the door":
            "{i}Okay, let's see... Please don't be locked..."
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
            mc "Ugh... calm down, [mc], think straight!"
            mc "I'll have to do this on my own. I'll tell someone once I have enough proof."
            mc "So think, what do I need to do?"
            mc "I need to find a way to get into the Zenelith's house when she's not home."
            mc "And I need to find a way to break that seal. Mh... I think Scarlet could help me out with this. She definitely knows something about seals!"
            if faila == 1:
                mc "Shit! I can't go to the Academy now, I'm expelled. Damn it!"
            mc "There are only [evedueltimer] days before the duel. I've got to do all this before that happens."
            mc "...Let's see if I can do this!"
            $ bothpath += 1
            $ metpriest += 1
            jump elfVillage
    return


label bothpath3:
    if time > 2:
        mc "She's probably in there right now. I should come in the daytime when she's not at home."
        jump elfVillage
    mc "Ok, let's do this."
    "You unlock the door with the master key."
    mc "It worked!"
    stop music
    "You lock the door after you get inside."
    scene priesthouse
    mc "{i}Man. This house is still dark, even in the day!"
    mc "{i}Now to open that door."
    if spellintroscarlet == 1:
        scene doorpriest1 with fade
        mc "{i}All I have to do is hold this rune in my hand, right?"
        "You hold the rune and push firmly onto the door."
        if wrongsealspell == 1:
            scene doorpriest2 with flash
            mc "{i}What?! It didn't work..."
            mc "{i}I think I chose the wrong symbol. Damn it!"
            mc "{i}I should memorize the damn symbol this time."
            hide window
            pause
            mc "{i}Ok, got it. Now I should go back and tell Scarlet."
            "You unlock the door and leave Zenelith's house, after locking it back up."
            $ time += 1
            jump elfVillage

        if rightsealspell == 1:
            mc "{i}It opened!"
            mc "{i}Now, I have to be very careful down here."
            "You slowly climb down the stairs and go into the basement."
            scene priestjail with fade
            play music creepymusic
            mc "{i}Wh-What is this place? It looks like some sort of dungeon..."
            mc "{i}So, this what she was hiding."
            "You take a look around the dungeon. The stone walls block almost every trace of light. Years of neglect over cleanliness emits an odor that catches you off guard as soon as you step in. You can only hear the occasional chains rustling and faintest droplets of water dripping around you. As you venture forward..."
            "You see a figure chained to the wall."
            mc "Oh Astylla!"
            scene slave1 with fade
            mc "H-Hey there...?"
            mc "{i}Is he dead? ...I think this the person I heard talking that day."
            mc "{i}Wait! It's a male elf! What is he doing down here?"
            scene slave2 with vpunch
            "Unknown" "...SEX ...SEX ...SEX!!!!"
            mc "{i}Holy shit! He's not dead!"
            "Unknown" "SEX! SEX! I'm ready for SEX!"
            mc "Shut the fuck up!"
            "Unknown" "I'm awake mistress, please use your toy, please-"
            mc "Shut up! I'm not your mistress- I'm a guy."
            show slave1 with dissolve
            "Unknown" "Haha... mistress trying to fool me, hiding her breasts. Haha, very funny, mistress... Your jokes are very fu-"
            mc "I'm not your fucking mistress, okay? I'm [mc], a human."
            "Unknown" "Hehehe... hehehe..."
            mc "{i}He's out of his mind."
            show slave2 with dissolve
            "Unknown" "Does the human want sex too, then~?"
            mc "Ugh... How long have you been down here?"
            show slave1 with dissolve
            "Unknown" "{size=-5}One, Two, Three, Four, Five, Six, Seven..."
            mc "I'm going to get you out of here, Ok?"
            "Unknown" "Fourteen, Fifteen... Eighteen, Nineteen..."
            mc "I'm going to bring Evelyn down here, okay? And we are going to save you..."
            "Unknown" "Fifty-nine, Sixty, Sixty-one..."
            mc "He isn't listening... maybe I should bring Aerin too."
            "Unknown" "Sixty-nine, Sevent-"
            mc "{i}He stopped!"
            label zendungeon:
            $ gameover = "zendungeon"
            scene slave2 with dissolve
            "Unknown" "Ae...rin...?"
            mc "Huh? ...You know her?"
            "Unknown" "Aerin... AERIN!"
            mc "{i}Wait. It can't be..."
            mc "Are you Aerin's broth-"
            "You hear the front door unlock."
            mc "{i}Oh no! Zenelith's is here!"
            mc "{i}Shit, what do I do now?!"
            menu:
                "Talk to her" if easyMode == False:
                    mc "{i}I should talk to her. We can settle this face to face, once and for all!"
                    scene priestjail with fade
                    "Zenelith opens the basement door and steps down. She sees you, but her usual facial expression doesn't change. She doesn't seem to be shocked or scared, she looks disappointed if anything."
                    show znpriesttalkangry
                    zn "W-What?"
                    show angry
                    mc "It's over, bitch! I found out about your little secret!"
                    zn "H-How did you get down here?! A pathetic human trespassing my property!"
                    mc "It doesn't matter how I got here, or if I'm human or not. What matters is the fact that you're fucked! I know who that is, it's Aerin's brother, isn't it?"
                    zn "..."
                    mc "I'm right, aren't I!"
                    zn "What do you want, little human?"
                    mc "What do I want? Nothing! I'm going to take him out of here and then I'm telling everyone about your dungeon here! And how you kept Aerin's brother prisoner! For who knows how long."
                    zn "...What if we made a deal?"
                    mc "No deals! You deserve to be punished for what you've done!"
                    zn "And I thought you had some smarts to you... Foolish ape."
                    mc "What?"
                    zn "Didn't your tiny human brain ever consider that I would be prepared for this?"
                    mc "Prepared? For what?!"
                    play sound magic
                    "All you see is a bright blue flash and everything goes black."
                    scene black
                    zn "Hahah! You are a stupid, pathetic ape after all... Hahaha..."
                    jump GameOver

                "Hide":
                    mc "{i}I should hide. If she sees me, I'm screwed!"
                    scene priestjail with fade
                    "You quickly take a look around, trying to find a place to hide. You see a bunch of crates stacked together and decide to hide behind them."
                    "Zenelith opens the basement door and comes down."
                    zn "You better be awake, toy!"
                    zn "...Oh, good. You're already awake."
                    mc "{i}Shit! How am I going to get out of here?!"
                    zn "I came a bit sooner today. You should at least thank me, toy!"
                    "Unknown" "Th-Thank you, Mistress."
                    zn "...Hmmm?"
                    zn "You sound different today. Did something happen?"
                    "Unknown" "......"
                    zn "Well, I know how to fix that. Now, where did I put the whip?"
                    mc "{i}What the hell is she doing to him? Is she using him as some kind of sex slave...?"
                    zn "Wait! ...I sense something."
                    mc "{i}Oh shit!"
                    zn "...Something dark! I's here with us!"
                    mc "Shit, shit, shit!"
                    "Zenelith starts to walk toward you."
                    mc "{i}What should I do... Uhh... I have my sword with me. I guess I'll have to fight!"
                    "Zenelith is almost apon you."
                    mc "{i}Huff... Huff... Here we go!"
                    scene priestjail with hpunch
                    "Unknown" "AAAAAAAAHHHHHH!!!!!!"
                    mc "{i}Huh?"
                    zn "What? What is it, toy?!"
                    "Unknown" "AAAAAAAAHHHHHH!!!!!! IT HURTS!!!!!!!"
                    zn "Wh-What's wrong?! Stop your screaming!"
                    "Zenelith runs towards the chained elf. You find the perfect time to escape. You take a deep breath and slowly sneak out of the basement."
                    "Before you leave you catch with the tail of your eye the image of Zenelith looking at Aerin's brother, for some reason she looks actually worried for her slave."
                    scene priesthouse with fade
                    pause 0.5
                    scene elfvillagen with fade
                    mc "{i}Phew I got out... I got out."
                    "You take a few deep breaths."
                    mc "{i}That guy down there... He was..."
                    mc "{i}He was... Aerin's brother!"
                    mc "{i}I mean... it has to be him. I think he distracted her on purpose, so I could get out."
                    mc "{i}What do I do now? Should I tell everyone about this? I still don't have any proof!"
                    mc "{i}Damn it! If I don't have proof, no one will believe me. And judging by that seal, Zenelith must be a powerful mage. She could easily make the basement disappear if I somehow convinced the Village people to inspect the house."
                    mc "{i}I don't think I'll be able to take Aerin's brother out of there, he is chained to the wall, and those chains don't look weak... If only I could show them what happened down there... without Zenelith finding out."
                    mc "{i}......"
                    mc "{i}YES! I got it!"
                    mc "{i}The Eye Orb! I can use the Eye Orb to show the Village people what's going on down there."
                    if ieyeorb < 1:
                        mc "{i}Sander told me I could buy one from the merchant."
                    else:
                        mc "{i}Sander has the Eye Orb, I should get it back from him."
                    if easyMode:
                        mc "{i}But maybe I also need something to protect me from her magic..."
                        mc "{i}...I'll ask Scarlet."
                    mc "Alright [mc], just a little bit more work and I'll manage to do it."
                    $ needOrb = True
                    $ bothpath += 1
                    $ time = 3
                    jump elfVillage
    scene doorpriest1
    menu:
        "Open it":
            scene doorpriest2 with flash
            mc "Shit! I forgot about the seal."
            mc "I need to find a way to break it. I better talk to Scarlet."
            jump elfVillage
    return


label bothpath4:
    if goteyeorb == 0:
        mc "I need to get an Eye Orb!"
        jump elfVillage
    mc "Let's do this!"
    stop music
    scene priesthouse with fade
    mc "I think she's not home yet."
    scene doorpriest1
    "You take a deep breath, then you open the door."
    scene doorpriest3 with dissolve
    mc "{i}Ok, I have to get everything right from this point on."
    scene priestjail
    "You take the Eye Orb into your hands and head down to the basement."
    scene slave1 with fade
    mc "Hey."
    "Unknown" "H-Hey... it's you. You're back!"
    mc "Yes, and I'm getting you out of here."
    "Unknown" "What? H-How? These chains are unbreakable..."
    mc "You'll have to wait a little bit more, I'm going to get the others for help. See this? It's an Eye Orb. I can use it to show the others what's happening down here."
    "Unknown" "Th-That will work... B-But the mistress is strong!"
    mc "She is, but together, we'll be able to take her down."
    "Unknown" "Aerin! Is she... is she still alive?"
    mc "Yes, she's doing fine."
    "Unknown" "Oh, thank the Four Mothers!"
    mc "You're her... brother... right?"
    "Unknown" "Y-Yes, m-my name is M-Morgan."
    mc "What happened to you? The whole Village thinks you're dead!"
    morg "I was... kidnapped... and brought here..."
    mc "By Zenelith."
    morg "Y-Yes."
    mc "Why?"
    morg "I-I don't know... she-"
    scene slave1 with vpunch
    zn "I knew you would be here."
    scene priestjail with fade
    show angry
    show znpriesttalkangry
    mc "You! ...How did you know?!"
    zn "I can feel your presence, that dirty scent you carry... I knew it was you the other day!"
    mc "What are you doing here with him? Why do you have him locked down here?!"
    zn "It doesn't concern you, filthy ape."
    mc "Everyone, even his own sister thinks he's dead and it's all because of you!"
    zn "I-I've done this for the Village's sake! You have no right to accuse me of anything!"
    mc "Bullshit! How does this help the Village?"
    zn "...It wouldn't make a difference even if I told you, because you're already dead!"
    mc "Huh?"
    if protectionspell < 2:
        "Zenelith casts a spell and blasts a blue org towards you."
        scene black
        "You don't have time to react that everything suddenly goes black."
        jump GameOver
    else:
        "Zenelith sends a blue orb flying at you. Suddenly a red sphere encloses around your body and stops the orb."
        zn "Impossible!"
        "With a sudden burst, the orb flies back and hits Zenelith instead. She makes a force field around her but it's too weak, the orb breaks through the barrier and hits her right in the stomach. She falls to the ground, all her clothes burnt off."
        scene priestjail with vpunch
        zn "AHHH!"
        show angry
        mc "{i}Scarlet's protection magic! It saved my life!"
        zn "That protection magic... H-How can a mere human possess such strong magical power?!"
        mc "How does it feel to kneel before a \"filthy ape\", huh?"
        zn "You will regret this!"
        mc "Come here, bitch, time for you to have a taste of your own medicine."
        "You grab her by the hair and drag her along the ground."
        mc "Whew, fuck! You really are a fucking heavy, fat cow."
        zn "Let go of me ape...! You're... I-It hurts!"
        mc "Oh, like the way you hurt Morgan? Serves you right!"
        "You find some chains hanging from the ceiling. You hoist her up and grab her weak hands. You chain the hands up together, restraining her wrists together, and created a link up to the ceiling. You hang her almost lifeless body hanging from the ceiling."
        scene elfpreistback with fade
        mc "Now, tell me why! Why did you do it?"
        zn "I-It was to protect the Village."
        mc "How?!"
        zn "......"
        mc "What made you do such a horrible thing? You made Aerin suffer! You made her live alone for so long!"
        mc "{i}What's up with me? I feel like I'm about to catch on fire. This feeling of rage! It's so strong!"
        mc "Tell me, or I'll rip that pretty face right off!"
        zn "...He was the last male survivor! He had to live, in order for the Village to survive..."
        mc "So you locked him in a dungeon?"
        zn "H-He told me that he was going to Hern, to defend the wall. I couldn't let that happen! He would face the same fate as the other men. I begged him to stay, but he wouldn't listen to me. He said he was doing it for his sister, to keep her safe."
        zn "I begged and begged but he wouldn't listen. So, I had no other choice but to lock him up. It was for his own good..."
        mc "Hah. You're lying, you slut!"
        zn "Wh-What?!"
        if millyInfo == True:
            mc "He was the only one who decided to stay here! He would never leave his sister!"
            mc "You think all of us humans are inepts don't you?"
        else:
            mc "You can't fool me. I am not a stupid ape."
        if nessaInfo == True:
            mc "I'm sorry your brothers died because their comrades were cowards, but if you keep underestimating me, you'll end up badly!"
        elif millyInfo == True:
            mc "I'm sorry your brothers died because their comrades were cowards, but if you keep underestimating me, you'll end up badly!"
        zn "Y-You're just screaming out nonsense."
        mc "No! You know what I think? I think that YOU wanted him all for yourself!"
        zn "What?!"
        menu:
            "You're just a crazy slut!":
                $ trueZenReason = False
                mc "You are making all of that up! You're just a crazy slut! You kidnapped him just to have a toy to have fun with! You think I don't know that?!"
                zn "Th-That's not-!"
                mc "Admit it, you're just a horny old elf whore who can't live without dick!"
                zn "N-No! I did it for the Village!"
                mc "...Still lying, huh?!"
            "You wanted him all for yourself!":
                $ trueZenReason = False
                mc "Yeah! You were so worried that you wouldn't be able to have him, you thought someone might take him from you. So you kidnapped him, locked him up. Just so you would be able to use him as much as you wanted."
                zn "Th-That's not-!"
                mc "Admit it, you're just an egoisticalold elf whore who only cares about herself and her needs!"
                zn "N-No! I-I did it for the Village!"
                mc "...Still lying, huh?!"
            "You hoped he'd give you child!" if childlessZen == True:
                $ trueZenReason = True
                mc "You couldn't give birth when it was your time so you decided to use him now instead, didn't you?! You kidnapped him and chained him up so you could get his seed and get pregnant!"
                zn "Wh-What?!"
                mc "Oh, don't think I don't know. You were the only one from your generation who didn't become a mother. Everyone left you alone because you couldn't even help keep the Village alive!"
                zn "Sh-Shut up!"
                mc "But it failed, didn't it? Could it be you are... infertile?"
                zn "Y-You shout your f-filthy mouth right now!"
                mc "Hah! Or what?!"
                zn "..."
                mc "An infertile elf, the worst kind of elf, am I right?"
                zn "..."
                mc "Tsk. Disgusting... Your frustration is no excuse for something like this! You've hurt everyone in the Village! You've hurt him! You've hurt Aerin!"
                mc "..."
        $ sawpriest += 1
        menu:
            "Leave her":
                mc "I don't care. Soon, the whole Village is going to find out about what you did..."
                mc "{i}I'll leave her here and get the others."
            "Teach her a lesson":
                $ RapeZen = True
                $ persistent.rapeZenelith = True
                mc "I guess it's time to teach you a lesson."
                zn "Wh-What?"
                mc "Oh, don't worry, seeing what you've been doing the past century and a half, you will enjoy this punishment."
                zn "N-No... Y-You won't d-dare to-"
                "You pull down your pants and quickly grab her ass with your hands"
                scene priestr movie
                mc "{i}Wow..."
                mc "{i}For someone who's been having sex for 150 years she sure is tight!"
                zn "P-Please stop!"
                mc "Why? You aren't enjoying this?"
                zn "Ahn-! I-I'm n-naahhh~"
                mc "Hah, you're enjoying this so much you can't even talk back properly! Now that's satisfying!"
                "You continue to fuck her for ten minutes, her complains disappeared pretty early on, replaced only by moans."
                "Then, finally, you cum inside of her."
                show priestsexcum1 with flash
                mc "Ahh..."
                scene elfpriestbackc with fade
                mc "Now, that felt great, didn't it?"
                zn "{size=-5}Y-Yes..."
                mc "What did you say?"
                zn "N-No! Y-Your member d-didn't feel good a-at all!"
                mc "Pfft, sure thing."
                mc "Now I'll go give everyone the news. \"Morgan's alive and Zenelith is evil!\""
        "As you leave, you find a key on the floor."
        mc "{i}This must have fallen when she got hit by that orb."
        "You take it and unlock Morgan's chains. He's unconscious. You lift him unto your shoulders and carry him out of the basement. As soon as you step outside, you're met by two familiar faces, Eve, and Nessa!"
        scene priesthouse
        mc "Eve, Nessa, what are you doing here?!"
        e "I should ask you the same thing, little one."
        n "...Who's that guy?"
        mc "It's Morgan."
        "{color=#B6E268}Eve and {color=#8DE549}Nessa" "MORGAN?!"
        n "You mean that's Aerin's brother?!"
        mc "Yes!"
        e "H-How?"
        mc "Zenelith! She had him locked up this whole time!"
        e "What?!"
        mc "Yeah! She's been using him as a sex slave for all this time..."
        n "Sex slave?! Oh, poor Morgan! Is he alright?"
        mc "He's fine. He just passed out earlier, he'll be fine."
        e "Where is the priestess?!"
        mc "She's down there in the basement. I caught her."
        e "Let me go look. Nessa, you take Morgan to Aerin."
        n "Eve?"
        e "Hmm?"
        n "You do it."
        e "What?"
        mc "Yeah Eve, I think it's better if you do it."
        e "What difference does it make?"
        mc "Trust me, Eve."
        e "Fine! But go teach Zenelith the same lesson I'd teach her."
        if RapeZen == True:
            mc "Mhh... The lesson I taught her probably isn't the same one she'd teach her..."
        n "Come on now, go give that girl her brother back... and also her friend."
        e "Be careful you two."
        n "No problem, I'm captain of the Village guard. This is what I do!"
        "Eve carries Morgan out of the house."
        n "Now, let's go take a look at that whore."
        mc "Right behind you."
        scene priestjail with fade
        "You go down the basement with Nessa. But to your surprise, Zenelith has escaped!"
        scene elfpreistback2
        mc "What?! She's gone? But how? She was right here!"
        n "She must've escaped. I need to tighten the guard. [mc], you better head home for now. It's not safe for you to be out here anymore."
        mc "O-Ok."
        scene elfvillagen with fade
        mc "{i}How did she escape?! I had her!"
        mc "......"
        mc "{i}But I managed to save Morgan, that's more important."
        mc "{i}I'm so tired, I better head home and come back tomorrow."
        mc "{i} Huh, I guess I didn't have to use this Eye Orb after all."
        "You head back to Randel, you feel happy, but maybe too happy. You contemplate on if what you did to Zenelith was right or not, but you feel that what she did cannot go unpunished... at least that's what you hoped."
        $ persistent.zenelithDefeated = True
        scene homenight
        $ bothpath += 3
        $ eveduel -= 1
        $ time = 4
        jump home
    return


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
    e "Aerin's being made the Elder, the ceremony is being held as we speak."
    mc "Really? So, they decided to make Aerin the Elder."
    e "I refused to become the Elder, so they gave her the job."
    mc "That's great news! But I have a question. Last night, did you guys talk?"
    show talkwae
    e "We did, after Aerin stopped crying. She cried for almost another hour after she saw her brother... I had to listen to her weeping before I could talk to her."
    mc "Hehehehe, she must've been pretty shocked."
    e "She certainly was."
    mc "So what exactly did you guys talk about?"
    show sadhtalke
    e "We talked a lot, actually. She said she was sorry for the way she acted and that she has now changed. It was a pleasant surprise."
    mc "That's great! So... The two of you are friends now?"
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
    n "It was a good thing you came to our Village, [mc]. Now, since everything is ready, all that is left is to surprise Aerin, right?"
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
    morg "Never been better! I never thought I'll be able to sleep in a bed like this again. My body is still weak, the Village doctor said I should at least rest for two years."
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
            morg "She didn't seem to enjoy it much either, she was always so frustrated, as if there was something wrong with me... maybe with her. When she was especially angry... She would whip me."
            morg "While I was in there, I slowly started to lose track of time. After a certain point, I didn't even feel like I existed anymore..."
            morg "But that night, when I heard Aerin's name, I regained myself. It was like waking up from a deep sleep."
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
    scene aerinhouseparty
    play music happy
    "When you go out of the room, you see the house is filled with elves getting ready for the party."
    "{i}I don't think I've ever seen that many Elves gathered in one place like this. It almost reminds me being in the Guild back home. The air's filled to the brim with energy. I know Nessa said she and the others didn't do anything too fancy, but nonetheless, the place looks great."
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
    "{i}I know that this isn't really Aerin's style, but she's adapting quickly and looks dangerously close to having fun."
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
    mc "I see that, but why? You know you aren't banished anymore, right?"
    sa "I know... b-b-but these women. They're animals! Last night I came to meet Eve, these things suddenly jumped out from the darkness and they... They just didn't stop! {i}sob..."
    mc "......"
    sa "I barely got out alive. So, this time, I came prepared."
    mc "Where did you even get those clothes from?"
    sa "I found them."
    mc "\"Found them\" or stole them, on one of your peeping missions?"
    sa "A good adventure sometimes has to skip the little details. Hey, but tell me. How the hell are you still walking on two legs?"
    mc "What do you mean?"
    sa "These women, didn't they...?"
    mc "Oh, Nessa covered for me. She told everyone in the Village that... I have a sexually transmittable disease."
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
    mc "{i}Heh, they really know each other well."
    show happya
    a "[mc]!"
    show talksadhappymc
    mc "Aerin, finally got the time to talk to me, huh?"
    a "You... you..."
    "Aerin hugs you."
    show blushtalka
    a "Thank you so much [mc], I don't know how I could-"
    mc "Awww, you're just like your brother! It's over, I'm glad I could help. Now just enjoy the party."
    a "{i}Sniff...{/i} Ok."
    mc "Come on, then!"
    a "Ok- Oh, wait. Please give me a moment."
    scene aerinbroyell1
    pause 0.5
    scene aerinbroyell2 with vpunch
    pause 0.5
    a "Keep your hands off him! He's still supposed to be resting!"
    scene aerinbroyell3
    mc "{i}She's already getting into the Elder role, I see."
    scene partyaerin with flash
    "Everyone starts to dance and have a good time."
    pause
    "{i}I guess I'm not that used to parties either, but I'd be lying if I didn't say I was having a ball. The room is warm with the heat of people dancing like lunatics. It seems like after a few drinks, no one here cares about how they look. It really is a sight to behold."
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
    mc "{i}Even with everyone leaving, no one seems sad about it. In fact, they all seem happy. It's a pretty safe bet, even one Sander would win, that the night isn't ending for some of them."
    mc "{i}I guess it goes to show even if you live for hundreds of years, everyone likes to cut loose and have fun at times."
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
    mc "Wow, this place is great."
    play music nurture
    a "It's relaxing, isn't it?"
    mc "It sure is."
    a "......"
    mc "......"
    mc "So how's it feel to be the Elder?"
    a "I-I don't know, it's great, I guess."
    mc "You guess?! You've wanted this your whole life!"
    scene mcatalks
    a "Yeah, but so many things have happened. It almost feels too good to be true."
    a "I became the Elder, I got my brother back. I got my friends and Village people back, and..."
    scene mcatalkh
    a "I met you."
    mc "......"
    mc "{i}How do I respond to that? Come on, think of some cheesy line..."
    mc "I'm glad that I met you too."
    scene mcak3
    a "{i}Blush"
    mc "{i}Nailed it!"
    a "I know you don't like being thanked a lot, but I have to say it. Thank you [mc], you've given me everything. I don't know how I'm supposed to repay you."
    mc "Just be happy, don't be sad anymore. That's all I want."
    a "[mc], I'm getting this weird feeling. Something I haven't felt before"
    mc "......"
    a "I think... I...{p}I think I love you."
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
