# Guess game with functions
import random

def main():
    global attempt
    attempt = 1                                                                 #uj játéknál visszaállítom 1-re a próbálkozások számát
    if victory_point < 0:
        print("\n*** GAME OVER ***\n*** Goodbye! ***")
        exit()
    else:
        print("Please, choose one of these:")
        print("\tEasy game(0-5): E\t\tMedium game(0-10): M\t\tHard game(0-20): H")
        if victory_point > 0:
            print(f"\tVisit the gift shop: G\tYour victory point(s): {victory_point} point(s)")
        print("\tEXIT: X\n")
        choice = str (input("Your choice:").lower() )

        if choice == "e": game(1,5)
        elif choice == "m": game(3,10)
        elif choice == "h": game(5,20)
        elif victory_point > 0 and choice == "g": gift_shop()
        elif choice == "x": exit()
        else:
            main()


def game(p, interval):
    global victory_point, attempt
    guessed_number = random.randint(0, interval)
    user_guess = userGuess(p, interval)

    while not guessed_number == user_guess:
        if attempt > 3:
            victory_point -= p
            print(f"\n *** YOU LOST! ***\nYou lost {p} extra point(s)")
            main()
        else:
            if user_guess < 0 or user_guess > interval:
                print(f"Warning! You should guess between 0 and {interval}!")
            else:
                if user_guess > guessed_number: print("Guessed number is smaller, try again")
                elif user_guess < guessed_number: print("Guessed number is greater, try again")
            user_guess = userGuess(p,interval)

    victory_point += p
    print(f"\n *** You win! ***\nThe guessed number is {guessed_number}, you win {p} extra point(s)!")
    main()

def userGuess(p,interval):       #csak lecsekkolja, hogy számot adtam-e meg
    global attempt
    attempt +=1                                 #számolja a kisérleteket, akkor is ha nem szám!
    try: user_guess = int(input("Your guess?"))
    except:
        print("Only number please! Try again!")
        game(p,interval)
    return user_guess

def gift_shop():
    global victory_point
    giftShop = {1:"Candy", 3:"Chocolate bar", 5:"Ice cream", 10:"Guided tour to the moon!"}
    print(f"You can buy a gift, if you have enough victory point(s) for it!\n"
          f"You have {victory_point} point(s)!\n\n"
          f"\tFor 1 point you can buy a {giftShop[1]}!\n"
          f"\tFor 3 points you can buy a {giftShop[3]}!\n"
          f"\tFor 5 points you can buy a {giftShop[5]}!\n"
          f"\tFor 10 points you can buy {giftShop[10]}\n")

    gift_point = int( input("How many point(s) would you like to spend?\n") )

    if gift_point > victory_point:
        print("You have not enough points, try again")
        gift_shop()

    try:
       print(f"You spent {gift_point} point(s), and you get a/an {giftShop[gift_point]}\n")
       victory_point -= gift_point
    except:
        print("You can only spend exactly 1, 3, 5 or 10 points, please typ it correctly!\n")
    main()

victory_point, attempt = 0, 1
main()