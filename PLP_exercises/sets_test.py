#ask user_input to create first set of integers
set1_input = input("Enter integer values to be added to the set sepreated by spaces: ")
set1_integers = set(map(int, (set1_input.split())))

#ask user_input to create second set of integers
set2_input = input("Enter integer values to be added to the set sepreated by spaces: ")
set2_integers = set(map(int, (set1_input.split())))

#finding intersection of the two sets
common_elemnts = set1_integers.intersection(set2_integers)

#print common integers
print("Common elements ", common_elemnts)