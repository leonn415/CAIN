# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define config.has_autosave = False
define config.has_quicksave = False
define s = Character("Soldier")
define i = Character(what_italic = True)
define y = Character("Young Woman")
define v = Character("Villager")
define o = Character("Elderly Man")

init python:
    # Define a custom text tag ("pause") that slows down the text speed by 90%
    def pause_tag(tag, argument):
        return [(renpy.TEXT_TAG, "cps=*.1"), (renpy.TEXT_TEXT, " "), (renpy.TEXT_TAG, "/cps")]

    # Define a custom text tag ("ellipsis") that puts an ellipsis at a reduced speed
    def ellipsis_tag(tag, argument):
        return [(renpy.TEXT_TAG, "cps=*0.3"), (renpy.TEXT_TEXT, ". . . "), (renpy.TEXT_TAG, "/cps")]

    config.self_closing_custom_text_tags["pause"] = pause_tag
    config.self_closing_custom_text_tags["ellipsis"] = ellipsis_tag

label start:
    if persistent.tl == 1:
        jump intro
    else:
        jump normal_1
label intro:
    scene intro 1
    pause
    scene black with dissolve
    scene intro 2 with dissolve
    pause
    scene black with dissolve
    scene intro 3 with dissolve
    pause
    scene black with dissolve
    scene intro 4 with dissolve
    pause
    scene black with dissolve
    scene intro 5 with dissolve
    pause
    scene black with dissolve
    scene intro 6 with dissolve
    pause
    scene black with dissolve
    scene intro 7 with dissolve
    pause
    scene black with dissolve
    scene intro 8 with dissolve
    pause
    scene black with dissolve
    jump normal_1

label normal_1:
    $ day = 1
    $ hunger = 0
    $ defiance = 0
    $ rehab = 0
    scene bg hamlet evening with dissolve

    "As the sun creeps its way down the horizon{pause}an orange tinge bleeds into the forest."

    "The trees and grasses{pause}all the various foliage about{pause}stain in the light{pause}appearing as if painted in odd hues{pause}The shades of color surround{pause}and they confound{pause}much like the villagers escorting you."

    "These strange people have been corralling you,{pause}much like cattle{ellipsis}Not a word has been said of their intentions,{pause}and all the while they only circle,{pause}the weight of their stares behind you."

    "You are,{pause}at length,{pause}brought along a weathered bridge and toward a barren hamlet.{pause}It is as if the threshold of the bridge protected all behind it from terrible blight.{pause}Ahead,{pause}shriveled,{pause}gnarled and dead trees dot between the hovels."

    "Yellow weeds graze against your boots as you are led down a path.{pause}The silence of their march was sparsely interrupted by the wailing of children and the pallid squawking of birds."

    jump normal_2

label normal_2:

    scene bg cabin day

    "You are led to a cabin near the center of the hamlet.{pause}The door is opened with a creak and you are herded in."

    "The cabin is small but surprisingly well–equipped.{pause}There’s a straw bed,{pause}a table,{pause}and a few chairs.{pause}More impressively,{pause}there seems to be an indoor pit latrine behind some wooden boards."

    "You drag your body to the bed and sit down slowly.{pause}The sharp pain resurges now that you are able to relax.{pause}You really need to check your leg."

    "Leaning the spear you've been using as a crutch against the wall,{pause}you clench your teeth as you raise your legs onto the bed."

    "A young woman enters the cabin."

    show girl neutral

    "Most of her face is covered in flesh folds and lesions,{pause}but you can tell from the rest of her body that she is around your age.{pause}She is holding a bucket of water and some cloth."

    "She approaches the foot of the bed,{pause}struggling to handle the bucket with her stumps for hands."

    "You reach out for the bucket,{pause}only for her to flinch away from you,{pause}the bucket toppling over."

    s "Ah—{pause}"

    "The young woman sits in the puddle of water,{pause}her hair and dress soaked.{pause}You look toward the other villagers,{pause}hoping they would lend a helping hand,{pause}only to be stunned by the cold stares thrown her way."

    jump normal_3

label normal_3:

    scene bg cabin dark

    "Day hastefully becomes night."

    "The cabin is pitch black.{pause}The room is now unrecognizable from the day."

    "The abnormal silence of the forest is eerie.{pause}The only thing you can manage to hear is the blowing of the wind."

    "You then hear a door creak as it slowly opens with a contrasting bright light coming from a candle,{pause}it’s the woman from before."

    scene bg cabin night

    show girl neutral

    "The woman comes up and lays a tray on the table.{pause}On the tray is a bowl of soup,{pause}a cup of cold water,{pause}and a lit candle."

    s "Thank you{ellipsis}"

    "She nods and turns to leave."

    "You attempt to sit up."

    s "Wait!{pause}Can you—{pause}"

    "She continues walking towards the door."

    s "—can you tell me about this place?{pause}Anything{ellipsis}please{ellipsis}"

    "She turns back towards you.{pause}You think you might have changed her mind."

    hide girl neutral

    "But you hadn’t.{w} Without a single word,{pause}she simply bows before leaving you alone in the cabin,{pause}again."

    "You are left alone,{pause}listening to the late night ambience."

    "You drag your body to the table and pick up the bowl in front of you.{pause}Pieces of meat rock back and forth in the thin liquid."

    if persistent.tl == 1:
        jump normal_4
    else:
        jump days
