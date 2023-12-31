#Achievements

default persistent.normal_end = False

default persistent.starvation_end = False

default persistent.fall_end = False

default persistent.cushioned_end = False


#you die from not eating for 7 consecutive days
label starvation_ending:
    "It's been seven days since you've eaten anything.{pause}As you stand up from the table to move away,{pause}you collapse."

    "For the next few minutes you feel with whatever awareness you have the muslces in your heart failing."

    "You have died."


    scene black with Dissolve(3)

    "Ending (2/6)"

    show qrcode with dissolve:
        xalign 0.5

    "Thank you for playing CAIN!{pause}Please fill out the feedback form to tell us what you thought of CAIN!"

    call credits
    $ persistent.tl += 1
    $ MainMenu(confirm=False)()

label trip_ending:
    "With your walking stick in one hand,{pause}you run awkwardly towards the forest."

    "Just when you are about to reach the edge,{pause}you trip on your own feet."

    "Your throat lands perfectly onto the tip of your stick.{pause}It doesn't penetrate your neck,{pause}but the damage is done."

    "You fall to the ground,{pause}spasming.{pause}You foam at the mouth as the air leaves your brain."

    scene black with Dissolve(3)

    "Ending (3/6)"

    show qrcode with dissolve:
        xalign 0.5

    "Thank you for playing CAIN!{pause}Please fill out the feedback form to tell us what you thought of CAIN!"

    call credits
    $ persistent.tl += 1
    $ MainMenu(confirm=False)()
label weak_ending:
    "She screams as she flings your arm back,{pause}hair and skin stuck to the rock."

    "She turns around,{pause}wearing your face."

    "You scream and tackle her to the ground before you could process what it means."

    "You wrestle,{pause}making incoherent noises like animals."

    "Something strikes you from behind,{pause}and your body goes into shock."

    "Then,{pause}everything goes black."


    scene black with Dissolve(3)

    "Ending (4/6)"

    show qrcode with dissolve:
        xalign 0.5

    "Thank you for playing CAIN!{pause}Please fill out the feedback form to tell us what you thought of CAIN!"

    call credits
    $ persistent.tl += 1
    $ MainMenu(confirm=False)()

label malnurished_ending:
    "It's been days since you've eaten anything.{pause}You shake uncontrollably and your good leg slides off the opposit wall.{pause}Your fingers lose their grip on the ledge,{pause}and you make one final swipe at the seat cover in vain."

    if pile == 8:
        jump cushioned_ending
    else:
        jump fall_ending

#you die from being too weak to support yourself in the pit latrine
label fall_ending:
    "You fall straight down in a ludicrous position:{pause}three limbs up and grazing the wall."

    "The leg that you cannot lift hits the ground first.{pause}Not at a pretty angle,{pause}no.{pause}Then,{pause}your tailbone."

    "The shock from the contact shoots straight up your spine,{pause}fracturing it and breaking your spinal cord."

    "How fortunate you are to be unconscious as your organs,{pause}and then you,{pause}die."

    scene black with Dissolve(3)

    "Ending (5/6)"

    show qrcode with dissolve:
        xalign 0.5

    "Thank you for playing CAIN!{pause}Please fill out the feedback form to tell us what you thought of CAIN!"

    call credits
    $ persistent.tl += 1
    $ MainMenu(confirm=False)()

#you die from being too weak to support yourself in the pit latrine AND get absorbed by meat
label cushioned_ending:
    "You embarassingly flail your good limbs around,{pause}trying to grab onto anything you could."

    "This,{pause}of course,{pause}fails and instead your behind hits{ellipsis}something soft?"

    "Something smooth and cushy has saved you from the fall."

    "You move around to stand on your feet,{pause}then you bend over to inspect the substance below you."

    "You scoop its side,{pause}and to your surprise,{pause}it breaks of from itself easily.{pause}The piece in your hand is a little rubbery,{pause}almost like the congealed foam you get from cooking meat."

    "You lift up the piece observe it in the sunlight,{pause}but it jumps for your face."

    scene black

    "You keel over,{pause}as much as one can in a pit latrine."

    "You feel something climb into your boots and up your chainmail."

    "The thing has entered all of your orifices,{pause}and possibly tearing new ones."

    "Every inch of your skin and lining burns,{pause}and you can't even scream."

    "Fortunately for you,{pause}your brain is not a long trip from the nostrils.{pause}You will be relieved soon."

    "Ending (6/6)"

    show qrcode with dissolve:
        xalign 0.5

    "Thank you for playing CAIN!{pause}Please fill out the feedback form to tell us what you thought of CAIN!"

    call credits
    $ persistent.tl += 1
    $ MainMenu(confirm=False)()
