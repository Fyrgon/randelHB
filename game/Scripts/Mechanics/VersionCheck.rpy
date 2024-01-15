default Cheats = False
default timidMC = False
default boldMC = False
default normalMC = False

label versionCheck:
    if (version == 141+2023090415) or (version == 141+0415):
        $ version = 141.1
    if version < 143:

        if version < 141.1:
            if timidMC == True:
                $ mcTimid == True
            if boldMC == True:
                $ mcBold = True
            if normalMC == True:
                $ mcNormal = True

            if version < 141:
                if Cheats == 1:
                    $ easyMode = True
                if level >= 15:
                    $ level = 15
                if swordlvl >= 15:
                    $ swordlvl = 15
                if bowlvl >= 15:
                    $ bowlvl = 15
                if magiclvl >= 15:
                    $ magiclvl = 15

                if version < 130:
                    if sawelfvillage == 0:
                        $ sawelfvillage = False
                    if sawelfvillage >= 1:
                        $ sawelfvillage = True
    $ version = 143
    jump home2
