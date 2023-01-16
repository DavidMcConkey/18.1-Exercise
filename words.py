def print_upper_words(words, limiter):

    for word in words:
        for letter in limiter:
            if word.startswith(letter):
                print(word.upper())
                break


print_upper_words(["apple", "pears"], limiter=["a", "p"])
