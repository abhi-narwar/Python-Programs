punctuation='@,-,.'
str='abhisheknarwar@gmail.com'
s2=''
for i in str:
    if i not in punctuation:
     s2+=i
print(s2)
