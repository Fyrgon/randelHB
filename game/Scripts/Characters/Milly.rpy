default millyInfo = False
default childlessZen = False


label talkmilly:
    menu:
        "Where can I find the elf priestess?" if bothpath >= 1 and bothpath <= 3:
            mc "Where can I find the elf priestess?"
            mi "She mostly spends her time in the shrine room. You probably won't be able to meet her there, only priests are allowed to enter."
            mc "Alright, when does she leave?"
            mi "She leaves at night."
            mc "Ok, thanks."
            mi "What are you up to, [mc]?"
            mc "Nothing, I just wanted to ask her something."
            scene elfvillage
            mc "{i}So she comes home at night... I should wait until then to meet her."
            jump elfVillage

        "About Aerin" if aerinQ == 1:
            mc "Do you know Aerin?"
            show talkhmi
            hide talkwami
            mi "Yeah! She's my best friend!"
            mc "What!?"
            show talkwami
            mi "Yeah I know, I know she and my sister don't really get along well, but she really likes me, and I like her too. She always plays with me when Eve isn't in the village."
            mc "Really, she doesn't look like a playful kind of person."
            hide talkwami
            show talkshmi
            mi "She might look a bit dull, but she's a really nice person. You have to understand that she's gone through a lot."
            mc "You're right."
            mi "I think you should visit her."
            mc "What?! Why should I?"
            mi "After her mother was banished, she's always been tucked away in her house. She didn't really talk to anyone in the village, so the village stopped paying attention to her too."
            mi "But I can tell she really likes visitors now!"
            mc "Yeah, but why me?"
            show talkwami
            mi "Well, you're a new face, and she would probably open up to you more. And besides, she won't be able resist your manly charms."
            show talkwamc
            mc "Hahaha, very funny."
            mi "Just do it, will ya? You'll thank me later."
            mc "We'll see."
            $ aerinQ = 2
            jump talkmilly

        "About you":
            mc "I'm curious, how come there's such a huge age gap between you and Eve? I mean, she's like 300 and you're, what? 160? that's over a century."
            mi "...I guess I'll have to teach you something about elves."
            mi "Now, pay attention: You see, an elf can only be impregnated once, and the maximum number of offspring that they can give birth to is three."
            mc "Really? I had no idea about that."
            mi "Yeah, these things are not the kind of topics discussed in human books, but it makes a lot of sense if you ask me."
            mc "How so?"
            mi "Let's say that elves can give birth to as many offspring as they want. Considering that the normal lifespan of an elf is about 500 years, how many offspring do you think a female would have during her lifetime?"
            mc "...A lot?"
            mi "A helluva lot, as you humans say."
            mi "We would have populated every inch of Astylla if that were the case."
            mc "Hm, I guess it kind of makes sense."
            mi "So you see... it has to be balanced, as all things should be."
            mc "Yeah, I get it now."
            mc "But you still haven't answered my question."
            mi "I'm getting there, hold your horses."
            mi "As I was saying... Once a female is impregnated the time the babies are given birth to are different. Some could be born together and some after 50 or 60 years or in my case, after 145 years."
            mc "{i}Man, I'm being lectured on elf reproduction by a little girl and she's totally cool about it."
            mc "{i}I can't even imagine Sander hearing about this without giggling or saying some stupid joke like \"Ohh, so that means elves can have as much sex as they want without getting pregnant, huh?\", he can be really immature."
            mc "But still, isn't the time gap too long?"
            mi "Time is relative, [mc]."
            mc "Huh?"
            mi "I mean that the perception of time changes from person to person. For you, 100 years feel like a lifetime. But for us, it feels like a decade."
            mi "We are isolated from the outside world and so invested in our own version of reality that our perception of time is entirely different."
            mc "Oh..."
            mi "I'll tell you something interesting, and you to better understand this!"
            mc "I'll try."
            mi "So, like, I said our sense of time here is different, right?"
            mi "But when an elf leaves a place like this and goes to the outside world, his or her sense of time is totally..."
            mi "...fucked!"
            mc "...?!"
            mi "What? I'm trying to make this easier for you by using human terms."
            mc "Oh, okay, yeah, sure. Go on."
            mi "So, when the elf leaves the village to visit the outside world, their senses of time clash together. They get adjusted to the new flow of time, and that's a painstakingly long and difficult process."
            mi "So now think what happens when that elf comes back to the elf village and starts living here again."
            if chartrait == 1:
                mc "Uh... they feel like time has slowed down?"
                mi "Exactly, because they are adjusted to the outside world, a day feels like eternity in here."
            else:
                mc "Uh..."
                mi "Since they are adjusted to the time flow of time in the outside world, a day feels like it's an eternity here."
            mc "{i}She's pretty smart. I guess age does make you wiser... even if you look like a little girl."
            mc "{i}Man, I wish I could be half as wise as she is one day..."
            mc "Thanks for that lecture, my head feels like it's about to burst."
            mi "Sorry if I stuffed too much knowledge in that tiny human brain of yours."
            mc "Hey!"
            mi "Heheh."
            mc "So this must be why Eve hates this place."
            mi "Yeah. After spending some time in the outside world, she couldn't manage staying here for extended periods of time. It was practically torture for her, but she stayed here and endured it because of me."
            mc "I get that."
            mi "So I told her to leave this place."
            mc "...You're a good sister."
            mi "I just made the most logical decision."
            jump talkmilly

        "About the Priestess" if bothpath <= 4:
            $ millyInfo = True
            mc "You're her apprentice, so... What can you tell me about the Elder Priestess?"
            mi "Most people don't really like her..."
            mc "...I figured."
            mi "But she can actually be a nice person."
            mc "Can she, now?"
            mi "Well, she doesn't have many friends in the village..."
            mi "Because of her role she's not really approachable... And so most people don't talk to her out of strict necessity."
            mc "I see."
            mi "She's also the oldest one in the village, I've heard her brothers were the only friends she had and they both died in the war while fighting alongside humans..."
            mc "...Is that why she dislikes humans so much?"
            mi "Who knows."
            mi "But she's actually nice with me! She is very wise and a good teacher."
            mi "But she is kind of weird... She always disappears at certain hours of the day."
            mc "Disappears?"
            mi "Well, she says she goes home, but one time I went to her home and, when I knocked, she didn't answer."
            mi "It's not like anyone else noticed... Nobody goes to talk to her outside of when she's at the temple."
            mc "She could do anything at her house and nobody would find out, you're saying?"
            mi "Hahah, I guess!"
            mc "Well, thanks for telling me more about her. I'm gonna go now."
            mi "Alright! See you [mc]-ayya."
            jump talkmilly

        "Elf history":
            mc "Could you teach me a bit about elf history?"
            mi "You really wanna know about that?"
            mc "Uh, yeah, why not?"
            mi "Where should I even start?"
            mc "How about from the beginning? You elves have been living in Astylla for a longer time than humans. There might even be things you know about us that even we don't."
            mi "Hmm... fine."
            mi "Then it's time for an in-depth history lesson, so listen carefully."
            mc "Yes, ma'am!"
            mi "So at the very beginning, what is now Astylla was a wasteland; inhabitable, no one thing could survive there. But there was a race that lived in Astylla at that time, the dwarfs. They lived underground."
            mi "After many years, our kind; the elves, came from the stars and cleansed Astylla of its impurities, and was now a place blooming with life. The elves inhabited the earth. "
            mi "After some time had passed, the dwarven race came out to the surface. The dwarfs also slowly started to inhabit the surface, but they didn't interfere with the elves. We learned to live together."
            mi "As time passed by, all sorts of creatures started to appear and disappear. There were animals, birds, fish and all sorts of unimaginable and indescribable creatures. Some survived, and the others either died off, or moved to another place."
            mi "Then there was the apes' time to prosper. In other words, your ancestors. We saw how they gradually started to imitate us, they started to walk on two legs, they started to wear clothing- well- if you can call it that, they began making tools and even started to speak our language."
            mc "Wait a minute, I thought Astyllian was the elves' language."
            mi "It was, but as time went on, the language changed. With help from both the dwarven tongue and Astyllian, they merged and created modern day language."
            mc "Interesting. Continue shitting on humankind, please."
            mi "I haven't even started yet. believe me, the fun is yet to be had."
            mi "So after some time, the humans started to build settlements, and their population increased at an unimaginable speed. Eventually, we all had to learn to live together. Though there were some problems between the elven and human race, it was mostly peaceful."
            mi "But everything changed 1500 years ago. Once the Demon King was summoned, Astylla was in chaos."
            mc "The Demon King? 1500 years ago? Our Demon King?"
            mi "Well, almost. You see, the Demon King is a spirit that some say to be as old as elves."
            mi "Many elves have become the Demon King according to our history, he gets summoned every thousands of years or so, and every time we fight against him and win... Or at least we used to."
            mi "The Demon King was the first elf to summon the spirit of the Demon King since our arrival in Astylla. He created all the monsters you see around, like the goblins or the direwolves."
            mc "Wow... I didn't know that..."
            mi "There's lots that humans don't remember anymore."
            mi "You see, after a long war, us elves managed to banish him again. We had lost most of our people since we had been at the front in the war unlike most humans, who ran as far as they could to avoid getting slaughtered."
            mi "Still, we thought it was over. We had defeated the Demon King once again, and he'd never come back..."
            mi "But then, 400 years ago, the elf prince, Rem, used a spell and summoned the Demon Lord's spirit... and became the Demon King."
            mi "The Demon King was out to kill every elf living in Astylla, as he recognized the potential and knowledge of the elves and saw that we were the biggest threat to him. So that was when the all-out war between the elves and the Demon King's Army, began."
            mi "We tried to use the same spell we used before, but he had found a way to make himself and his creatures immune to it..."
            mi "The dwarves joined the elves in battle, but what did the pathetic humans do...?"
            mi "They fucking crawled into a corner and started building a wall to save their own asses. They didn't care about the fact that the elves were getting slaughtered left and right."
            mc "Oh..."
            mc "{i}That does sound like typical humans, only caring about themselves and screwing everyone else over in the process."
            mi "In the end, most of the elves were killed. The remaining elves and dwarves had no choice but to flee inside of the walls."
            mc "So the humans did do something useful after all!"
            mi "Useful?! We could have won the entire war if the humans had joined us."
            mc "Yeah, that's one way to put it, I guess..."
            mi "So that's the history of how Astylla came to be."
            mc "Wow, there was so much I didn't know. Thank you!"
            mi "No problem."
            jump talkmilly

        "Village history":
            $ childlessZen = True
            mc "What's the story of this village?"
            mi "You want to learn about the village history?"
            mc "Yes."
            mi "Okay then. This village is nearly 1500 years old. After the first war against the Demon King, four female elves who had lost their husbands to the war decided that they would flee to the forest and make a secret village where they would be safe."
            mi "These four brave elves are the Great Four Mothers. They were the ones that built this village."
            mi "All four of them were pregnant. And after some time, they all gave birth to twins."
            mi "The first generation had four males and four females."
            mi "The village kept expanding, with each generation being bigger than the previous one. The sixth generation had 27 elves."
            mc "27?! That's more elves than the ones in the village right now!"
            mi "Yes... It's because the war started just when the 6th generation was becoming adult."
            mc "All of the men were sent to war and all of them died... And of the 9 women in the village, only 8 got pregnant who then gave birth to Me, Eve, and all the others you see in the village."
            mc "Who was the elf that didn't get pregnant?"
            mi "It was elder priestess Zenelith."
            mc "Oh... That probably wasn't nice for her..."
            mc "Wait, then she's the oldest elf in the village?"
            mi "Yes, she's the last of the sixth generation. She's over 400 years old."
            mi "The seventh generation is the current adult one; it consisted of five males and eleven females... but all the men have died in war."
            mc "I heard one disappeared."
            show talksmi
            show normalmc
            mi "We just say he disappeared, but most of us think he was killed. He went on a hunting trip and he never returned."
            mi "His name was Morgan, he was Aerin's brother."
            show talkwanmc
            mc "I heard about that... She must've been distraught."
            mi "Yeah, she managed to make it through everything. She really is a strong elf."
            mc "Hmm."
            mi "That's about it."
            show normalmi
            hide talksmi
            mc "Thanks, Milly."
            show talkhmi
            mi "It was my pleasure!"
            jump talkmilly

        "Leave":
            mc "Bye, Milly-nangi."
            mi "Bye-bye!"
            jump elfVillage
