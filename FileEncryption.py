import csv

infile = open('Info_Security.txt','r')
outfile = open('encrypted_text1.txt','w')

text = infile.read()

alphabet = {'A':'!', 'a':'@', 'B':'#', 'b':'$', 'C':'%', 'c':'Y', 'D':'^', 'd':'&', 'E':'*', 'e':'(', 'F':'R', 'f':'U', 'G':')',
    'g':'_', 'H':'-', 'h':'=', 'I':'+', 'i':'`', 'J':'1', 'j':'2', 'K':'3', 'k':'4', 'L':'5', 'l':'P', 'M':'6', 
    'm':'7', 'N':'8', 'n':'9', 'O':'0', 'o':'[', 'P':']', 'p':'{', 'Q':'}', 'q':'?', 'R':'~', 'r':'|', 
    'S':'<', 's':'>', 'T':'/', 't':'z', 'U':'a', 'u':'b', 'V':'c', 'v':'d', 'W':'e', 'w':'f', 'X':'g',
    'x':'h', 'Y':'i', 'y':'j', 'Z':'k', 'z':'l', '.':'m', ':':'n', ' ':'o'
    }

encrypted = [print(alphabet[j])for j in text]

#print(alphabet[j])
'''

infile = open('Info_Security.txt','r')
outfile = open('encrypted_txt.txt','w')

file_read = infile.read()
encrypted_txt = ''
for ch in file_read:
    if ch in alphabet:
        encrypted_txt += alphabet[ch]

outfile.write(encrypted_txt)

infile.close()
outfile.close()



for letter in text:
    if letter in alphabet:
        outfile.write(alphabet[letter])
    else:
        outfile.write(letter)

code_items = alphabet.items()

for letter in file_read:
    if not letter in alphabet.values() or letter == '.' or letter == ':':
        outfile.write(letter)
    else:
        for k,v in code_items:
            if letter == v and letter != '.':
                outfile.write(k,end='')
'''


#Truly clueless as to why this is not working
