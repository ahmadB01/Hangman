import datas
from os import system

restart = 'Y'
drawings = datas.get_drawings()

# replay loop
while restart == 'Y':
    system('clear')
    restart = ' '
    word = datas.get_random_word()
    display = '*' * len(word)
    lives = len(drawings)-1
    
    # scores initialization
    username, score, scores = datas.init_scores()
    print('{}\'s score : {}'.format(username, score))
    
    # hangman game
    while display != word and lives >= 0:
        # drawing display
        for drawing in drawings[::-1][lives]:
            print('\t\t'+drawing)
        print('Word: {}'.format(display))

        letter = ''
        while not letter.isalpha() or len(letter) != 1:
            letter = input('Enter a letter: ').upper()
        
        if letter in word:
            print('Yes, the word contains the \'{}\' letter!'.format(letter))
            for i, k in enumerate(word):
                if k == letter:
                    display = display[:i] + letter + display[i+1:]
        else:
            print('Nop, the word does not contain the \'{}\' letter!'.format(letter))
            lives -= 1
                
    system('clear')
    if lives >= 0:
        # won
        score += lives
        print('Congratulations, you won with {} tries left!'.format(lives))
        print('Therefore, {}\'s score is {}'.format(username, score))
    else:
        # lost
        print('You lost! {}\'s score is {}'.format(username, score))

    print('The word is indeed : {}'.format(word))

    # scores registration
    scores[username] = score
    datas.register_scores(scores)

    while restart not in ('Y', 'N'):
        restart = input('Do you want to restart? (Y/N) ')[0].upper()
        
print('Goodbye!')