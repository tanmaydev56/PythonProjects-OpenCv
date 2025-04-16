n = 40
guess_it = 1
while (guess_it<=9):
    guess = int(input("guess kar bhai"))
    if guess < 40:
        print("uss no. se chotha hai")
    elif guess > 40:
        print("uss no. se bada hai ")
    else:
        print("jeeet gya bhaii tu")
        print("tune",guess_it,"try liye")
        break
    print("your tries",guess_it)
    guess_it = guess_it +1
if(guess_it>9):
    print("game over")
