#create empty dict to store user info
user_information = {}

#ask user for input 
name = input("Enter your name: ")
age = input("Enter your age: ")
fav_color = input("Enter your fav_color: ")

#store user input in dict
user_information['name'] = name
user_information['age'] = age
user_information['fav_color'] = fav_color

#print dict
print("Here's your information stored in the dictionary: ")
print(user_information)