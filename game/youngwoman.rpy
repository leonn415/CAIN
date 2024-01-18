
label make_convo:
    menu:
        "Compliment":
            menu:
                "Food":

                    s "I really like the food here,{pause}haha."

                    if dumped:
                        "You realize that she's holding your untouched meal from before."

                        s "Too bad I haven't been feeling well enough to eat,{pause}haha."

                    y "{ellipsis}"

                    "She stares at you blankly,{pause}as if she had heard something stupid."

                "Weather":

                    s "The weather sure is nice today{ellipsis}"

                    "She looks out the window,{pause}you follow her motion and see that it's pitch-black outside."

                    y "{ellipsis}"

                    s "{ellipsis}"

                "Her":
                    call compliment from _call_compliment
        "Inquire":
            $ inq = renpy.random.choice(['Have you lived here for long?', 'The other people, do they treat you well?', 'Where did my spear go?', 'What is this meat in the soup?'])

            s "[inq]"

            y "{ellipsis}"

            "She huffs lightly,{pause}as if you've asked her something in a language she clearly doesn't understand."

        "{ellipsis}":
            hide girl neutral with dissolve

            "You can't think of anything to say.{pause}Before you knew it,{pause}she's already left."

            return

    "Unfortunately for you,{pause}it doesn't seem like you'll get anything out of her anytime soon."

    "She turns away and leaves."

    hide girl neutral

    "What should you do with the bowl of soup?"

    return

label compliment:
    $ favor += 1
    #Your rizz
    $ comp = renpy.random.randint(1, 5)
    if comp == 1:

        s "Thank you for always bringing me food{ellipsis}"
        if dumped:
            "The young woman eyed the cold leftover in her hands."

            s "I- I don't always have the energy to get up,{pause}I'm sorry{ellipsis}it must be a lot of trouble."
    elif comp == 2:

        s "I must be adding onto your workload right? You are so hardworking."
    elif comp == 3:

        s "You move so elegantly everytime I see you."
    elif comp == 4:

        s "I can tell you are a caring girl{ellipsis}you will make a great mother one day."
    elif comp == 5:

        s "Surely a quiet and hardworking girl like you have an admirer or two{ellipsis}"

    #Her reaction
    if defiance >= 6:
        "You are sure she reacted,{pause}but your eyes are too blurred to see anything."
    elif favor == 1:
        y "{ellipsis}"

        "You think you catch a light twitching in the folds on her face."

    elif favor == 2:
        y "{ellipsis}"

        "She lowers her head and holds her arms above her chest."

    elif favor == 3:
        y "{ellipsis}"

        "She briefly bites the good side of her lips."

    elif favor == 4:
        y "{ellipsis}"

        "She turns her head,{pause}then lowers it.{pause}You think she might be shy."

    return
