import random

print('** Welcome to the game **')
print('** are you ready to start the game ? **')
print(' YES or NO ? ')

words_1=['air','age','art','bar','box','cap','cat','die','dog','gym']
words_2=['fish','bird','wing','boat','ship','tire','city','road','farm','room']
words_3=['house','school','office','library','hospital','space','green','People','father','brother']

word_1=random.choice(words_1)
word_2=random.choice(words_2)
word_3=random.choice(words_3)

Chance_again_1= 15
Chance_again_2= 10
Chance_again_3= 5

yes_no=input()
x=[]

if yes_no=='YES' or yes_no=='yes' or yes_no=='Y' or yes_no=='y':
    print('** Please specify the game level **')
    print(' 1 : Easy , 2 : Normal , 3 : Hard ')
    level=int(input())
    if level==1 :
        for i in range(len(word_1)):
            x.append("_")  
        while Chance_again_1>0 :
            print(''.join(x))
            Input_characters_1=input()
            if Input_characters_1 in word_1:
                print(' yes continue ')
                for i in range(len(word_1)):
                    if word_1[i]==Input_characters_1:
                        x[i]=Input_characters_1
            else :
                Chance_again_1 = Chance_again_1 - 1
                print(' no !! try again , Number of chances again : ' , Chance_again_1)
    if level==2 :
        for i in range(len(word_2)):
            x.append("_")         
        while Chance_again_2>0 :
            print(''.join(x))
            Input_characters_2=input()
            if Input_characters_2 in word_2 :
                print(' yes continue ')
                for i in range(len(word_2)):
                    if word_2[i]==Input_characters_2:
                        x[i]=Input_characters_2
            else :
                Chance_again_2 = Chance_again_2 - 1
                print(' no !! try again , Number of chances again : ' , Chance_again_2)
    if level==3 :
        for i in range(len(word_3)):
            x.append("_")
        while Chance_again_3>0 :
            print(''.join(x))
            Input_characters_3=input()
            if Input_characters_3 in word_3 :
                print(' yes continue ')
                for i in range(len(word_3)):
                    if word_3[i]==Input_characters_3:
                        x[i]=Input_characters_3
            else : 
                print(' no !! try again , Number of chances again : ' , Chance_again_3)
else :
    print("We look forward to seeing you again :( ")