path_to_file = "./books/frankenstein.txt"

def get_book_text():
    with open(path_to_file) as f:
        file_contents = f.read()
        print(file_contents)

get_book_text()