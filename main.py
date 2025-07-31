from stats import wordcount

def get_file_text(file_path):
    with open(file_path) as file:
        contents = file.read()
        return contents

def main():
    file_path = "./books/frankenstein.txt"
    text = get_file_text(file_path)
    word_count = wordcount(text)

    message = f"{word_count} words found in the document"

    print(message)

main()