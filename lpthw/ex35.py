from sys import exit


def gold_room():
    print("This room is full of gold. How much do you take?")
    try:
        choice = int(input("> "))
    except ValueError:
        print("Man, learn to type a number. How much gold do you take?")
        choice = int(input("> "))
    if choice < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
    while True:
        choice = input("> ")
        if choice == "take honey":
            dead("The bear looks at you and then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear is enraged. It chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulu_room():
    print("Here you see the great evil Cthulu.")
    print("He, it, whatever, stares at you, and you go insane.")
    print("Do you flee for your life, or eat your head?")
    choice = input("> ")
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Yum!")
    else:
        cthulu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)


def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which door do you take?")
    choice = input("> ")
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
