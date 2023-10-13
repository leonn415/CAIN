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

label normal_2:

    scene bg cabin evening

    "You are led to a cabin near the center of the hamlet. The door is opened with a creak and you are herded in."

    "The cabin is small but surprisingly well–equipped. There’s a straw bed, a table, and a few chairs. More impressively, there seems to be an indoor pit latrine behind some wooden boards."

    "You drag your body to the bed and sit down slowly. The sharp pain resurges now that you are able to relax. You really need to check your leg."

    "Leaning the spear against the bed, you clench your teeth as you raise your legs onto the bed."

    "A young woman enters the cabin."

    show girl neutral

    "Most of her face is covered in flesh folds and lesions, but you can tell from the rest of her body that she is around your age. She is holding a bucket of water and some cloth."

    "She approaches the foot of the bed, struggling to handle the bucket with her stumps for hands."

    "You reach out for the bucket, only for her to flinch away from you, the bucket toppling over."

    s "Ah— "

    "The young woman sits in the puddle of water, her hair and dress soaked. You look toward the other villagers, hoping they would lend a helping hand, only to be stunned by the cold stares thrown her way."

    #jump normal_3

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
