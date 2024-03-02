screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("{b}Start") action Start()

        else:

            textbutton _("{b}History") action ShowMenu("history")

            textbutton _("{b}Save") action ShowMenu("save")

        textbutton _("{b}Load") action ShowMenu("load")

        textbutton _("{b}Options") action ShowMenu("options")

        if _in_replay:

            textbutton _("{b}End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("{b}Main Menu") action MainMenu()

        textbutton _("{b}Gallery") action ShowMenu("gallery")

        textbutton _("{b}Credits") action ShowMenu("about")

        if renpy.variant("pc"):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("{b}Controls") action ShowMenu("help")

            ## The quit button is banned on iOS and unnecessary on Android.
            textbutton _("{b}Quit") action Quit(confirm=not main_menu)
