#Achievements

default persistent.normal_end = False

default persistent.starvation_end = False

default persistent.fall_end = False

default persistent.cushioned_end = False


#you die from not eating for 7 consecutive days
label starvation_ending:
    "It's been seven days since you've eaten anything. As you stand up from the table to move away, you collapse."

    "For the next few minutes you feel with whatever awareness you have the muslces in your heart failing."

    "You have died."

    scene black with Dissolve(3)
    $ persistent.tl += 1
    $ MainMenu(confirm=False)()

#you die from being too weak to support yourself in the pit latrine
label fall_ending:
    "It's been days since you've eaten anything. You shake uncontrollably and your good leg slides off the opposit wall. Your fingers lose their grip on the ledge, and you make one final swipe at the seat cover in vain."
    if pile == 8:
        jump cushioned_ending
    "You fall straight down in a ludicrous position: three limbs up and grazing the wall."

    "The leg that you cannot lift hits the ground first. Not at a pretty angle, no. Then, your tailbone."

    "The shock from the contact shoots straight up your spine, fracturing it and breaking your spinal cord."

    "How fortunate you are to be unconscious as your organs, and then you, die."

    scene black with Dissolve(3)
    $ persistent.tl += 1
    $ MainMenu(confirm=False)()

#you die from being too weak to support yourself in the pit latrine AND get absorbed by meat
label cushioned_ending:
    "You embarassingly flail your good limbs around, trying to grab onto anything you could."

    "This, of course, fails and instead your behind hits... something soft?"

    "Something smooth and cushy has saved you from the fall."

    "You move around to stand on your feet, then you bend over to inspect the substance below you."

    "You scoop its side, and to your surprise, it breaks of from itself easily. The piece in your hand is a little rubbery, almost like the congealed foam you get from cooking meat."

    "You lift up the piece observe it in the sunlight, but it jumps for your face."

    scene black

    "You keel over, as much as one can in a pit latrine."

    "You feel something climb into your boots and up your chainmail."

    "The thing has entered all of your orifices, and possibly tearing new ones."

    "Every inch of your skin and lining burns, and you can't even scream."

    "Fortunately for you, your brain is not a long trip from the nostrils. You will be relieved soon."

    $ persistent.tl += 1
    $ MainMenu(confirm=False)()
