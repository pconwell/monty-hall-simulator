import random

debug = False

def monty():
    # There are only three possible combinations of door orders. The car can only either be behind door A, door B or door C.
    # For the purpose of the simulation, we could put the car behind the same door each time and the math would work out
    # just fine, but for the sake of completness we will randomly pick one of the three possibilities that we explicitly spell out:

    c = {'A':{'One':'Car','Two':'Goat','Three':'Goat'},
         'B':{'One':'Goat','Two':'Car','Three':'Goat'},
         'C':{'One':'Goat','Two':'Goat','Three':'Car'}
         }

    stage = c[random.choice(['A', 'B', 'C'])]
    if debug: print(f"stage layout: {stage}")

    # Now that we have one of the three possible door orders, we need to pick our door (remember, in the real game, you
    # don't know what's behind the door). The host will also not pick a door with the car for the 'switch'.

    doors = ['One', 'Two', 'Three']
    pick = doors.pop(random.randrange(len(doors)))

    # We've now picked our (random) door. One of two things can happen from here: Either we picked the car and the host will
    # reveal either of the other two doors OR we picked a goat and the host will show us the other goat.

    if stage[pick] == 'Car':
        if debug: print(f"initial choice: {pick}")
        if debug: print('car was picked, picking one of the two remaining doors')
        show = doors.pop(random.randrange(len(doors)))
        hide = doors.pop(random.randrange(len(doors)))
    else:
        if debug: print(f"initial choice: {pick}")
        if debug: print('car was not picked, picking the remaining goat')
        for i in doors:
            if stage[i] == 'Goat':
                show = i
            else:
                hide = i

    if debug: print(f"pick: {pick} ({stage[pick]}) - remember, this is still hidden")
    if debug: print(f"show: {show} ({stage[show]})")
    if debug: print(f"hide: {hide} ({stage[hide]})")

    # now that we have picked a (random) door and have been shown one of the remaining doors, let's (randomly) decide
    # if we want to swap doors. In other words, we will flip a coin to decide if we will swap the pick and hide doors.

    swap = random.choice([True, False])

    if debug: print(f"Swap? {swap}")

    if swap:
        outcome = hide
    else:
        outcome = pick

    if debug: print(f"final door choice: {outcome} ({stage[outcome]})")

    return [swap, stage[outcome]]

l = []
for i in range(100):
    s, o = monty()
    l.append((s, o))

for i in l:
    print(i)

print('done')
