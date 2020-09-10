import random
words = ["water","laptop","smartphone"]
hints = ["You can drink it","This thing needs for study remotely","You can call with this thing"] 
random_word = random.randint(0,2)
word = words[random_word]
hint = hints[random_word] # Have a list of words, and randomly pick a word from a list
board = list("_" * len(word))
game_over = False
r = 0
print(" -"*10)
print("This is the Guess Game!")
print(" -"*10)
while not game_over:
    a = 0
    r += 1
    if r%2 == 0:
        b = 0
        print(f"Guess a word: {' '.join(board)}")
        print(f"Player 2\'s turn: ")
        print(f"Hint: {hint}")
        user_guess = input("Enter the word or the letter: ")
        user_guess = user_guess.lower()
        if len(user_guess) == 1:
            for i in range(len(word)):
                if word[i] == user_guess:
                    board[i] = user_guess
                    b += 1
            if b == 0:
                print(" -"*10)
                print("Incorrect, think again...") # if the letter is incorrect, show some message
                print(" -"*10)
            for i in range(len(word)):  # if the letter is already guessed, do not change anything
                if word[i] == board[i]:
                    a += 1
            if a == len(word):
                print(" -"*10)
                print("Player 2 guessed the word!!")
                game_over = True
        else:
            if user_guess == word:
                print("Correct! Congratulations!")
                for i in range(len(word)):
                    board[i] = word[i]
                game_over = True
            else:
                print("Incorrect, think again...")
        print(f"Guess word: {' '.join(board)}")
        print(" -"*10)
    else:
        b = 0
        print(f"Guess a word: {' '.join(board)}")
        print(f"Player 1\'s turn: ")
        print(f"Hint: {hint}")
        user_guess = input("Enter the word or the letter: ")
        user_guess = user_guess.lower()
        if len(user_guess) == 1:
            for i in range(len(word)):
                if word[i] == user_guess:
                    board[i] = user_guess
                    b += 1
            if b == 0:
                print(" -"*10)
                print("Incorrect, think again...") # if the letter is incorrect, show some message
                print(" -"*10)
            for i in range(len(word)):  # if the letter is already guessed, do not change anything
                if word[i] == board[i]:
                    a += 1
            if a == len(word):
                print(" -"*10)
                print("Player 1 guessed the word!!")
                game_over = True
        else:
            if user_guess == word:
                print("Correct! Congratulations!")
                for i in range(len(word)):
                    board[i] = word[i]
                game_over = True
            else:
                print("Incorrect, think again.")
        print(f"Guess word: {' '.join(board)}")
        print(" -"*10)


# if the letter is incorrect, show some message               /Checked/
# if the letter is already guessed, do not change anything    /Checked/
# randomly add some points if a letter is guessed      
# Have a list of words, and randomly pick a word from a list  /Checked/

# Two players game. Player one's turn. Guess the word.        /Checked/
