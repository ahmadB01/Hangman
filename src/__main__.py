import utils
from os import system

restart = 'Y'
drawings = utils.get_drawings()

# replay loop
while restart == 'Y':
    system('clear')
    restart = ' '
    word = utils.get_random_word()
    display = '*' * len(word)
    lives = len(drawings)-1
    
    # scores initialization
    username, score, scores = utils.init_scores()
    print(f'{username}\'s score : {score}')
    
    # hangman game
    while display != word and lives >= 0:
        # drawing display
        for drawing in drawings[::-1][lives]:
            print(f'\t\t{drawing}')
        print(f'Word: {display}')

        letter = ''
        while not letter.isalpha() or len(letter) != 1:
            letter = input('Enter a letter: ').upper()
        
        if letter in word:
            print(f'Yes, the word contains the \'{letter}\' letter!')
            for i, k in enumerate(word):
                if k == letter:
                    display = display[:i] + letter + display[i+1:]
        else:
            print(f'Nop, the word does not contain the \'{letter}\' letter!')
            lives -= 1
                
    system('clear')
    if lives >= 0:
        # won
        score += lives
        print(f'Congratulations, you won with {lives} tries left!')
        print(f'Therefore, {username}\'s score is {score}')
    else:
        # lost
        print(f'You lost! {username}\'s score is {score}')

    print(f'The word is indeed : {word}')

    # scores registration
    scores[username] = score
    utils.register_scores(scores)

    while restart not in ('Y', 'N'):
        restart = input('Do you want to restart? (Y/N) ')[0].upper()
        
print('Goodbye!')
