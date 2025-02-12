#bookbot
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars = count_chars(text)
    sorted_chars = dict(sorted(chars.items()))
    chars_sorted_list = chars_dict_to_sorted_list(chars)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    
    print("Sorted Alaphabetically")
    for c in sorted_chars:
        if c.isalpha():
            print(f"The '{c}' character was found {chars[c]} times")
    print()
    print("Sorted by Count")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print() 
    print("--- End report ---")    

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def count_chars(text):
    chars_dict = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()