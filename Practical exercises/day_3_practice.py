"""IF, ELIF, ELSE"""

# 1. Write a program that will ask to input a temperature in Celsius or Fahrenheit units.
# Convert to C if the input is in F units and otherwise if it's in C units.
# Sample input -> 36C
# Output will be -> 96.8F
# Գրել ծրագիր, որը կփոխակերպի Ցելսիուսով/Ֆարենհայթով տրված ջերմաստիճանը Ֆարենհայթի/Ցելսիուսի։ Ջերմաստիճանը պետք է
# ներմուծվի հետևյալ ֆորմատով` 36C, 96.8F և այլն։

temp = input('Enter a temperature in F or C units: ')
unit = temp[-1].lower()

if unit == 'c':
    print(f'{temp} in Fahrenheit units is: ', float(temp[:-1]) * 9 / 5 + 32)
elif unit == 'f':
    print(f'{temp} in Celsius units is: ', (float(temp[:-1]) - 32) * 5 / 9)
else:
    print('Your input ')

# converted = (float(temp[:-1]) * 9 / 5 + 32) if unit == 'c' else (float(temp[:-1]) - 32) * 5 / 9
# print(converted)

# 2. Given and integer, write a program which will output Fizz, if the number is divisible by 3, Buzz, if it's divisible
# by 5, and FizzBuzz if it's divisible by both.
# Գրել ծրագիր, որը կտպի Fizz, եթե ներմուծված թիվը բաժանվում է 3-ի, Buzz, եթե բաժանվում է 5-ի և FizzBuzz, եթե բաժանվում է
# և՛ երեք, և՛ 5-ի։ Հակառակ դեպքում տպել հենց թիվը։

# 3. Write a program that will take an input string from the user. If the string starts with "a" or "o", output it as it
# is, otherwise output the reverse of the string.
# Ստուգել, արդյո՞ք ներմուծված սթրինգը սկսվում է a կամ o-ով։ Եթե հա տպենք սթրինգն ինչպես կա, իսկ հակառակ դեպքում՝ սթրինգի
# հակառակը։

string = input('Enter a string: ')

if string.startswith('a') or string.startswith('o'):
    print(string)
else:
    print(string[::-1])

# 4. Write a program that will take an example password as an input. If the password contains more than 6 and less than
# 12 characters and it contains both numerical and alphabetical characters and a symbol from !, $, %, print that the
# password is good. Otherwise, prompt the user to change the password next time.
# Պահանջել մուտքագրել ծածկագիր։ Եթե ծածկագիրը պարունակում է 6-ից 12-ից նիշ և պարունակում է թվանշաններ, տառեր և հետևյալ
# սիմվոլներից մեկը !, $, %, տպել, որ ծածկագիրն ուժեղ է։ Հակառակ դեպքում զգուշացրեք օգտատիրոջը, որ ծածկագիրը պետք է
# փոխվի։

password = 'wasdasdwad123!'

if 6 < len(password) < 12:
    if '!' in password or '$' in password or '%' in password:
        pass


# 5. Ask for three numerical inputs. Find the sum of these numbers. If the sum is even, print the square of the sum,
# otherwise print the sum as it is.
# Գտնել ներմուծված երեք թվերի գումարը։ Եթե այն զույգ է, տպել գումարի քառակուսին։ Հակառակ դեպքում տպել գումարը։

