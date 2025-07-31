from stats import word_count, character_count

def get_file_text(file_path):
    with open(file_path) as file:
        contents = file.read()
        return contents

def main():
    file_path = "./books/frankenstein.txt"
    text = get_file_text(file_path)
    num_words = word_count(text)
    character_dict = character_count(text)

    message = f"{num_words} words found in the document"

    print(message)
    print(character_dict)

main()