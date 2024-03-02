########## Note for Myself: #######################
## This can be done in a different, better way.  ##
## By adding a variable for when quests are      ##
## finished, you can put the tips for each quest ##
## in a single if statement tree, instead of     ##
## multiple different if statements — which      ##
## repeat endlessly "X's Storyline"              ##
###################################################


screen screenjournal:
    modal True
    add "images/journalscrn.webp"
    vbox ymaximum 0.8 xalign 0.8 yalign 0.1 xsize 0.32 xanchor 0.8 yanchor 0:
        ## Storyline 1
        if q1 == 0:
            text "{b}Guild Storyline{/b}"
            text "> I should visit the Guild again."
        if q1 == 1 :
            text "{b}The Way of the Voyeur{/b}"
            text "> I need to learn about the invisibilty spell."
            text "...I could ask Scarlet."
        if q1 == 2 and ieyeorb == 0:
            text "{b}The Way of the Voyeur{/b}"
            text "> I need to buy an Eye Orb from the merchant."
        if q1 == 2 and ieyeorb == 1:
            text "{b}The Way of the Voyeur{/b}"
            text "> Ok... It's peeking time..."
        if q1 == 3:
            text "{b}The Way of the Voyeur{/b}"
            text "> I should give the Eye Orb to Sander."

        ## Storyline 2
        if q2 == 0 and q1 == 4:
            text "{b}Guild Storyline{/b}"
            text "> ...I should talk to Evelyn."
        if q2 == 1 and readalphafalcon == 0:
            text "{b}Show Who's The Alpha{/b}"
            text "> I need to learn about the \"Alpha Falcon\"."
        if q2 == 1 and readalphafalcon == 1:
            text "{b}Show Who's The Alpha{/b}"
            text "> I need paint for a green arrow. Uncle Pete should have some."
        if q2 == 2 and alphafalcon < 3:
            text "{b}Show Who's The Alpha{/b}"
            text "> It's time to hunt."
        if q2 == 2 and alphafalcon >= 3:
            text "{b}Show Who's The Alpha{/b}"
            text "> I've killed 3 Alpha Falcons. Now I gotta go speak to Eve."



        if level < 10:
            text "{b}Advancing in the Guild{/b}"
            text "> I want to reach Bronze-Rank in the guild..."
            text "> Better start leveling up."
        if level >= 5:
            if icamping == 0:
                text "{b}Advancing in the Guild{/b}"
                text "> Now that I can go on quests, I should buy some camping gear."
            if level >= 10:
                if party == 0:
                    text "{b}Advancing in the Guild{/b}"
                    text "> Now that I've reached level 10, I can become a Bronze-Rank adventurer!"
                if party == 1 and showpetebadge == 0:
                    text "{b}Advancing in the Guild{/b}"
                    text "> I'm a Bronze-Rank Adventurer now! I should go and tell Uncle Pete the good news."
                if party == 1 and sawtriss == 0:
                    text "{b}Advancing in the Guild{/b}"
                    text "> I should visit the Guild."
                if party == 1 and sawjuly == 1:
                    text "{b}July's Storyline{/b}"
                    text "> July is hiding something. I should sneak into the Guild at night and see what's going on."
                if party == 1 and sawjuly == 2 and sawjuly < 4:
                    text "{b}July's Storyline{/b}"
                    text "> I should check on July and see what's really going on."




        if sawmegan == 1:
            text "{b}Megan's Storyline{/b}"
            text "> I should go hunting today."
        if sawmegan == 2:
            text "{b}Megan's Storyline{/b}"
            text "> I should go tell July about the bandits I saw in the forest."
        if sawmegan == 3 and metmegangq == 0:
            text "{b}Megan's Storyline{/b}"
            text "> I should meet Megan at the Guild Quarters after noon."




        if sawtriss == 1:
            text "{b}Triss' Storyline{/b}"
            text "> I feel like going into the forest today."
        if trissq1 == 1 and ibugnet == 0:
            text "{b}Triss' Storyline{/b}"
            text "> I should buy a bug net to catch butterflies."
        if trissq1 == 1 and ibugnet == 1:
            text "{b}Triss' Storyline{/b}"
            text "> Ok I got the net. Now I just have to go meet her in the afternoon."
        if trissq1 == 2 and mettrissgq == 0:
            text "{b}Triss' Storyline{/b}"
            text "> I should meet Triss at the Guild Quarters after noon."




        if party == 1 and evesex == 0 and sequest1 == 0:
            text "{b}Eve's Storyline{/b}"
            text "> I should probably talk to Eve if I want to go on a quest with them."
        #Q1pre
        if bothpath > 6 and evemillyquest == 0:
            text "{b}Eve's Storyline{/b}"
            text "> I should go see how Eve's doing in her quarters."
        #Q1t-Q1
        if evemillyquest == 1 and ledricquest == 0:
            text "{b}Eve's Storyline{/b}"
            text "> I need to get some camping gear so that I can go questing with Eve."
            text "> I'll meet her at her quarters afterwards."
        #Q2
        if ledricquest == 1 and evekiss == 0:
            text "{b}Eve's Storyline{/b}"
            text "> I should go to the guild to meet up with Eve."
        #Q3
        if evekiss == 1 and eveknow == 0:
            text "{b}Eve's Storyline{/b}"
            text "> I should go talk with Eve about what happened the other day..."
        #Q4
        if eveknow == 1 and evesex == 0:
            text "{b}Eve's Storyline{/b}"
            text "> Time to tell her how I feel."




        if loriFunValue > 0 and loriDone == False and loriDropped == False:
            text "{b}Lori's Storyline{/b}"
            if loriEventValue < 4:
                text "> Keep studying with Lori."
            if loriEventValue == 4:
                if askedAboutLori == False:
                    text "> I could ask around and find out what's up with Lori..."
                    text "> Even if I don't, I have to apologize."
                else:
                    text "> Now that I know about her father I understand..."
                    text "> Let's go apologize."
            if loriEventValue == 5:
                text "> She likes adventuring so much... What if I take her on a quest?"
                text "> Let's go ask her."
            if loriEventValue == 6:
                text "> Let's ask Gabe if she can take care of the library."
            if loriEventValue == 7:
                text "> Now, when I'm ready, I can take Lori on a quest."
                text "> I should definitely go before it's afternoon, though..."
            if loriEventValue == 8:
                text "> After what happened the other day... Lori definitely likes me."
                text "> I should do the right thing and go talk to her."
            if loriEventValue == 9:
                if loriDateDate > day:
                    text "> Tomorrow afternoon I need to be at the market."
                elif loriDateDate == day and time < 2:
                    text "> This afternoon I've got my date with Lori..."
                    text "> Let's make sure I show up at the market."
                elif loriDateDate == day and time == 2:
                    text "> I need to be quick and get to the market or I'll miss my date!"
                else:
                    text "> ...I've missed the date with Lori."
            if loriEventValue == 10:
                text "> I wonder..."
                text "> ...Will she tell me her true feelings if I go visit her again?"




        if day >= 5 and gabee1 == 0:
            text "{b}Gabe's Storyline{/b}"
            text "> Go to the academy in the afternoon."
        if gabee1 == 1:
            text "{b}Gabe's Storyline{/b}"
            text "> I need to find a history book. I should go to the Library."
        if gabee1 == 2:
            text "{b}Gabe's Storyline{/b}"
            text "> I couldn't find a book in the Library. Lori told me to ask Boris."
        if gabee1 == 3 and didtest == False:
            text "{b}Gabe's Storyline{/b}"
            text "> I should study the books and go to Gabe's house after noon."
        if didtest == True and testDone == False:
            text "{b}Gabe's Storyline{/b}"
            text "> I should wait until the test."
        if testDone == True and level < 10:
            text "{b}Gabe's Storyline{/b}"
            text "> I should focus on levelling up in the Guild."
        if testDone == True and level >= 10 and gabequest2 == 0:
            text "{b}Gabe's Storyline{/b}"
            text "> I think I saw a new quest on the Questboard."
        if gabequest2 == 1 and gabequest3 == 0:
            text "{b}Gabe's Storyline{/b}"
            text "Train Gabe."
        if gabefinger > 2 and gabefingerclass == 0:
            text "{b}Gabe's Storyline{/b}"
            text "> I should go to class. I have a special training for Gabe in mind."
        if gabefingerclass == 1 and dildoi == 0:
            text "{b}Gabe's Storyline{/b}"
            text "> I should buy Gabe a present. Something that will help her with her training."
        if gabedildo >= 3 and gabetrip == 0:
            text "{b}Gabe's Storyline{/b}"
            text "> I should go to Gabe's house after noon."
        if gabequest2 >= 1 and gabequest3 == 0:
            text "{b}???'s Storyline{/b}"
            text "> Go to the Academy."





        if theanight == True and stealthlvl == 0 and TheaMolest == True:
            text "{b}Thea's Storyline{/b}"
            text "> Thea keeps waking up. I need to find a way to do more..."
            text "> Who could I ask for advice on something like this?"
        if findtheaclothes == 1:
            text "{b}Thea's Storyline{/b}"
            text "> I need some clothes for Thea. Who could help me with that?"
            text "> ...Someone from the Academy I guess."
        if thearuntimer > 0 and thearun ==1:
            text "{b}Thea's Storyline{/b}"
            text "> I didn't see Thea around today. I should go check on her."
        if theajob == 1:
            text "{b}Thea's Storyline{/b}"
            text "> I should wait for a few days."
        if theagotjob == 1 and theadogfood == 0:
            text "{b}Thea's Storyline{/b}"
            text "> I should check on Thea."
        if petedinner == 1 and sanderevedinner < 1:
            text "{b}Thea's Storyline{/b}"
            text "> I should tell Thea that I'm inviting Sander and Eve for dinner tonight."
        if sanderpetedinner == 0  and sanderevedinner == 2:
            text "{b}Thea's Storyline{/b}"
            text "> Invite Uncle Pete and Sander for dinner."
        if sanderpetedinner == 2 and theadinner < 2:
            text "{b}Thea's Storyline{/b}"
            text "> I wonder what Thea would think about having a special dinner with me. Ugh... Man up and ask her, [mc]!"
        if theadinner == 3 and theasex == 0:
            text "{b}Thea's Storyline{/b}"
            text "> I should go see Thea at work. The Tavern should be at the Market. Let's go in the evening."
        if theaguildjob < 2 and theasex == 1:
            text "{b}Thea's Storyline{/b}"
            text "> Go to the Guild and ask July if Thea could get a job there."
        if theaguildjob == 2:
            text "{b}Thea's Storyline{/b}"
            text "> Tell Thea she got the job!"
        if theaguildjob == 3 and theaguild == 0:
            text "{b}Thea's Storyline{/b}"
            text "> Let's see how Thea's doing at her new job. Let's go in the evening."




        if sawcynth == 3:
            text "{b}Cynthia's Storyline{/b}"
            text "> I should talk to Cynthia at the Academy."
        if sawcynth >= 6  and party == 1 and cynthquest2 == 0 and savecynth == 1:
            text "{b}Cynthia's Storyline{/b}"
            text "> Go to the Guild in the afternoon."
        if cynthquest2 == 1 and cynthquest3 == 0:
            text "{b}Cynthia's Storyline{/b}"
            text "> I should talk to Cynthia in the afternoon."
        if cynthquest3 == 1 and cynthtrain < 7:
            text "{b}Cynthia's Storyline{/b}"
            text "> I should train with Cynthia after noon."
        if cynthtrain >= 7 and cynthquest4 == 0:
            text "{b}Cynthia's Storyline{/b}"
            text "> Cynthia asked me to come with her on a monster hunt. I should talk to her in the Guild when I'm ready."
        if cynthquest4 == 1 and  cynthquest5 == 0:
            text "{b}Cynthia's Storyline{/b}"
            text "> Today's a good day to go hunting. I should go to the forest."
        if cynthquest5 >= 1 and cynthboots == 0 and  sawjuly >=5:
            text "{b}Cynthia's Storyline{/b}"
            text "> I should check on Cynthia and see if she's doing fine. Better go to the Guild after noon."
        if cynthquest5 >= 1 and cynthboots == 1 and cynthquest6 == 0:
            text "{b}Cynthia's Storyline{/b}"
            text "> Wait a few days."
        if cynthquest6 == 1 and cynthkiss == 0 and savecynthia == 1:
            text "{b}Cynthia's Storyline{/b}"
            text "> Go to the Academy."
        if cynthquest6 == 1 and cynthkiss == 0 and savecynthia == 0 and cynthmemloss == 0:
            text "{b}Cynthia's Storyline{/b}"
            text "> Go to the Academy."
        if cynthkiss >= 1 and cynthdate == 0:
            text "{b}Cynthia's Storyline{/b}"
            text "> I've got a date with Cynthia! I should talk to her at the Guild when I'm ready."
        if sawjuly <5 and cynthquest5 >= 1:
            text "{b}Cynthia's Storyline{/b}"
            text "> Progress in July's Storyline."




        if cynthdate >= 1 and thcynthconfess == 0 and theasex > 0:
            text "{b}Thea and Cynthia's Storyline{/b}"
            text "> I should tell Thea about Cynthia one of these nights."
        if thcynthconfess == 1:
            text "{b}Thea and Cynthia's Storyline{/b}"
            text "> I should confess to Cynthia too."
        if thcynthconfess == 2:
            text "{b}Thea and Cynthia's Storyline{/b}"
            text "> Go to the Guild before it's evening."
        if thcynthconfess == 3 and thcynthconfesstimer < 3:
            text "{b}Thea and Cynthia's Storyline{/b}"
            text "> Wait a few days and then go to the Guild in the evening."
        if thcynthconfess == 3 and thcynthconfesstimer >= 3:
            text "{b}Thea and Cynthia's Storyline{/b}"
            text "> Go to the Guild in the evening."
        if thcynthconfess == 4:
            text "{b}Thea and Cynthia's Storyline{/b}"
            text "> Go to the Guild before night."


        if gabequest3 >= 1 and TaliyaQ < 1:
            text "{b}???'s Storyline{/b}"
            text "> There's a new quest on the Questboard."
        if TaliyaQ == 1:
            text "{b}Taliya's Storyline{/b}"
            text "> I should go train with my sword at the Arena."
        if TaliyaQ == 2:
            text "{b}Taliya's Storyline{/b}"
            text "> I should go to the Market every once in a while."
        if TaliyaQ == 3 and penepisellosessoomosessuale == False:
            text "{b}Taliya's Storyline{/b}"
            text "> I should go to the Arena in the morning."
        if TaliyaQ == 3 and penepisellosessoomosessuale == True:
            text "{b}Taliya's Storyline{/b}"
            text "> Go to the Market in the morning."
        if TaliyaQ == 4 and t4qt > day and Q4Pre == False:
            text "{b}Taliya's Storyline{/b}"
            text "> Wait a few days and then go talk to Taliya at the Academy."
        if TaliyaQ == 4 and t4qt <= day and Q4Pre == False:
            text "{b}Taliya's Storyline{/b}"
            text "> I should go talk to Taliya at the Academy."
        if Q4Pre == True and TaliyaQ == 4:
            text "{b}Taliya's Storyline{/b}"
            text "> Go to Market in the morning."
        if dayTQ5 == day+2:
            text "{b}Taliya's Storyline{/b}"
            text "> I should rest for today."
        if dayTQ5 == day+1:
            text "{b}Taliya's Storyline{/b}"
            text "> I have got to go to the Market tomorrow morning."
        if dayTQ5 >= day and time == 0 and TaliyaQ == 5:
            text "{b}Taliya's Storyline{/b}"
            text "> I need to go to the Market or Taliya will go without me."
        if TaliyaQ == 6 and Taliya6Talk == False:
            text "{b}Taliya's Storyline{/b}"
            text "> I should go to the Arena at the Academy."
        if TaliyaQ == 6 and Taliya6Talk == True and time == 3:
            text "{b}Taliya's Storyline{/b}"
            text "> Let's head to the Guild and go to the barracks from there."
        elif TaliyaQ == 6 and Taliya6Talk == True:
            text "{b}Taliya's Storyline{/b}"
            text "> I should go to the Guild in the evening so that I can go to the barracks from there."



        if zenQ == 1 and dayZ == 0:
            text "{b}Zenelith's Storyline{/b}"
            text "> I should go and ask Uncle Pete if he has tools tomorrow."
        if zenQ == 1 and dayZ >= 1:
            text "{b}Zenelith's Storyline{/b}"
            text "> I should ask Uncle Pete for some tools to repair the Shack."
        if zenQ == 2 and furnitureZ == False:
            text "{b}Zenelith's Storyline{/b}"
            text "> I should buy a table and some chairs for Zenelith's shack."
        if zenQ == 2 and Zdress == False:
            text "{b}Zenelith's Storyline{/b}"
            text "> I should buy Zenelith a dress."
        if zenQ == 2 and Zdress == True and furnitureZ == True:
            text "{b}Zenelith's Storyline{/b}"
            text "> I've got everything, time to visit Zenelith."
        if zenQ == 3:
            text "{b}Zenelith's Storyline{/b}"
            text "> Go visit Zenelith."
        if zenQ == 4:
            text "{b}Zenelith's Storyline{/b}"
            text "> Go visit Zenelith."
        if zenQ == 5:
            text "{b}Zenelith's Storyline{/b}"
            text "> Zenelith was a bit down, maybe I should pay her a visit."
        if zenQ == 6:
            text "{b}Zenelith's Storyline{/b}"
            text "> Go visit Zenelith in the morning."


        if zenS == 1:
            text "{b}Zenelith's Storyline{/b}"
            if (zd1 == True) or  (zd2 == True) or  (zd3 == True) or (zd4 == True):
                text "> Let's go see if Zenelith has calmed down."
            else:
                text "> Let's go check on Zenelith."
        if zenS > 1 and zenS < 5:
            text "{b}Zenelith's Storyline{/b}"
            text "> Go feed her until she understands who's boss."
        if zenS == 5 and asked4gift == False:
            text "{b}Zenelith's Storyline{/b}"
            text "> Talk with Zenelith."
        if zenS == 5 and asked4gift == True and gaveZBag == False:
            text "{b}Zenelith's Storyline{/b}"
            text "> Get the books, the bed and Zenelith's bag and then bring them to the shack."
        if zenS == 5 and gaveZBag == True:
            text "{b}Zenelith's Storyline{/b}"
            text "> Go back to the shack."
        if zenS == 6:
            text "{b}Zenelith's Storyline{/b}"
            if zentimer == 0:
                text "> Go visit Zenelith again."
            elif zentimer < 0:
                text "> I need to visit Zenelith again, I've left her alone too long."
            else:
                text "> Wait [zentimer] more days."
        if zenS == 7 and analDone == False:
            text "{b}Zenelith's Storyline{/b}"
            text "> I can finally use her as much as I want now."
            text "> Maybe if I try hard enough I could get her to do something more..."




    imagebutton:
        xpos 1
        ypos 1
        idle "journalbackscrn"
        hover "journalbackscrn1"
        action Hide("screenjournal"), Show("hud")
