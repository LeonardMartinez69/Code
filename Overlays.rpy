screen ScoreOverlay():
    tag score_overlay
    frame:
        anchor (0.5, 0.0)
        background Solid("#ffffff99")
        offset (0, 10)
        pos (0.5, 0.0)
        vpgrid:
            cols 2
            frame:
                background None
                xsize 200
                text _("Points") xalign 0.5 bold True
            frame:
                background None
                xsize 200
                text _("Mistakes") xalign 0.5 bold True
            text "[variables.points]" xalign 0.5
            text "[variables.mistakes]" xalign 0.5