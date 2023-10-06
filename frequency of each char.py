#frequency of each char of string
'''
>>>hello
  h:1
  e:1
  l:2
  o:1

>>>banana
   b:1
   a:3
   n:2

'''
st=input('entern the string')
for i in st:
    print(f'{i}:  {st.count(i)}')
