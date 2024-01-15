screen GameOverScreen():
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.75
        ypos 0.65
        idle "MainMenuButton.webp"
        hover "MainMenuButtonHover.webp"
        action MainMenu()

    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.25
        ypos 0.65
        idle "RetryButton.webp"
        hover "RetryButtonHover.webp"
        action Jump("GameOverReturn")
