import random
# To install colorama, run the following command in your VS Code terminal:
# python3 -m pip install colorama
from colorama import Fore, Back, Style, init
init(autoreset=True) #Ends color formatting after each print statement

from wordle_secret_words import get_secret_words
from valid_wordle_guesses import get_valid_wordle_guesses

#they are 5 letters and are valid word pool

valid_wordle_guesses = set(get_valid_wordle_guesses())
secret_words = set(get_secret_words())


def basic_check(guess: str, secret_word: str):
    
    if(not(guess.isalpha() and secret_word.isalpha())):
        return False
    else:
        return True
def get_feedback(guess: str, secret_word: str) -> str:
    '''Generates a feedback string based on comparing a 5-letter guess with the secret word. 
       The feedback string uses the following schema: 
        - Correct letter, correct spot: uppercase letter ('A'-'Z')
        - Correct letter, wrong spot: lowercase letter ('a'-'z')
        - Letter not in the word: '-'

        Args:
            guess (str): The guessed word
            secret_word (str): The secret word

        Returns:
            str: Feedback string, based on comparing guess with the secret word
    
        Examples
        >>> get_feedback("lever", "EATEN")
        "-e-E-"
            
        >>> get_feedback("LEVER", "LOWER")
                "L--ER"
            
        >>> get_feedback("MOMMY", "MADAM")
                "M-m--"
            
        >>> get_feedback("ARGUE", "MOTTO")
                "-----"

    
    '''
    ### BEGIN SOLUTION
    guess = guess.lower()
    secret_word = secret_word.lower()
    
    if(not basic_check(guess, secret_word)):
        return "-----"

    copy_secret = secret_word
    return_string = ["-", "-", "-", "-", "-"]
 
    
    # for i in range(0, len(guess)):
    #     if(guess[i] in copy_secret):
    #         if (guess[i] == secret_word[i]):
    #             return_string += guess[i].upper()
    #         else:
    #             return_string += guess[i]
    #         copy_secret.replace(guess[i], "", 1)
    #         print(copy_secret)
    #     else:
    #         return_string += "-"
    
    for i in range(0, len(guess)):
        if (guess[i] == secret_word[i]):
            return_string[i] = guess[i].upper()
            copy_secret = copy_secret.replace(guess[i], "", 1)

    
    for k in range(0, len(guess)):
        if(guess[k] in copy_secret) and (guess[k] != secret_word[k]):
            return_string[k] = guess[k]
            copy_secret = copy_secret.replace(guess[k], "", 1)

    
    return ''.join(return_string)
    ### END SOLUTION 

def get_AI_guess(guesses: list[str], feedback: list[str], secret_words: set[str], valid_guesses: set[str]) -> str:
    '''Analyzes feedback from previous guesses/feedback (if any) to make a new guess
        
        Args:
         guesses (list): A list of string guesses, which could be empty
         feedback (list): A list of feedback strings, which could be empty
         secret_words (set): A set of potential secret words
         valid_guesses (set): A set of valid AI guesses
        
        Returns:
         str: a valid guess that is exactly 5 uppercase letters
    '''
    ### BEGIN SOLUTION
    
    return_string = ["-", "-", "-", "-", "-"]
    bad_letters = set()
    close_letters = set()
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    
    for i in range(len(guesses)):
        for j in range(len(guesses[i])):
            if feedback[i][j] == "-":
                bad_letters.add(guesses[i][j])
            
    for i in feedback:
        for j in range(len(i)):
            if (ord(i[j]) > 64) and (ord(i[j]) < 91):
                return_string[j] = i[j]
    
    for i in range(len(return_string)):
        if return_string[i] != "-":
            for j in alphabet:
                if not (j in bad_letters):
                    return_string[i] = j
                    break
    
    
    return ''.join(return_string)
    
    
   #loop through guesses to see which words dont work
    ### END SOLUTION 

# TODO: Define and implement your own functions!


if __name__ == "__main__":
    print(Fore.RED + 'some red text')
    print(Back.GREEN + 'and with a green background' + Back.YELLOW + "dsl;fmlksdfg")
    print(Style.DIM + 'and in dim text')
    print(Style.RESET_ALL)
    print('back to normal now')
    # TODO: Write your own code to call your functions here
    print(get_feedback("MOMMY", "MADAM"))
    pass