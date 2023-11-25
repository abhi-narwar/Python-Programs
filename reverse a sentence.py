def reverse_sentence(sentence):
    if len(sentence) == 0:
        return sentence
    else:
        return reverse_sentence(sentence[1:]) + sentence[0]
        #return reverse_sentence(sentence[1:]) + sentence[0]

# Example usage:
my_sentence = "Hello, World!"
reversed_sentence = reverse_sentence(my_sentence)

print("Original Sentence:", my_sentence)
print("Reversed Sentence:", reversed_sentence)
