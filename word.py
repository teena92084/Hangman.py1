
import string
import random

def load_words():
    
    word_list = ["navgurukul", "learning", "kindness"]
    return word_list
    
    
def choose_word():
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()

    return secret_word  
    
