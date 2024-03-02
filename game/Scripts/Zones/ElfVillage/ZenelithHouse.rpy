default needOrb = False

label zenelithHouse:
    $ gameover = "zenelithHouse"
    hide screen hud
    if bothpath == 1:
        mc "It's locked! I guess no one's there."
        jump elfVillage
    if bothpath == 2:
        mc "It's locked. How do I get in?"
        mc "There has to be a key... But how do I find it? And there's no way Zenelith is giving it to me."
        mc "If only there was a way I could get in without that key. I could break down the door, but that would cause a whole lot of other problems."
        mc "This is related to the Village security. I should talk to Nessa, she has to know a way."
        jump elfVillage
    if bothpath == 3:
        jump bothpath3
    if bothpath >= 4:
        jump bothpath4
    return
