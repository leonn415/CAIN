#this label represents the day cycle in the game
label days:
    #night
    if day == 6:
        jump normal_5
    scene bg cabin night
    if day > 1:
        show girl neutral
        "The young woman is here with another bowl of warm soup."
        call make_convo
    call eat from _call_eat
    #morning
    $ day += 1
    scene bg cabin day
    if defiance > 0 and not dumped:
        "Your dinner has gone cold overnight."
    else:
        "The young woman has left your breakfast on the table."
    $ dumped = False
    call eat from _call_eat_1
    call visit
    call exercise
    jump days

label visit:
    if day == 2:
        show oldman neutral

        "The old man you walked directly behind in the forest is here."

        "He sits down on one of the chairs,{pause}staring in your direction."

        "You try to ask him questions,{pause}but he ignores you with great expertise."

        "He sits there silently for what seems to be a few hours before leaving."

    if day == 3:
        show oldman neutral

        "The old man is here again."

        "This time he is followed by a few young kids."

        "They don't look a day older than 10,{pause}but you can never be sure."

        "You call out to them,{pause}but they only look at you wide-eyed.{pause}You wonder if they even know how to speak."

        call kids

    elif day == 4:
        show oldman neutral

        "Today he's brought different kids than yesterday.{pause}You wonder if it's some rotated schedule."

        call kids
    elif day == 5:
        show oldman neutral

        "The old man is here with an old woman,{pause}they scurry around the cabin as you sit "

    elif day == 6:
        "The old man didn't come today."

    hide oldman neutral
    return

label kids:
    if defiance > 0 and not dumped and not leftovers:
        "One of the children reaches for your meal,{pause}left untouched on the table.{pause}Her hand is immediately swatted away by the old man."

        "She opens her mouth.{pause}You expected her to squeal,{pause}but no sound comes out."

        "The bizarre entourage merely sits around you for a while before seeing themselves out."

        $ leftovers = True
    else:
        "You know you’ve heard the children cry,{pause}so their silence now in your presence puzzles you."

        "All they’ve done in the cabin is play with dirt and dry grass."

        i "is that{ellipsis}a bone?"

        "A girl is wearing a small ribcage on her finger like a ring."

        "A smaller boy crawls to her and tries to suck on it."

        "You remind yourself that whatever meat it is in your soup is too big to be a small animal."

        if hunger >= 4:
            "You scratch your stomach."

        "Your visitors leave again.{pause}You are left alone."

    return

label exercise:
    "You unwrap the fabric on your leg and examine the bruises."

    if heal <= 2:
        "It's rather gnarly,{pause}the huge wound on your leg is barely starting to scab.{pause}The pain stops you from even contracting the muscles."
        if hunger <= 2:
            "Perhaps you need more food to heal."

    elif heal <= 4:
        "You can lift your leg by a little now,{pause}though it still causes you great pain."
        menu:
            "Exercise":
                $ rehab += 1
            "Leave it":
                $ heal += 1
    elif heal >= 5:
        "You can use the leg to stand now,{pause}albeit still needing the help of the stick."
        menu:
            "Exercise":
                $ rehab += 1
            "Leave it":
                $ heal += 1
    $ heal += 1
    return
