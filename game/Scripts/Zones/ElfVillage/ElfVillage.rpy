label elfvillage:
    stop music
    show screen hud
    if time > 2:
        scene elfvillagen
        play music night
    else:
        play music home
        scene elfvillage


    if savedaerin == 1 and sawaerinelder == 0:
        mc "I should go see Aerin. She said she was in the temple."

    if evelost == 1 and sawaerinelder == 0:
        jump aerinkiss

    if aerinlost == 1 and aerindead == 0:
        jump aerinbadend

    if bothpath > 6 and savedaerin == 0:
        jump ElfGoodEnding

    if metpriest == 0 and bothpath >= 1 and time == 4:
        jump meetZenelith



    menu:


        "Zenelith's house" if bothpath >= 1 and savedaerin == 0:
            jump zenelithHouse



        "Graveyard":
            jump elfGraveyard


        "Eve's house" if savedaerin == 0 and aerinlost == 0 and evelost == 0:
            jump eveHouse


        "Temple":
            jump elfTemple


        "Aerin's house" if sawaerin >= 2 and dumpaerin == 0 and savedaerin == 0 and aerindead == 0:
            jump aerinHouse


        "Prison":
            jump elfPrison


        "Head back to Randel":
            if time == 4:
                jump home
            jump forest
