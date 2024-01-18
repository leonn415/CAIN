# Not really sure where this fits in the credits but they should be credited
# Ren'py forum user "leon" made most of the code for these scrolling credits

label credits:
    $ credits_speed = 30 # scrolling speed in seconds
    # Change the y-position of the first point to be bigger as the credits list grows.
    scene black with dissolve
    show cred at Move((0.5, 6.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    #$ renpy.pause(30, hard=True)
    return

init python:
    credits = ("Original Screenplay", "Leon Tsai"), ("Project Lead", "Leon Tsai"), ("Programming Lead", "Austin McGregor"), ("Programming", "Allison"), ("Programming", "Abrianna Cheung"), ("Programming", "Jocelyn"), ("Programming", "Austin McGregor"), ("Programming", "Roderic"), ("Programming", "Jalana Smith")

    credits += ("Programming", "Leon Tsai"), ("Script Writing", "Leon Tsai"), ("Script Adaptation", "Christian"), ("Script Adaptation", "Ellen Crews"), ("Script Adaptation", "Katherine"), ("Script Adaptation", "Kayla"), ("Script Adaptation", "Gray Patrick"), ("Script Adaptation", "Leon Tsai"), ("Script Adaptation", "Nicky Turk")

    credits += ("Script Adaptation", "Lindsey Zhang"), ("Editing", "Abrianna Cheung"), ("Editing", "Ellen Crews"), ("Editing", "Austin McGregor"), ("Editing", "Gray Patrick"), ("Editing", "Reid"), ("Editing", "Ryan"), ("Editing", "Leon Tsai"), ("Editing", "Nicky Turk")

    credits += ("Story Contribution", "Christian"), ("Story Contribution", "Kayla"), ("Story Contribution", "Gray Patrick"), ("Story Contribution", "Leon Tsai"), ("Story Contribution", "Nicky Turk"), ("Concept Art", "Jolie Chen"), ("Concept Art", "Kang"), ("Concept Art", "Odd Scribbles"), ("Concept Art", "Leon Tsai")

    credits += ("Concept Art", "Lindsey Zhang"), ("Storyboard", "Jolie Chen"), ("Storyboard", "Esther Moon"), ("Storyboard", "Odd Scribbles"), ("Storyboard", "Leon Tsai"), ("Storyboard", "Lindsey Zhang"), ("Environmental Art", "Odd Scribbles"), ("Environmental Art", "Lindsey Zhang"), ("Sprites", "Leon Tsai")

    credits += ("Promotional", "Esther Moon"), ("Promotional", "Leon Tsai"), ("Font", "Leon Tsai"), ("Music Contribution", "Amanda"), ("Special Thanks To", "\nDr. Ida Yoshinaga, for advice on punctuation"), ("Special Thanks To", "\nRen'Py forum user leon, for the scrolling credits code")

    credits_s = "{color=#ffffff}{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}" + renpy.version() + "{/color}"

init:
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{color=#ffffff}{size=80}Normal End{/size}{/color}", text_align=0.5)
    image send = Text("{color=#ffffff}{size=80}S End{/size}{/color}", text_align=0.5)
    image mend = Text("{color=#ffffff}{size=80}M End{/size}{/color}", text_align=0.5)
    image lend = Text("{color=#ffffff}{size=80}L End{/size}{/color}", text_align=0.5)
    image fend = Text("{color=#ffffff}{size=80}F End{/size}{/color}", text_align=0.5)
    image eend = Text("{color=#ffffff}{size=80}E End{/size}{/color}", text_align=0.5)
    #image thanks = Text("{color=#ffffff}{size=80}Thanks for Playing!{/size}{/color}", text_align=0.5)
