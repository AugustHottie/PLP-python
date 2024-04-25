#create list to store list of words
word_list = ['hello', 'bebegim', 'adamin', 'askim', 'i love you', '<3']

#use list-comprehension to create a new list that contains odd number of characters
odd_length_words = [word for word in word_list if len(word) % 2 == 0]

#print new list
print("Words with odd number of characters", odd_length_words)