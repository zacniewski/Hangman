import random
with open('animals.txt', 'r') as openfile:
    s=openfile.read().split()
secret_word = random.choice(s)
#print("Magic word is:",secret_word)
turns=5
print("WELCOME TO HANGMAN GAME")
print("You've got", turns,"turns. Every mistake decreseases amount of turns.")
print("HINT: Only names of animals are to guess.")
chosen_letters=[]
for j in range(len(secret_word)):
    chosen_letters.append('_')

def guessing():
    global turns
    if(turns>0):
        print(turns,"turns left")
        letter=input("Make your guess:")
        add_letter(secret_word,letter,chosen_letters) 
        
        if(letter in secret_word)==False:
            print("Sorry, no letter %s in your word" %letter)
            turns=turns-1    
        else:pass        
        
        if('_' not in chosen_letters):
            print("THAT'S END")
            sorting(secret_word,chosen_letters) #sort and count elements
    list_to_str=(str(chosen_letters)).replace(',',' ').replace('[','').replace(']','')
    print(list_to_str)
        
def sorting(word1,word2):
    w1=sorted(word1)
    w2=sorted(word2)
    if(w1==w2):
        print("You win!!!! YOUR HANGMAN SURVIVES !!! The correct word was %s" %word1.upper())
    else:
        print("SORRY, YOUR HANGMAN DIED !!! Your version was %s" %(str(word2)).upper().replace(',',' ').replace('[','').replace(']',''))
        print("The correct word was %s" %word1.upper())
    exit()
    
def add_letter(word,letter,list2):#adding letters if they exists in secret_word
    global turns
    for j in range(len(word)):
        if(letter==word[j]):
            print("Good choice. The letter %s is in your word:" %letter)
            list2.insert(j,letter)
            list2.pop(j+1)
        else:pass
       
while (turns>0):
    guessing()
sorting(secret_word,chosen_letters)
    

