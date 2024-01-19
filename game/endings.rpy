#Achievements
#Have these endings been achieveved?

default persistent.normal_end = False

default persistent.s_end = False

default persistent.m_end = False

default persistent.l_end = False

default persistent.f_end = False

default persistent.e_end = False


#this label represents the day cycle in the game
label days2:
    scene onlayer blurry
    scene blank with dissolve

    "Leon" "Hi,{pause}thanks for playing thus far.{pause}You've reached the second part of the game by gaining enough of the young woman's favor,{pause}kudos to you."

    "Leon" "However,{pause}I,{pause}um,{pause}haven't written the rest of it.{pause}Think of it as you've reached the end of this demo."

    "Leon" "Please feel free to keep on playing if you've like to see other endings.{pause}They are each named after alphabets: S.M.E.L.F."

    "Leon" "When you are finished,{pause}please spare some comments for us,{pause}thank you so much!"

    #call QR from _call_QR
    $ persistent.tl += 1
    $ MainMenu(confirm=False)()

#Reject ten meals in a row
label s_ending:
    "It's been five days since you've eaten anything.{pause}As you stand up from the table to move away,{pause}you collapse."

    "For the next few minutes you feel with whatever awareness you have the muslces in your heart failing."

    "You have died."

    show send onlayer blurry:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(2, hard=True)

    "For Starvation"

    scene onlayer blurry
    scene black with Dissolve(3)

    #call QR from _call_QR_1
    $ persistent.tl += 1
    $ MainMenu(confirm=False)()

#If rehab <= 2
label m_ending:
    "With your walking stick in one hand,{pause}you run awkwardly towards the forest."

    "Just when you are about to reach the edge,{pause}you trip on your own feet."

    "Your throat lands perfectly onto the tip of your stick.{pause}It doesn't penetrate your neck,{pause}but the damage is done."

    "You fall to the ground,{pause}spasming.{pause}You foam at the mouth as the air leaves your brain."

    "Perhaps if you had regained some more mobility you would've gotten further."

    show mend onlayer blurry:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(2, hard=True)

    "For Misstep"

    scene onlayer blurry
    scene black with Dissolve(3)

    #call QR from _call_QR_2
    $ persistent.tl += 1
    $ MainMenu(confirm=False)()
#rehab <= 4
label l_ending:
    "Despite making it out of the forest,{pause}the efforts you invested in rehabilitation were not enough."

    "She screams as she flings your arm back,{pause}hair and skin stuck to the rock."

    "She turns around,{pause}wearing your face."

    "You scream and tackle her to the ground before you could process what it means."

    "You wrestle,{pause}making incoherent noises like animals."

    "Something strikes you from behind,{pause}and your body goes into shock."

    "Then,{pause}everything goes black."


    scene black with Dissolve(3)

    show lend onlayer blurry:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(2, hard=True)

    "For Loser"
    scene onlayer blurry

    #call QR from _call_QR_3
    $ persistent.tl += 1
    $ MainMenu(confirm=False)()

#You fasted 6 consecutive meals before the 7th morning
label malnurished_ending:
    "It's been days since you've eaten anything.{pause}You shake uncontrollably and your good leg slides off the opposit wall.{pause}Your fingers lose their grip on the ledge,{pause}and you make one final swipe at the seat cover in vain."

    if pile == 8:
        jump e_ending
    else:
        jump f_ending

#Didn't dump enough meals
label f_ending:
    "You fall straight down in a ludicrous position:{pause}three limbs up and grazing the wall."

    "The leg that you cannot lift hits the ground first.{pause}Not at a pretty angle,{pause}no.{pause}Then,{pause}your tailbone."

    "The shock from the contact shoots straight up your spine,{pause}fracturing it and breaking your spinal cord."

    "How fortunate you are to be unconscious as your organs,{pause}and then you,{pause}die."

    show fend onlayer blurry:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(2, hard=True)

    "For Falling"

    scene onlayer blurry
    scene black with Dissolve(3)

    #call QR from _call_QR_4
    $ persistent.tl += 1
    $ MainMenu(confirm=False)()

#Throw away at least 8 meals
label e_ending:
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

    show eend onlayer blurry:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(2, hard=True)

    "For Embraced"

    scene onlayer blurry
    scene black with Dissolve(3)

    #call QR
    $ persistent.tl += 1
    $ MainMenu(confirm=False)()

#For play testing
#Uncomment all instances of this this at demos
#label QR:
    #scene blank with dissolve
    #show qrcode:
        #xalign 0.5
        #yalign 0.25

    #"Thank you for playing CAIN!{pause}Please fill out the feedback form for any comments and suggestions."
    #return

#init python:
    #def delete_all_saves():
        #for savegame in renpy.list_saved_games(fast=True):
            #renpy.unlink_save(savegame)
