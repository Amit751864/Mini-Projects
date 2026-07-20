'''                       the perfect guess
We are going to write a program that generation a random number  and asks  the user to guess it

if the player's guess is higher than the actual number , the program display "lower number 
please . similarly if the user's guess is too low the program prints higher number please 
when the user guesses the correct number , the program  display the number of guesses the player used to arrive at the number 
 HINT use the random module

'''


from random import randint 
n = randint(1,100)
a =-1
guesses =1

while(a != n):
    a = int(input("Guess The Number : "))
    if (a>n):
        print("lower number please")
        guesses +=1
    elif(a<n):
        print("higher number please")
        guesses +=1

print(f"you have guessed the number {n} correctly in  { guesses} attempt")