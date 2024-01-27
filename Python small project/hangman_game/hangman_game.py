import hangman_stages
import random
import words

random_words = random.choice(words.word)
# print(random_words)
print("Hey welcome to hanging man game!")
display = []
for each in random_words:
    display += '_'
print(display)
lives = 6
game_over = False
while not game_over:
    gauss_latter = input("Enter your latter").lower()  # t
    for position in range(len(random_words)):
        if random_words[position] == gauss_latter:
            display[position] = gauss_latter
    print(display)

    if gauss_latter not in random_words:
        lives -= 1
        print(f"wrong gauss you have only {lives} chances")
        print(hangman_stages.staeges[lives])
        if lives == 0:
            game_over = True
            print("you loss the game")
    if '_' not in display:
        game_over = True
        print('you win')
