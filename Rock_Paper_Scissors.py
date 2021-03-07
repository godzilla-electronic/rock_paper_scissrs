#import library
    #os library
import os
    #Random library
from random import choice
    #choose word
import inquirer
    #exit from app
import sys

#clear the screen
def clear():
    os.system('clear')
    os.system('cls')

#run clear
clear()

#Select name for game
print("                                 > Mr.game <")

#print welcome to the game
print("""
Hi friend,i hope you are doing well
  Welcome to RPS(Rock Paper Scissors) game
""")

print("                     ---------------------------------------\n")

#list for count item
li = []

#list for better count
key_li = ['End']

#game loop
while True:
    #select random word
    random = choice(['Rock','Paper','Scissors'])
    
    #multiple choos
    questions = [
        inquirer.List('type',
            message="Select the desired option ",
            choices=['Rock','Paper','Scissors','','','End'],
        ),
    ]
    answers = inquirer.prompt(questions)['type']
    if answers not in key_li:
        #add item to list for count item in list
        li.append(answers)
        #show count item in list
        print (f"Hand {len(li)} ")
    #exit from game
    if answers == 'End':
        sys.exit()
    #win\lose
    if random == answers:
        print ("We were equal")
    if random == 'Rock' and answers == 'Scissors':
        print ("You lose!")
    if random == 'Rock' and answers == 'Paper':
        print ("You win!")
    if random == 'Paper' and answers == 'Scissors':
        print ("You win!")
    if random == 'Paper' and answers == 'Rock':
        print ("You lose!")
    if random == 'Scissors' and answers == 'Rock':
        print ("You win!")
    if random == 'Scissors' and answers == 'Paper':
        print ("You lose!")
    #print random word
    print("My thing was :",random)
    print("                     ---------------------------------------\n")