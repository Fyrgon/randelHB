default loritea = 0
default readwallcrawler = 0
default readalphafalcon = 0
default readimp = 0
default readwolf = 0


label monsterindex:
            hide screen hud
            if loritea == 0:
                scene black with fade
                l "Oh, [mc]. Would you, uhm... like some tea to drink while you read?"
                mc "Yeah, sure! That would be great."
                l "I'll bring you a cup right away... You're ok with Kahata tea, right?"
                "Lori quickly walks away."
                mc "Yeah!"
                l "Ok, awesome!"
                "After a few moments, Lori brings you a cup of tea."
                mc "That was quick."
                l "Hahaha, yeah. I made some tea a while ago... I made extra... {p}just in case you came over today."
                mc "......"
                mc "Thanks..."
                l "Hope you like the tea!"
                $ loritea += 1

            hide screen hud
            show animationread
            play sound chime
            $ renpy.notify ("{color=#fff}Type in the entry you're looking for.")
            $ bom = renpy.input("{i}So, let's see... What was I looking for?")
            if bom == "":
                mc "Ugh... I forgot..."
                jump library
            if bom.lower().strip() == "boar" or bom.lower().strip() == "boars":
                "The Boar, also called wild boar or wild pig, is the largest of the wild pigs and is native to forests of all of Astylla. It is bristly haired, grizzled, and blackish or brown in colour and stands up to 90 cm. This beast is swift, nocturnal, and omnivorous."
                "It lives in groups and all members of the species possesses sharp tusks, and, although normally unaggressive, it can be a dangerous animal as it is very territorial."
                "Old males, though, are solitary and have close to no hair on their black bodies. Old males are stronger than younger ones, but the bones in the top of their skulls are more fragile and thin which allows hunters to take them down very easily by hitting them on the head."
                $ time += 1
                jump library

            if bom.lower().strip() == "falcon" or bom.lower().strip() == "falcons":
                "The Falcon is a diurnal bird of prey characterized by long, pointed wings and swift, powerful flight. It is present all over Astylla. It spends most of its day in the sky hunting and only flies down at night to sleep."
                "This bird isn't the most agile creature in the sky, but it's fast and can evade arrows from novice bowmen."
                $ time += 1
                jump library

            if bom.lower().strip() == "alpha falcon" or bom.lower().strip() == "alpha falcons":
                "An Alpha Falcon, mostly found in the eastern regions of Astylla, is a bigger, yet more agile type of Falcon that is very hard to shoot down as they have excellent reflexes."
                "One can distinguish an Alpha Falcon from its more common counterpart thanks to the red dot on their head, emblematic of the beast. These falcons normally come out of their nests at {b}noon{/b} and roam during the {b}afternoon{/b}."
                "Though these birds have good reflexes, it has been proven time and time again that they have a hard time distinguishing the color green."
                "This is taken advantage of by hunters through the usage of {b}green arrows{/b} which blends with the greenery of the forest and allows the arrow to not be seen until it's too close to be avoided by the falcon."
                mc "{i}Hm... So, I need to use a green arrow huh? ...Where can I get paint?"
                mc "{i}Uncle Pete! He paints a lot. I could ask him."
                play sound chime
                $ renpy.notify ("{color=#fff}You learned about Alpha Falcons.")
                $ readalphafalcon += 1
                $ time += 1
                jump library

            if bom.lower().strip() == "goblin" or bom.lower().strip() == "goblins":
                "Goblin, the most dangerous of the common monsters in Astylla, a green human-like creature as tall as a child but still stronger than its appearance implies. A goblins is capable of basic reasoning, but its mind is limited in many areas."
                "It lives in groups which are very good at planning ambushes for preys bigger than themselves, sometimes even attacking unassuming humans. Large hunting parties are not uncommon. So those who travel through the forest should be warry."
                "{b}Goblin urine is venomous{/b}. When skin comes in contact with the urine, it can lead to quick and painful deaths. Goblins use this to their advantage by coating their weapons with urine or throwing it at their opponents."
                play sound chime
                $ renpy.notify ("{color=#fff}You learned about Goblins.")
                $ time += 1
                jump library

            if bom.lower().strip() == "wallcrawler" or bom.lower().strip() == "wallcrawlers":
                "Wallcrawler, a creature bound to the deep ends of caves, with four limbs and a mouth full of teeth. It's very rare to see a Wallcrawler out in the open and is usually sign of a migration."
                "Wallcrawlers are attracted to coal which they consume and transform inside their system as fuel and to form their ever-growing claws, teeth and thorns."
                "A Wallcrawler doesn't normally attack people, but if provoked, it breathes fire as a defense mechanism. Its body heals incredibly fast and can regenerate anything from lost limbs to a lost head. The only part of its body it can't regenerate is its heart."
                "{b}Undamaged Wallcrawler hearts are very valuable{/b} for their alchemical reagents. Many experienced and veteran adventurers collect them and sell them for moderate sums of money though just as many young adventurers die trying to do the same."
                mc "{i}Hmm... Wallcrawler hearts are valuable? If I manage to get one... Though maybe I should think of my own safety first. I better train a bit more if I want to make sure I can do it and get out in one piece."
                play sound chime
                $ renpy.notify ("{color=#fff}You learned about Wallcrawlers.")
                $ time += 1
                $ readwallcrawler += 1
                jump library

            if bom.lower().strip() == "imp" or bom.lower().strip() == "imps":
                "An Imp, usually innocently described as mischievous, is a dangerous red-skinned fiend with strong wings and razor-sharp claws able to pierce steel. An imp alone can be a serious threat if provoked."
                "Imp flocks are known to cause harm to small villages in the countryside. They often slaughter cattle but in some rare occasions they're known to have caused greater destruction and even kidnapped young maidens."
                "It is said that imps were used to be trapped inside artifacts such as gemstones or vials and summoned for service with magic. Which is why in modern times the {b}Imps seem to fear these gemstones{/b} which are now used as repellent against imps."
                play sound chime
                $ renpy.notify ("{color=#fff}You learned about Imps.")
                $ time += 1
                $ readimp += 1
                jump library

            if bom.lower().strip() == "vampire" or bom.lower().strip() == "vampires":
                "A vampire is a terribly dangerous monsters with human semblance, only distinguishable characteristic being their red eyes and elongated canines."
                "Vampires were the first monsters summoned by the Demon King and were used to infiltrate enemy armies and to fill the role of the Demon King's assassins."
                "A Vampire feeds exclusively on human blood and are capable of using illusion magic and turning invisible. A vampire also possesses extreme amounts of brute force and exceptional agility. Close-quarter combat is not advised."
                "Its skin burns under the sunlight and as such a vampire usually avoids it in crafty ways to hide irs true nature when blending with humans. Otherwise it simply roams after the sunset, during the night."
                "Besides sunlight, a vampire's only weakness is its heart which can only be stopped through impalement or complete removal which don't allow the vampire to regenerate from the wound."
                play sound chime
                $ renpy.notify ("{color=#fff}You learned about Vampires.")
                $ time += 1
                jump library

            if bom.lower().strip() == "lelluk" or bom.lower().strip() == "lelluks":
                mc "There is nothing on the Lelluk."
                if sawcynth >= 5:
                    mc "I guess Cynthia wasn't lying about it being super rare."
                jump library

            if bom.lower().strip() == "direwolf" or bom.lower().strip() == "direwolfs" or bom.lower().strip() == "direwolves":
                "A Direwolf is a large wild canine that can grow to be as tall as a man and weight as much as a bear. A Direwolf is far more aggressive than a normal wolf, attacking and killing anything it can catch."
                "Direwolves can be found singly as lone wolves, exiled from the pack, or in packs numbering five to eight Direwolves."
                "A lot of hunters and adventurers hunt dire wolves for their pelts, which can be easily sold for a fairly good price."
                "When hunting Direwolves, the best course of action is to look for lone wolves, as packs can be very dangerous even for a group of adventurers."
                $ time += 1
                play sound chime
                $ renpy.notify ("{color=#fff}You learned about Direwolves.")
                $ readwolf = 1
                jump library

            if bom.lower().strip() == "ledric" or bom.lower().strip() == "ledrics":
                "A Ledric is a dangerous and very intelligent monster which seems to have the {b}ability to communicate verbally with humans{/b}."
                "This creature uses a very intelligent mechanisms for hunting which consists in the release of a toxin in the air which lingers for about five hours."
                "When inhaled by a creature, it causes hallucinations, dizziness, fatigue, and sexual arousal. The Ledric's toxin has a special stimulant which causes arousal in animals and is the main ingredient of most love potions."
                "{b}Hallucinations can cause the victim to see the Ledric as a different being and potential mate{/b}. The Ledric uses this to attract the victims towards itself. Normally, adventurers and travelers wear masks to prevent the effects of the toxin."
                "Even without its toxin, a Ledric can be lethal. It's armed with a large tail which resembles that of a scorpion and is very strong. Caution is advised."
                jump library
                $ time += 1
                play sound chime
                $ renpy.notify ("{color=#fff}You learned about Ledrics.")
                jump library

            if bom.lower().strip() == "troll" or bom.lower().strip() == "trolls":
                "Trolls are a ravenous, predatory species of giant humanoids found mostly in areas far from settlements in almost all the regions and climates of Astylla."
                "They are uncivilized, monstrous creatures with voracious appetites that rarely leave their home. They're solitary and not as smart as some of their far cousins, the goblins."
                "These monsters are extremely strong. Whenever one gets too close to a city, their extermination is delegated to Diamond-Rank Adventurers or parties of Gold-Rank Adventurers."
                "Their strength is unrivaled by any humanoid monster outside of Devils, if you ever encounter one without prepared, running might be your best option."
                jump library
                $ time += 1
                play sound chime
                $ renpy.notify ("{color=#fff}You learned about Trolls.")
                jump library

            if bom.lower().strip() == "blood butterfly" or bom.lower().strip() == "blood butterflies":
                "SOMEONE IS TOO LAZY TO WRITE THIS RIGHT NOW."
                jump library
                $ time += 1
                play sound chime
                $ renpy.notify ("{color=#fff}You have NOT learned about blood butterflies.")
                jump library

            if bom.lower().strip() == "glob" or bom.lower().strip() == "globs":
                "SOMEONE IS TOO LAZY TO WRITE THIS RIGHT NOW."
                jump library
                $ time += 1
                play sound chime
                $ renpy.notify ("{color=#fff}You have NOT learned about globs.")
                jump library

            else:
                mc "There's no such entry in the book."
                hide animationread
                jump library
