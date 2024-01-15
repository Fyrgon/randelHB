default magiclecture = False
default wentToClassEver = 0
default magicLessons = 0

label magicalClass:
    menu:
        "Learn" if time < 3:
            $ wentToClassEver += 1
            scene lecturemage3 with dissolve
            if magicLessons == 0:
                s "Good day, everyone. Get to your seats and we'll start today's lesson. I'll write some stuff on the blackboard in the meantime."
                scene lecturemagelesson1 with dissolve
                pause 1.5
                s "Alright, let's begin then."
                s "Today's topic is: Mana Conductivity."
                s "So, we all know what magic does. You say words and then something happens. What we will learn today is {b}why{/b} this happens."
                s "As we said in our first class, mana is the energy source which we manipulate through spells to make magic. But how exactly do we do that? Mana {b}is{/b} everywhere after all, so why can't everyone just use it after they learned some Astyllian?"
                s "Mana is produced from within our planet, and according to elven folklore, within all stars as well. To manipulate it we need to grasp it and release it with our hands."
                s "A few high ranked mages are able to do this without using their hand, but if anyone here was capable of it, they'd already be at the Capital training under the best of the best."
                s "In order to take mana from the earth to our hands we need a conductor. These conductors are what we call staffs: devices able to conduct mana from its source through our body into our hands."
                s "Now, it is actually possible to conduct mana without a staff but only in small quantities. With enough practice one could be able to conduct more mana, but without a conductor mana quickly becomes lethal the more you store into your body, which is why it's not advised for anything outside of cantrips."
                s "Unlike us, some demons are actually capable of high-tier magic without the use of a conductor. Which is why Demon mages are extremely dangerous: Unlike us, they don't have to worry about never losing their staff, our most prized possession as mages."
                s "Alright, this is enough for today, get out and have fun."
                "Students" "Bye, Miss Scarlet!"
                "Everyone begins leaving the class and as they do you hear a few passing comments."
                "Student 1" "God, she's so hot."
                "Student 2" "Is she really our age?"
                "Student 3" "Who cares, I just wish I could fuck her."
                mc "{i}God, these guys are horny."
                "As you make your way to the door, Scarlet waves at you."
                scene lecturemage1 with dissolve
                show normalm
                show prot smile
                s "How's it going?"
                mc "I'm fine. How about you though? Do you really not mind all these perverts making stupid comments about you?"
                s "Nah, it's fine. They won't lay a finger on me."
                mc "How do you know that?"
                s "[mc]... I can easily turn each one of them into dust, you know?"
                mc "Oh, right."
                mc "{i}I still feel like they'd be annoying."
                s "But as long as they're nice, who knows what might happen."
                mc "What?"
                s "What?"
                mc "...You're fift-"
                "Scarlet puts her hand on your mouth to shut you up."
                s "Shhh!"
                "She looks around and then back at you."
                s "{size=-3}They still think I'm about 20 years old."
                mc "...You're hopeless."
                s "I just have fun teasing, it's all."
                mc "You sure do. See ya."
                s "Buh-bye!"
            else:
                "The class went on for a while."
            $ time += 1
            jump academy
        "Talk to Scarlet":
            jump Scarlet
