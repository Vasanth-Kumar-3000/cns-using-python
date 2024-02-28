alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string_in=input('Enter the string :')
key=int(input('Enter the key value :'))
string_out=""
for i in range(len(string_in)):
    char=string_in[i].upper()
    location=alpha.find(char)
    new_location=(location+key)%26
    string_out+=alpha[new_location]

print("ENCRYPTED TEXT IS :"+string_out)

plaintxt=""
for i in range(len(string_out)):
    char=string_out[i].upper()
    location=alpha.find(char)
    new_location=(location-key)%26
    plaintxt+=alpha[new_location]
    
print("PLAIN TEXT IS :"+plaintxt)