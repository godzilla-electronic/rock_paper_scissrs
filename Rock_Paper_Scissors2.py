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
key_li = ['End','Back to menu','Clear']

#game history
def game_history():
    print("""
The first known mention of the game was in the book Wuzazu [zh] by the Chinese Ming-dynasty writer Xie Zhaozhi [zh] (fl. c. 1600), who wrote that the game dated back to the time of the Chinese Han dynasty (206 BCE – 220 CE).
  In the book, the game was called shoushiling. Li Rihua's book Note of Liuyanzhai also mentions this game, calling it shoushiling (t. 手勢令; s. 手势令), huozhitou (t. 豁指頭; s. 豁指头), or huaquan (划拳).
    Throughout Japanese history there are frequent references to sansukumi-ken, meaning ken (fist) games where "the three who are afraid of one another" (i.e. A beats B, B beats C, and C beats A).
      This type of game originated in China before being imported to Japan and subsequently also becoming popular among the Japanese.
        The earliest Japanese sansukumi-ken game was known as mushi-ken (虫拳), which was imported directly from China.In mushi-ken the "frog" (represented by the thumb) triumphs over the "slug" (represented by the little finger),
          which, in turn prevails over the "snake" (represented by the index finger), which triumphs over the "frog".
            Although this game was imported from China the Japanese version differs in the animals represented.
              In adopting the game, the original Chinese characters for the poisonous centipede (蜈蜙) were apparently confused with the characters for the slug (蛞蝓).
                The most popular sansukumi-ken game in Japan was kitsune-ken (狐拳).
                  In the game, a supernatural fox called a kitsune (狐) defeats the village head, the village head (庄屋) defeats the hunter,
                    and the hunter (猟師) defeats the fox. Kitsune-ken, unlike mushi-ken or rock–paper–scissors, is played by making gestures with both hands.
                      Today, the best-known sansukumi-ken is called jan-ken (じゃんけん),which is a variation of the Chinese games introduced in the 17th century.Jan-ken uses the rock, paper, and scissors signs and is the game that the modern version of rock paper scissors derives from directly.
                        Hand-games using gestures to represent the three conflicting elements of rock, paper, and scissors have been most common since the modern version of the game was created in the late 19th century, between the Edo and Meiji periods.
    """)

#game_training
def game_training():
    print ("""
The players may count aloud to three, or speak the name of the game (e.g. "Rock! Paper! Scissors!"),
  either raising one hand in a fist and swinging it down with each syllable or holding it behind their back.
    They then "throw" by extending it towards their opponent.
      Variations include a version where players throw immediately on the third count (thus throwing on the count of "Scissors!"),
        or a version where they shake their hands three times before "throwing".
    """)

def game():
    #game loop
    while True:
        #select random word
        random = choice(['Rock','Paper','Scissors'])
        
        #multiple choos
        questions = [
            inquirer.List('type',
                message="Select the desired option ",
                choices=['Rock','Paper','Scissors','','Clear','Back to menu','Exit'],
            ),
        ]
        answers = inquirer.prompt(questions)['type']
        if answers not in key_li:
            #add item to list for count item in list
            li.append(answers)
            #show count item in list
            print (f"Hand {len(li)} ")
        #for clear screan
        if answers =='Clear':
            clear()
        #exit from game
        if answers == 'Exit':
            sys.exit()
        #back to menu
        if answers == 'Back to menu':
            break
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

#menu app
def app():
    while True:
        #menu
        questions =  [
            inquirer.List('menu',
                choices=['Run game','Game history','Game training','','Clear','End'],
            ),
        ]
        answers = inquirer.prompt(questions)['menu']
        #run game
        if answers == 'Run game':
            game()
        #run game history
        if answers == 'Game history':
            print ("                     ---------------------------------------\n")
            print ("                                 Game history")
            game_history()
        #run game training
        if answers == 'Game training':
            print ("                     ---------------------------------------\n")
            print ("                                 Game training")
            game_training()
        #clear the screen
        if answers =='Clear':
            clear()
        #exit from app
        if answers == 'End':
            sys.exit()

#run app
app()