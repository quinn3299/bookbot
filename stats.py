def get_num_words(text):
    words = text.split()
    total_words = len(words)
    return total_words

def count_characters(text):
    char_counts = {}
    for char in text:
        lowercase_char = char.lower()
        if lowercase_char in char_counts:
            char_counts[lowercase_char] += 1
        else:
            char_counts[lowercase_char] = 1
    return char_counts

def sort_on_num(dict):
    return dict["num"]


def sort_num(char_counts):
    character_stats = []
    for character, count in char_counts.items():
        character_dict = {"char": character, "num": count}
        character_stats.append(character_dict)

    character_stats.sort(reverse=True, key=sort_on_num)
    print(character_stats)

    return character_stats