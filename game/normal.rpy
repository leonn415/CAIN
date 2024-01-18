label normal_4:

    scene bg cabin night

    "You stir around with a spoon.{pause}Hesitantly,{pause}you lift a piece of meat to your mouth."

    "The meat has an unfamiliar texture.{pause}You can’t quite put a finger on it."

    "The cold water ignites your dry throat,{pause}causing it to close in on itself painfully."

    "You make your way back to the bed and slowly drift into sleep."

    $ _dismiss_pause = False

    scene black with Dissolve(1)

    scene bg cabin day with Dissolve(1)

    "When you wake up,{pause}another bowl of soup is already on the table.{pause}Next to it is some water and a washcloth."

    "For the next few days,{pause}you go through more or less the same routine."

    "You wake up to eat and wash up,{pause}then check your leg and try to rehabilitate."

    "The villagers seem to have switched out your spear with a stick while you were asleep,{pause}and you use it to walk around the cabin.{pause}Whenever you try to go outside,{pause}a group of elderly villagers will sprint to block your path."

    "Every day,{pause}elderly villagers come into the cabin,{pause}sometimes with small children.{pause}They don’t interact with you besides watching you like some exotic animal."

    "You soon give up asking questions from them."

    jump normal_5

label normal_5:

    scene bg cabin night

    show girl neutral

    "As the light of the candle flickers,{pause}you’re seated at the table,{pause}alone in your thoughts.{pause}Suddenly,{pause}a loud creak interrupts the quiet as the door creeps open."

    "Standing in the doorway was the young woman,{pause}carrying your dinner.{pause}As you glance up,{pause}the woman pauses for a moment before eventually approaching."

    "She sets a bowl down on the edge of the table,{pause}standing a mere foot away from you."

    s "Hey."

    "The young woman visibly flinches at the sudden sound of your voice.{pause}She shrinks back,{pause}as her eyes flicker towards the door."

    "You pull your arms back,{pause}feigning surrender in hopes of appeasing the girl."

    s "No,{pause}wait!{pause}It’s okay,{pause}I won’t touch."

    show girl neutral

    "You pause,{pause}taking a moment to truly look at the young woman for the first time.{pause}Your eyes search for hers under the folds of deformed flesh that cling to her face."

    s "I know you can’t tell me what’s happening,{pause}but won’t you at least tell me about yourself?{pause}So many people come to see me,{pause}yet no one seems to listen."

    "You notice that the woman seems antsy,{pause}so you give her a reassuring smile."

    s "Except{ellipsis}you,{pause}of course."

    "You pause,{pause}leaning forward with a warm expression."

    s "You always take care of me,{pause}bring me things to help me get better."

    "The young woman’s expression seems to soften for just a moment.{pause}She reaches her wrist towards you,{pause}stretching out towards your face."

    "At the last moment,{pause}however,{pause}she hesitates as her eyes flicker with a hint of emotion.{pause}Was there a chance that she could sympathize with you?"

    show girl touched

    "For what seems like an eternity,{pause}the room fills with a heavy silence.{pause}You stare at her,{pause}eyes wide as her wrist is just a touch away from your face."

    if favor >= 4:
        menu:
            #"Caress her skin folds":
                #$ favor += 1
                #jump days2
            "Grab her":
                jump days2
            "Stay still":
                pass

    s "Won’t you take pity on me?{pause}I just want a friend."

    "The woman instantly retracts her wrist.{pause}Her eyes widen for a moment as she staggers back and hurriedly rushes out of the cabin."

    if not normalrun:
        "Seems like you've failed to gain her favor,{pause}perhaps you should've swallow your pride and tried harder."

    hide girl

    $ _dismiss_pause = False

    scene black with Dissolve(0.9)

    jump normal_6

label normal_6:

    scene black

    "You open your eyes only to see an unending void,{pause}darkness stretching out in every direction."

    "You stumble to your feet,{pause}trying to make sense of the dark expanse before you when your eyes catch an eagle-like bird illuminated by a single beam of light."

    "Walking closer,{pause}you see the bird is picking at something."

    "Upon closer inspection,{pause}the bird is feeding on a dead mouse,{pause}only picking at the face of it."

    jump normal_7

label normal_7:

    scene bg cabin night

    "Your eyes snap open,{pause}and a dark ceiling greets your vision.{pause}You’re back in the cabin.{pause}Or rather,{pause}you never left."

    "The rough fabric bedding,{pause}heavy with sweat,{pause}wraps around your body like chains.{pause}You itch all over from a night spent in its cruel embrace."

    "You sit up and take a look around as you throw the fabric from your raw skin.{pause}The cabin is still and serene.{pause}You hear only your raging heartbeat and heaving gasps."

    "You lie back down and let the sheets cover you once more.{pause}You keep your gaze on the cabin’s entrance and drift once more into unconsciousness."

    $ _dismiss_pause = False

    scene black with Dissolve(0.9)

    jump normal_8_placeholder

label normal_8_placeholder:

    $ _dismiss_pause = False

    scene bg cabin morning with Dissolve(0.9)

    show particleFog

    "Morning fog seeps into the cabin from below the door."

    "The door opens,{pause}in walks the young woman."

    "She lets out a panicked shriek heard loud enough for the entire hamlet.{pause}Another villager comes running."

    v "What’s wrong?!"

    y "He’s gone!"

    v "Quick!{pause}Everyone form groups of three and search!"

    if not normalrun and defiance >= 6:
        jump malnurished_ending

    "You are hanging from the inner edge of the pit latrine.{pause}As the hurried footsteps grow distant,{pause}you push the toilet seat away and pull yourself up."

    "You listen with your ear against the walls before slipping out the door."

    jump normal_9

label normal_9:

    scene bg forest

    #show tiledFog at Pan((0,0), (1600,0), 5, repeat=True)

    show particleFog

    if not normalrun and rehab <= 2:
        jump m_ending

    "The hamlet fades into the distance as you stagger deep into the forest,{pause}not once looking back."

    "Pain courses through your leg as you stumble through the thick haze.{pause}The branches claw at your skin,{pause}the air weighs heavily in your lungs,{pause}and your body burns with each step."

    "But only one thought is pounding in your head: {w}run."

    "{ellipsis}"
    #programmer: is it possible to just have no dialogue here and add in a twig snapping/leaves rustling sound effect? answer: yes

    "You whip your head around,{pause}listening for something,{pause}anything."

    "Suddenly,{pause}the forest filled with the sound of twigs snapping and shouting from each and every direction."
    #If we are implementing a mini-game,{pause}here’s where it’ll start

    "You let your body drop straight to the ground,{pause}curling up beneath the shadows of a nearby tree."

    "Lying still as stone,{pause}you didn’t dare to think of making a single noise,{pause}for a mere breath may be the difference between life and death."

    "Soon the voices start to fade as footsteps grow faint into the murky morning.{pause}You hoist yourself up with a grunt only to begin running once more."

    scene bg battlefield

    show particleFog

    "After what felt like an eternity of running,{pause}your pace steadies as the blurred outline of the battlefield emerges from the fog."

    "As you inch closer and closer towards the clearing,{pause}the hazy curtain of white seems to dissipate as a familiar figure appears at the edge of the battlefield."

    "It’s the young woman."

    menu:
        "Pick up a rock":
            pass
    menu:
        "Move closer":
            pass
    menu:
        "Closer":
            pass
    menu:
        "More":
            pass
    menu:
        "Crack her skull":
            pass

    if not normalrun and rehab <= 4:
            jump l_ending

    "She lets out a tiny yelp before she falls face-first into the river."

    "You kneel down beside the young woman,{pause}holding her face down into the water until it stops bubbling."

    "You flip her body over with a grunt.{pause}However,{pause}you are not met with her deformed face,{pause}but your own lifeless visage."

    "{ellipsis}"
    #programmer could you put in a heartbeat sound effect & possibly make the screen pulse (if that’s a thing) answer: yes,{pause}that’s possible

    "Your face turns hot as your vision starts to become bleary.{pause}With trembling hands,{pause}you stagger from the ghastly sight of the body."

    "Your stomach drops,{pause}you hesitantly bring your hands up to your face,{pause}murmuring to yourself in denial as you feel the skin that was meant to be yours."

    "The only thing you can hear is your heartbeat as your breathing becomes more and more erratic.{pause}Your legs tremble as you bring yourself up off the ground and take a step back,{pause}only to be met with a giant plop as your body sinks into the depths of the river."

    jump normal_ending

label normal_ending:

    $ persistent.tl += 1
    $ persistent.normal_end = True
    $ _dismiss_pause = False

    scene black with Dissolve(3)

    scene bg battlefield with Dissolve(3)

    "It’s a warm day with a clear sky."

    "A village is bustling with life.{pause}Kids take off their socks and shoes to play in the clear,{pause}glistening river."

    "From somewhere upstream,{pause}steadily,{pause}past green trees,{pause}young grass,{pause}tiny flowers,{pause}and lively animals,{pause}all under the blue sky,{pause}is the body of a soldier floating idly down the river."

    "The body is fully intact and doesn’t leave a bloody trail in the water."

    "The face on the body is that of a deformed young woman."

    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    $ renpy.pause(3, hard=True)

    call credits from _call_credits
