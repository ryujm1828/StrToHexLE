print("String to 8Byte HEX LE")
inputstr = input()
str1 = ["" for i in range (1000)]
k = 0
j = 0
for i in reversed(inputstr):
    str1[k] += str(format(ord(i),'x'))
    j+=1
    if j == 8:
        k+=1
        j = 0


for i in str1:
    if(i == ""):
        break
    print("0x"+i)
