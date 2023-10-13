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
