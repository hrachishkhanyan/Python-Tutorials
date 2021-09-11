"""LOOPS"""

# 1. Write a program to loop through a range from 0 to 100 and print the even numbers only.
# Գրել ցիկլ, որը կտպի 0-100 զույգ թվերը։

# for i in range(0, 101, 2):
#     print(i)
#
# for i in range(0, 101):
#     if i % 2 == 0:
#         print(i)

# 2. Write a program to loop through a range from 350 to 677 and print only numbers ending with 7.
# Գրել ցիկլ, որը կտպի 350-677 միջակայքի միայն այն թվերը, որոնք ավարտվում են 7-ով։

# for i in range(350, 678):
#     if i % 10 == 7:
#         print(i)

# 3. Print every 6th number from 0 to 100.
# Տպել 0-100 ամեն 6-րդ թիվը։

# for i in range(0, 101, 6):
#     print(i)

# 4. Write a program that will output the multiplication table.
# Գրել ծրագիր, որը կտպի բազմապատկման աղյուսակը։

# for i in range(1, 10):
#     for j in range(1, 10):
#         print('{:>2} * {} = {:>2}'.format(i, j, i * j), end='\t')
#     print()

# 5. Write the FizzBuzz program. Only this time, loop through a range of 0-100 and for each iteration, print Fizz,
# if the loop variable is divisible by 3, Buzz, if it's divisible by 5, and FizzBuzz if it's divisible by both.
# Գրել նախորդ դասի FizzBuzz ծրագիրը, սակայն այս անգամ ցիկլի միջոցով տպել առաջին 100 թվերի FizzBuzz արժեքները։

# for i in range(0, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)

# x = range(1,101)
# for i in x:
#     if i % 15 == 0:
#         print('{} FizzBuzz'.format(i))
#     elif i % 5 == 0:
#         print('{} Buzz'.format(i))
#     elif i % 3 == 0:
#         print('{} Fizz'.format(i))
#     else:
#         print(i)

# for i in range(1, 101):
#     result = ''
#
#     if i % 3 == 0:
#         result += 'Fizz'
#     if i % 5 == 0:
#         result += 'Buzz'
#
#     if result == '':
#         result = i
#
#     print(result)

# 6. Write a program that will loop through a range of 0-1000 and print out only prime numbers.
# Տպել 0-1000 միջակայքի պարզ թվերը։

# prime = True
#
# for i in range(3, 1001):
#     for k in range(2, i):
#         if i % k == 0:
#             prime = False
#
#     if prime:
#         print(i, end=' ')
#     else:
#         prime = True
import math

# for i in range(2, 1001):
#     for j in range(2, int(i / 2) + 1):
#         if i % j == 0:
#             break
#     else:
#         print(i)

# 7. Write a program that will keep a random number from 1-10 (use random package). The user must guess that number.
# They can input as many times as they want. Terminate the program with a congratulation message when the user has
# guessed the number.

# To make this more interesting, you can add lives (attempt limit) for the user, and after each guess let them know if
# their guess was larger or smaller from the actual number.

# Գրել խաղ, որը կպահի 1-100 պատահական թիվ։ Խաղացողը պետք է գուշակի այդ թիվը։ Նա կարող է այնքան անգամ գուշակել, ինչքան
# ցանկանում է։ Ավարտել ծրագիրը շնորհավորանքի նամակ տպելով, երբ խաղացողը թիվը գուշակի։

# Խաղն ավելի հետաքրքիր դարձնելու համար կարելի է սահմանափակել հնարավորությունների քանակը։ Կարելի է նաև խաղացողին
# տեղեկացնել, արդյո՞ք նրա մուտքագրած թիվը մեծ է պահված թվից, թե փոքր։

# import random
#
# rand_num = random.randint(0, 100)
# lives = 8
#
# while True:
#     if lives == 0:
#         print('Loser!')
#         break
#
#     print(f'You have {lives} lives left...')
#     guessed_num = int(input('Guess a number: '))
#
#     if guessed_num == rand_num:
#         print('Congrats!')
#         break
#     elif guessed_num > rand_num:
#         print('Guess is larger than the actual number')
#     else:
#         print('Guess is smaller than the actual number')
#
#     lives -= 1


"""Bonus"""

# 8. Given a string, print a string where for every character in the original, there are two characters.
# Տրված է սթրինգ։ Տպեք նոր սթրինգ, որը կպարունակի օրիգինալ սթրինգի բոլոր տառերը կրկնապատկված։

# Օրինակ, եթե ունենք հետևյալ սթրինգը՝ Monty, պետք է ստանանք MMoonnttyy

# string = 'Monty'
# result = ''
#
# for char in string:
#     result += 2 * char
#
# print(result)

# string = "Monty"
#
# for char in string:
#     print(char * 2, end="")

# 9. Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So
# "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
s = 'xxcaazz'
s1 = 'xxbaaz'

for i in range(len(s)):
    print(s[i:i + 2])
    print(s1[i:i + 2])

# 10. Reverse a string without the use of indexation (e.g. [::-1]).
# Շրջել սթրինգը առանց գործածելու str[::-1]

string = 'Monty'
result = ''

for i in range(len(string) - 1, -1, -1):
    result += string[i]

for i in range(0, len(string)):
    result += string[len(string) - 1 - i]
print(result)
