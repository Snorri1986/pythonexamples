from random import choice

capital = "Topeka"

bird = "Western Meadowlark"

flower = "Sunflower"

song = "Home on the range"

def randomfunfact():
    funfacts = [
        "Kansas is considered flat, but it does have a mountain.",
        "Wichita is the largest city in the state, but many would guess it is Kanasas City.",
        "A considerable portion of Kanasas City is actually in Missouri."
    ]

    index = choice("0123")

    print(funfacts[int(index)])