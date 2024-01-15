label splashscreen:
    if version < 141 and persistent.mmSong == "Disquiet.mp3":
        $ persistent.mmSong = "disquiet.mp3"
    if persistent.mmSong == "disquiet.mp3":
        jump moresplashscreen
    else:
        $ persistent.mmSong = "menu.mp3"
    label moresplashscreen:
    scene splashlogo with fade
    play sound bunis
    pause 4
    stop sound fadeout 1.2
    scene rinmakesgames with fade
    play music seagulls
    pause 4
    stop music fadeout 3.0
    scene splashwarning with fade
    pause 10
    scene main_menu with fade
    return


default choseTraits = False
default choseName = False
label start:
    $ persistent.mmSong = "menu.mp3"
    show screen skipintro
    scene black
    play music windhowl
    pause 2
    show text "{fi}{color=#fff}All the choices you make will affect the final outcome of the game.{/color}{/fi}" with dissolve
    pause 4
    hide text with dissolve
    pause 1
    show text "{fi}{color=#fff}Certain choices you make can lead to character deaths which will completely terminate their quest line.{/color}{/fi}" with dissolve
    pause 5
    hide text with dissolve
    show text "{fi}{color=#fff}Choose wisely.{/color}{/fi}" with dissolve
    pause 3
    hide text with dissolve
    pause 1
    show text "{color=#fff}{i}Mom! Dad!{/color}"
    window hide
    pause 2
    hide text with dissolve
    scene mcsml with dissolve
    pause 5
    scene jumpscare1
    pause 2
    play sound chime
    $ renpy.notify ("{color=#fff}Left click to go forward.")
    he "We need to go!"
    pause 3
    he "They're coming!"
    play sound campfire
    pause 2
    scene talkdream
    he "We need to go! NOW!"
    window hide
    pause 1
    he "MOM! DAD!"
    play sound bamintro2
    $renpy.pause(delay = 2.25, hard = True)
    stop music
    $renpy.pause(delay = 0.3, hard = True)
    show animation1
    $renpy.pause(delay = 2.4, hard = True)
    scene jumpscare5
    scene black with flash
    he "{i}Ugh..."
    play music home fadein 1
    pause 0.5
    scene black with flash
    pause 0.2
    scene wakeup1 with flash
    he "{i}...That dream again."
    he "{i}What were they saying?"
    he "{i}...It sounded like-"
    scene wakeup2
    he "{i}Wait... the sun is already up!"
    scene wakeup1
    he "{i}Damn it! I've overslept!"
    he "{i}God... looks like I'm gonna be late on the first day of Academy."
    show text "{color=#fff}You quickly get up and get changed.{/color}" at truecenter with dissolve
    pause 3
    hide text with dissolve
    scene homedayblur
    he "Wait- I haven't had breakfast..."
    menu:
        "Eat something":
            $ mcBreakfast = True
            "You stop another few minutes to eat something before heading out."
            he "Alright, time to go."
        "Get to the Academy on time":
            $ mcBreakfast = False
            show animation2
            "You decide you can't be late on your first day and quickly head out."
    hide animation2
label trait:
    scene traitsbg with fade
    show text "{color=#fff}Choose your character trait." with dissolve
    pause 2
    hide text with dissolve
    call screen traits
    pause 1
label out1:
    $ choseTraits = True
    scene villageback with fade
    show thinkmc with easeinright
    he "Mmh... the Academy should be right around the corner..."
    show sadtalkuncle with easeinleft
    hide thinkmc
    show suprised
    u "{i}Pant... Pant..."
    show suprised
    show sadtalkuncle
    u "Whew... Thank god your still here."
    show unclenormal
    hide suprised
    hide lookdownsupmc
    show talkwamc
    he "Uncle Pete! What's up?"
    hide talkwamc
    show smilemc
    show uncletalk
    u "Huff... huff... Hey kid."
    u "It's your first day of Academy, right?"
    hide uncletalk
    show unclenormal
    show talkmc
    he "Yeah, I'm heading there right now."
    hide talkmc
    show smilemc
    hide unclenormal
    show uncletalk
    u "Then I want you to have this."
    scene sword with fade
    # We need a new sword CG
    he "What?! Really?"
    u "Of course. It's my old sword."
    he "Wow... Uncle, I don't know what to say... are you sure?"
    u "Yeah. An old fisherman like me has no use for it now."
    u "Oh, and take these as well. You wanted to join the Adventurers' Guild, didn't you?"
    $ money += 30
    $ renpy.notify("{color=#FFBB00}You receive 30 silver coins")
    menu:
        "Thank you so much, Uncle":
            scene villageback
            show unclesmilet
            show talksadhappymc
            he "Thank you so much, Uncle."
            show screen notice
            pause 2
            hide screen notice
            $ unclerel += 10
            show uncletalk
            show normalmc
            u "No problem, kiddo!"
            hide uncletalk
            show unclenormal
            hide talksadhappymc
            show talkwamc
            he "This sword looks really well made. How did you even get it?"
            hide talkwamc
            hide unclenormal
            show normalmc
            show unclesmilet
            u "You know how I used to be a traveling merchant back in the day?"
            u "I used to come by things like this all the time."
            hide unclesmilet
            hide normalmc
        "Thank you, but I gotta go or else I'll be late":
            scene villageback
            show unclesmilet
            show talksadhappymc
            he "Thank you so much, Uncle! But I'm late I really gotta go!"
            show uncletalk
            show normalmc
            u "No problem, kiddo!"
            hide uncletalk
            hide talksadhappymc
            hide normalmc
        "Well, whatever give it here. I'm late":
            scene villageback
            show unclesmilet
            show talkmc
            "Well, whatever give it here. I'm late."
            $ unclerel -= 10
            show saduncle
            show screen notice2
            pause 2
            hide screen notice2
            pause 0.5
            hide saduncle
    show normalmc
    show uncletalk
    u "Y'know son, being part of the first generation grown without hearing about the Demon King really is great."
    u "Back when I was a young lad you'd hardly see anyone so lightheartedly excited about going to the Academy."
    hide normalmc
    show questionmc
    he "Huh, how come? Were you all scared of the Demon King?"
    hide questionmc
    show questionmc
    u "No, no. You see, it didn't work like it does nowadays. Once we'd be done with the academy we'd be sent to fight the Demon Army regardless of wanting or not. Joining the army wasn't voluntary."
    u "A lot of people were definitely scared of dying, and a lot were very excited to help defend the country..."
    u "...but nobody looked as carefree as you do today. I'm so glad everything went well."
    "As he says those last words, you think you hear some melancholy in his voice, but he quickly changes subject."
    u "Oh! Another thing."
    u "Gabrial's back in town."
    u "She'll be at the Academy too."
    hide normalmc
    hide uncletalk
    show unclenormal
    show talksadhappymc
    he "Really? It's been almost six years since she left."
    hide unclenormal
    hide talksadhappymc
    show normalmc
    show uncletalk
    u "I guess she finished her studies at Westian."
    show talkhappymc
    he "Yeah."
    hide talkhappymc
    u "She was the first friend you've made when I first brought you to Randel. Do you remember that?"
    he "Yeah."
    u "You two would do everything together... Heh, those were the days."
    u "I used to imagine the two of you getting married and settling down here."
    show angry
    he "Uncle Pete!"
    hide angry
    show angrynmc
    # Need an angry blush model
    show unclesmilet
    u "Hahaha, I'm just messing with ya. Hahaha, look how red your face is."
    he "{i}Uncle Pete really likes to make fun of me..."
    u "Don't take anything this old geezer says seriously. You just go out there and do your best, you hear me?"
    show talksadhappymc
    hide angrynmc
    he "I will..."
    show talksadhappymc
    he "{i}Shit, I forgot I'm late!"
    he "Nice talking to you, Uncle. But I gotta go now, I'm already late."
    he "Bye!"
    he "And thanks for the sword!"
    scene villageback
    show unclenormal
    show normalmc
    hide normalmc with easeoutleft
    hide unclenormal with dissolve
    show uncletalkturn with dissolve
    u "No problem!"
    u "Ah... They grow up so fast."
    stop music
    scene academy with fade
    show normalmc with easeinright
    if mcBreakfast == True:
        he "{i}God- The first period is about to start!"
    if mcBreakfast == False:
        he "{i}I made it. It looks like I'm still early."
    he "{i}Hmm... It looks bigger from the outside..."
    hide normalmc
    show thinkmc
    he "{i}......"
    he "{i}Is that girl in the hoodie staring at me?"
    he "{i}Why is she staring at me?"
    menu:
        "Maybe she likes me...":
            $ mcBold = True
            he "{i}Maybe she likes me...?"
            he "......"
            he "{i}How is that the first thing that comes to my head?"
            he "{i}I mean, sure, I'm hot, but still."
        "It's probably nothing":
            $ normalmc = True
            show normalmc
            he "{i}It's probably nothing"
            hide normalmc
        "...She's judging me":
            $ mcTimid = True
            show lookdownsupmc
            he "{i}Do I look weird?"
            he "{i}I knew I should've gotten some nicer clothes before going to the Academy..."
            hide lookdownsupmc
        "It's definitely because I'm late" if mcBreakfast == True:
            $ mcTimid = True
            show lookdownsupmc
            he "{i}...Is it because I'm late? Do I look that much out of place?"
            he "{i}That's what I get for having breakfast when I'm already late..."
            hide lookdownsupmc
    if mcBold == True:
        show smilemc
        he "{i}Ohoh, she's coming this way! Guess I was right."
    if mcNormal == True:
        show mcNormal
        he "{i}Wait, she's coming this way!"
    if mcTimid == True:
        show surprisedblushmc
        he "{i}Wait! She's coming this way!"
        he "{i}Just relax, act cool."
    scene academytalkblr
    if mcTimid == True:
        show surprisedblushmc
    if mcBold == True:
        show smilemc
    if mcNormal == True:
        show normalmc
    show talkgabe
    "{color=#DB93FF}Hoodie girl" "Hi."
    show normalgabe
    if mcBold == True:
        he "{i}There she goes! I knew I'd be popular the moment I stepped in here!"
    if mcNormal == True:
        he "{i}She just talked to me."
        he "..."
    if mcTimid == True:
        he "{i}She just talked to me."
        he "......"
        pause 5
        he "{i}I should probably say something..."
    menu:
        "Hey":
            if mcBold == False:
                show blushtalkhappymc
                he "Hey."
                hide normalgabe
                hide blushtalkhappymc
                hide normalgabe
                show normalmc
                show talkgabe
                "{color=#DB93FF}Hoodie girl" "It's so good to see you again. It's been so long."
            else:
                show talkwamc
                he "Hey."
                hide normalgabe
                hide talkwamc
                hide normalgabe
                show normalmc
                show talkgabe
                "{color=#DB93FF}Hoodie girl" "It's so good to see you again. It's been so long."
        "Hey, babe":
            $ heyBabe = True
            if mcBold == False:
                he "{i}Ok, be confident. Girls like that."
                he "{i}...I think."
                pause 1
                hide surprisedblushmc
                show talkwamc
                he "Hey, babe."
                pause 3
                show wagabe
                he "{i}Uh-oh. I guess she didn't like that."
                pause 2
                hide wagabe
                hide normalgabe
                hide talkwamc
                show normalmc
                show talkgabe
                "{color=#DB93FF}Hoodie girl" "...It's good seeing you too. It's been so long."
            else:
                he "{i}Heh, time to shine."
                he "Hey, babe."
                pause 3
                show wagabe
                he "{i}Huh... That was an unexpected reaction."
                pause 2
                hide wagabe
                hide normalgabe
                hide talkwamc
                show normalmc
                show talkgabe
                "{color=#DB93FF}Hoodie girl" "...It's good seeing you too. It's been so long."
    show suprised
    pause 1
    show talkwamc
    he "Do I know y-"
    he "Wait, Gabe, is that you!?"
    hide talkgabe
    hide talkwamc
    show normalmc
    show talkwagabe
    g "Of course it's me, dummy!"
    he "Sorry, I hadn't recognized you."
    if heyBabe == True:
        g "Really? Is that why you were trying to pick me up?"
        if mcBold == True:
            show talkwamc
            he "...Maybe."
        else:
            show talksadhappymc
            he "...No, sorry about that."
            hide talksadhappymc
            show talkwagabe
            g "It's alright."
        show talksadhappymc
        he "You know, you look totally different."
        show talkwagabe
        show smilemc
        g "Really?"
        he "Yeah."
    else:
        g "You couldn't recognize me? Really? I'm your best friend!"
        hide talkwagabe
        show normalgabe
        show talksadhappymc
        he "How could I? You look totally different!"
        show talkwagabe
        show smilemc
        g "Really?"
        he "Yeah."
    menu:
        "You look kinda shifty":
            hide smilemc
            show talksadhappymc
            he "I don't know... you look kinda shifty with the hoodie."
            show wagabe
            pause 2
            hide wagabe
        "You look cute":
            $ gaberel += 5
            if mcBold == False:
                show blushtalkhappymc
            else:
                show talkwamc
            he "You look kinda cute with the hoodie."
            $ gabeLooksCute = True
            show cutegabe
            g "......"
            g "It's not supposed to look cute."
            show screen notice
            pause 2
            hide screen notice
            show worriedblushdgabe
            show talkwamc
            he "Oooh, I see."
            g "Wh-what?"
            he "You're going for that {b}mysterious{/b} look, aren't you?"
            hide worriedblushdgabe
            show smilemc
            show cutegabeu
            g "N-No."
            he "Well, that's good then, because you definitely don't look mysterious."
            hide cutegabe
            show angrygabeblush
            show smileecmc
            show yellblushgabe
            g "Come on, man! I put a lot of effort into this outfit!"
            g "A-And I'm not trying to act mysterious, alright!?"
            he "Ok, ok! I was just messing with you."
            g "Jeez, I forgot how much of a jerk you can be."
            hide yellblushgabe
            show angrygabeblush
            hide worriedblushdgabe
            hide angrygabeblush
            hide cutegabeu
            hide smileecmc
            hide talkwamc
            hide blushtalkhappymc
    scene academytalkblr
    show talkwamc
    show normalgabe
    he "Heh... So, how was Westian?"
    show smilemc
    show talkgabe
    g "It was... ok."
    hide talkgabe
    hide smilemc
    show talkwamc
    he "I guess you're a very powerful mage now, aren't you?"
    hide talkwamc
    show normalmc
    show talkgabe
    g "No, dummy. They only teach how to be fluent in Astyllian at Westian. I only read and studied the spells. Using them is a whole different story... It's not really a lot."
    hide talkgabe
    show thinkmc
    menu:
        "Humble as usual":
            $ gaberel += 5
            show talkwamc
            he "Six years have passed and you're still humble as ever."
            hide talkwamc
            show smilemc
            show cutegabe
            g "It's true, it wasn't much, I basically just learnt Astyllian..."
            hide smilemc
            show talkwamc
            he "Oh yes, you \"just learnt Astyllian\". We both know how impressing that is, c'mon."
            hide talkwamc
            show smilemc
            g "Shuddup."
            hide smilemc
            show talkwamc
            he "Will you admit you're great when you'll surpass everyone else in our magic arts class?"
            hide talkwamc
            show smilemc
            g "Nhhh... Fine! Shut up already, you jerk."
            hide cutegabe
            show normalgabe
            hide smilemc
            show talkwamc
            he "Eheh, alright, alright, I'll stop teasing you."
            hide talkwamc
            show smilemc
        "That still sounds interesting":
            show talkwamc
            $ gabeFeltLikeIt = True
            he "Well, that still sounds like it was a nice experience."
            he "Y'know, learning Astyllian, the Elven tongue, it's not like everyone just does that."
            he "I wish I knew Astyllian already, I could focus on all the other classes without problems."
            hide talkwamc
            show smilemc
            show talkgabe
            g "Well, I guess you're right."
            g "I still kinda feel like it was a waste of time though."
            g "It's why I came here. They say that the new magic arts teacher is really good."
            hide talkgabe
            hide smilemc
            show talkwamc
            he "...Did you really come back to Randel by yourself for a magical arts teacher?"
            hide talkwamc
            show smilemc
            show sadgabe
            g "..."
            hide sadgabe
            show talksgabe
            g "...I just felt like coming back home."
            hide talksgabe
            show sadgabe
            hide smilemc
            show thinkmc
            he "{i}Huh?"
            hide thinkmc
            show talkmc
            he "Well... I'm glad you came back."
            hide talkmc
            show smilemc
            hide sadgabe
        "So you wasted your time?":
            show talkmc
            he "What? So that means you know all the spells but can't use them?"
            hide talkmc
            show smilemc
            show talkgabe
            g "Yeah, that's why I came here. They say that the new magic arts teacher is really good."
            hide smilemc
            hide talkgabe
            show talkwamc
            he "So... you spent six years reading spell books?"
            hide suprised
            hide talkwamc
            hide talksadhappymc
            show normalmc
            show talkgabe
            g "Yeah, pretty much."
            show normalgabe
            show talksadhappymc
            he "That... sounds kinda boring."
            hide suprised
            hide talksadhappymc
            show normalmc
            show talkwagabe
            g "...Kinda."
            hide talkwagabe
        "I'll surpass you in no time!":
            $ surpassGabe = True
            show talkwamc
            he "Pfft, guess it'll be easy to surpass you in all classes, then."
            hide talkwamc
            show smilemc
            show talkgabe
            g "Oh, really?"
            hide talkgabe
            hide smilemc
            show talkwamc
            he "Of course, I'll become a mage just to spite you."
            hide talkwamc
            show smilemc
            show talkwagabe
            g "Oh, I really wanna see you try."
            hide talkwagabe
            hide smilemc
            show smileecmc
            he "Eheheh."
            hide smileecmc
            hide talkmc
            show smilemc
    show talkwagabe
    g "Well, enough about me, how's your life?"
    if chartrait == 1 :
        g "Still a shut-in reading books all day?"
        show angry
        he "Shut-in? You're one to talk. You were the same."
        g "I definitely went out more than you did. You wouldn't even go to the library, I had to bring all the books to your lazy ass."
        hide angry
        show talkwanmc
        he "Fine, you have a point... I just liked staying home."
        g "So, who brought you the books after I left? ...Oh wait, let me guess, Uncle Pete?"
        hide talkwanmc
        show talksadhappymc
        he "Yeah."
        g "What a lazy dork."
        he "Ok, ok, I'm better now, see? I'm going out more now."
        g "Oh yeah, of course."
        hide talksadhappymc
        he "{i}Gabe's right. She was kind of the only friend I had when I was little... She would always come to my house with books that weìd read together all day."
    if chartrait == 2:
        g "Still getting beaten up all the time?"
        show angry
        he "Beaten up? I never got beaten up!"
        g "Ooh, sure... I wonder who that boy was? The one I'd have to cover with bandages every time he'd come to my house after a fight."
        he "That happened like one time."
        g "Hmm... Ok, whatever you say, tough guy."
        he "{i}Gabe's right. I really did go to her every time after I got into a fight. I could always count on her."
        show talkmc
        hide angry
        he "I'm not that much of a hothead now"
        g "Yeah. I noticed your limbs are intact, so I guess you're right."
        show angry
        hide talkmc
        he "What's that supposed to mean?"
        g "Hehehe..."
        hide angry
    if chartrait == 3:
        g "How's the gang?"
        show talkwanmc
        he "The gang?"
        g "Yeah, the gang, your buddies. Daniel, Justin... The guys you spent most of your time playing with."
        he "Oh, yeah... We haven't hung out in a while."
        g "What, really?"
        he "Yeah."
        g "Why?"
        he "Eh..."
        he "No reason in particular, really, we just grew up."
        g "That's sad. You guys were running around all day."
        hide talkwanmc
        show talksadhappymc
        he "Well, it's not like we hate each other."
        he "{i}Thinking back, why exactly did we stop hanging out? We were so close."
        hide talksadhappymc
    if mcBreakfast == False:
        "Your stomach grumbles"
        he "{i}Oh right. I was in such a hurry that I forgot to eat before coming here."
        g "...You seem hungry."
        he "No I'm not."
        "Gabe takes out a sandwich from her bag"
        show bread
        g "{i}sigh{/i} ...Want a sandwich?"
        menu:
            "Yes please":
                $ gabeSandwich = True
                he "Yes please."
                g "Well, you sure haven't changed, you dork."
                "She hands you the sandwich and you start eating it"
                he "Wow, this *munch* is good... Did you make it?"
                g "Yeah."
                he "I didn't know you were such a good cook!"
                g "Making a sandwich isn't actually considered cooking, but I'll take the compliment."
                he "It's way better than the ones Uncle Pete used to make..."
                g "Heheh, thanks."
                $ gaberel += 5
            "Grab the sandwich but don't say thanks.":
                $ gabeSandwich = True
                g "Wh- You're welcome."
                he "{i}Nom nom..."
            "No, thanks":
                he "No, thanks."
                g "Your loss."
    hide bread
    g "Ok, that's enough chatting. Let's go to the class, shall we?"
    show talkwamc
    he "Sure. After you, ma'am."
    g "Hehehe..."
    scene academytalkblr
    show normalgabe
    show talkhappymc
    pause 0.4
    show smilemc
    hide normalgabe with easeoutright
    "{i}Gabe's really changed a lot. It was really nice talking to her after all this time."
    pause 0.2
    show suprised
    "{color=#fff}Groundskeeper" "Hey, lad, wait up!"
    show normalgk with easeinleft
    hide suprised
    show normalmc
    pause 0.3
    show talkgk
    "{color=#fff}Groundskeeper" "I got a little job for you. Go get them boxes to the store room."
    hide talkgk
    show talkmc
    he "Why me? Aren't you the groundskeeper here?"
    he "It's your job."
    show talkgk
    hide talkmc
    "{color=#fff}Groundskeeper" "You kids these days! I got enough work as is. Go and move those boxes already!"
    "{color=#fff}Groundskeeper" "I already sent another one of you brats to clean the place up."
    hide talkgk
    show talksadhappymc
    he "...But my class is about to start."
    hide talksadhappymc
    show talkgk
    "{color=#fff}Groundskeeper" "So what? Who needs em? Now take the boxes and go!"
    scene black
    show text "{color=fff}You reluctantly take the boxes to the storeroom." at truecenter with dissolve
    pause 4
    hide text with dissolve
    scene storeroomblr
    show normalmc with easeinright
    pause 2
    show thinkmc
    he "{i}Phew, I finally made it. Those boxes were heavy..."
    he "{i}......"
    he "{i}Wait, didn't the groundskeeper send another student to clean this place? It looks really dusty."
    he "{i}I bet they bailed out. I should've probably done the same."
    he "{i}Anyway, my job here is done. I gotta ru-"
    "{color=#EFC667}Unknown voice" "{i}Zzz..."
    hide thinkmc
    show suprised
    he "...The hell was that?"
    "{color=#EFC667}Unknown voice" "{i}Zzz......"
    he "{i}There it is again."
    hide suprised
    show thinkmc
    "{i}It sounds like someone's sleeping."
    "{i}It's coming from one of these lockers."
    scene sleepmclose with fade
    "{color=#EFC667}Unknown voice" "{i}ZZZZ......"
    he "There's someone inside."
    menu:
        "Open":
            $ persistent.scarLocker = True
            scene sleepm with vpunch
            pause 1
            he "{i}Shit!"
            he "{i}Who is this? Is this who the groundskeeper sent?"
            scene sleepm
            pause 2
            he "{i}Judging by her outfit, she looks like a mage."
            he "{i}Damn mages and their sexy outfits."
            menu:
                "Peek":
                    $ peek = True
                    he "{i}Man, her outfit is so revealing. It's making me super horny right now."
                    he "{i}Might as well take a little peek..."
                    scene sleepm2 with dissolve
                    pause 4
                    he "{i}She's not wearing any panties!"
                    he "{i}Ok... slowly... just a little more..."
                    scene sleepm2
                    pause 2
                    scene sleepm2 with hpunch
                    he "{i}Shit! She's waking up, damn it!"
                    scene storeroomblr
                    show normalmc
                    show yawnm
                    "{color=#EFC667}Mage" "{i}Yaaawn..."
                    hide yawnm
                    show talkm
                    "{color=#EFC667}Mage" "Hi."
                    show talkmc
                    he "Hi..."
                    hide talkmc
                    "{i}Why... Why, Lord? I was so close."
                    jump mage2
                "Wake her up":
                    he "{i}I'm not a damn pervert. I gotta wake her up."
                    he "Hey, wake up."
                    "{color=#EFC667}Mage" "Ngh... What... Huh?"
                    jump mage
        "Knock":
            he "{i}I should knock, that's the decent thing to do, right?"
            he "Hey, wake up!"
            "You knock on the locker a few times"
            "{color=#EFC667}Unknown voice" "Whoa, ow! Wh... What the hell?"
            he "{i}Sounds like she's waking up."
            jump mage

label mage:
    scene storeroomblr
    show normalmc
    show yawnm
    "{color=#EFC667}Mage girl" "{i}Yaaawn..."
    hide yawnm
    show talkm
    "{color=#EFC667}Mage girl" "Hello there."
    hide talkm
    show normalm
    show talkmc
    he "Hi."
    hide talkmc

label mage2:
    show normalm
    show talkm
    "{color=#EFC667}Mage girl" "Man, how long was I out? That was one good nap."
    hide talkm
    show talksadhappymc
    he "I don't know."
    he "{i}She looks... weirdly familiar."
    he "...Did the groundskeeper send you here to clean the place?"
    hide talksadhappymc
    show sadtalkm
    "{color=#EFC667}Mage girl" "Oh right, I totally forgot! Yeah, yeah, he did send me here, but then I saw this small locker... It looked so cozy that I had to get inside of it. Then, before I knew it, I fell asleep!"
    hide sadtalkm
    show sadsmilem
    show talkwamc
    he "Just like that."
    hide talkwamc
    hide normalmc
    show smilemc
    hide sadsmilem
    show talksleepm
    "{color=#EFC667}Mage girl" "Just like that."
    hide talksleepm
    show talkhappymc
    he "So, it's your first day too, huh?"
    hide talkwamc
    hide talkhappymc
    show talkm
    "{color=#EFC667}Mage girl" "Mh...? Oh! Yeah."
    s "The name's Scarlet, by the way."
    hide talkm
    show talkhappymc
    he "Nice to meet you."
    hide talkhappymc
    show smilemc
    pause 1
    show wasmilem
    pause 3
    hide smilemc
    show talkwamc
    he "What?"
    hide talkwamc
    show smilemc
    show talkwam
    s "And you are?"
    hide talkwam
    show talksadhappymc
    $ mcn = renpy.input("Oh, sorry, I'm...")
    if mcn.strip() == "":
        s "What? You didn't say anything."
        $ mcn = renpy.input("I said my name is...")
        if mcn.strip() == "":
            "Bunis" "Hello, I'm the developer! Please enter a name. If not, a default name will be given."
            $ mcn = renpy.input("My name is...")
            if mcn.strip() == "":
                "{color=#FF8EF5}Rin the Other Dev" "Guess you're going with the default name, {b}Robin{/b}."
                $ mcn = "Robin"
    $ choseName = True
    show talkwam
    hide talksadhappymc
    s "Alright, [mc], it's a pleasure to meet you as well. Now then, are you going to help me clean this place?"
    hide talkwam
    show angry
    mc "Isn't that supposed to be your job?"
    hide angry
    show angrynmc
    show sadtalkm
    s "Oh, come on, [mc], help me out! I can't do all this by myself!"
    hide sadtalkm
    show plsm
    s "Pweeease??"
    menu:
        "I'm late for class, sorry":
            hide angrynmc
            hide plsm
            show talksadhappymc
            show sadm
            mc "I'm late for class, sorry, I really gotta go."
            hide talksadhappymc
            show talkwanmc
            mc "Aren't you coming? Our class must've started by now."
            show normalmc
            show sadtalkm
            s "I've still got cleaning to do. You go ahead, I'll come after I finish this up."
            show talkwanmc
            mc "Alright, try not to be late."
            jump class1
        "Ok, fine!":
            $ scarel += 10
            hide angrynmc
            hide plsm
            show angry
            mc "Ok, fine!"
            show screen notice
            pause 2
            hide screen notice
            hide angry
            show angrynmc
            show teethecm
            s "Yaaay!"
            show talkmc
            mc "Uhm... I don't have a broom."
            hide teethecm
            show talkm
            hide talkmc
            s "You can have mine!"
            show normalm
            hide talkm
            show talkwanmc
            mc "Then what are you going to use?"
            hide talkwanmc
            show talkm
            s "Oh, I have my staff here. I can turn it into just about anything."
            hide talkm
            show talkwamc
            hide angrynmc
            mc "Really? Wow, that's cool."
            show normalmc
            hide talkwamc
            show talkwam
            s "Yeah, I know, I use it for {b}all{/b} kinds of things..."
            show thinkmc
            show anythingm
            hide talkwam
            pause
            show talkwanmc
            mc "{i}Wait, what's with that look? Does she mean what I think she means?"
            show talksadhappymc
            mc "Uhm... Yeah... Haha... That's, uhm, really convenient..."
            hide talksadhappymc
            hide anythingm
            show yawnm
            s "...You didn't get it?"
            s "Sigh... I thought kids these days were more open about this stuff."
            hide yawnm
            show thinkmc
            mc "What?"
            s "Heh... Just forget it."
            mc "{i}She did mean it! ...Or did she?"
            "The two of you start cleaning."
            show sweep with fade
            "After about a minute, Scarlet dozes off."
            show sweep with vpunch
            mc "You're asleep AGAIN?!"
            s "Yeah I'm so tired... But, hey, look, I'm still cleaning."
            mc "That's cheating."
            s "{i}Zzz... Zzz..."
            mc "{i}What's with this girl? Always falling asleep... And how is she so good at magic? She's supposed to be a recruit."
            mc "{i}...Wait, are these the minimum requirements to be a mage? This girl's casting spells and has a shape-shifting staff while I can barely swing a sword!"
            scene black  with fade
            show text "{color=fff}You finally finish cleaning up the place." at truecenter
            pause 2
            hide text with fade
            scene storeroomblr
            show normalmc
            pause 1
            show yawnm
            pause 1
            hide yawnm
            show talkm
            s "Yay! We did it!"
            hide talkm
            show normalm
            show talkwanmc
            mc "Technically, it was me and your staff."
            hide talkwanmc
            show teethecm
            s "Hehe..."
            show talkmc
            mc "Ok, now we seriously need to go."
            hide talkmc
            show uhm
            s "We?"
            show talkwanmc
            mc "Yeah {b}we{/b}! Aren't you coming? Our class must've started already!"
            hide talkwanmc
            show sadtalkm
            s "Oh yeah, I'm coming. You go ahead. I have to get some stuff."
            show sadsmilem
            show talkwanmc
            mc "What- Alright, whatever, I'm going. Don't be late."
            hide sadsmilem
            hide talkwanmc
            hide normalmc with easeoutright
            show sadtalkm
            s "O-Ok... see you soon!"
            show sadsmilem
            mc "Bye!"

label class1:
    scene black
    show text "{color=fff}You go to the class door. You slowly poke your head in and scout out the surroundings." at truecenter with fade
    pause 2.5
    hide text with fade
    scene lecture with fade
    "The class has already started, but the teacher hasn't noticed you yet. You look around for a space to slowly creep in."
    "Then you see someone waving from the corner of the class."
    scene class with fade
    "Looks like Gabrial saved you a seat."
    "You slowly duck, stealthily move to Gabrial and get seated."
    scene lecturetalk with fade
    g "What took you so long?"
    mc "Uhh... I'll explain later. What did I miss?"
    scene lecture
    g "Uh... Nothing really that important."
    g "He's just been rambling on and on about rules and discipline all this time."
    mc "Ok, that's good to know. Thank you for saving me a seat, by the way."
    scene lecturetalk
    g "Oh, it's nothing."
    b "...so, even though we're living the most peaceful times Astylla has seen in the past four centuries, you need to take this seriously."
    b "Sometimes I'm amazed by the lack of knowledge some of the common folks around here have, so we'll start with general culture..."
    scene black with dissolve
    show text "{color=fff}The class goes on for a while and you quickly get bored." at truecenter with fade
    pause 2.5
    hide text with fade
    scene lecturetalk
    mc "{i}Scarlet still hasn't shown up... She must have fallen asleep again."
    mc "{i}Man, this is so boring..."
    menu:
        "Look around the class":
            $ sawcynth += 1
            $ persistent.stareCynthia = True
            mc"{i}Might as well look around the class. Who knows what kind of cute girls are here..."
            "You look around the class slowly so that no one notices you... Especially Gabe."
            "Then your eyes fix on a girl."
            scene stare with fade
            mc "{i}Wow, she's pretty."
            mc "{i}I haven't seen her before..."
            g "Cynthia Gardner."
            scene lecture
            mc "Wh-What? Who?"
            g "I know you were staring at her, [mc]."
            menu:
                "No, I was not":
                    mc "No, I was not..."
                    g "Pfft. Yeah, right."
                "Ok, fine, you caught me":
                    mc "Ok, fine, you caught me... So what? Can't a guy look at a cute girl every once in a while?"
                    if gabeLooksCute == True:
                        $ gaberel += 5
                        mc "After all, wasn't I looking at you as well earlier?"
                        g "Wh-What? Sh-Shut up."
                        mc "...And now you're blushing."
                        g "I'm not!"
                        mc "Eheh, sure thing."
                        jump threelinesbelowthisone
                    g "Jeez, [mc], I didn't know you were such a perv."
                    mc "Perv?! I was just looking at her!"
                    g "Yeah, right."
            label threelinesbelowthisone:
            mc "Anyways... Is she new in town? I've never seen her before."
            g "Yeah, she's from Thane."
            mc "In the east?"
            g "Yeah. Thane is under high alert, don't you know? "
            g "Since it's right below Fort Hern. If the fort goes down, they'll be the first to get attacked."
            mc "So what? Hern's still holding, right?"
            g "Yeah, but for how long? They say the Demon King's army is getting stronger."
            menu:
                "It will be up to us to protect it then":
                    $ mcMrHero = True
                    mc "It will be up to us to protect it then."
                    g "......"
                    g "Pfft- Hahahah! \"It will be up to us to protect it.\" ...Hahaha, you should hear yourself!"
                    mc "What? I'm serious. It's the reason they send us to the Academy, to prepare us in the case of war."
                    g "Haha! Yeah, yeah. Ok, almighty [mc], you'll be there to save us!"
                    mc "...Meanie."
                "Say nothing":
                    mc "Mh."
            g "Anyway, back to Cynthia."
            g "From what I've heard she's a really nice person. Friendly, caring... and beautiful of course."
            mc "Mh..."
            g "Don't even think about it, [mc]. You don't stand a chance. All the boys in the Academy are going after her."
            mc "That's harsh."
            g "What? I'm just being honest."
            mc "Yes, yes. Of course."
            "The class goes on for a while."
            mc "{i}Ugh, this is so boring... I'm starting to fall asleep..."
            menu:
                "Stare at Cynthia again":
                    mc "{i}Might as well look at Cynthia again."
                    "You slowly look at Cynthia from the corner of your eye so that Gabe doesn't notice."
                    scene stare
                    mc "She looks so pretty..."
                    scene stare
                    pause
                    mc "Like... An... Angel..."
                    scene stare1 with dissolve
                    mc "An...gel..."
                    scene black with dissolve
                    pause
                    g "{size=-5}[mc], wake up! Goddammit, [mc]! Wake up!"
                    "You hear Gabe whisper harshly as she nudges you with her elbow."
                    scene lecturetalk with vpunch
                    "You automatically stand up."
                    b "Glad to see you're up... Mister...?"
                    mc "[mc], sir."
                    b "Ok, Mr. [mc], I see you found the lesson to be boring... Then I assume you already knew what I was teaching?"
                    mc "No, sir, I... Wha-"
                    $ caughtboris += 1
                    b "Ok then. Let's see, Mr. [mc], would you kindly tell me what I was teaching just now?"
                    menu:
                        "History of Astylla":
                            mc "History of Astylla?"
                            b "It seems like you haven't paid the slightest attention...{p}{size=+4}GET OUT OF MY CLASS, NOW!"
                            $ kickedOutOfClass = True
                            jump out
                        "Forts of Astylla":
                            mc "Forts of Astylla."
                            b "Ok, it seems you paid more attention than I initially thought."
                            b "Ok then, Mr. [mc], what is the name of the fort located at the east border of Astylla?"
                            if chartrait == 1:
                                play sound chime
                                $ renpy.notify("{color=#fff}Bookworm check: {color=#00C413}Success!")
                                mc "{i}Wait I've read about this. It's Fort Hern."
                            menu:
                                "Fort Hern":
                                    mc "Fort Hern."
                                    b "Oh... uhm... It seems like you actually did know... O-Ok then, sit down and don't let me catch you dozing off again."
                                    "You sit down and Gabe gives you a thumbs up."
                                    g "Nice work, [mc]."
                                    "The class goes on for what feels like an eternity."
                                    jump out
                                "Westian":
                                    mc "Westian."
                                    b "I'm sorry, Mr. [mc], but that is incorrect... I'll forgive you this time. Don't let me catch you dozing off again... you may sit down. "
                                    "The class goes on for what feels like an eternity."
                                    jump out
                                "Mordor":
                                    mc "Mordor."
                                    b "Mordor? ...What? Was that some place you saw in your dreams while you were sleeping, Mr. [mc]?"
                                    b "I'm sorry, Mr. [mc], but that is incorrect... I'll forgive you this time. Don't let me catch you dozing off again... you may sit down. "
                                    "The class goes on for what feels like an eternity."
                                    jump out
                        "Astyllian Mages":
                            mc "...Astyllian mages?"
                            b "It seems like you haven't paid the slightest attention...{p}{size=+4}GET OUT OF MY CLASS, NOW!"
                            $ kickedOutOfClass = True
                            jump out
                        "Angels":
                            mc "Uhm... Angels?"
                            b "WHAT?! {size=+4}GET OUT OF MY CLASS, NOW!"
                            $ kickedOutOfClass = True
                            jump out
                "No, I have to focus on the class":
                    he "{i}No, I have to focus. This might be important."
                    jump DemonKingTalk
        "No, I have to focus. This might be important":
            mc "{i}No, I have to focus. This might be important."
            jump DemonKingTalk

label DemonKingTalk:
    b "Astylla has four main forts built from the kingdom's walls."
    scene lecture
    pause
    scene lecturedraw
    b "In the south we have Dermis, in the north we have Winden, in the west, Dorm, and in the east we have the biggest: Fort Hern."
    b "...As you know, the Dark Lands are  currently beyond Hern to the east. That is where the Demon King's army is stationed."
    b "This is why Hern is where most of our army is deployed. It's what blocks the Demon King's army advance."
    b "...and despite the Demon King having died 14 years ago, his generals and his army still stands. Though weakened, they are far greater in numbers compared to our forces."
    b "Never forget that the threat still remains."
    b "Luckily for us, though, Fort Hern is one of the finest pieces of bellic architecture in our country."
    b "It was built to last and through the centuries it hasn't been conquered once despite the countless sieges from the Demon King's army."
    "Gabe poke your arm."
    g "You know how they say that Gladius Hans killed the Demon King during the last Hern Siege?"
    mc "Yeah?"
    g "Well, while I was in Westian I've heard of some rumors. It seems no one is sure if the Demon King actually died. After the celebrations Hans' whole party just vanished."
    mc "Well yeah, they went into retirement, didn't they?"
    g "Well, that's what people say, but no one knows where they are."
    mc "So you're saying they ran away?"
    g "...Something like that, yeah."
    mc "Why?"
    g "Who knows? Some say that when the Demon King dies part of his soul is transfused with his slayer."
    g "So they sealed themself off somewhere to contain the Demon King."
    mc "Why not just kill Hans?"
    g "What?"
    mc "I mean, if Gladius Hans killed himself, wouldn't the Demon King die with him?"
    g "Well, possibly, yes. But maybe there's something that prevents that."
    g "Like... Maybe if he killed himself, the Demon King would be released."
    g "And it would possess someone else again."
    mc "Mh... yeah, that would make sense."
    "You listen to the rest of the lesson until class ends."
    jump out

label out:
    scene academytalkblr with fade
    show normalmc
    show normalgabe
    pause 1
    if kickedOutOfClass == True:
        show talkgabe
        g "Kicked out on the first day, that's certainly a way to stick out."
        hide talkgabe
        show talkmc
        mc "Listen, it's not my fault, alright?"
        hide talkmc
        if surpassGabe == True:
            show talkgabe
            g "Yes, yes, it's all part of your plan to surpass me in all classes."
            hide talkgabe
            show angry
            mc "Shuddup."
            hide angry
        show talkwagabe
        g "Anyways, magic arts class is next. Let's go."
    else:
        show talkhappymc
        mc "Well, that was boring as hell. What's our next class?"
        hide talkhappymc
        show talkgabe
        g "It's Magical Arts. Come on, let's go."

label mageclass:
    scene lecturemage1 with fade
    g "The teacher is late!"
    mc "Yeah."
    "The door opens and the teacher quickly runs to the board."
    scene lecturemage3
    s "Good morning class, sorry I'm late."
    mc "{i}HUH!?"
    mc "{i}Scarlet- She's our magic arts teacher?! What the hell?"
    scene lecturemage2
    g "Wow, she's younger than I thought. She almost looks our age."
    mc "......"
    g "[mc]?"
    mc "Y-Yeah, she does..."
    scene lecturemage3
    "The class goes on for a while and after some time, it ends."
    "You go and meet up with Scarlet before she leaves."
    scene lecturemage1
    show normalm
    show normalmc
    show talkmc
    mc "Excuse me, Miss Scar-"
    hide talkmc
    show talkwam
    s "Oh, hello there, [mc]. Please just call me Scarlet."
    hide talkwam
    show talkmc
    mc "B-But, y-you were..."
    hide talkmc
    show talkwam
    s "Yeah, I know, you're surprised."
    s "I'm sorry I didn't tell you earlier."
    hide talkwam
    show talkwanmc
    mc "But, why?"
    hide talkwanmc
    show talkm
    s "I don't know, it was kinda fun!"
    hide talkm
    show talkwamc
    mc "So the groundskeeper also mistook you for a student?"
    hide talkwamc
    show teethm
    s "Yeah, it's my first day here anyway. I guess he didn't know."
    hide teethm
    show talkwanmc
    mc "And you didn't say anything?"
    hide talkwanmc
    show talkwam
    s "Nope!"
    hide talkwam
    show talkwanmc
    mc "Why?"
    hide talkwanmc
    show talkm
    s "It just feels great to be young again you know?"
    hide talkm
    show talkwanmc
    mc "What?"
    hide talkwamc
    show talkwam
    s "I'm older than you think, [mc]."
    hide talkwam
    show talkwamc
    mc "But you look very young..."
    show talkm
    hide talkwamc
    s "I know! It's because of a de-aging spell."
    show talkwamc
    hide talkm
    mc "De-aging spell?"
    mc "Never heard of that before."
    hide talkwamc
    show talkm
    s "That makes sense. I don't mean to brag, but the de-aging spell is an S-class spell. Many mages can't use it."
    hide talkm
    show talkmc
    mc "Wow... So, does that mean you're like... hundreds of years old?"
    hide talkmc
    show sadtalkm
    s "I'm not that old, you dolt."
    hide sadtalkm
    show talkwanmc
    mc "Alright, how old are you then?"
    show talkm
    hide talkwanmc
    s "Fifty-three."
    hide talkm
    show talkmc
    mc "Still a bit old."
    hide talkmc
    show smileecmc
    show talkwam
    s "Oh, shut up, [mc]."
    mc "Hehe..."
    show talkwam
    s "Ok kid, you better go now. I've got another class."
    hide talkwam
    show talkwamc
    mc "Ok, now you're really starting to sound old."
    hide talkwamc
    show smilemc
    show teethecm
    s "Ahah, see you, [mc]."
    hide teethecm
    show talkwam
    s "And also, [mc], I hope this doesn't change anything."
    s "We're still friends, right?"
    hide talkwam
    show talkhappymc
    mc "......"
    mc "Yeah."
    s "Glad to hear it."
    hide normalm with easeoutleft
    if peek == True:
        s "Oh, and another thing. The next time I catch you peeking...{p}{b}I'll kill you."
        show suprised
    ## Arena
    scene black with fade
    show text "{color=#fff}You wave to Gabe as you separate and go to the arena for your combat art class." at truecenter
    with fade
    pause
    hide text
    scene arena with fade
    "You see all the students gathered at the arena. You quickly join them."
    "You can hear some students talking."
    "{color=#fff}Student 1" "Did you hear General Taliya is here? She came to train us."
    "{color=#fff}Student 2" "What? No way! Are you serious?"
    "{color=#fff}Student 1" "Yeah, man, they've seen her around town these past few days..."
    "{color=#fff}Student 2" "Will she teach us how to defeat a minotaur single-handedly?"
    "{color=#fff}Student 1" "Who cares about that! I wanna see her without armor on-"
    show normalt with easeinright
    "A woman in armor marches in front of the students."
    show aten
    "{color=#DD8E8B}Woman in armor" "Attention students!"
    hide aten
    show talkt
    t "My name is Taliya Bridges. As you may know, I am here to train all of you new recruits."
    t "Because Randel is one of the closest towns to Hern, we need as many soldiers from this town as possible."
    t "That is why I personally came to Randel to make sure each one of you will be trained well enough to defend Astylla."
    t "Ok everyone, get ready for training. I'll get into something comfortable as well."
    "Taliya starts to strip down her armor."
    scene tt1
    pause 2
    mc "{i}Wow, that guy had a point..."
    "You notice all the other students ogling her as well, but she doesn't seem to care."
    scene tt2
    t "Ok recruits, line up. We'll start by learning how to properly use a sword."
    t "Everybody, draw your swords!"
    "You reach to grab your sword."
    scene black with flash
    scene tt1
    "A sudden chill runs down your spine as soon as you touch the hilt of your sword for the first time."
    mc "{i}What the hell was that...?"
    mc "{i}Agh- my chest is burning..."
    "You almost lose consciousness, but somehow you manage to hold on."
    "Taliya seems to notice but when you stop showing any signs of pain, she looks back to the other students."
    mc "{i}Huff... That was weird... The hell was it?"
    scene tt2
    t "Alright, recruits, we'll be practicing basic strikes today."
    t "Let's begin now."
    show animationsword
    "You train for a while, practicing many different movements with the sword."
    if chartrait == 2:
        "The training lasted longer than you thought. You were pretty good compared to the other recruits."
    else:
        "The training lasted longer than you thought. At the end your hands feel like they're about to fall off."
    hide animationsword
    scene tt2
    t "That's enough for today, recruits. You did a good job. I hope to see you all a lot in the training field."

    ### School End
    scene academytalkblr with fade
    show normalmc with easeinright
    mc "Man, what a day."
    show normalgabe with easeinleft
    pause
    show talkgabe
    g "Hey, [mc]! How was your combat arts class?"
    hide talkgabe
    show angry
    mc "It was hell, that's what it was."
    hide angry
    g "Heheh."
    show talkgabe
    g "I'm glad studying at Westian allowed me to skip some of the first year classes. Demonology and Military History are much more fun than Physical and Weapon Training..."
    hide talkgabe
    show angry
    mc "We both skipped Writing, at least."
    hide angry
    show talkgabe
    g "Heheh... Well, see you tomorrow, [mc]."
    hide talkgabe
    show talkhappymc
    mc "Wait, Gabe, if you don't mind me asking... Where do you live now?"
    hide talkhappymc
    show talkwagabe
    g "In my old house, silly. Next to the Adventurers' Guild."
    hide talkwagabe
    show talksadhappymc
    mc "Oh! Then it won't be hard to find you."
    hide talksadhappymc
    show talkwagabe
    g "Now that I think about it... You always wanted to join the Adventurers' Guild, right? Aren't you going to join?"
    hide talkwagabe
    show talkhappymc
    mc "Yeah. I'm going there before going home."
    hide talkhappymc
    show talkgabe
    g "Really? Good luck then!"
    hide talkgabe
    show talkhappymc
    mc "Thanks, See you later!"
    scene villageback with fade
    show normalmc with easeinleft
    pause
    hide normalmc
    show smilemc
    mc "{i}Time to go to the Adventurers' Guild."
    mc "{i}I've been wanting for this moment for so long..."
    mc "{i}I wanted to wait until I joined the Academy so I could train my abilities while being an Adventurer, now I don't have anything to wait for."
    mc "{i}And finally they won't kick me out for being too young!"
    hide smilemc with easeoutright

    ## Guild Introduction
    play music aguild
    scene adventurersguild_day with fade
    pause 3
    scene agblr with dissolve
    show smilemc
    mc "{i}Ahh... Finally, I'll be able to call this home."
    mc "{i}I can't wait to get started. I wonder where I'm supposed to find July... Apparently I need to ask her if I want to join..."
    show talkow with easeinleft
    show suprised
    e "Quick, move aside."
    hide suprised
    show talksadhappymc
    mc "H-Huh? Alright."
    mc "{i}Wow, an elf girl! She must be Evelyn! I've heard a lot about her and her companion, Sander."
    "You move slightly to the side."
    mc "But, uhm... Could you tell me where I can find July...? I'm here to join."
    hide talkow
    show talkhse
    hide talksadhappymc
    show smilemc
    e "......"
    e "Oh really? It's nice to see young faces around here for a change."
    e "How old are you, little one?"
    show talkhappymc
    show smilese
    mc "Nineteen."
    hide talkhappymc
    show talkhse
    e "Mhh... Is that so? Well, then, she's right over there behind the counter."
    show talkhappymc
    hide talkhse
    mc "Thanks."
    hide talkhappymc
    show lookdownsupmc
    sa "Ughh... Uhh... Just give one more drink Eve, I can take... It..."
    hide lookdownsupmc
    show talkwase
    e "Shut up, Sander. You had too much and I'm cutting you off!"
    e "Eh... This is my friend, Sander. He just had a little too much today... I'm taking him outside before he throws up all over the place... again."
    sa "It was just 19 beers, Eve... I've had way more beforeee."
    e "Anyway, I gotta go, little one... Welcome to the Guild... Oh, I'm sorry. I didn't get your name."
    show talkhappymc
    mc "It's [mc]."
    e "Alright, welcome to the Guild, [mc]!"
    $ renpy.notify("{color=#fff}Quest started: Guild Quest")
    hide talkwase
    hide smilese with easeoutright
    hide talkhappymc
    mc "{i}She was nice... I had heard about those two a lot, I guess it's true that she's more like Sander's mom than anything else..."
    mc "{i}Well, time to go talk with July."
    scene adgc1 with fade
    mc "{i}...Is she asleep?"
    mc "Uhm..."
    scene adgc2 with vpunch
    j "Yes...? What brings you to the Adventurers' Guild?"
    mc "{i}Oh shit, she scared me."
    mc "Oh, uhm, I thought tha-"
    j "I was asleep? ...Yeah, I get that a lot... My eyes are just really tiny. Hehehehe."
    j "So, are you here to join?"
    mc "Yeah."
    j "Ooh, that's nice! A new Adventurer, eheh. How old are you?"
    mc "Nineteen."
    j "And your name?"
    mc "[mc]."
    j "[mc], can you sign this paper, please?"
    scene adgc2
    pause
    scene adgc3 with dissolve
    pause
    "You skim through the paper, it's pretty generic stuff. You sign it and hand it back to her."
    scene adgc4
    j "Ok... That settles the legality side of things, now listen closely."
    j "There are five ranks in the Guild: Recruit, Bronze, Silver, Gold, and Diamond."
    j "You will start at the Recruit rank. To achieve a higher rank you will need to gain experience."
    j "You gain experience by completing quests and slaying monsters. Quests will be assigned according to your respective rank."
    j "When you reach Bronze, you will get your first badge and will be considered an actual Adventurer... Only after you will have achieved Bronze-Rank, you'll be allowed to join or form a party."
    j "Here's a sheet which shows the class progression with respect to the Adventurer level."
    show gn with dissolve
    j "Until you've reached level 5, you won't be allowed to take on any quests. Till then, you can go to the forest and slay beasts to gain experience... But remember, the deeper into the forest you go, the more dangerous the monsters become. Here's a map which shows the areas of the forest."
    show mf with dissolve
    j "If you slay any boars, please bring them to the Guild."
    mc "Will I get paid?"
    j "Yes... 5 silver per boar until you become a Bronze Adventurer, then you'll get 20 silver per boar."
    mc "Nice."
    j "And here's your EXP Charm."
    mc "Uhh... What does it do?"
    j "Didn't I tell you?"
    mc "...No."
    j "Oh my goodness, sorry. I'm getting too old for this teehee."
    mc "{i}C'mon girl, you're not even forty..."
    j "Let me explain. This EXP Charm will collect {b}Experience Points{/b} every time you slay a monster or complete a quest, the latter giving you much more EXP than simple monster-slaying."
    j "Think of it as some sort progression tracker. It's what allows you to level up in the Guild."
    mc "Oh, cool."
    j "Remember to wear it at all times. It won't collect experience unless you wear it."
    mc "Ok."
    j "Oh, and in case you're wondering, among the various monsters in the outer valley, falcons are the ones that give the most Experience."
    scene adgc4
    j "That's all for my briefing."
    j "You do have weapons, right?"
    mc "Yeah."
    j "Good, any more questions?"
    scene adgc3
label qg:
    menu:
        "When can I go on quests?":
            j "When you reach level five. Until then, hunt boars or slay monster to gain experience. "
            jump qg
        "Can I slay other monsters?":
            j "You can. Just be careful, most of them are very dangerous. Be sure you are trained enough with your sword and bow before you do."
            j "Also, you should study about monsters before slaying them. Go to the Library and find the Book of Monsters and use it to find the weaknesses of any monster you might expect to encounter."
            jump qg
        "Where can I get new equipment?":
            j "There's a trading caravan just outside the Guild. You can buy equipment from there."
            jump qg
        "No more questions":
            mc "No more questions. Thank you!"
    j "See you soon, young Adventurer."
    j "Make sure you go check out the Library!"
    mc "Ok, bye, July."
    mc "{i}Well then, let's go check out the library."
    stop music
    scene library with fade
    pause
    show normalmc
    mc "Man, this place looks deserted. I guess the people in Randel aren't big readers..."
    if chartrait == 1:
        mc "It's my first time here as well, even though I was such a bookworm back then."
    show talkl
    show suprised
    scene libraryblr
    show grumpl
    show suprised with vpunch
    "{color=#8C79C6}Half-Elf girl" "Hey, who are you?"
    mc "{i}Ah shit, got startled again."
    hide suprised
    hide talkl
    show grumpl
    show talkhappymc
    mc "Uh, I'm [mc]. Can you tell me where I can find the librarian?"
    show talkl
    hide talkhappymc
    show smilemc
    l "You're looking at her. I'm Lori, I'm the librarian here."
    show talksadhappymc
    mc "Oh sorry, I-"
    hide talksadhappymc
    show talkl
    l "Enough with the act! Why are you here?"
    l "Hiding from the guards? Hiding from your parents? Or are you waiting for some girl so you can fool around in here?!"
    hide talkl
    menu:
        "I'm here to find a book":
            $ lorirel += 20
            show talksadhappymc
            mc "Uhm... No, I'm here to find a book actually."
            hide talksadhappymc
        "Did anyone ever tell you that you're cute?":
            $ flirtingWithLori = True
            show talkwamc
            mc "...Did anyone ever tell you that you're cute?"
            hide talkwamc
            show smilemc
            show grumpl
            l "..."
            show talkl
            l "Could you not?"
            hide talkl
            show smileecmc
            mc "Alright, alright, I get it."
            hide smileecmc
            show talksadhappymc
            mc "I'm actually here to find a book though."
            hide talksadhappymc
    show normall
    pause 2
    show talkwal
    l "Wait... Are you actually here to read?"
    hide talkwal
    show talksadhappymc
    mc "...Yeah."
    show talkhl
    l "Really?! Oh my god, I- ...I mean, {b}we{/b} rarely get any actual readers here!"
    hide talkhl
    show talkhsl
    l "Sorry for being harsh... Most people come here just to fool around."
    hide talkhsl
    if flirtingWithLori == True:
        show talkwamc
        mc "It's alright, don't worry about it."
        hide talkwamc
        show talkhsl
        l "I'm just not used to people actually coming here for books..."
        hide talkhsl
        show talkwamc
        mc "Are you more used to people telling you that you're even cuter when you smile?"
        hide talkwamc
        show blushl with dissolve
        $ lorirel += 5
        pause 2
        hide blushl
        show talkl
        l "Stop it."
        hide talkl
        show smileecmc
        mc "Fiiine."
        hide smileecmc
    show talkhnl
    l "So! What's the name of the book you are looking for?"
    hide talkhnl
    show smilel
    show talkhappymc
    mc "The Book of Monsters."
    hide talkhappymc
    show talkhnl
    l "Oh! So, that means you are an Adventurer?"
    hide talkhnl
    show talkhappymc
    mc "Yeah."
    show talkhl
    l "That's awesome!"
    hide talkhl
    show talkhsl
    l "I've always wanted to become one myself but... I am too weak and I'm rather scared of monsters."
    hide talkhsl
    show talkhappymc
    mc "Heh, everyone's scared of monsters."
    mc "And, after all, adventures aren't fun without danger, right?"
    hide talkhappymc
    show talkhsl
    l "Hehehe, you're right, [mc]. I bet you'll be a great Adventurer!"
    l "But sorry, [mc], I won't be able to give you the book today. I haven't taken it out in years, so I'll have to look for it... Come back tomorrow, I'll be sure to give it to you then."
    hide talkhsl
    show talkhappymc
    mc "It's ok. I'll come back tomorrow then."
    hide talkhappymc
    show talkhsl
    l "By the way... [mc], are you a student at the Academy?"
    hide talkhsl
    mc "Yeah."
    show talkhsl
    l "If you have any trouble with your studies, feel free to ask... I'll be glad to help."
    hide talkhsl
    show talksadhappymc
    mc "Really? Thanks, Lori, I really appreciate that."
    hide talksadhappymc
    show talkhsl
    l "No problem! I like helping others, y'know... and it gets really boring sitting in here all day."
    hide talkhsl
    show talkhappymc
    mc "Heh, don't worry, I'll be back."
    if flirtingWithLori == True:
        mc "Wouldn't miss a chance to see your cute smile."
        hide talkhappymc
        show blushl with dissolve
        pause 1
        l "..."
    hide talkhappymc
    hide smilemc
    show talkhnl with dissolve
    l "Bye!"
    scene black with fade
    scene homenight with dissolve
    pause 1
    show normalmc
    mc "{i}Finally, I'm home. That was one hell of a day."
    mc "{i}Now I can jump into my bed!"
    "{i}Knock knock knock"
    show thinkmc
    mc "{i}Ugh, who is it this late?"
    scene ut1 with fade
    mc "Hello? Who's there?"
    u "Open up, [mc], it's me."
    mc "Oh, Uncle Pete, wait a sec..."
    scene ut2 with dissolve
    u "Hey, kid... I was just passing by, so I came for a quick chat."
    scene ut3 with dissolve
    u "And I brought fish."
    scene ut2 with dissolve
    $ petefish += 1
    mc "Thanks, Uncle Pete, why don't you come in?"
    u "No, no. I just came for a quick visit and it's already late. How was your first day?"
    mc "It was cool. A bit hectic, but alright... and I saw Gabrial."
    mc "She's changed a lot since I last saw her."
    scene utsmirk with dissolve
    pause 2
    mc "What?"
    u "She's grown a lot, hasn't she?"
    mc "Yeah?"
    u "...Mh."
    mc "Wait... again!? Don't you ever get tired of the same joke, uncle?"
    scene ut2 with dissolve
    u "Hahahahaha... I sure don't get tired seeing your face blush every time."
    mc "There's nothing like that, we're just friends, ok!?"
    u "I get it, I get it, I won't bring it up again... Haha."
    u "Anything else?"
    mc "Huh... Oh, I joined the Adventurers' Guild too!"
    u "Really?"
    u "You always wanted join, didn't ya? Ever since you were a little boy. I'm so proud of you, [mc]."
    mc "Thanks, Uncle Pete."
    u "So, what's it like having the house to yourself?"
    mc "It's ok, but you didn't have to leave, Uncle Pete."
    u "Nah, you're a big kid now. You don't want old farts like me staying with ya. And besides, I've always liked the fishing hut more than this dusty old place."
    mc "Hey, it's not that bad."
    u "Heh."
    mc "Oh, and another thing. I had that dream again."
    u "The one with your parents? Was it the same thing?"
    mc "Yeah, but this time I think they said something."
    u "What did they say?"
    mc "It didn't make any sense... It kinda sounded like..."
    scene ut4
    mc "\"...You are not our son.\""
    mc "I don't know what it means."
    scene ut2
    u "It's probably nothing. Dreams usually don't make much sense... I've had a lot of weird dreams myself."
    u "Don't worry about it too much, kid."
    mc "Yeah, but I keep seeing it again, and again..."
    u "You just need to get some good rest... Go to sleep earlier."
    mc "Yeah, I really haven't slept much recently."
    u "Ok then, [mc], eat the fish and-"
    mc "Sleep early."
    u "...Sleep early. See you, kid."
    mc "Bye, Uncle Pete! Same goes for you... It's too late to go fishing, you know?"
    u "Hah, smartass."
    scene ut1 with dissolve
    mc "{i}Anyway, he's right. I better go to bed."
    scene sleep with fade
    mc "Ahh... I've missed you, bed."
    play music fairytalewaltz
    hide screen skipintro with dissolve
    scene black with fade
    pause 1
    #show text "{color=#fff}Would you like to enable cheats?"
    #pause 2
    #hide text
    #menu:
    #    "No (Recommended for first time players)":
    #        he "No cheats for me."
    #    "Yes (Recommended for players who are coming back)":
    #        he "No grinding for me."
    #        $ easyMode = True
    #show text "{color=#fff}Would you like to enable monogamy?"
    #pause
    #show text "{color=#fff}This options only blocks you from having a specific polygamorous relationship, you can still do multiple routes at once."
    #pause
    #hide text
    #menu:
    #    "No (No danger in doing multiple routes at once)":
    #        he "I want threesomes."
    #    "Yes":
    #        he "I'll do my best to not get caught."
    #        $ monogamy = True
    #scene black with fade
    show text "{size=+20}{color=#fff}{b}Chapter 1: Life in Randel" at truecenter
    pause 4
    scene tutorial1 with fade
    pause 20
    scene tutorial2 with dissolve
    pause 30
    scene tutorial3 with dissolve
    pause 20
    scene tutorial4 with fade
    pause 25
    scene tutorial5 with dissolve
    pause 20
    scene tutorial6 with dissolve
    pause 20
    scene tutorial7 with fade
    pause 10
    jump home













label skippingIntro:
$ money = 30
$ petefish = 1
hide screen skipintro
scene black with fade
$ skippedIntro = True
if choseTraits == False:
    show text "{color=#fff}Please choose a trait."
    pause 2
    hide text with fade
    call screen traits
    label skippingBack:
    $ choseTraits = True
    pause 1
show text "{color=#fff}Please choose a personality."
pause 2
hide text
menu:
    "Bold":
        $ renpy.notify("{color=fff}Personality trait:{/color} {color=#FF6600}Bold")
        $ mcBold = True
    "Normal":
        $ renpy.notify("{color=fff}Personality trait:{/color} {color=#3AC400}Normal")
        $ normalmc = True
    "Timid":
        $ renpy.notify("{color=fff}Personality trait:{/color} {color=#0094FF}Timid")
        $ mcTimid = True
pause 1
if choseName == False:
    show text "{color=#fff}Enter your name."
    pause 2
    hide text
    $ mcn = renpy.input("My name is...")
    if mcn == "":
        "Bunis" "Hello, I'm the developer! Please enter a name. If not, a default name will be given."
        $ mcn = renpy.input("My name is...")
        if mcn == "":
            "{color=#FF8EF5}Rin the Other Dev" "Guess you're going with the default name, {b}Robin{/b}."
            $ mcn = "Robin"
    $ choseName = True
    pause 1
#show text "{color=#fff}Would you like to enable cheats?"
#pause 1
#hide text
#menu:
#        "No":
#            he "No cheats for me."
#        "Yes":
#            he "No grinding for me."
#            $ easyMode = True
jump home
