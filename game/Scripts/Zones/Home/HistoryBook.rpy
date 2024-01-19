label readingAtHome:
    hide screen interactivehome
    $ readgabe1 += 1
    "The book has three parts, each divided in multiple chapters. Which do you check out?"
    menu:
        "Part One":
            jump historyPart1
#        "Part Two":
#            jump historyPart2
#        "Part Three":
#            jump historyPart3
        "Nevermind":
            jump home


label historyPart1:
    "Part one has two chapters. Which one do you read?"
    menu:
        "1. History of Randel":
            "Randel was founded 340 years ago by a man named James Randel. He was a farmer from Hern. He came to the valley where Randel stands with his wife and two daughters. Back then like it does nowadays, Randel's soil was very fertile."
            "James Randel decided to start a new farm right there. After some months of work and wait, the crops started growing and his farm prospered. Hearing of the quality of the soil, many other farmers came to Randel."
            "They asked if James would let them put up their own farms here and since he was a generous man, he let them build around his farm until, after less than a decade from settling there, a village had formed."
            "Back then it was known as \"Randel's Town\" or \"Randelton\" but after James Randel passed away, the town started being simply called \"Randel\" and the name stuck."
            $ time += 1
            jump home
        "2. An Overview of the Demon War":
            "In the year 1120, the old Kingdom was ruled by King Woren. He had two sons: Rem, the eldest and Ron, the youngest."
            "As Woren was becoming old, he had to decide who would be his heir. According to Elven customs, it should've been the eldest but Rem was deemed unfit to rule, having no qualities of a king. So, Ron, who excelled in every area one could, was named as heir to the throne."
            "When the king died and Ron was crowned as king, Rem became furious. He thought he deserved to rule over the kingdom and this lead him even more astray."
            "Rem had been studying ancient history and he found out about a spell which would make him into a King... the Demon King."
            "He cast the spell and summoned the Demon King. The soul of the Demon King immediately latched onto Rem, the closest living vessel and possessed him."
            "With his newfound body, the Demon King built an army of artificial monsters that we call \"Demons\" and attacked the old kingdom."
            "Rem had to act quickly and he had the entire kingdom flee across the Mountains of Arp in what we today refer to as the \"Great Displacement\". Thanks to General Astyl, the Demon Army was stopped where Hern stands today and enough time was given to the dwarves to build the modern walls of Astylla which were finished in the year 1131"
            "After 433 years of constant war against the Demon King he was finally defeated under the rule of King Olin. The Demon King was slain during the Final Hern Siege by Sir Gladius Hans, the leader of the adventurer party known as \"The Maryas\" which were then hailed as heroes. Since then, the war against the Demon Army has slowed down and it seems Astylla may finally see the end of the war."
            $ time += 1
            jump home
        "Nevermind":
            jump readingAtHome

#label historyPart2:
    "Part two has three chapters. Which one do you read?"
    menu:
        "3. Pre-Ancient History":
            "In the year 1120 in the human calendar, Astylla was ruled by an elf king, King Woren. He had two sons, Rem the older son and Ron the younger. The king was getting old and he needed a heir."
            "According to Astyllian customs, Rem should've been made the heir to the throne as he was the eldest but instead the king named Ron as the heir to the throne."
            "This was mostly because Rem was deemed unfit to rule. He had no qualities of a king. Ron however excelled in all his studies and was also a great warrior. So, it was seen as fair to name him as the heir."
            "When the king died, Ron was crowned as king. Rem was furious, he wanted the throne. So, he wanted his brother dead. He had also recently discovered an ancient book which described a being of tremendous power."
            "A being that could corrupt living beings, the Demon King. After years of searching, Rem found the spell that could summon the evil being. He managed to summon the Demon King."
            "What he wasn't aware of is that the Demon King needed a living vessel. Immediately after he was summoned, Rem was possessed, his soul was destroyed and replaced by the Demon King."
            "After a few months, the Demon King attacked Astylla with his army and centuries of fighting took place. Astylla, which once covered the entire realm was pushed back into the small confined land we all live in today."
            "The Demon King was finally slain fifteen years ago by the hero Sir Gladius Hans. Sir Gladius Hans was the king's protector at the time. He was from the high elven family. Traditionally, they were a family of warriors dedicated to protecting the king."
            $ time += 1
            jump home
        "4. First Demon War":
            $ time += 1
            jump home
        "5. Old Kingdom History":
            $ time += 1
            jump home


label historyPart3:
    "Part three has five chapters. Which one do you read?"
    menu:
        "6. Astyllian History: Astyl":
            $ time += 1
            jump home
        "7. Astyllian History: Rem's Reign":
            $ time += 1
            jump home
        "8. Astyllian History: Aruel's Reign":
            $ time += 1
            jump home
        "9. Astyllian History: Mavir's Reign":
            $ time += 1
            jump home
        "10. Astyllian History: Olin's Reforms":
            $ time += 1
            jump home
