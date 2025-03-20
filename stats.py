def split_book(contents):
    words = contents.split()
    word_count = len(words)

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    return word_count


def num_characters(contents):
    character_dict = {}
    for char in list(contents):
        char = char.lower()
        if char not in character_dict:
            character_dict[char] = 1
        else:
            character_dict[char] += 1

    return character_dict


def char_sort(dict):
    def sort_on(dict):
        return dict["count"]

    char_list = []
    for entry in dict:
        if entry.isalpha():
            char_list.append({"character": entry, "count": dict[entry]})

    char_list.sort(reverse=True, key=sort_on)

    print("--------- Character Count -------")
    for entry in char_list:
        print(entry["character"] + ": " + str(entry["count"]))
