s = '00 00 16 16 17 17 17 16 16 16 16 17 17 16 16 17 17 16 16 17 17 16 17 17 17 16 17 17 16 17 16 16 16 16 17 17 16 16 16 16 17 16 17 17 17 16 16 17 17 16 16 17 17 16 17 17 16 00 00'
s = s.replace(' ','')
s = s[4:-4]
s = s.replace('16','0')
s = s.replace('17','1')

#print s

text = ''
char = '' 
a=len(s)//8 +1
zero='0'
for i in range(1, a):
    temp = s
    pos = i * 8
    result = temp[:pos] + zero + temp[pos:]  # Insert zero at position 'pos'
    for i in range(0, len(result)):
        char += result[i]  # Use result instead of s to accumulate characters
        if len(char) == 8:
            print(char)
            text += chr(int(char, 2))
            char = ''
    print(text)
    text=''
    print('------------------')



