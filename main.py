def get_file_text(file_path):
    with open(file_path) as file:
        contents = file.read()
        return contents
    
def wordcount(text):
    words = text.split()
    count = 0
    for word in words:
        count += 1
    return count

def main():
    file_path = "./books/frankenstein.txt"
    text = get_file_text(file_path)
    word_count = wordcount(text)

    message = f"{word_count} words found in document"

    print(message)

main()