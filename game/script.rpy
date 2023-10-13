# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Soldier")
define i = Character(what_italic = True)
define y = Character("Young Woman")
define v = Character("Villager")

init python:
    # Define a custom text tag ("pause") that slows down the text speed by 90%
    def pause_tag(tag, argument):
        return [(renpy.TEXT_TAG, "cps=*.1"), (renpy.TEXT_TEXT, " "), (renpy.TEXT_TAG, "/cps")]

    # Define a custom text tag ("ellipsis") that puts an ellipsis at a reduced speed
    def ellipsis_tag(tag, argument):
        return [(renpy.TEXT_TAG, "cps=*0.125"), (renpy.TEXT_TEXT, ". . . "), (renpy.TEXT_TAG, "/cps")]
    
    config.self_closing_custom_text_tags["pause"] = pause_tag
    config.self_closing_custom_text_tags["ellipsis"] = ellipsis_tag

label start:
    jump intro

label intro:
    scene intro 1
    pause
    scene intro 2 with dissolve
    pause
    scene intro 3 with dissolve
    pause
    scene intro 4 with dissolve
    pause
    scene intro 5 with dissolve
    pause
    scene intro 6 with dissolve
    pause
    scene intro 7 with dissolve
    pause
    scene intro 8 with dissolve
    pause
    jump normal_1

label normal_1:

    scene bg hamlet evening with dissolve

    "As the sun creeps its way down the horizon,{pause}an orange hue bleeds into the forest.{pause}The trees and grasses stain in the light,{pause}appearing as if painted in odd hues.{pause}The shades of color surround you,{pause}and they confound you,{pause}much like the villagers escorting you."
    
    "These strange people have been corralling you,{pause}much like cattle{ellipsis}Not a word has been said of their intentions,{pause}and all the while they only circle,{pause}the weight of their stares behind you."
    
    "You are,{pause}at length,{pause}brought along a weathered bridge and toward a barren hamlet.{pause}It is as if the threshold of the bridge protected all behind it from terrible blight.{pause}Ahead,{pause}shriveled,{pause}gnarled and dead trees dot between the hovels."

    "Yellow weeds graze against your boots as you are led down a path.{pause}The silence of their march was sparsely interrupted by the wailing of children and the pallid squawking of birds."

    jump normal_2

label normal_2:

    scene bg cabin evening

    "You are led to a cabin near the center of the hamlet.{pause}The door is opened with a creak and you are herded in."

    "The cabin is small but surprisingly well–equipped.{pause}There’s a straw bed,{pause} a table,{pause}and a few chairs. More impressively,{pause}there seems to be an indoor pit latrine behind some wooden boards."

    "You drag your body to the bed and sit down slowly.{pause}The sharp pain resurges now that you are able to relax.{pause}You really need to check your leg."

    "Leaning the spear against the bed,{pause}you clench your teeth as you raise your legs onto the bed."

    "A young woman enters the cabin."

    show girl neutral

    "Most of her face is covered in flesh folds and lesions,{pause}but you can tell from the rest of her body that she is around your age.{pause}She is holding a bucket of water and some cloth."

    "She approaches the foot of the bed,{pause}struggling to handle the bucket with her stumps for hands."

    "You reach out for the bucket,{pause}only for her to flinch away from you,{pause}the bucket toppling over."

    s "Ah—{pause}"

    "The young woman sits in the puddle of water,{pause}her hair and dress soaked.{pause}You look toward the other villagers,{pause}hoping they would lend a helping hand,{pause}only to be stunned by the cold stares thrown her way."

    jump normal_3

label normal_3:

    scene bg cabin night
 
    "Day hastefully becomes night."

    "The cabin is pitch black.{pause}The room is now unrecognizable from the day."

    "The abnormal silence of the forest is eerie.{pause}The only thing you can manage to hear is the blowing of the wind."

    "You then hear a door creak as it slowly opens with a contrasting bright light coming from a candle,{pause} it’s the woman from before."

    "The woman comes up and lays a tray on the table.{pause}On the tray is a bowl of soup,{pause}a cup of cold water,{pause}and a lit candle."

    s "Thank you…"

    "She nods and turns to leave."

    "You attempt to sit up."

    s "Wait!{pause}Can you—"

    "She continues walking towards the door."

    s "{size=-10}—can you tell me about this place?{pause}Anything….{pause}please…." #programmer please make this text smaller (use a variable to store the smaller text size)

    "She turns back towards you. You think you might have changed her mind."

    hide girl

    "But you hadn’t.{w}Without a single word, she simply bows before leaving you alone in the cabin, again."

    "You are left alone, listening to the late night ambience."

label normal_5:

    scene bg cabin night

    show girl neutral

    "As the light of the candle flickers,{pause}you’re seated at the table,{pause}alone in your thoughts.{pause}Suddenly,{pause}a loud creak interrupts the quiet as the door creeps open."

    "Standing in the doorway was the young woman,{pause}carrying your dinner.{pause}As you glance up,{pause}the woman pauses for a moment before eventually approaching."

    "She sets a bowl down on the edge of the table,{pause}standing a mere foot away from you."

    i  "Ah.{pause}She stuck around this time."

    s "Hey."

    "The young woman visibly flinches at the sudden sound of the soldier’s voice.{pause}She shrinks back,{pause}as her eyes flicker towards the door."

    "You pull your arms back,{pause}feigning surrender in hopes of appeasing the girl."

    s "No,{pause}wait!{pause}It’s okay,{pause}I won’t touch."

    show girl neutral 

    "You pause,{pause}taking a moment to truly look at the young woman for the first time.{pause}Your eyes search for hers under the folds of deformed flesh that cling to her face."

    s "I know you can’t tell me what’s happening,{pause}but won’t you at least tell me about yourself?{pause}So many people come to see me,{pause}yet no one seems to listen."

    "You notice that the woman seems antsy,{pause}so you give her a reassuring smile."

    s "Except…you,{pause}of course."

    "You pause,{pause}leaning forward with a warm expression."

    s "You always take care of me,{pause}bring me things to help me get better."

    "The young woman’s expression seems to soften for just a moment.{pause}She reaches her wrist towards you,{pause}stretching out towards your face."

    "At the last moment,{pause}however,{pause}she hesitates as her eyes flicker with a hint of emotion. Was there a chance that she could pit you?"

    "For what seems like an eternity,{pause}the room fills with a heavy silence. You stare at her,{pause}eyes wide as her wrist is just a touch away from your face."

    s "Won’t you take pity on me?{pause}I just want a friend."

    "The woman instantly retracts her wrist.{pause}Her eyes widen for a moment as she staggers back and hurriedly rushes out of the cabin."

    hide girl

    scene black with Dissolve(0.9)

    #jump normal_6

    # would it be good to end the scene with a slow fade to black?? yeah —Leon

label normal_7:

    scene bg cabin night

    "You open your eyes in cold sweat."

    "You look around the cabin and find yourself alone.{pause}He lies back down on the pillow with a sigh."

    "You watch the cabin door in your peripheral and drift off again."

    scene black with dissolve

    jump normal_ending

label normal_ending:

    "It’s a warm day with a clear sky."

    "A village is bustling with life.{pause}Kids take off their socks and shoes to play in the clear,{pause}glistening river."

    "From somewhere upstream,{pause}steadily,{pause}past green trees,{pause}young grass,{pause}tiny flowers,{pause}and lively animals,{pause}all under the blue sky,{pause}is the body of a soldier floating idly down the river."

    "The body is fully intact and doesn’t leave a bloody trail in the water."

    "The face on the body is that of a deformed young woman."

    show qrcode with dissolve:
        xalign 0.5

    "Thank you for playing CAIN!{pause}Please fill out the feedback form to tell us what you thought of CAIN!"

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Soldier")
define i = Character(what_italic = True)
define y = Character("Young Woman")
define v = Character("Villager")

init python:
    # Define a custom text tag ("pause") that slows down the text speed by 90%
    def pause_tag(tag, argument):
        return [(renpy.TEXT_TAG, "cps=*.1"), (renpy.TEXT_TEXT, " "), (renpy.TEXT_TAG, "/cps")]

    # Define a custom text tag ("ellipsis") that puts an ellipsis at a reduced speed
    def ellipsis_tag(tag, argument):
        return [(renpy.TEXT_TAG, "cps=*0.125"), (renpy.TEXT_TEXT, ". . . "), (renpy.TEXT_TAG, "/cps")]
    
    config.self_closing_custom_text_tags["pause"] = pause_tag
    config.self_closing_custom_text_tags["ellipsis"] = ellipsis_tag

label start:
    jump intro

label intro:
    scene intro 1
    pause
    scene intro 2 with dissolve
    pause
    scene intro 3 with dissolve
    pause
    scene intro 4 with dissolve
    pause
    scene intro 5 with dissolve
    pause
    scene intro 6 with dissolve
    pause
    scene intro 7 with dissolve
    pause
    scene intro 8 with dissolve
    pause
    jump normal_1

label normal_1:

    scene bg hamlet evening with dissolve

    "As the sun creeps its way down the horizon,{pause}an orange hue bleeds into the forest.{pause}The trees and grasses stain in the light,{pause}appearing as if painted in odd hues.{pause}The shades of color surround you,{pause}and they confound you,{pause}much like the villagers escorting you."
    
    "These strange people have been corralling you,{pause}much like cattle{ellipsis}Not a word has been said of their intentions,{pause}and all the while they only circle,{pause}the weight of their stares behind you."
    
    "You are,{pause}at length,{pause}brought along a weathered bridge and toward a barren hamlet.{pause}It is as if the threshold of the bridge protected all behind it from terrible blight.{pause}Ahead,{pause}shriveled,{pause}gnarled and dead trees dot between the hovels."

    "Yellow weeds graze against your boots as you are led down a path.{pause}The silence of their march was sparsely interrupted by the wailing of children and the pallid squawking of birds."

    jump normal_4

label normal_4:

    scene bg cabin day

    "You drag your body to the table and pick up the bowl in front of you.{pause}Pieces of meat rock back and forth in the thin liquid."

    "You stir around with a spoon.{pause}Hesitantly,{pause}you lift a piece of meat to your mouth."

    "The meat has an unfamiliar texture.{pause}You can’t quite put a finger on it."

    "The cold water ignites your dry throat,{pause}causing it to close in on itself painfully."

    "You make your way back to the bed and slowly drift into sleep."

    "When you wake up,{pause}another bowl of soup is already on the table.{pause}Next to it is some water and a washcloth."

    "For the next few days,{pause}you go through more or less the same routine."

    "You wake up to eat and wash up,{pause}then check your leg and try to rehabilitate."

    "The villagers seem to have switched out your spear with a stick while you were asleep,{pause}and you use it to walk around the cabin.{pause}Whenever you try to go outside,{pause}a group of elderly villagers will sprint to block your path."

    "Every day,{pause}elderly villagers come into the cabin,{pause}sometimes with small children.{pause}They don’t interact with you besides watching you like some exotic animal."

    "You soon give up asking questions from them."

    jump normal_7

label normal_7:

    scene bg cabin night

    "You open your eyes in cold sweat."

    "You look around the cabin and find yourself alone.{pause}You lie back down on the pillow with a sigh."

    "You watch the cabin door in your peripheral and drift off again."

    scene black with dissolve

    jump normal_ending

label normal_ending:

    "It’s a warm day with a clear sky."

    "A village is bustling with life.{pause}Kids take off their socks and shoes to play in the clear,{pause}glistening river."

    "From somewhere upstream,{pause}steadily,{pause}past green trees,{pause}young grass,{pause}tiny flowers,{pause}and lively animals,{pause}all under the blue sky,{pause}is the body of a soldier floating idly down the river."

    "The body is fully intact and doesn’t leave a bloody trail in the water."

    "The face on the body is that of a deformed young woman."

    show qrcode with dissolve:
        xalign 0.5

    "Thank you for playing CAIN!{pause}Please fill out the feedback form to tell us what you thought of CAIN!"
