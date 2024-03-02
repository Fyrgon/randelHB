label eveWinsDuel:
    "The both of them are now ready for battle. Zenelith stands in the center."
    zn "May the great four mothers bless the both of you. Let the duel begin!"
    scene elfduel with fade
    play music battlemusic1
    "Both Eve and Aerin are standing at their sides of the arena, waiting for the duel to start. The gong hits and both opponents start furiously running at each other, strike after strike."
    "Eve as expected has the upper hand, but Aerin does not fall much behind, she still has hope, hope that she can win. However, Eve is not going to let that happen. With one last menacing look at her opponent, she strikes."
    "The only thing you can hear is the thud of Aerin's unconscious body hitting the ground."
    scene black
    "Aerin is taken to the temple."
    stop music
    mc "{i}Eve won!"
    scene elfvillage
    show normale
    show worriedmc
    $ aerinlost += 1
    mc "Eve, congratulations! You were awesome!"
    e "Thank you, little one..."
    mc "{i}She doesn't look that happy."
    mc "So... Aerin... what's going to happen to her?"
    e "Sh... will have to leave."
    show sadtalke
    hide normale
    e "I'm sorry, [mc], but I've got to go. I'm very tired."
    hide sadtalke with easeoutright
    mc "Oh, yeah, sorry."
    mc "{i}She looks really sad. I think the fact that Aerin is getting banished still hurts her. They were friends after all."
    if aerinpath == 1 or bothpath < 3:
        # Couldn't help Aerin
        mc "{i}I couldn't help her in the end."
        mc "I should go see her."
        scene aerinhouseblr
        "As you go into Aerin's house, you see her packing up her things. The house already feels empty."
        show sada
        show worriedmc
        mc "Aerin, I-I..."
        show shytalkha
        a "It's ok, [mc]. I'm ok."
        mc "I tried my best, Aerin. I tried to find a way to help you, but... I just needed more time."
        a "[mc], I never really understood why you were so kind to me, but thank you. You were a friend to me, one of very few I have."
        mc "Where are you going to go?"
        a "There's a whole world out there."
        a "...There must be a place where I'll be accepted."
        mc "..."
        mc "Come live with me."
        a "Huh?"
        mc "You can stay in my house, I'm sure you'll like it there!"
        show shytalka
        a "I-I can't."
        mc "Please, it's ok."
        a "......"
        mc "Please, at least consider it."
        a "...Ok."
        a "You should go now, the Village guards might come here for me."
        mc "Ok."
        mc "But remember... my house is always open for you."
        a "Thank you, [mc], I'm really happy that I met you."
        scene elfvillage with fade
        mc "{i}Damn it! Why couldn't I save her?!"
        mc "{i}I hope she accepts my offer, she doesn't have to be alone!"
        scene black with fade
        "You go back to Randel. When you reach home, it's already dark."
        $ time = 4
        jump home
    elif bothpath >= 3:
        # Wanted to help them both, found Zenelith but couldn't stop her
        mc "{i}I couldn't help her in the end!"
        mc "{i}But I have to tell her about her brother!"
        mc "{i}I have to go see her."
        scene aerinhouseblr
        "As you go into Aerin's house, you see her packing up her things. The house already feels empty."
        show sada
        show worriedmc
        mc "Aerin! There's something I want to tell you."
        a "[mc]?"
        mc "Your brother! He's alive. Zenelith has him locked up."
        a "WH-WHAT?!"
        "You hear the front door open."
        mc "YOU! How did you..."
        a "Priestess Zenelith! What have you done with my brother?"
        zn "So, you told her. I knew it was you, that day. I can sense it, that dirty scent you carry."
        mc "Y-You won't get away with this!"
        zn "We'll see about that."
        a "Is my brother al-"
        "In a split second, Aerin is sent flying across the room."
        mc "AERIN!"
        "Before you have time to react, blue orbs comes and hit you. The pain is excruciating as every orb tears through your flesh and bones. Everything goes black."
        scene black
        pause 0.5
        scene gameover with fade
        pause
        return
    else:
        # Didn't want to help Aerin
        mc "{i}It's sad that Aerin has to leave."
        "You go back to Randel. When you reach home, it's already dark."
        $ time = 4
        jump home



label aerinbadend:
    $ aerindead += 1
    hide screen hud
    show thinkmc
    mc "{i}I wonder how Eve's doing?"
    show talkangryn with easeinright
    mc "Hey, Nessa where you goi-"
    n "[mc], it's Aerin!"
    mc "What!"
    n "Come quick!"
    scene black with fade
    "You follow Nessa, you can tell that she's in a hurry."
    mc "{i}What's going on?"
    scene elfgraves with fade
    play music windhowl
    "You reach the elf graves."
    "The graveyard is quieter than usual. You see Zenelith standing in the distance, you can make out another figure on the ground in front of her."
    "The both of you run to the scene."
    scene aerindead with fade
    $ persistent.aerinDead = True
    $ aerinDead = True
    if bothpath >= 1 or aerinpath == 1:
        mc "No...{p}This can't be happening!"
        mc "{i}Sh-She said... she would come with me!"
        "You are soon joined by Eve."
    else:
        mc "{i}Oh no...{p}Oh Astylla no! It's Aerin!"
        "You are soon joined by Eve."
    e "Wh... What happened?!"
    zn "I caught her trespassing. I asked her to leave, but she refused. She drew her weapon at me, so I had... no choice."
    e "No... Aerin... {i}sob{/i} ...How could you?!"
    n "{i}sob"
    e "How could you?! How could you do this to her?!"
    zn "She was trespassing."
    e "She must have come here to... see her brother's grave..."
    zn "That doesn't justify her actions."
    e "You.... YOU BITCH! {i}sob"
    e "GET OUT OF MY SIGHT!!!"
    zn "How dare you insult me!"
    e "I don't care, I'm the Elder! As such, I hereby declare you banned from this village! You will no longer be allowed here!"
    zn "That's just preposterous!"
    if bothpath >= 1 or aerinpath == 1:
        "You're unable to process what's happening around you. You're unable to utter a single word."
        mc "{i}She said... she said..."
        mc "{i}She would be ok..."
        scene black with fade
        "You don't feel anything, everything went silent. You head back to Randel without looking back, leaving the grim tragedy behind. You fall to bed as soon as you're home."
        show text " {color=#fff}I could have saved her...{/color}"
        with dissolve
        pause
        hide text with dissolve
        $ time = 4
        jump home
    mc "{i}Eve... Why did Aerin's death hit her this hard...?"
    mc "{i}Maybe deep down, she still saw Aerin as her friend..."
    mc "{i}...I should probably leave, give Eve some space."
    "You leave the Elf Village and head home."
    $ time = 4
    jump home
