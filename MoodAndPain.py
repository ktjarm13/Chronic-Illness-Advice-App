pain=int(input("What is your pain level?\n"))
mood=int(input("What is your mood level?\n"))
if pain<=4:
    print("Do some yoga.")
elif pain>=9:
    print("Lie down and rest.")
else:
    print("Have a bath.")
if mood<=2:
    print("Time to cry.")
elif mood>=7:
    print("Who are you?")
else:
    print("Move yo body or yo mind.")