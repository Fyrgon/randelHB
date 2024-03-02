default meganq1 = 0
default metmegangq = 0

label meganq0:
         if time > 3:
             mc "It's too late to visit the Guild."
             call screen screenmap
         hide screen screenmap
         hide screen hud
         play music aguild

         scene agblr with fade

         show smilese
         show smilemc
         show talksadhappymc
         mc "Oh. Hi, Eve. What's up? Had a party without me?"
         show talkhse
         hide talksadhappymc
         e "Oh, no, little one. Sander just had... a little drinking contest with Triss and, well... as you can see, he lost."
         hide talkhse
         sa "That b-bitch... I'll get her... n-next time. {i}Hic..."
         show talkhse
         e "You always say that, Sander. And you always lose."
         show talkwanmc
         mc "Who's Triss?"
         hide talkwanmc
         e "Oh. I think you haven't met her. She was out on a quest for about a month. She just returned yesterday."
         show talkwanmc
         mc "On a quest for a month?!"
         e "Yeah. She's a Diamond-Rank Adventurer, so it's normal for her quests to take months."
         mc "A Diamond?! Wow, never seen one before."
         e "Hehe, yeah, they're pretty rare. And they're always out on quest, so you don't see them that often."
         hide talkhse
         show talkhappymc
         mc "Mh, I see."
         show talkow
         e "But I advise you to stay away from her, little one."
         scene trissshow with fade
         pause
         mc "Huh, why?"
         scene agblr with fade
         show talkow
         hide talkhappymc
         show talkwanmc
         e "She's, Uhm, how should I say this? ...She's, uh, inappropriate."
         mc "Inappropriate?"
         sa "She's a SLUT!"
         show talkow
         e "Sander! Keep it down!"
         show talkhse
         e "But, yeah, I guess that's a better word. Haha."
         hide talkhse
         mc "Mhh... Well, I'll keep that in mind."
         show talkmec with easeinleft
         m "Excuse me."
         show talkhse
         hide talkmec with easeoutright
         e "Oh, sorry, Megan."
         mc "What's her problem?"
         e "Oh, that's Megan. Always in a hurry."
         mc "Is she a Diamond as well?"
         e "No. She's... a... Silver, I think. I really don't know much about her, honestly."
         mc "Really?"
         e "Yeah. Hehe. She doesn't talk much."
         mc "Mh."
         e "Anyway, I'll go put Sander in his room."
         e "Hey, wait a minute... You're Bronze now, didn't you get a room at the Quarters?"
         show talksadhappymc
         mc "No... July said it's still under construction."
         e "Ohhh, I see. Anyway, you should visit us sometime."
         mc "Yeah, I should. I'll swing by sometime."
         e "That would be great. See you, little one."
         mc "Bye, Eve."
         $ sawtriss += 1
         $ sawmegan += 1
         jump guild


label meganq:
    hide screen hud
    mc "I feel like going a little deeper into the forest today."
    mc "I'm getting sick of only hunting in this area. I'm a Bronze now anyway, can handle it."
    "You decide to go deeper into the forest."
    "As you stroll, the overgrowth from the trees begins to darken the path. You see a creek up to the bank to watch the water gently trickle downstream. As you sit there, you begin to hear a couple of people talking in the distance."
    mc "Huh? That sounds like a person, kinda weird for people to be this deep into the forest..."
    scene banditcamp with fade
    "{color=#fff}Unknown Man 1" "Hey Marco... why aren't they still here? "
    "{color=#fff}Unknown Man 2" "Relax man, they still might be raiding Siglis."
    "{color=#fff}Unknown Man 1" "Ah, come on! We've been here for hours!"
    "{color=#fff}Unknown Man 2" "Yeah, yeah, we said we were gonna regroup here, so we are gonna do exactly that."
    mc "Are they bandits? They seem too well-equipped to be bandits..."
    "{color=#fff}Unknown Man 1" "This is so boring..."
    "{color=#fff}Unknown Man 2" "Don't you have anything else to do besides complaining?"
    "{color=#fff}Unknown Man 3" "Don't we have one of those cows?"
    "{color=#fff}Unknown Man 2"  "......"
    "{color=#fff}Unknown Man 2" "Oh no, not this again..."
    "{color=#fff}Unknown Man 1" "I want the big one."
    "{color=#fff}Unknown Man 2"  "You know that's a bull, right?"
    "{color=#fff}Unknown Man 1" "A hole is a hole!"
    mc "I should leave before I see something I'm gonna regret..."
    $ sawmegan += 1
    jump forest


label meganq1:
    scene adventurersguild_day with fade
    j "When did this happen, sir?"
    "{color=#fff}Farmer" "I don't know! I just went to the market, and when I got back, my two cows were gone! I'm sure it must be some damn bandits!"
    scene adgc6
    j "Ok, sir. I'll assign an Adventurer as quickly as possible."
    scene adgc7
    "{color=#fff}Farmer" "Please... those cows are my livelihood! I might as well be dead without 'em!"
    m "I'll find them."
    j "Megan? Are you sure? You just got back from your last quest."
    scene adgc7
    m "I'll manage. This shouldn't take long anyway."
    "{color=#fff}Farmer" "Oh, thank you! May Astylla bless ya, miss!"
    m "Are you certain bandits did this?"
    "{color=#fff}Farmer" "Yes, I'm sure! They were locked up tight in the barn. It was broken when I got home."
    m "Mh... bandits it is then. July, do you have any idea which group did this?"
    scene adgc6
    j "I'm not sure. There has been a recent increase in the number of raids near Randel. It'll be hard to find their base, they don't stay in one place for long."
    scene adgc7
    m "I guess I'll have to hunt them down."
    mc "Wait!"
    scene adgc2
    j "Yes, [mc]? Do you have something to say?"
    scene adgc7
    mc "Yeah I... I saw a group of bandits in the forest."
    scene adgc6
    j "In the Outer Valley? That isn't very well hidden for a bandit camp."
    scene adgc7
    mc "I went a bit deeper into the forest. I saw a group of bandits and... they had a couple cows..."
    "{color=#fff}Farmer" "Really?! Oh, thank Astylla! Were they ok?"
    mc "Uhm... Yeah... Totally fine..."
    scene adgc5
    j "Hold it right there... You went deeper into the forest?! I told you to stick to the outer valley!"
    mc "It's fine, nothing happened. I'm a Bronze-Rank Adventurer now. I think it's time I went a bit further in to the forest."
    j "You could've gotten hurt, [mc]!"
    scene agblr
    show normalmc
    show normalmec
    show talkmec
    m "Could you two have a couple's squabble some other time? Kid, you said you saw them, right?"
    hide talkmec
    show talkmc
    mc "Yeah."
    hide talkmc
    show talkmec
    m "Do you remember the exact location?"
    hide talkmec
    show talkwanmc
    mc "Yeah! It was near the creek-"
    show suprised
    show talkmec
    m "Come with me."
    hide suprised
    hide talkmec
    mc "Huh?"
    show talkmec
    m "It'll be easier if you just showed me the way. I can handle the rest."
    hide talkwanmc
    j "I don't thi-"
    show talkwamec
    m "It's ok, July. He's a Bronze, right? I'm sure he can handle it."
    j "Ok... Whatever."
    m "Come on. Let's get a move on. It's already getting dark."
    show talkmc
    mc "Ok, sure."
    scene forrest with fade
    "You head into the forest with Megan, she follows behind at a steady pace as you leave the outer valley and find the creek to follow to the bandit camp. The sky turns towards hues of red and orange as the sun begins to set."
    play music night
    scene sneak1 with fade
    pause
    scene sneak2
    m "There's a lot more than I expected... at least a dozen of them."
    mc "There are the cows... I see them towards the back of the camp."
    m "Of course, they're on the far side..."
    mc "How do we reach them?"
    m "This is my mission, [mc]. You'll be staying here while I sneak through and untie them. If this all goes right, I'll be able to get them out without anyone noticing."
    mc "There's a lot of them. What if you... uhm... get caught?"
    m "Get caught?! You clearly haven't heard of me!"
    m "Do you know why they call me \"The Black Mist\"? I can sneak through anything! I'm the definition of silence."
    mc "...Right..."
    m "They never see me coming... and I leave behind only whispers of my name..."
    mc "{i}That doesn't even make sense."
    mc "Sorry, I guess I didn't know."
    m "Huh. Well, you stay here, [mc]. Ok?"
    mc "Sounds like a plan."
    scene sneak3
    pause 0.5
    scene sneak5
    pause 0.5
    scene sneak6
    pause 0.3
    scene sneak7 with vpunch
    mc "Shit! Someone definitely heard that..."
    "{color=#fff}Bandit 1" "Huh? Did you hear that?"
    "{color=#fff}Bandit 2" "We should go check it out."
    "{color=#fff}Bandit 1" "Ugh... come on..."
    "{color=#fff}Bandit 2" "Just fucking go."
    mc "Come on, Megan, let's go! They haven't seen us yet!"
    m "No... It's too late..."
    mc "No, it's not if we leave {b}right now."
    m "I screwed up..."
    mc "It's fine, Megan, we can still run."
    m "Well, I guess I'll just have to kill them all."
    mc "What?"
    play music battlemusic1
    "Megan takes off her cape and pulls a huge sword from her scabbard."
    scene megansword with dissolve
    mc "Hey, what are you doing?! There's too many of them!"
    m "Every fucking time! Why can't these missions go smoothly for once!"
    show megan berserk
    pause 2
    scene sneakend
    mc "Oh... fuck."
    scene meganberserk
    "Megan jumps into the clearing, startling the closest bandit, for only a moment before bringing her blade, crashing down on top of his head."
    play sound slash1
    "She rushes forward with a war cry and quickly downs the second bandit investigating before he can even yell for help. The entire camp seems to come alive as the commotion starts."
    "Megan is a black blur of deadly motion, quickly cutting down bandit after bandit as they rush her.  Soon, roughly a dozen men surround her, stumbling over the bodies of their comrades they attempt to attack Megan."
    "With improbable speed, she slices two of the incomers' throats with the large blade and kicks another in the crotch. As she dispatches the last of the bandits, the last survivor starts to run away from the slaughter."
    "She lifts her sword over her head and throws it at the bandit."
    "It fully lodges into his back and he falls to the ground. Then, the camp is silent."
    scene sneakend
    mc "O'... Merciful... Astylla..."
    play music night
    scene forrestn with fade
    show smirkme
    show suprised
    show bloodyme
    m "{i}huff huff huff{i} ...Whew! That was amazing!"
    mc "......"
    show angry
    mc "...What the fuck was that?!"
    scene forrestn
    show angry
    show talkwame
    show bloodyme
    m "What?"
    mc "Black Mist? You're more like Red Mist! \"The definition of carnage\"!"
    m "I got the job done, didn't I?"
    mc "You made yourself out to sound like the ultimate assassin! Not a berserker!"
    m "Just take the cows and go to the Guild."
    mc "What are you going to do?"
    m "Well, I can't go back covered in blood, can I?"
    mc "But what am I supposed to say about what happened here?"
    m "Think of something."
    mc "Really?"
    m "Come on, [mc]!"
    mc "Fine... ugh..."
    mc "I guess I could say you chased after some bandits that ran away or something."
    scene forrestn
    show talkwahme
    show thinkmc
    show bloodyme
    m "Nice, that's perfect! Tell July I went to track the bandits instead though."
    m "Chase doesn't seem to sound..."
    show talkwanmc
    mc "Stealthy?"
    m "Yeah, exactly! Oh, and another thing, do not speak a word about this to anyone."
    mc "What? Your slaughter fest?"
    m " Yeah, my slaughter fe- ...Ok, yeah, whatever you wanna call it."
    mc "It was a slaughter fest. It was the single largest amount of people I have ever seen killed in less than ten minutes."
    m "...Do I have your word?"
    mc "Sure, whatever."
    scene black with fade
    "You take the cows and go back to the Guild."
    scene adgc6
    j "[mc], what happened? Where's Megan?"
    scene adgc7
    mc "Yeah... some of the bandits got away and she... went to track them."
    scene adgc6
    j "Ok... and the cows?"
    scene adgc7
    mc "I retrieved them. They're outside."
    scene adgc2
    j "Great, I'll let the farmer know so he can come get them."
    j "Here's something for the trouble."
    play sound chime
    $ renpy.notify("{color=#fff}You gained 50 gold.")
    $ money += 50
    j "Oh, and [mc], about the forest incident..."
    scene adgc7
    mc "Come on July! It wasn't that dangerous."
    scene adgc6
    j "I wanted to apologize."
    mc "Wait, what?"
    j "I shouldn't have yelled, and I was in the wrong. I just didn't realize how much you've grown as an Adventurer. You're Bronze-Rank! You can handle yourself now."
    scene adgc7
    mc "Well... thanks, July. I know you were only trying to look out for me."
    scene adgc5
    j "Don't get me wrong, this doesn't mean you can go anywhere you want, of course. No going past the deep forest, got it?"
    scene adgc7
    mc "Yeah, yeah. Ok, fine."
    mc "Well, anyways, have a good night, July."
    $ persistent.sneakyMegan = True
    scene adgc2
    j "Goodnight, [mc]."
    $ sawmegan += 1
    $ meganq1 += 1
    $ time = 4
    jump home
