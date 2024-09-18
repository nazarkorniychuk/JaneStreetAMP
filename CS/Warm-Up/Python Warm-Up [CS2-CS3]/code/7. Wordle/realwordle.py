import random
# To install colorama, run the following command in your VS Code terminal:
# python3 -m pip install colorama
from colorama import Fore, Back, Style, init
init(autoreset=True) #Ends color formatting after each print statement

from wordle_secret_words import get_secret_words
from valid_wordle_guesses import get_valid_wordle_guesses


valid_wordle_guesses = set(get_valid_wordle_guesses())
secret_words = set(get_secret_words())


    
def basic_check(guess: str, secret_word: str) -> bool:
    return (guess.isalpha() and len(guess) == 5 and guess.upper() in valid_wordle_guesses)


def get_feedback(guess: str, secret_word: str) -> str:

    ### BEGIN SOLUTION
    guess = guess.lower()
    secret_word = secret_word.lower()
    
    if(not basic_check(guess, secret_word)):
        return "-----"

    copy_secret = list(secret_word)
    return_string = ["-", "-", "-", "-", "-"]

    
    for i in range(len(guess)):
        if (guess[i] == secret_word[i]):
            return_string[i] = guess[i].upper()
            copy_secret[i] = None

    for k in range(len(guess)):
        if(guess[k] in copy_secret) and (guess[k] != secret_word[k]):
            return_string[k] = guess[k]
            copy_secret[copy_secret.index(guess[k])] = None
    
    return ''.join(return_string)


def get_AI_guess(guesses: list[str], feedback: list[str], secret_words: set[str], valid_guesses: set[str]):
    for word in list(secret_words):  
        if not all(get_feedback(guesses[i], word) == feedback[i] for i in range(len(guesses))):  # basically checks if all comparisons in the for loop equate to true
            secret_words.remove(word)
    if (secret_words):
        return random.choice(list(secret_words))
    return random.choice(list(valid_guesses)) 
                

def secret_word_setter():
    return random.choice(list(secret_words))

def coloring(feedback: str, player_guess):
    result = ""
    for j in range(len(feedback)):
        if feedback[j].isupper():
            result = result + Back.GREEN + player_guess[j].upper()
        elif feedback[j].islower():
            result = result + Back.YELLOW + player_guess[j].upper()
        elif feedback[j] == "-":
            result = result + Back.BLACK + player_guess[j].upper()
    return result

if __name__ == "__main__":
    init()
    
    list_of_all_guesses = []
    aiguess = []
    feedback = [] 
    aifeedback = []
    
    secret_word = secret_word_setter()
    print(secret_word)
    winorlose = False
    player_guess = None
    
    for i in range(6):
        if(player_guess == None):
            player_guess = "crate"
            aiguess.append(player_guess)
            aifeedback.append(get_feedback(player_guess, secret_word))
        else:
            player_guess = get_AI_guess(aiguess, aifeedback, secret_words, valid_wordle_guesses)
            aiguess.append(player_guess)
            aifeedback.append(get_feedback(player_guess, secret_word))

        
        if(player_guess.lower() == secret_word.lower()):
            winorlose = True
            feedback = list(get_feedback(player_guess, secret_word))
            list_of_all_guesses.append(coloring(feedback, player_guess))
            for j in list_of_all_guesses:
                print(j)
            print("You won in " + str(i+1) + " guesses")
            break
        elif (basic_check(player_guess, secret_word)):
            feedback = get_feedback(player_guess, secret_word)
            list_of_all_guesses.append(coloring(feedback, player_guess))
                            
        for j in list_of_all_guesses:
            print(j)
        print("\n\n")
    
    if not winorlose:
        print("Decoc") 
           
    pass