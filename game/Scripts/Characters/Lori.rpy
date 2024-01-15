default loriTalked = 0
default loriLiedAboutSchool = False
default loriKnowsDroppedOut = False

label loriTalk:
hide screen hud
scene libraryblr with dissolve
show talkhappymc
show smilel
mc "Hi, Lori."
hide talkhappymc
show smilemc
show talkhl
l "[mc], it's nice to see you! What brings you in today?"
hide talkhl
menu:
#    "Hang out with Lori":
#        mc "Just thought of coming over to hang out."
#        l "[mc], you know the Library isn't a place to hang out at..."
#        mc "Yeah you're right sorry, I'll go then."
#        l "...B-But I could make an exception for you!"
#        mc "Really?"
#        l "Yeah! There's nobody else here right now, who's going to get angry because we're talking?"
#        mc "Makes sense to me. I'll leave as soon as someone arrives."
#        l "Sure thing. Come on now, have a seat."
#        scene black with dissolve
#        "Lori zooms in the back of the Library, so you sit down and wait for her to come back. When she's back a few minutes later she's got two cups in her hands, presumably one for her and one for you."
#        mc "What's that?"
#        if loriTalked < 2:
#            l "Oh, it's tea."
#            if loriTalked == 1:
#                mc "Just like last time."
#                l "Heheh, yup."
#            else:
#                mc "Oh, nice."
#        else:
#            l "The usual."
#            mc "Nice."
#        "She gives you the cup and the two of you start sipping."
#        if loriTalked == 0:
#            jump loriTalk1
#        if loriTalked == 1:
#            jump loriTalk2
#        if loriTalked > 1:
#            jump loriTalkRepeat
    "Ask for a history book" if gabee1 == 1:
        show talkhappymc
        mc "Can I get a history book?"
        show talkhl
        l "Oh, yeah. What book are you looking for?"
        mc "Uh... Randel's Local History Book...?"
        l "Ah... You're studying for the test, right?"
        mc "Yeah."
        show talkhsl
        l "I'm sorry, [mc], the last history book was taken just a few hours ago."
        show talkwanmc
        mc "What! Really?"
        l "Yeah, a lot of students came in looking for one."
        show talksadhappymc
        mc "I guess I was too late."
        l "Hmm... Maybe you can ask Mr. Boris."
        mc "My teacher? Are you sure he'd let me?"
        l "Well, that's the only way you're going to get a book."
        mc "I have no choice then."
        l "Good luck."
        $ gabee1 += 1
        jump library

    "Ask about Rosa Flowers" if askloriaboutrosa == 1:
        show talkhappymc
        mc "Do you know what a Rosa Flower is?"
        l "I do."
        mc "Great! What does it look like?"
        l "It's pink and has five petals, it can be found in almost any season."
        mc "That's a relief. Where do you think I can find one?"
        l "You can probably find some in the Outer Valley, they're not that rare."
        mc "Ok, thanks."
        l "Happy to help."
        $ knowrosa += 1
        $ askloriaboutrosa -= 1
        scene Library with fade
        mc "{i}So, they're in the Outer Valley, that's good. I should go get some quick."
        jump library

    "Nothing.":
        show talkhappymc
        if flirtingWithLori == True:
            mc "Nothing really, just wanted to see the cutest librarian in town."
            hide talkhappymc
            show blushl
            l "..."
            hide blushl
            show talkhsl
            l "W-Well, here I am."
        else:
            mc "Nothing in particular, just wanted to see how you were doing."
            hide talkhappymc
            show talkhsl
            l "O-Oh! I'm doing good."
        hide talkhsl
        show talkhappymc
        mc "Good to know. See you later then."
        hide talkhappymc
        show talkhsl
        l "Bye, [mc]."
        jump library







#label loriTalk1:
#    l "So, how's it going? Been on any fun adventures recently?"
#    mc "Honestly yeah, lots."
#    l "Oh, that's great. You also go to the Academy, right?"
#    if faila == True:
#        menu:
#            "Yes":
#                $ loriLiedAboutSchool = True
#                jump loriYesSchool
#            "Not anymore":
#                $ loriKnowsDroppedOut = True
#                mc "Oh, uhm, actually..."
#                l "Yes?"
#                mc "I... failed the exam."
#                l ""
#                mc ""
#                l ""
#    else:
#        label loriYesSchool:
#        mc "Yeah."
#        l "How... How is it like?"
#        mc "Huh? What do you mean?"
#        l ""
#        mc ""


#label loriTalk2:



#label loriTalkRepeat:
