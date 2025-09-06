import sys

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    text =text.lower()
    num_characters = {}
    for i in text:
        if i in num_characters:
            num_characters[i] += 1
        else:
            num_characters[i] = 1

    return num_characters
def sort_dict_by_value(d):
    return d["value"]

def pretty_report(text):
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    list_num_characters = []
    for char, count in num_characters.items():
        if char.isalpha():
            list_num_characters.append({"char": char, "value": count})
    list_num_characters.sort(key=sort_dict_by_value, reverse=True)
    
    report = "============ BOOKBOT ============\n"
    report += f"Analyzing book found at {sys.argv[1]}...\n"
    report += "--------- Word Count -------\n"
    report += f"Found {num_words} total words\n"
    report += "--------- Character Count -------\n"
    for item in list_num_characters:
        report += f"{item['char']}: {item['value']}\n"

    report += "============= END ===============\n"

    return report