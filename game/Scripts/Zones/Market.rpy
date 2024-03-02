label market:
    hide screen screenmap
    if time >= 4:
        scene villagen
        mc "It's too late to be here."
        jump maplimbo
    scene villageback

    if loriEventValue == 9 and loriDateDate == day and time == 2:
        jump lori9

    if marketDebt > 0:
        mc "{i}Before I go buy anything I should probably pay my debt back..."

    if TaliyaQ == 2:
        jump TaliyaQ2

    if TaliyaQ == 3 and penepisellosessoomosessuale == True and time == 0:
        jump TaliyaQ3b

    if Q4Pre == True and TaliyaQ == 4 and time == 0:
        jump TaliyaQ4

    if time == 0 and TaliyaQ == 5:
        jump TaliyaQ5
    menu:
        "Go to the tavern" if time == 3 and theadinner == 3:
            jump theafirsttime
        "Go buy Zenelith a dress" if zenQ == 2 and Zdress == False and marketDebt <= 0:
            mc "{i}Let's find a new dress for her..."
            "You walk around the market for a while. You see many nice dresses, but a lot of them definitely wouldn't fit on her."
            "Then you see a blue dress that looks exactly her size. You approach the seller."
            mc "How much is that?"
            "{color=#fff}Tailor" "It's 15 gold."
            if money < 15:
                mc "{i}Astylla damn it, I don't have that much on me."
                mc "Is it fine if I come back later? I don't have enough money for that right now."
                "{color=#fff}Tailor" "Alright."
                jump market
            mc "Here's the money."
            "{color=#fff}Tailor" "Thank you very much."
            "You give the tailor the money and take the dress with you."
            $ Zdress = True
            $ money -= 15
            jump market
        "Go buy furniture for the shack" if zenQ == 2 and furnitureZ == False and marketDebt <= 0:
            scene furnitureshop with fade
            "You find a store that sells furniture and you go inside. After inspecting the place, you decide what to buy."
            "{color=#fff}Furniture Maker" "It's 120 gold in total."
            if money < 120:
                mc "{i}120?! I don't have that much!"
                mc "Alright, I'll come back for them, don't sell them until then, alright?"
                "{color=#fff}Furniture Maker" "Alright."
                jump market
            mc "Alright, here's the money."
            "You pay the furniture maker."
            "{color=#fff}Furniture Maker" "You need any help moving this stuff? It's quite heavy."
            mc "Oh, don't worry about that."
            "You cast the spell Scarlet taught you and suddenly the table is a lot lighter that you can easily lift it with one hand."
            "{color=#fff}Furniture Maker" "What the-"
            mc "Hehe. Alright then, see you."
            $ furnitureZ = True
            $ money -= 120
            jump market
        "Pay the debts back" if marketDebt > 0:
            if money < marketDebt:
                mc "{i}Wait, I don't have enough money... I need [marketDebt] gp. Better go get some."
                jump home
            "You go pay the people with whom you had debts."
            mc "{i}Alright. Debts paid."
            $ money = money-marketDebt
            $ marketDebt = 0
            jump market
        "Buy a bed" if zenmattress == False and asked4gift == True:
            if scarlettaughtthatonespell == False:
                "You wander around the Market for some time. You haven't really ever went shopping for beds or bedding before in your life."
                "After a few minutes you find someone selling a few mattresses, you go to buy one, but then you stop."
                mc "{i}Wait, how am I going to take a mattress all the way through the forest?"
                mc "{i}I can't just carry it over my shoulder the whole way through..."
                mc "{i}I could use a mule, but... I don't have one, they're expensive, and I'm not going to buy one just for this."
                stop music fadeout 2
                mc "{i}Maybe Scarlet knows a spell that could be useful for this! Maybe there's a spell that can make stuff smaller or something..."
                play music academy fadein 1
                scene lecturemage2 with fade
                "You decide to go to the Academy, and there you find Scarlet. She's almost done with her class, so you wait outside."
                pause 1
                scene lecturemage1 with fade
                stop music fadeout 3
                "Once the class is done you walk in."
                show normalm
                show prot normal
                mc "Hey, Scarlet."
                s "Hey, [mc], what's up?"
                mc "Is there any spell that can make objects smaller?"
                s "Not any useful for whatever you want to use it for."
                mc "Wha- How can you know that?"
                s "The only one I know of requires an immense amount of energy and also doesn't allow you to move the object that has been made smaller, its uses are very reduced."
                mc "Damn it..."
                s "Why you ask?"
                mc "Uhm... Stuff."
                s "Stuff, huh? Alright there might still be a way for me to help you, anyways."
                mc "Really? How?"
                s "There's a spell that can make objects lighter, it's not the same but it would still be useful, wouldn't it?"
                mc "Oh, yeah! Definitely!"
                s "Alright then, let me teach it to you."
                scene black with fade
                show text "{color=#fff}Scarlet teaches you the spell." at truecenter
                pause 1
                $ scarlettaughtthatonespell = True
                scene lecturemage1 with fade
                hide text
                mc "Thanks a lot, Scarlet!"
                s "No problem."
                stop music fadeout 1
                scene villageback
                play music tavern
                "You go to where you found the mattress earlier and ask for the price."
                "{color=#fff}Shopkeeper" "It's 20 pieces."
                if money < 20:
                    mc "{i}I don't have that much..."
                    mc "Alright, I'll come back with the money."
                    jump home
                else:
                    mc "Alright, here's the money."
                    $ money -= 20
                    "You pay the shopkeeper and take the mattress. You use the spell Scarlet taught you to make it lighter, and then roll it and tie it so that it's easier to carry."
                    $ zenmattress = True
            else:
                "You go back to the shopkeeper to buy the mattress."
                "{color=#fff}Shopkeeper" "It's 20 pieces."
                if money < 20:
                    mc "{i}I still don't have that much..."
                    mc "Alright, I'll come back with the money."
                    "{color=#fff}Shopkeeper" "I hope so."
                    jump home
                else:
                    mc "Alright, here's the money."
                    $ money -= 20
                    "You pay the shopkeeper and take the mattress. You use the spell Scarlet taught you to make it lighter, and then roll it and tie it so that it's easier to carry."
                    $ zenmattress = True
    mc "I have nothing to do here right now."
    jump maplimbo
    scene villageback
