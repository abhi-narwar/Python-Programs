sentence = input("Enter a sentence: ")
vowel_count = 0
vowels = set("aeiouAEIOU")
for i in sentence:
   if i in vowels:
        vowel_count += 1
print("Number of vowels in the sentence:", vowel_count)
