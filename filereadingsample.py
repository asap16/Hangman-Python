
def retrieve_words():
    find_words = open('hangman_english_words.txt')
    list_of = []
    item = find_words.readline()
    for item in find_words:
        word = item.strip()
        list_of.append(word)
    return list_of

print(retrieve_words())
