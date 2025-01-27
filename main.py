
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    num_words = count_words(file_contents)
    num_characters = count_characters(file_contents)
    print(f"Total of words: {num_words}")
    print(num_characters)


def count_words(book):
        words = book.split()
        return len(words)
        
def count_characters(book):
    characters = {}
    textLowered = book.lower()

    for i in textLowered:
        if i in characters:
            characters[i] += 1
        else:
            characters[i] = 1

    return characters


main()

