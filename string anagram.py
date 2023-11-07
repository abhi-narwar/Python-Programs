str1=input("enter the string")
str2=input("enter the string")
if len(str1)==len(str2):
    print("it is anagram")

else:
    for i in str1:
        if i not in str2:
            print("it is not anagram")
            break

    else:
        print("it is anagram")
