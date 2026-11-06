def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            lst.append(word)
            ctr += 1
    print("Number of words that match the criteria:\n ", lst)
    return ctr
count = match_words(['abc', 'xyz', 'aba', '1221'])
print("Number of words that match the criteria:\n ", count)