def delete_repeated_words(input_string):
    words = input_string.split()
    unique_words = set()
    result_words = []

    for word in words:
        if word not in unique_words:
            unique_words.add(word)
            result_words.append(word)

    result_string = ' '.join(result_words)
    return result_string

my_sentence = "This is a test sentence. This sentence is a test."
result_sentence = delete_repeated_words(my_sentence)

print("Original Sentence:", my_sentence)
print("Sentence without repeated words:", result_sentence)
