"""create a program that automates searching for a word definition in a dictionary"""
import json
import difflib 

#open the JSON file
def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        # Load JSON data into a dictionary
        return json.load(file)

#function that returns definition of a word
def get_definition(word, dictionary):
    word = word.lower()
    if word in dictionary:
        return dictionary[word]
    else:
        suggestions = difflib.get_close_matches(word, dictionary.keys(), n=3)
        if suggestions:
            return f"Word not found. Did you mean: {', '.join(suggestions)}?"
        else:
            return "Word not found."
        
#main function
def main():
    #load the dictionary
    dictionary = load_dictionary('data.json')

    #get user input 
    word = input("Enter a word to get its definition: ")

    #get definition of word
    definition = get_definition(word, dictionary)

    #print word
    print("Definition of word: ", definition)

if __name__ == "__main__":
    main()