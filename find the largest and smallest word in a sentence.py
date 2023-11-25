def find_largest_and_smallest_words(sentence):
    words = sentence.split()
    largest_word = smallest_word = words[0]
    for word in words:
       
        if len(word) > len(largest_word):
            largest_word = word
        elif len(word) < len(smallest_word):
            smallest_word = word

    return largest_word, smallest_word


my_sentence = "Python is an amazing programming language"
largest, smallest = find_largest_and_smallest_words(my_sentence)

print("Largest Word:", largest)
print("Smallest Word:", smallest)
