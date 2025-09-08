from random import choice



#declaring game variables
words = ["hungerGame","water","paper"]
words = choice(words)
guessed = []
lives = 7
game_over = False


while not game_over:
    ans = input("Type quite or guess a letter: ")

    try:
        guesses = ["_"] * words(len)

    except:
        if ans == "quit":
         print("How sad, Thanks for playing anyway")
         game_over = True
    
        elif ans in words:
         print("You guessed correctly")
         hidden_word = "".join(guesses)
         print(f"Word to guess: {hidden_word}")
         print(f"Lives left: {lives}")
         ans = input()
        

    else:
        lives = -1
        print(f"Sorry lad, you lost a life, lives left: {lives} ")

    





