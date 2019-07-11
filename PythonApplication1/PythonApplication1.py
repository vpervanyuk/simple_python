import module1 

game = module1.Game(3)

while True:
    game.set_new_number()
    while True:
        key = input("guess the number: ")  
        try:
            guess = int(key)
            bulls, cows, code = game.check_bulls_cows(guess)
            if code == 1:
                print("you win!")
                break
            elif code == -1:
                print("wrong number! (h for help)")
                continue
            elif code == 0:
                print("bulls:", bulls, "cows:", cows)
                continue
        except:
            if key == 'g':
                print("the number was: ", game.number)
                break
            elif key == 'h':
                print("help :)")
                continue
            else:
                print("wrong number! (h for help)")
                continue
    play_again = input("play again (y/n)? ")
    if play_again != 'y':
        break



