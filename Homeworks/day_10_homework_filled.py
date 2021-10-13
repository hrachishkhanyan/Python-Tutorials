"""MODULES"""
import random
import os
import re
import time
import datetime
# 1. Hangman!
# Create the hangman game. A list containing random words is provided. Each time the program runs, one random word must
# be selected. Then the user will try to guess the letters of the word. They will have lives equal to the length of the
# word. Now, about the formatting. Say we have the word car. The program must then output underscores equal to the
# length of the word.

# Guess a letter!
# _ _ _
#
# if we input 'a', the program will output:

# Guess a letter!
# _ a _

# and so on.

# Ստեղծում ենք մեր սեփական "Կախաղան" խաղը։ Ծրագիրը պահելու է պատահական բառ տրված "random_words" ֆայլից: Խաղացողը պետք է
# գուշակի տառ։ Եթե տառը բառի մեջ գոյություն չունի, խաղացողը կորցնում է "կյանք" (կյանքերը բառի երկարության չափ են): Եթե
# տառը կա, այն բացվում է և խաղացողը անցնում է հաջորդ տառը գուշակելուն։ Ծրագրի աշխատանքը պետք է հետևյալ տեսքն ունենա։
# Ենթադրենք բառը car է։ Կոնսոլում հետևյալ տեսքստն ենք տեսնելու

# Guess a letter!
# _ _ _

# Եթե ներմուծենք a, կստանանք հետևյալ տեսքստը

# Guess a letter!
# _ a _

# և այդպես շարունակ։ Եթե խաղացողի կյանքերը սպառվեն, տեղեկացրեք նրան և խաղից դուրս եկեք։ Հաղթելու դեպքում տպեք
# շնորհավորանք

# with open(r'C:\Users\hrach\Downloads\random_words (1).txt', 'r') as file:
#     words = file.readlines().copy()
#     print(words)
#     length = len(words)
#     random_num = random.randint(0, length)
#
#     random_word = words[random_num].replace('\n', '')
#
# word_len = len(random_word)
#
# prompt = ['_ ' for i in range(word_len)]
# lives = word_len

# while True:
#     print('Guess the word!')
#
#     print(''.join(prompt))
#
#     guessed_letter = input('Guess a letter...')
#     random_word_list = list(random_word)
#
#     if guessed_letter in random_word:
#         indexes = []
#
#         for i in range(len(random_word)):
#             if random_word[i] == guessed_letter:
#                 index = random_word_list.index(guessed_letter)
#                 indexes.append(index)
#                 random_word_list[index] = ''
#         print(indexes)
#         for j in range(len(prompt)):
#             if j in indexes:
#                 prompt[j] = guessed_letter
#
#         index = random_word.index(guessed_letter)
#
#         prompt[index] = guessed_letter
#     else:
#         lives -= 1
#         print(f'The letter is not in the word. Lives left: {lives}')
#
#     if ''.join(prompt) == random_word:
#         print(f'Congrats! The word was {random_word}')
#         break
#
#     if lives < 1:
#         print(f'You have lost... The word was {random_word}')
#         break


# 2. Write a function that will return the longest word in the random words file from the previous exercise.
# Գրել ֆունկցիա, որը կվերադարձնի "random_words" ֆայլի ամենաերկար բառը։


def longest_word(path):
    with open(path, 'r') as file:
        words = file.readlines().copy()
        length = 0
        res = ''

        for word in words:
            if len(word) > length:
                length = len(word)
                res = word

    return res


print(longest_word('./random_words.txt'))

# def len_word(n):
#
#     res = re.findall(r"\w+", n)  # 'car, exercise, function, Write'
#     word = max(res, key=lambda x: len(x))
#     return word
#
#
# random_words = 'car, exercise, function, Write'
# print(len_word(random_words))



# 3. Write a function that will take a string containing the path to a file as an argument and return its size in
# kilobytes.
# Գրել ֆունկցիա, որը կվերցնի սթրինգ արգումենտ։ Սթրինգը պետք է լինի որոշակի ֆայլի path-ը։ Ապա վերադարձնել այդ ֆայլի
# չափսերը կիլոբայթերով։ Հուշում՝ օգտվել os մոդուլից:
# path = './random_words.txt'
# print(f'{os.stat(path).st_size} kb')

# 4. Create a random number generator without using random module. The implementation is up to you. You may use
# current timestamp as a random seed.
# Գրել ֆունկցիա, որը կվերադարձնի պատահական թիվ։ Պատահական թվերի գեներատոր պարունակող մոդուլ չօգտագործել։ Իմպլեմենտացիան
# կախված է ձեզնից։ Մտածեք որոշակի ալգորիթմ և ըստ դրա գեներացրեք թիվ։ Կարող եք օգտագործել մեր անցած seed-ի գաղափարը։


def rand_gen(seed, end=None):
    random_number = int(str(seed)[-4:-1])

    if end:
        return random_number % end

    return random_number


print(rand_gen(time.time(), 50))

# 5. Create a file and put your shopping list in it. The file must start with current day's date.
# Ստեղծել ֆայլ, որը կպահի ձեր գնումների ցուցակը (ինչ ապրանք։ քանի հատ)։ Ֆայլը պետք է սկսվի տվյալ օրվա ամսաթվով։


def create_shopping_list(path, food, quantity):
    mod = 'w'
    if os.path.exists(path):
        mod = 'a'

    with open(path, mod) as file:
        if mod == 'w':
            today = datetime.datetime.now()

            print(today.strftime('%d/%m/%y'), file=file)

        file.write(f'{food}: {quantity}\n')


create_shopping_list('./test.txt', 'Fish', '2kg')
create_shopping_list('./test.txt', 'Egg', '10')

create_shopping_list('./test.txt', 'Rice', '1kg')


# def guess_the_words(word):
#     secret = word
#     print(secret)
#     guesses = 'aeiou'
#     lives = len(secret)
#     while lives > 0:
#         missed = 0
#         for letter in secret:
#             if letter in guesses:
#                 print(letter, end=' ')
#             else:
#                 print('_', end=' ')
#                 missed += 1
#
#         print()
#
#         if missed == 0:
#             print('\nYou Win!')
#             print('Thank you for game')
#             break
#
#         guess = input('\nguess a letter: ')
#         guesses += guess
#
#         if guess not in secret:
#             lives -= 1
#
#             print('\n', lives, 'more lives')
#             if lives == 0:
#                 print('\n\nThe word was')
#                 print(secret)
#                 return secret
#
#
# print(guess_the_words(random_word))