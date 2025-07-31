#splits provided text into words and counts them
def word_count(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

#counts each different character and returns dictionary with counts
def character_count(text):
    #defines the dictionary storing counts
    counter = {}

    words = text.split()

    #iterates through each word in the text
    for word in words:
        #iterates through each character in each word
        for character in word:
            #makes character lowercase to make the count case insensitive
            character = character.lower()
            #creates a key in the counter dictionary if there is none, otherwise iterates the count by 1
            if character in counter:
                counter[character] = counter[character] + 1
            else:
                counter[character] = 1

    #returns the dictionary with the count of each character
    return counter