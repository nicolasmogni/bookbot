
def main():
    book = get_book('books/frankenstein.txt')
    num_words = get_words_len(book)
    num_characters = get_count_chars_dict(book)
    list = chars_dict_to_list(num_characters)

    print('***** Report of Frankenstein book *****')
    print(f'Total of words: {num_words}')
    print("")
    for i in list:
        print(f"The '{i['char']}' character was found {i['num']} times")

    print('***** End report *****')

def get_book(book_path):
    with open(book_path) as f:
        return f.read()

def chars_dict_to_list(dict):
    dict_list = [{'char': letter, 'num': count} for letter, count in dict.items() if letter.isalpha()]    
    dict_list.sort(key=sort_on, reverse=True)
    return dict_list

def sort_on(dict):
    return dict['num']

def get_words_len(book):
    words = book.split()
    return len(words)
        
def get_count_chars_dict(book):
    characters = {}
    lowered_book = book.lower()

    for i in lowered_book:
        if i in characters:
            characters[i] += 1
        else:
            characters[i] = 1

    return characters


main()