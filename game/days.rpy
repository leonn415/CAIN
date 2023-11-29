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
    jump days

label visit:
    "The old man you walked directly behind through the forest is here."
