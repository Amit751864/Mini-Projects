'''
snake , water gun game 
we all have played snake ,water gun game in childhood if you haven't google the 
rules of this game write a python program capable of palying this game with the user
'''
import random
''' 1 for snake
 -1 for water
 0 for gun'''


computer = random.choice([-1,0,1])
youstr = input("enter the choice :")
youDict = {"s" : 1, "w": -1, "g":0}
reverseDict = {1:"Snake",-1:"Water",0:" Gun"}
you = youDict[youstr]
#by now w ehave 2 numbers variable you and computer

print(f"you choose{dict[you]} \nComputer choose{reverseDict[computer]}")

if(computer == you):
    print("its draw")

else:
    #if((computer -you)==-1 or (computer -you)==2): ya sab analyse kar ke pta chala ha
         #print("you lose")
    #else:
         # print("you win")     
    if(computer ==-1 and you ==1):
        print("You win !")

    elif(computer==-1 and you ==0):
        print("you lose")

    elif(computer==1 and you ==-1):
        print("you lose")

    elif(computer ==1 and you == 0):
        print("you win")
            
    elif(computer ==0 and you == -1):
        print("you win")

    elif(computer ==0 and you == 1):
        print("you lose")

    else:
        print("something went wrong")    


 