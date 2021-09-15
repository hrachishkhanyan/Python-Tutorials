"""VARIABLES, TYPES, MAINLY STRINGS"""

# 1. Create a new string which will be a palindrome from the given string․
# Ստեղծել նոր սթրինգ, որը տրված սթրինգի պալինդրոմը կլինի։

str_1 = 'Hello!'
print(str_1 + str_1[::-1])

# 2. Using slicing, create a new string which will contain the second and last words of the given string.
# Ստեղծել նոր սթրինգ, որը կպարունակի տրված սթրինգի երկրորդ և վերջին բառերը։

str_2 = 'We are on a quest for the holy grail!'
print(str_2[3:6], str_2[-6:-1])

# 3. Write a program that will output user's input to the console․
# Գրել ծրագիր, որը կտպի օգտատիրոջ հավաքածը կոնսոլում։

# print(input('Enter something: '))

# 4. Write a program that will prompt the user to enter a number. Then by using string formatting, output the given
# string containing the number instead of {}
# Գրել ծրագիր, որը կպահանջի ներմուծել թիվ։ Այնուհետև տրված սթրինգում {} փոխարինել այդ թվով։

hhg = 'First shalt thou take out the Holy Pin. Then shalt thou count to {}, no more, no less.'
x = int(input('Enter your number: '))
print(hhg.format(x))
# print(hhg.replace('{}', x))

# 5. Change the formatting of the poem, so the output matches the following:
# Փոխել տրված բանաստեղծության ֆորմատավորումը, որպեսզի այն տպվի հետևյալ տեսքով։

# All that is gold does not glitter,
#       Not all those who wander are lost;
#           The old that is strong does not wither,
#               Deep roots are not reached by the frost.

poem = """All that is gold does not glitter,
\t\tNot all those who wander are lost;
\t\t\tThe old that is strong does not wither,
\t\t\t\tDeep roots are not reached by the frost.
"""

print(poem)

# 6. Let x = 10 and y = 3. Print the result of x / y to up to 4 decimals.
# Հաշվել x / y-ը և տպել արդյունքը ստորակետից հետո 4 թվի ճշտությամբ։

x = 10
y = 3
# z = x / y
# print('{:.4f}'.format(z))
print('{:.4f}'.format(x / y))

# 7. Modify the given string, so that the first letter is the only upper-case one.
# Մոդիֆիկացնել տրված սթրինգը, որպեսզի մեծատառով լինի միայն առաջին տառը։

str_3 = 'MORNING, NICE DAY FOR FISHING AIN\'T IT?!'
print(str_3.lower().capitalize())

# 8. Replace the 'a'-s in the string with an empty string.
# Ջնջել սթրինգի բոլոր 'a'-երը։

str_4 = 'Are actors anticipating academy awards at all?'

# 9. Given a string, format it in such a way so that the output looks like this․
# Տրված սթրինգը տպել հետևյալ ֆորմատով՝
# -> "I am King       Arthur       of Camelot        , will you
#                                              join my quest for the Holy Grail     ?"

string = 'I am King Arthur of Camelot, will you join my quest for the Holy Grail?'

# 10. Write a program that will tell you whether the inputted number is odd.
# Ստուգել արդյո՞ք օգտատիրոջ կողմից ներմուծված թիվը կենտ է։

x = int(input())

"""This is comment"""

print('The number is odd: ', x % 2 == 1)


