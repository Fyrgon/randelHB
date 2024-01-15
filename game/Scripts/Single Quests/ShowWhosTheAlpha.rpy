default alphafalcon = 0

label swta1:
    show talkwamc
    show smilee
    mc "Guess who'll be joining your party soon?"
    show watalkeve
    hide talkwamc
    show smilemc
    e "Wh-What... who?"
    hide watalkeve
    show talkhappymc
    mc "Me!"
    hide talkhappymc
    show watalkeve
    e "What?!"
    show talkwae
    e "I mean... That's nice, little one. But you have to be at least a Bronze-Rank Adventurer to join us."
    hide talkwae
    hide watalkeve
    show talkmc
    mc "Yeah, I know. Sander told me I could join when I reach Bronze."
    show watalkeve
    hide talkmc
    e "S-Sander? Ugh... that idiot... did he ask you do something for him?"
    mc "Uhm... y-yeah..."
    e  "What did- You know what, I don't want to know."
    show talkwanmc
    mc "Do you not want me to join your party?"
    hide talkwamc
    show normalmc
    hide watalkeve
    show sadhtalke
    e "Oh, it's not that, little one... It's just that Sander and I normally take on high-risk quests, so- "
    show angry
    hide sadhtalke
    mc "So you think I won't be able to keep up with you guys?!"
    show sadtalke
    e "No, I didn't mean that..."
    hide sadtalke
    mc "Ok then, give me a test. I'll show you that I'm worthy of joining your..."
    menu:
        "\"Elite\"":
            mc "...\"Elite\" party."
            hide angry
            show sadtalke
            e "...You don't need to-"
            hide sadtalke
            show angry
            mc "No. Just tell me what I need to do."
            e "......"
            mc "Tell me."
            show watalkeve
            e " Fine, little one..."
            hide watalkeve
            hide angry
        "Elite":
            mc "...Elite party."
            hide angry
            show sadhtalke
            e "You don't need to-"
            hide sadhtalke
            show talkwanmc
            mc "No. Just tell me what I need to do."
            e "......"
            mc "Tell me."
            show watalkeve
            e "Fine, little one..."
            hide watalkeve
            hide talkwan
    e "Hmm... What can I give you..."
    show talkwae
    e "...I want you to hunt down three Alpha Falcons."
    hide talkwae
    show talkwanmc
    mc "Alpha Falcons?"
    mc "What do they look like?"
    hide talkwanmc
    e "That's all I'm going to tell you little one. The rest you should do on your own."
    show talkwamc
    mc "I get it. That's ok... Challenge accepted!"
    e "Good luck."
    play sound chime
    $ renpy.notify("{color=#fff}Quest started: Show Who's The Alpha")
    scene agblr
    show thinkmc
    mc "Hmm... Ok, so I need to find out more about Alpha Falcons... better {b}check The Book of Monsters{/b} and see what I can find."
    $ askeve -= 1
    $ afq += 1
    $ q2 += 1
    jump guild

label swta2:
    hide screen hud
    show talkhappymc
    hide uncletalk
    mc "Uncle, do you have some green paint?"
    hide talkhappymc
    show uncletalk
    u "Yeah, I should have some. Why don't you check for me? It should be over there."
    mc "Thanks."
    scene black with fade
    "You search for the paint and find a bucket of green paint amongst your uncle's painting supplies."
    mc "Found it!"
    "As you raise the bucket from the floor, you see a painting covered by a cloth next to it."
    scene peteart with fade
    mc "What's this? You working on a new painting, Uncle Pete?"
    u "Oh, yeah. I started that one recently."
    mc "Can I see it?"
    u "N-No, it's not done yet. I'll show it to ya when it's done."
    mc "......"
    mc "Well, ok then."
    scene fishhut
    show talkhappymc
    show uncletalk
    u "What do you need the green paint for anyway?"
    mc "It's for this arrow."
    u "A green arrow? You're trying to hunt an Alpha Falcon, aren't ya?"
    mc "Yeah... wait, how do you know?"
    u "My father was a hunter. He taught me a few tricks of the trade."
    mc "Really? I didn't know that."
    u "Just because you have a green arrow doesn't mean you can take it down easily. You still have to be good with the bow. The arrow has to be fast enough, otherwise it'll dodge it. Make sure to have a good draw."
    mc "Thanks for the tip. I didn't know you knew this much about bows, Uncle Pete."
    u "Heh. There's a lot you don't know about me, kid."
    mc "Heheh... See, you Uncle Pete."
    u "See ya- Wait, want me to help you paint the arrow?"
    menu:
        "I can do it myself":
            show talkwamc
            mc "I just have to brush it with green paint, right? I think I can handle that. Thank you anyway."
            show sadtalkuncle
            u "Oh... Ok then, but be careful."
            mc "I'll be fine. Bye, Uncle Pete."
        "Yeah, sure!":
            mc "Yeah, sure! You're the expert."
            u "It's hardly anything, you just have to brush it with green paint."
            "Uncle Pete paints the arrow and gives it to you."
            mc "Thanks, Uncle Pete!"
            u "No problem! You be careful, ok?"
            mc "I will. Bye."
    play sound chime
    $ renpy.notify("{color=#fff}You obtained a green arrow.")
    $ q2 = 2
    $ greenarrow += 1
    $ afq -= 1
    jump talku



label swtaH:
if time == 1 or time == 2:
    hide screen hud
    "You start to search for an alpha falcon. After hours of searching, you finally find one."
    scene huntfg2
    mc "There it is, it has a red spot. Finally found one."
    "You take out your bow."
    mc "Let's get this done."
    if bowlvl >= 2 and greenarrow ==1:
        "You draw your bow and shoot."
        scene huntfg1
        mc "Yes!"
        scene huntf4 with vpunch
        mc "Ok, that's one alpha falcon down."
        $ exp += 30
        call levellingUp from _call_levellingUp_4
        $ alphafalcon += 1
        "You take the falcon and leave."
        $ time += 1
        jump forest
    "You draw your bow and shoot."
    scene huntfg3
    mc "Shit, it dodged it!"
    mc "I guess I still have to train more."
    jump forest
mc "It's not here, I think they come out in the afternoon. Better come back at that time."
jump forest



label swta3:
    show normalmc
    show talkwanmc
    show normale
    mc "Ok, I did it."
    show talkwae
    e "What, really?! It would seem that I underestimated you, little one!"
    show talkwamc
    mc "So this means I'm in, right?"
    hide talkwanmc
    hide talkwamc
    e "I suppose so!"
    show talkhappymc
    mc "Hehehe."
    show talkhe
    e "I'm looking forward to working with you. You better reach Bronze quick or we might recruit someone else! Hehehe..."
    menu:
        "Hey, that's unfair!":
            show talkwanmc
            mc "Hey, that's unfair! You told I could join."
            show sadhtalke
            e "Relax child, I'm just playing with you!"
            show talkwanmc
            mc "Oh, hehehe, sorry... I'll see you soon."
            e "Good luck, little one."
        "I'll do my best, ma'am":
            mc "I'll do my best, ma'am."
            e "Hehehe. Good luck, little one, hope to see you soon!"
            mc "You too. Bye!"
    e "By the way, here's something for your trouble."
    $ renpy.notify("{color=#fff}You gained 10 silver")
    $ money += 10
    mc "Wow, thanks!"
    $ renpy.notify("{color=#fff}Quest complete: Show Who's Alpha")
    $ greenarrow -= 1
    $ evequest +=1
    $ q2 += 1
    jump guild
