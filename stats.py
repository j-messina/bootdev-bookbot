from collections import Counter
def get_num_words(text):
    return len(text.split())

def get_char_count(text, option = ""):
    if option == "alpha":
        filtered_chars = [text_char for text_char in text.lower() if text_char.isalpha()]
        result = Counter(filtered_chars)
    else:
        result = Counter(text.lower())
    return result

def get_sorted_chars_dict_list(text, option = "alpha"):
    original_dict = get_char_count(text, option) # temp is a dict atm
    results_list = []
    for key, val in original_dict.items():
        results_list.append(dict(char = key, num = val))
    results_list.sort(reverse=True, key=sort_on)
    return results_list
    
def sort_on(dict_item):
    return dict_item["num"]
