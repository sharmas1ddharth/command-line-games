import random

words = ['shoes', 'socks', 'shirt', 'slippers', 'sweater']

word = random.choice(words)

print('\nGuess the item')

guesses = ''

turns = 10

while turns > 0:
    fail = 0

    for char in word:
        if char in guesses:
            print(char)
        else:
            print('_ ')

            fail += 1

    if fail == 0:
        print('You win')
        print('The word is', word)
        break

    guess = input('\n\nGuess the item : ')
    guesses += guess

    if guess not in word:
        turns -= 1
        print('wrong')
        print('You have', + turns,'left')

        if turns == 0:
            print('You lose')