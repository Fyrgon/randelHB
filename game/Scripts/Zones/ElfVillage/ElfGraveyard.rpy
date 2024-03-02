label elfGraveyard:
    stop music
    if time == 4:
        mc "It's too late to go there."
        jump elfVillage
    if aerinQ == 0 and aerinlost == 0:
        jump aerin1
    if sawegraveyard == False:
        scene elfgraves with fade
        mc "Whoa, so this is the graveyard, it looks kinda empty and, well, dead. There's not even a hundred graves here... It is a pretty small Village after all."
        mc "I wonder how old the Village is?"
        $ sawegraveyard = True
    scene elfgraves with fade
    menu:
        "Leave":
            jump elfVillage
    return
