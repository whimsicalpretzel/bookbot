def main():

    char_dict = {}

    with open('books/frankenstein.txt') as f:
        file_contents = f.read()

    def word_count():
        words = file_contents.split()
        return len(words)
        #print(len(words))

    def count_chars():
        lower_letters = file_contents.lower()
        for letter in lower_letters:
            if letter not in char_dict:
                char_dict[letter] = 0
            char_dict[letter] += 1
        #print(char_dict)

    count_chars()

    total_words = word_count()



    dict_list = list(char_dict.items())

    def sort_on(item):
        return item[1]
    
    def create_report(total_words):
        first_line = '--- Begin report of books/frankenstein.txt ---'
        word_count_line = f'{total_words} words found in the document'
        report_body = ''
        last_line = '--- End report ---'

        dict_list.sort(reverse=True, key=sort_on)

        for entry in dict_list:
            if entry[0].isalpha():
                report_body += f"The '{entry[0]}' character was found {entry[1]} times\n"

        report = f'{first_line}\n{word_count_line}\n\n{report_body}{last_line}'

        print(report)

    create_report(total_words)

main()