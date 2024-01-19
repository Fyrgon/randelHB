default metMerv = False

label store:
    if time > 3:
        scene villagen
        mc "{i}It's too late to go there"
        jump maplimbo
    hide screen screenmap
    play music home
    scene mervins1
    if metMerv == False:
        me "Welcome to Mervin's Trading Center."
        mc "And... what are you supposed to be selling?"
        me "Anything."
        mc "Anything?"
        me "Correct."
        mc "So where's all the stuff?"
        me "In the pot."
        mc "In the pot?"
        me "Yeah. Tell me what you want and I will give it to you for the best price."
        mc "I see. Is that like a magic pot or something?"
        me "Listen kid, if you wanna buy something, do it or scram."
        mc "Ok, ok, sheesh."
        $ metMerv = True
    me "What would you like to buy? I have everything you need."
    menu:

        "Buy some books for Zenelith" if asked4gift == True and zenbooks == False:
                mc "Do you happen to sell books as well?"
                me "Of course. What kind of book are you looking for?"
                mc "Anything an elf would enjoy reading."
                me "Tough one, kid. I'll see what I have."
                scene mervins2 with dissolve
                me "Alright, for these it's 40 silver."
                if money < 40:
                    mc "Oh, damn it, I don't have enough silver."
                    me "That's a shame, kid. But you can always come back when you got enough."
                    mc "You're right, see you then."
                    jump store
                else:
                    mc "Gotcha. Here's the money."
                    $ money -= 40
                    me "Here's your books, young lad. Pleasure doing business with ya."
                    $ zenbooks = True
                    jump store

        "Buy Zenelith a bed" if zenmattress == False and asked4gift == True:
            mc "This might sound stupid but do you happen to have a bed?"
            me "..."
            mc "What?"
            me "I don't have anything that wouldn't fit inside the pot."
            mc "That includes a bed."
            me "It includes the bed, yes."
            mc "Alright, I'll go look somewhere else."
            mc "{i}Guess the Market might be a better place..."
            jump store

        "Buy wine" if theadinner == 1 and iwine == 0:
            mc "Can I buy some wine?"
            me "Of course. What kind of wine are you looking for?"
            me "We got here some Dornish white wine if you're looking for something fancy. Or you could just buy the normal cheap wine, your pick."
            mc "Hmmm..."
            menu:
                "Buy cheap wine (10 silver)":
                    if money < 10:
                        mc "I don't have enough money. I'll come back later."
                        jump store
                    $ money -= 10
                    mc "Give me the cheap one."
                    me "I figured, here take it. That will be 10 silver."
                    $ cheapwine += 1
                    $ iwine += 1
                    jump store

                "Buy expensive wine (150 silver)":
                    if money < 150:
                        mc "I don't have enough money. I'll come back later."
                        jump store
                    $ money -= 150
                    mc "I'll have the... Dornish one."
                    me "Excellent choice. For a second, I thought you were going to cheap out, heh."
                    me "Here you go."
                    scene mervins2 with dissolve
                    show igoodwine with dissolve
                    pause
                    hide igoodwine with dissolve
                    mc "Thanks."
                    $ goodwine += 1
                    $ iwine += 1
                    jump store

        "A gift for Gabe" if dildoi == 0 and gabefingerclass == 1:
            mc "Do you have... something that can, uhm, pleasure women?"
            me "Huh, you don't have one?"
            me "I could give you one but I don't know how you'd attach it to yourself."
            mc "What? No! I mean something like a sex toy."
            mc "I've herd there's something called a {b}dildo."
            me "Oh yes, yes, I have it. A fancy toy that is, only rich ladies use those silly contraptions."
            mc "Could I have one?"
            me "What's wrong with your pecker, boy?"
            mc "There's nothing wrong with it, It's for something else."
            me "Oh... I get ya, you want to know what it feels like, eh?"
            mc "NO!"
            mc "{i}Sigh...{/i} just tell me how much it will cost."
            me "Uhh... 1000 silver."
            mc "Come on, Mervin."
            me "......{p}998?"
            mc "Ok, bye."
            me "No wait! I'll give it for 146 silver, happy?"
            mc "Huh... ok, that's better."
            menu:
                "Buy":
                    if money < 146:
                        mc "{i}I dont have enough money."
                        mc "I'll come back later."
                        jump store
                    mc "Ok, take the money."
                    scene mervins2 with dissolve
                    me "Here's a dildo for the young man."
                    $ dildoi += 1
                    $ money -= 146
                    scene mervins1 with dissolve
                    me "Enjoy."
                    mc "...Thanks."
                    jump store
                "Later":
                    mc "I'll come back later."
                    jump store
        "Eye Orb (30 silver)" if ieyeorb < 1:
            if money >= 30:
                mc "I'd like to buy an Eye Orb"
                me "Here you go"
                scene mervins2 with dissolve
                show itemeyeorb with dissolve
                pause
                hide itemeyeorb with dissolve
                $ ieyeorb += 1
                $ goteyeorb += 1
                scene mervins1 with dissolve
                mc "Thank you."
                $ money -= 30
                me "Pleasure doing business with ya."
                if bothpath == 4:
                    mc "Ok now I have a Eye Orb, all that is left is to go in there and capture everything. Then that bitch will be done for."
                    mc "But what if I get caught while  I'm down there. I nearly got caught the last time. Should I get some help?"
                    mc "She's a strong mage! I guess I'll fight fire with fire."
                    mc "I'll have to meet Scarlet again. I hope she hasn't got tired of helping me."
                    $ bothpath += 1
                    jump store
                jump store
            mc "I dont have enough silver."
            jump store
        #"A book for lori (40 silver)" if ibooklori == 0:
           # if money >= 40:

              #  mc "i want to buy a book for lori"
              #  me "ummmmmm okay what kinda books does she like"
              #  mc "romance novels"
              # me "coming right up"
               # scene mervins2 with dissolve
              #  show ibooklori with dissolve
              #  pause
              #  hide ibooklori with dissolve
              #  $ ibooklori += 1
             #   scene mervins1 with dissolve
             #   mc "thank you"
             #   $ money -= 40
              #  me "pleasure doing business with ya"
              #  jump store
            #mc "i dont have enough silver"
           # jump store

        "Camping gear (50 silver)" if icamping < 1:
            if money >= 50:
                mc "I'm looking for some camping gear."
                me "Here you go."
                scene mervins2 with dissolve
                show campgeari with dissolve
                pause
                hide campgeari with dissolve
                $ icamping += 1
                scene mervins1 with dissolve
                mc "Thank you."
                $ money -= 50
                me "Pleasure doing business with ya."
                jump store
            mc "I dont have enough silver."
            jump store
        "A bug net (40 silver)" if ibugnet == 0:
            if money >= 40:
                mc "I want to buy a bug net."
                me "A bug net eh?"
                me "Coming right up."
                scene mervins2 with dissolve
                show ibugnet with dissolve
                pause
                hide ibugnet with dissolve
                $ ibugnet += 1
                scene mervins1 with dissolve
                mc "Thank you."
                $ money -= 40
                me "Pleasure doing business with ya."
                jump store
            mc "I dont have enough silver."
            jump store
        "Buy magical lamp(200 silver)" if magic_lamp == 0:
            if money >= 200:
                mc "I would like to buy that lamp."
                me "Oh, are you going to sneak around during the night?"
                me "Not my bussines... here you are."
                scene mervins2 with dissolve
                show magic_lamp with dissolve
                pause
                hide magic_lamp with dissolve
                $ magic_lamp = 1
                scene mervins1 with dissolve
                mc "{i}Well that was expensive but I can move around more now."
                $ money -= 200
                me "Enjoy the light just don't stare to it for too long, no complaints!"
                jump store
            mc "I dont have enough silver."
            jump store
        "Sell diamond" if diamond == 1:
            mc "Here, I've got something for you."
            "You show the diamond to Mervin."
            me "Let me see..."
            "He inspects it for a while with one hand on his chin."
            me "Hmm... this is very valuable boy, where did you get it?"
            mc "I found it while I was on a quest."
            me "A quest you say..."
            me "Ok... I'll give you 100 silver for it, whatcha say?"
            mc "100 silver? The dwarf in the cave said I could sell it for at least 200 silver."
            me "...Dont lie to me boy. This might be a valuable diamond but its not worth 200 silver!"
            menu:
                "How about 150?":
                    mc "Ok what about 150?"
                    me "...{p}......"
                    me "Ok, fine I'll give you 150."
                    mc "{i}Well, still better than 100 silver."
                    play sound chime
                    $ renpy.notify("{color=#fff}You gained 150 silver")
                    $ diamond -= 1
                    $ money += 150
                    jump store
                "Take the diamond and leave":
                    mc "Alright, give it here. I'll find some other place to sell it."
                    me "What- wait!"
                    mc "...Hm?"
                    me "Ok, what if I gave you 130 silver for it?"
                    mc "No."
                    me "150!"
                    mc "I said 200, if you can't give me that then I'll pass."
                    me "...{p}......"
                    me "Ok, fine!"
                    mc "Heh."
                    play sound chime
                    $ renpy.notify("{color=#fff}You gained 200 silver")
                    $ money += 200
                    $ diamond -= 1
                    jump store
        "Sell the Wallcrawler Heart" if wcheart == 1:
            mc "Hey there, I've got something for you."
            "You show Mervin the Wallcrawler Heart."
            me "Oh my..."
            "He looks at it for a while, trying to see if it's the real thing or a fake."
            me "Hmm... Yup, this is a Wallcrawler Heart. It's really valuable, where did you get it?"
            mc "I got it while on a quest."
            me "A quest, you say..."
            me "Alright... I'll give you 200 silver for it, whatcha say?"
            mc "{i}I have no idea if that's the actual price but it sounds like a lot of money to me."
            mc "200 silver it is."
            me "You made a good deal today, lad."
            play sound chime
            $ renpy.notify("{color=#fff}You gained 200 silver")
            $ money += 200
            $ wcheart -= 1
            jump store
        "Buy Zenelith a dress" if zenQ == 2 and Zdress == False:
            mc "Do you happen to have dresses?"
            me "I do but I have to warn you. I can't guarantee you size, color, materials, quality, origin-"
            mc "Okay, okay! I get it. I'll go look somewhere else."
            me "I'm just trying to help."
            mc "Well, thanks. I'll go then."
            mc "{i}Guess the Market might be a better place..."
            jump store
        "Buy furniture for the shack" if zenQ == 2 and furnitureZ == False:
            mc "This might sound stupid but do you have a table?"
            me "..."
            mc "What?"
            me "I don't have anything that wouldn't fit inside the pot."
            mc "That includes a table."
            me "It includes the table, yes."
            mc "Alright, I'll go look somewhere else."
            mc "{i}Guess the Market might be a better place..."
            jump store
        "Go back":
            jump maplimbo
            pause
