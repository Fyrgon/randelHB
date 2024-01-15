label sleepvars:
    if thcynthconfess == 3:
        $ thcynthconfesstimer += 1

    if cynthboots >= 1:
        $ cynthtimer += 1

    if studygabe2 == 1 and testdone == 0:
        $ testtimer += 1

    if nessaquest == 1:
        $ nessaquesttimer += 1

    if evelost == 1:
        $ evelosttimer += 1

    if aerinlost:
        $ aerinlosttimer += 1

    if eveduel == 1:
        $ evedueltimer -= 1

    if sequest1 == 1:
        $ evetimer += 1

    if aquest2 == 2:
        $ waitthea += 1

    if thearun == 1:
        $ thearuntimer += 1

    if theajob == 1:
        $ theajobtimer += 1

    if theaclothestimer == 1:
        $ theaclothestimerstart += 1

    if gotpunchedtriss == 1:
        $ punchtriss -= 1

    if zenQ == 1:
        $ dayZ += 1
    if zenS >= 1:
        $ lastAte += 1

    if zenS == 6:
        $ zentimer -= 1

    $ day += 1
    $ time = 0

    if evedueltimer == 0:
        jump elfduel

    $ zenSexDone = False
