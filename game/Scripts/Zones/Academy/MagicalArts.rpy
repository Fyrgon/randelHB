default magiclecture = False
default wentToClassEver = 0
default magicLessons = 0

label magicalClass:
    if time >= 3:
        mc "{i}Seems like Scarlet isn't in the class this late... where can she be?"
        menu:
            "Go back":
                jump academy
            "Go look for her" if magiclvl >= 10:
                scene storeroomblr
                show thinkmc
                mc "{i} Could she be here?"
                "{color=#EFC667}Familiar voice" "{i}Zzz..."
                hide thinkmc
                show suprised
                mc "... maybe she is ..."
                "{color=#EFC667}Familiar voice" "{i}Zzz......"
                mc "{i}In th locker again?"
                hide suprised
                show thinkmc
                "You come closer the locker a sleeping sounds are comming from."
                scene sleepmclose with fade
                mc "There's someone inside."
                menu:
                    "Open":
                        scene sleepm3 with vpunch
                        pause 1
                        mc "{i}Holy moly!"
                        mc "{i}What were she doing here like this?"
                        scene sleepm3
                        pause 2
                        he "{i}Damn... what a view... What should I do?"
                        label nakedScarletInALocker:
                        menu:
                            "Keep watching":
                                mc "{i}Man, her boobs are quite big and they seems still firm for her age."
                                mc "{i}Her pussy seems quite wet."
                                he "{i}Were she masturbating here or does she have a wet dream?"
                                jump nakedScarletInALocker
                            "Play with her":
                                if stealthlvl < 3:
                                    scene black
                                    $ renpy.notify ("{color=#fff}Stealth skill check: {color=#A50000}Fail! ([stealthlvl] >= 3)")
                                    "As you touched Scarlet roughly she woke up suddenly and her eyes glowed with anger and magical energy. Before you could say anything or she recognizing you, her spell incinerated you."
                                    jump GameOver
                                show animationboobhand
                                show animationfinger
                                pause
                                mc "{i}She likes it."
                                mc "{i}I guess her tits are really sensitive."
                                pause
                                mc "{i}Sooooo soft... and her pussy is leaking a lot."
                                pause
                                hide animationboobhand
                                hide animationfinger
                                show sleepm3 with vpunch
                                show sleepm3 with hpunch
                                mc "{i}Did Scarlet just cum?"
                                mc "{i}Looks like she's waking up. I better leave or she might turn me into a frog."
                                show sleepmclose
                                pause
                                $time += 1
                                jump academy
                            "Rub one off":
                                mc "My dick feels like it's gonna explode... Must... release..."
                                show animationfap
                                pause
                                mc "I'm gonna cum...!"
                                hide animationfap
                                show cumth with vpunch
                                show fap1
                                pause
                                hide cumth with dissolve
                                mc "Oh yeah, that felt great..."
                                scene sleepmclose
                                pause
                                $time += 1
                                jump academy
                            "Wake her up":
                                mc "{i}I'm not a damn pervert. I gotta wake her up."
                                "You close the locker, move away and speak as if you were looking for her."
                                he "Hey, Scarlet, are you here?!? I need to talk to you!"
                                "A sudden sounds of a person waking up can be heard from the locker with a soft curse and then Scarlet walks out of the locker"
                                s "Ah, [mc], you are looking for me? I was just checking the -"
                                mc "You were sleeping in the locker again..."
                                s "Haha, yeah, you got me... You've said you want to talk to me. Let's talk in the classroom then."
                                jump ScarletTalk
                    "Knock":
                        he "Hey, Scarlet, are you there? I need to talk to you."
                        "A sudden sounds of a person waking up can be heard from the locker with a soft curse and then Scarlet walks out of the locker."
                        s "Ah, [mc], you caught me sleeping here again... You've said you want to talk to me. Let's talk in the classroom then."
                        jump ScarletTalk
    else:
        menu:
            "Learn":
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
                    s "Mana is produced from within our planet and according to elven folklore, within all stars as well. To manipulate it we need to grasp it and release it with our hands."
                    s "A few high ranked mages are able to do this without using their hand but if anyone here was capable of it, they'd already be at the Capital training under the best of the best."
                    s "In order to take mana from the earth to our hands we need a conductor. These conductors are what we call staffs: devices able to conduct mana from its source through our body into our hands."
                    s "Now, it is actually possible to conduct mana without a staff but only in small quantities. With enough practice one could be able to conduct more mana but without a conductor mana quickly becomes lethal the more you store into your body, which is why it's not advised for anything outside of cantrips."
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
