default TaliyaQ = 0
default TaliyaTrain = False
default fakeName = "Colby"
define torturerMC = False
default askedTaliya1 = 0
default waydtT = False
default aydtaT = False
default airiT = False
default countonmcT = False
default yamiTaliya = False
default TQ1p1 = False
default penepisellosessoomosessuale = False
default clamp4 = False
default butt4 = False
default t4qt = 1361366
default Q4Pre = False
default Taliya6Talk = False
default dayTQ5 = 16136
default askedTaliyaKiss = False
default twigRescue = False
default taliyaQTE1 = "a"

label TaliyaQ0:
hide screen screenmap
hide screen hud
scene ambush1 with fade
stop music
stop sound
play music forest
"As you make your way to Corban, you're surprised to see no monsters around. It's not really a route that's travelled often, so someone strong probably walked all the way to Corban recently."
"You're glad, though, as it would've been a pain in the ass having to battle for such a simple quest."
scene corban with fade
play music home
"You finally arrive to the city. Despite it being smaller than Randel, the houses and streets aren't that different, but that makes sense."
"Apparently about 200 years ago there was an epidemic in Randel and a few hundred citizens left the town and established a few hours away from the town to avoid being hit as well."
"You walk around the town for a while looking for Hern Street, and when you finally find it, you immediately see the forge. A big building that easily stands out from the rest in that street."
scene forge with fade
"You get in and find Philmon forging an axe. You tell him why you're there and hand him the letter."
"After he's read it, he goes in the back and returns a few minutes later with a silver sword in his hands. He hands it to you and waves you off."
scene corban with fade
mc "{i}Well, that was quick. Though I guess not much interesting can happen on a fetch quest-"
scene corbanstreet with vpunch
"You suddenly bump into someone- Wait, where are you?"
show prot surprised
show tarm normal
mc "...General Taliya?"
show tarm angryt
t "What the- Wait, are you a student from the Academy in Randel?"
show prot questiont
mc "Uh... Yes?"
show tarm smirk
t "Perfect."
"Taliya looks behind a corner into another street. Curious, you do the same."
"You see what looks like a regular house, a sign on front says it's a butcher. Really nothing out of the ordinary until you realize how many armed people there are."
show tarm talk
t "There more guards than I thought..."
mc "...Uhm, General Taliya? What's that place? What are you doing here?"
t "That's one of the hideouts of the Black Snakes. They're a minor criminal gang here in the province."
mc "Uh-huh..."
t "Alright, since you're here, I need you do something. You gotta go inside that building and find a way to lead all the guards outside."
mc "Huh? Wait what-"
"Taliya looks at you and raises an eyebrow."
mc "B-But how am I supposed to do that?!"
t "It's easy to get in. You see, they're drug dealers. If you get in with the excuse of buying drugs they..."
mc "...they'll let me in? I just go \"drugs pretty please\" and they let me in?"
t "What? Of course not. There's a password."
mc "Which is?"
t "It's... It's a dumb password, just go there and tell the guy at the door \"Bunny doesn't hop Humbert's fence\""
mc "Bunny doesn't hop Humbert's fence...?"
t "...Don't ask."
mc "Alright..."
mc "Still, what exactly are you doing here?"
t "Clear out the hideout and put an end to their operations."
mc "...Clear out as in \"kill\"?"
t "If they give me another choice, I'll take it... But I'll probably have to kill them."
mc "Could you remind me why you need me?"
t "I don't {b}need{/b} you, but you could make this job a lot easier."
menu:
    "What if I don't want to help?":
        mc "What if I don't want to help? I didn't come here to risk my life."
        t "Then it's an order, recruit."
        mc "Wh-"
        t "Stop complaining or you'll face consequences back in Randel."
        if mcBold == True:
            mc "{size=-5}Bitch..."
            t "Said anything, recruit?"
            mc "...Nothing."
    "Fine, I'll help":
        mc "Alright, I'll help then."
        t "That's nice to hear, recruit."
mc "But, uhm, how would I make this job easier?"
t "They would recognize me. You, instead, should be able to get inside without any problems."
mc "They'd recognize you?"
show tarm sadt
t "W-Well y-yeah... I-I'm a general of the Astyllian army and I've already busted quite a few operations on this side of the country."
mc "{i}Huh, I didn't know she was that famous... I guess it makes sense."
show tarm talk
t "What I need you to do is get them all together in one place so that I can make sure nobody gets away. I need this mission to be completed as straight as possible."
t "This is a busy street and if the fight were to break out of the building, I'd rather let them go than involve civilians."
mc "......"
t "Got it?"
mc "Yes ma'am, though..."
t "What? Speak up, recruit."
mc "...How am I supposed to do that?"
t "By finding a way to get all the guards to you."
mc "...How."
t "I don't know, I have not been in there. You'll have to figure it out youself."
t "But remember: Be careful. Don't be reckless, I'll come in 5 minutes from when you've passed that door no matter what happens. If you do it quickly and then buy yourself enough time I'll be able to save you."
mc "A-Alright..."
t "If you really want to go I'll let you go."
if mcBold == True:
    mc "Thanks for the offer, but I think I'm going to do this."
elif mcNormal == True:
    mc "No, I'll do this."
elif mcTimid == True:
    mc "N-No, I can do this."
t "That's the spirit! I wish all recruits had your same sense of duty. Now go- {p}Oh, wait."
mc "Huh?"
t "take this."
"Taliya hands you a pouch filled with gold."
mc "What's this for?"
t "If you decide to buy something as cover you'll need that."
mc "Oh, thanks.{p}Alright, I'm going."
hide tarm
"You leave Taliya and approach the hideout. You stop at the door and a thug looks at you unimpressed."
scene hideoutentrance
"Thug" "Whatcha lookin' for, kid?"
mc "Uhm... Uh... B-Bunny doesn't hop Humbert's fence...?"
"Thug" "......"
"The thug eyes you from top to bottom."
"Thug" "Second door from the back. Knock four times."
mc "Thank you."
"Thug" "Huh?"
mc "N-Nothing."
"You quickly make your way inside and begin looking for the room the thug described"
mc "{i}Second door from the back... Oh! That's the one."
"You take a deep breath as you stand in front of the door, then you grab the handle and twist it, opening the door."
stop music
scene gang1 with fade
mc "{i}Uhh... Don't tell me that's..."
"Boss" "Come in, don't stand still, boy."
"You gulp and take a step inside. The door closes behind you. Now you're definitely not going to be able to change your mind about this."
"Boss" "Damn kid, you look like a fish out of water. You sure you're in the right place?"
mc "H-Huh?! Y-Yes I'm sure!"
mc "{i}God that was loud..."
"Boss" "Mh... Alright then, kid, how much you looking for?"
mc "Oh, I..."
mc "{i}What do I say, what do I say, what do I say-"
menu:
    "How much you got?":
        mc "...Actually, how much have you got with you?"
        "Boss" "Hah! How much we got! Is this kid serious?"
        mc "I am."
        "Boss" "Hahahaha! You're a fun one. We've got enough for a whole company, I don't think you have the money to buy that."
        mc "..."
        "You take your pouch and throw it onto the table."
        mc "How much for this, then?"
    "...Want however much this can buy me":
        "You take your pouch and throw it onto the table."
        mc "...I want however much this can buy me."
    "...Wanted to talk about something else":
        mc "...I am not here to buy."
        "Boss" "Huh? Then what are you here for? Got a grudge?"
        if mcBold == True:
            mc "No... I'm here for a job."
        else:
            mc "N-No. I... I'd like a job."
        "Boss" "Hah! You? Sorry kid we aren't looking for anyone at the moment."
        mc "...Fine."
        "You take your pouch and throw it onto the table."
        mc "How much for this?"
"Boss" "Wow, that's... Those are a lot of coins for a kid."
"Boss" "...Who sent you? There no fucking way a brat can make this much by himself."
mc "......"
label sessogayconigay:
$ gameover = "sessogayconigay"
scene gang1
$ fakeName = renpy.input("It was... ")
if fakeName == "":
    "{i}Retry."
    jump sessogayconigay
if fakeName == "Taliya":
    "Boss" "What?!"
    "Thug 1" "This kid's got a death wish, I think."
    "Boss" "Be serious kid."
    mc "{i}Let's not fool around..."
    label saygex:
        $ fakeName = renpy.input("It's...")
        if fakeName == "":
                "{i}Retry."
                jump saygex
        if fakeName == "Taliya":
                mc "I'm telling you it was Taliya."
                "Boss" "You think you're funny, dontcha?"
                mc "Why? Taliya told me to come and say hi."
                "Thug" "You're not fucking funny, kid."
                mc "Who said I'm trying to?"
                "Boss" "..."
                "Boss" "Kill him."
                mc "You can tr-"
                "You feel something poking through you from behind."
                "When you look down, you see the tip of a blade sticking out of your stomach covered in blood. It seems there was someone behind you."
                jump GameOver
if mcBold == True:
    mc "Hah, fine, you got me. [fakeName] sent me."
    "Boss" "[fakeName]? Who the fuck is that?"
    mc "Oh, you'll meet him soon enough. He's from..."
else:
    mc "It was [fakeName]."
    "Boss" "[fakeName]? Who the fuck is that?"
    mc "H-He's from..."
label retardedMCtime:
scene gang1
$ gameover = "retardedMCtime"
menu:
    "Randel":
        mc "...Randel."
        "Boss" "Randel? Wait... Airi, isn't your old friend in Randel right now?"
        "Airi" "Who...?"
        "Boss" "Taliya."
        "Airi" "O-Oh... Yeah she is."
        "Boss" "As I thought...{p}Merl, kill him."
        mc "What-"
        "Boss" "I'm not stupid kid. She sent you here, didn't she?"
        mc "Wait no, she's not-"
        "You feel something cold sticking out from your chest."
        "Airi" "Aw... What a shame, he was cute."
        "Boss" "Airi, shut up and alert everyone: Taliya might be around. We'll get out from the back."
        "Airi" "Fine..."
        jump GameOver
    "Capital":
        mc "...The Capital."
        "Boss" "The Capital! Hahah! this [fakeName] must be a real brave guy isn't he? Trying to get anything in the Capital under the king's watch..."
        mc "Yeah... He's a brave man..."
        "Boss" "You have no fucking idea what you're talking about, do you?"
        mc "I-"
        "Boss" "Merl, take him out."
        mc "Wait-"
        "You feel something cold sticking out from your chest."
        "Airi" "Aw... What a shame, he was cute."
        "Boss" "Airi, shut up and alert everyone: If there's one there might be more. We'll get out from the back."
        "Airi" "Fine..."
        jump GameOver
    "Westian":
        scene gang2
        mc "...Westian."
        "Boss" "Hah, so he's trying to steal Lumion's territory? He's got balls... But the enemy of my enemy is my friend, isn't that right?"
        mc "Y-Yeah, that's why I'm here."
        "Boss" "Alright, I guess I'll let you buy our stuff, though I gott say... You guys really don't like him do ya? You're the fourth guy this week who came with the same idea, right Merl?"
        "Merl" "He's the third one."
        "Boss" "Third, right, still too many honestly. If so many people are unhappy with him we might expand our territory there..."
        mc "Hahah... I'd rather you don't."
        "Boss" "We'll see, kid. Who knows what the future has for us."
        "Boss" "Here, I'll give you a discount... With interests."
        mc "...Thanks,"
        "Boss" "T'was a pleasure."
mc "{i}Wait, I still haven't found a way to get them all in one place! I need to think fast, what do I do?"
"Airi" "So... Can I go now, boss?"
"Boss" "Huh? Sigh... Sure, mess him up."
"Airi" "Thanks!"
mc "What?"
"Boss" "Consider this a bonus."
mc "What are you talking about?"
"Airi walks towards you."
"Boss" "This whore here is going to get a piece of you."
mc "The hell?"
"Airi" "I just can't resist cuties like you~"
"Boss" "Don't do it in here... And for Astylla's sake keep it down."
scene black with fade
"Airi grabs you by your hand and leads you outside the room with her"
mc "{i}Wait, wait, wait, is she serious? I don't want to turn her down honestly, but I've got a job to do. Taliya should break-in any moment now..."
"The two of you go downstairs. She hastily strips you of your clothes, Only leaving your underwear on. Then she gets on top of you and starts running her tongue along your body."
scene mcl with hpunch
mc "W-What are you doing?"
"Airi" "I'm gonna taste all of you~"
mc "{i}Oh, she's nuts, but I'm definitely not stopping her now."
"Airi" "Oh look what we got down here~ Your friends seems really eager to meet me~"
"Airi slowly pulls your underwear down and bites her lip as your shaft is slowly revealed."
"Airi" "It looks so tasty~ This is why I like small boys so much..."
mc "{i}Th-That's kind of a weird sentence, but I'm already butt-naked, I-I don't think I'll be able to finish the mission Taliya gave me... No, [mc], this isn't the time, you've got a mission!"
scene mclsuckbase
"Airi smiles at you and slides down, her face right in front of your cock. She takes a deep breath and then, with a single movement, she fills her mouth with your cock."
show mclsuck3 with vpunch
mc "F-Fuck!"
show mclsuck
pause 5
mc "{i}Oh, she's so good~ ...No! F-Focus! I need to find a way out...!"
pause 2
mc "Ahh...."
pause 6
mc "{i}Think... Think...{p}God, the only thing I can think about is how good this feels!"
pause 3
mc "{i}I'm g-gonna cum..."
pause 5
mc "I-I'm gonna..."
"Airi" "Do it!"
hide mclsuck
show mclsuck4 with hpunch
hide mclsuck3
"Airi grabs you by your hips and pulls you in, you feel her whole mouth wrapped around you cock. You begin to helplessly cum inside of her throat."
show mclsuck4 with vpunch
pause 0.2
show mclsuck3 with vpunch
pause 0.2
show mclsuck4 with vpunch
pause 1
show mclsuck1
mc "Ha... Hah..."
mc "{i}Hah! I've got an idea! ...A dumb idea, but an idea."
mc "{i}I guess this is what they call post-nut clarity."
"You clear your throat."
scene mclsuckscreambase with vpunch
mc "HELP! SOMEONE'S GOT IN THE BUILDING!"
show mclsuckscream
"Airi" "...The fuck?"
mc "AHHHH!!!"
"You begin hearing voices from upstairs, people walking inside the house, confused as to what is going."
mc "{i}Oh god, it's working..."
scene mclsuckscreambase
"Airi" "Kid, what the fuck is wrong with you?"
"Thug 1" "{size=-4}Who the hell is screaming? Where's the intruder?!"
"Thug 2" "{size=-4}We could hear it from outside! Has anyone even seen anyone someone suspicious? I let a kid in not too long ago!"
"Thug 1" "{size=-4}That kid? Even if he were an enemy we would probably be fine."
scene mclsuckscreambase with hpunch
mc "HELP ME!!!"
"Boss" "It's coming from downstairs, go check it out!"
"Airi" "Shut the fuck up-"
"You hear the front door smashing open, then a few heavy steps."
mc "{i}She's here!"
"Boss" "{size=-2}Who the hell are you?"
t "{size=-3}Do not move and stay quiet if you want to-"
"Boss" "{size=-1}Get her!"
"...And then fighting ensues."
"Airi" "The hell's going on?!"
"Airi" "I swear to Astylla if you're involved in this you won't see the light of the day again!"
mc "...Gulp."
"Airi gets up and quickly runs upstairs."
mc "{i}Oh, I'm so good at this! Let's go upstairs, Taliya might need help!{p}...{p}...Maybe I should put my clothes back on first."
scene black with fade
"You swiftly dress up and then make your way upstairs. With each step the smell of iron gets more intense."
"Then, you finally arrive upstairs."
mc "{i}I-I..."
scene taliyagangkill with fade
play music creepymusic
"The floor is littered with corpses, the rugs are soaked with blood, and the floor is just as red. The stench is almost unbearable. Only then you realize that in the middle of the room, covered with blood, is Taliya. Between her and you stands Airi."
mc "Wh-What the-"
"Airi" "What the... What the fuck?! D-Did you do this?! Who-"
"Taliya pulls down her hood."
mc "{i}She... slaughtered all of them."
"For some reason, you seem to be unable to move your body. You can feel your heart beating in your ears."
"Those are... a lot of bodies."
t "Airi... Hello."
"Airi" "W-What...? ...Yami? Are you-"
t "Yes."
"Airi" "You... YOU! HOW COULD YOU KILL ALL OF THEM?!"
t "What do you mean why? They were horrible people. We both know that."
"Airi" "They were my family!"
t "Your family? They used both of us. They threatened me and they threatened you. You can't seriously think they cared for you."
"Airi" "...I can. You're the one who betrayed us! They were taking care of us and even after you were gone they took care of me!"
t "...Airi, please."
"Airi" "...D-Don't call me by name, not after what you've just done."
t "Please."
"Airi looks down, she seems to be looking for someone."
"Airi" "I am one of them. If they deserved to die then I do as well, isn't that right?"
"Airi" "You will have to kill me just like you killed them."
"Airi gets down and grabs something, but before you can even see what it is, she's behind you with a knife on your throat."
scene mcknifepoint with flash
t "Airi please calm down, put the knife down, we can do this another way."
"Airi" "I'm helping you, don't you see? This way you'll feel less guilty of killing your best friend."
mc "{i}Why can I not move...?"
"You feel the knife push more into your throats. You feel some blood running down your neck."
t "Airi, stop."
"Airi" "Now I'm gonna walk out of 'ere and you're gonna stand right fucking there as I leave."
t "Don't make me do this, you know I'm here for you."
"Taliya takes a few steps forward."
"Airi tightens the blade around your neck. It's starting to hurt quite a bit."
"Airi" "If you cared about me you wouldn't have killed Kollin."
t "Airi, look at me in the eyes. You know these eyes wouldn't lie to you."
"Airi" "..."
"Airi avoids Taliya's gaze, she looks to the ground and she's once again reminded of the corpses."
"Airi" "SHUT UP! SHUT UP! SHUT UP!"
"You feel Airi shaking, you're close enough to her body to feel her light sobbing as she yells."
scene mcknifepoint2
pause 3
"Airi" "I'm not coming with you! I'd rather go with them to hell! Stop getting closer or I'll kill him!"
"Her crying is making her grip more unstable, less powerful..."
mc "{i}I need to stop her..."
"Airi" "...As you wish."
"Taliya slowly takes another step."
mc "{i}I need to-"
"Airi" "DON'T M-MOVE CLOSER YAMI! I-I SWEAR I-"
play sound stab
scene mcknifepoint3 with hpunch
"You hear the knife drop, then you feel Airi's lifeless lean into you as it slowly falls to the ground."
scene mcknifepoint3
pause 1
scene emptyredroom
stop music fadeout 1
mc "{i}W-What...?"
"You don't see Taliya. She's behind you, probably behind Airi's body, and you can hear her breath, unsteady, as she shakingly sheathes her sword. She doesn't say a word and quickly walks out."
"Slowly the shock fades away and is replaced with horror as the stench of iron makes its presence clear again. You can almost taste it."
"You quickly rush out of the building and see Taliya."
scene corbanstreet
mc "H-Hey! W-Wait!"
"Taliya briefly stops. She tightens her fists and then turns around."
show prot sadt
show tarm normal
mc "W-Where are you going?"
show tarm talk
t "...to a tavern. You drink?"
mc "H-Huh?"
mc "{i}How can she maintain her composure after all of that?"
"Taliya takes a deep breath. You see her whole body slowly begin to relax."
show tarm sadt
t "Yes, you want to come? You did a great job, recruit, the least I can do is offer you a drink."
mc "...You just killed that whole gang."
t "Yes, I did."
mc "H-How can you be so calm? T-That was horrible! A-And who was that? A-Airi-"
t "Kid, stop talking. If we're going to have this conversation we'll have it after I've drunk enough to have it."
mc "...fine."
scene generictavern with fade
play music tavern
"The two of you are sitting in a tavern, the silence between the two of you is almost suffocating."
"Finally a waitress arrives and puts the two beers Taliya ordered on the table."
t "Thank you."
"Taliya grabs one of the mugs and starts drinking."
scene taliyadrink
mc "So..."
t "What?"
mc "Aren't we gonna talk about what just fucking happened?"
t "Hey! Watch your language, recruit. I'm still your general."
mc "...Sorry."
"Taliya's serious expression slowly melts into a much sadder one, she looks down at the table."
t "What do you want to know?"
mc "..."
mc "Who... Who exactly were those people? Were you really there just for the drugs?"
"Taliya takes a sip of beer."
t "No, I wasn't just there for the drugs... I hoped to save an old friend."
mc "And old friend?"
t "Yeah. That... That used to be my gang."
mc "...Your gang?"
t "They took me when I was a kid. You see, I'm an orphan, and in these poorer areas orphans in the streets are often taken in by gangs to use..."
mc "{i}She's an orphan...?"
t "Kids are an easy way to smuggle drugs, so they kept us."
mc "{i}Huh... Well I guess I do look less suspicious than her."
mc "So your friend..."
t "Airi... We used to look out for one another, we were like sisters."
mc "So... What happened?"
"Taliya looks up at you."
t "You're really asking a lot, [mc]"
mc "Yeah- Wait, you remember my name?"
t "Huh? Of course I do. Knowing the names of my recruits is part of my duty."
mc "I see."
mc "So... You're not going to answer that last question...?"
t "I won't. I'm not in the mood."
mc "I understand, sorry."
t "Ah... It's fine, it's understandable you want an explanation after everything that just happened."
mc "..."
t "I'll tell you the rest another day."
mc "Really?"
t "Yeah."
mc "{i}She's friendlier than I thought she'd be considering how stern she is at the Academy..."
t "How about we talk about you? How's the Academy going for you?"
mc "Huh? Oh, it's going fine."
t "You're pretty good with the sword, have you trained before?"
mc "Oh, no. I've never trained with the sword before."
t "Huh..."
mc "But I'm an adventurer, so I probably got some practice doing that."
t "I see. The guild in Randel honestly has a lot of high-rank adventurers, I'd bet any of them could be a great mentor, and they'd definitely be of great help at Hern."
mc "They're all really carefree, I don't think they'd be of much help at Hern."
t "The stronger an adventurer is, the more easygoing they are. They don't have to worry about etiquette like us in the army have to."
mc "Yeah... You're probably right."
t "Do you think you'll stay in the army after finishing the Academy?"
mc "I'm... I'm not sure."
t "It's fine, you still have time to decide. Just remember that whatever peace we have now is fragile."
t "You probably don't remember when the Demon King was still alive, but as soon as the Demon army will have organized itself again, we'll need people capable of defending out country at Hern, and you're going to be more than capable by then."
mc "...Thanks, ma'am."
"Taliya puts down her drink and looks around for the waitress and when she's found her she makes a gesture."
t "Alright, I'm done here, so I think I'll go. Are you done with your drink?"
mc "Uhm... No, there's still a bit..."
t "...[mc], you barely took a sip. You could've told me you don't drink."
mc "No, that's not it, I just... I just don't feel like it right now."
t "Give it here."
"You hand her your mug. She grabs it and then gulps it all down. You look at her with your mouth open."
t "So, did you buy a room?"
mc "Huh?"
t "A room. Don't tell me you're heading back at sunset."
"You glance outside and realize it's almost dark outside."
mc "Oh. I hadn't noticed it got so late... I guess I have no choice."
t "Mh, go ask the inn keeper. If you don't have enough silver I'll lend you some."
mc "Thanks."
scene generictavern
"You walk up to the counter where the Inn Keeper is writing something down. When he sees you he gives you a weird look."
mc "Uh, hello? Is there a free room I can rent for tonight?"
"Inn Keeper" "Ah, sorry chap, we're all out of rooms."
mc "Dang it."
"Inn Keeper" "Very sorry, mate."
mc "It's fine, I'll look somewhere else."
"Inn Keeper" "There's another inn fifteen minutes from here, right past the Market Square."
mc "Alright, thank you."
scene taliyadrink
"You go back to Taliya."
t "So?"
mc "They're full"
t "Ah."
mc "He said there's another inn fifteen minutes from here, I think I'll go there."
t "You can sleep in my room if you want, there's enough space for two anyways."
mc "What?"
t "Yeah, no point going all the way there."
mc "A-Are you sure?"
t "...Ohh! I get it. Ahaha, you don't have to be so shy recruit. In the army everyone sleeps together, it's nothing to be scared of... And anyways every time someone tried something funny they got their ass kicked either instantly or the next morning."
mc "Oh, aha... Well then, if you say so, I'll accept."
t "Let's go then."
scene corbaninnroom with fade
play music night
"The two of you walk upstairs and reach the room Taliya rented. Once inside you notice the room to be smaller than the ones in other inns you've been in... And so is the bed."
show prot normal
show tal normal
mc "{i}That's... I guess we're going to sleep real close."
show tal smilet
t "You can sleep on the bed, I'll use the floor."
show prot questiont
mc "What? Why would you sleep on the floor?"
t "I have a bedroll with my traveling pack, it's fine. The two of us can't fit in the bed any way."
mc "Then I'll sleep on the floor."
show tal sadt
t "It's not really necessary, I don't get why you're insisting so much."
mc "You're a lady, I won't take the bed if you'll have to sleep on the floor."
t "...Oh."
show tal smirk
"Taliya chuckles."
t "Fine then, I'll take the bed."
"Taliya puts down her bag and unties the bedroll. She gives it to you."
t "Here."
mc "Thanks."
t "Oh, I forgot to pay the tab, I'll be right back. Take a quick bath while I'm down."
mc "Alright."
hide tal smirk with easeoutright
"Taliya leaves the room."
show prot smile
mc "{i}I... definitely didn't expect this to go like this. Sleeping in the same room as General Taliya..."
"You put down your backpack next to the bed and open it. You take out a change of clothes, so glad to have one always packed."
mc "{i}Time for a bath."
"You head to the bathroom's door and as you get in you realize there's no lock. You look around to see if there's any other way to close the door shut, but it seems useless."
scene innbathroom
show prot normal
mc "{i}...Whatever it's not like she's the one who'd enjoy peeping on the other's naked body... Ahem."
"Inside the bathroom there's a bucket next to a tub, definitely bigger than the bed, which is already only half filled with water."
mc "{i}...If we're both supposed to bathe with this water I'll have to use as little water a possible."
hide prot questiont
"You strip and then get inside the tub, the water is lukewarm."
mc "{i}...What a day."
mc "{i}She really is as strong as they say... but I didn't expect a general of the army to have such a... \"questionable\" past."
mc "{i}If I tell anyone what happened today she's probably going to kill me."
"Suddenly you hear a voice from the other side of the bathroom's door."
t "Is there enough water?"
mc "Huh-! Uhm, not really? There's barely enough for myself..."
t "Alright, I'll go get some."
mc "A-Alright."
"A few minutes pass by when you hear Taliya coming back."
t "I'm back, brought the water."
mc "Thanks, I'll come get-"
show tal normal with easeinleft
"The door slams open and Taliya comes in with a huge bucket. You stand up and almost jump out of the tub."
mc "What the-!"
"Taliya walks up to the tub and looks at you, standing there, shaked and naked."
t "Uh, excuse me."
mc "Wh- Yes! S-Sorry!"
"You move to the opposite side of the tub and turn around as she pours the water in."
t "Now it should be enough for the two of us."
hide tal normal
"Then, without another word she puts the bucket down and leaves."
mc "{i}Uhhh, wh-what THE HELL just happened?"
mc "{i}She wasn't messing around when she said she was used to being around men..."
mc "{i}Then maybe... No, now's not the time, let's finish taking this bath and go to bed."
hide prot normal with dissolve
"You quickly finish washing yourself and put on your change. As you leave the bathroom you tell Taliya you're done and she heads in."
scene karnakinnroom
mc "{i}I'll go straight to bed, I'm so tired... But maybe I'll wait for Taliya to get out so I can say goodnight."
"You get inside the bedroll on the floor and lie there for a while."
"Finally, you hear Taliya get out of the tub. A minute or two passes by when she then opens the door... in her underwear."
show smiletanu with easeinright
mc "{i}Whoa mama."
t "Oh, you're still awake."
mc "I, uh... couldn't fall asleep."
t "You should. I'll leave early tomorrow and if you're not awake when I leave someone will probably kick you out when they find you."
mc "Yes ma'am."
t "Goodnight, recruit."
mc "Goodnight."
"Taliya blows out the room's candles."
scene black with fade
mc "{i}Time to sleep."
"The night passes by..."
stop music
t "{size=+2}Rise and shine, recruit!"
mc "Wuh- What the-"
t "Get up and get ready, we're leaving!"
scene karnakinnroom with fade
mc "What... It's morning already?"
t "Of course it is, and it's been for a while already as well."
mc "Nhhh..."
t "Come on, recruit, let's go."
"As you get up you look outside the window and see how there's barely any light outside yet and groan with contempt."
"Once you're finally done packing your stuff Taliya looks at you and grabs her bag."
t "Alright, we re leaving."
scene generictavern with fade
"As you leave the tavern she puts the room's key on the counter along with a note and then follows you outside."
mc "Yawn..."
t "C'mon, [mc], you'll start feeling sleepy soon enough."
"And so the two of you leave for Randel."
"After a while of walking in the forest, you look at Taliya and then speak up."
scene forest with fade
play music forest
mc "So..."
t "...So?"
mc "You said you'd tell me more about your past..."
t "Never said when."
mc "Oh c'mon."
t "Alright, alright... You've already seen too much anyway."
t "C'mon, ask. What do you wanna know?"
mc "Mh..."
label taliyaQuestioning1:
menu:
    "Why are you doing this?" if waydtT == False:
        $ askedTaliya1 += 1
        $ waydtT = True
        mc "Why are you doing this? Was it just for... her?"
        t "Today? Yes. But this isn't the first time I've busted a gang, I've been doing it ever since I've been allowed to by my rank in the army."
        mc "Really?"
        t "Ever since I was a child I've seen what gangs do to people, I've seen kids get addicted to drugs, friends turning on each other and do for money, I've seen kids getting killed in a dark alley because they kept a coin for themselves... And now I've seen my best friend die."
        mc "I... I didn't know it was that serious, in Randel-"
        t "Randel is the safest town in the east. Countless adventurers are always around and the Academy allows there to be so many veteran teachers around that even if someone tried to start something they'd be stopped in a day... Plus, without a lord to pay, corruption gets real hard."
        mc "...I guess that's true."
        t "But even then if drugs managed to get in Randel... it'd be a disaster."
        t "If only it wasn't for that damned Demon Army..."
        mc "What's got the Demon Army got to do with gangs?"
        t "Codayn is the official name, but it's more commonly called Breath... Demon's Breath is a drug manufactured by the Demon Army which has been smuggled in our country for the past two decades to destabilize Astylla. It was one of the last creations of the Demon King before his death."
        mc "Oh..."
        t "It's not like everything was fine and dandy before, I lived in the streets as a child before any of this and I was taken in by a gang before as well, but... Ever since the drugs arrived, everything has become so much worse that... I couldn't stand by anymore."
        t "It's why I ran from here and went to the Capital to join the army. I knew I couldn't stop any of this if I just stayed there, I needed real power to bring justice... But justice can't change people once they're so far off..."
        mc "..."
        jump taliyaQuestioning1
    "Are you doing this alone?" if aydtaT == False:
        $ askedTaliya1 += 1
        $ aydtaT = True
        mc "Is there nobody else helping you doing this?"
        t "...Yes, I'm always alone on missions, but I have a few trusted officers whom I trust with gathering intel for me. I know I won't get hurt in any of these missions, so I'd rather not take anyone else with me... I wouldn't stand to lose someone because of my incompetence like it almost happened today."
        mc "But you said it yourself, didn't you? If you were alone they could've escaped."
        t "Yeah, you're right, but I'd rather chase them for months than see more blood than necessary be shed."
        menu:
            "You can count on me.":
                $ countonmcT = True
                mc "You can count on me."
                t "What?"
                mc "If you ever need, I'll be glad to help you again."
                t "You almost died today."
                mc "But you saved me, General Taliya."
                t "Oh, don't call me that now."
                mc "You're strong, I trust that you can get just one person home safe."
                t "...{p}...Thank you."
            "...":
                mc "..."
        jump taliyaQuestioning1
    "Airi..." if airiT == False:
        $ askedTaliya1 += 1
        $ airiT = True
        mc "About Airi, your friend, I... would you mind telling me more about her? Why didn't she come with you?"
        t "I tried getting her to come with me... But it was already too late. Her way of dealing with everything around her was to accept it. She decided she was a part of the gang and begun rising the ranks... and she also got addicted to Codayn."
        t "I begged her to come with me but she wouldn't, so I left her and the town, promising I'd come back for her..."
        t "...And I did come back for her."
        mc "..."
        t "But it didn't go as I've always hoped it would, and now I know I'll only see her face again in my dreams... and my nightmares."
        t "I was weirdly calm after I killed her.{p}I could feel my body trembling a little afterwards but... I was numb. Killing my best friend felt like killing any other criminal... And that makes me feel much worse than having killed her."
        mc "...She wasn't the girl you knew anymore, years have passed and she was threatening to kill one of your recruits. She wasn't your best friend anymore Taliya."
        mc "You killed a stranger."
        t "..."
        "Taliya stares at her hands."
        t "Maybe you're right."
        jump taliyaQuestioning1
    "Who's Yami?" if yamiTaliya == False:
        $ yamiTaliya = True
        mc "Who's... Yami?"
        t "That's... my name."
        mc "...Probably a stupid question, but isn't your name Taliya?"
        t "...Taliya is the name I gave myself after leaving Corban. I didn't want anyone to be able to find out about my past, they might've stopped me from becoming what I am now if they knew."
        mc "Yami..."
        t "Gosh, it's so weird hearing that now..."
        mc "If it bothers you I'll call you Taliya."
        t "...Yeah, call me Taliya."
        jump taliyaQuestioning1
    "That's all." if askedTaliya1 > 0:
        mc "...That's all."
t "Mh."
"The two of you stay quiet for some time."
t "Hey, [mc]?"
mc "Mh?"
t "Thanks for listening."
mc "Uhm... it's nothing? I mean, I was the one asking questions, so of course I listened."
t "I... I guess you're right. I'm just not used to talking openly about this... or about anything really."
mc "Does that mean we're friends?"
t "Friends?"
mc "Yeah."
t "...I'll think about it, [mc]."
"She smiles and you smile back."
"And so the two of you walk all the way to Randel, casually chit chatting along the way."
scene villageback
show prot smile
show tal smile
mc "Looks like we're here."
t "Yup."
t "Well, [mc], it's time to part ways. I'll see you at the academy."
mc "I'll be there, ma'am."
t "Heh, goodbye."
mc "Bye."
hide tal
mc "..."
mc "{i}I guess I'm friends with General Taliya now... All because one guy wanted his sword."
mc "{i}...Worth it."
$ renpy.notify("{color=#fff}You gained 25 silver")
$ money += 50
pause 1
$ renpy.notify("{color=#fff}You gained 60 experience")
$ exp += 60
$ day += 1
$ time = 0
$ TaliyaQ = 1
$ persistent.Taliya1 = True
jump guild



label TaliyaQ1:
hide screen screenmap
hide screen hud
if TQ1p1 == False:
    t "I have to admit, recruit, you show a lot of promise."
    mc "Thank you ma'am."
    t "Come with me, [mc]."
    "Taliya moves towards a more open area and grabs a practice sword."
    t "Let's see how good you actually are."
    mc "Where's my practice sword?"
    t "Oh there's no need for one. Besides, you need to train with your own sword so that you grow accustomed to it as if it were part of your body."
    mc "But what if I hurt you?"
    t "Taliya chuckles."
    t "I don't think we have to worry about that yet."
    t "Alright, lets begin"
    show text "{color=#fff}Press space, click or tap the screen while the dot is on the green to win!" at truecenter
    pause 1.5
    hide text with dissolve
    scene taliyaminigame3
    $ fightMiniGame = "postTaliyaTrain1"
    $ fmgd = 6/(swordlvl/25)
    if fmgd < 1:
        $ fmgd = 1
    jump start_fightMiniGame
    label postTaliyaTrain1:
    if randel_fails < 3 and swordlvl > 12:
        "Taliya starts attacking you. It's clear she's not being serious, but you're still parrying all her hits. You're doing pretty good."
        "After a few parries you decide it's your turn to try and hit her so you step in and try a thrust. You can see a look of surprise on her face before she steps aside, parries you, and then taps you on the head with the tip of her training sword."
        t "Hit."
        mc "Not really that surprising."
        t "I'd say it was surprising, though. It's not often a novice can catch me off guard like that."
        mc "Well, thanks."
        t "It wouldn't take much to make you into a formidable swordsman. Just..."
        "She thinks for a second before continuing her sentence."
    elif randel_fails < 3:
        "You start parrying a few of her hits, and you think you're doing good, but Taliya soon decides she can be serious with you and with just two hits she knocks you down on the ground."
        scene taliyaq1b with hpunch
        t "Not bad recruit. I'm impressed."
        mc "And you still beat me with two hits..."
    else:
        "You parry a hit or two, but even though you think you're doing good, soon enough you stumble while retreating and end up on the ground."
        scene taliyaq1b with hpunch
        t "Not horrible, but there's a lot of room for improvement."
        mc "Thanks, I guess."
    $ randel_fails = 0
    t "Practice the basics more. You swing around your sword more than necessary, if you controlled it more you'd be able to hit and parry much faster."
    mc "Understood, ma'am."
    scene arena
    show tarm smilet
    show prot sad
    t "Come back when you feel ready again.{p}...Actually, on second thought, why don't you come in the evenings? We'll train then."
    mc "Uhm, isn't the academy closed at that time, ma'am?"
    "Taliya looks around to see if anyone's close enough to hear you speak and then looks back at you and whispers."
    show tarm smirk
    t "{size=-2}I have the keys."
    mc "Ohh..."
    t "Now go, train more."
    $ TQ1p1 = True
    jump academy
if TQ1p1 == True:
    jump sexxopaxxo
label sexxopaxxo:
if time < 3:
    "It's not evening yet."
    jump arenar
elif TaliyaTrain == False:
    t "There you are. Let's get started."
    scene taliyaminigame3
    $ fightMiniGame = "postTaliyaTrain2"
    $ fmgd = 6/(swordlvl/20)
    if fmgd < 1:
        $ fmgd = 1
    jump start_fightMiniGame
    label postTaliyaTrain2:
    if randel_fails < 3:
        "You immediately begin assault Taliya, trying to bypass her defenses, but it doesn't work. It's not like you didn't try or didn't put up a fight, but Taliya is just {b}that{/b} good."
        "So, Taliya simply pushes your sword to the side and then thrusts towards your chest."
        mc "Owch..."
        t "You're actually pretty promising, you know?"
        mc "Am I?"
        t "You are. At least compared to the rest of my recruits."
        mc "Sigh... Not like it changed much."
    else:
        "Once again, you manage to parry a few hits before Taliya thrusts and hits you in the chest, making you fall again."
        t "I can see you've improved."
        mc "Your sarcasm isn't funny, you just kicked my ass again."
        t "I did kick your ass again, but that's because I'm me, not because you didn't improve a bit. Your stance improved, you didn't trip on yourself."
        mc "Oh wow, I guess now I can lose standing."
    $ randel_fails = 0
    t "You're too negative, [mc], but I understand it can be frustrating. I {b}am{/b} way stronger than you and there's no way you'll beat me in a fair fight even if you train every day for a few yers."
    play music motivational
    t "Let's do it like this, to make it more feasible, I'll fight blindfolded."
    mc "...Blindfolded?"
    t "Yes."
    "Taliya takes a red cloth and ties it around her eyes."
    scene taliyaq1a
    mc "Are you... sure this works?"
    t "I am."
    mc "I still think somehow you're gonna beat my ass."
    t "Don't put yourself down, [mc], with that mindset you'll never become stronger."
    mc "I'm pretty sure it's impossible for me to beat you."
    t "Aren't adventurer supposed to do exactly that? Win against impossible odds? Come on, [mc], you can do this."
    mc "Sigh..."
    t "Hmm... I know. You're missing an incentive."
    mc "Huh?"
    t "Beat me and you'll get a reward."
    mc "...A reward?"
    t "Yes."
    mc "...What kind of reward?"
    t "I think I know exactly what you'd like, but you gotta beat me to find out."
    mc "{i}Huh? D-Does she really know? Is it what I'm thinking it is?"
    mc "Interesting... Alright, I'm in."
    t "That's it. There's the motivation I wanted to see."
    t "Now show me what you've got."
    "Taliya raises her sword."
    $ TaliyaTrain = True
else:
    t "Alright, let's see what you've got."
    "Taliya gets into position."
$ fmgd = 4/(swordlvl/10)
if fmgd < 1:
    $ fmgd = 1
if swordlvl < 10:
    scene taliyaq1a
else:
    scene taliyaq1c
$ fightMiniGame = "postTaliyaTrainChecks"
jump start_fightMiniGame
label postTaliyaTrainChecks:
if randel_fails < 3:
    $ randel_fails = 0
    jump heckYeahTaliya
else:
    $ randel_fails = 0
    jump fuckYouFailedAgainAgainstTaliya
label fuckYouFailedAgainAgainstTaliya:
    scene taliyaq1b
    $ sword += 1
    if chartrait == 2:
        $ sword += 1
    if sword == 2:
        play sound chime
        $ renpy.notify ("{color=#00C413}Your Sword stat has increased.")
        $ swordlvl += 1
        $ sword = 0
    "You try your best, yet it's clear you still have no chance against Taliya."
    mc "Sigh... Am I at least getting better?"
    t "Oh yeah, slightly."
    mc "Yay..."
    t "You can go now."
    "You leave."
    jump home
label heckYeahTaliya:
    $ sword += 1
    if sword == 2:
        play sound chime
        $ renpy.notify ("{color=#00C413}Your Sword stat has increased.")
        $ swordlvl += 1
        $ sword = 0
    if chartrait == 2:
        $ sword += 1
        $ renpy.notify ("{color=#00C413}Your Sword stat has increased twice!")
    "You try your best, and this might be the time where you actually manage to hit her."
    "You reach in with your sword but this breaks your stance and Taliya sends you to the ground with one strike."
scene taliyaq1b
t "Nice try, but it didn't work."
"As you get up, you look at her with frustration. Then, you see it: a cut in her clothes. You did it."
scene tt3
mc "Oh, I think it did."
"Taliya looks down on her clothes."
scene tt4
t "Oh, wow. Well done, [mc]."
mc "Thanks, thanks."
scene arena with fade
show prot smirk
show tarm smilet
t "This is the first step on y-"
mc "Now, now. Where's my reward?"
t "Reward? Oh, yeah.... I see you're impatient."
"Taliya grabs a book from the table and hands it to you. \"The Way of the Sword\" is written on its cover."
t "Here. This is one of the most important books a swordsman will ever read. It helped me a lot and it'll help you as well."
show prot questiont
menu:
    "Tell her it wasn't what you were expecting":
        $ askedTaliyaKiss = True
        mc "...A book."
        t "Uhm, yes?"
        mc "..."
        t "You don't like it? Don't you understand how important this is to learn swordsmanship?"
        mc "Yeah... I guess."
        t "Why? What kind of reward were you expecting? I hope it wasn't money."
        mc "I don't know, it was the way you said it that made me think that maybe......I'd get at least a kiss."
        t "...{p}...Hahahah!"
        mc "..."
        show tarm talk
        t "...You are serious, aren't you?"
        if mcTimid == True:
            mc "W-Well, y-yeah..."
        else:
            mc "I mean, that is a nice reward after all..."
            t "What-"
        "Taliya's face goes red."
        show tarm angryt
        t "Wh-Who the hell do you think you're talking to?! I-I'm your general!"
        show prot sad
        mc "But-"
        t "No but's! Get down and do me 20 push-ups!"
        mc "W-What?"
        t "You're still up?! Make it 50!"
        mc "Wait! I'm sorry!"
        t "...Y-You can't expect to say something like that and get away with it, recruit! Get to your push-ups or they'll turn into 100!"
        mc "But-"
        hide tarm angryt with easeoutright
        "Taliya turns around, all red in the face, and begins walks away."
        mc "...Grr."
        hide prot sad with easeoutbottom
        "You get on the ground and start doing push-ups. When you reach the 31st your arms give in and you fall on the ground."
        mc "Dang it..."
        "When you get up you see Taliya is gone."
        mc "{i}I probably shouldn't have said that."
        "You leave and go home."
        $ TaliyaQ = 2
        jump home
    "Just say thanks":
        mc "...Thanks."
        t "I'm glad you like it. Go home now and if you've got any questions you know you can ask me."
        mc "Alright, I will. Bye."
        t "Bye."
        "You wave at her and leave."
        $ TaliyaQ = 2
        jump home



label TaliyaQ2:
stop music
stop sound
hide screen screenmap
hide screen hud
play music home
"As you walk through the market you see Taliya in the distance, shopping in a casual attire."
mc "{i}Uh-oh... Let's leave."
"But just as you turn around, Taliya notices you."
t "Oh! hello there."
mc "{i}She's talking to me isn't she."
"She waves at you and walks up to you."
show tal normal
show prot normal
t "Good day, [mc]."
mc "Good day, ma'am."
t "I'm kind of lost, do you happen know where the woodworker is?"
mc "Carlo's? Yeah."
t "Could you show me the way?"
mc "Uh, sure."
hide prot normal with easeoutright
hide tal normal with fade
"You begin leading her towards the workshop."
mc "So, uh, why you heading there?"
t "The barracks need a few new tables, apparently it's been a while since last time they've been renewed."
mc "I see."
"After five minutes of walking, you finally arrive."
show prot hopet with easeinleft
show tal smile with easeinleft
mc "Here we are."
t "Thank you, recruit."
mc "No problem, ma'am."
if askedTaliyaKiss == False:
    jump didntAskTaliyaKiss
mc "{i}She hasn't mentioned what happened last time... And she's being friendly."
mc "{i}Maybe I could apologize for last time..."
label SEXNANDAYOOO:
menu:
    "Apologize":
        jump keepgoingtq2
    "Say goodbye":
        "This will end Taliya's route and prevent you from reaching the game's ending."
        "Are you sure you want to continue?"
        menu:
            "Yes.":
                mc "{i}Nah, it's alright, she seems to have forgiven me."
                t "Well, goodbye, recruit."
                mc "Oh, uh, bye general."
                "Taliya leaves, she looks kind of disappointed. You shrug it off and wal away."
                $ TaliyaQ = -1
                jump market
            "No.":
                jump SEXNANDAYOOO
label keepgoingtq2:
mc "Uhm, general Taliya?"
t "Yes?"
mc "I'm sorry for the other day."
show tal smilet
t "Apologies accepted. I'm sorry I wasn't clear enough, I should've expected something like that from a teenager..."
mc "Why, don't men flirt with you?"
t "No, I usually scare them away."
mc "Huh? Why?"
t "Why are you even asking? I'm the fearsome General Taliya, the Black Fire, the Demons' Demon, and many other dumb epithets..."
mc "Sexy."
t "Recruit!"
mc "I'm sorry, I'm sorry."
t "You're hopeless."
mc "No, but really, I'm sorry I shouldn't have said that, it was inappropriate and I didn't even thank you for your gift. Thanks."
t "You're welcome."
mc "I hope that we can... still be friends?"
t "..."
t "Yeah, sure, we can."
mc "Yippie!"
t "Don't get too excited or I'll change idea."
t "hehehe"
mc "Oh."
t "That was a joke."
mc "Ah... Haha..."
label didntAskTaliyaKiss:
t "Well, since you're here already, would you like to come in with me?"
mc "Sure, he's actually a friend of my uncle."
t "Oh, really? I see."
scene forge
"The two of you walk in and you see a small man working on a stool next to a window. When he notices you he waves."
"Carlo" "Welcome!"
mc "Hello."
"Carlo" "Oh? Do my eyes decieve me? [mc]!"
mc "Yeah, it'is me."
"Carlo gets up and walks up to you."
"Carlo" "It's been a long time you last came for a visit, and who's your friend?"
mc "Oh, she's Taliya, she-"
"Carlo" "General Taliya?"
t "Yes, that's me."
"Carlo" "Oh! What an honor, pardon my lack of courtesy. How can I be of assistance?"
t "The barracks' tables are old, we need new ones."
"Carlo" "Oh? Well maybe I can fix the ones you already have... I'll come tomorrow morning to check if they can be salvaged, otherwise I'll makes some new ones... It'll take me a week."
t "I see, thank you."
"Carlo" "No problem."
t "Well, then I'll go"
mc "Alright I'll-"
"Carlo" "So, boy, what's up?"
mc "Huh? I-"
"Carlo" "Come on, come, it's been a while since you've last visited, tell me what you've been doing these past months."
"You see Taliya leave as Carlo keeps talking with you. He seems to have no intention of stopping and after ten minutes you decide it's enough."
mc "Yeah, yeah, but now I really gotta go, there's a guy who's waiting for me."
"Carlo" "Oh? You're right, you're right, sorry kid, you know that when I start talking I don't stop. See ya!"
mc "See ya, it was nice talking with you."
mc "{i}Even though right now I wanted to talk with Taliya..."
"Carlo" "Take care!"
mc "You too!"
"And so you leave."
scene villagen with fade
play music market
mc "{i}Well, it's fine anyway, I'll see her tomorrow at the Academy."
"Just as you think that, you see a man in the distance running with a bag between his arms and before you can react, you see Taliya running after him."
mc "{i}What the- Who's so dumb to steal from General Taliya? Ah, whatever, let's go see what's going on."
scene taliyarapistalley
show tal normal
"You follow them through the town's alleyways, almost losing them repeatedly, they finally stop... But as you get closer you notice that now there's another man surrounding Taliya with the first one."
show taliyarapist1
"Man 1" "Wow, what a piece of woman you've got us today, Griehan."
t "Hand over my bag."
"Griehan" "Oh, I'm really sorry missy, here, you can have it back."
"You see Griehan extend his arm, bag in his hand, but as soon as Taliya goes to grab it, the man grabs her arm and pulls her closer towards him."
mc "{i}...These guys are so dead."
"Or so you thought, but Taliya doesn't move an inch as the man slides his hand on her ass."
"Man 1" "Be careful, she's got a sword."
"Griehan" "As if she can even use it. Missy here isn't gonna scare any of us."
t "I'll ask you again. Give me my bag."
"Man 1" "Hah! She's so funny! Bitch we aren't giving you anything back... at least not until we had our fun."
"Taliya stays still, her expression is like steel."
"Griehan" "You're right, let's have fun. Haze, undress her."
"Haze" "Immediately."
"Haze slowly takes off her belts, but Taliya still isn't moving."
mc "{i}Of for fuck's sake Taliya, the hell are you doing?"
"The man puts his hands on her shirt and starts unbuttoning it."
mc "{i}Enough's enough."
image angrynmcflip = im.Flip("angrynmc.webp", horizontal=True)
show angrynmcflip with easeinleft
show taliyarapist1 with hpunch
"Without another second of thought, you suddenly charge in and punch the man in the face. He falls to the ground and everybody looks at you shocked."
"Griehan" "You piece of shit!"
show  tal angryt
t "[mc]!"
mc "Hello there. Step away from her, scum."
"Haze" "You little- That hurt."
t "[mc], step away I'll handle this now."
mc "You will?"
"Griehan" "Yeah, tell your kid to get the fuck out of here if he values his life."
mc "I think {b}you{/b} should get the fuck out of here if you value your life."
t "[mc]..."
"Griehan" "Big words coming from such a small guy. How about you show me if you can fight too?"
mc "Sure thing."
"You ready your punches and then strike... Well, that was your intention anyways. He dodges your punch with easy and returns another punch straight in your chest. You feel your lungs empty themselves as you fall on the ground."
show angrynmcflip with hpunch
pause 0.1
hide angrynmcflip with easeoutbottom
mc "Fuck..."
show taliyarapist2
hide taliyarapist1
"The man points at Taliya."
"Griehan" "Alright, now you can stay there on the ground as we have our way with this sweetie here-"
hide tal angryt with easeoutleft
show taliyarapist2 with vpunch
pause 0.5
hide taliyarapist2
show taliyarapist3
pause 0.4
show taliyarapist4
hide taliyarapist3
pause 0.2
show taliyarapist5
hide taliyarapist4
pause 0.7
show taliyarapist6
hide taliyarapist5
"Griehan" "H-Huh?"
"Haze" "W-What the-"
show taliyarapist7
hide taliyarapist6
"Griehan" "FUCK! AGH-"
t "This will be the last time I ask."
scene taliyacreepy with flash
play sound horror
pause 0.5
"Taliya pulls her blade closer to herself, as if to taste the blood."
t "Give me my bag and scram... Unless you need something else amputated."
"Haze" "Fuck man let's leave she's not kidding!"
"Griehan" "Take your fucking bag!"
"Griehan throws the bag at her and runs away with Haze."
t "..."
stop sound
scene taliyarapistalley
show tal normal
"Taliya walks up to you and offers you a hand to get up."
t "You alright?"
menu:
    "Take her hand":
        "You grab her hand and get up."
        show prot normal with easeinbottom
        mc "...Thanks."
        t "You didn't have to do that, I had the situation under control."
        show prot angryt
        mc "You did? They were already undressing you."
        t "Yeah but they hadn't hurt me yet, so it's fine."
        mc "No it isn't, you're a woman, not an object. You should have more dignity."
        show tal smirk
        t "Pfft-"
        mc "What?"
        t "Oh, nothing."
        mc "..."
        t "Don't worry, if they ended up actually doing anything I'd have killed them."
        mc "Sure..."
    "Get up yourself":
        "You look at her hand then glare at her before getting up yourself."
        show prot angryt with easeinbottom
        mc "You could've done that sooner."
        t "What?"
        mc "Why were you leting them do those things to you?"
        t "Oh, how much did you see?"
        mc "Too much. I couldn't stand watching any longer and I went in."
        show tal smirk
        t "Pfft-"
        mc "Why the hell are you laughing?"
        t "Oh nothing, you're cute."
        mc "What?"
        t "Being heroic and all that."
        mc "Taliya I'm serious."
        t "I am too. If they ended up trying anything I'd have killed them. I was just giving them a chance to stop."
        mc "They were already trying something from what I saw."
        t "So what? They hadn't hurt me yet."
        mc "That doesn't matter, you shouldn't let anyone touch you like that, you're a woman not an object."
        "Taliya's eyes widen."
        t "Heheh~ Alright, alright, I'll keep that in mind. But who knows, maybe you'll have to save me again~"
        mc "...You're hopeless."
        t "I guess we both are."
        mc "Hah. Hah."
t "How did you find me, anyway?"
mc "Well, I saw that guy running and then you after him so..."
t "So you followed me."
mc "Yeah."
t "I see."
mc "Let's leave this place now though."
t "Alright- Wait!"
mc "What?"
show tal sad
"You see Taliya searching the inside of her bag. Then she sighs defeated."
t "Somehow, they still managed to take the purse with the money."
mc "The hell? When?"
t "No idea. Serves me right, I guess."
show prot smirkt
mc "Yeah, it does."
t "Hey!"
show tal smilet
"Taliya punches you lightly in the shoulder."
t "I'm the only one here allowed to make fun of me."
show tal smile
mc "Sorry, sorry."
mc "{i}It's really weird seeing her this friendly..."
t "Alright let's go back to the market square."
mc "Actually..."
"You point to the sky, it's already getting dark."
t "Oh, I didn't notice. Guess we're going to head home instead."
mc "Yeah."
t "Well, goodbye recruit."
mc "Wait, now that I think about it..."
t "Yeah?"
mc "Do you sleep in the barracks?"
t "No? Of course not. I stay at a place miss Scarlet arranged for me, it's between the Academy and the barracks."
mc "Oh, I see"
t "How come you're asking?"
mc "Oh, nothing."
t "Nothing, huh?"
show tal smirk
"Taliya grins."
t "Alright, bye [mc]."
mc "B-Bye?"
hide tal smirk with easeoutright
"Taliya leaves you and walks away."
scene taliyarapistalley with fade
mc "Why did she grin out of nowhere...? The hell..."
"And thus, kind of confused, you walk back home."
$ time = 2
$ TaliyaQ = 3
$ persistent.Taliya2 = True
jump home


label TaliyaQ3:
hide screen screenmap
hide screen hud
"When you arrive at the arena, you see Taliya waving at you."
show tarm normal
show prot normal
t "Morning, recruit."
mc "Goodmorning, ma'am."
show tarm sad
t "How's your...?"
"She points at your face."
show prot hopet
mc "Oh, that? I'm fine, I almost forgot about it.."
t "Good."
mc "So, uh... Any, uhm, development with your fight against drugs?"
show tarm smilet
t "Somehow it doesn't sound nearly as serious when you say it."
mc "Hey!"
t "...Though I didn't know you were interested."
mc "Well, of course I am."
show tarm talk
t "If you say so...{p}Well, just yesterday I got a letter from one of my men and I think I might have a lead."
mc "Oh, that's good, isn't it?"
t "Yeah, it is."
mc "So? What's the lead, if I can ask."
t "...Straight to the point, huh?"
mc "Yup, that's me."
t "Sigh... You see, I think I've found out who's the main distributor... and he's from Karnak."
mc "Karnak, huh? You'll head there soon?"
t "Yeah, that's the plan."
mc "{i}...Maybe I could go with her."
mc "Can I come with you?"
t "Are you serious?"
mc "Yeah, I told you I'd help."
"Taliya raises an eyebrow."
mc "Sure, you probably don't need my help but... I've never been outside of Astylla... Please...?"
t "......You're so annoying."
t "Fine, you can come."
mc "Yes!"
t "Meet me at the Market in the morning. Pack your stuff because we'll be out a few days, it's a long ride even with the wagon we'll be taking."
mc "Got it."
t "Now get back to training, though."
mc "Yes, ma'am."
$ penepisellosessoomosessuale = True
jump arenar



label TaliyaQ3b:
hide screen screenmap
hide screen hud
stop music
stop sound
"You arrive at the market pretty early in the morning and you see Taliya next to a wagon. You wave at her and she waves back as you walk up to her."
mc "Goodmorning."
t "You're late."
mc "But-"
t "No but's, c'mon get in the wagon."
mc "Alright."
"You hop on the wagon and then Taliya follows you. She knocks on the wall next to her and the wagon begins moving."
"It's been a long time since you last traveled in one of these. How much was it? 15 years? You couldn't tell for sure."
"But this time your destination is Karnak, a town beyond the safe walls of Astylla. For a moment a chill runs through your spine, but then you see Taliya sitting in front of you and you're reassured."
mc "{i}Nothing can happen if she's around."
mc "{i}Well, nothing to me."
#WIP - Have Taliya and the MC chit-chat about the world for some easy exposition.
play music forest
scene ambush1 with fade
pause 0.5
scene taliyacart1 with fade
"The journey there takes a few days. Most of it you spend chit-chatting with Taliya and staring at the ever-changing landscape around you."
"Finally, on the third day, Taliya announces how much time is left."
t "...Tomorrow we'll be there."
mc "Yeah."
"It's been three days already and you're really, really bored."
t "You should sleep now, we'll be there by tomorrow morning."
mc "Really? Then I'll gladly skip to that. Goodnight."
t "Goodnight, [mc]."
"And so you fall asleep on the wagon one last time..."
stop music
scene black with fade
"...{p}...{p}..."
"Taliya wakes you up."
scene taliyacart1 with dissolve
t "Wake up, we're almost there."
mc "Huh...? Where- Oh! Yes, Karnak, yeah."
"Taliya raises an eyebrow."
t "If you look outside you're still in time to see Karnak in it's entirety."
mc "Oh? Let me see!"
"You poke your head out in the desert and right there you see it. Karnak."
play music karnak
scene karnak with flash
pause 1.2
mc "Wow I... I had never seen the desert before. It's so... grand."
t "Yeah, it always feels like that, even after having seen it countless times."
mc "I bet it does."
t "Do you know the reason there's a desert here?"
mc "Because it's hot?"
t "Well, that too, but it's actually because the land here is toxic, filled to the brim with oil that so easily sprouts."
mc "Why would've anyone even have come here then?"
t "Well, it wasn't always like that. There was enough dirt on top to live without problem once, but the Demon King's army burnt this entire region... It's actually how they found out about their oil reserves. But before it still used to be a very rich province of the Old Astylla."
mc "Wow... And that huge tower is all of Karnak, isn't it?"
t "Now you know why they call it the Spiral City."
mc "Yeah, I can definitely see why. How further does it go?"
t "I'm not sure exactly, but I know the entire city has almost one million citizens."
mc "One million?! That's like... twenty times Randel."
t "And they all live just there without anyone bothering them... not even the Demon Army."
mc "Oil really is that valuable, huh? Though you'd figure the demons would attack this place."
t "Yeah, you'd figure, but in the past 15 years they haven't been attacked once by demons."
mc "Wow."
t "But yeah, oil is really valuable, and slaves make it much easier to get."
mc "Right, slavery is legal here."
t "Yes. And they don't even try to hide it. See that golden dome? That's where the rich live, right on top of everyone else... And the slaves, well, they're forced to live at the bottom of the city, where they work on the extractions."
mc "I wish we could do something about it."
t "Me too, but this isn't Astylla, I have no power here."
mc "And I guess another war on top of the one against demons isn't really a good idea, is it?"
t "Indeed."
mc "Ugh."
t "I hate this place too, but at least we won't have to worry about our treatment. Astyllians are treated very well, though it's mainly because they don't want a war either."
mc "Hm. And who is this distributor we're going to see? ...I hope we won't have to go at the bottom of the city."
t "Oh, no, he's a noble."
mc "Oh, thank Astylla."
t "I'll give you a briefing when we're there, even though we can already see the city so well it's still an hour away. Now that you're awake I'll get some rest."
mc "Huh?"
scene taliyacart2 with dissolve
t "..."
mc "Taliya?"
t "Zzz..."
mc "{i}What the- Can she just fall asleep on command like that?"
"You get closer to her and stare at her..."
mc "{i}...Wow, she really is sleeping."
mc "{i}Time to just stare outside until we arrive."
scene karnak
"And so you do exactly that. You stare at the Spiral City as it gets closer and closer and closer, until you're finally in front of the city's gates. There's dozens more wagons in front of yours trying to enter the city and just as many leaving."
scene karnakspire with fade
pause 1
t "We've arrived."
mc "Huh- Yeah."
mc "{i}Wh-When did she wake up?"
t "Man, there's always so many carts... The heat during the wait always gets unbearable."
mc "And how much will we have to wait?"
t "...At least an hour."
mc "Oh God..."
"..."
"..."
"..."
"An hour is a lot."
"..."
"..."
"You'll be waiting here for a while, won't ya?"
"..."
"Just kidding, {b}you{/b} get to skip it."
scene karnakinterior with fade
play sound market
"The town square is truly enormous. It really shows that this is the biggest market in the world. The arrays of little shops and stalls are never ending."
"As you walk through it, you finally reach the main street, on the sides there's countless bars, restaurants, bakeries, taverns and inns. If it weren't for the artificial light of the oil lamps, you'd think you were in the Capital"
show tal normal
show prot normal
mc "There's so many inns."
t "Yeah."
t "Which one should we pick?"
show prot hopet
mc "...You're asking me?"
show tal smile
t "Yeah, go ahead."
mc "Uhh"
"The choice is hard, especially because you don't know the price of each. Many are themed around something, some are even themed around being \"Adventurer Inns\"."
"The choice is hard but in the end you choose a little inn called \"Foxie's Inn\". It's in the corner between the main road and a smaller secondary street. It's not as tall or as impressive as any of the inns around it, but it's the only one that feels like an inn you'd see in a small Astyllian town, it really does just feel a lot more familiar than everything around it."
mc "Let's go there."
t "Alright."
scene innlowerfloor
"You go in carrying your bags. The place has less people than you'd expect from an inn in Karnak. You walk up to the counter with Taliya and see a lady in her mid-50s sitting there. She smiles at the two of you and Taliya buys a room."
"Inn Keeper" "It's the first one the the right, enjoy your stay."
menu:
    "Thank you":
        mc "Thank you."
        "You and Taliya go into your room."
        jump roomieYEEE
    "How come there's so little people in here?":
        mc "How come there's so little people in here?"
        "Inn Keeper" "Oh, it's normal."
        mc "It is?"
        "Inn Keeper" "Oh, yeah, we barely get any clients."
        mc "How come?"
        "Inn Keeper" "We're not rich."
        mc "...Huh?"
        "Inn Keeper" "Money is money, kid. If we got more clients the other inns would get less. They'd lose money and... Well, they don't want to lose money."
        mc "But that's not fair."
        "Inn Keeper" "Many things aren't kid. If you aren't born rich the middle floor is as far as you will ever get."
        mc "Isn't there anything you could do?"
        "Inn Keeper" "There is, we've already done it."
        mc "Like what?"
        "Inn Keeper" "We're the cheapest inn on this floor... But that's useless if nobody knows you exist."
        mc "Oh."
        "Inn Keeper" "It's alright kid, I don't complain anymore. Things are the way they are after all. Now go, your friend's probably waiting."
        mc "Alright, goodbye."
        "You wave lightly and then go to your room where you find Taliya."
label roomieYEEE:
scene karnakinnroom with fade
show tal smile
show prot smile
t "This place is surprisingly modest for Karnak."
mc "Yeah, I guess you're right."
t "...But it is also incredibly cheap, great choice."
"As you look around the room your realize it has two oil lamps on both sides of the room."
mc "Oh wow, even a place as small as this has oil lamps to light the room."
t "Oh right, you probably haven't seen many used to light a room, have you?"
mc "Nope, we don't really have any."
t "Yeah, even in the Capital most houses are still lit by candles. Oil might be a lot more convenient, but it's too expensive."
t "Anyways, enough talk. Put your stuff there and get changed if you want to. we'll be heading out in two hours."
show prot smirkt
mc "To catch the distributor?"
t "Yeah."
mc "Sigh... Well, I guess I've got two hours to visit Karnak."
show tal talk
t "We're not here on a vacation, [mc]."
mc "I know, I know.{p}Speaking of which, can you finally tell me who this guy is?"
t "Leon Varg, a very wealthy merchant... Excedingly so."
mc "So you think it's him?"
t "I don't think it's him, I'm sure of it. I've been investigating for years and everything always leads to Karnak... If he's not my guy, I don't know who could be."
mc "Alright, but how are we going to get this guy? Are we just going to walk into his house like last time?"
t "No, we can't do something like that here. I've found out where he'll be tonight."
mc "Where?"
t "A slave auction one floor below."
mc "And then what? We just talk to him? I don't think that'll be easy for us."
t "It won't, but I have a plan. We'll just use the auction to find him, we won't get him there."
mc "Couldn't we get him mixed up with someone else?"
t "It's a private auction... Well — it's more of a show than an auction — but no, he'll be the only one there, we won't get him mixed up."
mc "Okay, then. Sounds reasonable."
t "Mhm. We have time to get ready. I think I'll go to the bath house that's right across the street. If you want to come along I don't mind."
mc "{i}Come along? Of course I do!"
mc "Yes! ...I-I mean, y-yeah I sweated so much while we were waiting to get in..."
"Taliya stares at you unimpressed."
t "Let's go then."
scene karnakinterior with fade
"You leave everything you don't need in the room and grab a change of clothes, then you follow Taliya across the street to the bath house."
"When you enter, your dreams are immediately shattered: it's not a mixed bath."
mc "{i}Dang it..."
t "Don't wander too much when you're done, I need you back in time, got it?"
mc "Yes, ma'am."
t "...You know, you don't have to call me ma'am."
mc "I don't?"
t "You said we were friends, didn't you?"
mc "Yeah, I did. Sorry, Taliya."
t "It's alright."
"Taliya puts her towel on her shoulder and starts walking towards the women's bath."
t "I'm going in, see you later."
mc "Bye."
scene bathhouse with fade
"You sigh and walk into the men's bath. It's a really tall and large bath, definitely bigger than any other bath you've seen before. Just the pool is bigger than your house."
"As you walk to get into the bath, you see a fat, balding man already inside the bath. Behind him a young girl who's giving him a massage."
mc "{i}Wait, wasn't this the men's bath?"
"Then you notice the chains at her feet."
mc "{i}Oh... I guess slaves only count as property."
"Man" "No, no! It's further down."
"Man" "That's too low..."
"Man" "That's too high!"
"Man" "Put some more force into it, c'mon!"
"Man" "Ugh, you're worthless. Wasted silver on you for nothing. Leave."
"The girl looks down and then sheepishly leaves."
mc "{i}What an arse."
"You get in the bath and enjoy some relaxation. It's nice and all, but after a while you get bored and decide to leave. As you do that you see the other man sleeping inside the bath, probably having fallen asleep."
mc "{i}..."
show prot normal with fade
mc "{i}I wonder if Taliya is still bathing... wait, I could spy on the women's bathroom using the invisibility spell-"
show twignormal with easeinleft
show prot question with hpunch
"You bump into the slave girl. Her eyes widen and she immediately bows."
show twigtalk2
"Slave girl" "I'm extremely sorry, master!"
show prot hopet
mc "No, no, it's alright."
mc "...What's your name?"
"{color=#fff}Slave Girl" "M-My name, sir?"
mc "Yeah, your name."
"{color=#fff}Slave Girl" "...My master calls me Twig, sir"
mc "Twig."
"{color=#fff}Slave Girl" "Yes, sir. Master gave me this name b-because of my constitution."
mc "And what's your real name?"
tw "T-Twig?"
mc "Do you have no other name?"
tw "Uhm, n-no, sir."
mc "Do your parents call you Twig as well?"
tw "My mother died when giving birth to me, and I've never met my father, sir."
mc "...I-I see."
mc "{i}Let's change subject."
mc "How old are you, exactly?"
show twigtalk1
tw "Did I do something wrong, sir?"
mc "What? No. Why would you think that?"
tw "I'm not usually allowed to speak, sir."
mc "I just wanted to know more aout you."
tw "Know more about me?"
tw "...But, sir, I'm not for sale. I already have a master."
mc "{i}...So this is how slaves are brought up, huh?"
mc "I know you have a master, and he's an asshole."
show twigblush
tw "S-Sir, please don't say that."
mc "He is."
hide twigblush
tw "..."
mc "I'm not trying to buy you, I'm just trying to be friendly. Y'know what friends are, right?"
tw "But, sir, we can't be friends, it's against the law."
mc "What?"
hide twigtalk1
tw "I-I'm a slave, sir."
mc "And?"
tw "I-I..."
mc "I don't care about the law in this city, I'm just passing by."
tw "P-Passing by, sir?"
mc "I'm Astyllian, I'm not a master or a slave owner, I'm a person just like you."
mc "And if you find that hard to understand, just pretend I'm as much of a slave as you."
tw "B-But-"
mc "It's fine, really."
show twigblush
tw "..."
show twigtalk1
tw "How... H-How far is it?"
mc "What is?"
tw "A-Astylla..."
mc "Four days of travel."
tw "So far..."
mc "Have you ever left Karnak?"
tw "N-No..."
mc "Really?"
tw "N-No, sir. M-Master doesn't take me with him when he goes abroad."
mc "Of course not."
tw "..."
tw "D-Do you need anything else, sir?"
mc "[mc]."
tw "Huh?"
mc "It's [mc], not sir."
tw "I cannot call you by name, sir, nor anyone else."
mc "Not even if I ask you nicely?"
tw "I still cannot, sir."
mc "Can you at least drop the \"sir\"?"
tw "..."
"You hear her stomach grumble."
mc "You're hungry, aren't you?"
tw "No, si-{p}...No."
hide twigtalk1
"Her stomach grumbles again."
mc "Come, I'll give you some."
tw "Wh-What?"
mc "Food, for you."
"You grab her hand and pull her along."
tw "S-Sir...! M-My master is still in the bath!"
mc "The pig's asleep don't worry."
tw "P-Pig!?"
scene karnakinterior
show twignormal
"You walk across the street with her and tell her to stay there. You go into your room, grab an apple and quickly come back."
scene karnakinterior with fade
show prot hopet with easeinleft
show twigblush with easeinleft
mc "Here, for you."
"You hand it over."
tw "B-But..."
mc "It's yours now, eat."
tw "..."
"She reluctantly starts eating it. You smile as she begins eating it more eagerly with each bite."
tw "...Th-Thank you, sir."
mc "You can go back now."
tw "Thank you, s-"
mc "But first, please, call me by my name. Nobody will hear you."
tw "..."
tw "Thank you for the apple, [mc]."
mc "You're welcome."
tw "N-Now I'll go, my Master must be looking for me, goodbye."
hide twigblush with easeoutright
"She turns around and rushes back to the bath."
mc "{i}...And she's gone. At least she got an apple."
"You see Taliya walking home from the bath house wearing a coat."
show prot question
mc "What's that you wearing?"
t "It's for the auction."
mc "...Do I need one as well?"
t "No."
mc "Oh alright."
t "Who was that girl?"
mc "Uhm, just... a girl."
t "She was a slave, wasn't she?"
mc "Yeah."
t "......"
mc "What? She was hungry and I gave her some food."
t "Sigh... I'll let it slide this time. But please try to avoid getting attention onto us."
mc "Yes, Yes."
"The two of you finally go back to your room. Taliya is sitting on the bed."
scene karnakinnroom with fade
mc "So, the plan. I think it could be useful if I also know what we're going to do."
t "Alright listen, here's what we're going to do: We're going to be in the slave auction."
mc "The private auction?"
t "Yes. You see, there's a reason it takes place below this floor... He's looking for a sex slave."
mc "A... sex slave?"
t "Yes."
mc "And you're going to..."
t "Yes. And you'll have to pose as my master."
mc "I don't..."
t "What?"
mc "I don't really look like a slave master, do I? ...Especially not yours."
t "Don't worry, it'll be fine."
mc "If you say so."
t "I do."
mc "So, we get in like that... and then?"
t "If he buys us, he'll take us with him somewhere isolated, then we'll strike."
mc "And if he doesn't buy us?"
t "Then there's plan B."
mc "I'm afraid to ask you what that entails."
t "It's killing everyone."
mc "...I figured."
t "Don't worry, we'll do our best to be picked."
mc "Not that it'll be hard for you to be picked."
t "What do you mean?"
mc "Well, uhm, you, uh, are attractive and all."
t "You think so? That's new to me."
mc "Is it?"
t "Well... Guys never really hit on me. Even before I was a general."
mc "{i}You probably were just as scary before..."
mc "Well, it's true, so at least we won't be immediately ruled out."
t "Yeah, you're right."
"Taliya puts down her weapons."
t "Be sure to leave your sword and anything else you might have here, they'll probably check us."
mc "Alright."
"You put your sword down and then the two of you leave the room, heading towards the lower floor."
mc "Is it far?"
t "Not much."
mc "Alright."
scene karnakinterior with fade
"You walk, and walk, and walk. At some point you arrive at a grand staircase, one half heading upwards to the floor above, the other half heading down to the floor below. As you walk down you see how the decorations on the staircase slowly reduce in number and quality, so gradually that you only notice once you've reached the floor below."
mc "Wow, the difference is already palpable."
t "Yeah, it gets bad really quickly. Let's go, the place where the auction will take place isn't too far away."
mc "Alright."
"The two of you walk some more until you arrive at what was probably a warehouse once, but is now pretty rundown. You see a man leaning on the door."
t "{size=-4}Alright, merchant, it's time to begin our act."
mc "{size=-4}I'll do my best, ma'am."
"You walk up to the man and he stares at the two of you without saying a word."
mc "I'm here for-"
"The man shakes his head and then points with his thumb at the door."
mc "I see."
scene doorman1
"You knock."
"A grate in the door slides open, and you see a dimly lit face on the other side. Whoever it is he doesn't say a word, so you're forced to speak up first."
scene doorman2
mc "I've brought her."
"The man's eyes turn to Taliya who's standing behind you."
"Man 1" "...And the male performer?"
mc "Male performer?"
"Man 1" "Yes."
mc "{i}Shit."
mc "That's, uhm..."
"You look back at Taliya but she's looking at her feet."
mc "{i}Fuck, alright, whatever."
mc "...Me, I'm the male performer."
"Man 1" "...alright."
scene doorman1
"Then closes the grate."
"Man 2" "Alright stand still, I have to check for weapons."
"Man 2" "You, slave, take off your coat."
t "Yes, sir."
"Taliya removes her coat, and your mouth drops."
scene taliyaflash with fade
pause 1.3
mc "{i}Holy shit."
mc "{i}I guess she came well prepared."
"The man checks you pretty quickly, but then he moves to Taliya and he's much, much more thorough... You're doing your best to not snap at him for molesting her like that."
mc "Sir?"
"Man 2" "Yes, yes, I'm done. No weapons on her either."
"He goes back to the door and knocks three times, then he turns back at you."
"Man 2" "She's really well trained, she didn't flinch at all."
"You reluctantly smile at him as the door opens."
mc "Thanks."
"You and Taliya walk inside while you do your best to not stare at her half-naked body."
t "{size=-4}Good job."
mc "{size=-4}Thanks..."
scene auctionhouse with fade
"You walk through a hallway and then a man points you to a room. You enter and find yourself in a really tall room with a stage where several men and women are standing. A well-dressed man comes running towards you."
"Man" "Oh, for Astylla! You're late, you should've been here ten minutes ago, we're starting in two minutes!"
mc "Sorry, I had a problem with one of my slaves before departing."
"Man" "Ugh."
"The man then looks behind you and back at you."
"Man" "...Where's the male performer?"
mc "That would be me."
"Man" "Wanted to use her one last time before selling her? Whatever, you're number 10, get on the stage and go to your table."
mc "Yes, sir."
"The two of you get on the stage and move towards a table with a card on top of it with the number 10 written on it... But that's not all there is on the table. Right next to it there's a few \"Toys.\""
mc "{size=-3}A-Are we supposed to use these?"
t "{size=-3}...I don't know."
mc "{size=-3}Great."
"You look around and you see everyone at their own table, then, the man from before gets on the stage and clears his throat."
"Man" "The auction is now going to commence. I'd like to thank all the merchants for presenting us with their goods which we hope our acquirer will enjoy."
"The man gestures towards a person seated on a balcony high above. The shadow hides his face, but you can figure who it is."
"Man" "To show the value of these goods, the male performers will only use the tools provided to them to show the acquirer how durable they are, no oral, anal or vaginal sex is allowed, so please use them to your heart's content if you wish to impress our guest. Good luck, may the show the begin."
"And then the man leaves the stage."
mc "{size=-3}What the fuck..."
t "{size=-3}I didn't expect this."
mc "{size=-3}What do we do?"
t "{size=-3}Let's... Let's keep going."
mc "{size=-3}Are you sure?"
t "{size=-3}Yes. He's too far for me to reach him."
mc "{i}May Astylla protect me from the consequences of what I'm about to do."
menu:
    "I'm sorry, Taliya":
        $ good += 1
        mc "{i}Because it seems we have no choice."
        mc "{size=-3}I'm sorry, ma'am."
        t "{size=-3}It's ok, [mc]."
    "Lets get started":
        mc "Let's get started, then."
mc "{i}So..."
"You look around to see what the others are doing and see they've all tied their slaves with a rope hanging from the ceiling."
mc "Oh, right."
"You see a rope coming down from the ceiling right next to you."
mc "Time to tie you up."
t "...and then?"
mc "I don't know, I'll improvise along the way."
t "..."
t "I'll take these off then."
"Taliya removes the little clothes she had on and you begin tying her up to the ceiling."
mc "{i}This would probably be so hot if it weren't for our mission."
"When you're finally done, she's hanging ass up in the air."
scene taliyabondage1 with fade
pause 2
mc "{i}Now though... what should I do?"
label KEEPFUCKINGGOINGBITCHTHISISBONDAGE:
menu:
    "Clamps" if clamp4 == False:
        $ clamp4 = True
        mc "{i}Yes, let's use those."
        "You take the clamps and put them on her nipples, she flinches lightly."
        show taliyabondageclamp with vpunch
        t "H-Hey..."
        if butt4 == True:
            jump KEEPGOINGAHAAH
        jump KEEPFUCKINGGOINGBITCHTHISISBONDAGE
    "Butt plug" if butt4 == False:
        $ butt4 = True
        mc "{i}This is probably fine."
        "You take the buttplug and insert it."
        show taliyabondageplug with vpunch
        t "Ngh..."
        if clamp4 == True:
            jump KEEPGOINGAHAAH
        jump KEEPFUCKINGGOINGBITCHTHISISBONDAGE
label KEEPGOINGAHAAH:
scene taliyabondage1
show taliyabondageclamp
show taliyabondageplug
pause 1
mc "{i}And now, the only thing left is..."
"You look at the table and see a dildo, a gag, and a whip."
menu:
    "Dildo":
        t "{size=-3}[mc]... That motherfucker wants to see when we break, use the whip."
        mc "{size=-3}Y-You sure?"
        t "{size=-3}For fuck's sake, [mc], take it already."
        mc "..."
    "Whip":
        mc "{i}Alright, time to show how resistent she is."
"You grab the whip and get next to her to not cover the view."
mc "Get ready."
t "I'll take it."
scene taliyabondage2
play sound whip
show taliyabondageclamp
show taliyabondageplug with hpunch
pause 1
"You whip her once, she barely moves. Twice, and her expression doesn't change."
t "{size=-3}Harder..."
scene taliyabondage3
show taliyabondageclamp
play sound whip
show taliyabondageplug with hpunch
pause 1
"You whip her harder a few times, but she is still barely affected by it."
mc "{i}She really is made of stone, isn't she?"
t "{size=-3}Don't hold back."
mc "{size=-3}That's what I'm doing..."
"You take a deep breath and then hit her with all your strength."
mc "Take this, you slut!"
scene taliyabondage4
show taliyabondageclamp
play sound whip
show taliyabondageplug with vpunch
pause 1
t "Mh~"
mc "{i}Wait, did she..."
mc "Oh, you like this? What a slut."
t "C'mon! Harder!"
"You can hardly see him, but it seems the man up there turned his gaze to you two."
mc "{i}We got his attention! Let's not waste this opportunity."
mc "Oh, talking back, I see. Fine."
"You grab the gag from the table and put it on her."
scene taliyabondage4b
show taliyabondageclamp
show taliyabondageplug
pause 3
mc "The only noise I want to hear from you is moaning."
scene taliyabondage5
show taliyabondageclamp
play sound whip
show taliyabondageplug with vpunch
pause 1
"You whip her again, and then again, and again."
mc "How do you like that? Hard enough for you?"
t "Mnh~!"
scene taliyabondage6
show taliyabondageclamp
play sound whip
show taliyabondageplug with vpunch
pause 2
mc "{i}Wait is she... is she wet?"
mc "...Slut."
t "Mnh!"
mc "Look at you dripping wet, soaking the floor... I think I know a solution."
"You grab the dildo and thrust it in."
scene taliyabondaged3
show taliyabondageclamp
show taliyabondageplug with vpunch
t "Mmh~!"
mc "Oh yeah, you like that, don't you?"
"You keep thrusting in and out, now you're really starting to get turned on."
scene taliyabondaged2
show taliyabondageclamp
show taliyabondageplug
pause 0.5
scene taliyabondaged1
show taliyabondageclamp
show taliyabondageplug
pause 0.3
scene taliyabondaged2
show taliyabondageclamp
show taliyabondageplug
pause 0.15
scene taliyabondaged3
show taliyabondageclamp
show taliyabondageplug with vpunch
t "Mnh..."
scene taliyabondaged2
show taliyabondageclamp
show taliyabondageplug
pause 0.5
scene taliyabondaged1
show taliyabondageclamp
show taliyabondageplug with vpunch
mc "Cum for me."
t "Nh~!"
"Taliya squirts."
scene taliyabondageend
show taliyabondagesquirt with vpunch
pause 0.4
scene taliyabondageend
show taliyabondagesquirt with vpunch
pause 0.3
scene taliyabondageend
show taliyabondagesquirt with flash
pause 0.2
scene taliyabondageend
pause 5
mc "{i}This is definitely not an act anymore... We really just did this, and in front of all these people..."
mc "{i}I need to resist, I can't let us fail the mission... Only Astylla knows what I'd do to her right now if it weren't for that."
"Man" "Times up!"
mc "{i}Oh, thank Astylla."
"Man" "The acquirer has chosen."
t "..."
"Man" "Number 10! Congratulations, your slave has been chosen. Please untie her and follow me."
mc "{i}We won!"
t "{size=-3}Mhnnhm..."
mc "{i}Oh, right."
"You remove her gag, she's still panting."
scene taliyabondageend2
mc "{size=-3}We, uhm, we did it"
t "{size=-3}I-I know, now untie me, quickly."
"You untie her and give her back her clothes, then the two of you go down the stage, all the other merchants in the room are looking at you angrily, probably jealous."
"Man" "Please, follow me so you can meet the acquirer and discuss the price."
mc "Yes, please lead the way."
"The three of you walk to the other side of the room and go down through a hatch that leads to a corridor. At the end of it you see a door."
scene pervtorturecorridor with fade
show prot sad
"Man" "He's waiting you on the other side. Now if you excuse me, I'll go back up."
mc "Yes, thank you very much."
"Man" "It's my pleasure."
stop music fadeout 2
show taundiebase with easeinright
"The man leaves and so you're left alone with Taliya."
t "...Good job."
mc "...Thanks."
mc "{i}How are we supposed have a normal conversation after what just happened?L-Let's just move on."
"You begin walking towards the door."
t "{size=-3}Be ready."
scene tortureroom with fade
"You open the door and you find yourself in a room dimly lit by a single candle. You can vaguely make out a big sofa on the other side of the room where Leon Varg is sat. Separating you from him, there's a table with some papers on and a bag of what you assume to be gold."
scene pervcloseup with fade
mc "{i}I should say something..."
mc "Thank you for the honor of choosing my slave, master Leon."
"Leon" "The honor is mine, she is exactly what I was looking for, nothing more, nothing less."
"He gets up and walks up to her, he smiles and examines her, walking around her a few times."
"Leon" "Incredible physique. Is she used to doing hard labour?"
mc "{i}You could say that."
mc "Yes, master Leon."
play music dark
"Leon" "Excellent, she will last a lot longer then."
scene tortureroom with flash
"Leon pulls a rope hanging from the ceiling and the room lightens up and you can finally see everything there."
"And everything there is... terrifying."
"The walls of the room are covered in blood and scratch marks, right next to them, there's countless contraptions and devices, clearly used for torture."
mc "{i}What the fuck."
"Leon" "See, I'm really a particular kind of guy, it's hard to amuse me... But if there's one thing that I love, is seeing how long I can play with a slave until she dies."
mc "Taliya, I-"
"Taliya dashes towards Leon and pushes him up to the wall, grabbing him by the neck."
scene tortureroom with vpunch
"Leon" "Wh-what the hell is your slave doing?! Guard-"
"Taliya's hand is engulfed by a red aura and then it turns into a blade."
t "Scream and you're dead."
"Leon" "Wh-who the hell are you people?! Wh-What do you want from me?"
t "We're here to ask some questions."
"Leon" "H-Huh?"
t "Tell us everything about the codayn you sell."
"Leon" "C-Codayn? I don't know anything!"
t "Not talking, huh?"
t "Well, I guess we can repurpose what's in this room for you, can't we?"
"Leon" "W-Wait!"
t "[mc], grab this fucker."
"Leon" "No, please!"
"You walk up to him and grab him, he tries to fight back but even you are stronger than him."
t "Come here, we'll put him on this."
mc "Sounds good."
"Leon" "Please! Let me go!"
"You ignore him and take him up to a table with cuffs on both ends, it looks like some sort of torture device."
scene pervtorture1 with hpunch
"Leon" "P-Please..."
t "Don't take us for idiots. We know what you do already, we only need to know how and why."
"Leon" "I-I don't know what you're t-talking about!"
scene pervtorture2 with dissolve
"Taliya cranks a wheel and the contraption pulls his arms and legs further apart."
"Leon" "FUCK! P-Please!"
mc "...Are we sure we aren't making too much noise?"
t "I'm pretty sure they're used to this amount of screaming."
scene pervtorture2 with vpunch
"She turns the wheel further."
"Leon" "NGH!"
t "Speak."
"Leon" "...N-No!"
scene pervtorture3 with vpunch
"She turns it further."
"Leon" "AGH- OK! OK! I-I'll speak! I'll tell you everything! Please! It hurts!"
scene pervtorture2 with dissolve
"Taliya turns the wheel back slightly."
t "Alright, we're listening."
"Leon" "Th-They're made...{p}...Right here in Karnak."
t "What!? Where?!"
"Leon" "A-At the bottom... There's a network of caves..."
t "Who is making them? Are there demons in Karnak?"
"Leon" "No! O-Or at least I don't think so, I-I don't know them personally..."
mc "Then how did you get in contact with them?"
"Leon" "I didn't! One day they just started giving me this stuff for free!"
t "...For free?"
"Leon" "Y-Yes! I give them slaves every once in a while, b-but they're nothing compared to the wealth I receive from it!"
"Taliya looks at you."
t "...This doesn't sound right. Something sinister is going on. How do I reach these caves?"
"Leon" "Th-They're at the very bottom, I-I've never been there, but I know they're the only ones there! W-With the heat and the smell only slaves can be forced to go so far underground!"
"Leon" "P-Please let me go I don't know anything else."
t "You know we can't let you live."
"Leon" "No! I promise I won't tell anyone I've met you! P-Please!"
t "......"
"Leon" "P-Please...!"
"Taliya looks at you."
"Her arm goes back to normal."
menu:
    "Let him live":
        $ good += 1
        mc "...He won't say anything, c'mon."
        t "..."
        mc "We can let him go, he's not a threat to anyone not in chains."
        t "..."
        mc "I know he's a monster, but killing him won't change anything."
        t "Sigh."
        "Taliya starts cranking the wheel the other way."
        scene pervtorture1 with dissolve
        t "I hope you're happy, [mc]."
        mc "I am."
        "You untie Leon. You notice he's shaking as you do so."
        scene tortureroom with fade
        t "Let's leave."
        mc "Yes, let's go."
        "The two of you begin making your way towards the door."
        mc "{i}Oh, I really hope he won't say anything."
        "You hear steps rapidly approaching you, but before you can do anything Taliya dashes past you."
        "You hear something falling to the ground, and when you turn around you see the man you just freed on the ground, a knife clutched in his hand as he bleeds to death. Taliya standing in front of him with her back facing you."
        t "You were right, he won't say anything to anyone."
        mc "..."
        t "Let's go."
        "And as the two of you leave the room, Taliya speaks once again."
        t "Don't take it personally, [mc]. He was a disgusting man, and he chose to be one up till the very end."
        mc "...I guess you're right. He did deserve that."
    "Do what you have to do":
        $ evil += 1
        $ good += 1
        mc "...Do what you must."
        scene pervtorturecorridor with fade
        "You walk away outside of the room."
        "Leon" "...No, no, no! NO!"
        "You hear Leon's last choked scream, then Taliya come out from the door."
        mc "Let's go."
    "That would be too easy for him":
        $ evil += 1
        $ torturerMC = True
        mc "This bastard doesn't deserve a quick death, let me do it."
        "You turn the wheel."
        "His limbs are stretched even further."
        "Leon" "Agh-!"
        mc "All those innocent slaves... They went through this too, didn't they? You sick fuck."
        "Leon" "S-Stop!"
        "You keep turning the wheel."
        "Leon" "NGH-"
        mc "How many?!"
        "Leon" "AAAH!"
        mc "How many innocent people did you kill!?"
        "The image of Twig appears in your mind for a brief moment."
        "You hear a crack."
        "Leon" "AAAAAAAAAHHH!!!"
        t "[mc]! That's enough!"
        "Taliya pushes you away and stabs Leon in the neck, he gargles on his own blood as life quickly fades from him."
        mc "F-Fuck..."
        scene tortureroom
        "You feel your body shaking, your breath is heavy and you feel something wet running down your cheeks."
        t "[mc]...?"
        t "..."
        t "Are you ok?"
        mc "Y-Yeah..."
        "You wipe your tears."
        t "Let's go."
        "The two of you walk out of the room."
scene pervtorturecorridor with fade
"As you walk out of the building the two guards look at you surprised, but before they can do anything Taliya knocks one out with a kick and the other one by slamming him against the wall."
"She looks at you and then the two of you silently decide to go back to the inn."
scene karnakinnroom with fade
"Once there, the two of you sit on your beds."
show tal angryt
show prot shock down
t "...Alright, we got all the information we need. They really were under my nose all this time."
t "We could attack them tomorrow... But we should probably come back better prepared."
t "What do you think, [mc]?"
mc "......"
t "[mc]?"
stop music
show prot sad
mc "Huh?"
show tal sad
t "Are you sure you're ok?"
mc "Sigh... Yes, I-I am."
t "Alright, we'll discuss this tomorrow then, it's been a rough evening."
mc "No I'm fine. I just-"
mc "...I just can't believe people like him exist."
t "He got what he deserved."
if torturerMC == True:
    mc "You think I went too far?"
    t "No"
    t "Some people are too far gone to be saved."
    t "He chose how to live his life and he got his comeuppance."
    mc "..."
mc "...A-And back there, I'm sorry if I was too... rough."
t "What...? Oh! You mean that. Hahah..."
t "..."
t "Ahem. It's nothing I couldn't handle, and after all we didn't have a choice, did we?"
mc "Yeah, but I mean..."
t "It's thanks to your \"performance\" if that creep picked us."
mc "...I still feel bad about it."
t "Don't, forget it ever happened. It'll be better for both of us."
mc "I'm sorry."
show tal smirk
t "Oh stop apolgizing, you only brutally molested me."
"She gives you a coy smile."
show prot hopet
mc "Sigh... Alright."
show tal sadt
t "Seeing in what condition you are, I think it's better if we go back to Randel."
show prot questiont
mc "What? No! I can keep going."
t "I was stupid enough to bring you along, I won't take you further."
mc "What do you mean? I'm here of my own voliton."
t "I'm serious, [mc], this is dangerous."
mc "So what? I know you're the all-mighty Taliya, but I can handle myself too."
t "I understand but-"
mc "No, you're not doing this alone. You would've had to kill every single person there today if I wasn't with you."
t "......"
t "Alright, fine."
t "But we are still going back to Randel."
mc "Why?"
t "If the drugs are produced here... There could be anyone down there, we need to be much better prepared."
mc "...Why? Aren't you, like, super strong?"
t "I am, but I didn't bring my armor."
mc "Why?"
t "To be less noticeable."
mc "Alright... But what about Leon? Don't you think they'll just leave when they find out we killed him?"
t "They will if they find out, but when a member of his social status dies in such a place the authorities usually make a cover-up story up to explain his death."
mc "...But at some point they might find out anyways."
t "Yes, which is why we'll come back fast."
mc "Alright, I trust you. You're my general after all."
show tal talk
t "Oh yeah, right, I am. You {b}have to{/b} trust me."
mc "Yup."
mc "By the way..."
t "Yeah?"
menu:
    "Ask her about the arm-blade":
        $ persistent.TaliyaNecklace = True
        mc "...The thing you did earlier, the blade thing... How did you do that without a staff?"
        t "Oh it's actually quite simple."
        "Taliya grabs her necklace and shows it to you."
        scene taliyanecklace with fade
        pause 1
        mc "Is that...?"
        t "Indeed, it's a magic crystal."
        mc "They store mana, right?"
        t "Yeah, it's what allows me to cast spells quickly when needed... though if I use it too much then I need weeks to refill it."
        t "Fortunately I never need to use it for long. Thanks to this I can enhance my physical abilities enough to quickly end any fight."
        mc "Oh... So I {b}do{/b} have a chance to beat you."
        t "Oh yeah, in a million years when you'll be awarded one for becoming a Marshal of the Astyllian army."
        scene karnakinnroom with fade
        show tal smile
        show prot smile
        mc "They really are that rare aren't they?"
        t "Yeah, and for some reason every Diamond-rank adventurer I meet always has at least one."
        mc "Really?"
        t "Yeah, sometimes I'm really envious of you adventurers."
        mc "You shouldn't, you're stronger than any adventurer I know."
        t "Maybe with this, yeah. But without it... I'm not much better than many of my subordinates."
        t "I'm still just a human, and a woman at that... No matter how much I train there will always be someone stronger than me, either human or not."
        t "This crystal allows me to be on par with monsters much stronger than me... But even so, often that's not enough."
        mc "...Often enough is enough."
        t "...But hey! It {b}does{/b} take a lot of training and endurance to use a crystal. Most people would get knocked out if they tried to use it."
        mc "Really?"
        t "Of course. I'm still not some random shmuck."
        mc "Oh, I never thought differently."
        t "Let's head to bed now. We have to sleep while we can."
        mc "When are we heading out tomorrow?"
        t "At dawn."
    "Nothing":
        mc "Ah, nothing, let's just go to bed."
        t "Alright, at bed we shall go. We'll leave at dawn."
show prot question
mc "But that's in a few hours-"
t "Good, a few hours of sleep. Let's not waste them."
mc "...Alright."
scene karnakinnroom with fade
"The two of you hop into your own beds."
t "Goodnight."
mc "Goodnight."
"Taliya turns the lights off and the room goes completely dark."
scene black
mc "{i}Wow, today has been... overwhelming."
mc "{i}Slavery is so foreign to me... But before the current king rose to power it was legal in Astylla too..."
mc "{i}How could people treat others like that? How could he torture to death so many human beings..."
if torturerMC == True:
    "..." "{sc=1.5}You did the same thing{/sc}"
    mc "{i}That was different! He deserved it.{p}...I did nothing wrong."
mc "{i}...Now he won't be able to do it anymore."
mc "{i}......."
mc "{i}...And also the stuff I did to Taliya today... Maybe I went too far."
menu:
    "But I liked it":
        mc "{i}But... I still liked it."
        mc "{i}Is that really weird, though?"
    "It was necessary":
        mc "{i}It was necessary."
mc "{i}...But I also feel like she liked it."
mc "{i}She moaned and she even came... That only happens when you're enjoying it, right?"
mc "{i}Ugh, whatever, let's just go to sleep."
mc "{i}I only have a couple of hours of rest."
scene black with fade
"And so you close your eyes shut...{p}...{p}And you fall asl-"
t "Wake up, recruit!"
mc "Wuh-"
scene karnakinnroom
t "It's dawn we need to go, get ready."
t "I packed our stuff and already put it on the wagon, let's get going."
mc "W-Wait, you didn' have to... You could've... yawn... woken me up earlier."
t "Yeah sure, come on let's go."
scene karnakinterior with fade
"She forces you up and then you two leave the inn and get on the wagon. As soon as you sit down you fall asleep again."
scene black with fade
"The way back isn't that much different from the way there, but with everything that happened at Karnak, it really feels like a different journey."
scene villageback
"And so once again you end up in Randel. The wagon stops in the town's square and Taliya and you hop down with your bags."
t "Alright recruit, go gome and get some rest. You deserve it."
mc "When are we going back?"
t "Rest first. I'll let you know when we're going back."
mc "Alright."
"You turn around to leave, but Taliya calls after you."
t "[mc]... Thank you for helping, I mean it."
mc "You're welcome."
t "See you later, kid."
mc "See ya."
"And thus you go back home."
$ TaliyaQ = 4
$ time = 1
$ day += 7
$ t4qt = day+3
$ persistent.Taliya3 = True
jump home

label TaliyaQ4Pre:
show tarm talk
show prot smile
t "Oh hello there, I was looking for you."
mc "You were?"
t "We're departing tomorrow."
mc "Alright, I'll get ready."
t "Excellent, we'll meet tomorrow morning at the market then."
t "Make sure you bring everything you need, who knows what we might run into down there."
mc "Got it."
$ Q4Pre = True
jump arenar

label TaliyaQ4:
stop music
stop sound
hide screen screenmap
hide screen hud
show prot smile
"At the same place as the last time, you find Taliya and a wagon. You wave at her and she waves back."
show tal smile with easeinleft
t "Good, you're here. Let's get going then."
scene taliyacart1 with fade
"The two of you get into the wagon and once again you leave."
scene black with fade
"..."
"..."
scene karnak with fade
play music karnak
"...And just like last time, after three entire days, on the morning of the fourth, you arrive at Karnak. This time around there's less people than last time, but Taliya tells you that it's simply because today isn't a busy day."
scene karnakinterior with fade
show prot question with easeinright
show tal normal with easeinright
mc "So, are we going there directly?"
t "I don't see a reason to wait. Let's start making our way down."
mc "Alright."
hide prot question with easeoutleft
hide tal normal with easeoutleft
"And so, the two of you start your descent into the depths of the Spiral city."
scene movingdownslums with fade
"Soon enough the wide staircases of the ground floor become narrow pathways running along the walls in a giant spiral towards the bottom of the city. Every floor you go down the more houses seem to be rundown, at some point even a few tents start appearing, and people start to look more ragged. The only buildings that never look any worse are big industrial complexes, shining in the middle of each floor."
"Finally after almost an hour of descending, you see a dozen guards blocking the staircase further down. They all turn to look at you two."
t "We need to pass."
"The guards stay silent for a moment as they look at each other, then one looks back at Taliya."
"Guard 1" "...Came to pick up a slave?"
t "Yes."
"Another guard with a big notepad looks up at Taliya."
"Notepad Guard" "Name and permit."
"You notice Taliya twitching lightly."
t "Sorry, I explained myself badly. I have reason to suspect that a slave stole a valubale item from me and is down there."
"A guard scoffs. He has more armor than his companions and a big feather sticks out at the top of his helmet. He's probably the captain."
"Guard Captain" "A slave... stole from you and you think they're in the slave district? I'm sorry missy but I don't think that's possible."
t "Why not?"
"Guard Captain" "You're not from here, are you?"
t "We are not, we were supposed to depart today but I can't without the item I lost."
"Guard Captain" "Hah! Alright let me explain this to you, Astyllian. The place we guard the entrance of is the Slave District."
t "Yes, I know as much."
"Guard Captain" "Everyone who passes through here is searched by us, and we found nothing."
t "Could you not have missed it?"
"Guard Captain" "No, we couldn't have. We {b}love{/b} being thorough in our searches."
mc "..."
"Guard Captain" "Listen, the only slaves down here are working slaves, or slaves who behaved badly. If a slave stole anything and is in here, chances are the master found out they stole something and decided to punish them..."
"A guard snorts."
"Guard 1" "If this item is so valuable I doubt his master returned the item to the authorities, you better look for the owner."
"All the other guards laugh, though the captain manages to remain composed with a smile."
t "Well, I don't know the name of the master. If you let us pass we can identify the slave, ask for their master's name and we'll be on our way."
"Guard Captain" "..."
"Guard Captain" "You know, Missy, if you wanna go through so badly you can just ask."
t "..."
t "Can we go through?"
"Guard Captain" "Sure! But how about first you... lend us a hand?"
"The guards all laugh again. But you aren't finding it funny at all, and neither seems Taliya."
"She begins walking closer to the captain, and for a moment you fear she might do something rash, but then she hands him a pouch."
t "There's a hundred Astyllian gold coins in there. Enjoy."
"The guards remain all speechless and she starts walking past them. She gestures you to come as well, and you quickly make your way as well before they change idea."
"You start descending even further down. Once your far away from the guards you look at Taliya."
mc "...Was that all your money?"
t "Yes."
mc "Are you sure that was a good idea?"
t "We're not staying here for long. We'll leave as soon as we're done with this, I only brought it for emergencies."
if money < 1:
    mc "Well I didn't bring any so we'll definitely have to avoid emergencies."
else:
    mc "Thank god I've brought along [money] coins then."
if money >= 100:
    t "What- Why did you bring so much money along? You shouldn't bring that much on yourself. You might lose it."
    mc "Eh, never happened so far."
    t "Well, that's dumb."
elif money >= 20:
    t "Huh, well that's good to know. I really thought I had just gave up all our money."
    mc "You're welcome."
    t "Thanks, [mc]."
elif money >= 5:
    t "...You could've brought at least 20 coins."
    mc "Sorry, sorry."
    t "It's alright."
scene slums1 with fade
"Finally you arrive at the new floor and what welcomes you is, to be flattering, a shanty town. There's almost nothing that could be categorized as a building anymore, only tents made out of sheets and clothes."
"The only thing that can be considered a building is in the middle of the floor. A gigantic refinery, taking up almost half of the floor with all its adjacent structures."
"Hundreds of slaves are roaming around, most of them working while having barely anything to dress with, and a few are fighting over whatever little food they managed to find..."
"...As you're taking the view in, your nostrils suddenly fill with an abhorrent stench."
mc "Cough-"
"You see Taliya starting to walk quickly."
t "Let's be quick, this place smells worse than troll guts."
mc "Y-Yeah..."
"You follow her through the floor, apparently the way further down doesn't use the spiral staircase you had grown accustomed to and you need to traverse the district instead. As you walk past everyone, they all stare at the two of you, some are amazed, some seem to be ready to jump you, most look at you with pleading eyes."
"Taliya forces you to ignore them as she starts walking even faster until you reach a ledge with a metal ladder leading into pure darkness."
show prot sad
show tal normal
mc "Please don't tell me we're going down there."
show tal talk
t "We're going down there"
mc "Damn it."
t "Cover you nose with something, the smell's only going to get worse."
"You get on the ladder and descend to the lowest floor of the city."
scene darkcave with fade
"The smell gets as bad as it can once you reach the bottom. The ground is soggy, the whole place is extremely humid and hot... There's probably a reason not even the slaves are sent this deep."
mc "I think I'm going to throw up..."
t "Resist, [mc]. Whatever we're looking for can't be that further away."
"As you walk your eyes slowly get used to the darkness. You still can't see much, but you can tell some of the shapes apart."
t "Follow me, I'll lead you."
mc "Thank you-"
"You try to reach for Taliya but your foot catches something and you trip."
mc "Ow..."
"You sit up and look in front of you, looking for Taliya, instead you find something much more horrific."
scene corpse with vpunch
stop music
play sound horror
mc "AHHH!"
"Taliya turns around."
scene darkcave
t "Are you alright?!"
mc "I-It's... a b-body."
t "..."
t "So they really use this place as a dump."
"You feel your breath starting to pick up speed."
mc "Th-this place sucks, fuck! I'm not so sure I want to do this anymore."
"You feel Taliya grabbing you by the shoulders."
t "[mc]. Calm down."
mc "I-"
t "Breathing fast will only make the stench worse, relax."
"You feel Taliya's grip tightening, not enough to hurt you, but enough to make you feel more safe."
mc "..."
t "..."
"Your breath goes back to normal and you put your hand on hers."
mc "...Alright, I think I'm fine now."
t "Good."
"She lets you go."
t "Let's continue, the sooner we get this done the better."
"The two of you start to move again, but after just a minute, Taliya stops in her tracks."
t "You hear that?"
mc "What?"
t "Flowing water."
mc "...Now that you mention it, yes."
t "We're close."
"You follow the sound until you reach the entrance of a cave."
t "Found it."
mc "Finally."
t "Be ready."
mc "I am."
"The two of you go into the cave, it's a very long path but this comes with its benefits. Soon enough the smell gets better, then, in the distance you see torches."
mc "What the..."
t "Be quiet."
"The two of you silently move forward until the cave ends and you find yourself in a giant chamber, big stalactites coming down from the ceiling."
scene cavechamber with fade
mc "...I don't see anyone."
t "They couldn't have left so quickly."
"As you explore the chamber further you see dozens of sacks on one side of the chamber. Taliya cuts one open and a thick red dust starts leaking from it."
mc "...Codayn?"
t "Yes. They're definitely still using this place, they wouldn't have left behind so much produce."
"You keep walking until you arrive to a wide clearing. Small rays of light coming from the ceiling of the cave through small cracks revealing a hooded figure standing across the clearing."
mc "Wait, there's-"
play music creepymusic
scene demoncultist1 with fade
"Figure" "Welcome, General Taliya."
t "...Of course they were expecting us."
"From the dark several more hooded figures come out and surround you."
mc "An ambush!"
"The two of you draw your blades."
t "Get ready."
"Figure" "Oh c'mon, there's no need for weapons. We mean no harm, general."
t "How did you know we were coming?"
"Figure" "This is our home, general, we have eyes and ears all over this city."
mc "But how..."
"Figure" "My name is Maleik and we are all humble servants of the Demon King."
t "Betraying your own kind?"
mal "My kind? I wish to have nothing to do with such lowly beings. Our objective is to ascend and become the superior lifeform: Demons."
"He takes off the hood."
scene demoncultist2
mal "...As you can see we have already made some progress."
mal "We serve our lord, aiding in the distruction of humanity, in hopes that he will allow us to become demons like him."
t "..."
mal "As our lords fight at Hern, we corrupt Astylla from the inside. And there is no better way to do it than corrupt the minds of Astyllians with our drugs."
mc "...These people are crazy."
t "They are. Delusional too."
mal "Delusional? You are mistaken, you see, our drug isn't meant to simply corrupt the mind... but the body as well."
t "What...?"
mal "Let's show you what we've already achieved."
"The ground trembles and then from behind Maleik a huge monstruosity comes out."
scene taliyaminotaur with flash
play music battlemusic1
mal "Behold our power!"
mc "Th-That's... a minotaur?"
mal "This is Lawsen, he is the first of us who has achieved ascension and become a demon!"
t "I guess you weren't totally lying..."
t "Let's see if it's like the real deal."
"Taliya charges at the minotaur. She is incredibly fast and when he tries to attack her, she easily evades him. She grabs her sword and stabs the demon's hand, and even though the minotaur strikes back, she avoids it again."
mc "Wow... She's so-"
"You'd like to cheer for her, but unfortunately, the cultists attack you."
mc "{i}Alright, let's find out if training with Taliya wasn't for nothing."
scene cultistattack1 with vpunch
if swordlvl >= 10:
    $ renpy.notify ("{color=#fff}Sword skill check: {color=#00C413}Success! ([swordlvl] >= 10)")
    $ round1banditfight = 0
    jump finishfightt1
$ renpy.notify ("{color=#fff}Sword skill check: {color=#A50000}Fail. ([swordlvl] < 10)")
$ fightMiniGame = "abgiaeguodaghu"
$ fmgd = 3/(swordlvl/8)
if fmgd < 1:
    $ fmgd = 1
jump start_fightMiniGame
label abgiaeguodaghu:
$ randel_fails = 0
label finishfightt1:
    "They're good, just... not as good as you."
mc "Is that it?"
"You easily parry the few first hits, but you're losing ground. It's clear that their superiority in number is giving them an advantage."
"Cultists" "You won't get away with this!"
scene cultistattack1 with hpunch
if swordlvl >= 10:
    $ renpy.notify ("{color=#fff}Sword skill check: {color=#00C413}Success! ([swordlvl] >= 10)")
    $ round1banditfight = 0
    jump finishfightt2
$ renpy.notify ("{color=#fff}Sword skill check: {color=#A50000}Fail. ([swordlvl] < 10)")
$ fightMiniGame = "abgiaegu247odaghu"
$ fmgd = 4.25/(swordlvl/8)
if fmgd < 1:
    $ fmgd = 1
jump start_fightMiniGame
label abgiaegu247odaghu:
$ randel_fails = 0
label finishfightt2:
"Incredibly, you are managing to hold back all the cultists. It's probably not much considering they have probably never trained in their life and you hardly hit anyone, but you're still proud of yourself."
"...Or at least you were until you realize that Taliya has already defeated the minotaur. When the other cultists notice, they all get out of the way."
scene cavechamber with fade
t "Was that it?"
mal "You truly are the strongest Astyllian general."
"You start to smell something foul, then you notice green smoke surrounding you."
mc "Cough..."
mal "...Now imagine how strong of a demon you'd make."
t "Wh-What..."
"You see Taliya fall to her knees in front of you, and soon after you're on the ground as well."
mal "I never meant to kill you, Taliya, we want you alive. We want you as our strongest asset."
"The smoke is now so thick that you can hardly see Taliya anymore... Your vision is getting blurry."
mal "Don't worry this will only make you sleep."
t "[mc]... It's time to run."
"The two of you gather all your strengths and get up and you make a run for it."
label qborqorouqrb:
$ gameover = "qborqorouqrb"
mal "Get them."
scene darkcave with dissolve
"The cultists start running after you. The two of you are too dizzy to escape together."
t "They're going to get us... UGH!"
t "[mc]! Run! I'll hold them off!"
mc "What?! No!"
t "They'll catch us both!"
mc "I'll hold them off then!"
t "You can't, for fuck's sake! It's an order, recruit, run!"
menu:
    "Don't leave":
        mc "I'm not leaving you behind."
        "You stop and turn around. You unsheath your sword and prepare to fight. Taliya does the same."
        "The cultists catch up to the two of you and the fight begins... But you can hardly call it that. After just a few swings your arms already feel heavy, and then you hear Taliya falling to the ground."
        mc "T-Taliya!"
        "You keep fighting, but you can hardly hit anything with your sluggish swings."
        mal "I have to say, for a human you sure have a lot of resistance."
        "Someone pushes you down and you try to get up again, but your body works agains you."
        mal "...Too bad you're still weak."
        mal "Kair, kill him."
        mc "{i}No! Wait!"
        "You try to protest but no words leave your mouth. The last thing you see is Taliya being taken away."
        jump GameOver
    "Leave":
        mc "I'll come back for you!"
"You run. Taliya stays back."
stop music fadeout 4
"You run. You hear her grunts and the clashing of a sword."
"You run. You can't hear Taliya anymore."
"You stop. You've reached the ladder."
"You make your way up and then... everything goes dark."
scene black
pause 5
"You wake up in a rush, gasping for air."
mc "Where- Where am I?!"
scene tentinterior with dissolve
mc "{i}...A tent?"
show twignormal
tw "Hey."
mc "T-Twig?"
tw "...I'm glad you're alive."
mc "Wh-Where am I...?"
show twigtalk2
tw "You're in my tent, we're at the bottom of the city. I found you unconscious next to the Dump-"
mc "Taliya! Where's Taliya?"
tw "T-Taliya? I-Is she a friend of yours? I didn't see anyone else at the Ledge..."
"She looks a bit startled by your panicking."
mc "The ledge..."
"You frown as you hold your head with hand. It hurts a lot."
tw "You're very weak, I think you should rest."
mc "No, I can't, I need to go get Taliya."
"Twig completely ignores you and grabs a cup with water. She hands it to you."
tw "Please, drink some."
mc "Th-Thanks..."
"You grab the cup and drink from it, just that already makes you feel a bit better."
show prot questiont with easeinbottom
show twigtalk1
mc "I really need to go. I need to save Taliya before it's too late."
tw "Your friend is in danger?"
mc "Yes... They took her away and are going to turn her into a demon. If I'm not quick enough..."
tw "...Turn into a demon?"
mc "Yes."
tw "But if they took away your friend and knocked you down too, why do you know you'll be able to save her?"
mc "I don't."
tw "Th-Then why bother?"
mc "Why bother? She's my friend!"
tw "..."
tw "Friends... You would risk your life for them?"
show prot hopet
mc "Yes, and I'd do the same for you."
show twigsmile
tw "I see."
"She sighs."
tw "...But you're still weak."
mc "It's the poison... It'll go away."
tw "Alright then... have this."
"She grabs a piece of bread and hands it to you."
mc "No don't worry, I'm not hungry."
show twigblush
tw "...Please, I don't know how to repay you otherwise."
"You sigh."
mc "Alright, you win."
"You grab the piece of bread and eat it, she smiles lightly."
mc "I need to get back. Now."
tw "B-But you just passed out!"
mc "I don't care."
"You get up even though your body feels still a bit wobbly and walk out of Twig's tent."
scene slums1 with fade
show prot normal with easeinleft
tw "W-Wait!"
mc "I can't! Taliya might die if I'm not quick."
tw "..."
tw "Can I help you in any way?"
mc "You've already done enough, Twig, thank you."
tw "...Wait! I know."
"She rushes back into her tent and after a few seconds she comes back with a piece of cloth."
show twigsmile with easeinleft
tw "Here, you can use this to help you breathe down there."
show prot hopet
mc "You didn't have to."
show twignormal2
"She glares at you."
mc "Alright, alright. Thank you very much."
"You grab the cloth and tie it around your face. It doesn't help much, but it's definitely better."
mc "Now I have to go, Twig."
tw "Be safe."
mc "I'll try."
"You starts making your way to the ledge."
mc "{i}Why is Twig here...? She doesn't look like a working slave... Did that pig send her here to punish her?"
menu:
    "Get her out of here":
        mc "{i}She's too much of a nice girl to deserve this. After I've rescued Taliya I'll take her with me to Randel."
        $ twigRescue = True
    "Don't do anything":
        mc "{i}What are you thinking, [mc]? This isn't Astylla."
mc "{i}Let's get to Taliya now."
scene darkcave with fade
"You arrive at the ledge again and hop back down. You begin traversing the dark cave until once again you reach the chamber, this time you won't let them get you."
mc "{i}Alright [mc], we find Taliya and we get out as quickly as possible."
"It's amazing how your body has already stopped feeling weak. Every step you take is as firm as it can be and your eyes have gotten used to the darkness already."
"No, it's not just that... Your whole body feels different, almost lighter than usual. Earlier too... It wasn't pain, it was a different sensation... The same you have after moving your body in a way you're not used to."
"After a minute you've already found the cave and are traversing it. You put a hand on the grip of your sword and get ready. That's when you hear a few voices in the distance."
"Cultist 1" "I wish Lawsen didn't have to die for that."
"Cultist 2" "We needed to be sure she was as strong as the stories tell."
"Cultist 1" "I know, but as the first to ascend he deserved better."
play music battlemusic1
"You unsheath your sword and charge forward. They see you, but they don't have enough time to react that you've cut through both of their bodies. They fall to the ground with pipes in their hands, a red mist comes from them. You cough."
"And then you notice they weren't alone."
"Cultist 3" "HE'S BACK!"
mc "{i}Fuck."
"The one you couldn't kill starts running away, but you quickly catch up to him and stab him in the back."
scene cavechamber with dissolve
"And there you are, in the chamber again. You see all the cultists with weapons in their hand, red mist in the air... they were probably taking codayn. This time you won't let them poison you."
scene mcrage with vpunch
mc "WHERE IS SHE?!"
"You charge forward, the cultists charge at you. Maleik is nowhere to be seen."
scene cavechamber with dissolve
"Cultist" "She'll be with us shortly."
"Your grip on the sword tightens. You need to be fast."
"Your sword cuts through one of the cultists' chest, then another."
mc "{i}This is..."
"You stab a third one and they fall to the ground."
mc "{i}...Much easier than before."
"One of them manages to knock your sword out of your hand. It's too far to get it back, but it's only now that you notice a weird red aura around your body."
mc "{i}What..."
"The cultists attack you once again, but even without your sword you somehow hold your ground. Then an opening presents, and you reach in for one of the cultists' weapon. You grab their arm and twist it. You hear a loud crack but they don't let go of their weapon as they fall to the ground."
mc "{i}Perfect."
"Only six cultists are still standing, and they seem nervous, but they still come at you."
mc "C'mon guys, show me more of your demonic strength."
"You punch one in the face, knocking them unconscious... No, you heard a crack."
"Another one attacks you but you easily avoid it and punch then back in the face. They cough blood and fall to the ground."
mc "What..."
"Another one lounges at you, but you simply grab their weapon with one hand and toss it to the side. Their eyes widen as you headbutt them in the face, sending them flying straight to the ground."
"The three remaining cultists are staring at you as if they were looking at a monster."
"Cultist" "H-His eyes! Th-That aura!"
"Cultist 2" "H-He's ascending! Run!"
"They all drop their weapons and immediately start running away. You feel like following them, but you can't: Taliya is why you're here for."
"Cultist" "...Don't you see what's happening?"
scene demoncultist1 with fade
mc "{i}Maleik...? No, it's not him."
mc "Where is she."
"You start walking towards him."
"Cultist" "Your body is responding wonderfully to the drug, don't you feel the powACK-"
scene cavechamber with hpunch
"You grab him by the neck and lift him off the ground."
mc "Where. Is. She."
"Cultist" "D-Doesn't it feel great t-to be a Demon?"
"It does, you think to yourself. You're feeling so powerful right now, but you won't let him know that. You're here for Taliya."
"You tighten your grip, his face is starting to get red. He tries to say something but he can't manage, so he simply points with his finger in a direction."
mc "Thanks."
"You quickly tighten your grip until you snap his neck and only then you let him go. He falls to the ground lifeless."
"You run where Maleik said Taliya is and there you find her, strapped to a chair with a mask on. She looks weak."
scene taliyadrugedchair with fade
pause 1
"As you untie her you see your hands... They're covered in blood and the aura you thought you saw earlier is gone."
t "[mc]...?"
mc "Taliya, it's me."
"You remove her mask and then offer her your least-bloody hand to get up."
scene taliyadruged
mc "We need to get out, can you walk?"
"She tries to stand, but you notice she's still to weak. She's probably inhaled much more gas than you."
mc "Alright, it's fine, I'll carry you."
t "N-No, just help me walk."
mc "..."
"You let her put her arm around your shoulders"
mc "Wait, let me get your stuff first at least."
"You let her sit down again and then look for her clothes and, most importantly, her crystal. Fortunately they're all still there, on a table."
mc "{i}There was no need to take off her clothes, was there?"
scene cavechamber with fade
"You go back to her and help her dress up again, then the two of you slowly walk out of there. Taliya is still in a state of confusion, but she's slowly regaining her senses. As you walk past the first two cultists you killed she looks at you."
t "[mc]...? D-Did you..."
mc "Yes."
"You aren't sure if she's astonished or disgusted."
scene darkcave with fade
stop music fadeout 4
"When you arrive at the ladder you tell her to cling on to you and even though at the beginning she refuses, after trying to climb for herself and failing, she accepts."
scene slums1 with fade
"You climb out of the Dump, like Twig called it, and start making your way back up. You'll come get Twig as soon as Taliya has regained her strength."
"The guards you met on your way down snicker seeing you going back up."
"Guard 1" "Found what you were looking for? Hahah! We're still up if she wants to lend us a hand!"
"You stare at them dead in the eyes."
"Guard 1" "...Sheesh man, I was just joking."
"You walk for a while with Taliya still leaning into you, but after an hour of slowly walking your way up, she's finally able to at least walk on her own. Every once and then she trips on her own foot, but she manages to catch herself."
"Finally you reach an inn. You buy a room and get in with her. She sits on the bed."
$ money -= 10
scene karnakinnroom with fade
show tal sad
show prot sad
mc "...How are you feeling?"
t "Ngh... I'm fine..."
mc "It doesn't look like it. What did they do to you?"
t "They... straped me onto that thing and... pumped some kind of gas into me. I don't know what it was but it felt horrible- Mnh..."
"She touches her forehead as if to hold her head together."
mc "Taliya?"
"You sit beside her."
t "I'm fine..."
mc "You're not."
t "...So this is how it feels, ay?"
mc "What?"
t "Getting saved."
mc "Probably."
t "I don't remember the last time I needed to be saved... God, my body feels so weak..."
mc "I told you I'd come back for you."
show tal smile
t "Yeah... Thank you, [mc]."
mc "It's nothing. After all we're friends, aren't we?"
t "Hah, you're right... Though usually I'm the one who saves people."
mc "Sometimes a change of pace is good."
t "Yeah... Being saved feels nice..."
"She leans onto you, but you're not sure if it's on purpose or because she's still weak."
t "I think... I need to lay down a bit."
mc "Alright."
"You get up and she lays down on her bed. She seems to quickly fall asleep."
mc "I hope she's alright..."
"And so you also go to bed."
scene black with fade
"..."
"..."
"Suddenly you feel something climbing on top of you. You open your eyes and..."
scene taliyagrind0
mc "Taliya, what are you-"
mc "{i}Her eyes..."
t "Mnh... Shhh...."
"She kisses you."
mc "Wh-"
"She forces her tongue inside your mouth and makes out with you, but you're still too in shock to move. No, it's not just that. Her eyes aren't of her usual color... They're red."
mc "{i}These must be the effect of the codayin..."
"She quickly stops the kiss and sits back up while giggling."
scene taliyagrindanim
"She starts grinding on you, going back and fort for a while. She's clearly not into herself."
scene taliyagrindanim with hpunch
pause 5
mc "Taliya you should stop-"
scene taliyagrindanim with hpunch
pause 3
t "No... Why should I~?"
scene taliyagrindanim with hpunch
pause 5
mc "{i}This is {b}definitely{/b} because of those drugs..."
scene taliyagrindanim with flash
pause 4
t "This feels so good baby..."
scene taliyagrindanim with vpunch
pause 5
scene taliyagrindanim with vpunch
pause 1
scene taliyagrindanim with vpunch
pause 0.5
scene taliyagrindanim with vpunch
pause 0.1
scene taliyagrind5 with flash
pause 0.5
"She lets out one loud moan and then you feel something wet... She just came."
t "Give it to me, [mc]..."
menu:
    "Stop her":
        mc "{i}I can't take advantage of her in a situation like this..."
        scene innroomceilingnight with fade
        "You sit up and grab her by her shoulders. Her body feels really hot, literally."
        mc "Taliya, stop."
        t "Mnh... No... I want to keep going... You're so nice..."
        mc "Taliya."
        "She leans into you and keeps mumbling. You feel her hands on your body... She's craving for you."
        mc "That's it, Taliya, stop."
        "Her mumbles grow quieter and then her hands stop moving."
        mc "Taliya?"
    "Let her keep going":
        mc "If that's what you want..."
        t "Yay~"
        scene innroomceilingnight with fade
        "She goes down on your body, putting her face on your crotch. She giggles."
        t "Eheh... heh... It smells funny..."
        mc "{i}I wonder why."
        t "You're so nice, [mc]... and gentle..."
        mc "{i}Now she's just rambling."
        t "And so strong... yeah...... mh......"
        t "..."
        mc "...Taliya?"
"..."
mc "{i}Did she just fall asleep?"
mc "Sigh."
"You grab her and take her back to her bed, putting a sheet on her. As you walk back to your bed though, you realize the line of clothes thrown on the ground between the two beds: First her shirt next to her bed, then her belt, her pants, her boots... then her panties next to your bed."
mc "{i}Taliya would never act like this... It's definitely because of what they did to her. She wasn't feeling good at all."
"You realize you should probably hide the incriminating evidence and put everything next to her bed, folded tightly on a chair, and then you go back to sleep."
scene black with fade
"The next morning she wakes up as if nothing had happened."
scene karnakinnroom with fade
show prot normal
show tal normal
mc "Are you feeling better?"
t "Mh... A bit... My head still hurts a lot."
mc "{i}She doesn't remember, huh? ...She was probably delirious after all."
t "Now that we've verified what's going on in here, I will be able to justify bringing troops with me. Even if Karnak protested they can't do anything to stop us, they know under what conditions we let them exist.."
mc "Alright, seems reasonable. Will I still be allowed to come?"
t "...I'll sneak you in if the King doesn't let me bring you."
mc "The King?"
t "Who do you think my superior is?"
mc "Right, you're a general."
t "You forgot that?"
mc "Shut up."
t "Hahahah. Good job recruit. If you forget the rank of your superior in the army you end up in a lot of trouble, you know, right?"
mc "I said shut up."
t "Alright, alright, let's go now. I want to be back as soon as possible."
if twigRescue == True:
    mc "Wait!"
    t "What?"
    mc "I need to get Twig."
    t "Who's that?"
    mc "Remember the girl you saw last time?"
    t "[mc]. No. You aren't going to heroically save a slave. We'll get in trouble."
    mc "She's the one who saved me yesterday! We'd both be dead if it weren't for her. I owe her."
    t "Well you might owe her, but somebody {b}owns{/b} her. We can't just skip the law of this place like that."
    mc "We did just yesterday."
    t "With money. Do you have the money to buy her?"
    window hide
    show text "{color=#fff}In the current version of the game, Twig can't be saved." at truecenter
    pause 3
    hide text with dissolve
    show text "{color=#fff}Make a save here if you wish to save her in the future." at truecenter
    pause 3
    hide text with dissolve
    mc "...Maybe?"
    if money < 100:
        t "I'm sorry, [mc]. We don't have the money right now."
        mc "But I-"
    else:
        t "Right. You brought over a hundred coins with you."
        mc "Is that enough?"
        t "It depends. Can you describe her?"
        mc "She's a young girl, shorter than me, with black hair, green eyes, olive skin-"
        t "Oh."
        mc "What?"
        t "...Did you see her master? Do you know what's her job?"
        mc "I don't know her job, when I met her she was attending her master — a fat bastard — in the same bath house we went to."
        t "...How many coins did you say you have, again?"
        mc "I've got [money] with me."
        ### For the future. If the MC has 400 or more gold, Twig can be saved.
        t "I'm sorry, [mc]. She's the kind of slave that can costs many hundreds of coins."
        mc "Damn it."
    t "I get it. When we come back I'll bring enough money to buy her."
    mc "Really...?"
    t "If she really saved you then I owe her as much as I owe you. I'll buy her and we'll free her once in Astylla."
    mc "Thank you."
    t "Thank yourself, [mc]. And then we'll both thank her when we come back."
    mc "Alright, let's go then."
scene black with fade
"The two of you leave on a wagon again and reach Randel after two days, it's the middle of the night when you get down from the wagon at the town's square."
scene villageback with dissolve
show tal normal
show prot normal
t "I'll send a missive to the King with all the details tomorrow morning. An answer should arrive in two days, come here in the morning then."
mc "Alright."
t "See you, [mc]."
mc "See you Taliya."
$ time = 2
$ day += 6
$ TaliyaQ = 5
$ dayTQ5 = day+2
$ persistent.Taliya4 = True
jump home



label TaliyaQ5:
hide screen screenmap
hide screen hud
stop music
stop sound
play music market
"You arrive at the market in the early morning. The sun is still rising and you see Taliya along with about a hundred soldiers. Behind them there's eleven wagons."
t "Goodmorning, [mc]."
mc "Goodmorning, general."
t "You can call me Taliya, don't worry."
mc "I can?"
t "Yeah, you're a friend I've invited, not one of my subordinates."
mc "Are you really sure? I feel like we're gonna get some awkward stares..."
t "They won't. They're my subordinates and they respect me enough not to do that."
mc "If you say so."
"Taliya turns around and faces her troops."
t "{size=+3}TIME TO GO! Everybody get on your wagon, we're leaving!"
mc "{i}She knows how to scream, huh..."
t "You can come on my wagon, there's space."
mc "Alright."
if twigRescue == True:
    mc "Ah, did you remember to..."
    t "Yes, I've got it with me."
    mc "Good."
"The two of you walk up to the wagon in the front. As you get up you realize there's a few more soldiers in there. Taliya introduces you to them. They seem friendly but they're still very formal and you don't feel that comfortable."
stop music fadeout 2
scene black with fade
"The wagons depart, and once again you go through the same journey you've already been two times before. You can almost recite all the town from Randel to Karnak by memory: Ashterbur, Gilles, Barew, Scetyrm-"
t "[mc]?"
scene taliyacart1 with dissolve
"You suddenly awake. It's daytime and you can see that you're already in front of the door to Karnak."
mc "Y-Yeah?"
t "We're going in."
mc "I thought we'd have to wait much more."
t "We won't. They know what we're here for and they're letting us through first."
mc "Oh, that's good."
t "We'll leave half of the company outside to make sure nobody escapes."
mc "Seems good."
play music market
scene karnakspire with fade
"Half of the wagons go in. When everyone gets down you can almost feel the tension in the air in the main square. It's usually a lot more lively but now it almost feels like a fight is going to break out at any moment. All of you begin heading towards the cave."
mc "{size=-2}They're all looking at us..."
t "They're not really that fond of Astylla."
mc "...Yeah but-"
t "There's fifty of our men guarding the entry of the city, and another 50 inside. It's normal, don't worry. It's actually already really nice that they let us in with no problem."
mc "I guess you're right."
scene karnakinterior with fade
"You keep descending through the city with the men behind you until you finally reach the entrance of the last floor. There's even more guards than last time."
"Guard Captain" "You! I remember you!"
t "Of course you do. Now move. We've been authorized to enter this floor."
"The guards stand there for a second, but then they move out of the way, a few spit on the floor."
"Guard Captain" "Filthy Astyllians... First you sneak past us, and now you bring your whole army along? Arrogance and Astylla can't seem to not go together."
t "There's no need to comment."
"Guard Captain" "This is Karnak, feel lucky you're being let pass after the mess you did last time. When slaves start disappearing it's us who get in trouble."
t "Slaves? Disappear?"
"Guard Captain" "What? You didn't know? The day after you came around slaves started disappearing. We've counted at least a hundred."
mc "{i}...Twig."
t "Damn it, I should've known this would happen."
scene karnakinterior with vpunch
t "Everybody! Hurry up! We need to get down there as quickly as possible!"
"Everybody quickly starts marching again, faster than before, and so you quickly reach the ledge. Some soldiers take out lamps and light them, then you all climb down."
play music creepymusic
scene darkcave with fade
"With the lamps, it's suddenly much, much easier to move through the Dump. You make your way through the cave and when you arrive to the chamber, nobody is there to be seen... At least not anyone alive."
scene cavechamber with fade
"Unlike last time, the chamber is filled with cages and inside each of them... dead slaves, all of them disfigured and at least partially mutated."
t "...Fuck."
mc "These are the slaves, aren't they?"
t "They are."
mc "And they're all right here..."
t "They're property that can be replaced with enough money... they probably didn't even bother looking for them."
mc "This is making me sick..."
"You mean it both figuratively and literally. You still haven't gotten as used as all the soldiers around you to seeing these kinds of gruesome spectacles."
t "Now we know how they tested their shit."
"The unit moves forward towards the dark side of the chamber. On the way there you start seeing more tools and equipment, most definitely used to turn people into demons. Then everyone starts smelling something foul."
mc "God... What is this smell..."
t "..."
t "Unfortunately, I think I know. Scottie, Basche, make some light."
"Two men move in front of you, their lanterns raised."
"Slowly a mount of dead bodies piled on top of each other is revealed. Most of them aren't fully human anymore, but it's clear the transformation process killed them... and it must've been very painful too."
mc "I'm going to puke-"
"You vomit on the floor, Taliya puts a hand on your back to comfort you, but you can feel from her touch she's upset too."
"Soldier" "Fucking monsters..."
t "They must've tried to turn as many people as possible into demons before leaving... There's at least a hundred dead people in here."
"Soldier" "They're all..."
t "Mid transformation. They failed each and every attempt... And they still kept going."
"You move away from that horrible view, but as soon as you turn around, in a corner, you see something else."
stop music
"No, not something, it's someone. It's..."
scene twigdeath with fade
pause 3
mc "T-Twig!"
"You run up to her corpse."
play music desolation
mc "Fuck- Twig!"
"You shake her as if that could bring her back to life."
mc "Twig!"
"You fall to your knees."
"Taliya slowly walks up to you and puts a hand on your shoulder.."
t "...She's gone, [mc]."
mc "B-But why... Why her..."
"You start sobbing."
if twigRescue == False:
    t "You knew her?"
    mc "Yes... S-She... She didn't deserve any of this..."
    "Your sobs quietly turn into tears as Taliya kneels down next to you."
    t "I'm sorry, [mc]. We'll find the bastards who did this."
else:
    t "They couldn't have known she helped you, [mc]. Don't feel responsible"
    mc "S-She... She didn't deserve any of this..."
    "Your sobs quietly turn into tears as Taliya kneels down next to you."
    t "She got unlucky."
    mc "{i}...Wasn't being born a slave unlucky enough?"
    t "Don't worry, [mc]. We'll avenge her when we find those bastards."
mc "..."
t "You should head back, now."
mc "No, It's... I'm alright."
t "I'm not asking, this is an order. Get out of here and wait us above the ledge."
mc "Huh?"
"She glares at you."
mc "Fine."
t "Good."
scene cavechamber with fade
"The two of you get up, and as you walk away from the cave, you hear Taliya shouting orders."
t "{size=+1}Search everything. And I mean EVERYTHING. Boxes, barrells, sacks, bodies, even rocks!"
scene darkcave with fade
pause 1
scene karnakinterior with fade
"You climb up the ladder and then you sit on the ledge, looking down."
mc "{i}I could've done something..."
mc "..."
mc "{i}But what...? How could've I saved her..."
"You stare into the nothingness for what feels like an infinity, the shock of everything you just saw catching up to you along with guilt."
"Then, you see Taliya and her soldier pop up from below with their lamps and they begin to climb. Taliya is the first to reach you."
t "We're done, we're going back up."
mc "Yeah, let's."
"You all head back up to the ground floor and reunite with the other half of the company. It seems they didn't see anyone suspicious leaving the town. It seems the cultists had left before you even arrived."
t "If only I could've been quicker..."
"Soldier" "We couldn't have been faster, general."
t "...Sigh."
scene innlowerfloor with fade
"You then head to an inn with enough room for the whole company and rent it for the night. All soldiers sleep in rooms together except for you and Taliya, who both have your own room."
"Soon enough the soldiers begin drinking, the whole company gets drunk, yet you don't really feel like drinking... It's not the time to party. Not after that."
"You look around and see Taliya. She's talking with a few of her troops, so you decide to leave her alone and just leave. You walk up to your room and sit on your bed. You can still hear them singing and dancing from below, but at least now it's much more muffled."
scene karnakinnroom with fade
show prot surprised
"You sigh. You really hoped you could get Maleik and the few others that escaped you last time."
"You stare at the ceiling for an hour before you hear the door creaking open. You raise your head and see Taliya poking in through the door."
t "Hey."
mc "Hey."
"She walks in the room and closes the door behind herself."
t "I didn't see you leave. What are you doing up here?"
mc "I just don't feel like partying."
t "......"
show taliyamctalk1 with dissolve
"Taliya sits next to you."
t  "...How are you?"
mc "Oh, I am completely fine after seeing dozens of disfigured corpses piled up, why ask?"
t "..."
mc "How can you fool around as if that didn't happen..."
t "[mc]..."
t "We're soldiers. This kind of things aren't new to us... If they were always sober they'd all feel much worse than you."
mc "Is it that bad out there?"
t "Yes. Outside the walls that protect Astylla this is the norm."
mc "..."
mc "...So that's what it means when we say demons are pure evil, isn't it?"
t "Yes. Engrain that into your brain, this is what we're fighting against. Humanity isn't just about our race... It's about morality."
mc "..."
if twigRescue == False:
    t "That girl, who... was she?"
    mc "She's the slave girl I fed the first time we came here... She even helped me after I passed out when I escaped the cult..."
    t "Oh... I'm sorry [mc]."
    mc "What's done is done... there's no bringing her back now."
else:
    t "I'm really sorry for what happened to Twig."
    mc "..."
    t "If I hadn't gave away my money maybe I could've bought her back than, I'm-"
    mc "Don't be. We... couldn't have known."
t "If only I found them earlier, this wouldn't have happened. I'm sorry, [mc]."
mc "What? No, how is it your fault?. If it wasn't for you they'd kept experimenting on people, they'd have kept making and distributing drugs, they- Who knows how many people you've saved."
t "...Thanks, [mc]."
scene taliyamctalk2
t "Though, well, I couldn't have done it without my trusty sidekick."
mc "What? I barely did anything."
t "Right. Barely anything."
t "[mc], if you hadn't saved me back there I would've turned into... a monster. I'm here because of you."
mc "..."
t "Not a lot people get to hear that from me, you know? You should feel proud."
mc "Heh."
t "..."
scene taliyamctalk1
t "You still look kinda down, you sure you don't want to come down?"
mc "Uhm, no thanks. I'll stay here."
t "Is there anything I could do to help you feel better?"
mc "Taliya, really. I'll just go to sleep."
t "Ok."
scene taliyamctalk3
"She gives you a kiss on the cheek."
mc "{i}What-"
t "Hope that helped a bit."
t "Good night, [mc]."
"You're so shocked that you only manage to reply once she's already left the room."
scene karnakinnroom with fade
mc "G-Good night!"
mc "...I guess in the end I got my reward."
"You go to sleep."
scene black with fade
"The next morning you all leave and head back to Randel. The way back is really boring, and neither you or Taliya mention the kiss."
mc "{i}Not that it was anything that incredible... It was just a kiss on the cheek."
mc "{i}But..."
"You hadn't seen Taliya around her comrades before these last few days. She is friendly with them, but it's clear she's just being a good boss. She treats you much differently, even before you saved her."
mc "{i}Maybe she..."
mc "{i}No, just because we're friends doesn't mean she likes me. She's like twice my age..."
scene karnak with fade
pause 1
scene forrest with fade
pause 1
scene villageback with fade
show prot normal
"And so, after the usual three days of travel, you arrive at Randel again. Taliya gives a short speech to her troops and then they go off. You expected her to leave as well, but she stays there."
show tal normal
"She turns towards you."
t "I expect to see you at the Academy, recruit."
mc "I'll be there, general."
t "Heh, see ya, [mc]."
mc "See ya."
"And then she leaves as well."
hide tal normal with easeoutleft
mc "{i}She really opened up hasn't she?"
mc "{i}I'm glad."
$ TaliyaQ = 6
$ TimerT6 = day+4
$ day += 7
$ time = 1
$ persistent.Taliya5 = True
jump home

label TaliyaQ6Pre:
hide screen screenmap
hide screen hud
"When you arrive at the Academy's arena, you see Taliya. She waves at you to come and so you walk up to her."
show prot smile
show tal smile
t "Hey there, [mc]."
mc "Should we really use our names even here?"
t "Do you really think word about you coming along with me hasn't spread around?"
mc "It did?"
t "Yeah. It's better to show we're just friends than ignore it or even weirder rumors will spread."
mc "I guess you're right."
mc "So, was there anything you wanted to tell me or was it just that?"
t "No, there's something else too. We're holding a party at the barracks and I thought it'd be nice to invite you."
mc "Really? Why?"
t "What do you mean why?"
mc "I'm not really a soldier or anything."
t "First of all, you're a recruit and that counts. Second of all, and most importantly, we're partners aren't we?"
mc "Yeah, I guess you're right... I just hope I won't stick out like a sore thumb."
t "Hah, don't worry about it."
mc "What's the occasion, by the way?"
t "Oh, right, uhm... It's a farewell party."
mc "For whom?"
t "Me."
show prot question
mc "What?"
t "Yeah... Things are getting hectic at Hern and the King has ordered me to go and help manage the situation."
show prot sad
mc "Oh."
mc "...When will you be leaving?"
t "In a few days. I need to settle everything I've got pending... Then I'll leave."
mc "...I see."
show tal smirk
t "Y'know, it's kind of obvious you're sad. You can say it."
show prot questiont
mc "Wh-What? Hahaha, no, no at all..."
t "You'll miss me, won't you?"
mc "As if I'd ever miss such a grumpy general..."
t "..."
t "So, what do you say then, one last duel before I leave?"
mc "You're on."
t "No blind fold this time, let's see how much you've improved."
scene taliyaminigame3
$ fightMiniGame = "a23456789087654"
$ fmgd = 4/(swordlvl/25)
if fmgd < 1:
    $ fmgd = 1
jump start_fightMiniGame
label a23456789087654:
if randel_fails < 4 and swordlvl > 18:
    "It's only been about a month since you started, but you've improved a lot. You've seen Taliya fight for real during your time with her and you can sense her fighting you more seriously now than she did the first time."
    t "You know, [mc]."
    menu:
        "Stay focused":
            "You ignore her and keep fighting. Even if she's not trying to kill you and you're in the best shape you've been so far, it's still really hard to keep up with her."
            t "It's honestly amazing how quickly you've learned to fight like this. Saying you're a natural is..."
            "She steps in and thrusts her sword towards you."
            $ qtesection = "taliyaQTE1"
            call screen qte1
            label gitGudIdiot:
                "You don't manage to avoid her hit in time and she hits you in your chest. You tumble to the ground."
                t "...an understatement. Who knows, maybe you actually have the talent to surpass me in a few years."
                mc "Yeah, in a few years."
                t "I'm twice your age, [mc], that's still pretty good."
                mc "I guess you're right."
            label taliyaQTE1:
                "You manage to duck in time and you try to attack her back now that she's exposed. Her eyes widen as she sees your sword coming towards her, but then she smiles and manages to really quickly take a few steps back before you can reach her."
                t "...an understatement, indeed. It seems you've learned how to avoid that."
                mc "I did."
                "The two of you now stand a few feet apart, out of reach from each other."
                t "But will you be able to do it twice?"
                mc "Will you?"
                "Taliya giggles."
                t "I might not if I don't get serious."
                mc "Then what are you wa-"
                # For the future. I want a CG here.
                "You can't even finish the sentence that Taliya dashes towards you at a speed you didn't know she was capable of and she lightly taps your chin with the hilt of her sword. She's now standing only a few inches away from you."
                t "I was waiting for you to get distracted."
                "You can see she's sweating a bit, and her breath is heavier than usual. Ignoring how hot she looks like that, it's clear that {b}that{/b} was her getting serious."
                mc "Well, you got me."
                "Taliya finally moves away from you."
                t "If I didn't, I'd have resigned this evening."
                mc "Heh."
                t "By the way..."
        "Answer":
            mc "What?"
            t "It's honestly amazing how quickly you've learned to fight like this. Saying you're a natural is..."
            mc "...is? What is-"
            "You don't get time to finish your sentence that she has dashed towards you and hit you with the tip of her sword right on your stomach."
            t "...an understatement. Yet, you should probably focus more on fighting or those skills will go to waste."
            mc "You're the one who started talking."
            t "I'm also your general, your teacher, and one of the strongest people you know."
            mc "Sigh..."
            t "Don't be sad. You're good enough to become just as strong as I am in a few years."
            mc "Yeah, in a few years."
            t "I'm twice your age, [mc], that's still pretty good."
            mc "Yeah, I guess you're right."
elif randel_fails < 4:
    $ renpy.notify ("{color=#fff}Sword skill check: {color=#A50000}Fail. ([swordlvl] < 19)")
    "You are doing much better than last time, but you still aren't hitting her... She's too strong."
    t "Not bad."
    "Taliya takes a step closer and hits you right in the chest."
    t "But it can still improve."
    mc "Ow..."
    "She lends you her hand."
    t "You'll go far, you've learned a lot in so little time."
    mc "Not today, clearly."
    t "Eventually."
else:
    "You try as hard as you can, but... She takes a step closer and hits you right in the chest."
    t "A bit sloppy today, aren't we?"
    mc "That is definitely not the only reason I lost."
    t "Hahah, you're right. I'm quite good myself."
$ randel_fails = 0
scene arena with fade
show tal normal
show prot normal
"Taliya suddenly looks down. Her eyes fixed on your sword as if she has only now noticed something."
t "Your sword... Can I look at it?"
mc "Uhm... yeah?"
"You hand her the sword Uncle Pete gifted you and she inspects it."
t "Where did you get this sword from?"
mc "My uncle gave it to me."
t "Your uncle?"
mc "Yes."
t "How did he manage to get it?"
mc "He used to be a travelling merchant; he said someone sold it to him."
t "...Unbelievable."
show prot question
mc "What's so special about the sword?"
t "...You see the symbol here?"
"She points at the symbol engraved at the hilt of the sword."
t "It's the symbol of the Maryas."
mc "As in, {b}the{/b} Maryas?"
t "Yeah. If this isn't a fake... It could be the very same blade that slayed the Demon King."
mc "You mean it could've been Gladius Hans'?"
t "Well, either his, or of one of the other Maryas. Y'know, Rina, Ulof, and Scar."
mc "I doubt it was Scar's."
t "Hey! Mages have swords too... Sometimes."
mc "Yeah, yeah."
"Taliya hands you the sword."
t "Keep it. I'll see if I can spare some time to talk to your uncle before I leave."
t "Where does he live?"
mc "In the fish hut by the lake."
t "Alright, thank you [mc]. Now go back to training."
mc "I will."
$ Taliya6Talk = True
jump arenar



label TaliyaQ6:
hide screen screenmap
hide screen hud
scene villagen with fade
mc "Here we are. Now let's head to the barracks."
"You keep walking from the guild and soon enough you reach the barracks. As a matter of fact you realize just know how close they are. It's barely a five-minute trip."
"When you arrive you see Taliya outside. She waves at you and you walk up to her."
t "You finally arrived."
mc "...I'm not late, am I?"
t "You're not, don't worry, they just started partying. Come on in."
play music taverndance
scene taliyaq6party with fade
"The two of you walk inside and you finally see the barracks from inside for the first time in your life. It looks really lively with all the people there enjoying the banquet."
"You assume that usually it's not like this... after all this is a farewell party for their general."
scene taliyaq6party with hpunch
show prot normal
show tal normalr
"Someone bumps into you."
show prot question
mc "Hey-"
t "Leave them, once you give them alcohol, they're not-"
"The person you bumped into turns around. You've seen them before..."
image  tsadflip = im.Flip("taliya/tsad.webp", horizontal=True)
hide tal normalr
show tsadflip
show normalwatr with easeinleft
tr "Oh, sorry, didn't see you there."
t "..."
tr "What?"
t "What are you doing here?"
tr "The door was open."
t "Ugh..."
mc "You two know each other?"
t "Unfortunately."
tr "Of course we do."
mc "How?"
t "Please don't."
tr "Don't mind her. She's just a wee bit shy. I was actually her first instructor."
mc "What?"
tr "Yuh-huh. The Demon Lord hadn't been slain yet and I was still in the army when she came to the Capital."
mc "You were in the army?"
tr "Aren't you?"
mc "...Huh?"
tr "Oh c'mon, didn't you read the contract you had to sign to become an adventurer?"
mc "Well, actually, not really...? I kinda just signed it without thinking about it."
tr "..."
t "..."
tr "Well, the Adventurers' Guild is part of the army, we're just more special. We get to do whatever the hell we want unless there's a big crisis and the King decides to call us all in."
mc "Ah, I see."
tr "Our adventurer ranks actually have their equivalent in the army. As a Diamond-rank Adventurer, I'm actually a Commander by default, though I actually became a major during the war."
mc "I see... and what's that got to do with Taliya?"
tr "They liked me so much they decided to give me the job to instruct new recruits..."
"She looks at Taliya and smirks."
tr "...Guess who had just enrolled in the army?"
t "Please don't remind me."
tr "Oh I could tell you so many stories, lad, but the look in her eyes tells me she'd beat me up if I tried."
mc "Hahah... Hah..."
"The three of you go silent."
tr "Well, it was a pleasure having you here Taliya. I'll go back to drinking now. See ya after!"
hide normalwatr with easeoutright
hide tsadflip
show tal sad
show prot smirkt
t "Sigh..."
mc "Why you looking so tense? Were you really that bad?"
t "What do you think?"
mc "{i}Oh right... She was an orphan and a criminal before getting into the army. Heh, must've been a little pest then."
mc "Right, right."
scene taliyaq6party with dissolve
"The two of you keep wandering around the party, drinking and eating in the mean time. At one point music starts and everyone starts dancing, but Taliya seems unwilling to join everyone else, so you also don't."
"After a while some people start getting tired and sit down. A few of them sit next to the two of you and ask you about how you met and what you did together on your missions."
"You feel a bit awkward having all these questions aimed at you, but Taliya helps you out answering for you when you don't know how."
"Somehow even when drunk they seem to respect Taliya a lot, not even one of them makes a weird remark towards her. She, on the other hand, remembers the name of each and every one of them."
mc "{i}She really is a model general."
"Then, when she seems to be finally sick of all the questions, she grabs a cup and slams it on the table."
t "Alright folks! Which one of you wants to try outdrink me?"
"Soldier 1" "Not me!"
"Soldier 2" "General, we all already know you can drink us under the table!"
t "I'll accept multiple matches! Come on who wants to go first!"
"Suddenly a soldier nudges you."
scene drinkgame with fade
"Soldier 3" "Why don't we give [mc] a go? He's the only one here who hasn't had the chance to challenge her before!"
"Soldier 1" "Hell yeah!"
mc "W-Wait! Me? No way! I can't-"
"Multiple Soldiers" "[mc]! [mc]! [mc]! [mc]!"
"Soldier" "Come on [mc]! We're rooting for ya!"
t "So, [mc], what do you say?"
t "It's ok if you're too scared, I get it, you're a kid after all..."
mc "A kid? Alright, alright, I see how this is. I accept."
"Taliya smiles."
t "Alright, then! Bring us as much beer as you can! These mugs will be empty soon!"
"Soldiers" "Cheers!"
"You and Taliya begin drinking. She had already drunk more than you before the match even started but she's handling it like a champ. Better than you at least."
t "C'mon, [mc]! You're already all red! Hahaha!"
mc "It's... my tenth drink..."
"The two of you keep going another while, but she's already ahead of you. On the 14th mug you can feel yourself getting ready to puke."
mc "I... give up..."
t "I won! Hahah! Who's next?"
"Everyone cheers and a few soldiers grab you and lift you up above the crowd."
scene taliyaparty
tr "I want to go next!"
t "What?!"
"You hear Taliya's voice fading as you are thrown around farther from her."
"The party goes on for a few more hours into the night, you find out that Triss apparently won the drinking contest while you're left sitting on a table."
"You see Taliya going around and having fun, and in the end the alcohol gets the best of you and you pass out."
scene black with dissolve
stop music
pause 1
"Someone shakes you."
"{color=#C64745}???" "Dad...?"
scene black
pause 1
"{color=#C64745}???" "You need to rest, don't go..."
mc "{i}Huh...?"
scene black
pause 1
"{color=#C64745}???" "Mhh..."
scene black
pause 0.7
"{color=#DD8E8B}???" "Mh~"
"You feel a chill through your nether regions."
"{color=#DD8E8B}???" "So big..."
scene taliyaq6party with flash
"You suddenly open your eyes and straighten up. You're sitting on one of the benches in front of the tables of the barracks' dining hall, but you're still feeling something weird... Something warm and wet..."
scene taliyablowjob with vpunch
pause 3
mc "WH-WHAT!?"
"When you look down, you see Taliya sucking you off. Her cheeks are flushing red, she is... definitely really drunk."
"She looks up at you innocently, but you aren't liking how this is going, so quickly get up."
scene taliyaq6party with vpunch
show tal normal
show prot angry
mc @angryt "What the hell are you doing?"
t @sadt "...Sucking you of?"
show tal sad
mc "..."
show prot normal
mc @talk "You're drunk, Taliya."
t @smilet "Yeah, and?"
show tal smile
mc @talk "You're not yourself, let's not do anything we might regret tomorrow mor-"
"Taliya walks up to you and puts her fingers on your chests. She moves her head even closer and then she whispers into your ear."
t @smilet "{size=-2}I've wanted to do this for a while."
show prot surprisedb
mc @surprisedt "Y-You're too drunk, Taliya, you're not th-thinking straight."
t @smilet "No, no, [mc]. I only got this drunk for you~"
"You gulp."
t @smilet "I want you to take advantage of me... pin me down and fuck me."
$ persistent.Taliya6 = True
menu:
    "Try to walk away":
        $ good += 1
        show prot angry
        mc @angryt "No, Taliya. I won't do this. Let me go, I'm leaving."
        show tal sad
        t @sadt "No! Don't go..."
        mc @angryt "See you tomorrow."
        "Taliya grabs you by the wrist as you're walking away. You can feel her eagerness just by the way she's holding on to you."
        menu:
            "Walk Away":
                "You slither out of her grasp and quickly make your way outside the barracks. She makes an attempt at following you but she trips halfway."
                scene villagen with fade
                "Once outside you breathe a sigh of relief."
                mc "{i}What the hell got into her? Could these be the lasting effects of the drug? God, I hope not."
                mc "{i}Whatever that was, I did the right thing. She was clearly out of her mind."
                scene taliyablowjob with flash
                pause 0.5
                scene villagen
                "For a brief moment your mind flashes back to her sucking you off."
                mc "{i}No, [mc]. Bad. Stop thinking about that and let's leave."
                "You start walking towards your home. Even though it's really dark you easily find your way home. It shows you've been living here most of your life."
                scene homenight
                mc "Time to sleep."
                $ time += 1
                $ TaliyaQ = 7
                call sleepvars
                jump home
            "Let her have you":
                "You stop walking, when you turn around you can see her smiling."
                hide tal sad
                show tal smile
                $ persistent.Taliya6fem = True
        t @smilet "There you go, good boy."
        "She walks closer to you, to the point where you can feel her breath. It stinks of alcohol... Though it could also be your own smell."
        t "I'll help you get in the mood... alright?"
        if mcBold == True:
            mc "You're going to start sucking me off again?"
            t "Oh, I've got a better idea~"
        else:
            mc "A-Alright."
        scene taliyaq6party with dissolve
        "Taliya starts taking off your clothes and while she does you realize that you're still in the middle of the dining hall."
        if mcBold == True:
            mc "Are you sure nobody is going to wake up?"
            t "Not if you're nice and quiet~"
        else:
            mc "W-Wait, Taliya, w-what if someone wakes up?"
            t "They won't, don't worry. If you're not relaxed you won't enjoy it~"
        "Once you're fully naked, she starts removing her clothes in front of you. You've already seen her naked, but never {b}undressing{/b}, and now she's doing it in front of you. You can already feel your dick getting hard."
        "She turns around and smiles at you staring at her body."
        t "Like what you see, [mc]?"
        mc "I do."
        t "Would you like to feel it, too?"
        mc "Most definitely."
        t "Perfect."
        "Taliya walks up to you and before you can do anything she turns around and..."
        scene taliyathighjob1 with vpunch
        pause 2
        mc "Wuh-"
        "Your dick twitches between her tight grasp and you hear her let out a satisfied giggle."
        t "I suppose you're already enjoying this?"
        if mcBold == True:
            mc "I am, but please, keep going."
        elif mcNormal == True:
            mc "It feels great."
        else:
            mc "Y-Yeah I am."
        scene taliyathighjob
        show taliyathighjob2
        if mcBold == True:
            t "Alright, big boy. Get ready~"
        else:
            t "Then you'll like what's next even more~"
        hide taliyathighjob2 with hpunch
        play music taliyathighjob
        play sound femalemoan
        pause 3.5
        play sound sexbreath
        mc "Ngh..."
        "Her scent fills your nostril. You had never realized before how good she smells.{w=5}{nw}"
        window hide
        play sound femalemoan
        pause 1
        t "Feels nice?{w=2.5}{nw}"
        mc "Y-Yeah.{w=2.5}{nw}"
        window hide
        pause 1.5
        play sound femalemoan fadein 0.5
        pause 2
        play sound sexbreath
        "Even being so slow, her thighs around your dick are making you feel so good. With each thrust you feel closer to cumming.{w=6}{nw}"
        window hide
        pause 0.5
        play sound femalemoan
        pause 3
        t "How are we holding up? Are we close to cumming?{w=3.5}{nw}"
        mc "N-Not yet...{w=2.5}{nw}"
        window hide
        pause 1
        play sound sexbreath
        pause 1
        play sound femalemoan
        pause 2
        t "You're so hard~ I can't wait to have you inside of me~{w=4}{nw}"
        mc "Then how about you do that already?{w=3.2}{nw}"
        play sound femalelaugh
        t "That would spoil all the fun~{w=4}{nw}"
        window hide
        pause 2
        play sound femalemoan
        pause 1.53
        play sound sexbreath
        pause 2
        t "Wanna see me go faster?{w=3}{nw}"
        stop music fadeout 1
        mc "H-Huh?"
        play sound femalelaugh
        play music taliyathighjob2
        scene taliyathighjobfast with dissolve
        mc "O-Oh d-dear Astylla!"
        play sound femalelaugh
        window hide
        pause 2
        mc "Nh~!"
        window hide
        pause 3
        mc "Ahn~"
        window hide
        if mcBold == True:
            t "I love seeing you squirm like that~"
            mc "And I love your thighs...!"
            t "And I'll make you love the rest~{w=8}{nw}"
        else:
            t "I love seeing you squirm like that~{w=8}{nw}"
        window hide
        pause 2
        mc "T-Taliya...!"
        t "Yes, baby?"
        mc "I-I'm gonna..."
        window hide
        pause 3
        mc "...C-Cum!"
        stop music
        scene taliyathighjobcum1 with vpunch
        t "Cum for me, [mc]~{w=0.5}{nw}"
        play sound femalemoan2
        scene taliyathighjobcum1 with flash
        scene taliyathighjobcum2 with dissolve
        mc "Hah..."
        t "You came so much~"
        mc "Yeah..."
        mc "{i}She made me cum so easily... God she's hot."
        t "Let's see how well you perform on top~"
        mc "W-What?"
        t "Let's go~"
        scene taliyaq6party with dissolve
        "Taliya grabs you by the hand and quickly starts dragging you away somewhere. You don't have time to protest about your clothes being left on the floor of the dining hall."
        scene taliyaroom with fade
        "You follow her through a flight of stairs into a dark room which you assume to be hers. She gets on her bed and shakes her ass at you."
        t "Come get me, big boy~"
        scene taliyasex
        show taliyaroom
        mc "Gladly."
        "You get right behind her on the bed and then grab her by the hair. She gasps, and then, without hesitation, you slide your cock right in."
        hide taliyaroom with fade
        play music taliyathighjob2
        pause 3
        t "Ahh~! Fuck!"
        window hide
        pause 2
        t "You're so good..."
        window hide
        pause 3
        t "Y-You really aren't just a kid, a-are you? Mnh~!"
        mc "Of course I'm not. Who did you take me for?"
        scene taliyasex with vpunch
        pause 5
        t "AH~!"
        window hide
        pause 6
        t "[mc]... I'm gonna..."
        mc "Me too..."
        t "D-Don't do it inside, I can't-"
        mc "I know."
        scene taliyasex with vpunch
        t "Ahn~!"
        scene taliyasex with vpunch
        t "Y-You're so-"
        scene taliyasex with vpunch
        t "FUCK~!"
        scene taliyasex with vpunch
        pause 0.5
        scene taliyasex with flash
        pause 0.2
        stop music
        scene taliyasexanimcumout1 with flash
        pause 0.3
        scene taliyasexanimcumout2 with vpunch
        t "Huff... Huff..."
        "The two of you lie down on the bed next to each other, both extremely tired."
        scene taliyaroom with fade
        t "That was amazing."
        mc "Y-Yeah..."
        if cynthdate > 0:
            mc "{i}Twice in a row... At least Cynthia had her potions..."
        t "..."
    "Top her":
        mc "{i}Fuck it. If this is what she wants then I'll give it to her."
        mc "Fine then."
        scene taliyaq6party with hpunch
        t "Yay~!"
        mc "But not here! Let's go to your room."
        t "You're not gonna do me on the table?"
        mc "I would love to, but if anyone wakes up we're fucked. C'mon lead the way."
        t "Mh... I guess you're right..."
        "She begins walking away. You grab a candle and follow her."
        scene taliyaroom with fade
        "When you arrive at Taliya's room you notice she has already packed her things."
        mc "{i}She really is going away, huh?"
        "Taliya seems too drunk to care... or maybe that's exactly why she brought you here. Is this her way of paying you back before you leave?"
        "You look at her completely undressing herself. You can feel your dick already getting hard."
        "She walks to the bed and removes the heavy brown blanket on top before sitting on the bed and turning towards you."
        t "I'm ready. You, though..."
        "She looks at your pants and grins."
        t "...are just as eager! C'mon get over here!"
        "You don't let her tell you twice. You walk towards her and push her down on the bed.{p}You spread her legs and quickly push your dick inside. You don't even put the candle down."
        scene taliyawax1 with vpunch
        t "F-Fuck! R-Rough aren't we?"
        mc "You know you like it."
        t "Never said I don't~"
        mc "Happy to hear that."
        "You thrust again. Her pussy is the tightest you've ever seen."
        scene taliyawax1 with vpunch
        t "Mh~ It's even bigger than I thought..."
        mc "And you're... so fucking tight!"
        scene taliyawax1 with vpunch
        pause 2
        t "Hey."
        mc "W-What?"
        t "Why don't you put that candle down and put your hands to use on me~?"
        mc "Oh, right-"
        mc "{i}Wait... What if I...."
        show taliyawax1b
        t "W-Wait what are you-"
        mc "Let's try something~"
        "The look she's giving you is a big scared, but you can feel her pussy getting wet."
        t "T-Try wh-"
        "You thrust again and, as you do so, wax drips on her."
        scene taliyawax2 with vpunch
        t "A-Ah~!"
        mc "{i}Wait did she just... orgasm?"
        scene taliyawax2
        show taliyawax2b with dissolve
        pause 2
        t "Y-You're so-Ah~! U-Unfair!"
        mc "Did you just cum?"
        t "M-Maybe..."
        mc "{i}Wow, it only took this much to make her so meek? I ain't stopping now then."
        mc "Then let's make sure you do."
        t "W-What do you me-Ahn~!"
        scene taliyawax3 with vpunch
        pause 1
        scene taliyawax3 with vpunch
        pause 1
        scene taliyawax4 with vpunch
        t "F-Fuck!"
        mc "That's what I'm doing~"
        scene taliyawax4 with vpunch
        pause 1
        scene taliyawax4 with vpunch
        t "G-God I knew this w-was a good idea! Ah~!"
        mc "Shut up already, I only wanna hear moans coming from that mouth!"
        scene taliyawax5 with vpunch
        t "AH~!"
        scene taliyawax5 with vpunch
        pause 1
        scene taliyawax5 with vpunch
        pause 0.5
        scene taliyawax5 with vpunch
        t "Mnh~! Ah!"
        scene taliyawax5 with vpunch
        t "I-I'm g-gonnAh~!"
        mc "Cum? Good."
        scene taliyawax5 with vpunch
        pause 0.5
        mc "{i}I think I'm going to cum too..."
        scene taliyawax5 with vpunch
        pause 0.5
        t "I'm-!"
        mc "C-Cumming!"
        scene taliyawax6 with vpunch
        t "Ahhh~!"
        scene taliyawax6 with vpunch
        t "Ahaha~!{p}Fuck! Mh... Hah~"
        scene taliyawax6
        show taliyawax6b
        pause 3
        t "Astylla be blessed... Hah..."
        mc "Ready for round two?"
        t "R-Round what?"
        scene taliyasex
        show taliyaroom
        "You smirk and quickly turn her over. You put away the candle so quickly the flame goes out, but you can still see even in this dark."
        "You grab Taliya by the hair and before she can protest even once, you thrust inside of her."
        hide taliyaroom with fade
        play music taliyathighjob2
        pause 3
        t "Ahh~! Fuck!"
        window hide
        pause 2
        t "You're so good..."
        window hide
        pause 3
        t "Y-You really aren't just a kid, a-are you? Mnh~!"
        mc "Of course I'm not. Who did you take me for?"
        scene taliyasex with vpunch
        pause 5
        t "AH~!"
        window hide
        pause 6
        t "[mc]... I'm gonna..."
        mc "Me too..."
        t "D-Don't do it inside, I can't-"
        mc "I know."
        scene taliyasex with vpunch
        t "Ahn~!"
        scene taliyasex with vpunch
        t "Y-You're so-"
        scene taliyasex with vpunch
        t "FUCK~!"
        scene taliyasex with vpunch
        pause 0.5
        scene taliyasex with flash
        pause 0.2
        stop music
        scene taliyasexanimcumout1 with flash
        pause 0.3
        scene taliyasexanimcumout2 with vpunch
        t "Huff... Huff..."
        mc "Enjoyed it?"
        t "Enjoyed it? It was fucking amazing."
        mc "Hah. I'm glad."
        t "What about you? Enjoyed your time?"
        mc "Most definitely."
        t "At least you came outside once..."
        mc "Ahhh... Sorry."
        t "Whatever..."
        mc "..."
        "The two of you lie down on the bed next to each other, both extremely tired."
        scene taliyaroom with fade
        t "That was amazing."
        mc "Y-Yeah..."
        if cynthdate > 0:
            mc "{i}That was so intese... At least with Cynthia we have the potions..."
        t "..."
window hide
pause 3
t "[mc]...?"
mc "...Yeah?"
t "I'm leaving tomorrow."
mc "..."
t "You've been by my side this past few weeks and you've been a great friend."
mc "...But?"
t "Don't make me say it, c'mon. You know what it is."
mc "I don't."
t "I'm twice your age, [mc]."
mc "And? We're both adults."
t "I...{p}...{p}...You're right, that's an excuse."
mc "What is it then?"
"Taliya sighs."
scene taliyaroom with fade
play music rmelancholy fadein 3
t "We're in the middle of a war, [mc]... We might never see each other again."
mc "Don't say that."
t "I've never had someone like you before, [mc]. Not in the past fifteen years."
mc "..."
t "I'm not sure if what I feel is love, but I know that I care about you a lot. You've done a lot for me too.{p}It had been a while since I last was just... Taliya. Not General Taliya, just... regular me."
t "I always put others first and forget about myself... after all I hardly need anyone to look after me."
t "I hadn't needed someone's help in over a decade and no one else has felt the need to protect me, but you... Even though you had no reason to, you still cared for me and made me feel... valued."
t "You made me realise that... I want this. I want someone like you in my life... But I can't have {b}you{/b}. Not while the Demon Army is still standing. Not while any one of us could be dead tomorrow."
mc "..."
t "I'll end this war and I'll come back for you. In the mean time, this was the only way I could thank you before leaving."
"She hugs you lightly."
mc "I... Don't know what to say."
t "Then don't say anything.{p}Rather, you don't mind sleeping here with me, do you?"
mc "Mh... I don't think I mind."
t "Good, let's sleep then."
"The two of you get into bed. You blow onto the candle and the room descends into darkness. Taliya hugs you."
scene sleeptaliya with fade
"The two of you stay like that for some time."
scene sleeptaliya
pause 5
t "{size=-3}When I'm back, I'll tell you I love you."
mc "Mh?"
scene sleeptaliya
pause 2
t "..."
scene sleeptaliya
pause 3
mc "{i}...She was sleep-talking?"
scene sleeptaliya
show sleeptaliya2 with dissolve
pause 2
mc "Goodnight."
scene black with fade
"And so, you fall asleep as well."
scene taliyaroommor with fade
stop music fadeout 3
"The next day when you wake up she's already gone. For a moment you panic but when you leave the room you find her eating something. She offers you some food and then the two of you leave her house."
scene villageback with fade
show prot sad
show tal sad
mc "So... when will you be leaving?"
t "In a few hours, there's a few things I need to do first."
mc "I see."
show tal smile
t "I'll do my best to meet again someday, I promise."
show prot hopet
mc "I know you will."
t "Goodbye, [mc]."
mc "Goodbye."
$ day += 1
$ time = 0
$ TaliyaQ = 7
$ persistent.Taliya6dom = True
jump home
