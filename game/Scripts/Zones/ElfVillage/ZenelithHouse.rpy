default needOrb = False

label zenelithHouse:
    $ gameover = "zenelithHouse"
    hide screen hud
    if bothpath == 1:
        mc "It's locked! I guess no one's there."
        jump elfvillage

    if bothpath == 2:
        mc "It's locked. How do I get in?"
        mc "There has to be a key... But how do I find it? And there's no way Zenelith is giving it to me."
        mc "If only there was away I could get in without that key. I could break down the door, but that would cause a whole lot of other problems."
        mc "This is related to the village security. I should talk to Nessa, she has to know a way."
        jump elfvillage
    if bothpath == 3:
        if time > 2:
            mc "She's probably in there right now. I should come in the daytime when she's not at home."
            jump elfvillage
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
                jump elfvillage

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
                mc "Oh my god!"
                scene slave1 with fade
                mc "H-Hey there...?"
                mc "{i}Is he dead? ...I think this the person I heard talking that day."
                mc "{i}Wait! It's a male elf! What is he doing down here?"
                scene slave2 with vpunch
                "Unknown" "...SEX ...SEX ...SEX!!!!"
                mc "{i}Holy shit! He's not dead!"
                "Unknown" "SEX! SEX! I'm ready for SEX!"
                mc "Shut the fuck up!"
                "Unknown" "I'm awake mistress, please use your toy, ple-"
                mc "Shut up! I'm not your mistress- I'm a guy."
                show slave1 with dissolve
                "Unknown" "Hehehe... mistress trying to fool me, hiding her breasts. Hehehehe, very funny, mistress, your joke are very fu-"
                mc "I'm not your fucking mistress, okay? I'm a guy, just like you."
                "Unknown" "Hehehe... hehehe..."
                mc "{i}He's out of his mind."
                show slave2 with dissolve
                "Unknown" "Does the guy want sex too, then? Heheheheh!"
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

                    "Talk to her":
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
                        "You quickly take a look around, trying to find a place to hide. You see a bunch of crates stacked together, You quickly run and hide behind them."
                        "Zenelith opens the basement door and comes down."
                        zn "You better be awake, toy!"
                        zn "...Oh, good. You're already awake."
                        mc "{i}Shit! How am I going to get out of here?!"
                        zn "I came a bit sooner today. You should at least thank me, toy!"
                        "Unknown" "Th-Thank you Mistress."
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
                        mc "{i}Damn it! If I don't have proof, no one will believe me. And judging by that seal, Zenelith must be a powerful mage. She could easily make the basement disappear if I somehow convinced the village people to inspect the house."
                        mc "{i}I don't think I'll be able to take Aerin's brother out of there, he is chained to the wall, and those chains don't look weak... If only I could show them what happened down there... without Zenelith finding out."
                        mc "{i}......"
                        mc "{i}YES! I got it!"
                        mc "{i}The Eye Orb! I can use the Eye Orb to show the village people what's going on down there."
                        if ieyeorb < 1:
                            mc "{i}Sander told me I could buy one from the merchant."
                        else:
                            mc "{i}Sander has the Eye Orb, I should get it back from him."
                        mc "Alright [mc], just a little bit more work and I'll manage to do it."
                        $ needOrb = True
                        $ bothpath += 1
                        $ time = 3
                        jump elfvillage
        scene doorpriest1
        menu:
            "Open it":
                scene doorpriest2 with flash
                mc "Shit! I forgot about the seal."
                mc "I need to find away to break it. I better talk to Scarlet."
                jump elfvillage
    if bothpath >= 4:
        if goteyeorb == 0:
            mc "I need to get an Eye Orb!"
            jump elfvillage
        mc "Let's do this!"
        stop music
        scene priesthouse with fade
        mc "I think she's not home yet."
        scene doorpriest1
        menu:
            "Open":
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
                mc "What happened to you? The whole village thinks you're dead!"
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
                zn "I-I've done this for the village's sake! You have no right to accuse me of anything!"
                mc "Bullshit! How does this help the village?"
                zn "...It wouldn't make a difference even if I told you, because you're already dead!"
                mc "Huh?"
                if protectionspell == 2:
                    "Zenelith sends a blue orb flying at you. Suddenly a red sphere encloses around your body and stops the orb."
                    zn "Impossible!"
                    "With a sudden burst the orb flies back and hits Zenelith instead. She makes a force field around her but it's too weak, the orb breaks through the barrier and hits her right in the stomach. She falls to the ground, all her clothes burnt off."
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
                    zn "I-It was to protect the village."
                    mc "How?!"
                    zn "......"
                    mc "What made you do such a horrible thing? You made Aerin suffer! You made her live alone for so long!"
                    mc "{i}What's up with me? I feel like I'm about to catch on fire. This feeling of rage! It's so strong!"
                    mc "Tell me, or I'll rip that pretty face right off!"
                    zn "...He was the last male survivor! He had to live, in order for the village to survive..."
                    mc "So you locked him in a dungeon?"
                    zn "H-He told me that he was going to Hern, to defend the wall. I couldn't let that happen! He would face the same fate as the other men. I begged him to stay, but he wouldn't listen to me. He said he was doing it for his sister, to keep her safe."
                    zn "I begged and begged but he wouldn't listen. So I had no other choice but to lock him up. It was for his own good..."
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
                            zn "N-No! I did it for the village!"
                            mc "...Still lying, huh?!"
                        "You wanted him all for yourself!":
                            $ trueZenReason = False
                            mc "Yeah! You were so worried that you wouldn't be able to have him, you thought someone might take him from you. So you kidnapped him, locked him up. Just so you would be able to use him as much as you wanted."
                            zn "Th-That's not-!"
                            mc "Admit it, you're just an egoisticalold elf whore who only cares about herself and her needs!"
                            zn "N-No! I-I did it for the village!"
                            mc "...Still lying, huh?!"
                        "You hoped he'd give you child!" if childlessZen == True:
                            $ trueZenReason = True
                            mc "You couldn't give birth when it was your time so you decided to use him now instead, didn't you?! You kidnapped him and chained him up so you could get his seed and get pregnant!"
                            zn "Wh-What?!"
                            mc "Oh, Don't think I don't know. You were the only one from your generation who didn't become a mother. Everyone left you alone because you couldn't even help keep the village alive!"
                            zn "Sh-Shut up!"
                            mc "But it failed, didn't it? Could it be you are... infertile?"
                            zn "Y-You shout your f-filthy mouth right now!"
                            mc "Hah! Or what?!"
                            zn "..."
                            mc "An infertile elf, the worst kind of elf, am I right?"
                            zn "..."
                            mc "Tsk. Disgusting... Your frustration is no excuse for something like this! You've hurt everyone in the village! You've hurt him! You've hurt Aerin!"
                            mc "..."
                    $ sawpriest += 1
                    menu:
                        "Leave her":
                            mc "I don't care. Soon, the whole village is going to find out about what you did..."
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
                            "The finally you cum inside of her"
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
                    n "No problem, I'm captain of the village guard. This is what I do!"
                    "Eve carries Morgan out of the house."
                    n "Now, let's go take a look that whore."
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
                "All you see is a bright blue flash and everything goes black."
                scene black
        jump GameOver
