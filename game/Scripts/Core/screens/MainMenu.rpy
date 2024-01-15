screen main_menu():


    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use mainmenubuttons

    if gui.show_name:

        vbox:
            yalign 0.05
            text "{color=#fff}Beta [config.version]":
                style "main_menu_text"

    ##Links
    imagebutton:
        idle "patreonbutton"
        hover "patreonbutton1"
        action OpenURL("https://www.patreon.com/randeltales")
        xalign 0.007
        yalign 0.99

    imagebutton:
        idle "discord"
        hover "discord1"
        action OpenURL("https://discord.gg/5SutjWP")
        xalign 0.06
        yalign 0.995

    imagebutton:
        idle "twitter"
        hover "twitterhover"
        action OpenURL("https://twitter.com/randeltales")
        xalign 0.134
        yalign 0.99

    #imagebutton:
    #   idle "clickme"
    #   hover "clickme1"
    #   action ShowMenu("updateinfo")
    #   xalign 0.32
    #   yalign 0.4
