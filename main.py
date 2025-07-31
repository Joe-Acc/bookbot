from stats import word_count, character_count
import sys

def get_file_text(file_path):
    with open(file_path) as file:
        contents = file.read()
        return contents
    
def formatted_print(file_path, num_words, character_dict):

    #prints file path, word count, and some formatting headers
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    #iterates through the character count dictionary printing each count
    for character in sorted(character_dict):
        print(f"{character}: {character_dict[character]}")



def main():
    # if no file path has been provided returns the following message
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
    else:
        file_path = sys.argv[1]
        text = get_file_text(file_path)
        num_words = word_count(text)
        character_dict = character_count(text)

        formatted_print(file_path, num_words, character_dict)

main()