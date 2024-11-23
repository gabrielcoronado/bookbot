def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        total_words = words_counter(file_contents)
        char_dictionary = char_counter(file_contents)

        print(f"{total_words} words found in the document")

        for el in char_dictionary:
            for key, value in el.items():
                print(f"The '{key}' character was found {value} times")


def words_counter(book):
    words = book.split()
    return len(words)

def char_counter(book):
    chars = {}
    list_ = []
    lower_case = book.lower()

    for char in lower_case:
        if char.isalpha():
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1

    for char in chars:
        list_.append({char : chars[char]})

    sorted_data = sorted(list_, key=lambda x: list(x.values())[0], reverse=True)
    return sorted_data

main()