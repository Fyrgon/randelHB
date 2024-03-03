default talkedWithThea = 0

label theaMenu:
if time == 4 and theagotjob == 1 and TheaMolest == True and theanight == False:
    mc "{i}It's been a while since Thea came back from work. She must be tired."
    mc "{i}She must be sleeping like log."
    mc "{i}......"
    mc "{i}A beautiful log."
    mc "{i}Hah..."
    mc "{i}No, what the hell am I thinking? I shouldn't a perv."
    "..."
    "......"
    "{i}Or should you?"
    menu:
        "No.":
            mc "{i}No! [mc], you're better than this! You're not a sick pervert who molests innocent girls at night!"
            mc "{i}Just sleep, dammit!"
            $ TheaMolest = False
            jump home
        "Go into Thea's room":
            mc "I can't resist."
            mc "I need to see her..."
            "You slowly creep into Thea's room."
            mc "What do I do if she isn't asleep? How will I explain this..."
            $ theanight = True
            jump theanight
menu:
        "Sleep with Thea" if time == 4 and theasex > 0:
            jump theasexy

        "Peep on Thea" if theanight == True and TheaMolest == True and time == 4:
            hide screen hud
            mc "{i}She's sound asleep."
            jump theanight

        "Talk with Thea" if thealive == 1 and theaintro == 1 and time < 4:
            hide screen hud
            if theadinner == 2 and time == 3:
                jump beforetheDinnerwithjustThea
            if theagotjob == 1 and time == 3:
                mc "{i}She's at work."
                jump home
            if thearuntimer > 0:
                jump theagrave
            if  punchtriss == 1 and thealives ==  1:
                show talkwamc
                show talksadhappymc
                show sadnth
                show blackeye
                mc "Hi."
                show worriedth
                th "Oh, [mc], what happened to your face?"
                hide worriedth
                hide talkhappymc
                mc "Huh, oh, it's nothing..."
                mc "I just kinda fell."
                th "Let me look at it."
                "Thea gently inspects your eye."
                show worriedth
                th "Does it hurt?"
                mc "Nah, I'm fine. It might just heal itself."
                th "Wait, I think I have some herbs for this. I plucked some earlier to make some soup. There might be some left."
                th "I'll go check, wait here."
                "Thea runs to the kitchen, and after a while, she comes back with some grinded leaves."
                th "We're in luck! There were some herbs left. Now, stay still."
                show black with fade
                "Thea carefully applies the medicine around your black eye."
                $ punchtriss -= 1
                hide black
                show smilemc
                show talksth
                th "There, that's better."
                mc "Wow, that helped a lot. Thanks, Thea."
                th "No problem."
                show gambaruth
                th "Be more careful next time!"
                mc "Yeah, alright, mom."
                show talknth
                th "Hehe."
                jump home
            jump theaTalkHome

        "Have dinner with Thea" if time == 4 and thealives >= 1:
                hide screen hud
                if seconddinnerthea >= 1:
                    scene theadinner with fade
                    "The two of you have dinner."
                    scene mctheawash with fade
                    "The two of you talk about your day."
                    if thcynthconfess == 4:
                        mc "{i}She seems pretty normal."
                        mc "{i}I guess I was overreacting."
                        mc "{i}Or she could be really good at hiding her intentions."
                        mc "......"
                        mc "{i}there it is, I'm overreacting again."
                        mc "{i}Relax, [mc]. Thea is not going to kill you."
                        mc "{i}Thea is not going to kill you"
                    jump sleeping
                if petesawthea > 1:
                    scene theadinner with fade
                    mc "Whew, I'm done."
                    th "If you keep eating like that you might get fat."
                    th "And it'll be my fault at the end."
                    mc "Nah, don't worry. I stay in shape, it'll be fine."
                    th "Buut you do look like you've gained a few pounds."
                    mc "Are you serious?"
                    th "I am."
                    "You take a look at yourself."
                    mc "I don't think so."
                    th "Hmm... To me you have."
                    th "I'll have to reduce the amount of food I'm preparing hear after."
                    mc "What? Noooo!"
                    th "Sorry, [mc]. This is for your own good."
                    mc "{i}Sigh...{/i} fine."
                    th "Good."
                    mc "......"
                    mc "Alright, lets go to sleep then. It's getting late."
                    th "Yeah."
                    "The two of you wash your plates and go to sleep."
                    mc "Good night."
                    th "Good night."
                    $ seconddinnerthea += 1
                    jump sleeping
                if firstdinnerthea > 0:
                    scene theadinner with fade
                    "The two of you have dinner. You have a small conversation but it's still awkward as usual."
                    mc "Good night"
                    th "Good night"
                    jump sleeping
                scene theadinner with fade
                mc "Whew... I'm full."
                mc "The food was really great."
                th "I'm glad you liked it. I wanted to make something special, to thank you... For letting me stay, in your home."
                menu:
                    "Be cheesy":
                        mc "Our home, now."
                        th "Oh... yes, our home."
                        mc "{i}She's blushing! man, is being cheesy this effective against women?"
                    "Don't":
                        mc "{i}Let's not be cheesy."
                        mc "Then I guess I made a good choice, hah."
                        "Thea smiles politely."
                "..."
                "......"
                th "so... Uhm... How was your day?"
                mc "Uhm, it was fine. Nothing really special."
                th "Oh, ok."
                mc "..."
                mc "How was yours?"
                th "Mine?"
                th "Same as yours really."
                mc "Oh, ok."
                mc "......"
                th "......"
                mc "{i}This is getting akward, what am I supposed to say?"
                mc "How are you liking the house? "
                th "I-I really like it."
                th "......"
                mc "{i}Come on, Thea, give me something to work with."
                th "......"
                mc "{i}It's no use."
                mc "I'll be going to bed, it's getting late."
                th "Oh, alright."
                th "Leave your plate at the table, I'll wash it."
                mc "I'll wash it, don't worry."
                th "O-Ok."
                "You wash your plate."
                mc "Goodnight."
                th "Goodnight."
                $ firstdinnerthea += 1
                jump sleeping

        "Tell Thea about the job" if theaguildjob == 2 :
            mc "Thea, I got good news. You got the job."
            th "Really?!"
            mc "Yes!"
            "Thea gives you a tight hug."
            th "Oh, thank you, [mc]."
            mc "She told me you can come in the evenings."
            th "Alright."
            th "Oooh, I can't wait! I'm a bit nervous actually."
            mc "Don't worry, you'll do great."
            th "I hope so. Thanks, [mc]."
            mc "You're welcome."
            $ theaguildjob += 1
            jump home

        "{color=#ff0000}Dinner with Sander and Eve{/color}" if time == 0 and petedinner == 1 and sequest1 == 0 :
            "Complete Sander and Eve's quest."
            jump home
        "Dinner with Sander and Eve" if time == 0 and petedinner == 1 and sequest1 == 1 and sanderevedinner < 1:
            if money < 50:
                mc "{i}Thea said she would need 50 gold. I'll have to get that first."
            $ money -= 50
            mc "Here Thea, the money for tonight."
            th "Ah yes, thank you. I'll buy everything on my way home from work."
            mc "Ok, then I'll send them a letter."
            th "Alright."
            scene mcroom with fade
            "You take a piece of paper and start writing."
            mc "{i}I better send it to Eve. Not sure if Sander knows how to read."
            "You finish writing the letter and give it to your messenger pigeon."
            mc "Take this to the Adventurer's Guild."
            $ sanderevedinner += 1
            "The bird flies away."
            jump home

        "{color=#ff0000}Dinner with Sander and Pete.{/color}" if sanderpetedinner == 0  and time == 0 and sanderevedinner == 2 and showpetebadge == 0:
            "Show your Bronze badge to Uncle Pete."
            jump home
        "Dinner with Sander and Pete" if sanderpetedinner == 0  and time ==0 and sanderevedinner == 2 and showpetebadge == 1:
            if money < 50:
                mc "{i}I still need 50 gold."
                jump home
            mc "Here Thea, the money for tonight."
            th "Ah yes, thank you. Who are we inviting today?"
            mc "I thought of inviting Uncle Pete and Sander."
            th "Oh, alright. I'll bring the groceries while coming home from work."
            th "Alright."
            scene mcroom with fade
            "You take a piece of paper and start writing."
            mc "{i}Uncle Pete said he wanted to meet Sander."
            "You finish writing the letter and give it to your messenger pigeon."
            mc "Take one to the Adventurer's Guild and the other to Uncle Pete."
            $ sanderpetedinner += 1
            "The bird flies away."
            jump home




label theaTalkHome:
show smilemc
show normalth
show talkhappymc
if time == 0:
    mc "Good morning!"
    show talknth
    th "Good morning, [mc]."
menu:
    #"Have a quick chat.":
        #if talkedWithThea == 0:
        #    "a"
        #if talkedWithThea == 1:
        #    "a"
        #if talkedWithThea > 1:
        #    "a"
        #$ talkedWithThea += 1
        #jump home
    "Special Dinner with Thea" if sanderpetedinner == 2 and theadinner < 2:
        jump theainvite
    "Nothing":
        mc "Just wanted to check on you. You doing ok?"
        th "Yeah."
        mc "See you later then!"
        th "Bye, [mc]."
        jump home














label theanight:
    scene sleeptheabase
    show blancketth
    menu:
        "Pull down the sheets":
            $ pants = 1
            $ bra = 1
            $ panties = 1
            hide blancketth
            show brath
            show pantiesth
            show pantsth
            pause
            mc "Wow... Beautiful, shiny legs."
            window hide
            jump molest
        "Leave":
            mc "I don't feel like it now."
            jump home
label molest:
    menu:
        "Pull down her pants" if pants == 1:
            mc "{i}Please don't wake up..."
            if stealthlvl < 1:
                mc "Shit, she's waking up. I better leave."
                show blancketth
                pause
                $ time += 1
                jump home
            $ pants -= 1
            hide pantsth with dissolve
            pause
            mc "Damnit, she has underwear on. She must've bought them."
            jump molest
        "Pull down her panties" if pants == 0 and panties == 1:
            if stealthlvl < 2:
                mc "Shit, she's waking up. I better leave."
                show blancketth
                pause 1
                $ time += 1
                jump home
            $ panties -= 1
            hide pantiesth with dissolve
            $ persistent.theaNakedSleep = True
            pause
            mc "Cant believe I'm doing this..."
            jump molest
        "Finger her pussy" if panties == 0:
            if stealthlvl < 3:
                mc "Shit, she's waking up. I better leave."
                show blancketth
                pause
                $ time += 1
                jump home
            show animationfinger
            show sleeptheabase2 with dissolve
            pause
            mc "She likes it."
            pause
            mc "Her pussy is sucking my fingers in!"
            menu:
                "Faster":
                    mc "Time to go faster."
                    hide animationfinger
                    show animationfingerfast
                    pause
            show sleeptheabase3 with vpunch
            pause 1
            mc "She came!"
            hide animationfinger
            hide animationfingerfast
            mc "Looks like she's waking up. I better leave."
            show blancketth
            pause 1
            $ time += 1
            jump home
        "Remove her bra" if bra == 1:
            if stealthlvl < 1:
                mc "Shit, she's waking up. I better leave."
                show blancketth
                pause 1
                $ time += 1
                jump home
            $ bra -= 1
            hide brath with dissolve
            pause
            mc "Her boobs are so perfect."
            jump molest
        "Touch her breasts" if bra == 0:
            if stealthlvl < 3:
                mc "Shit, she's waking up. I better leave."
                $ time += 1
                jump home
            show sleeptheabase2 with dissolve
            show animationboobhand
            pause
            mc "She likes it."
            mc "I guess her tits are really sensitive."
            pause
            mc "Sooooo soft..."
            pause
            hide animationboobhand
            show sleeptheabase3 with vpunch
            mc "Did she just cum?"
            hide animationboobhand
            mc "Looks like she's waking up. I better leave."
            show blancketth
            pause
            $ time += 1
            jump home
        "Rub one off":
            mc "My dick feels like it's gonna explode... Must... release..."
            show animationfap
            pause
            mc "I'm gonna cum...!"
            hide animationfap
            show cumth with vpunch
            show fap1
            pause
            hide cumth with dissolve
            mc "Oh yeah, that felt great..."
            hide fap1
            show blancketth
            pause
            $ time += 1
            jump home
        "Go back":
            show blancketth
            pause
            jump home
    return
