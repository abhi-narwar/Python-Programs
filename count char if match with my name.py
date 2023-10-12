str=input("")
char_count=0
char=set("abhishekABHISHEK")
for i in str:
    if i in char:
        char_count+=1
print(f"number of char match with set ia equal to{char_count}")
