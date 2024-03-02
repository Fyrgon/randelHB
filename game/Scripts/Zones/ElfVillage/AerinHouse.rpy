label aerinHouse:
    stop music
    hide screen hud
    if time == 4:
        mc "I shouldn't bother her at this time."
        jump elfVillage

    if aerinQ == 2:
        jump aerin2
    if aerinQ ==3:
        jump aerin3

    scene aerinhouseblr
    show talkha
    show smilemc
    a "Oh [mc], you're back."
    mc "Hey."
    menu:
        "Talk":
            mc "I see you quite often at the elf graveyards."
            a "Oh, yeah."
            mc "Why?"
            show talksada
            a "I'm going to my brother's grave when I feel... {p}...Lonely."
            show worriedmc
            mc "I thought your brother was missing."
            a "That's what they say to make me feel better. I know he's gone. He said he would never leave me alone. He said we'd always be together until death."
            a "The reason why he isn't here is because... he's dead."
            mc "I'm sorry, Aerin."
            a "It's ok, [mc]. It still comforts me thinking about him, so I visit his grave every day."
            show shytalka
            a "Ah, sorry. I made it depressing, didn't I?"
            mc "Oh, no, no. Haha."
            show shytalkha
            a "I know, why don't we have some tea to lighten the mood?"
            show talksadhappymc
            mc "That's a good idea."
            scene teaaerin
            "You have a cup of tea and a muffin. After that, you take your leave."
            jump elfVillage
        "Leave":
            mc "Just came to check on you."
            a "Is it that or do you want more cupcakes?"
            mc "You got me."
            a "Hahaha."
            scene teaaerin
            "You have a cup of tea and a muffin. After that, you take your leave."
            jump elfVillage
    return
