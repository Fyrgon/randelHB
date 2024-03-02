label forest:
    if time > 4 or (time == 4 and magic_lamp < 1):
        scene forrestn
        mc "It's too late to be in the forest."
        jump maplimbo
    hide screen screenmap
    play music forest
    if saq < 1:
        hide screen hud
        scene forest
        call wotv1 from _call_wotv1
        scene forest with dissolve
        show thinkmc
        mc "{i}What the hell...? How am I supposed to spy on girls without getting caught...?"
        mc "{i}{b}I could use a spell to make me invisible{/b} or something. I should ask Scarlet..."
        show worriedmc
        $ renpy.notify("{color=#fff}Quest started: The Way of the Voyeur")
        mc "{i}Ugh, I'm gonna regret this..."
        $ q1 += 1
        $ saq += 1
        jump forest
    show screen hud
    if time >= 3:
        scene forrestn
    else:
        scene forest
    if cynthquest4 == 1 and  cynthquest5 == 0:
        jump cynthquest5
    if sawtriss == 1:
        jump trissq
    if sawmegan == 1:
        jump meganq
    if sawelfvillage >= 1 and sanderhigh == 0 and elfday+12 <= day:
        jump sanderHigh
    if elfday+7 <= day and zenBegun == False and bothpath >= 6 and killZen == False:
        jump ZenelithEncounter

    menu:
        "Meet Triss" if time == 2 and trissq1 == 1:
            if ibugnet == 0:
                mc "I need to buy a bug net first."
                jump guild
            jump trissq1

        "Go look for Zenelith's bag" if asked4gift == True and zenbag == False:
            jump zen5B

        "Go to Zenelith's Shack" if zenQ > 0 and zenRouteEnd == False:
            jump zenShack
        "Go pay Zenelith a visit" if zenS > 0 and zenRouteEnd == False:
            jump zenShack

        "Go to the Elf Village" if sawelfvillage == 1:
            jump elfVillage

        "Outer Valley":
            if day >= 8 and sawjunglegirl == 0:
                hide screen hud
                "You search the valley for a while."
                "Suddenly as you are walking along, a boar rushes past you and disappears into the bushes."
                mc "{i}Huh?"
                "You hear branches shake in the nearby trees. You see a figure hop from branch to branch."
                "Then it stops and looks at you."
                scene junglegrl with fade
                "Her crimson eyes stare right into you."
                mc "H-Hello?"
                window hide
                pause
                "Mysterious Figure" "......"
                "Then, she hops onto another tree and disappears into the forest."
                scene forest
                mc "Who was that?"
                $ sawjunglegirl += 1
                jump forest

            menu:
                "Look for Rosa Flowers" if knowrosa == 1 and rosa < 4:
                    if rosa == 0:
                        mc "Let's see if I can find some."
                        "You search for a while, but you are unable to find anything."
                        mc "Nothing! I thought these weren't rare!"
                        mc "I should come back again."
                        $ rosa += 1
                        $ time += 1
                        jump forest

                    if rosa == 1:
                        mc "Ok, let's see if we'll get lucky this time."
                        "You search the forest, but you still couldn't find the flower."
                        "Disappointed, you decide to head back home. Just as you're about to leave, you see a little girl carrying a pink flower."
                        mc "Hey! Excuse me, can you stop for a second?"
                        "Girl" "What is it, mister?"
                        mc "Is that a Rosa Flower?"
                        "Girl" "Yes, it's my mother's favorite. I thought of giving it to her as a present for her birthday!"
                        mc "{i}It's a Rosa Flower! How did that kid manage to find it? It doesn't matter, I need that Rosa Flower."

                        menu:
                            "Take it by force":
                                mc "{i}I really need that flower. Who knows, it could be the last one."
                                mc "I'm sorry, kid."
                                "You grab the flower out of her hands and run away."
                                "Girl" "Hey! Give that back! *sob*"
                                $ rosa += 3
                                scene forest with fade
                                mc "{i}Yes! Finally, I got the flower! I'm not proud of myself, but still, I got it done."
                                mc "{i}Now I have to use this on Eve. It should be just before the duel. I should wait till the duel happens. Only [evedueltimer] more days."
                                $ time += 1
                                $ rosa += 3
                                jump forest

                            "Trade for 50 gold" if money >= 50:
                                mc "Oh, that's nice. But you see, I'm looking for a Rosa Flower as well. How about we trade?"
                                mc "I'll give you 50 gold for that flower. You can get a better present for your mother with that money."
                                "Girl" "Uhm..."
                                mc "{i}Come on kid, take the money. Don't be stupid."
                                "Girl" "Ok!"
                                mc "Great!"
                                "You give her the money and take the flower. The little girl skips along."
                                "Girl" "Thank you, mister!"
                                mc "{i}Now I have to use this on Eve. It should be just before the duel. I should wait till the duel happens. Only [evedueltimer] more days."
                                $ time += 1
                                $ rosa += 3
                                $ money -= 50
                                jump forest

                            "Leave it":
                                mc "{i}I'm not a monster. I can't take this flower from her. I'll just come back tomorrow and try to find it."
                                mc "Tell your mother that a random stranger wished her a Happy Birthday."
                                "Little girl" "Hehe! I will. Bye, mister!"
                                $ time += 1
                                $ rosa += 1
                                jump forest

                    if rosa == 2:
                        mc "Please, at least this time..."
                        "You search for the flower, but you are still unable to find it."
                        mc "{i}Why, just why can't I find it? That little girl found it, why can't I?"
                        mc "{i}sigh... I'll come back tomorrow then."
                        $ time += 1
                        $ rosa += 1
                        jump forest

                    if rosa == 3:
                        mc "Please Astylla..."
                        "You search the forest for a while. You decide to go deeper into the valley. After searching for hours, you find it near a lake."
                        mc "{i}Yes! I found it, finally!"
                        mc "{i}Now I have to use this on Eve. It should be just before the duel. I should wait till the duel happens. Only [evedueltimer] more days."
                        $ rosa += 1
                        $ time += 1
                        jump forest



                "Hunt":
                    jump OuterValley

        "Outer Forest" if persistent.bronzeParty == True:
            jump OuterForest
    return
