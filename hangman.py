
import random
import string
from word import choose_word
from images import IMAGES

def ifValid(user_input):
    if len(user_input) != 1:
        return False

    if not user_input.isalpha():
        return False
    
    else:
        return True
def is_word_guessed(secret_word, letters_guessed):
    
    if secret_word==get_guessed_word(secret_word,letters_guessed):
        return True
    else:
        return False

def get_guessed_word(secret_word, letters_guessed):

    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    
    return guessed_word


def get_available_letters(letters_guessed):

    all_letters = string.ascii_lowercase
    letters_left=""
    for letter in all_letters:
        if letter not in letters_guessed:
            letters_left+=letter

    return letters_left

    # Hint function

    
def get_hint(secret_word,letters_guessed):
    import random
    letters_not_guessed=[]

    index = 0
    while index < len(secret_word):
        letter = secret_word[index]
        if letter not in letters_guessed:
            if letter not in letters_not_guessed:
                letters_not_guessed.append(letter)
        index+=1
        return random.choice(letters_not_guessed)


def hangman(secret_word):

    print ("* * * Welcome to the game, Hangman! * * *")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("")

    letters_guessed = []

    total_lives=remaining_lives=8
    image_selection=[0,1,2,3,4,5,6,7]
    level=input("enter the level in which you want to play""\n""a for easy""\n""b for medium""\n""c for hard level:-")
    if level not in ['a','b','c']:
        print("invalit choice.\n Game start with easy level")
    if level=="b":
        total_lives=remaining_lives=6
        image_selection=[1,2,3,5,6,7]
    elif level=="c":
        total_lives=remaining_lives=4
        image_selection=[1,2,3,5]
    else:
        if level!="a":
            print("your choice is in valid""\n""game is starting in easy leval")
    letters_guessed=[]
    count=0
    while (remaining_lives>0):
      available_letters = get_available_letters(letters_guessed)
      print ("Available letters: " + available_letters)

      guess = input("Please guess a letter:- ")
      letter = guess.lower()
      if (not ifValid(letter)):
            print("invalid input")
            pass

      if letter=="hint":
          if count<1:
                print("your hint for this secret_word is:"+get_hint(secret_word,letters_guessed))
          else:
              print("sorry,you allready use hint")
          count+=1
      else:
        if letter in secret_word:
            letters_guessed.append(letter)
            print(letters_guessed)
            print ("Good guess: "+ get_guessed_word(secret_word, letters_guessed))
            print ("")

            if is_word_guessed(secret_word, letters_guessed) == True:
                print (" * * * Congratulations, you won! * * * ")
                print ("")
                break

        else:
          print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
          letters_guessed.append(letter)
          print(IMAGES[image_selection[total_lives-remaining_lives]])
          remaining_lives-=1
          print("remaining_lives =",remaining_lives)
          print ("")
    else:
        print(" sorry your lose the game ,the word was "+str(secret_word)+".")
    
secret_word = choose_word()
hangman(secret_word)
    
    
    

























