"""DATA STRUCTURES"""

# 1. Write a program to find the sum of the even elements in the list. Use loops and not the sum() function!

lst = [21, 56, 66, 45, 42, 14, 86, 12, 31, 69, 86, 38, 82, 25, 59, 17,  6, 63, 41, 67]

# 2. A dictionary is given, containing different foods as keys and their contents as values. Unfortunately, we are
# lactose intolerant. Loop through the dictionary and output the food name and 'I can't consume that' if it contains
# lactose and 'Yum!' otherwise.
# The output for the milk may look like this:
# 'Milk? I can't consume that'

foods = {'Milk': 'Calcium, Lactose', 'Nutella': 'Calcium',
         'Cheese': 'Calcium', 'Yoghurt': 'Calcium, Lactose',
         'Spinach': 'Calcium', 'Fish': 'Calcium'}

# 3. A dictionary is given, containing student's grades. The student has failed if the effective grade is lower than 40,
# his grade is satisfactory if it's in between 40-59, good if it's in between 60-79 and outstanding if it's in
# between 80-100. Print the corresponding grade and description.

grades = {'Maths': 7,
          'Physics': 11,
          'Geography': 10,
          'History': 8,
          'Geometry': 19}

# 4. Create a list using a comprehension, which will contain odd numbers only.

# 5. Add to a list all the words in the given string that have a length <=4. Do this using both loops and a
# comprehension.

litany = """I must not fear. Fear is the mind-killer. 
Fear is the little-death that brings total obliteration.
I will face my fear.
I will permit it to pass over me and through me.
And when it has gone past, I will turn the inner eye to see its path.
Where the fear has gone there will be nothing. Only I will remain."""

# 6. Write a generator comprehension which will contain every 4th number from 100-200. Then loop over it and print the
# element.

# 7. Write a program that will print a list containing first 50 numbers in Fibonacci sequence.

# 8. Write a program to combine two dictionary adding values for common keys.

# 9. Write a program to create a dictionary from a string. The letters are the keys and the values are the counts of
# the corresponding letters.

# 10. Remove the keys that have None value from the dict.
colors = {'Color 1': 'Red', 'Color 2': 'Blue', 'Color 3': 'Green', 'Color 4': None, 'Color 5': 'Yellow', 'Color 6': None}