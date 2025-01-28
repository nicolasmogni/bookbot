
def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    num_words = count_words(file_contents)
    num_characters = count_characters(file_contents)
    # print(f'Total of words: {num_words}')
    # print(num_characters)

    dictionary_list = [{'char': letter, 'num': count} for letter, count in num_characters.items() if letter.isalpha()] 
    dictionary_list.sort(key=sort_on, reverse=True)

    print('***** Report of Frankenstein book *****')
    print(f'Total of words: {num_words}')
    for i in dictionary_list:
        print(f"The '{i['char']}' character was found {i['num']} times")

    print('***** End report *****')

 
def sort_on(dict):
    return dict['num']

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

