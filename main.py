with open("books/frankenstein.txt") as f:
    book = f.read()

def count_words(book):
    count = 0
    words = book.split()
    for i in range(len(words)):
        count += 1
    return count
        


def count_characters(book):
    lowercase_text = book.lower()
    char_count = {}
    for char in lowercase_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


words = count_words(book)
characters = count_characters(book)

list_of_dicts = [{"character" : char, "count" : count} for char, count in characters.items() if char.isalpha()]

def sort(dict):
    return dict["count"]

list_of_dicts.sort(reverse=True, key=sort)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{words} words found in the document\n")
for i in list_of_dicts:
    print(f"The '{i["character"]}' character was found {i["count"]} times")
print("--- End report ---")














#---------------------------------------------------------------------
# list_of_dictionaries = []
# for char, count in characters.items():
#     list_of_dictionaries.append({char:count})

# print(list_of_dictionaries)
#---------------------------------------------------------------------



#---------------------------------------------------------------------
# Let's say we want to count letters in "banana"
#text = "banana"

# Method 1: Using a dictionary and loop
# char_count = {}
# for char in text:
#    if char in char_count:
#        char_count[char] += 1
#    else:
#        char_count[char] = 1

# Or Method 2: Using string's count() method
#unique_chars = set(text)
#char_count = {}
#for char in unique_chars:
#    char_count[char] = text.count(char)

#Both approaches would give you:

# char_count would be:
# {'b': 1, 'a': 3, 'n': 2}
#---------------------------------------------------------------------