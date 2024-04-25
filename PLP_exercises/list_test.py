create_list = input("Create a list of integers seperated by spaces: ")

#split user_input into individual integers
split_int =create_list.split()

#convert the list of str to int
integers = [int(num) for num in split_int]

#calculating the sum of integers
summed_list = sum(integers)

#displaying the sum
print("Sum of values in your list is: ",summed_list)