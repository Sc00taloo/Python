print('Enter name official file: ')
officialFile = input()
f = open(officialFile + '.txt', "w")
print('Enter official words: ')
while True:
    word = input()
    if not word:
        break
    f.write(word + '\n')
f.close()

print('Enter name main file: ')
mainFile = input()
fMain = open(mainFile + '.txt', "w")
print('Enter the sentences: ')
while True:
    word = input()
    if not word:
        break
    fMain.write(word)
fMain.close()

fDo = open(officialFile + '.txt', "r")
fDid = open(mainFile + '.txt', "r")
textBegin = fDid.readlines()
textString = ''
for el in textBegin:
    textString += str(el)
    textString += ' '
fDid.seek(0) 
for line1 in fDid:
    for line in fDo:
        length = len(line)
        length = length - 1
        textString = textString.lower()
        textString = textString.replace(line.lower().rstrip(), "*"*length)
fDo.close()
fDid.close()
print('Enter name complete file: ')
completeFile = input()
fComplete = open(completeFile + '.txt', "w")
fComplete.write(textString)
fComplete.close()