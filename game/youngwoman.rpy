
label make_convo:
    menu:
        "Compliment":
            menu:
                "Food":
                    y "..."

                    "She stares at you blankly, as if she had heard something unintelligible."

                "Weather":
                    "She looks out the window, you follow her motion and see that it's pitch-black outside."

                    y "..."

                    s "..."

                "Person":
                    call compliment
        "Inquire":
            y "..."

            "She huffs lightly, as if you've asked her something in a language she clearly doesn't understand."

        "...":
            hide girl neutral
            return

    "Unfortunately for you, it doesn't seem like you'll get anything out of her anytime soon."

    "She turns away and leaves."

    hide girl neutral

    "What should you do with the bowl of soup?"

    return

label compliment:
    $ favor += 1

    if defiance >= 6:
        "You are sure she reacted, but your eyes are too blurred to see anything."

    elif favor <= 3:
        y "..."

        "You think you catch a light twitching in the folds on her face."

    elif favor == 4:
        y "..."

        "She briefly bites the good side of her lips."

    elif favor == 5:
        y "..."

        "She turns her head, then lowers it. You think she might be shy."

    return
