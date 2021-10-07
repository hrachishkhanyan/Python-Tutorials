"""MODULES"""

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

# 2. Write a function that will return the longest word in the random words file from the previous exercise.
# Գրել ֆունկցիա, որը կվերադարձնի "random_words" ֆայլի ամենաերկար բառը։

# 3. Write a function that will take a string containing the path to a file as an argument and return its size in
# kilobytes.
# Գրել ֆունկցիա, որը կվերցնի սթրինգ արգումենտ։ Սթրինգը պետք է լինի որոշակի ֆայլի path-ը։ Ապա վերադարձնել այդ ֆայլի
# չափսերը կիլոբայթերով։ Հուշում՝ օգտվել os մոդուլից:

# 4. Create a random number generator without using random module. The implementation is up to you. You may use
# current timestamp as a random seed.
# Գրել ֆունկցիա, որը կվերադարձնի պատահական թիվ։ Պատահական թվերի գեներատոր պարունակող մոդուլ չօգտագործել։ Իմպլեմենտացիան
# կախված է ձեզնից։ Մտածեք որոշակի ալգորիթմ և ըստ դրա գեներացրեք թիվ։ Կարող եք օգտագործել մեր անցած seed-ի գաղափարը։

# 5. Create a file and put your shopping list in it. The file must start with current day's date.
# Ստեղծել ֆայլ, որը կպահի ձեր գնումների ցուցակը (ինչ ապրանք։ քանի հատ)։ Ֆայլը պետք է սկսվի տվյալ օրվա ամսաթվով։
