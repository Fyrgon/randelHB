screen screenmap():
    if time < 3:
        image ("mapbaseTEST.webp")
    elif time == 3:
        image ("mapbasee.webp")
    else:
        image ("mapbasenightTEST.webp")


    if time < 3:
        imagebutton:
            xalign 0.619
            yalign 0.043
            idle "MAPlibrary.webp"
            hover "MAPlibraryLIT.webp"
            activate_sound "hover.mp3"
            action Jump("library")
            tooltip _("{color=#fff}Library")
        imagebutton:
            xalign 0.829
            yalign 0.481
            idle "MAPadguild.webp"
            hover "MAPadguildLIT.webp"
            activate_sound "hover.mp3"
            action Jump("guild")
            tooltip _("{color=#fff}Adventurers' Guild")
        imagebutton:
            xalign 0.599
            yalign 0.587
            idle "MAPmervinhut.webp"
            hover "MAPmervinhutLIT.webp"
            activate_sound "hover.mp3"
            action Jump("store")
            tooltip _("{color=#fff}Mervin's Shop")
        imagebutton:
            xalign 0.573
            yalign 0.4
            idle "MAPgabehouse.webp"
            hover "MAPgabehouseLIT.webp"
            activate_sound "hover.mp3"
            action Jump("gabehouse")
            tooltip _("{color=#fff}Gabe's House")
        imagebutton:
            xalign 0.0001
            yalign 0.0001
            idle "MAPacademy.webp"
            hover "MAPacademyLIT.webp"
            activate_sound "hover.mp3"
            action Jump("academy")
            tooltip _("{color=#fff}Academy")
        imagebutton:
            xalign 0.69
            yalign 0.82
            idle "MAPmchouse.webp"
            hover "MAPmchouseLIT.webp"
            activate_sound "hover.mp3"
            action Jump("home")
            tooltip _("{color=#fff}Home")
        imagebutton:
            xalign 0.984
            yalign 0.09
            idle "MAPpetehouse.webp"
            hover "MAPpetehouseLIT.webp"
            activate_sound "hover.mp3"
            action Jump("fishhut")
            tooltip _("{color=#fff}Pete's Hut")
        imagebutton:
            xalign 0.0001
            yalign 0.9999
            idle "MAPforest.webp"
            hover "MAPforestLIT.webp"
            activate_sound "hover.mp3"
            action Jump("forest")
            tooltip _("{color=#fff}Forest")
        imagebutton:
            xalign 0.0275
            yalign 0.605
            idle "MAPmarket.webp"
            hover "MAPmarketLIT.webp"
            activate_sound "hover.mp3"
            action Jump("market")
            tooltip _("{color=#fff}Central Market")

    elif time == 3:
        imagebutton:
            xalign 0.619
            yalign 0.043
            idle "MAPlibrarye.webp"
            hover "MAPlibraryeLIT.webp"
            activate_sound "hover.mp3"
            action Jump("library")
            tooltip _("{color=#fff}Library")
        imagebutton:
            xalign 0.829
            yalign 0.481
            idle "MAPadguilde.webp"
            hover "MAPadguildeLIT.webp"
            activate_sound "hover.mp3"
            action Jump("guild")
            tooltip _("{color=#fff}Adventurers' Guild")
        imagebutton:
            xalign 0.599
            yalign 0.587
            idle "MAPmervinhute.webp"
            hover "MAPmervinhuteLIT.webp"
            activate_sound "hover.mp3"
            action Jump("store")
            tooltip _("{color=#fff}Mervin's Shop")
        imagebutton:
            xalign 0.573
            yalign 0.4
            idle "MAPgabehousee.webp"
            hover "MAPgabehouseeLIT.webp"
            activate_sound "hover.mp3"
            action Jump("gabehouse")
            tooltip _("{color=#fff}Gabe's House")
        imagebutton:
            xalign 0.0001
            yalign 0.0001
            idle "MAPacademye.webp"
            hover "MAPacademyeLIT.webp"
            activate_sound "hover.mp3"
            action Jump("academy")
            tooltip _("{color=#fff}Academy")
        imagebutton:
            xalign 0.69
            yalign 0.82
            idle "MAPmchousee.webp"
            hover "MAPmchouseeLIT.webp"
            activate_sound "hover.mp3"
            action Jump("home")
            tooltip _("{color=#fff}Home")
        imagebutton:
            xalign 0.984
            yalign 0.09
            idle "MAPpetehousee.webp"
            hover "MAPpetehouseeLIT.webp"
            activate_sound "hover.mp3"
            action Jump("fishhut")
            tooltip _("{color=#fff}Pete's Hut")
        imagebutton:
            xalign 0.0001
            yalign 0.9999
            idle "MAPforeste.webp"
            hover "MAPforesteLIT.webp"
            activate_sound "hover.mp3"
            action Jump("forest")
            tooltip _("{color=#fff}Forest")
        imagebutton:
            xalign 0.0275
            yalign 0.605
            idle "MAPmarkete.webp"
            hover "MAPmarketeLIT.webp"
            activate_sound "hover.mp3"
            action Jump("market")
            tooltip _("{color=#fff}Central Market")


    else:
        imagebutton:
            xalign 0.619
            yalign 0.043
            idle "MAPlibraryn.webp"
            hover "MAPlibrarynLIT.webp"
            activate_sound "hover.mp3"
            action Jump("library")
            tooltip _("{color=#fff}Library")
        imagebutton:
            xalign 0.829
            yalign 0.481
            idle "MAPadguildn.webp"
            hover "MAPadguildnLIT.webp"
            activate_sound "hover.mp3"
            action Jump("guild")
            tooltip _("{color=#fff}Adventurers' Guild")
        imagebutton:
            xalign 0.0275
            yalign 0.605
            idle "MAPmarketn.webp"
            hover "MAPmarketnLIT.webp"
            activate_sound "hover.mp3"
            action Jump("market")
            tooltip _("{color=#fff}Mervin's Shop")
        imagebutton:
            xalign 0.573
            yalign 0.4
            idle "MAPgabehousen.webp"
            hover "MAPgabehousenLIT.webp"
            activate_sound "hover.mp3"
            action Jump("gabehouse")
            tooltip _("{color=#fff}Gabe's House")
        imagebutton:
            xalign 0.0001
            yalign 0.0001
            idle "MAPacademyn.webp"
            hover "MAPacademynLIT.webp"
            activate_sound "hover.mp3"
            action Jump("academy")
            tooltip _("{color=#fff}Academy")
        imagebutton:
            xalign 0.69
            yalign 0.82
            idle "MAPmchousen.webp"
            hover "MAPmchousenLIT.webp"
            activate_sound "hover.mp3"
            action Jump("home")
            tooltip _("{color=#fff}Home")
        imagebutton:
            xalign 0.984
            yalign 0.09
            idle "MAPpetehousen.webp"
            hover "MAPpetehousenLIT.webp"
            activate_sound "hover.mp3"
            action Jump("fishhut")
            tooltip _("{color=#fff}Pete's Hut")
        imagebutton:
            xalign 0.0001
            yalign 0.9999
            idle "MAPforestn.webp"
            hover "MAPforestnLIT.webp"
            activate_sound "hover.mp3"
            action Jump("forest")
            tooltip _("{color=#fff}Forest")
        imagebutton:
            xalign 0.599
            yalign 0.587
            idle "MAPmervinhutn.webp"
            hover "MAPmervinhutnLIT.webp"
            activate_sound "hover.mp3"
            action Jump("store")
            tooltip _("{color=#fff}Central Market")

    $ tooltip = GetTooltip()

    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top False
            frame:
                xalign 0.5
                text tooltip
