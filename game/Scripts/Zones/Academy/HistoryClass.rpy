default historyClass = 0

label borisClass:
    stop music
    if time > 0:
        "Aww man, I missed the class. Hope Boris didn't notice..."
        jump academy
    scene lecturetalk with fade
    if gabefinger > 2 and gabefingerclass == 0:
        jump gabeClassFingering
    $ historyLecture = "history" + str(historyClass)
    if historyClass < 2:
        jump expression historyLecture
    else:
        "The lesson droned on as per usual."
        $ time += 1
        jump academy

label history0:
    b "Good morning, class."
    b "Today's lesson is about the town's history. For those of you who can read, it's the History of Randel chapter in Randel's Local History Book."
    b "Randel was founded 340 years ago by a man named James Randel. He was a farmer in Hern. He came here with his wife and two daughters. Randel just as today has very rich soil."
    b "James Randel thought to start a new farm here. After a few months, he finally built his farm, and as you might expect, his farm prospered. After a few years, other folk heard of this place and came to Randel."
    b "They asked if James would let them put up their own farms here, Randel was a generous man and accepted their offer, and after a while, many farms started popping up in the area."
    b "After a few years, Randel was officially a town, though at first it was called Randelton. When James Randel passed away, the townsfolk turned the name of the town into just Randel in his honor..."
    "The lesson went on and Boris elaborated further on Randel's history, but he made it very clear that the only thing the students needed to remember were the basics."
    $ historyClass += 1
    $ time += 1
    jump academy

label history1:
    b "Good morning, class. Today, we'll be talking about something which you might see the end of in your lifespan."
    b "We'll be talking about the Demon War."
    b "So, the war started 448 years ago, in the year 1120. The Old Kingdom was ruled by the Elf King Woren. He had two sons: Rem, the eldest, and Ron, the youngest. The king was getting old and he needed a heir."
    b "According to Elven tradition, Rem should've been made the heir to the throne as he was the firstborn, but instead the king named Ron as the heir to the throne."
    b "This was mostly because Rem was deemed unfit to rule. He had no qualities of a king. Ron however excelled in all his studies and was also a great warrior. So, it was thought to be fair to name him as the heir."
    b "When the king died, Ron was crowned as king and Rem became furious. He thought he deserved to rule over the kingdom, and this lead him even more astray."
    b "Rem had been studying ancient history, and he found out about a spell which would make him into a King... the Demon King."
    b "He cast the spell and summoned the Demon King. The soul of the Demon King immediately latched onto Rem, the closest living vessel, and possessed him."
    b "With his newfound body, the Demon King built an army of artificial monsters that we call \"Demons\" and attacked the old kingdom."
    b "Rem had to act quickly and he had the entire kingdom flee across the Mountains of Arp in what we today refer to as the \"Great Displacement\"."
    b "Thanks to General Astyl, the Demon Army was stopped where Hern stands today, and enough time was given to the dwarves to build the modern walls of Astylla which were finished in the year 1131"
    b "The Demon King was finally slain 15 years ago by the hero Sir Gladius Hans, arguably the greatest adventurer ever."
    b "Hans came from a noble family which used to be of pure elf blood, but with his mother being a human, and his father being just a quarter elf, he was indistinguishable from a regular human which made him very popular even before his great achievement..."
    "The lesson droned on for a few hours, but just like last time, he's just expanding upon what he's just said."
    scene lecturetalk with fade
    b "...And with this, I've explained all the information you need to know for the first test of the year. From now on I'll start explaining Ancient history which is for your midterm test."
    b "If you know how to read you can pick up the \"Randel's Local History Book\" at the library to revise whatever you want... If you don't know how to read, I hope you've got a good memory."
    "Everyone starts leaving."
    scene academy
    mc "{i}...Wait, he didn't say when the first test is."
    $ historyClass += 1
    $ time += 1
    jump academy

label history2:
    b "Good morning, class."
    b "Today we'll begin learning about Ancient History. Most of you probably know nothing about it unlike with some of the other things I've taught you so far, so I hope you'll understand that you need to pay attention in class."
    "Boris cleared his throat."
    b "So, when we talk about Ancient History, we are actually referring to four different eras. The Dwarven Era, The Coexistence Era, The Elfin Era, and The First Dinasty."
    b "Today we're talking about the first two of these eras, beginning with the Dwarven Era of which we date the start of at about 4000 years ago."
    b "The reason why the first known era in our history is called the Dwarven Era is because, as you might know, the first race to live in these lands we inhabit today were the dwarves. They had no exceptional qualities, but the world back then was also much safer. The monsters that today roam our planet didn't use to exist."
    b "Despite the lack of reason to develop past their basic needs for safety, the dwarves managed to discover the use of magic through the use of runes."
    b "Runes allowed them to develop much more than they would otherwise have, yet runes are a very limited form of magic and so they remained fairly limited in their magical use, developing instead their metallurgy, engineering, and architecture. We can see from some of the ruins from back then that even to this day we can't easily replicate some of their feats."
    b "About 2000 years ago, the elves arrived from the stars, and with them arrived spellcasting as well."
    b "\"Coexistence Era\" is how we call the first 500 years after the arrival of elves."
    b "During this era the two races mostly lived peacefully but separately, which allowed the two races to maintain their very distinct identity while also learning from each other."
    b "This separation of the races, though, meant that neither could learn what they needed to prosper from the other. The dwarves never became proficient with magic, and the elves never got any significant infrastructure up — it was so bad we barely have any Elvish remains from back then."
    "Boris then began expanding upon these two eras. He mostly repeated what he jsut said, naming a few rulers here and there, and a few minor conflicts, but nothing too important."
    $ historyClass += 1
    $ time += 1
    jump academy

label history3:
    b "Good morning, class. I didn't sleep well tonight so please try to be quiet."
    b "So... Where were we again?"
    "Random Student" "The Coexistence Era, sir."
    b "Ah, right, thank you. Today we're going to talk about The Elfin Era, then."
    b "Alright, so: after 500 years of relative peace, the world saw its first big catastrophe."
    b "The Demon King was summoned"
    b ""
    b ""
    $ historyClass += 1
    $ time += 1
    jump academy

label history5:
    $ historyClass += 1
    $ time += 1
    jump academy

#label history6:
#    b "Goodmorning class."
#    $ historyClass += 1
#    $ time += 1
#    jump academy

#label history7:

#label history8:

#label history9:

#label history10:
