label Chapter1End:
hide screen hud
scene forrest with fade
mc "Uncle Pete should definitely know something."
"{i}Knock knock knock"
stop music fadeout 2
"...{p}......"
mc "Uncle Pete, you there?"
"......"
play music morganarides
"{color=#C64745}Woman's voice" "Come in, the door's already open."
mc "{i}Huh? Who's that?"
mc "Sorry, Uncle Pete. If you're busy then I'll-"
window hide
scene yakinapete1 with flash
pause 3
"......"
"{color=#C64745}Unknown" "Hello there. Your uncle and I were just catching up."
"......"
"{color=#C64745}Unknown" "Pete, is that what they call you now?"
"{color=#C64745}Unknown" "Hahahah, pathetic. Oh, how the mighty have fallen."
"{color=#C64745}Unknown" "...?"
show mcpetedeath
pause 3
"{color=#C64745}Unknown" "Hmm... The kid's still in shock."
"{color=#C64745}Unknown" "Well, I can understand. You might have been having a pretty normal day before this... Feeling the country breeze without a worry in the world."
"{color=#C64745}Unknown" "And then, boom! You get to see this spectacle."
hide mcpetedeath
"......"
"{color=#C64745}Unknown" "{size=-3}...Still not saying anything."
"{color=#C64745}Unknown" "......"
"{color=#C64745}Unknown" "{i}Ahem.{/i} I know this must be very hard for you, losing your \"uncle\". Believe me, I've lost someone irreplaceable too."
"{color=#C64745}Unknown" "And this FUCKING BASTARD IS RESPONSIBLE FOR IT."
"{color=#C64745}Unknown" "Your uncle had this a long time coming."
"{color=#C64745}Unknown" "But don't worry. You'll be joining him soon..."
u "[mc]"
u "R...{p}U...{p}N...!"
scene mcpetedeath
stop music
play sound horror
"{color=#C64745}Unknown" "You're still alive! Man, would you look at that. I just pulled your guts out and you're still talking... Hahahaha!"
scene mctrans1
show animationsuprise
pause 1
"{color=#C64745}Unknown" "Amazing! I can torture you all over again!"
scene ut2 with flash
pause 0.1
scene petethumbsup with flash
pause 0.1
scene dmndrm2 with flash
pause 0.1
if showpetebadge >= 1:
    scene petestargaze with flash
    pause 0.1
if sanderpetedinner >= 1:
    scene dinnerpetesander with flash
    pause 0.1
scene yakinapete1 with flash
pause 0.1
scene mctrans1
show animationsuprise
pause 0.4
scene mctrans4
pause 1.0
scene mctrans5 with flash
pause 0.3
scene petehouse1
pause 0.4
play sound crash
scene petehouse2 with hpunch
pause 0.3
play music battlemusic1
scene yakinakidfight1
pause 0.5
show yakinakidfight2 with easeinleft
"{color=#C64745}Unknown" "What the hell- I did not see that coming."
show mcrage with flash
mc "I'M GOING TO KILL YOU!!"
"{color=#C64745}Unknown" "Alright, then! I needed some action."
"Your body is burning like never before. The rage has completely consumed you."
"You rush at her. You focus all your anger onto your sword and bring it relentlessly down on her."
"The two of you exchange blows. You swing your arms back and forth. It almost feels like they're going to rip right off."
"The demon leaps back and distances herself from you."
scene yakinakidfight1
pause 0.2
show yakinakidfight3 with easeinleft
"{color=#C64745}Unknown" "......"
"{color=#C64745}Unknown" "That Aura... Is that...?"
"{color=#C64745}Unknown" "It can't be."
"{color=#C64745}Unknown" "......"
show yakinakidfight2
"{color=#C64745}Unknown" "Change of plans, you're coming with me."
mc "WHAT!?"
"{color=#C64745}Unknown" "You heard me."
"She flicks her hand and opens up a portal."
play sound magic
show yakinakidfight4 with flash
"{color=#C64745}Unknown" "Let's go."
mc "HUH!?"
"Your body suddenly freezes and is lifted into the air."
"Just then, a red orb flies past you and hits the demon girl."
hide yakinakidfight2
show yakinakidfight3 with flash
play sound magic
"You fall to the ground."
show yakinakidfight3 with vpunch
"{color=#C64745}Unknown" "Gh- You old bitch!"
scene scarmajic
pause 1
s "You have no chance of winning against me on untainted land, Yakina."
y "Tsk... Fine."
scene yakinakidfight1
pause 0.2
show yakinakidfight2
show yakinakidfight4
y "But you're still too late."
stop music fadeout 0.9
"She goes into her portal and disappears."
scene yakinakidfight1 with flash
scene yakinakidfight1 with flash
s "[mc]! Are you alright!? Where's Hans- Where's your uncle?!"
"Your body starts to cool down. You feel like you used up all the energy in your body, and now it's starting to shut down."
"Your vision fades."
"You point at Uncle Pete's shack."
mc "U-Uncle... Pete..."
"Scarlet rushes into the shack."
"The last thing you hear is her scream before you black out."
scene black
"......"
"......"
"......"
scene yakinakid1 with fade
pause 0.2
scene black with fade
pause 0.2
scene yakinakid1 with fade
pause 0.1
scene black with fade
pause 0.2
scene yakinakid1 with fade
y "Hmm... What is it, daddy?"
y "A gift? For me?"
show yakinakid3
pause
y "Woah...! A sword! It's so pretty..."
show yakinakid2
show yakinakid3
y "Thank you, daddy!"
y "I promise to always protect you with this."
scene yakinapete1 with flash
pause 0.2
scene yakinakid1
pause 0.1
scene drmc1
pause 0.1
show wakeup1
pause 0.1
show wakeup2 with flash
scene scarroom
mc "Aah!"
scene backscar2
pause 1
s "...[mc], You're awake."
mc "Ugh..."
show yakinapete1 with flash
pause 0.2
hide yakinapete1
mc "Gh-!!!"
mc "Uncle Pete! He's ok, right?"
s "......"
s "I'm sorry [mc]."
mc "No..."
mc "Wh-Where is he?"
mc "Tell me!"
s "...He's gone."
s "We... We buried him two weeks ago."
mc "......"
mc "Two... Two weeks."
s "You've been unconscious for two weeks."
mc "{i}No, no, no, NO!"
mc "{i}This can't be real."
mc "{i}Uncle Pete...{p}Sob..."
s "......"
"Scarlet reaches out to caress you but pulls back."
s "I'll..."
mc "{i}...Sob..."
s "I'll give you some space..."
scene scarroom with fade
mc "{i}...Sob..."
mc "{i}Uncle Pete, why did this happen to you?"
if showpetebadge == 1:
    scene petestargaze with flash
    u "I just want to keep on watching you, to see you on your journey. That's all I want."
mc "{i}...Sob..."
mc "I'm sorry Uncle Pete, I couldn't save you."
scene black with fade
"You lie back in your bed, still feeling like this all was a nightmare. You close your eyes and go to sleep, hoping that when you wake up everything would be back to normal."
scene backscar2 with fade
s "[mc]"
mc "Huh...?"
s "Sorry to wake you up, but I... brought you some food."
s "You should eat... It's [mcfood]."
s "You... like it, right?"
mc "......"
mc "Thanks, Scarlet."
mc "......"
mc "Scarlet, I want you to tell me what's going on... None of this makes sense."
mc "....Why? Why did this happen- Wh-Who was that!?"
mc "And why did she..."
s "......"
s "That was Yakina. The Demon King's daughter."
mc "Wh-What?"
mc "What does Uncle Pete have to do with any of this?"
s "......"
s "{i}Sigh{/i} I guess it's only right for you to know the truth now, [mc]."
mc "...Huh?"
s "Your... ‘uncle'..."
s "......"
mc "Say it already!"
s "......"
s "...Your uncle is Gladius Hans."
mc "What!?"
mc "I-I always knew he was hiding something from me."
mc "But... I never..."
mc "Why? Why did he keep it a secret from everyone? Why was he hiding here?"
s "It was to protect you."
mc "...to protect me?"
s "Yes."
mc "I-I don't understand."
s "You know about the last Hern Siege, right?"
mc "Of course I do."
s "You know what happened there?"
mc "The Maryas killed the Demon King."
scene scars1 with dissolve
s "Yes. Eva, Jarl, your uncle, and I were a part of the Maryas."
s "On the day of the Hern Siege-"
mc "...you were a part of the Maryas?"
s "Well, Yes..."
mc "......Go on."
s "...On the day of the Hern Siege, our mission was to take down the Demon King once and for all."
s "Amidst the chaos, as we were looking for the Demon King...{p} We found you."
scene scars3 with dissolve
s "As a house was burning down, we heard a woman's cries for help from the inside."
s "We went to the rescue. The house was falling apart, and the woman kept shouting for help, saying she was trapped in there with her child."
mc "Was that... my mother?"
s "...Yes, sort of."
mc "Sort of?"
s "I-I'll get to that in a moment."
s "We only managed to get the kid outside. His mother got stuck under the house while we were getting out..."
s "Yet, once outside, we noticed the boy had died, likely from asphyxiation... Eva tried to heal him, but it was too late."
s "...He was gone."
s "And then the Demon King appeared."
scene scars6 with dissolve
mc "......"
s "We were finally face to face with our mortal enemy. We had the chance to end the war."
s "So we fought."
s "The Demon King was even stronger than we anticipated. It was a tremendous battle, all of us were pushed to our extreme."
s "And thanks to that, we managed to bring him to his knees."
s "...That's when Hans dealt the final blow."
scene scars2 with dissolve
s "When the Demon King's head dropped, his corpse released a dark aura that cursed all of us."
mc "A curse...?"
s "Yes, a curse that weakened our bodies... significantly."
mc "What does that mean?"
s "Let... Let me show you."
"Scarlet removes her robe."
scene backscar with dissolve
s "Only your uncle and I survived the curse. It drains your energy and, unless you can supply your body with much more... you die."
mc "Did the others...?"
s "Eva and Jarl were gravely injured when it happened. Their bodies couldn't keep up."
scene backscar2 with dissolve
s "...They died after a few days."
mc "...I'm sorry."
s "......"
mc "So Uncle Pete was cursed..."
s "Yes, that's why his body was so weak."
mc "......I didn't have a clue."
mc "All of this... It's like I'm in a dream."
s "...I am not finished with the story yet."
mc "...?"
s "The Demon King cannot be truly killed, we learned it that day."
mc "Huh?"
scene scars4 with dissolve
s "When the Demon King was killed, his soul was released... It looked for an empty vessel."
s "The Demon King's soul had been weakened by the battle, it didn't have enough strength to look for a suitable vessel, so it simply went to the nearest one."
s "...The body of the kid we saved, that was you."
s "And so the Demon King's soul merged with the kid's body."
mc "{i}So that's the reason for those dreams, that's how I managed to fight against Yakina..."
mc "{i}...Why do I feel like I always knew this?"
mc "So a part of the Demon King is living in my body?"
s "...{p}No, [mc]."
s "You are the Demon King."
mc "......"
mc "Wh-What? Just because a part of him is living inside me, doesn't mean I'm the Demon King."
s "I'm sorry, [mc]. Your body was empty. Nothing of the boy remained besides the body."
s "When the Demon King possessed your body, it came back to life... but it had lost all of its old memories along with its original soul."
s "Which means that you are the Demon King. That's the reason why you can't remember your past. Everything that happened before the Hern Siege was erased when you were killed."
mc "{i}What the hell is she trying to say? How could I be the Demon King?"
mc "{i}I'm me, I'm [mc]."
s "I'm sorry [mc]. This is why we were afraid to tell you any of this."
mc "......"
mc "I..."
mc "I don't care what you say, I'm still me, [mc]."
s "[mc]..."
mc "What happened after that?"
s "Eh?"
mc "You said you would tell everything. How did I end up here?"
s "......"
s "With the supposed death of the Demon King, the Demon Army retreated and we won the battle."
s "Everyone celebrated the victory against the Demon Army and we were awarded titles... You know all that."
s "Hans brought you to the Capital with him, after all that."
s "We didn't know what to do with you. We... weren't sure of what you were."
s "So we took care of you."
s "At first everything was going great. You were just a normal child."
s "Hans actually enjoyed taking care of you. It probably must have been a way for him to cope with the loss of Eva."
mc "Were Uncle Pete and her...?"
s "Yeah."
mc "..."
s "A couple of years went by. That's when I started to sense your dark aura growing stronger and stronger."
s "But you were still you. Cute and cuddly, more like Hans' son than the Demon King."
s "With your dark aura growing stronger, we couldn't keep you in the Citadel anymore. If the citadel mages found out about it, they would've taken you away."
s "Hans didn't want that, so he left the Capital with you."
mc "He left just like that?"
s "Yes. He didn't have anything left to do there anyway."
s "Because of his weak body he couldn't be a soldier anymore and he had no one left in the Capital."
mc "Oh..."
s "And that's how you ended up here in Randel. I don't know how the hell he found this place."
mc "......"
scene backscar2
menu:
    "What about you?":
        mc "What about you? What happened to you after the war?"
        s "Me?"
        s "Well, I was traveling around Astylla, studying, looking for a way to cure our curse."
        s "But I couldn't find anything in the end."
        mc "Why did you come here?"
        s "Hans- ...Your uncle sent me a letter asking me to come to Randel."
        s "He said he needed me... To look after you."
        mc "Why?"
        s "He said that he didn't have much time left... He felt that his body couldn't fight the curse for any longer."
        s "So I packed my bags and came to Randel."
        s "He was in very bad shape when I got here."
        mc "But... He looked perfectly fine..."
        s "He was probably hiding it from you."
        mc "...Hiding it?"
        mc "{i}Is that why he left the house and moved into the fishing hut? So that I wouldn't see him in pain?"
        mc "{i}Uncle Pete, you didn't have to..."
        s "I treated him from time to time, it slowed the process down."
        mc "..."
        mc "Thanks for looking after him, Scarlet."
        mc "I wish I could've helped him, but I did jack shit. Adventuring out there like a little kid, what was I thinking!?"
        mc "I didn't even think for a second he had some problems, I... I could've checked on him more... I..."
        s "[mc], don't say that!"
        s "He loved you, ok? He wanted you to be happy."
        mc "{i}Sob"
        s "Oh, [mc]."
        s "......"
        scene backscar3
        "Scarlet caresses you."
        s "I'm not sure how to do this... I don't think I'm cut for parenting... Heh... {p}{i}Sob..."
        mc "{i}Sob{/i}... You're not supposed to be crying..."
        s "{i}Sob{/i}... Heh, Sorry..."
        "Scarlet wipes off her tears."
    "...":
        mc "..."
s "I know that's a lot to take in..."
s "I-I'll leave you to it then. You should rest, [mc]... But only after you've eaten your food, ok?"
mc "Alright."
s "Alright."
"Scarlet gets up."
mc "Thank you, Scarlet."
mc "I don't know what I'd do without you."
s "...Rest well."
play music rvisitors fadein 5
scene scarroom
"{i}Knock knock"
sa "[mc], you in there?"
mc "...Sander?"
s "He's resting."
sa "It's been 2 weeks! You're telling me he's still out?"
mc "C-Come in, Sander."
sa "See? He's awake."
show scarroomse with easeinright
sa "Hey little man."
e "How are you doing, little one?"
mc "I... I'm okay."
e "We heard about what happened. A bandit attack, who could've thought."
mc "...A bandit attack?"
e "Yes... your uncle's house was attacked. Don't you remember?"
mc "{i}Ah, shit... Scarlet must have made up a story to keep our cover."
mc "My memory is... a bit foggy. I don't even know where I am right now, honestly."
e "This is Scarlet's home."
mc "Oh, that... makes sense."
sa "......"
"The two of them stare at you awkwardly, they don't know what to say."
sa "If you need anything... we're here for you, [mc]."
e "Yes all of us are."
mc "Thanks, guys."
"Eve gives you a hug."
if evesex >= 1:
    "She kisses you on the cheek."
"Sander pats you on the back."
if savedaerin >= 1:
    e "Oh, and... here."
    "Eve hands you a letter."
    e "This is from the village, I told them what happened..."
    "You open it."
    show millyletter
    pause
    mc "...Tell them I said thanks."
    "Eve nods."
    hide millyletter
e "We'll leave now. Scarlet might throw us out if we don't."
sa "See you, kid. We'll all get together once you're feeling better."
mc "Alright."
hide scarroomse with easeoutright
"The two of them leave."
if theasex > 0:
    e "Oh, Thea. Came to see [mc]?"
    th "Y-Yes, is he awake?"
    sa "Yeah, we just talked to him."
    th "Can I see him?"
    e "Go ahead."
    show scarroomth with easeinright
    th "How are you doing, [mc]?"
    mc "I'm... ok."
    th "{i}Sob"
    mc "H-Hey! W-Why are you crying?"
    th "I... {i}Sob{/i}... don't know..."
    th "I'm sorry, [mc]."
    mc "It's alright, Thea."
    mc "Come here."
    "You take her in your arms."
    th "I should be the one comforting you... {i}Sob."
    mc "You being here is more than enough."
    th "......"
    th "Your uncle was a very nice person..."
    th "Why do these horrible things happen only to the good people..."
    mc "......"
    mc "It's just the way it is."
    th "......"
    "Thea gets up."
    th "Since you're doing fine, I'll... leave. Scarlet said you should get some more rest."
    mc "I don't mind really."
    th "No, you should rest!"
    th "...R-Rest and get better."
    th" I'll have some good food ready when you come back home."
    mc "Alright..."
    th "Bye, [mc]."
    hide scarroomth with easeoutright
scene black with fade
"You close your eyes and try to get some rest."
scene scarroom
"{i}Knock knock"
g "[mc]?"
mc "{i} Looks like I won't be getting any rest."
mc "Come in."
show scarroomg with easeinright
g "Hey..."
mc "Hey."
g "You doing alright?"
mc "Yeah. Scarlet has patched me up pretty good."
g "It's a good thing you got the greatest healer in Astylla treating you."
mc "Huh?"
g "I mean Scarlet. You know... she's the Scarlet of the Maryas herself."
mc "Wait, you knew?"
g "I did some digging around to find out, but it wasn't th- Wait, how did you know?"
mc "She... She just told me."
g "Really? Didn't know you two were that close."
mc "......"
g "......"
g "Uncle Pete... I can't believe he's gone just like that."
mc "......"
g "I'm sorry if it's making you uncomfortable. This is all new to you, even though it's been two weeks for us."
mc "...It's alright, don't worry."
g "...Whenever I'd come over to your house to play when I was little, just seeing him would put me in a good mood."
g "I always wished... I had a dad like him."
mc "..."
g "He's in a better place now. He deserves it."
mc "Yeah."
g "...Ok, my times up."
g "I'll see you later then. If you need to talk, I'm here for you [mc]."
mc "I know."
g "Bye."
hide scarroomg with easeoutright
mc "......"
if cynthdate >= 1:
    mc "{i}Wonder if... Cynthia knows?"
    "You hear a conversation coming from outside your room."
    s "He's had too many visitors already. Let him rest."
    c "Ahhh, come on! It's just for a little while."
    show scarroomc with easeinright
    c "See? He's not even sleeping."
    s "You're the last one. I'm putting up a force field after."
    c "Hey, [mc]."
    c "You doing alright?"
    mc "Yeah, just getting pretty tired of hearing that same question."
    c "Oh, I'm sorry."
    mc "Nah, it's fine."
    c "I just... I just wanted to see if you were ok."
    mc "Well... how do I look?"
    c "You look fine. You got all your limbs intact and your dumb face is still the same."
    c "But... there are things that you can't see on the surface."
    mc "I'm doing ok..."
    c "......"
    c "Really?"
    mc "...Y-Yeah."
    c "That's good, that's good..."
    "Cynthia sits beside you."
    "She starts to stroke your hair."
    mc "...What are you doing?"
    c "I'm comforting you, asshole."
    mc "Oh, ok.{p}Kinda came out of nowhere."
    c "My god, [mc]. If you want me to leave, just say it."
    mc "What? I was just saying..."
    c "......"
    c "Seems like you really are doing ok."
    "From outside, you hear Scarlet's voice."
    s "{size=-3}Time's up!"
    c "W-What? B-But I-"
    c "...Guess I'll leave then..."
    c "That old hag needs you all to herself, it seems."
    mc "Heh."
    c "I'm glad that you're ok, [mc]."
    c "Please come see me once you've rested well enough."
    mc "I will. Thanks for cheering me up, Cynthia."
    c "...No problem."
    c "See you soon."
    "She gets up. She seems hesitant to leave you. Now that you think about it, having almost lost you once already probably means she's very worried."
    mc "Cynthia?"
    c "...What?"
    mc "You know that I love you, right?"
    c "...Me too, idiot."
    "And so she leaves as well."
    c "{size=-3}He's all yours."
    hide scarroomc with easeoutright
scene backscar3 with fade
stop music fadeout 5
s "Finally, some silence and peace for you."
s "Get some sleep, [mc], I mean it. If you want anything just call me, I'm right next to your room."
mc "Alright."
s "Goodnight."
mc "Goodnight."
scene black with fade
mc "{i}Sigh..."
mc "{i}I guess that was everyone."
mc "{i}Thank you, guys."
scene black
play music nightvigil fadein 3
pause 3
y "Hello..."
mc "Uh... Huh?"
y "I knew it would work!"
mc "Who...?"
scene yakinaend with dissolve
y "...It's me, Yakina."
mc "YOU!"
mc "Where are you!? How are you talking to me!?"
mc "As soon as I find you I'll rip you to shreds! You hear me!?"
y "...So you've forgotten everything."
mc "WHAT?"
y "You have his aura, but you're a different person."
mc "Of course I am! Did you really think I'm your father?"
mc "Well, too bad! He's dead."
if evil == 4:
    y "Oh, but he lives inside of you."
    y "I can see all your memories now that we are linked, and I can see all the things you've done..."
    y "I see you enjoy making slaves as much as father did~"
    mc "Shut up! It's different!"
    y "Keep telling yourself that."
    mc "I'll kill you! I'll kill you, and then you'll see exactly who I am!"
    y "Haha..."
    y "I'll be waiting."
    mc "I am going to kill you."
    jump creditsEnd
elif evil > 1 and good > 0:
    y "Tsk... But I can still sense him somewhere in there..."
    y "You're not as pure as you want the world to believe."
    mc "Wh-What?"
    y "I can see all your memories now that we're linked... I can see you've done some bad things as well, yet... your heart isn't black."
    mc "I told you. I'm no Demon King. I'm different."
    mc "And once I find you, you'll see exactly who I am."
    y "......"
    stop music fadeout 3
    y "He's still in there somewhere, I know it. I just need to bring him out."
    y "Alright, Hero. Come find me."
    mc "I will."
    y "I'll be waiting."
elif evil == 3:
    y "Heh... You keep telling yourself that. I can see all your memories... Everything you've done."
    mc "Wh- How...?"
    y "We're linked now, how did you think I was talking to you."
    mc "Ngh..."
    y "Oh my, you've done some bad things, boy. You deny it but you are a monster."
    y "I know my father is in there somewhere. It's all just a matter of time till he comes out."
    mc "No, you're wrong!"
    mc "I'll kill you! I'll kill you, and then you'll see exactly who I am!"
    y "Haha..."
    y "I'll be waiting."
    mc "I am going to kill you."
    jump creditsEnd
else:
    y "Tsk..."
    y "Your heart is pure."
    y "I can see all your memories, everything you've done, and yet..."
    mc "Wh- How...?"
    y "We're linked now, how did you think I was talking to you."
    mc "Ngh..."
    y "This is impossible, you are the Demon King..."
    mc "I told you. I'm no Demon King."
    mc "And once I find you, you'll see exactly who I am."
    y "......"
    stop music fadeout 3
    y "H-He's still in there somewhere, I know it... I just need to bring him out."
    y "Alright, hero. Come find me."
    mc "I will."
    y "I'll be waiting."
scene black with fade
show text " {color=#fff}A few days later. {/color}"
pause 2
hide text
stop music
scene petegrave with fade
play music rmelancholy fadein 1
mc "......"
s "You ready to go?"
mc "Yeah."
s "Are you really sure you want to do this?"
mc "Yes."
mc "I can't stay here, not anymore. I don't want to put anyone else in danger."
s "......"
mc "I want to go to the Capital. I'll join the army and then go kill that demon myself."
s "...I understand."
s "Shouldn't you at least tell everyone you're going?"
mc "I can't, I don't want anyone involved with this."
mc "I wrote them letters saying that I'm leaving, they'll find them once I'm gone."
s "......"
s "Alright, It's your decision."
s "Let's leave then."
stop music fadeout 2
mc "Okay."
"You leave Randel with scarlet."
play music bunispiano fadein 3
scene end with fade
mc "This village was my whole life. I never imagined I would leave it."
mc "Everyone I met, every memory I had here, I will cherish it for the rest of my life."
mc "Goodbye, everyone."
label creditsEnd:
$ persistent.mmSong = "disquiet.mp3"
$ persistent.pt1End = True
$ renpy.force_autosave()
scene black with fade
pause 1
scene endcredit with fade
pause 5
scene black with fade
scene credit1 with dissolve
pause 7
scene credit2 with dissolve
pause 7
scene credit3 with dissolve
pause 7
scene credit4 with dissolve
pause 7
scene credit5 with dissolve
pause 7
scene credit6
show screen creditButton
stop music fadeout 8
pause 8
hide screen creditButton with dissolve
scene black with dissolve
pause 1.5
$ MainMenu(confirm=False)()
return

screen creditButton():
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.555
        idle "creditbutton.webp"
        hover "creditbuttonhover.webp"
        action OpenURL("https://www.patreon.com/randeltales")
