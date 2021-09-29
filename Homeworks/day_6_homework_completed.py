"""FUNCTIONS"""
import random

# 1. We'll say that an element in an array is "alone" if there are values before and after it, and those values are
# different from it. Return a version of the given array where every instance of the given value which is alone is
# replaced by whichever value to its left or right is larger.
# Ենթադրենք տարրը "միայնակ" է, եթե նրանից առաջ կամ հետո գտնվող տարրերի արժեքը տարբերվում է իր արժեքից։ Ստեղծել ֆունկցիա,
# որը կվերցնի լիստ որպես արգումենտ և կվերադարձնի այդ լիստը ձևափոխված այնպես, որ բոլոր միայնակ տարրերը փոխարինված լինեն
# իրենցից աջ կամ ձախ գտնվող առավելագույն արժեք ունեցող տարրով ([4, 4, 1, 3, 3], այստեղ 1-ը կփոխարինվի 4-ով):

# def not_alone(arr: list) -> list:
#     for i in range(1, len(arr) - 1):
#         right = arr[i + 1]
#         left = arr[i - 1]
#         if arr[i] != left and arr[i] != right:
#             arr[i] = left if left > right else right
#             # lst[i] = max([right, left])
#     return arr
#
#
# lst = [4, 4, 1, 3, 3, 2, 2, 1, 5, 5, 6, 7]
#
# # print(not_alone(lst))
# assert not_alone(lst) == [4, 4, 4, 3, 3, 2, 2, 5, 5, 5, 7, 7], 'Something\'s wrong'
#
#
# def arr(a: list) -> list:
#     for i in range(len(a)):
#         if a[i + 1] == 'alone' and a[i] != a[i + 2]:
#             if len(a[i]) > len(a[i + 2]):
#                 a[i + 1] = a[i]
#                 # return a
#             elif len(a[i]) < len(a[i + 2]):
#                 a[i + 1] = a[i + 2]
#                 # return a
#         else:
#             print("Error")
#             return a
#     return a
#
#
# l = ['Hello', 'alone', 'go', 'book', 'alone', 'cooperation']
#
#
# lst = [1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 5, 5, 5]
# def rep(arr: list):
#     for i in range(len(arr)):
#         if (i != 0 and i != -1) and arr[i] != arr[i-1] and arr[i] != arr[i+1]:
#             if arr[i] < arr[i-1] < arr[i+1]:
#                 arr[i] = arr[i+1]
#             elif arr[i] < arr[i+1] < arr[i-1]:
#                 arr[i] = arr[i-1]
#
#     return arr
#
#
# print(rep(lst))
#
# # 2. Write a function to create and print a list where the values are square of numbers between 1 and 30
# # (both included).
# # Ստեղծել ֆունկցիա, որը կստեղծի և կտպի լիստ, որի արժեքները [1, 30] միջակայքում գտնվող թվերի քառակուսիներն են։
#
#
# def print_list():
#     lst = [i ** 2 for i in range(1, 31)]
#
#     print(lst)
#
#
# print_list()
# # 3. Write a function which will take one argument n. Return a list of size n, that will contain random numbers
# # from (-100, 400).
# # Ստեղծել ֆունկցիա, որը կվերցնի մեկ արգումենտ՝ n: Վերադարձնել n երկարությամբ լիստ, որը կպարունակի (-100, 400)
# # միջակայքում գտնվող պատահական թվեր։
#
#
# def rand_list(n: int) -> list:
#     lst = []
#
#     for _ in range(n):
#         lst.append(random.randint(-100, 400))
#
#     return lst
#
# print(rand_list(10))
#
# # 4. Write a function, that will take a list of words as an argument and return all the words in the list that start
# # with a vowel.
# # Ստեղծել ֆունկցիա, որը կվերցնի լիստ որպես արգումենտ (սթրինգերի) և կվերադարձնի մեկ այլ լիստ, որը կպարունակի այդ լիստի
# # բոլոր այն բառերը, որոնք սկվում են ձայնավորով։
#
# poem = '''All that is gold does not glitter,
# Not all those who wander are lost;
# The old that is strong does not wither,
# Deep roots are not reached by the frost.
#
# From the ashes a fire shall be woken,
# A light from the shadows shall spring;
# Renewed shall be blade that was broken,
# The crownless again shall be king.'''
#
#
# def only_vowel_words(string: str) -> list:
#     vowels = ['e', 'u', 'o', 'i', 'a']
#     # without_punct = [item[:-1] if item[-1] in [',', ';', '.'] else item for item in string.split()]
#
#     vowel_words = [item for item in string.split() if item[0].lower() in vowels]
#
#     return vowel_words
#
#
# print(only_vowel_words(poem))


# 5. We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
# Write a function to return the number of small bars to use, assuming we always use big bars before small bars. Return
# -1 if it can't be done.
# Մենք ուզում ենք պատրաստել որոշակի x կշռով շոկոլադ։ Ունենք փոքր և մեծ շոկոլադե սալիկներ, որոնք համապատասխանաբար
# կշռում են 1 և 5 կգ։ x կգ շոկոլադը պատրաստելու համար առաջինը օգտագործելու ենք մեծ սալիկները, ապա փոքր։ Սալիկները
# կտրատել հնարավոր չէ։ Գրել ֆունկցիա, որը կվերադարձնի անհրաժեշտ փոքր սալիկների քանակը։ Եթե հնարավոր չէ տրված սալիկների
# քանակով պատրաստել անհրաժեշտ շոկոլադը՝ վերադարձնել -1։
# Ֆւնկցիայի սահմանումն ունի հետևյալ տեսքը, որտեղ small, big -> հասանելի փոքր և մեծ սալիկների քանակը, իսկ goal-ը
# վերոնշյալ x-ն է։

goal = 7
small = 3
big = 2

def make_chocolate(small: int, big: int, goal: int):
    # if goal - 5 * big > small:
    #     return -1
    #
    # div = goal - goal % (5 * big)
    #
    # if div % small == 0:
    rem = 0

    if goal >= 5 * big:
        rem = goal - 5 * big
    else:
        rem = goal % 5

    if rem <= small:
        return rem

    return -1


print(make_chocolate(3, 1, 8))

# 6. Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other
# is "far", differing from both other values by 2 or more. Return False otherwise.
# Գրել ֆունկցիա, որը կվերցնի երեք ամբողջ թիվ որպես արգումենտ։ Վերադարձնել True, եթե b-ն կամ c-ն իրենց արժեքով
# տարբերվում են a-ից առավելագույնը 1-ով, երբ միաժամանակ մյուս երկուսը տարբերվում են իրարից 2-ով։ Հակառակ դեպքում
# վերադարձնել False։
# TODO Ուղղել հայերեն պահանջը


def close_far(a: int, b: int, c: int) -> bool:
    d_ab = abs(a - b)
    d_ac = abs(a - c)
    d_bc = abs(c - b)

    if (d_ab <= 1 and d_ac >= 2 and d_bc >= 2) or\
        (d_ac <= 1 and d_ab >= 2 and d_bc >= 2):
        return True

    return False


print(close_far(2, 3, 10))

def mod(a, b ,c):
    if abs(abs(a)-abs(b)) <= 1 and abs(abs(a)-abs(c)) >= 2:
        return True
    elif abs(abs(a)-abs(c)) <= 1 and abs(abs(a)-abs(b)) >= 2:
        return True
    else:
        return False

# 7. Write a function that gets a numerical list as an argument. Find the sum of the elements. If a certain element is
# 13 stop the count and return whatever was the sum before that.
# Ստեղծել ֆունկցիա, որը կգումարի տրված լիստի բոլոր թվերը և կվերադարձնի այն։ Եթե տարրերից մեկը 13 է, դադարեցնել հաշվարկը
# և վերադարձնել մինչև այդ պահը հաշված գումարը։

example_list = [4, 1, 2253, 32, 13, 64, 1, 90]


def unlucky_number(arr: list) -> int:
    total = 0

    for item in arr:
        if item == 13:
            print('Loop soon will be broken')
            return -1

        total += item

    for item in arr:
        total -= item

    print('Loop is broken')
    return total


s = unlucky_number(example_list)

print(f'{s=}')

# 8. Write down the following functions in a lambda form
# Գրել հետևյալ ֆունկցիաների լամբդա տարբերակները


def square(x):
    return x ** 2


sq = lambda x: x ** 2


def circle_area(r, pi=3.14):
    return pi * r ** 2


ca = lambda r, pi=3.14: pi * (r ** 2)


def sum_to_power(x, y, p):
    return (x + y) ** p


stp = lambda x, y, p: (x + y) ** p
# 9. Create a list from 1-100. Using the filter function, return a new list containing only the numbers ending with 7.
# Ստեղծել 1-100 թվերը պարունակող լիստ։ Օգտագործելով ֆիլտր ֆունկցիան, վերադարձնել նոր լիստ, որը կպարունակի օրիգինալի
# միայն այն թվերը, որոնք վերջանում են 7-ով

lst = [i for i in range(1, 101)]

not_seven = list(filter(lambda x: x % 10 == 7, lst))
print('=' * 100)
print(not_seven)


# 10. Create a function that will take a string as an argument. Return a new string which is the original string with
# each letter doubled. For example 'cat' will become 'ccaatt'
# Ստեղծել ֆունկցիա, որը կվերցնի սթրինգ։ Վերադարձնել սթրինգ, որը կլինի օրիգինալ սթրինգը, սակայն ամեն տառ կլինի
# կրկնապատկված։ Օրինակ cat—ը կվերադարձնի 'ccaatt'



def double_char(string: str) -> str:
    res_str = ''
    for char in string:
        res_str += 2 * char

    return res_str


def double_char_1(string: str) -> str:
    res_str = ''
    for char in string:
        res_str += 2 * char

    return res_str

str_1 = "cat"
print(double_char(str_1))
    # lst_from_str_1 = list(map(lambda x: x * 2, str_1))
    # str_2 = "".join(lst_from_str_1)


word = "taco"
word_2 = 'cat'


def double_str(word: str) -> str:
    a =	''.join(char * 2 for char in word)  # Որպեսզի ֆունկցիան ավելի ունիվերսալ լինի, թող արգումենտ վերցնի ու էդ արգումենտի
    # վրա աշխատի, ոչ թե գլոբալի
    return a


print(double_str(word_2))
