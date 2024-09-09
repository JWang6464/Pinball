'''
Jordan Wang
CS152 Section B
Professor Harper
04/18/2023
This module contains several different classes that contain attributes specific to those classes. In addition, each class
contains methods that serve to initialize and vary the preset values of the attributes. This module imports the graphicsPlus
and random modules and utilizes them to develop the visualization aspect of each shape/class.
'''

def main():
    prompt = 'Please enter a response for each word prompt:'
    print(prompt)
    # Create a list of words
    words = ["hi ", "this ", "is ", "me ", "hope ", "all ", "well ", "computer ", "basketball ", "best "]
    # Establish an empty dictionary
    mapping = {}
    # Loop over the words list
    for word in words:
        # Get a response from the user
        response = input(f"Enter a word for '{word}': ")
        # Assign to dictionary the response
        mapping[word] = response
    for key in mapping.keys():
        print(f"{key}: {mapping.get(key)}")


if __name__ == "__main__":
    main()