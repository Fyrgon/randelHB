init python:

    ### CONFIG ###
    # file extension of the CGs, used in creating automatic thumbnails
    cg_format = ".webp"
    # path to CGs
    cg_path = "images/"
    # number of columns of thumbnails in the gallery grid
    max_x = 3
    # number of rows of thumbnails in the gallery grid
    max_y = 3
    # this will be the width of the thumbnails, height will be calculated automatically for 16:9 aspect ratio thumbnails
    # recommended sizes:
    # 290 for 1280x720 resolution
    # 400 for 1920x1080 resolution
    thumbnail_x = 290
    ### END OF CONFIG ###

    max_page = max_x * max_y
    thumbnail_y = int(thumbnail_x * 0.5625) # to change the aspect ratio from 16:9 to 4:3, change the value in formula to 0.75
    gallery_resolution_scaling = config.screen_width / 1280.0
    gallery_navigation_width = int(290 * gallery_resolution_scaling)
    gallery_page = 0
    gallery_items = []
    ga = Gallery()
    ga.transition = dissolve
    ga.locked_button = im.Scale("images/gallery_overlay/gallery_locked.webp",thumbnail_x,thumbnail_y)

    # A class for gallery items (no need to change anything here)
    # when creating a GalleryItem object, provide images in a list, you can put more than one to have more images displayed consecutively after another under one button
    # if no thumbnail is provided as the 3rd argument, it will be built automatically from the 1st image in 16:9 aspect ratio
    # alternatively the path to the custom thumbnail can be provided as the 3rd argument during object creation
    class GalleryItem:
        def __init__(self, name, images, thumb=None):
            self.name = name
            self.images = images
            if thumb is None:
                self.thumb = im.Scale(cg_path+images[0]+cg_format,thumbnail_x,thumbnail_y)
            else:
                self.thumb = im.Scale(thumb,thumbnail_x,thumbnail_y)

        def num_images(self):
            return len(self.images)

image gallery_idle_overlay = im.Scale("images/gallery_overlay/gallery_idle_overlay.webp",thumbnail_x,thumbnail_y)
image gallery_background_overlay:
    "images/gallery_overlay/gallery_background_overlay.webp"
    zoom gallery_resolution_scaling

screen gallery():

    python:
        if len(gallery_items) == 0:
            ### CGs ###
            if persistent.scarLocker == True:
                gallery_items.append(GalleryItem("Sleeping Mage", ["sleepm", "sleepm2"]))
            if persistent.stareCynthia == True:
                gallery_items.append(GalleryItem("Staring Cynthia", ["stare"]))
            if persistent.peekingTime == True:
                gallery_items.append(GalleryItem("Peeking Time", ["bathescene1", "bathescene2", "bathescene3", "bathescene4", "bathescene5", "bathescene6", "bathescene8", "bathescene7",]))
            if persistent.nadiaBlowjob == True:
                gallery_items.append(GalleryItem("Nadia's Blowjob", ["nadia", "nadiasuck1", "nadiasuck2", "nadiasuck3", "nadiasuckcumout1", "nadiasuckcumout2", "nadiasuckcumin1", "nadiasuckcumin2"]))
            if persistent.nadiaLick == True:
                gallery_items.append(GalleryItem("Licking Nadia", ["nadialick1", "nadialick2", "nadialick3"]))
            if persistent.studying == True:
                gallery_items.append(GalleryItem("Chit chat with Gabe", ["studygabe1", "studygabe2"]))
####MISC STUFF
            if persistent.peteStargazing == True:
                gallery_items.append(GalleryItem("Watching the Stars", ["petestargaze"]))
            if persistent.bronzeParty == True:
                gallery_items.append(GalleryItem("Promotion Party", ["bronzeparty"]))
            if persistent.eveBath == True:
                gallery_items.append(GalleryItem("Evelyn Bathing", ["evebathe1", "evebathe2"]))
            if persistent.scenery == True:
                gallery_items.append(GalleryItem("Randel", ["end"]))
            if persistent.yakina == True:
                gallery_items.append(GalleryItem("Unknown Demon Girl", ["yakina"]))
            if persistent.testDone == True:
                gallery_items.append(GalleryItem("The Test", ["testgabe1"]))
####GABE STUFF
            #if persistent.gabeBondage == True:
            #    gallery_items.append(GalleryItem("Tied Gabe", ["gabebond2"]))
            if persistent.gabeSleep == True:
                gallery_items.append(GalleryItem("Sleeping Together", ["gabesleep1"]))
            if persistent.gabeFingering == True:
                gallery_items.append(GalleryItem("Fingering Gabe", ["gabefingerbase1", "animationgabefinger"]))
            if persistent.gabeDildo == True:
                gallery_items.append(GalleryItem("Gabe's Dildo", ["gabefingerbase1", "animationgabedildo", "gabecum"]))
            if persistent.gabeHandjob == True:
                gallery_items.append(GalleryItem("Gabe's Handjob", ["hjgabe", "gabehjSlow", "gabehjFast", "gabehjCum", "hjgabecum1"]))
            if persistent.gabePicnic == True:
                gallery_items.append(GalleryItem("Outdoors Sex with Gabe", ["gabesexcum", "gabesex movie"]))
            if persistent.gabeDoggy == True:
                gallery_items.append(GalleryItem("Doggy Style with Gabe", ["gabesexcum2", "gabesexanime2 movie"]))
            if persistent.gabeMissionary == True:
                gallery_items.append(GalleryItem("Missionary with Gabe", ["gabemissionary1", "animationgabemissionary"]))
            if persistent.taliyaGoblins == True:
                gallery_items.append(GalleryItem("Taliya fights the Goblins", ["goblinfighttalia", "goblintalia"]))
            if persistent.goblinBarrel == True:
                gallery_items.append(GalleryItem("Goblin Kids", ["goblinkid1", "goblinkid2"]))
####CYNTHIA STUFF
            if persistent.abandonCynthia == True:
                gallery_items.append(GalleryItem("Left Cynthia", ["cynthiaba1", "cynthiaba2", "cynthiaba3", "cynthiaba4"]))
            if persistent.saveCynthia == True:
                gallery_items.append(GalleryItem("Didn't leave Cynthia", ["cynthiaba1", "cynthiaba4", "cynthiaba4"]))
            if persistent.cynthCovers == True:
                gallery_items.append(GalleryItem("Cynthia Covers Herself", ["cynthsu"]))
            if persistent.cynthiaTent == True:
                gallery_items.append(GalleryItem("Sleeping in a Tent with Cynthia", ["sleepcynthia1", "sleepcynthia2", "sleepcynthia4", "sleepcynthia3","sleepcynthia4", ]))
            if persistent.globDeath == True:
                gallery_items.append(GalleryItem("Cynthia stabs a monster in the eye", ["glob1", "glob2", "glob3"]))
            if persistent.cynthiaFirstDate == True:
                gallery_items.append(GalleryItem("Cafe Date", ["cynthiadate2", "cynthiadate3", "cynthiadate1"]))
            if persistent.cynthiaTraining == True:
                gallery_items.append(GalleryItem("Resting after Training", ["restcynthia"]))
            if persistent.direWolf == True:
                gallery_items.append(GalleryItem("The Dire Wolf", ["direwolf", "direwolf1"]))
            if persistent.cynthFireplace == True:
                gallery_items.append(GalleryItem("Talking at the Fireplace", ["cynthiatalk3", "cynthiatalk2", "cynthiatalk4", "cynthiatalk1"]))
            if persistent.cynthMCFight == True:
                gallery_items.append(GalleryItem("Fighting with Cynthia", ["cynthmcfight"]))
            if persistent.savedCynthBandit == True:
                gallery_items.append(GalleryItem("Saving Cynthia", ["mcsavecynth"]))
            if persistent.cynthWatchingOver == True:
                gallery_items.append(GalleryItem("Cynthia Watching over you", ["cynthbed2", "cynthbed1"]))
            if persistent.cynthVampire == True:
                gallery_items.append(GalleryItem("July saving Cynthia", ["julysave1", "julysave2", "julysaveblood"]))
            if persistent.ears == True:
                gallery_items.append(GalleryItem("Cynthia's Collection", ["ears"]))
            if persistent.cynthStrip == True:
                gallery_items.append(GalleryItem("Cynthia Stripping", ["cynthstrip"]))
            if persistent.cynthFirstTime == True:
                gallery_items.append(GalleryItem("Cynthia's First Time", ["cynthsex1", "cynthsex21", "cynthsex3", "cynthsex4", "cynthsexanim movie", "cynthsexanimf movie", "cynthsexcumin", "cynthsexcumout"]))
####THEA STUFF
            if persistent.theaRape == True:
                gallery_items.append(GalleryItem("Thea's Rape", ["thearape1", "animationrapethea", "thearape4", "thearapekill"]))
            if persistent.theaBed == True:
                gallery_items.append(GalleryItem("Waking Thea", ["theabed1", "theabed2"]))
            if persistent.theaGrave == 1:
                gallery_items.append(GalleryItem("Thea at the Graves", ["theagrave1"]))
            elif persistent.theaGrave == 2:
                gallery_items.append(GalleryItem("Thea at the Graves", ["theagrave1", "theagrave2"]))
            if persistent.theaCleaning == True:
                gallery_items.append(GalleryItem("Thea Cleaning", ["theaclean"]))
            if persistent.theaGabe1 == True:
                gallery_items.append(GalleryItem("Surprive visit from Gabe", ["theagabe1", "theagabe2"]))
            if persistent.theaDoge == True:
                gallery_items.append(GalleryItem("Thea Cooking", ["theacook1"]))
                gallery_items.append(GalleryItem("Thea Doge", ["theadog1", "theadog2"]))
            if  persistent.theaNakedSleep == True:
                gallery_items.append(GalleryItem("Naked sleeping Thea", ["sleeptheabase"]))
            #if persistent.X == True:
            #    gallery_items.append(GalleryItem("X", ["X"]))
            #if persistent.X == True:
            #    gallery_items.append(GalleryItem("X", ["X"]))
            #if persistent.X == True:
            #    gallery_items.append(GalleryItem("X", ["X"]))
            if persistent.theaFirstTime == True:
                gallery_items.append(GalleryItem("Thea's Stare", ["theastare1", "theastare2"]))
                gallery_items.append(GalleryItem("Thea's First Time", ["theas1", "theas2", "theas3", "theas movie", "theas2 movie", "theascum"]))
####ELF VILLAGE STUFF
            if persistent.followedEve == True:
                gallery_items.append(GalleryItem("Following Eve", ["evestalk"]))
            if persistent.millyEve == True:
                gallery_items.append(GalleryItem("Elven Reunion", ["evemilly"]))
            if persistent.priestShow == True:
                gallery_items.append(GalleryItem("The Elf Priestess", ["elfpriestshow"]))
            if persistent.aerinDead == True:
                gallery_items.append(GalleryItem("Aerin's Death", ["aerindead"]))
            if persistent.zenelithDefeated == True:
                gallery_items.append(GalleryItem("Rescue Mission", ["priesthouse", "doorpriest1", "doorpriest3", "priestjail", "slave1", "slave2", "elfpreistback", "elfpreistback2"]))
            if persistent.zenelithRape == True:
                gallery_items.append(GalleryItem("Teaching her a lesson", ["priestsexcum1", "priestr movie"]))
####NESSA STUFF
            if persistent.nessaPantyless == True:
                gallery_items.append(GalleryItem("Nessa ain't got Panties", ["nessahot1", "nessahot2"]))
            if persistent.nessaBlowjob == True:
                gallery_items.append(GalleryItem("Nessa's Blowjob", ["jail", "nessabj movie", "nessabjcum"]))
            if persistent.sexNessa == True:
                gallery_items.append(GalleryItem("Screwing Nessa", ["nessasexstart", "nessasex movie", "nessacum", "nessasex2", "nessacum", "nessasexstart"]))
####AERIN STUFF
            if persistent.aerinTea == True:
                gallery_items.append(GalleryItem("Aerin's tea", ["teaaerin", "teaaerin2"]))
            if persistent.aerinKiss == True:
                gallery_items.append(GalleryItem("Aerin's First Kiss", ["mcak1", "mcak2", "mcak3"]))
            if persistent.aerinLickies == True:
                gallery_items.append(GalleryItem("Aerin's Cunnilingus", ["aerinasslick1", "aerinasslicka1", "aerinasslicka2", "aerinasslicka3", "aerinasslicka4", "aerinasslicka6", "aerinasslicka7"]))
            if persistent.aerinSex == True:
                gallery_items.append(GalleryItem("Making Love to Aerin", ["aerinsex1", "aerinsex2", "aerinsexfinal movie", "aerinsexcum"]))
            if persistent.helpAerin == True:
                gallery_items.append(GalleryItem("Helping Aerin", ["highelfroom", "aerinworkhelp"]))
####ZENELITH STUFF
            if persistent.introZen == True:
                gallery_items.append(GalleryItem("Zenelith on the Ground", ["zenelithdown"]))
                gallery_items.append(GalleryItem("Zenelith grabs your hand", ["zenelithhelp"]))
            if persistent.zenMurders == True:
                gallery_items.append(GalleryItem("Zenelith gets Revenge", ["znmcsmash"]))
            if persistent.zenRepaired == True:
                gallery_items.append(GalleryItem("Fixing the Shack", ["shackbuild"]))
            if persistent.zenPeek == True:
                    if persistent.zenPeek2 == True:
                        gallery_items.append(GalleryItem("Zenelith undressing", ["znchange1", "znchange2", "znchange3"]))
                    else:
                        gallery_items.append(GalleryItem("Zenelith undressing", ["znchange1", "znchange2"]))
            if persistent.zenHeal == True:
                gallery_items.append(GalleryItem("Zenelith heals you", ["zenelithmcheal2"]))
            if persistent.zenDirewolf == True:
                gallery_items.append(GalleryItem("Zenelith saves Eve", ["zendirewolves", "zenelithpowerf"]))
            if persistent.zenTroll == True:
                gallery_items.append(GalleryItem("Troll Quest", ["troll", "troll2", "troll3", "troll4"]))
            if persistent.zenGoodEnd == True:
                gallery_items.append(GalleryItem("Zenelith's Kiss", ["zenkiss"]))
                gallery_items.append(GalleryItem("Zenelith's Lovemaking session", ["zenelithsexrani", "zenelith movie", "zenelithsexc3", "zenelithsexc4"]))
####TALIYA STUFF
            if persistent.Taliya1 == True:
                gallery_items.append(GalleryItem("Gang of Thugs", ["gang1", "gang2"]))
                gallery_items.append(GalleryItem("Airi's Blowjob", ["mcl", "mclsuck"]))
                gallery_items.append(GalleryItem("Taliya's Wrath", ["taliyagangkill", "mcknifepoint", "mcknifepoint2", "mcknifepoint3", "emptyredroom"]))
                gallery_items.append(GalleryItem("Taliya drinks with you", ["taliyadrink"]))
            if persistent.Taliya2 == True:
                gallery_items.append(GalleryItem("Scary Taliya", ["taliyacreepy"]))
            if persistent.Taliya3 == True:
                gallery_items.append(GalleryItem("Taliya's Cart", ["taliyacart1", "taliyacart2"]))
                gallery_items.append(GalleryItem("Karnak", ["karnak", "karnakspire"]))
                gallery_items.append(GalleryItem("Karnak door guard", ["doorman1", "doorman2", "taliyaflash"]))
                gallery_items.append(GalleryItem("BDSM Taliya", ["taliyabondage1", "taliyabondage2", "taliyabondage3", "taliyabondage4", "taliyabondage4b", "taliyabondage5", "taliyabondage6", "taliyabondaged3", "taliyabondageend", "taliyabondageend2"]))
                gallery_items.append(GalleryItem("Leon", ["pervcloseup", "pervtorture1", "pervtorture2", "pervtorture3"]))
                if persistent.TaliyaNecklace == True:
                    gallery_items.append(GalleryItem("Taliya's necklace", ["taliyanecklace"]))
            if persistent.Taliya4 == True:
                gallery_items.append(GalleryItem("Exploring the Dump", ["darkcave", "corpse"]))
                gallery_items.append(GalleryItem("Demon Cultists in Karnak", ["demoncultist1", "demoncultist2", "taliyaminotaur", "cultistattack1"]))
                gallery_items.append(GalleryItem("Drugged Taliya", ["taliyadrugedchair", "taliyadruged"]))
                gallery_items.append(GalleryItem("Talya Grinding", ["taliyagrind0", "taliyagrindanim"]))
            if persistent.Taliya5 == True:
                gallery_items.append(GalleryItem("Twig's death", ["twigdeath"]))
            if persistent.Taliya6 == True:
                gallery_items.append(GalleryItem("Taliya drinking game", ["drinkgame"]))
                gallery_items.append(GalleryItem("Taliya farwell party", ["taliyaparty"]))
                gallery_items.append(GalleryItem("Taliya Blowjob", ["taliyablowjob"]))
                gallery_items.append(GalleryItem("Taliya Extra", ["taliyasexanimcumout1", "taliyasex", "taliyasexanimcumout2"]))
            if persistent.Taliya6fem == True:
                gallery_items.append(GalleryItem("Taliya Thighjob", ["taliyathighjob1", "taliyathighjob", "taliyathighjobfast"]))
            if persistent.Taliya6dom == True:
                gallery_items.append(GalleryItem("Taliya Waxplay", ["taliyawax1", "taliyawax2", "taliyawax3", "taliyawax4", "taliyawax5", "taliyawax6"]))
####SIDE STUFF
            if persistent.acidTrip == True:
                gallery_items.append(GalleryItem("Imaginary Sex", ["scarsex1", "scarsex2", "scarsex3"]))
            if persistent.trissStare == True:
                gallery_items.append(GalleryItem("Triss' Stare", ["trisstare"]))
            if persistent.trissFlash == True:
                gallery_items.append(GalleryItem("Triss' Flashing her Rack", ["flashtrissend", "animationtriss"]))
            if persistent.sneakyMegan == True:
                gallery_items.append(GalleryItem("Megan is Sneaky", ["sneak1", "sneak2", "sneak3", "sneak5", "sneak6", "sneak7", "megansword", "megan berserk", "sneakend", "meganberserk"]))
####END STUFF
            if persistent.pt1End == True:
                gallery_items.append(GalleryItem("Yakina's appearance", ["yakinapete1", "mcpetedeath", "mctrans1", "mctrans4", "mctrans5"]))
                gallery_items.append(GalleryItem("First fight with Yakina", ["petehouse1", "petehouse2", "mcrage", "scarmajic"]))
                gallery_items.append(GalleryItem("Young Yakina", ["yakinakid1", "yakinakid2"]))
                gallery_items.append(GalleryItem("Scarlet's Story", ["scars1", "scars3", "scars6", "scars2", "scars4"]))
                gallery_items.append(GalleryItem("Scarlet sitting next to you", ["backscar", "backscar2", "backscar3"]))
                gallery_items.append(GalleryItem("Yakina hacks your Mind", ["yakinaend"]))
                gallery_items.append(GalleryItem("Uncle Pete's grave", ["petegrave"]))
                gallery_items.append(GalleryItem("The End (for now!)", ["end"]))

            for item in gallery_items:
                ga.button(item.name)
                for img in item.images:
                    ga.image(img)


        start = gallery_page * max_page
        end = min(start + max_page - 1, len(gallery_items) - 1)


    ### Layout ###
    tag menu
    style_prefix "game_menu"
    add im.Blur(gui.main_menu_background, 1.5)
    add "gui/main_menu.png"
    if patreonVersion == True:
        add "gui/P_gallery_buttons.png"
    else:
        add "gui/gallery_buttons.png"
    add "gallery_background_overlay"

    hbox:
        vbox:
            style_prefix "navigation"
            yalign 0.9
            xsize gallery_navigation_width
            xpos gui.navigation_xpos
            spacing gui.navigation_spacing

            if patreonVersion == True:
                textbutton "Unlock All":
                    action Function(galleryUnlock)
            textbutton "Previous":
                if gallery_page > 0:
                    action SetVariable("gallery_page", gallery_page - 1)
            textbutton "Next":
                if (gallery_page + 1) * max_page < len(gallery_items):
                    action SetVariable("gallery_page", gallery_page + 1)
            textbutton "Return" action Return()

        grid max_x max_y:
            xfill True
            yfill True
            for i in range(start, end + 1):
                $ item = gallery_items[i]
                add ga.make_button(item.name, item.thumb, idle_border="gallery_idle_overlay", xalign=0.5, yalign=0.5)
            for i in range(end - start + 1, max_page):
                null
