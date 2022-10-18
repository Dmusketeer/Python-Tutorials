# Pig Latin takes the first consonant of a word, 
# moves it to the end of the word and adds on an 
# “ay”. If a word begins with a vowel you just add 
# “way” to the end. For example, pig becomes igpay, 
# banana becomes ananabay, and aadvark becomes 
# aadvarkway. Create a program that will ask the 
# user to enter a word and change it into Pig Latin. 
# Make sure the new word is displayed in lower case. 

userWord=input("Enter a word: ")
n=len(userWord)
if userWord[0]=="a" or userWord[0]=="e" or userWord[0]=="i" or userWord[0]=="o" or userWord[0]=="u":
    print(f"{userWord.lower()}way")
else:
    pigLatin=userWord[1:n+1]+userWord[0]+"ay"
    print(pigLatin.lower())
