screen mainmenubuttons():
    default lastsave = renpy.newest_slot(r"\d+")

    if lastsave is not None:
        vbox:
            xpos 0.217
            yalign 0.515
            textbutton "{b}Restart":
                text_style "menuz"
                action Start()
        vbox:
            xpos 0.307
            yalign 0.515
            textbutton "{b}Continue":
                text_style "menuz"
                action FileLoad(lastsave, slot=True)

    elif lastsave is None:
        vbox:
            xpos 0.247
            yalign 0.51
            textbutton "{b}Start":
                text_style "menuz"
                action Start()
    vbox:
        xpos 0.2475
        yalign 0.56
        textbutton "{b}Load":
            text_style "menuz"
            action ShowMenu("load")
    vbox:
        xpos 0.26
        yalign 0.61
        textbutton "{b}Options":
            text_style "menuz"
            action ShowMenu("options")
    vbox:
        xpos 0.257
        yalign 0.661
        textbutton "{b}Gallery":
            text_style "menuz"
            action ShowMenu("gallery")
    vbox:
        xpos 0.258
        yalign 0.712
        textbutton "{b}Credits":
            text_style "menuz"
            action ShowMenu("about")

    if renpy.variant("pc"):
            vbox:
                xpos 0.265
                yalign 0.765
                ## Help isn't necessary or relevant to mobile devices.
                textbutton "{b}Controls":
                    text_style "menuz"
                    action ShowMenu("help")
            vbox:
                xpos 0.248
                yalign 0.813
                ## The quit button is banned on iOS and unnecessary on Android.
                textbutton "{b}Quit":
                    text_style "menuz"
                    action Quit(confirm=not main_menu)
