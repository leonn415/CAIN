#this label represents everytime the main character must eat
label eat:
    menu:
        "Eat it":
            $ hunger +=1
            $ defiance = 0
            call hunger_response from _call_hunger_response
        "Don’t eat":
            $ defiance += 1
            call defiance_response from _call_defiance_response
            call dispose
    return

#determines the response when you eat
label hunger_response:
    if hunger == 1:
        "The meat has an unfamiliar texture.{pause}You can’t quite put a finger on it."
    elif hunger == 2:
        "It’s the same dish as last time,{pause}no surprises here."
    elif hunger == 3:
        "You wonder if it’s some local game,{pause}perhaps a type of hog."
    elif hunger == 4:
        "The meat is actually not so bad once you get used to it."
    elif hunger == 5:
        "You finished the meal rather swiftly."
    elif hunger == 6:
        "Perhaps you have taken a liking to the food."
    elif hunger == 7:
        "You don't remember the last time you enjoyed a meal this much."
    elif hunger == 8:
        "You have been craving this,{pause}clearly."
    elif hunger == 9:
        "You devoured the soup,{pause}your stomach itches for more."
    elif hunger == 10:
        "You feel itchy."
    elif hunger == 11:
        ".….."
    elif hunger == 12:
        "Delicious?"
    elif hunger == 13:
        "Good."
    elif hunger == 14:
        "Come."
    elif hunger == 15:
        "To the temple."
    elif hunger == 16:
        "Hehe."
    else:
        "Delicious."
    return
#determines the response when you don’t eat
label defiance_response:
    if hunger >= 12:
        "How funny,{pause}you."
        return
    elif defiance <= 2:
        "You are hungry,{pause}but you decide to go without this meal."
        return
    elif defiance <= 4:
        "Your health is waning,{pause}perhaps you should eat something soon."
        return
    elif defiance <= 6:
        "You are losing control of your limbs, but you persist with starving yourself."
        return
    elif defiance == 7:
        "Your body will soon fail to support you."
        return
    elif defiance == 8:
        "Your foolish determination is lethal."
        return
    elif defiance == 9:
        jump starvation_ending

label dispose:
    menu:
        "Dispose of the soup?"
        "Yes":
            $ dumped = True
            $ pile += 1
            "You take the bowl to the pit latrine and pour the soup down the hole in the middle of the seat.{pause}The plops of the meat chunks wet and slimy."
        "No":
            pass
    return
