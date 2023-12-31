# Not really sure where this fits in the credits but they should be credited
# Ren'py forum user "leon" made most of the code for these scrolling credits

label credits:
    $ credits_speed = 25 # scrolling speed in seconds
    scene black with dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide theend with dissolve

    # Change the y-position of the first point to be bigger as the credits list grows.
    show cred at Move((0.5, 3.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks with dissolve
    return

init python:
    credits = ("Editing", "Austin McGregor"), ("Programming", "Abrianna Cheung"), ("Programming", "Austin McGregor"), ("Programming", "Jalana"), ("Programming", "Jocelyn Ho"), ("Programming", "Li-An Tsai"), ("Programming", "Roderic Parson"), ("Writing", "Christian Sal"), ("Writing", "Ellen Crews"), ("Writing", "G. Patrick"), ("Writing", "Katherine Huang"), ("Writing", "Kayla Dang"), ("Writing", "Li-An Tsai"), ("Writing", "Lindsey Zhang"), ("Writing", "Nicky Turk")

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
    image theend = Text("{color=#ffffff}{size=80}The End{/size}{/color}", text_align=0.5)
    image thanks = Text("{color=#ffffff}{size=80}Thanks for Playing!{/size}{/color}", text_align=0.5)