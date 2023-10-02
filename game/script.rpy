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
    
    config.self_closing_custom_text_tags["pause"] = pause_tag

label normal_1:

    scene bg hamlet evening

    "As the sun creeps its way down the horizon, an orange hue bleeds into the forest. The trees and grasses stain in the light, appearing as if painted in odd hues. The shades of color surround you, and they confound you, much like the villagers escorting you."
    
    "These strange people have been corralling you, much like cattle… Not a word has been said of their intentions, and all the while they only circle, the weight of their stares behind you."
    
    "You are, at length, brought along a weathered bridge and toward a barren hamlet. It is as if the threshold of the bridge protected all behind it from terrible blight. Ahead, shriveled, gnarled and dead trees dot between the hovels."

    "Yellow weeds graze against your boots as you are led down a path. The silence of their march was sparsely interrupted by the wailing of children and the pallid squawking of birds."

