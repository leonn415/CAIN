#Achievements

default persistent.normal_end = False

default persistent.starvation_end = False


#you die from not eating for 7 consecutive days
label starvation_ending:
    $ persistent.tl += 1
    scene black
    "It's been seven days since you've eaten anything. The muscles in your heart can no longer sustain its own movement. You have died."
    $ MainMenu(confirm=False)()
