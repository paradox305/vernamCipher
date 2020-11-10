#idea is to make a CLI based application to build a vernam cipher
import random
def deckShuffle(card,n):
    for i in range(n) :
        # Generating Random number by shuffling deck of cards
        r = i + (random.randint(0,55) % (52 -i))
        tmp=card[i]
        card[i]=card[r]
        card[r]=tmp
def processing(howMany):
    for i in range(howMany):
        takingInput = input()
        convertedNum = ord(takingInput) - 96
    ##  Converting each index in its numerical values
        convertNumlist.append(convertedNum)
    # Appending the input in arrayList
        arrayList.append(takingInput)
        # print(modedCipher)
        # print(convertNumlist)
        # print(arrayList)
### Main Logic to build vernam cipher
def cipherprocess(convertNumlist,modedCipher,deckOfcards):
    for i in range(howMany) :
        bitCipher = int(convertNumlist[i])
        bit2Cipher = int(deckOfcards[i])
        bitSumcipher = int(bitCipher+bit2Cipher)
        modedCipher.insert(i , bitSumcipher)
        #Recode This part
        finalText = None
        finalText4 = None
        if bitSumcipher%26 == 0 :  #As when the result is zero the program acts stupid 
            finalText4 = 122       #hence hadto explicitely write for to print "Z" 122is the ascii value of Z
        elif bitSumcipher%26 != 0:
            finalText = bitSumcipher%26
            finalText4 = (finalText)+96
        cipheredText.append(chr(finalText4))


#Driver code
if __name__=='__main__':
    deckOfcards=[27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,
                42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,
                58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,
                74,75,76,77,78]
arrayList = []
convertNumlist = []
modedCipher = []
cipheredText = []
howMany = int(input("Enter the number of characters to cipher : "))
processing(howMany)
print("Please copy the below context   : ")
deckShuffle(deckOfcards,52)
print(deckOfcards)
cipherprocess(convertNumlist,modedCipher,deckOfcards)
#Printing Ciphered Text
print("Your Ciphered code is as below : ")
print(modedCipher)
print(*modedCipher, sep =' ')
print("Your Ciphered text is as below : ")
print(cipheredText)
print (' '.join(cipheredText))
