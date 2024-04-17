# fruits = ['apple', 'banana', 'liche', 'mango', 'peach' ]
# newList = [each_fruit for each_fruit in fruits if 'a' in each_fruit]
# print(newList)

text = "This is the first tist in comprehension"
unique_vowels = {t for t in text if t in 'is' }
print(unique_vowels)