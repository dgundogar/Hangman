import random


print("H A N G M A N")
print('Type "play" to play the game, "exit" to quit:')
choice = input()
print()
if choice == 'play':
    words = ['python', 'java', 'kotlin', 'javascript']
    correct = random.choice(words)
    list_correct = list('-' * len(correct))
    guesses = []
    remaining_attempts = 8
    while remaining_attempts > 0:
        print()
        print("".join(list_correct))
        letter = input("Input a letter: ")
        if len(letter) != 1:
            print("You should input a single letter")
        elif letter.islower() != 1 or letter.isalpha() != 1:
            print("Please enter a lowercase English letter")
        elif letter in guesses:
            print("You've already guessed this letter")
        elif letter in correct:
            for i in range(len(correct)):
                if correct[i] == letter:
                    list_correct[i] = letter
        elif letter not in correct:
            print("That letter doesn't appear in the word")
            remaining_attempts = remaining_attempts - 1
        guesses.append(letter)
        if '-' not in list_correct:
            print("You guessed the word", "".join(list_correct), "!\nYou survived!")
            break
    else:
        print("You lost!")
