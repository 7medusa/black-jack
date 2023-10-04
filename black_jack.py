from random import choice
colors = ["♦", "♥", "♣", "♠"]
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
black_jack = [10, "J", "Q", "K"]


def own_cards():
    global own_number1
    global own_number2
    global insgesamt_own
    own_number1 = choice(numbers)
    own_number2 = choice(numbers)
    own_card1 = f"{choice(colors)}{own_number1}"
    own_card2 = f"{choice(colors)}{own_number2}"
    print(f"own cards:\n{own_card1}\n{own_card2}\n")
    if own_number1 in black_jack:
        own_number1 = 10
    if own_number2 in black_jack:
        own_number2 = 10
    if own_number1 == "A":
        own_number1 = 11
    if own_number2 == "A":
        own_number2 = 11
    insgesamt_own = own_number1 + own_number2
    dealer_cards()


def dealer_cards():
    global dealer_number1
    global dealer_number2
    global insgesamt_dealer
    dealer_number1 = choice(numbers)
    dealer_number2 = choice(numbers)
    dealer_card1 = f"{choice(colors)}{dealer_number1}"
    print(f"dealer card number one:\n{dealer_card1}\n")
    if dealer_number1 in black_jack:
        dealer_number1 = 10
    if dealer_number2 in black_jack:
        dealer_number2 = 10
    if dealer_number1 == "A":
        dealer_number1 = 11
    if dealer_number2 == "A":
        dealer_number2 = 11
    insgesamt_dealer = dealer_number1 + dealer_number2
    black_jack_check()


def black_jack_check():
    if insgesamt_own == 21 and insgesamt_dealer == 21:
        print("both of you has a black jack\ntie")
    elif insgesamt_own == 21:
        print("you have a black jack\nwin")
        own_cards()
    elif insgesamt_dealer == 21:
        print("dealer has black jack\nlose")
        own_cards()
    else:
        add_cards()


def add_cards():
    global insgesamt_own
    while insgesamt_own < 22:
        eingabe = input("add a card?\n[y/n]>")
        if eingabe == "n":
            dealer_add_cards()
        elif eingabe == "y":
            new_number = choice(numbers)
            print(f"{choice(colors)} {new_number}")
            if new_number == "A":
                new_number = 11
            elif new_number in black_jack:
                new_number = 10
            insgesamt_own = insgesamt_own + new_number
            print(f"own value: {insgesamt_own}")
        else:
            print("error")
            return add_cards()
    print("too much cards")


def dealer_add_cards():
    global insgesamt_dealer
    global dealer_number1
    global dealer_number2
    if dealer_number1 in black_jack:
        dealer_number1 = 10
    if dealer_number2 in black_jack:
        dealer_number2 = 10
    if dealer_number1 == "A":
        dealer_number1 = 11
    if dealer_number2 == "A":
        dealer_number2 = 11
    while insgesamt_dealer < 17:
        new_number_dealer = choice(numbers)
        print(f"{choice(colors)} {new_number_dealer}")
        if new_number_dealer in black_jack:
            new_number_dealer = 10
        elif new_number_dealer == "A":
            new_number_dealer = 11
        insgesamt_dealer = insgesamt_dealer + new_number_dealer
    if insgesamt_dealer > 21:
        print("win")
        own_cards()
    comparison()


def comparison():
    print(f"own value: {insgesamt_own}")
    print(f"dealer value: {insgesamt_dealer}")
    if insgesamt_own == insgesamt_dealer:
        print("tie")
    elif insgesamt_own < insgesamt_dealer:
        print("lose")
    elif insgesamt_own > insgesamt_dealer:
        print("win")
    input("press an button to continue")
    print("\n\n\n\n\n\n\n")
    own_cards()


own_cards()
# A 2 werte gleichzeitig zuschreiben
# einsätze einarbeiten
