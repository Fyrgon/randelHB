default triedSavingThea = False
default livingWithThea = False
default gabesClothes = False
default gabeKnowThea = False

label impquest:
    scene ambush1 with fade
    play music forest
    "You follow the path shown on the map."
    "As you travel, watching trees pass by starts to get boring."
    mc "Ugh... So boring..."
    "You take a look in the bag and take out a crystal."
    mc "This thing looks really pretty. I wonder if it really works though?"
    "You walk along, observing the crystal. You see a figure coming your way reflected in its glass-like surface."
    scene linus with dissolve
    "{color=#fff}Merchant" "Hello there, young traveler! My name is Linus, I'm a travelling merchant by trade!"
    mc "Hello?"
    "{color=#fff}Linus" "I see you've got a Black Tourmaline Crystal there."
    mc "Yeah?"
    "{color=#fff}Linus" "Are you willing to trade?"
    mc "You mean the crystal?"
    "{color=#fff}Linus" "Of course, what else? Hahaha!"
    mc "Uhm..."
    "{color=#fff}Linus" "I can give you 50 silver for that."
    mc "{i}50 silver for one? ...Well, I have about a dozen of em'. So if I sell all of them, I could get..."
    mc "600 silver!"
    "{color=#fff}Linus" "Huh? ...No... I respect your bartering skills young sir but 50 silver is the best I can do for one!"
    mc "{i}Shit, I said that aloud!"
    "{color=#fff}Linus" "What do you say?"
    mc "{i}I could sell them... but then what about the peopel of Yorkel? They need this..."
    mc "{i}I could just sell one... it won't make much of a diffrence."
    mc "{i}But 600 silver is a lot..."
    mc "{i}What should I do...?"
    show text "{fi}{size=+2}{color=#000}{b}Actions have consequences...{/fi}" with dissolve
    menu:
        "Don't sell them":
            hide text with dissolve
            mc "I'm sorry. I'm actually on a quest. I have to deliver these to Yorkel."
            "{color=#fff}Linus" "Yorkel... For the imps, eh?"
            mc "Yeah."
            "{color=#fff}Linus" "That's fine then! You're a rather noble person. Nice to see people like you in these dark times."
            mc "Thank you."
            "{color=#fff}Linus" "I'll be on my way then!"
            mc "Safe travels."
            "{color=#fff}Linus" "To you too, my boy... may we meet again!"
        "Sell one crystal":
            hide text with dissolve
            mc "Ok..."
            "You give Linus the crystal you were holding."
            play sound chime
            $ renpy.notify("{color=#fff}You gained 50 silver.")
            $ money += 50
            "{color=#fff}Linus" "Pleasure doing business, lad."
            "{color=#fff}Linus" "I'll be on my way then."
            mc "Safe travels."
            "{color=#fff}Linus" "To you too, boy... may we meet again."
            mc "{i}It's just one crystal... They'll be fine."
        "Sell all the crystals":
            hide text with dissolve
            mc "{i}600 silver is too much to pass up... how could I refuse?"
            mc "{i}I'll sell these things and head to Yorkel... I'll make up some excuse when I get there."
            mc "{i}I'll tell I was attacked by bandits or something... Yeah, they'll believe me."
            mc "It's your lucky day, pops... I've got a bag full of these things."
            "{color=#fff}Linus" "What?"
            "You open the bag and show him the crystals. He looks at it and you see his eyes sparkle."
            "{color=#fff}Linus" "How many have you got there?"
            mc "A dozen."
            "{color=#fff}Linus" "Oh, really?! How did you manage to come to possess this bag of crystals if I may ask?"
            mc "......"
            mc "...You don't need to know that..."
            mc "Do you want the crystals or what?"
            "{color=#fff}Linus" "...I was just asking. It's ok if you're not comfortable telling me. You may have your reasons. It's hard living these days. I know that more than anyone."
            "{color=#fff}Linus" "I'll take em'."
            "You give the bag full of crystals to Linus."
            play sound chime
            $ renpy.notify("{color=#fff}You gained 600 silver.")
            $ money += 600
            $ soldcrystal += 1
            "{color=#fff}Linus" "Pleasure doing business!"
            "{color=#fff}Linus" "I'll be on my way then."
            mc "Safe travels."
            "{color=#fff}Linus" "To you too, boy... may we meet again!"
            mc "{i}Man... look at all this silver..."
            mc "{i}Those guys at Yorkel will be alright... They'll figure something out."
    scene ambush1 with fade
    "You continue your journey."
    mc "Almost there."
    "As you get closer, you see a cloud of smoke rising up from the direction of the village."
    mc "Oh no!"
    "You run to the direction of the village."
    scene yorkel with flash
    play music campfire
    "As you finally arrive, you see the village. All the houses are burning. Red embers rise above the town and fall into the surrounding forest as ash. You find the whole scene hard to look at."
    mc "Oh god... what happened here?!"
    "You suddenly hear a scream."
    mc "{i}Who was that... sounded like a girl nearby..."
    window hide
    "You rush out to investigate."
    label thearape:
    $ gameover = "thearape"
    scene thearape1 with fade
    pause
    "{color=#FF893A}Girl" "No, no, no... please!"
    mc "Shit! ...Those are Imps..."
    mc "What are they gonna do to to her?"
    "{color=#FF893A}Girl" "Please, don't do anything! I beg you!"
    mc "This doesn't look good..."
    label savingTheaMaybe:
    menu:
        "Save her" if triedSavingThea == False:
            if soldcrystal == 1:
                mc "There's nothing I can do. Those are extremely powerful monsters, I don't stand a chance against them."
                mc "Fuck! Why did I sell all of those crystals... SHIT!"
                $ triedSavingThea = True
                jump savingTheaMaybe
            mc "I need to save her... But how?"
            menu:
                "Use the crystals":
                    mc "{i}I better use them. These are B ranked monsters, I don't stand a chance against them otherwise."
                    "You take a crystal in one hand and your sword in the other."
                    "You slowly approach the Imps."
                    scene forrest
                    "As you get close, they turn to you with wicked grins on their faces."
                    "You point the crystal at them, not entirely sure if that's how you even use them."
                    "The moment they see the crystal, they screech and start rolling on the ground in pain."
                    "You cautiously walk closer, still pointing the crystal at them."
                    "Their screams start to intensify. They quickly fly away."
                    mc "{i}It worked!"
                    "You quickly run towards the girl."
                    $ thealive += 1
                    mc "She's unconscious... probably from shock."
                    "You pick her up and swing her onto your back."
                    mc "Thank god, she's not heavy, or I'd be dragging her out of here."
                    "I guess I'll have to leave these crystals, I can't carry them both."
                    "You carry her back to Randel. You feel her gently breathing as ash lazily falls around you, making the forest look ghostly. After the chaos of Yorkel, it's strangely serene."
                    stop music
                    scene homeday with fade
                    "You go into your house and put her on your bed."
                    show normalmc
                    mc "She's still out."
                    mc "I need to go back to the Guild to tell July everything that happened..."
                    mc "I probably shouldn't tell her about the girl though... things are already complicated."
                    "You head to the Guild and tell July about almost everything that happened."
                    scene adventurersguild_evening with fade
                    pause 2
                    scene adgc6
                    j "So you're telling me that... that Yorkel is... completely destroyed?"
                    mc "Yeah..."
                    j "Oh my goodness... we were too late..."
                    mc "You didn't tell me the Imp problem was that serious!"
                    j "I didn't know. They sent the request five days ago. They said in the missive that they had things under control, then..."
                    mc "Then what the hell happened?"
                    j "I don't know."
                    j "I'll send a message to Hern to see if they can send a few soldiers to look into this."
                    mc "Would they even care? Yorkel was a small village."
                    j "I know that but it's their duty to care."
                    j "Everything is so chaotic these days..."
                    j "You can go now, [mc]... Oh but what happened to the crystals?"
                    mc "Oh, I lost them when those Imps tried to attack me."
                    j "That's a shame..."
                    j "Anyway, here's your reward."
                    play sound chime
                    $ renpy.notify("{color=#fff}You gained 40 silver.")
                    $ money += 40
                    $ exp += 100
                    call levellingUp from _call_levellingUp_8
                    mc "Thanks."
                    j "Those poor souls..."
                    j "Such a shame..."
                    mc "I know."
                    j "You be on your way then. You must be very tired."
                    mc "Yeah... Goodnight, July."
                    j "Goodnight, [mc]."
                    stop music
                    scene homenight
                    show normalmc
                    play music night
                    mc "{i}What a day..."
                    show worriedmc
                    mc "{i}I'm so tired."
                    if thealive == 1:
                        mc "{i}Where the hell am I supposed to sleep?"
                        mc "{i}I think I had a spare mattress... and I can let her use Uncle Pete's old room."
                        "When you get home, you take out the spare mattress and dust out Uncle Pete's old room. It doesn't take long since Pete did not leave much behind after he moved out."
                        "With the mattress, it's a fairly barren room but still kind of nice. You find yourself hoping that she will like it."
                        mc "All done, I suppose."
                        mc "She doesn't look like she will be waking up anytime soon... I hope she's ok..."
                        mc "{i}Her clothes are pretty torn up. She must be cold."
                        hide worriedmc
                        hide normalmc
                        "You gently put your leather coat over her."
                        mc "That's better."
                        "You carry her to Uncle Pete's room and place her on the mattress."
                        scene sleeptheabase
                        show blancketth
                        mc "She must have gone through a lot. I feel sorry for her..."
                        mc "At least she's safe now."
                        mc "I better go to bed too, I'm on the verge of passing out."
                        show sleep with fade
                        show text "{color=#fff}End of day [day]." at truecenter
                        with dissolve
                        call sleepvars from _call_sleepvars_5
                        pause
                        scene homeday
                        show animation2
                        play music home
                        mc "Huh... it's morning already? It feels like I barely slept."
                        show suprised
                        "{color=#FF893A}Girl" "Hello? Is anybody there?"
                        mc "That must be the girl."
                        mc "I better get her something to eat."
                        "You quickly prepare some breakfast and head to Uncle Pete's room."
                        scene theabed2 with fade
                        "{color=#FF893A}Girl" "Who are you?! Where am I?!"
                        mc "My name is [mc] and you're in my house. Your village was attacked by Imps, remember?"
                        "{color=#FF893A}Girl" "......"
                        "{color=#FF893A}Girl" "No, no, no... this can't be real!"
                        mc "Do you know what happened?"
                        "{color=#FF893A}Girl" "{i}Sob{/i} I don't know... those imps started attacking out of nowhere and- and there was this demon woman! Sh-She torched the entire village!"
                        mc "{i}A demon? On this side of the walls...? That can't be..."
                        "{color=#FF893A}Girl" "My-My house... my Mom... Dad.."
                        mc "{i}Agh! Who cares about that! [mc], look at the state she's in!"
                        menu:
                            "Tell her to calm down":
                                mc "Calm down... calm down."
                                "{color=#FF893A}Girl" "{i}Sob"
                            "Let her go on":
                                "{color=#FF893A}Girl" "An-And Joey! He was so little, he couldn't... couldn't get out in time..."
                                "{color=#FF893A}Girl" "{i}Sob"
                        "{color=#FF893A}Girl" "Were there... others? Who else survived?"
                        mc "......"
                        mc "I'm so sorry... I could only save you... I think that all the others are gone."
                        "{color=#FF893A}Girl" "Oh no... W-Why...?"
                        "{color=#FF893A}Girl" "We were just a small village... why attack us? We never hurt anyone!"
                        "{color=#FF893A}Girl" "You should've just left me there to die! I have no reason to live anymore!"
                        "{color=#FF893A}Girl" "I-I lost everything... everything..."
                        "She curls up into a ball and keeps on crying."
                        mc "{i}I should give her some space until she calms down."
                        mc "You just take your time... I'll leave your food here. If there's anything, you need let me know ok?"
                        $ aquest2 += 1
                        jump home

                "Use your sword":
                    mc "{i}I don't need these things! I bet they don't even work."
                    mc "{i}I got my sword and my wits and that's all I need!"
                    scene forrest
                    "You decide to face them. You draw your sword and approach them slowly."
                    "Once you get close, all three of them turn at you and smile wickedly."
                    mc "Shit."
                    "One imp comes flying at you. You barely have time to react."
                    "The imp slices through your arm. It falls to the ground with a sickening thump."
                    "Pain overwhelms you as you fall to the ground."
                    "You hear the Imps' devilish laughter."
                    mc "{i}Ahhh... my arm...!"
                    mc "{i}I'm going to die... Uncle Pete... I'm so sorry."
                    "Tears fill your eyes."
                    "All three imps come and grab you by the legs. They drag you up to the sky while laughing and hissing."
                    "You see the village below you shrink as you are lifted up to the sky."
                    "Finally, the imps stop. You realize that you're so high up that Yorkel just looks like a red dot below you."
                    "Suddenly, you feel the imps grip on your legs release."
                    "You start falling..."
                    "...and falling..."
                    "...and falling."
                    scene black
                    pause
                    "Sorry, it had to go \"down that way\"...{p}...{p}..."
                    "Get it?"
                    "You should've used the crystals."
                    jump GameOver

        "I can't just watch this happen." if triedSavingThea == True:
            mc "I can't just stand here and do nothing!"
            mc "I don't care if it's dangerous. I have to do something!"
            scene forrest
            "You decide to face them. You draw your sword and approach them slowly."
            "Once you get close, all three of them turn at you and smile wickedly. "
            mc "Shit."
            "One imp comes flying at you. You barely have time to react."
            "The imp slices through your arm. It falls to the ground with a sickening thump."
            "Pain overwhelms you as you fall to the ground."
            "You hear the Imps' devilish laughter."
            mc "{i}Ahhh... my arm...!"
            mc "{i}I'm going to die... Uncle Pete... I'm so sorry."
            "Tears fill your eyes."
            "All three imps come and grab you by the legs. They drag you up to the sky while laughing and hissing."
            "You see the village below you shrink as you are lifted up to the sky."
            "Finally, the imps stop. You realize that you're so high up that Yorkel just looks like a red dot below you."
            "Suddenly, you feel the imps grip on your legs release."
            "You start falling..."
            "...and falling..."
            "...and falling..."
            scene black
            pause
            "Sorry, it had to go \"down that way\"...{p}...{p}..."
            "Get it?"
            "You should've used the crystals."
            jump GameOver

        "Just leave":
            mc "There's nothing I can do. Those are extremely powerful monsters, I dont stand a chance against them."
            mc "Damnit!"
            scene forrest with fade
            "You slowly back away and rush out of the town, leaving the roaring fires and cackling imps behind. You run in the direction of Randel."
            "For a while, ash falls around you like snow, making the forest a ghostly mockery of itself as the white ash clings to the trees."
            "You run until all of that is behind you, then arrive in Randel."
            show homeday
            show normalmc
            mc "I need to go back to the Guild to tell July everything that happened..."
            mc "I probably shouldn't tell her about the girl though... things are already complicated."
            "You head to the Guild and tell July about almost everything that happened."
            scene adventurersguild_evening with fade
            pause
            scene adgc6
            j "So you're telling me that... that Yorkel is... completely destroyed?"
            mc "Yeah..."
            j "Oh my goodness... we were too late..."
            mc "You didn't tell me the Imp problem was that serious!"
            j "I didn't know. They sent the request five days ago. They said in the missive that they had things under control, then..."
            mc "Then what the hell happened?"
            j "I don't know."
            j "I'll send a message to Hern to see if they can send a few soldiers to look into this."
            mc "Would they even care? Yorkel was a small village."
            j "I know that but it's their duty to care."
            j "Everything is so chaotic these days..."
            j "You can go now, [mc]... Oh but what happened to the crystals?"
            mc "Oh! I-I lost them when those imps tried to attack me."
            j "That's a shame..."
            j "Anyway, here's your reward."
            play sound chime
            $ renpy.notify("{color=#fff}You gained 80 silver")
            $ money += 80
            mc "Thanks."
            j "Those poor souls in Yorkel."
            j "Such a shame..."
            mc "I know."
            j "You be on your way then. You must be very tired."
            mc "Yeah, among other things. Goodnight, July."
            j "Goodnight, [mc]."
            scene homenight
            show normalmc
            mc "{i}What a day..."
            show worriedmc
            mc "{i}I'm so tired."
            $ aquest2 += 1
            show sleep with fade
            play sound chime
            $ renpy.notify("{color=#fff}Quest completed: Yorkel's Imp Problem")
            jump home


        "Just watch":
           $ evil += 1
           $ persistent.theaRape = True
           mc "There's nothing I can do. Those are extremely powerful monsters, I dont stand a chance against them."
           mc "I have no choice but to keep low and watch... Maybe I'll get an opening?"
           mc "Shit- They're going to rape her..."
           show animationrapethea
           pause
           mc "{i}...Why am I enjoying this? A-Am I this messed up?"
           pause
           "The imp keeps on pounding the girl"
           pause
           scene thearape4 with vpunch
           pause
           mc "I have to do something now bef-"
           scene thearapekill with hpunch
           "Suddenly one imp slits her throat with its claws."
           mc "O-Oh. They... Killed her."
           mc "I-I..."
           scene forrest with fade
           "You slowly back away and rush out of the town leaving the roaring fires and cackling imps behind. You run in the direction of Randel."
           "For a while ash falls around you like snow, making the forest a ghostly mockery of itself as the white ash clings to the trees."
           "You run until all of that is behind you, then you arrive in Randel."
           show homeday
           show normalmc
           mc "I should go back to the guild and tell July about everything that happened."
           mc "I shouldn't tell her about the girl though... Things are already complicated."
           scene adventurersguild_evening with fade
           pause
           scene adgc6
           j "So you're telling me that... that Yorkel is... completely destroyed?"
           mc "Yeah..."
           j "Oh my goodness... we were too late..."
           mc "You didn't tell me the Imp problem was that serious!"
           j "I didn't know. They sent the request five days ago. They said in the missive that they had things under control, then..."
           mc "Then what the hell happened?"
           j "I don't know."
           j "I'll send a message to Hern to see if they can send a few soldiers to look into this."
           mc "Would they even care? Yorkel was a small village."
           j "I know that but it's their duty to care."
           j "Everything is so chaotic these days..."
           j "You can go now, [mc]... Oh but what happened to the crystals?"
           mc "Oh! I-I lost them when those imps tried to attack me."
           j "That's a shame..."
           j "Anyway, here's your reward."
           play sound chime
           $ renpy.notify("{color=#fff}You gained 40 silver")
           $ money += 40
           $ exp += 100
           call levellingUp from _call_levellingUp_9
           mc "Thanks."
           mc "I guess no cheese then..."
           j "What?"
           mc "Cheese."
           j "Huh... I totally forgot. That doesn't concern me much as those poor souls."
           j "Such a shame."
           mc "I know."
           j "You be on your way then. You must be very tired."
           mc "Yeah... Goodnight, July."
           j "Goodnight [mc]."
           scene homenight
           show normalmc
           mc "{i}what a day..."
           show worriedmc
           mc "{i}Im so tired."
           $ aquest2 += 1
           show sleep with fade
           play sound chime
           $ renpy.notify("{color=#fff}Quest completed: Yorkel's Imp Problem")
           jump home


label theaintr:
    if time == 4:
        mc "She's probably asleep."
        jump home
    if waitthea == 0:
        mc "I should probably give her a little time."
        jump home
    if talkthea1 == False:
        scene theabed2 with fade
        $ persistent.theaBed = True
        mc "Hello, just wanted to check on you."
        "You can see her blush."
        "{color=#FF893A}Girl" "Listen, [mc]... I'm really sorry for what I said before... I didn't mean it."
        "{color=#FF893A}Girl" "You saved me... Thank you."
        mc "You're welcome. And it's ok, it was a pretty reasonable reaction. You've been through a lot."
        scene theabed1 with dissolve
        "{color=#FF893A}Girl" "I didn't introduce myself before. My name is Thea."
        mc "Thea, that's a really nice name. I haven't heard it before."
        th "Yeah, my mom gave it to me... She's from... was from Dermis."
        scene theabed2 with dissolve
        pause
        mc "Oh, I'm sorry I brought that up."
        th "No, it's ok... I'm fine."
        mc "{i}I have to change the subject."
        mc "So, how do you like it here?"
        scene theabed1
        th "It's really nice here and the bed here is super comfy. Thank you."
        mc "I glad you like it. This was my uncle's room."
        th "Really, does that mean he-"
        mc "Oh no... he's living somewhere else now."
        th "I see, haha..."
        th "And, uhm... [mc]..."
        mc "Yeah, tell me."
        th "I-I need some clothes..."
        mc "Oh, y-yeah sure, sure."
        th "It's not that I don't like this jacket you've given me but I need like... actual clothes?"
        mc "Yeah, sure, no problem! I'll find some."
        th "Thank you."
        $ knowThea = True
        $ aquest2 += 1
        $ talkthea1 = True
        $ findtheaclothes += 1
        jump home
    scene theabed1
    th "Did you find some clothes?"
    menu:
        "Yeah" if theaclothes == 1:
            mc "Yeah, I got them."
            th "Really?"
            mc "Yeah, I got them from a friend."
            play sound chime
            $ renpy.notify("{color=#fff}You gave Thea the clothes.")
            th "Thank you... will she be needing them back?"
            mc "No, I don't think so."
            th "Yay! I'll get changed then."
            mc "Ok."
            th "......"
            th "...I said I'll get changed then..."
            mc "Oh yeah, sorry, hehehe..."
            th "Hahaha."
            mc "{i}I'm such a dumbass."
            scene homeday
            "You wait outside for while Thea got changed."
            th "You can come in now, [mc]."
            show smilemc
            show normalth
            show talksadhappymc
            mc "Wow... You look great!"
            show sadsmileth
            pause
            hide talksadhappymc
            show talksth
            th "Thank you, these clothes are a perfect fit."
            th "Please thank your friend from me, will you?"
            show talksadhappymc
            mc "Sure."
            mc "{i}Yeah, right, like that's going to happen."
            mc "Ok then! I'll leave you for now."
            mc "Feel free to look around the house, you can use the kitchen too if you want."
            th "Thank you, [mc]."
            mc "No problem."
            th "I mean, thank you for everything. Saving me and giving me a place to stay. I really appreciate it."
            mc "Like I said, no problem. You can stay as long as you like."
            $ theaintro += 1
            $ thearun += 1
            $ theaclothes -= 1
            $ livingWithThea = True
            $ knowThea = False
            jump home
        "Not yet.":
            mc "No, not yet. Sorry."
            th "It's ok, tell me when you find them."
            jump home
    return


label theagrave:
    hide screen hud
    show worriedmc
    mc "She's not here?"
    show talkmc
    mc "Thea!"
    hide talkmc
    mc "Did she leave? Why? She was just fine..."
    mc "......"
    hide worriedmc
    show thinkmc
    mc "Where could she have gone?"
    mc "What's this?"
    "You find a note left on her bed."
    "\"Sorry, [mc], I took your shovel for a bit. I'll leave it at Yorkel, I won't be coming back. Thank you for everything.\""
    mc "My shovel..."
    mc "Wait no! She went back to Yorkel!"
    "You pack your things and head to Yorkel."
    scene ambush1 with fade
    mc "She has to be here."
    "When you reach the destroyed village."
    mc "{i}The soldiers never came, huh? Why am not surprised?"
    "You see Thea standing with a shovel in her hand."
    mc "Thea!"
    "She notices you."
    scene forrest with fade
    show normalmc
    show sadnth
    show talkwanmc
    mc "What the hell are you doing here?"
    hide talkwanmc
    show cryth
    th "I'm sorry, [mc], I had to come... I can't leave them like this."
    mc "...Why didn't you tell me. I would've helped."
    th "I can't ask that of you. You've already done so much for me."
    show talksadhappymc
    mc "Thea, come on, it's okay. You can't do this alone."
    th "{i}Sob"
    hide talksadhappymc
    show talkwanmc
    mc "Did you... find them?"
    th "...Yeah..."
    mc "Let's give them a proper burial then."
    scene black with fade
    play music sadbunis
    "You dig three graves with your shovel. You bring the three bodies, they're heavily burnt. One body looks like a child..."
    "You and Thea gently lower the bodies into their graves."
    scene theagrave1
    $ persistent.theaGrave = 1
    "Thea keeps on crying."
    menu:
        "Comfort her":
            scene theagrave2
            $ persistent.theaGrave = 2
        "Leave her be":
            mc "{i}I should let her be."

    th "What do I do now, [mc]?"
    th "I have nothing, I have nowhere to go..."
    mc "...You... can live with me, if you want."
    th "What?"
    menu:
        "I can take care of you.":
            mc "I can take care of you."
            th "Oh, [mc]..."
            show screen notice
            pause
            hide screen notice
        "Your life is not over.":
            mc "Your life is not over Thea, you can always start a new one."
            th "Start a new life?"
        "Say nothing":
            mc "......"

    th "No, I can't. I won't be burden on you."
    mc "It's ok, Thea. Really."
    th "......"
    mc "Thea?"
    th "I'll pay you."
    mc "What?"
    th "I'll pay rent."
    mc "What? But how?"
    th "I'll get a job in Randel."
    mc "You don't need to do that."
    th "I can. Just give me a price."
    mc "......"
    th "Please..."
    mc "Uhm... 20 silver a week?"
    th "Ok, I'll do the cooking, washing a-and the cleaning as well."
    mc "You don't need to go overboard, Thea. Let's just-"
    th "Please let me do this... please?"
    mc "......"
    mc "{i}She really wants to do this. I guess I'll just let her."
    mc "Ok, if you say so..."
    th "Thank you, [mc], thank you so much."
    th "{i}Mom, Dad, don't worry. I won't give up, I'll keep on fighting."
    mc "Come on, Thea. Let's go home."
    th "Home...?"
    stop music fadeout 5
    th " Yeah, let's go."
    $ thealives += 1
    scene black with fade
    "Both of you head back to Randel."
    $ thearuntimer = 0
    $ thearun += 1
    $ theajob += 1
    $ time = 3
    jump home
    return


label theaworks:
        hide screen hud
        show smilemc
        show normalth
        show talknth
        th "[mc], great news! I got a job!"
        hide talknth
        show talkhappymc
        mc "What, really? Where?"
        hide talkhappymc
        show talknth
        th "At the tavern, the owner said she'll pay me 10 silver per day."
        mc "{i}10 silver per day!? That's a lot. And here I am getting paid 5 silver for killing a boar while she gets 10 silver per day..."
        mc "{i}July owes me a raise..."
        hide talknth
        mc "That's amazing! Congratulations!"
        show talksth
        th "Thank you!"
        th "I'll be sure to pay you once a week."
        show talkwanmc
        mc "Ok... if you miss it, I'll double the price."
        show normalth
        th "Oh, really? I didn't know."
        show gambaruth
        th "Don't worry, I don't plan on missing any payments."
        show sadsmileth
        show smileecmc
        mc "Haha, I'm just kidding, Thea."
        hide sadsmileth
        hide gambaruth
        hide smileecmc
        show talksth
        th "Really?"
        mc "Yeah, of course!"
        mc "Anyway, what do you do at the tavern?"
        th "She said I'll have to serve tables and stuff."
        mc "When will you be working?"
        th "In the evenings."
        mc "Oh... Well good luck then."
        th "Thanks, [mc]."
        th "Now please excuse me, I have some cleaning to do."
        show gambaruth
        th "Your house is a total mess, you know."
        hide talksth
        show blushtalkhappymc
        mc "Haha, it's been a while since I last cleaned the place..."
        show talksth
        th "It's a good thing I'm here then."
        mc "Thanks, Thea."
        th "Don't mention it, it's the least I can do."
        scene theaclean with fade
        mc "{i}Looks like she's doing ok."
        $ theajob += 1
        $ theagotjob += 1
        $ persistent.theaCleaning = True
        jump home
        return


label theaxgabe:
    hide screen hud
    play sound doorknock
    "{i}Knock knock"
    show thinkmc
    mc "{i}Huh?"
    mc "Who is it?"
    g "It's me, Cynthia. Please open up, [mc]."
    mc "......"
    show talkwanmc
    mc "Hello, Gabe."
    show gabrial hopeful
    show smilemc
    g "How did you know it was me?"
    mc "Because I know your voice."
    g "Ahh, Darn it."
    mc "What brings you here?"
    g "Just came for visit. You come to my place all the time, so I thought I'd do the same for once."
    mc "That makes sense."
    "Gabe makes her way in and looks around herself, admiring the house."
    g "Whoa, this place hasn't changed a bit... It's bringing back memories."
    g "You've kept this place very clean. I'm surprised."
    if gabesClothes == False:
        mc "Ah... yeah."
        mc "{i}It really was all just thanks to Thea, though-{p}...Wait."
        mc "{i}Oh god, I haven't told Gabe about Thea. I guess I should do it now..."
        #mc "{i}Should I?"
        #menu:
        #    "Yes, you moron":
        #        mc "{i}Of course I should."
        mc "Well, actually..."
        g "Mh? What is it?"
        mc "You see, about a week ago I went on a quest to Yorkel..."
        g "Wait, where is this going? Wasn't Yorkel..."
        mc "Yes, it was."
        g "Oh Astylla."
        mc "You see, when I arrived at the village it was already in the middle of being destroyed. I had never seen so much chaos in my life, and I was powerless to stop it, yet... I saw a girl getting attacked by imps and I somehow managed to fend off the imps."
        g "Wow. Alright... but why are you telling me this?"
        mc "Well... She had nowhere to go, so I brought her home."
        g "Oh."
        mc "Yeah..."
        "A rattling sound comes from the kitchen."
        g "Is that her?"
        mc "...Yeah."
        scene theagabe2 with dissolve
        th "Uhm... [mc]? Some of your underwear is missing. Did you pu-"
        show theagabe3
        g "Hi there."
        th "O-Oh, hi!"
        scene homeday
        show prot normal
        show gabrial smile
        show normalth at flip
        th "Sorry, [mc] didn't tell me we had guests. My name's Thea, it's a pleasure to meet you."
        "Gabrial examines her from head to toe for a moment then she smiles"
        g "The pleasure, and surprise, is mine. Name's Gabrial, but you can call me Gabe. I'm one of [mc]'s childhood friends."
        "Gabe then turns towards you and raises an eyebrow."
        g "I'm glad she's safe, but are you sure making her do housework was necessary?"
        #    "Nah, what's the worst that could happen?":
        #        "peepoobleh"
    else:
        mc "Hehehe, thanks."
        if gabeKnowThea == False:
            mc "{i}Wait, Thea's here!"
            mc "{i}I didn't tell Gabe about her."
            mc "{i}Thea, please don't come out."
        show talksadhappymc
        mc "Do you... want tea or something?"
        g "......"
        show talkwag
        g "Do you know how to make tea?"
        mc "Uhm... no?"
        g "Then why ask, pea-brain!?"
        mc "Well, it's... common courtesy."
        g "Uh-huh. I drank tea before coming, so no thanks."
        mc "Ok."
        g "Aren't you getting ready?"
        menu:
            "For what?":
                mc "For what?"
                g "For Academy!"
                mc "Oh, yeah, Academy... I'll get ready soon."
                g "Ugh..."
            "I just woke up.":
                mc "I just woke up."
                g "Quick, get ready then."
                g "We can both go together."
                mc "Ok, ok."
        "A rattling sound comes from the kitchen."
        if gabeKnowThea == False:
            mc "{i}Must be Thea! I didn't tell Gabe about her. Shit!"
        else:
            mc "{i}Uh-oh."
        scene theagabe1
        g "What's that?"
        mc "Uhm... I-I don't know, must be the... m-mouse."
        if gabeKnowThea == False:
            mc "{i}Why am I such a bad liar?"
        g "Mouse?"
        scene theagabe2 with dissolve
        th "Uhm... [mc]? Some of your underwear is missing. Did you pu-"
        if gabeKnowThea == False:
            show theagabe3
            g "......"
            g "Oh, [mc] didn't tell me he had visitors."
            scene homeday
            show talkwanmc
            show talksadhappymc
            show normalgop
            mc "Uhm... G-Gabe, this is Thea."
            mc "Thea, this is Gabrial."
            show talksth
            th "Hello."
            show talkwagop
            g "H-Hi."
            g "That's a nice dress you're wearing. I had one just like that."
            "Gabe looks at you for an explanation."
            mc "Sorry... that I lied, Gabe. The clothes... were for Thea."
            show cutegop
            g "Why did you lie, [mc]? I would've given them anyway."
            mc "I-I don't know. I thought you... wouldn't believe me if I told you."
            g "And your Uncle Pete Story was more believable?"
            mc "I'm sorry, ok?"
            show gambaruth
            th "It's my fault for putting you in a tough spot, [mc]. I think I should explain myself."
            th "[mc] saved me when my village was attacked by imps. I-I was the only survivor. The whole village was destroyed."
            th "I had no place to go but [mc] took me in. He gave me a new life."
            show talksgop
            g "......"
            g "I'm... Sorry for your loss."
            g "...I-I don't know what else to say."
            th "......"
            g "[mc], you are really doing the hero thing, huh?"
            show talkhappymc
            mc "It was just the right thing to do..."
            g "I'm proud of you."
            g "But you've enslaved the poor girl."
        else:
            show theagabe3
            g "Oh, [mc] didn't tell me he had visitors."
            mc "Uhm... Gabe, this is Thea. Remember the girl I told you about? The one from Yorkel?"
            scene homeday
            show talkwanmc
            show talksadhappymc
            show normalgop
            show talksth
            th "Hello."
            show talkwagop
            show normalth
            g "Hi, I see my clothes fits you nicely."
            mc "Thea, this is Gabrial."
            th "Oh, thank you for the clothes. It's a lovely dress, very comfortable."
            g "I'm glad you like it."
            g "If I knew you were still here, I would've come to meet you. I would've brought a few more clothes with me."
            g "I thought you would've left."
            mc "...Thea's living with me for the moment."
            g "Uh-huh... didn't know that."
            g "Explains why this place looks so clean."
            g "I see you've enslaved the poor girl."
    hide talksadhappymc
    mc "What?"
    g "Look she's washing your underwear, cleaning the house, I bet she's doing the cooking too."
    mc "Well, she... Wanted to do that."
    hide normalth
    th "It's true. I wanted to repay [mc]. This was the only way I could."
    show normalth
    g "That's really nice of you."
    g "{i}Clears throat{/i} So, how is it living with [mc]? I hope he hasn't perved around you."
    mc "Hey!"
    th "Perved? I don't know what that means but [mc] has been very kind to me."
    g "Oh... good."
    show sadnth
    th "Uhm... [mc], I really need to dry these clothes before it rains. Can I...?"
    mc "Yes, you can go. You don't need to ask, Thea."
    scene homeday
    show talksth
    show normalgop
    show prot smile
    th "O-Ok, it was nice talking to you."
    g "Same. You're a very nice person, Thea."
    th "Oh... Th-Thank you, Gabrial"
    g "I-"
    "Thea smiles and leaves."
    hide talksth with easeoutleft
    hide normalgop
    show normalg
    g "-said you can call me Gabe..."
    hide normalg
    show talkwag
    g "God, I've never seen a girl so perfect."
    show talkwamc
    mc "Jealous?"
    $ gabethea += 1
    g @ gabrial pout "Of course I'm jealous, I could never be that nice."
    mc "Hmm... yeah, you are a bitch sometimes."
    g "...Yeah."
    g "So, what's the plan? When's the wedding?"
    show talkwanmc
    mc "What? There's no wedding. She's just staying here until she can get back on her feet."
    mc "...That girl's been through a lot."
    g "Hmm... You're right. Poor girl."
    g " You did a good thing, [mc]."
    g "But don't perv on her you hear?"
    show angry
    mc "I don't \'perv\' on her!"
    g "...I know, I know, I'm sorry. You're a good boy."
    hide angry
    g "So, are you coming to the Academy?"
    $ persistent.theaGabe1 = True
    menu:
        "Yes":
            mc "Yeah, let's go."
            jump academy
        "No":
            mc "You go ahead, I'll be late."
            g "Ok."
            jump home


label theadoge:
    hide screen hud
    mc "I wonder what Thea's doing?"
    "You head out to the living room. Thea seems to be in the kitchen and you can smell that she's cooking something good. You take a peek into the kitchen."
    scene theacook1 with fade
    pause
    th "{i}hum~ hum-hum~ hum-hum~"
    pause
    window hide
    "Thea moves away from the pot and goes to the other side of the kitchen."
    scene theacook2 with dissolve
    "You slither your way towards the pot."
    mc "{i}Mmm, smells good."
    menu:
        "Don't":
            mc "{i}I better leave it till it's ready."
            th "Oh, [mc], I didn't see you there."
            scene kitchen
            show smilemc
            show normalth
            mc "Hey, I just couldn't resist the smell."
            th "...It does smell good, doesn't it?"
            show talknth
            th "He'll love it."
            show  talkwanmc
            mc "He? It's not for us, then?"
            th "Us? Hehehe. No."
            th "This is for a little puppy I saw on my way home."
            show talksadhappymc
            mc "...Ah."
            th "Besides, I don't think you'd want to eat this. I made this from some of the leftovers I took from the tavern. We get a lot of scraps, so I thought doing this would be better than just throwing them out."
            mc "Oh thank god, I almost ate it!"
            th "Really? Hahaha. Does it look that tasty?"
            mc "Yeah. You just mixed all the leftovers?"
            th "Y-Yeah, kind of. I added a little meat gravy to it as well. That's why It smells good."
            mc "Wow."
            th "It's nothing really."

        "Taste":
            mc "{i}Ugh, I just can't help myself."
            "You take a spoonful of rice from the pot and eat it."
            mc "{i}So good."
            mc "{i}I hope she won't notice."
            th "Oh, [mc], I didn't see you there."
            scene kitchen
            show smilemc
            show normalth
            mc "Hey, I just couldn't resist the smell."
            th "...It does smell good, doesn't it?"
            show talknth
            th "He'll love it."
            show talkwanmc
            mc "He? It's not for us, then?"
            th "Us? Hehehe. No."
            th "This is for a little puppy I saw on my way home."
            show talksadhappymc
            mc "...Oohhh..."
            show talksth
            th "Besides, I don't think you'd want to eat this. I made this from some of the leftovers I took from the tavern. We get a lot of scraps, so I thought doing this would be better than just throwing them out."
            mc "...F-Funny, you should say that..."
            th "[mc]?"
            th "You didn't eat from this, did you?"
            mc "I-I did."
            th "You did?"
            th "......"
            show lolth with hpunch
            th "Hahahahaha-! {i}snort-{/i} Hahahaha!"
            "Thea laughs out loud, clutching her stomach."
            mc "Ugh..."
            hide lolth
            show crysmileth
            th "I'm s-sorry... hehehe... So, did it taste good?"
            mc "...Well, not feeling any side-effects but... best thing I've ever tasted."
            show lolth with hpunch
            th "Hahahahaha-! {i}snort-{/i} Hahahaha!"
            mc "I sure hope I'm not poisoned..."
            hide lolth
            hide crysmileth
            th "You'll be fine. Oh, [mc], it's been so long since I laughed this hard!"
            mc "I'm glad my stupidity at least made you happy."
            mc "So, you just mixed all the leftovers?"
            th "Y-Yeah, kind of. I added a little meat gravy to it as well. That's why It smells good."
            mc "Wow."
            th "It's nothing really."
    mc "Where did you see the pup?"
    th "He was near the market. I saw him while coming home from work."
    mc "Ah. Let's go then."
    th "O-Ok."
    "Thea packs up the food. The both of you go to the market."
    scene villageback with fade
    show normalmc with easeinright
    show normalthop with easeinright
    th "There he is."
    scene villageback with fade
    "Thea unwraps the food and leaves it near the pup. The puppy starts sniffing around a bit to find the source. The pup slowly comes to the food and starts to eat."
    mc "Where's his mother?"
    th "I didn't see her last time either."
    th "I think the puppy is... all alone."
    scene theadog1 with fade
    pause
    "Thea strokes the puppy as she silently watches him eat."
    mc "{i}Thea seems to really like the pup. Without a mother or other siblings, only to be left alone orphaned in the world. I guess she knows how it feels... to be all alone."
    mc "You should keep him."
    th "What?"
    mc "Would you like to keep the puppy?"
    th "...I... I would it be alright?"
    mc "I wouldn't mind."
    th "[mc]..."
    "Just as Thea reaches to carry the pup, you see another dog coming towards it."
    scene theadog2 with dissolve
    "The pup Thea holds struggles to get free. Thea promptly puts it down as it runs toward the bigger dog. The dog licks the puppy's head."
    pause
    window hide
    th "......"
    mc "That must be his mother."
    "Looking at Thea's eyes, you can tell that she is more sad than happy to see the pup with their mother."
    th "I guess it wasn't alone after all."
    mc "......"
    th "Shall we go, [mc]?"
    mc "...Ok."
    scene villageback with fade
    "The two of you head home. The atmosphere was more bittersweet than satisfying after that event."
    scene kitchen with fade
    show talksth
    show normalmc
    th "Sorry, [mc], I feel a bit tired. Can I go and lie down for a while?"
    show talksadhappymc
    mc "Y-Yeah. You don't need to ask, Thea."
    th "Th-Thank you."
    hide talksth with easeoutright
    show worriedmc
    mc "{i}Poor girl. She still seems to be in pain. How could I blame her? She lost everyone she cared about."
    mc "{i}I should find a way to cheer her up."
    $ theadogfood += 1
    $ time = 3
    $ persistent.theaDoge = True
    jump home
    return


label petemeeting:
    hide screen hud
    scene black with fade
    th "[mc]?"
    mc "Hmmm..."
    th "[mc]!"
    "You feel someone shaking you."
    scene homeday with fade
    show worriedth
    mc "Uhm... Thea... what is it?"
    show normalmc
    th "There someone at the door for you. I think it's your uncle."
    mc "Oh... Uncle Pete."
    mc "......"
    show suprised
    mc "{i}Uncle Pete!"
    mc "{i}He doesn't know about Thea!"
    show talksadhappymc
    mc "D-Did you open the door?"
    show talksth
    th "Y-Yes, is there a problem?"
    mc "Oh... No, no, th-thank you Thea."
    scene kitchen with fade
    "You quickly head into the living room and open the front door."
    show worriedmc
    mc "Uncle Pete, come in."
    show saduncle with easeinleft
    u "Hey, [mc], I-I think I caught you at a bad time."
    mc "Uhm... n-no, no... it's fine."
    u "...I'll come back later. Sorry kid, didn't know you had... {i}clears throat{/i} company."
    u "Bye, [mc]."
    hide saduncle with easeoutleft
    mc "Uncle Pete..."
    "He's gone before you can say anything more."
    show talksth with easeinright
    th "Did he leave already?"
    mc "Yeah."
    show worriedth
    th "Oh... Is everything ok?"
    show talksadhappymc
    mc "Yeah... yeah... he was just... surprised to see you."
    th "You... didn't tell your uncle about me?"
    mc "I-I... really didn't tell anyone about you."
    th "...Ah... ok."
    th "Oh no, did I cause trouble by answering the door? I'm sorry, [mc], I didn't know."
    mc "It's ok Thea, I should have told Uncle Pete."
    show normalth
    th "......"
    hide normalth
    hide worriedth
    th "[mc]?"
    mc "Hm?"
    th "Do you mind if I ask... why you didn't tell anyone about me?"
    mc "Uhm... I just didn't want anyone... to take it the wrong way."
    th "The... wrong way?"
    mc "Yeah... they might... assume... things, when they hear that a girl is staying at... my house."
    th "...I see."
    show worriedth
    th "They might think that you kidnapped me."
    mc "No!"
    mc "They might think we're... lovers."
    hide worriedth
    th "...Oh. I understand."
    show normalth
    th "......"
    hide normalth
    th "Do you think... your uncle thought so?"
    mc "Y-Yes."
    th "..."
    th "......"
    show talknth
    th "Why don't we invite your uncle for dinner?"
    mc "Huh?"
    th "Your uncle might have wanted to spend some time with you. If we invite him to dinner, we can explain everything to him and you can spend some quality time with your uncle as well."
    hide talknth
    th "Right?"
    mc "......"
    th "Oh, look at me talking like this is my house. I'm sorry."
    mc "This is your house as much as it is mine."
    th "......"
    show talkwamc
    mc "And your idea is great!"
    show talknth
    th "Y-You think?"
    mc "Yeah! I'll send him a letter now."
    th "Uhm, [mc], can we... do it tomorrow? I really need to prepare. We should have a good feast."
    hide talknth
    th "Right?"
    mc "Oh... yeah, yeah, sorry. Tomorrow then."
    th "Alright, I'm excited!"
    mc "Hehehe. So am I."
    $ petesawthea += 1
    $ time = 1
    jump home
    return


label petedinner:
    hide screen hud
    "{i}Knock knock"
    mc "{i}Must be Uncle Pete."
    "You hear Thea call for you from her room."
    th "[mc], that must be your uncle. Are you going to get it?"
    mc "Y-Yeah."
    mc "{i}Here goes."
    "You open the door."
    scene kitchenn with fade
    show talksadhappymc
    show unclenormal
    mc "Hey, Uncle Pete, you made it."
    show sadtalkuncle
    u "Yeah, it's not every day that you invite your old man for dinner."
    u "Oh, I see... that your... friend is still here."
    mc "Y-Yes, Uncle Pete. This is Thea."
    show normalthop
    th "Nice to meet you."
    u "You too, dear."
    mc "......"
    mc "Uhm, why don't we get seated?"
    u "Alright."
    scene dinnerpete with fade
    play music happy
    "All of you get seated at the table."
    u "Uhm, where are you from, dear? I haven't seen you in town before."
    th "I-I'm from Yorkel, sir."
    u "Yorkel? Isn't that a bit far?"
    u "Heheh. I guess distance isn't that much of problem in this day and age."
    mc "......?"
    "There is an awkward silence. All three of you stare at the empty table."
    u "I'm sorry, this is really, very strange to me. I'm not sure how I'm supposed to act."
    mc "What do you mean?"
    u "You... want my blessing. That's why we're having this meeting, right?"
    mc "..."
    mc "...Blessing?"
    mc "No, it's nothing like that!"
    th "Hehehe..."
    "Thea lets out a small chuckle. She finds it amusingly funny instead of embarrassing."
    u "Huh... that's not it?"
    "Uncle Pete looks confused."
    mc "No, Thea's just a friend. We invited you here just to make sure that we don't have any misunderstandings like we did now."
    u "O-Ok."
    mc "Uncle Pete, didn't you know that Yorkel was attacked?"
    u "Attacked? ...Wait, the imps? ...That was Yorkel?"
    mc "That one."
    u "I forgot. The whole village was destroyed if I remember correctly?"
    th "Y-Yes..."
    u "......"
    mc "I was on a quest to Yorkel to deliver some crystals. When I got there, the village was destroyed."
    "You tell everything that had happened. Uncle Pete listens to your story a with serious face. You've never seen him this way before."
    mc "She's living with me now."
    u "I can't... believe it."
    "Uncle Pete gives you a hard pat on the back."
    u "You did good, kid. I don't know what to say."
    mc "Thanks, Uncle Pete."
    u "If you need any kind of help, don't hesitate to come to me, Thea."
    th "...Th-Thank you sir, I'll keep that in mind."
    u "\"Sir\"? Hehehe... been a while since anyone called me that. Just call me Pete, dear."
    th "Ok."
    mc "Thea, why don't you bring in the food? I'm sure Uncle Pete might be hungry by now."
    u "I won't lie, I could eat an ox right now."
    th "I'll bring the food right away then."
    show theacutdinner with dissolve
    "Thea runs off to the kitchen."
    u "She's a nice girl, isn't she?"
    mc "Yeah, she is."
    u "So, the two of you are just friends?"
    mc "Y-Yeah."
    u "That's a shame. Trust me, [mc], you don't come across girls like that, often."
    mc "......"
    u "What do you say, [mc]? You already got most of it done, the only thing left is putting a ring on the finger. Hahahaha!"
    mc "Uncle Pete, don't be so loud. She might hear you."
    u "Oh, sorry, sorry. Just got a little exited there. I always wanted to see my boy getting married one day. Hehe."
    mc "{i}Uncle Pete's sounding more like a mother than a father."
    u "So, you don't have any idea of \"extending your friendship\"?"
    mc "I-I haven't thought about it."
    u "Come on, [mc]! I say give it a try."
    mc "Uncle Pete, why are you so concerned about this?"
    u "Because the two of you are perfect together, I can feel it."
    mc "You... said the same thing about Gabe and me."
    u "Did I...?"
    u "Ok, I might have. That's because she was the only girl you used to talk to back then."
    mc "{i}Sigh"
    mc "How do I know she even has the faintest idea about something like that. She's got enough problems as of now."
    u "I know. But having a close partner might be what she needs right now. Think about it."
    mc "......"
    mc "I can imagine how you were a merchant now."
    u "......"
    u "Ahaha! I guess I sold you on that idea."
    u "If you need any advice, your old man's got your back."
    mc "Uhm... ok."
    hide theacutdinner with dissolve
    th "Here's the food, sorry I was a bit late."
    u "No worries, dear. [mc] and I were having a long chat. We forgot that we were hungry. Hahaha."
    th "Hehehe."
    "You can tell she laughed out of politeness."
    "Thea sets the dinner on the table one by one."
    show dinnerfood with dissolve
    u "Whoah. Didn't expect a feast this big."
    mc "Thea, you really outdid yourself."
    th "Thank you... I did the best I could."
    u "Time to dig in then, don't mind me."
    "All of you start to eat. The food is good, that comes as no big surprise."
    u "The food is really good."
    mc "Yeah."
    th "Thank you."
    u "I wish someone would cook for me like this every day. Hehehe."
    "Uncle Pete winks at you while he says this. Thea doesn't seem to get the hint."
    mc "{i}Oh god..."
    u "So, Thea, how do you like it here at Randel?"
    th "Good, it's not that different from Yorkel."
    th "Except..."
    u "What?"
    th "N-Nothing."
    mc "Be honest, Thea, we won't mind."
    th "Well... the men here seem to be a bit lazy compared to home."
    th "I-I mean not everyone, certainly not [mc]."
    th "But I find a lot of people spending most of their time in the tavern."
    u "That is true, there's no denying that."
    th "People in Yorkel often worked in the fields. Almost all day."
    mc "Hmm."
    u "Yeah. See the reason is this..."
    u "Randel has very rich soil. Growing crops is easy here, barely takes any effort. Plus, the population is small, so we don't need a lot of food."
    u "The farmers really don't have to worry much."
    th "You're right. I guess that's why people call Randel the Farmers' Paradise."
    u "Correct."
    "The three of you talk some more while you finish your meal."
    hide dinnerfood with fade
    mc "Man, I'm full."
    u "Yeah, that was a good course."
    th "Glad everybody enjoyed it."
    u "Thank you for the meal, dear. I best be leaving now. If it gets dark, I'd have to sleep here."
    th "We could arrange a bed..."
    th "Right?"
    mc "Y-Yeah."
    u "Hahaha. No, no, I'm leaving."
    u "Goodnight, kids. Hope you'll invite me again."
    mc "We will. Take care, uncle."
    th "Goodnight."
    "Uncle Pete wishes the two of you goodnight and leaves."
    scene kitchenn with fade
    show talksadhappymc
    show normalth
    mc "That went well."
    show talknth
    th "Yeah. Your uncle is really kind and understanding."
    show talksth
    th "I think you were worried for no reason."
    mc "Yeah, I tend to overthink things."
    th "I'm glad everything worked out."
    mc "Same here."
    th "I'll get the dishes washed then."
    mc "Let me help you."
    th "Please, [mc], there's no need for that."
    mc "Hey, you cooked all this amazing food and I'm supposed to just do nothing and go to sleep? This was our dinner, remember?"
    mc "I have to help with something."
    th "...I don't really mind doing these myself."
    "You pick up some plates."
    mc "Come on, let's go."
    th "O-Ok."
    scene kitchenn with fade
    "The both of you carry the plates to the kitchen. You place them all on the sink."
    "You open the tap and take a plate and start washing."
    th "Um... [mc], it's better if you folded your sleeves. They're getting wet."
    mc "Oh, yeah-yeah."
    "You fold up your sleeves."
    mc "{i}[mc], you dumbass, how could you forget?! Wait, did I ever fold my sleeves when washing the dishes?"
    mc "{i}Oh right, I never did the dishes. Uncle Pete did them for me."
    "The two of you start washing the dishes one by one."
    mc "These are an awful lot for three people."
    th "Hehehe... I guess so."
    mc "......"
    mc "So..."
    mc "How's work at the tavern? I never got to ask."
    th "...It's fine. But it does get very hectic at times."
    mc "Yeah, I can imagine."
    th "But the pay's good and the innkeeper says I do a good job. So it's not that bad."
    mc "Hmm."
    mc "Do you like working there?"
    th "Y-Yeah."
    mc "That didn't sound honest."
    th "Well, it's a yes and a no. There are good days and then there are bad days."
    mc "Like what?"
    th "You want to hear them?"
    mc "Yeah, I'm curious."
    th "About the good ones or the bad ones?"
    mc "The bad ones. I would like to know what a bad day is like for Thea."
    th "{i}Sigh ...Ok."
    scene mctheawash with fade
    "Thea starts to talk about her days in the tavern. She seems very enthusiastic, like a child telling what happened at school to her parents."
    th "...And the guy vomits into the cup and hands it to me."
    th "Then he goes \"I'm not paying. See, I didn't drink any.\"."
    mc "Hahaha... What did you do?"
    th "I told the manager. And you won't believe this, he didn't charge him. He told me to serve it to someone else."
    mc "EWWWW What?! No way!"
    th "Yeah! I couldn't believe it too."
    mc "So, did you serve it to someone else?"
    th "......"
    th "Yeah, I didn't have a choice. It was doing that or getting fired."
    mc "Oh god."
    th "It went ok. I served it to the person who was drunk the most. He didn't notice. Hehehe."
    mc "Smart."
    th "Hehehe..."
    mc "But the innkeeper shouldn't have done that."
    th "Yeah. He's always too afraid to act in situations like that."
    mc "So, anyone can boss him around?"
    th "Not everyone. He's only afraid of the... big guys. You know, the ones that walk like this?"
    "Thea imitates someone walking with their hands wide apart."
    mc "Oh, hahahah, I get it. Big guys."
    th "Yeah. I hate those kinds of people. They always seem to have their brains replaced for their muscles."
    mc "Hehehe, yeah, muscleheads."
    "The two of you keep on talking. Thea doesn't seem to stop."
    mc "{i}I've never seen her talk this much before. I guess she needed someone to talk to."
    mc "{i}I feel bad that I didn't talk with her like this before."
    mc "{i}She must've had no one to talk to and it's my fault. I didn't even introduce her to anyone, who else does she have to talk to other than me?"
    mc "{i}I feel like an asshole."
    mc "Hey, Thea?"
    th "Hmm?"
    mc "Why don't we have more dinners like this, with other people?"
    th "......"
    mc "I can introduce you to everyone I know."
    th "......"
    th "That would be great, [mc]."
    mc "You think so too?"
    th "Yes."
    mc "You don't mind having to cook for lots of people?"
    th "Why would I mind? I love cooking for people, it's my favorite thing to do, you know."
    mc "Explains why you're so good at it."
    th "I guess so. Hehehe."
    th "So, who else are we going to invite?"
    mc "Hmm... let's see."
    mc "......"
    mc "Sander and Eve."
    th "Oh, who are they?"
    mc "Some of my friends from the Guild."
    th "Oooh, adventurers! That sounds great."
    mc "When can we invite them?"
    th "Anytime."
    mc "Ok."
    th "OK!"
    mc "{i}Thea looks really excited. It feels good to see her out of her shell."
    mc "Hey, Thea, I forgot to ask. How much did you spend for tonight's dinner?"
    th "Uhm... it's nothing, just a small amount."
    mc "How much?"
    th "Like... 30 silver."
    mc "30 silver!"
    th "Y-Yeah."
    mc "And that's for three? If we're having both Eve and Sander, it's going to cost more."
    th "It will. But don't worry, I got it covered."
    mc "No, I'll pay. I know you're not going to let me pay for today but you can't stop me from paying for the next dinner."
    th "[mc]-"
    mc "No, you can't convince me!"
    th "......"
    th "Oh, ok."
    mc "Thank you."
    mc "So how much might it cost, chef?"
    th "Err... 20 silver."
    mc "20 silver? Didn't you tell me that tonight's dinner costed 30?"
    th "Huh... did I?"
    mc "......"
    mc "...You're lowering the price on purpose, aren't you?"
    th "...N-No."
    mc "Come on, Thea."
    th "{i}Sigh{/i} It might take... about 45 silver."
    mc "Ok, 50 then."
    th "Huh? But I said-"
    mc "It's ok, having some extra is always better."
    th "...If you say so."
    mc "I'll give you the money in the morning. You can get the groceries by then, right?"
    th "Y-Yeah."
    mc "Good."
    "You finish washing the plates."
    mc "I guess we're done here."
    th "We are."
    scene kitchenn with fade
    show talksadhappymc
    show normalth
    mc "Thanks, Thea. Tonight was great."
    show talksth
    th "Wh-Why are you thanking me?"
    mc "Well, first, it was your idea. And second... it was your food."
    th "......"
    th "I guess... you're welcome then."
    mc "...I better get to bed. It's gotten very late."
    th "It has."
    mc "Goodnight then."
    th "Goodnight."
    hide talksth
    th "......"
    show talksth
    th "And [mc]...?"
    hide talksth
    mc "Hmm?"
    show talksth
    th "Thank you..."
    th "Thank you... for everything."
    show talkwamc
    mc "Well, that came out of nowhere."
    th "I-I just felt like saying that."
    mc "......"
    mc "You're welcome. Really."
    scene homenight with fade
    "You go to bed."
    mc "{i}I can't believe how good today went. Total opposite of what I was expecting."
    mc "{i}Thea enjoyed her time a lot."
    mc "{i}I should spend more time with her from now onwards."
    if theanight == True:
        mc "{i}...I feel terrible now, what was I even thinking going to her room at night?"
        mc "{i}She's suffered enough. And if she found out that the only person she can rely on is molesting her in her sleep, she'd lose it..."
        mc "{i}I should stop, shouldn't I?"
        menu:
            "Yes.":
                $ TheaMolest = False
                mc "{i}Yeah, from now on I won't go into her room when she's sleeping anymore."
            "No.":
                $ evil += 1
                "{i}...Be she won't find out."
                "{i}Yeah, I'll just... be more careful."
    $ petedinner += 1
    jump home


label sanderpetedinner:
    hide screen hud
    play sound doorknock
    "{i}Knock knock knock"
    mc "I'll get it!"
    scene kitchenn
    show talkhappymc
    mc "Uncle Pete, come in."
    show uncletalk with easeinleft
    u "Hello."
    u "I didn't come empty-handed this time, here."
    "Uncle Pete hands you some fish. You give it to Thea."
    u "I'm glad you kids invited me again."
    play sound doorknock
    "{i}knock knock"
    u "Huh, more guests?"
    mc "Yeah, must be Sander."
    scene kitchenn
    show talksadhappymc
    show talkwas with easeinleft
    show uncletalkop
    sa "Foof. It's freezing out there today."
    mc "Uncle Pete, this is Sander."
    mc "Sander, Uncle Pete."
    "The both of them shake hands."
    sa "Oh, a pleasure to meet you. [mc] here has said a lot about you."
    u "Hehehe, he's said a lot about you too."
    sa "I guess we don't need introductions then."
    scene kitchenn
    show smilemc
    show unclesmiletop
    show talkwaecs

    "Sander and Uncle Pete" "Hahahaha!"

    mc "Come, sit down."
    scene dinnerpetesander with fade
    play music happy
    sa "Oh, yes, I've been dying to eat Thea's food again."
    u "Heheheh, I guess I ain't the only one."
    "Sander and Uncle Pete" "Hahahaha!"
    mc "\They're getting along well. Almost too well, it's weird."
    th "I'll bring the food right away then."
    show theacutdinner with dissolve
    u "Yes, hurry!"
    sa "Bring it as fast as you can!"

    sa "Why don't we have a drink until the food arrives. You do drink, right Pete?"
    u "Oh, yes. I'm not sure about this kid here."

    u "His tolerance is a bit low."
    sa "I know! hahahaha!"
    mc "Hey! I'm more used to it now."
    sa "Hahaha, we'll see."
    "Sander keeps his bottle on the table."
    sa "Bring some cups, will ya?"
    "You bring four cups. Sander pours the booze."
    sa "Cheers!"
    "Everyone" "Cheers!"
    u "Khaaaah..."
    u "Strong stuff!"
    sa "Hehehe, yeah. It's moonshine, I made it myself."
    u "Whoah, it's great."
    sa "Thanks."
    u "What do you think, kid?"
    "You take a one quick gulp. You feel like you just drank pieces of glass; you whole body starts to burn."
    mc "{i}Cough{/i} It's... good."
    "Sander and Pete" "Hehehe!"
    "Thea comes in with the food. She sets them on the table."
    hide theacutdinner
    show dinnerfood with dissolve
    sa "Thea, I poured one for you. Tell me what you think about my moonshine."
    th "Oh, ok."
    u "It's pretty strong."
    th "......"
    "Thea picks up the cup and takes a few gulps and gently keeps it on the table, like she just drank a cup of tea."
    th "It's good."
    "The three of you stare at her like you've seen something inhuman."
    th "Wh-What?"
    sa "Was it... strong?"
    th "Y-Yeah, a bit."
    mc "A bit?!"
    u "Hahahahaha! This girl keeps getting better and better!"
    sa "Yeah, kid, you can learn a thing or two from her."
    mc "Very funny, guys."
    "Thea looks confused, like she did something wrong."
    sa "Hehe. Anyhow, let's get to the eating, shall we? I'm starving."
    u "Yeah."
    "You all start to eat."
    sa "{i}Munch"
    u "So, Sander, what can you say about my boy here? I hear you've been adventuring together."
    sa "The kid's alright. I mean, {i}munch{/i} he's already saving damsels in distress. He'll do fine."
    u "Hehehe."
    "You finish eating. The drinks are almost over."
    "You manage to finish half of it, you have no chance of finishing the rest because you can't lift the cup anymore."
    "Sander and Uncle Pete are almost done with their drinks. You can tell that they're not doing so well either."
    "You turn to Thea. She's finished her drink. He stares at you guys like looking at a bunch of amateurs."
    sa "Haaaah, I'm full..."
    u "Mmmmm..."
    sa "Now... {i}hic{/i} we dance!"
    u "Not sure my old bones would work but why the hell not!"
    sa "Yeah, that's the spirit!"
    sa "Come on, [mc]! Get your ass up here!"
    mc "Haaa?"
    mc "I-I don't feel... like it."
    u "Come on!"
    "Uncle Pete and Sander lift you up from your seat."
    scene petesanderparty with fade
    pause
    sa "Ok, what we gonna sing, Pete?"
    u "Uhm... how about the \"Maiden of Dorn\"?"
    sa "Yes!"
    "The both of them start to sing."
    "Pete and Sander" "\'Ohhhhh- Maiden of Dorn, her heart full of scorn...\'"
    "Uncle Pete and Sander continue singing while swinging you like a puppet."
    "Thea laughs and claps while they sing."
    "All the sounds and lights turn into a blur as you are tossed around the room. But you can feel that everyone is having a good time... at the expense of your safety."
    "The both of them continue singing until they have no songs left to sing."
    sa "Ohhhhh- Maiden of Dorn, he-"
    u "We already sang... that. {i}hic"
    sa "Oh, did... we? I guess we're out of songs."
    u "Foof, sorry boys, I'm beat."
    sa "Yeah, me too."
    u "[mc], you still with us?"
    mc "Yeeeeesss."
    th "Hehehehe."
    "All of you let go of each other. You can barely stand. You wobble your way to the chair and get seated. You start seeing stars flashing before your eyes."
    "Sander is already flat on the floor."
    scene kitchenn with fade
    u "Hey, Sander... wake up!"
    sa "...Bring Eve..."
    u "Who?"
    mc "Come on, Sander. Eve's not here."
    sa "Aww... Whaaa-"
    u "Come on."
    "Uncle Pete and Thea lift Sander up. Sander leans on Pete's shoulder."
    u "Where should I take him?"
    mc "Uncle, are you sure you can..."
    u "Yeah... don't worry."
    sa "Just leave me at the Guild..."
    sa "Eve will pick me up."
    u "Alright. We'll be leaving then. Thank you for the food, kids."
    th "Take care."
    sa "Good... night."
    "The both of them leave the house."
    mc "Argh... my head."
    show worriedth
    show blushsmilemc
    th "[mc], it's better if you go and sleep. I'll do the dishes."
    mc "No... no... I can help."
    show gambaruth
    th "No... You'll just end up breaking them."
    show worriedmc
    mc "B-But."
    th "No Buts... you go to sleep this instant."
    mc "Alright, alright, no need to be so harsh."
    show talksth
    th "Hehehe, sorry."
    scene homenight with fade
    "You head to your room, bumping into some furniture in the process. You hear Thea laughing behind you."
    "You fall to your bed, your head is still spinning."
    "Slowly, everything goes dark and you're asleep."
    scene black with dissolve
    stop music
    show text "{color=#fff}End of day [day]." at truecenter
    with dissolve
    pause
    hide text with dissolve
    call sleepvars from _call_sleepvars_6
    "..."
    "......"
    "........."
    mc "Urgh..."
    scene homeday with fade
    pause 0.3
    scene black with fade
    pause 0.3
    play music home
    scene homeday with fade
    pause 0.2
    scene black with fade
    pause 0.2
    scene homeday with fade
    show worriedmc

    mc "Ahhg, my head. Drank too much last night."
    show talksth
    th "Oh, [mc], you're finally up."
    mc "Eh?"
    th "It's past noon, you know."
    mc "Ahhh."
    th "Here, drink this."
    mc "What is it?"
    th "Lemon juice with honey, it'll help with the headache."
    mc "Oh... thank you."
    show talknth
    th "Drink up, I'm heading off to work."
    mc "Ok, stay safe."
    hide talknth
    th "Hehehe, I'm not going to war, [mc]."
    show talksadhappymc
    mc "Yeah, I don't know why I said that."
    th "Hehehehe. Bye."
    mc "Bye."
    scene homeday with fade
    "You watch as Thea leaves the house."
    "You finish drinking Thea's drink. It tastes weird but you like it."
    mc "{i}My headache is starting to go away. I guess it works."
    $ time = 3
    $ sanderpetedinner += 1
    jump home


label sanderevedinner:
    hide screen hud
    scene homenight
    play sound doorknock
    "{i}Knock knock."
    mc "{i}Our guests are here."
    mc "Thea, can you get the door?"
    th "Yes... S-Sure."
    sa "OPEN UP!"
    e "SHHH!"
    sa "Oh, hello, who's this?"
    th "I'm Thea. Nice to meet you."
    scene kitchenn with fade
    show normalthop
    show talksr
    show wasmilee
    show talksadhappymc with easeinright
    mc "Guys!"
    e "Hello, little one."
    sa "Hey, [mc]. You didn't say you were inviting your girlfriend. I would've worn something better."
    e "You don't have anything else to wear."
    sa "I do!"
    "Thea tries to suppress her laughter over their antics."
    mc "Come, guys, please sit."
    scene dinnersandereve with fade
    play music happy
    e "So, what's the occasion, little one?"
    sa "Yeah, this came out of nowhere."
    mc "Well, the main reason is... I wanted to introduce you guys to Thea."
    mc "It was Thea's idea to have a dinner."
    e "Oh."
    e "So... how long have you two been together?"
    mc "{i}Why does everyone assume the same thing!? It's annoying as hell!"
    mc "It's not what you think. Thea and I are just friends."
    mc "She's from Yorkel."
    sa "Yorkel? Wait, isn't that the village that was burnt down?"
    mc "Yes."
    "You tell Sander and Eve the entire story."
    sa "Whoah, [mc]. You're a damn hero!"
    e "You've done a great deed, little one."
    sa "So, you've been living with [mc] since then?"
    th "Y-Yes."
    sa "But I kinda get the feeling I've seen you somewhere before."
    mc "She works at the tavern."
    sa "Oh, yeah! That's where."
    e "Wait, you go to the tavern? I thought you hated the place."
    sa "I go there sometimes, when the Guild runs out of booze."
    mc "Why don't you like the tavern?"
    sa "The drinks there are piss, no offence."
    th "Oh... none taken."
    sa "And why go to the tavern when you can get free drinks at the Guild? Hahahaha."
    e "That's the main reason right there."
    sa "Speaking about drinks, we almost forgot."
    sa "We didn't come empty handed. We brought booze!"
    "Sander places a large bottle of booze on the table."
    sa "I know [mc] loves it. Hehehe."
    e "Stop teasing the boy, Sander."
    sa "Whaaat? I was being serious."
    e "We brought something else as well."
    e "Tada!"
    if mcfood == "chicken":
        e "We brought some chicken since [mc] told us that it was his favorite thing to eat."
        mc "Wow guys, you shouldn't have. Thank you."
    if mcfood == "salad":
        e "We brought salad since [mc] told it was his favorite thing to eat."
        mc "Wow guys, you shouldn't have. Thank you."
    if mcfood == "bread with apple jam":
        e "We brought some apple pie. [mc] said his favorite thing to eat was bread with apple jam but that didn't feel right for dinner. So we brought some apple pie instead."
        mc "Wow guys, you shouldn't have. Thank you."
    if mcfood == "fish":
        e "We brought some fish since [mc] told us that it was his favorite thing to eat."
        mc "Wow guys, you shouldn't have. Thank you."
    if mcfood == "boar porkchops":
        e "We brought some wild boar since [mc] told us that it was his favorite thing to eat."
        mc "Wow guys, you shouldn't have. Thank you."
        th "...We already have wild boar."
        e "Oh."
        th "B-But the more the better!{p}...Right?"
        e "Absolutely!"
        sa "Heheh, I like this girl."
    th "I'll get the food then."
    mc "Ok."
    show theacutdinner with dissolve
    e "Little one, how come you never told us about her before?"
    sa "Yeah."
    mc "......"
    mc "I-I don't know. I kinda felt like she needed some time alone, after everything that happened."
    e "Hmm..."
    sa "Ohh, I get it. Little man didn't want anyone to find out about his little girlfriend. He wanted her all to himself."
    mc "What!?"
    e "...That does seem like a more reasonable explanation."
    mc "Eve, you too!?"
    e "Hehehe, we were just joking, little one."
    sa "Yeah. You did great saving that girl, little man."
    e "Yes, we're proud of you."
    mc "Th-Thanks."
    sa "Oh, looks like the food is here."
    hide theacutdinner with dissolve
    "Thea places the food on the table."
    show dinnerfood
    sa "Wooo-hooo! I can't wait to dig into this."
    mc "Go ahead."
    "Everybody starts to eat."
    sa "So good!"
    e "Sander, your mouth's full! Stop shouting!"
    "[mc] and Thea" "Hehehehe."
    e "The food is delicious, Thea."
    th "Thank you."
    sa "{i}Munch Munch"
    sa "Hey, Eve, didn't- {i}munch{/i} we hear that Yorkel was being rebuilt?"
    e "Oh, yes. We heard that a small group of people survived and they're now starting to rebuild the village."
    mc "Really, that's great news!"
    th "...Yeah."
    mc "{i}Thea's home is being rebuilt."
    mc "{i}Will she leave after the village is rebuilt?"
    mc "{i}But her family is already gone, she doesn't have reason to go back, right?"
    mc "{i}Huh? Am I actually worried that she would leave me?"
    "You continue the dinner."
    sa "Let's have some booze, shall we?"
    mc "Alright."
    th "I'll bring the cups."
    "Thea brings four cups from the kitchen. Sander pours the booze into all four cups."
    sa "Cheers!"
    "Everyone" "Cheers!"
    "Sander takes a sip from his cup."
    sa "Ahhhhhh..."
    sa "Good food and booze. Is there anything better?"
    e "I haven't eaten this much in ages. Hehehe."
    th "I'm glad you all liked it."
    sa "Haaa... What a girl. If I was like 20 years younger, I would've married her, no questions asked. Hahahaha."
    e "SANDER! Are you drunk already, you idiot? Don't say things like that, you're making the poor girl blush."
    sa "HAHAHAH! I'll say what I want, woman!"
    "Thea seems to enjoy the drama between Sander and Eve rather than getting embarrassed."
    th "Hehehe."
    e "Don't mind him, dear. He just has a habit of saying stupid things like this."
    th "I don't mind. Hehehe."
    sa "See, she gets a joke. Unlike you, you old hag."
    e "Oh, shut up."
    "[mc] and Thea" "Hehehehe."
    mc "{i}Having these two argue is rather entertaining."
    "A few moments pass. Everybody finishes eating."
    sa "Hey, why don't we sing a song?"
    mc "Huh?"
    sa "Sing a song! What's a party without some singing and dancing?"
    e "Agreed!"
    sa "I know, why don't the two of you give us a little dance while we sing."

    mc "Us? Wh-Why?"
    sa "Come on, don't be shy. Besides, Eve and I are too drunk to dance anyway."
    sa "Come, come, come!"
    "Sander drags the two of you out of your seats."
    "He pushes both of you to the center of the room."
    "Eve and Sander starts to sing."
    mc "{i}Guess we don't have a choice, huh?"
    scene mctheadance with fade
    pause
    window hide
    mc "{i}I look back at Thea. Surprisingly, she doesn't seem to mind."
    th "Might as well give them something to remember, right?"
    mc "Yeah... Though I think they'll forget after this."
    th "Hehehe."
    mc "{i}Our eyes focus on each other. Our hands touching palm to palm in a perfect fit."
    mc "{i}Sander and Eve start to sing. I anticipated to move the moment Thea took her steps."
    mc "{i}I honestly never danced like this before but... Following Thea's movements is almost becoming natural for me."
    mc "{i}It's like Thea and I have been in sync with each other... That I understand her movements very well."
    mc "{i}Every turn, every step, it's like I know how she feels... Her living with me really does wonders."
    mc "{i}But then... What happens if she goes back? All that time I spent with her would have been for nothing..."
    mc "{i}As soon as the song finishes, Thea and I bow to each other."
    mc "{i}Eve gives out her applause... Wait, what about Sander?"
    scene kitchenn with fade
    show smilemc
    show sadsmilethop
    show smilee
    e "Yay. That was beautiful."
    th "Thank you."
    "Sander is asleep on his chair."
    show angrytalke
    e "Hey, wake up!"
    sa "...Mmh... No."
    e "Come on, the party's over."
    sa "......"
    sa "Carry me please."
    e "{i}Sigh"
    hide angrytalke
    hide smilee
    "Eve picks up Sander. She does it with ease which shows that she must've done this about a hundred times."
    show talkwase
    e "Thank you, both of you. We had a great time."
    sa "...Yeeaahh..."
    show talksadhappymc
    mc "Thank you for coming. Get home safe."
    e "Goodnight, little ones."
    hide talkwase with easeoutleft
    "Eve and Sander leave."
    mc "Phew, finally over."
    th "Hehehehe."
    "The both of you pick up the plates and go to the kitchen."
    "You start to wash the dishes."
    scene mctheawash with fade
    th "Those two are really fun to be with."
    mc "Yeah."
    th "They reminded me of my little brother and sister."
    th "They always used to fight with each other but they were always together. They didn't show but they loved each other a lot."
    th "I always used to watch how they would go from playing to fighting each other in the mud in a matter of seconds. Hehehe."
    th "......"
    "Thea stares at the sink for a while."

    th "We should invite them again sometime, right?"
    mc "Y-Yeah."
    "The two of you finish washing the dishes. There's not much talk today."
    stop music
    scene kitchenn with fade
    show worriedmc
    show sadsmileth
    mc "Thea, about your village."
    show talksth
    th "Yes, looks like I won't have to bother you for long."
    hide talksth
    mc "Do you really want to leave?"
    show talksth
    th "Huh...?"
    th "......"
    th "Y-Yeah, I can't trouble you forever."
    th "Right?"
    mc "{i}I'm going to say it."
    show talksadhappymc
    mc "You can stay here, I mean..."
    mc "I don't want you to leave."
    th "......"
    mc "I like having you here and you don't have anyone back at the village."
    th "......"
    th "[mc]... I-I..."
    scene kitchenn
    show surprisedblushmc with hpunch
    show cryth
    "Thea hugs you tight."
    mc "Wha..."
    show smilemc
    th "Thank you, [mc]. I really didn't want to leave."
    th "I like staying here too."
    mc "I-It's settled then. You're a permanent resident of Randel."
    th "Hehehe... Yeah."
    mc "Great."
    show blushth
    show blushsmilemc
    "The two of you stare at each other, waiting for someone to make a move."
    th "......"
    "Thea looks away in embarrassment."
    show talksth
    th "I-I guess I'll get to bed then. I'm very tired."

    mc "Y-Yeah, me too."
    mc "Goodnight."
    th "Goodnight."
    scene homenight with fade

    mc "{i}I got Thea to stay!"
    mc "{i}I guess I do have feelings for her."
    mc "{i}But, what was that back there? Was she waiting for me to make a move?"
    mc "{i}...Does she feel the same way?"
    mc "{i}Sigh... I'm too drunk to think now."
    $ sanderevedinner += 1
    jump home


label beforetheDinnerwithjustThea:
scene kitchen with fade
mc "{i}Seems like Thea's home... I think she's in the kitchen."
scene theacook1 with fade
th "Oh, hi [mc]."
mc "You're home early."
th "Yeah. I came a bit earlier today. It's a special day, right?"
mc "Yeah."
mc "Just to be sure, this is for us, right?"
th "Hehe. Yes, [mc]."
mc "Good. It smells great, can't wait."
th "I'll call you once the food is ready."
mc "Ok."
jump home

label theainvite:
    if theadinner == 1:
        if iwine == 0:
            mc "{i}I'll have to buy some wine first."
            jump home
        show talksadhappymc
        mc "How about we have that da- I mean dinner today?"
        show talksth
        th "Alright."
        mc "Alright! See you tonight."
        th "O-Ok..."
        th "B-but we're in the same house. So, I'm not allowed to see you till tonight?"
        mc "Oh- I forgot. Hehehe."
        mc "{i}[mc], you idiot!"
        show lolth
        th "Hehehe, I'm joking, [mc]."
        th "See you tonight then."
        mc "Y-Yeah, tonight."
        th "Hehehe, ok [mc]. If you don't mind, I have some cleaning to do."
        mc "Alright."
        scene homeday with fade
        mc "Come on, get it together, [mc]. Stop acting like an idiot in front of her."
        $ theadinner += 1
        jump home
    $ theadinner += 1
    show talksadhappymc
    mc "Hey Thea, I was thinking. Why don't we have a special dinner, just the two us."
    show blushth
    th "Only the two of us?"
    mc "Y-Yeah. I just realized the two us haven't had dinner together, alone I mean."
    th "......"
    th "Ok."
    mc "Great-"
    show gambaruth
    th "But on one condition."
    show talkwanmc
    mc "huh?"
    th "I'm paying."
    mc "Aarrgh... Why are you always insisting to pay?"
    th "Because I want to."
    mc "... But why-"
    mc "Oh, fine."
    show talkhth
    th "Yes!"
    mc "Well, at least let me get the drinks. What kind of man would I be if I let the woman pay for everything?"
    th "......"
    th "Alright then."
    mc "Thank you."
    th "So... when are we having this \"special\" dinner."
    hide talkwanmc
    mc "Uhm... I'll let you know."
    th "OK, make sure you tell me in the morning."
    mc "Alright."
    show talksth
    th "I'm looking forward to it."
    mc "Hehehe, me too."
    scene homeday with fade
    mc "I just asked her out for dinner."
    mc "Well, it's technically not \"out\" since the both of us live in the same house. Ugh, who cares?"
    mc "Hope this goes well!"
    mc "I have to buy drinks. I better not cheap out here."
    mc "I'll have to visit Mervin."
    jump home
    return




label theadinner:
    hide screen hud
    th "[mc], dinner's ready!"
    mc "I'm coming!"
    scene kitchenn with fade
    "You go to the dining area."
    "The table is arranged with two candles and neatly placed plates, spoons, forks and knives. The napkins are neatly arranged into a pyramid shape."
    th "Get seated, I'll go bring in the food."
    "You do as you're told and got seated."
    "After a few moments, Thea brings the food and places it on the table."
    "She then gets seated."
    scene theadinner with fade
    play music nurture
    th "{i}Phew{/i}... Finally done. Hope you weren't hungry."
    mc "Not at the moment."
    $ theadinner += 1
    mc "The table arrangements are really done nicely. Where did you get the candles?"
    th "I-I bought them."
    mc "Just for tonight?"
    th "Y-Yeah, there was a new merchant in the market selling all kinds of candles and lamps. They looked really pretty so I bought them."
    th "They were very cheap, so don't worry."
    mc "They look nice. Really helps to set the mood."
    th "Glad you like them."
    mc "......"
    mc "The food looks great, as usual."
    th "Thank you."
    mc "Oh, here, I brought some wine."
    th "Let me see."
    if cheapwine == 1:
        th "Oh..."
        "Thea inspects the bottle. She shows a slight sense of disappointment."
        mc "What?"
        th "Huh? ...No, it's nothing."
        mc "Sorry, this is all they had."
        show theadinner3
        th "No, no, I don't mind."
        mc "Let's try it then."
        "You pour the wine into the two cups."
        mc "Cheers!"
        th "Cheers."
        th "Mmmh. Yup."
        mc "...I'll buy something better next time."
        th "It's fine, [mc]."
    if goodwine == 1:
        show theagoodwine with easeinright
        pause
        "Thea takes the bottle and inspects it with great interest. Her face lights up with delight."
        th "Whoah! A Dornish white blend!"
        mc "A what?"
        th "Th-This is some really good wine, [mc]! How much did it cost?"
        mc "Uhm... not much."
        th "Really! Wow."
        mc "You really know your wines."
        th "Heh... Yeah."
        th "My pa' brewed all kinds of wine and beer. He was a master brewer, according to the townsfolk."
        mc "Really?"
        th "Yeah. He taught me a lot about wines and beer."
        th "Pa' didn't have anyone to help him with brewing. My young brother Joie was too small, so I offered to help."
        mc "So, you helped your father make booze?"
        th "Heheh, yeah. I know it sounds strange, coming from a girl."
        mc "No, that sounds awesome. That explains why you're so good at drinking."
        th "I guess. I used to taste a lot of his brews, heh."
        mc "Let's see how it tastes then."
        "You pour the wine into the two cups."
        mc "Cheers!"
        th "Cheers."
        th "Mmmh. This is good."
        mc "It's not that strong."
        th "It's not supposed to be."
        menu:
            "I like it.":
                mc "I think I like wine."
                th "Me too. The smell of bouquet, the flavor of grapes straight out of the vineyards, even the zesty, velvet touch that hits your tastebuds..."
                mc "You definitely sound like a master brewer's daughter."
                th "Sorry."
                mc "No, no, it's fine. I like it, makes drinking it fancier."
                th "Hehehe. Yeah."
            "It's too weak for me.":
                mc "I don't know. Doesn't have much of a kick."
                th "True but I like it. It's got that bouquet smell, the flavor of grapes straight out of the vineyards, even the zesty, velvet touch that hits your tastebuds..."
                mc "You definitely sound like a master brewer's daughter."
                th "Sorry."
                mc "No, no, it's fine. I like it, makes drinking it fancier."
                th "Hehehe. Yeah."
    mc "Let's eat then."
    "The two of you start eating. There's a wider variety of food compared to the previous dinners. You can definitely tell that she went all out."
    mc "The food's great."
    th "Thanks."
    "The two of you continue to eat in silence."
    mc "{i}Ok, I have to start a conversation."
    mc "So... how's work?"
    th "It's the usual. It's pretty boring. You won't enjoy hearing about it."
    mc "Oh... ok."
    th "Tell me about your work, your adventures. They might be far more interesting than my stories."
    mc "Alright, let's see..."
    "You tell Thea about all your adventures. Each point in your previous adventures you can remember being most eventful, you explain as best you can."
    "Regardless, Thea peers into you, showing with great interest."
    th "Wow, that's amazing. I've heard that goblin urine is really toxic; just touching it will kill you, right?"
    mc "Yeah, I still can't believe I dodged it."
    th "Whoah."
    mc "Don't you like to go on adventures?"
    th "Me? Uhm, no. I'm more of an indoor-type person. I like doing housework."
    mc "Oh, I see."
    "You take a sip of wine."
    mc "This wasn't strong at first but I can kinda fell it kicking in now."
    th "Yeah and there's still a lot left in the bottle."
    mc "Why don't we have a small drinking game?"
    th "Drinking game?"
    mc "Yeah. Haven't you played?"
    th "N-No."
    play music happy
    mc "Alright, you play it like this."
    mc "I guess something about you. If I'm wrong, I take a shot. And if I'm right, you take two shots."
    th "Ok, I think I get it. But why do I have to take two shots?"
    mc "To make it fair, you're too good at drinking."
    th "Hehehe, fine."
    mc "Here we go. Round one."
    menu:
        "You had never left your hometown before coming here.":
            mc "You had never left your hometown before coming here."
            th "So now I'm supposed to drink?"
            mc "Wait, was I right?"
            th "Yeah."
            mc "Hah!"
            mc "Yeah, go ahead, drink up."
            th "Alright."
            "Thea drinks."
        "You've never gotten drunk.":
            "You've never got drunk before."
            th "Wrong."
            mc "Damn it!"
            th "You're supposed to drink now right?"
            mc "{i}Sigh{/i} Yeah."
            "You take a sip."
            play sound gulp
            $ drinkth += 1
            scene theadinner with vpunch
            mc "Khaaaah..."
    menu:
        "You love reading.":
            "Uhm... you love reading."
            th "Hmm... I do read but I wouldn't say I \'love\' reading."
            mc "Urrgh. Guess I'll have to drink."
            th "Yes!"
            "You take another sip."
            play sound gulp
            $ drinkth += 1
            scene theadinner with vpunch
            mc "Khaaaah..."
        "You love animals.":
            "You love animals."
            th "Damn it. That was an easy guess."
            mc "Hehehe."
            "Thea drinks."
    menu:
        "You never let anyone do your work.":
            mc "You never let anyone do your work."
            th "Ok, you got me."
            mc "YAAAS!"
            mc "Drink! Drink! Drink!"
            "Thea drinks"
        "You've never scolded anyone.":
            mc "You've never scolded anyone."
            th "Never scolded anyone? I'm not an angel, [mc]."
            th "Actually I get mad pretty fast. I've scolded you a couple of times if I remember correctly."
            mc "Hmm, I guess your definition of scolding and mine are different."
            th "So, what now?"
            mc "I guess I'll drink then."
            th "I could let you win the round if you want."
            mc "Hey, stop treating me like a kid!"
            th "Hehehehe"
            "You drink."
            play sound gulp
            $ drinkth += 1
            scene theadinner with vpunch
    menu:
        "You like cooking":
            mc "You like cooking."
            th "Another easy one."
            mc "I'll do anything to win."
            th "Here goes."
            "Thea drinks."
            th "Khaaaah..."
            mc "Starting feel it, I see."
        "You like dancing.":
            mc "You like dancing."
            th "Wrong. I don't really like it because I'm not good at it."
            mc "What?! But you danced with me."
            th "And was I good?"
            mc "Yeah. I mean, I'm no expert in dancing myself but I think you did pretty well."
            th "Really?"
            th "Hmm but it still doesn't mean I like it. I'm kinda neutral about it now."
            mc "Oh, come on!"
            th "Drink up, [mc]."
            "You drink."
            play sound gulp
            $ drinkth += 1
            scene theadinner with vpunch
    "Hello, this is your stomach. I have this to say: {i}Ugh..."
    th "You don't look so good, [mc]."
    mc "Ha! It'll take more than that to take me down."
    th "Hehehe. This is fun."
    mc "{i}Come on, [mc]! Haul ass!"
    "The game continues. You can't really tell how long the two of you have been going at it. You win some, Thea wins some and the end it's safe to say that the both of you are drunk."
    if  drinkth > 3:
        scene theadinner3 with fade
        pause 0.2
        scene theadinner3d with dissolve
        pause 0.2
        scene theadinner3 with dissolve
        mc "Ughh..."
        th "[mc], are you alright?"
        scene theadinner3d with dissolve
        mc "...Uhm..."
        th "[mc]!"
        mc "Yes, I'm fine, {i}hic{/i} darling."
        scene black with vpunch
        stop music
        play sound crash
        th "[mc]!"
        show text "{color=#fff}End of day [day]." at truecenter
        with dissolve
        pause
        hide text with dissolve
        call sleepvars from _call_sleepvars_7
        mc "Mmmh..."
        scene homeday with fade
        pause 0.2
        scene black with fade
        pause 0.2
        scene homeday with fade
        mc "Urgh... Wha-?"
        if didtest > 0:
            $ time = 3
            mc "Wait... it's evening?"
            mc "Did I pass out yesterday?"
            "You find a glass of lemon juice and a paper note underneath it."
            mc "Thea must have left this here."
            th "I'm at work. I made some lemon juice, please drink it if you have a headache. I had a great time last night, thank you."
            mc "Last night."
            mc "Urgh, I can't remember the end."
            mc "I remember asking Thea if we could play a drinking game and that's it. I guess it didn't go well."
            mc "Well, at least she had a good time."
            jump home
        else:
            "You feel someone tugging your arm."
            $ time = 0
            mc "H-Huh? D-Did I pass out?"
            th "Yes! But it's alright. I woke you up in time."
            mc "For what?"
            th "I remember you mentioning today was your test day?"
            mc "OH GOD! THE TEST!"
            "You quickly get ready to go to the academy. Thea gives you a lemon juice to help you with the hangover."
            mc "Thanks Thea! See ya!"
            th "No problem. Good luck!"
            jump testHangover
    scene theadinner2 with fade
    pause 0.2
    scene theadinner2d with dissolve
    pause 0.2
    scene theadinner2 with dissolve
    mc "Alright! ...The bottle's finished, just one more... round to go."
    th "Let's do it! Hehehe."
    mc "YEAH!"
    scene theadinner2d with dissolve
    mc "...Let's see..."
    menu:
        "My hs a lw a l go u wa ldwa.":
            mc "You love me."
            th "Wh-Whaaaaa?"
            mc "W-Wait I... m-meant-"
        "Do e f si o  you as ha d kwa.":
            mc "You love me."
            th "Wh-Whaaaaa?"
            mc "W-Wait I... m-meant-"
        "Poeop a he is i oei oa a.":
            mc "You love me."
            th "Wh-Whaaaaa?"
            mc "W-Wait I... m-meant-"
    menu:
        "I hd ask ald lwadds.":
            mc "I love you."
            th "...[mc]?"
        "I hei a a ks lkalas.":
            mc "I love you."
            th "...[mc]?"
        "No sai ius a wll s.":
            mc "I love you."
            th "...[mc]?"
    scene black with vpunch
    stop music
    play sound crash
    th "[mc]!"
    mc "Mmmh..."
    show text "{color=#fff}End of day [day]." at truecenter
    with dissolve
    pause
    hide text with dissolve
    call sleepvars from _call_sleepvars_8
    scene homeday with fade
    pause 0.2
    scene black with fade
    pause 0.2
    scene homeday with fade
    mc "Urgh... Wha-?"
    $ time = 3
    mc "Wait... it's evening?"
    mc "Did I pass out yesterday?"
    "You find a glass of lemon juice and a paper note underneath it."
    mc "Thea must have left this here."
    th "I'm at work. I made some lemon juice, please drink it if you have a headache. I had a great time last night, thank you."
    mc "Last night."
    mc "Urgh, I can't remember the end."
    mc "I remember asking Thea if we could play a drinking game and that's it. I guess it didn't go well."
    mc "Well, at least she had a good time."
    jump home




label theafirsttime:
    hide screen hud
    play music tavern
    scene tavern with fade
    show thinkmc with easeinright
    $ theadinner += 1
    mc "{i}Whoah. This place... looks horrible."
    mc "{i}Thea's been working in a place like this?"
    "You see Thea serving drinks. She stands out like a diamond in the rough, among the improper, unsanitary environment she's in."
    "You wave at her. She sees you and hurries over to talk to you."
    show talksth with easeinleft
    th "Hey, [mc]. What are you doing here?"
    show talksadhappymc
    mc "Well, I decided to drop in and see you at work."
    th "Oh. Hehehe. Do you want a drink?"
    mc "Uhm..."
    hide talksadhappymc
    show sadsmileth
    mc "{i}I don't feel like drinking in a place like this. But if I say that out loud, I'll probably hurt her feelings."
    show talksadhappymc
    mc "Yeah, ok."
    show talkhth
    th "Great! Take a seat, I'll bring you your drink."
    mc "Alright."
    hide sadsmileth
    hide talksth
    hide talkhth with easeoutleft
    "Thea runs off to the back of the tavern and out of your vision."
    hide talksadhappymc
    mc "Huh, she didn't even ask me what drink I'll be having."
    mc "I guess they serve only one kind of drink."
    scene tavern with fade
    "You look around and all you see are big, mean looking men sitting on the tables around you."
    mc "I can't believe Thea's been working here all this time."
    mc "It's no wonder Sander doesn't like this place."
    play sound glass
    "Suddenly, you hear the sound of a plate shattering."
    "Unknown" "Hahaha! What the fuck?! Why the hell is this bitch so jumpy?!"
    "You turn around and see Thea on the floor and a big man standing in front of her."
    mc "{i}Thea!"

    scene thug with fade
    show thug1
    "Unknown" "I just touched your ass, girl!"
    "Unknown" "And look what you've done, you've spilled my drink!"
    scene theaprotect
    th "I-I'm sorry, sir, I-I'll bring you another r-right away."
    "Unknown" "Oh, you don't need to do that, sweet girl. How about you repay the drink in anoth-"
    show theaprotect1 with easeinright
    mc "Hey, fucker! Get away from her!"
    "Unknown" "What? Who the hell are you?"
    mc "None of your business. Now lay off her!"
    th "[mc]!"
    play sound punch
    hide theaprotect1 with vpunch

    "The man kicks you in the stomach."
    "All the air leaves your lungs as you fall to the ground."
    scene thug
    show thug1
    "Unknown" "Listen here, ya' little shit! I can do whatever the fuck I want!"
    "Unknown" "Back in my town, tavern wenches would be all over me before I would do anything. The lady wants me and you know it."
    scene theaprotect
    pause
    mc "...Hrgh..."
    show theaprotect1 with dissolve
    mc "She..."
    show theaprotect2 with dissolve
    mc "She... doesn't like brainless muscleheaded pricks like you!"
    play music battlemusic1
    "Unknown" "Why you little-!"
    play sound punch
    hide theaprotect1
    hide theaprotect2 with hpunch
    "A hard punch to your face puts you on the ground once more."
    th "Please! Stop this!"
    scene thug
    show thug1
    "Unknown" "Looks like your boyfriend's done!"
    "Unknown" "Come on, hero! Get up! Is that all you got?!"
    "Unknown" "I'm standing right here! Gimme your best shot!"
    hide thug1
    stop music
    play sound punch
    show thug2 with hpunch

    "{b}OOOOAAAAAFFFFFF—!!!{/b}"

    hide thug2
    show thug3
    show thug4
    pause 0.005
    hide thug3
    pause 0.9
    play sound crash
    stop music
    show thug4 with hpunch
    mc "Huh?"
    hide thug4 with easeoutleft
    pause
    scene meganpunch1 with fade
    mc "Th-Thanks."
    scene meganpunch2 with dissolve
    pause
    scene meganpunch3 with dissolve
    "The woman walks out of the tavern before you can say anything."
    mc "{i}Who was that?"
    scene tavern with fade
    show angrynmc
    show cryth
    th "[mc]! Are you alright?"
    mc "Y-Yeah, I'm fine."
    mc "Come on, let's get out of here."
    scene tavern with fade
    "An old fat man comes forward."
    "{color=#fff}Old Fat Man" "What the hell happened here?! Why is there a person stuck in my wall?!"
    "{color=#fff}Old Fat Man" "And you, where the hell do you think you're going?! Clean up this mess right now!"
    th "I-I'll be back in-"
    mc "Is he the owner?"
    "{color=#fff}Tavern Owner" "Yes, I'm the owner of this fine establishment. What's your problem, boy? Are you to blame for all of this?"
    mc "Didn't you see what just happened? Why do you let your employees get treated like this?"
    "{color=#fff}Tavern Owner" "This is a tavern, boy. And she is a tavern wench. Dealing with people like that is a part of the job."
    mc "Well, she's not gonna be a tavern wench anymore."
    "{color=#fff}Tavern Owner" "What?!"
    th "[mc], what are you doing?"
    mc "You don't need to work in a place like this."
    th "B-But-"
    mc "Come on, let's go."
    th "......"
    th "Alright."
    "{color=#fff}Tavern Owner" "HEY! You can't just walk off with my tavern wench!"
    mc "Yeah, well, FUCK YOU!"
    scene villagen with fade
    "The two of you go home."
    scene homenight with fade
    show worriedth
    show angrynmc
    th  "[mc], please sit. I'll go tend to your wound."
    mc "It's ok, Thea. Doesn't hurt that much, really."
    "As soon as Thea's hand caresses your cheek, a sharp sting runs across your face."
    mc "Ooowww...!"
    show gambaruth

    th "See? Stay there, I'll be right back."

    hide worriedth
    hide gambaruth with easeoutright

    mc "Fine."
    scene homenight with fade
    "You sit on your bed."
    mc "Aagh, my whole body hurts... That asshole."
    mc "At least he got what he deserved. Who was that woman?"
    "Thea comes into the room with a cloth and a small bowl with water."
    "She sits beside you."
    th "This might hurt a bit."
    play music nurture
    scene theawound2 with fade
    "Thea gently wipes your cheeks with the wet cloth."
    th "What were you thinking, [mc]? He could've done a lot worse if that lady didn't show up."
    mc "He was harassing you. I couldn't just stand there and watch."
    th "He was just... doing what those stupid people always do. You overreacted, as you always do."
    mc "What?! You mean these things happen regularly?!"
    th "No, not regularly, just sometimes. They aren't as serious as you think."
    th "Those guys may look tough but they're only talk."
    mc "B-But... why didn't you tell me about these things?"
    th "I-I don't know."
    th "I thought you might not let me go there again if I told you about it."
    mc "Of course I won't! How do you work at a place like that?"
    th "I-It's not that bad."
    mc "Not unless you get taken advantage of."
    mc "Imagine being raped, mentally scarred from all that torture? And right after you've lost everything?"
    th "...I... do know."
    mc "{i}Sigh{/i} ...Why do you work there, Thea?"
    th "......"
    th "It was the only place where I could get a job."
    mc "What?"
    th "All the other places I went to didn't take me. How can you blame them?"
    th "How could they give a job to a girl from another village who they know nothing about?"
    mc "You could've just told me this, without going to work at a place like that."
    th "I-I..."
    th "I-I... Couldn't trouble you with my problems anymore, [mc]. You've done so much for me."
    mc "I'll keep doing everything I can to make you happy. You know that, Thea."
    mc "You're my responsibility. Never again will I'll let you suffer another memory like that."
    th "......"
    mc "I love you."
    th "Wh-What?"
    show theawound3 with dissolve
    mc "I love you, Thea."
    th "......"
    scene theawound1 with dissolve
    th "......"
    "Thea kisses you."
    th "I love you too, [mc]. From the day that you came back for me at Yorkel."
    th "I wanted to tell you so bad."
    mc "It's ok, Thea."
    "The two of you kiss passionately. You pin Thea to the bed."
    scene theawound4 with dissolve
    pause 0.3
    scene theastare1 with vpunch
    pause
    th "...It's getting hot."
    mc "Why don't we do this then?"
    menu:
        "Take off her top.":
            "You remove Thea's top."

    th "[mc]..."
    mc "You're beautiful, Thea."
    th "Th-Thank you."
    th "......"
    scene theastare2 with dissolve
    th "Why am I the only one undressed. It's kinda embarrassing."
    mc "Sorry."
    "You remove your shirt as well."
    stop music fadeout 3.0
    scene theas1 with fade

    pause
    window hide
    play music night
    th "......"
    th "Down there... you're... thing is hard."
    mc "I-I can't help it."
    th "......"
    th "Do you want to...?"
    mc "What?"
    th "...Have sex."
    mc "Yes!"
    th "Wa... Wait, th-that was a fast response."
    mc "Don't you want to?"
    th "......"
    th "...I-I don't know. I've never... done it before."
    mc "It's ok if you don't want to."
    th "......"
    th "No, let's do it."
    mc "Are you sure?"
    th "I... can't leave you like this."
    mc "......"
    scene theas2 with dissolve
    pause
    th "P-Please be gentle, it's my first time."
    mc "Don't worry."
    scene theas3 with dissolve
    pause
    th "Ooff... ok."
    mc "I'm going to start moving."
    th "W-Wait..."
    th "I feel like throwing up."
    mc "Just relax..."
    th "Ok."
    "Thea takes a deep breath."
    th "......"
    mc "Are you alright?"
    th "Yeah... yeah."
    th "Y-You can start moving now."
    show theas movie
    pause
    th "Ahhhh..."
    mc "{i}So tight!"
    th "...Aaahhhhh..."
    pause
    menu:
        "Ask if she's ok.":
            mc "You're doing ok, right?"
            pause
            th "...Y-Yeah."
            th "It hurts..."
            th "But it also... feels good at the same time..."
            mc "I-It'll get better..."
            mc "I'm going to go a bit faster."
            th "Aahhh... A-Alright."
            "You pick up the pace."
            th "Aaaahhhhhhh...!"
            pause
        "Just keep fucking her.":
            "You pick up the pace."
            th "Aaaahhhhhhh...!"
            pause
    hide theas movie
    show theas2 movie
    th "It's starting to..."
    th "Feel good!"
    th "...Aaahhhh... Aaahhhh!"
    mc "I'm almost there..."
    th "Aaahhhh... W-Whaa-?"
    mc "I'm going to cum."
    th "Aaahhhh... oh... ok."
    mc "Can I do it inside?"
    th "Aaahhh... do... whaaa-?"
    mc "{i}She's totally out of it."
    mc "Cum... inside."
    th "Do it..."
    th "...inside, [mc]... I want... to make you happy!"
    mc "Urrgghh!"
    mc "I'm cumming!"
    scene theascum with flash
    pause 0.2
    scene theascum with flash
    pause 0.2
    scene theascum with flash
    pause 0.2
    th "Aaaaaaahhhhhh!!!"
    mc "{i}Pant... pant... pant..."
    scene theassleep with fade
    th "Haaaaah..."
    th "That felt... really good."
    mc "Yeah, it did."
    th "I'm so happy, [mc]."
    mc "...Me too."
    mc "......"
    mc "Hey, Thea."
    th "Hmmm?"
    mc "You are going to quit your job at the tavern, right?"
    show theassleep2 with dissolve
    th "B-But how am I supposed to pay rent without a job?"
    mc "You don't need to."
    mc "I mean, y-you're not a tenant anymore."
    hide theassleep2 with dissolve
    $ persistent.theaFirstTime = True
    th "......"
    th "I still have to support you..."
    mc "......"
    mc "I'll find another job for you then."
    th "But I went to all the places I could think of."
    mc "Hmmm, how about the Adventurer's Guild?"
    show theassleep2 with dissolve
    th "You want me... to become an adventurer?"
    mc "No. The Guild has a bar."
    mc "You could do you're same job at a better place."
    hide theassleep2
    th "That would be great!"
    mc "I'll ask July tomorrow."
    th "Thank you, [mc]!"
    mc "You're welcome."
    mc "Now, go to sleep."
    mc "It's been a long day."
    th "Y-Yeah."
    th "Goodnight."
    mc "Goodnight."
    scene black with fade
    show text "{color=#fff}End of day [day]." at truecenter
    with dissolve
    pause
    hide text with dissolve
    call sleepvars from _call_sleepvars_9
    $ theasex += 1
    $ theaguildjob += 1
    jump home


label theasexy:
            hide screen hud
            scene theassleep with fade
            pause
            th "You're very comfy, [mc]."
            mc "Hehehe, thanks."
            menu:
                "Have sex":
                    mc "Mind having some fun before going to sleep?"
                    th "Ohh, ok."
                    th "You just can't resist me, can you?"
                    mc "Come here."
                    show theas movie with fade
                    pause
                    window hide
                    th "Ahhhhh!"
                    pause
                    th "Ahhh... ahhh!"
                    pause
                    mc "I'm going to cum..."
                    th "Me too"
                    scene theascum with flash
                    pause 0.2
                    scene theascum with flash
                    pause 0.2
                    scene theascum with flash
                    pause 0.2
                    th "Ahhhhh!"
                    scene theassleep with fade
                    th "Haaaah... I'll never get tired of that."
                    mc "Me too."
                    scene black with fade
                    show text "{color=#fff}End of day [day]." at truecenter
                    with dissolve
                    pause
                    hide text with dissolve
                    call sleepvars from _call_sleepvars_10
                    jump home
                "Just sleep.":
                    mc "Good night."
                    th "...Good night."
                    scene black with fade
                    show text "{color=#fff}End of day [day]." at truecenter
                    with dissolve
                    pause
                    hide text with dissolve
                    call sleepvars from _call_sleepvars_11
                    jump home
                "Confess about Cynthia." if cynthdate >= 1 and thcynthconfess == 0:
                    mc "{i}Here goes nothing."
                    mc "Thea, I have something to say."
                    th "Uhm... What is it?"
                    mc "...{p}..."
                    mc "{i}Come on, say it."
                    th "[mc]?"
                    mc "I... I slept with cynthia."
                    th "......"
                    mc "I'm sorry Thea... I-I'm such a bastard."
                    th "Do you love her?"
                    mc "......{p}Yes."
                    th "...Do you love me?"
                    mc "Yes!"
                    th "Then that's what matters."
                    mc "Wait... You're not mad?"
                    th "I love you, [mc]. The things you've done for me... I just can't think of anyone who has cared more for me."
                    th "I... don't feel like I have the right to control you."
                    th "I don't want you to think of me as some kind shackle that prevents you from being with anyone else. I love you no matter what."
                    th "And if you love me, I don't know why you're so worried about it."
                    th "Cynthia is a really nice person and she cares about you a lot. I'm happy for both of you."
                    mc "..."
                    mc "......"
                    th "What?"
                    mc "I-I don't know what to say..."
                    th "You don't have to say anything... The fact that you told me the truth means you care about me. You already said what you had to."
                    mc "I'm sorry..."
                    th "I told you I'm fine..."
                    mc "I love you, Thea."
                    th "I love you too..."
                    "......"
                    th "Does cynthia know about us?"
                    mc "...No."
                    th "Are you going to tell her?"
                    mc "...I dont know."
                    th "......{p}You'll do the right thing."
                    mc "......"
                    "The two of you fall asleep. Her reaction makes you feel conflicted."
                    "Tonight, you don't sleep as well as you wanted to."
                    scene black with fade
                    $ thcynthconfess += 1
                    show text "{color=#fff}End of day [day]." at truecenter
                    with dissolve
                    pause
                    hide text with dissolve
                    call sleepvars from _call_sleepvars_12
                    jump home
            return
