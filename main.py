import string

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    word_count = count_words(text)
    print(f'{word_count} words found in the document')

def count_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

with open("books/frankenstein.txt", 'r') as file:
    frank_text = file.read()

lowercase = frank_text.lower()

frank_dict = {}

alphabet = set(string.ascii_lowercase)

for lower in lowercase:
    if lower in alphabet:
        if lower in frank_dict:
            frank_dict[lower] += 1
        else:
            frank_dict[lower] = 1

frank_dict_sorted = sorted(frank_dict.items(), key=lambda frank_dict: frank_dict[1], reverse=True)

print("--- Begin report of books/frankenstein.txt ---")

main()

for char, times in frank_dict_sorted:
    print(f" The '{char}' character was found {times} times")

print("--- End report ---")





# AI solution

# with open('books/frankenstein.txt', 'r') as file:
#     contents = file.read()    
# print(contents)






