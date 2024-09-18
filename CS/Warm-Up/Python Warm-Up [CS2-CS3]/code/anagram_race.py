import itertools
from TimingProfiler import TimingProfiler

def basic_checks(word1:str, word2:str)-> tuple[bool, str, str]:
    '''Implements top-level checks common to each is_anagram approach. 
       Anagram basic checks include ensuring the two input words:
        -aren't be the same word
        -are case insensitive
        -don't include characters other than A-Z, a-z
        -have the same length, with at least two letters

       Args:
         word1: The first word
         word2: The second word

       Returns:
         bool: False if the two words fail a basic check, True otherwise
         str: A lowercase version of word1 only containing A-Z, a-z
         str: A lowercase version of word2 only containing A-Z, a-z
        
       Examples:
        >>> basic_checks("baste2", "Beast")
        True, baste, beast
        >>> basic_checks("baste", "Beasts")
        False, baste, beasts
    '''
    ### BEGIN SOLUTION
    word1 = word1.lower()
    word2 = word2.lower()
    if word1 == word2:
        return False
    for i in word1:
        if ord(i) >= 122 or ord(i) <= 61:
            return False
    for i in word2:
        if ord(i) >= 122 or ord(i) <= 61:
            return False
    if len(word1) != len(word2):
        return False
    return True
        
            

    ### END SOLUTION 


def is_anagram_exhaustive(word1:str, word2:str)->bool:
    '''Generate all possible permutations of the first word until you find one that is the second word.
       If no permutation of the first word equals the second word, the two are not anagrams.

       Args:
        word1: The first word
        word2: The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''
    ### BEGIN SOLUTION
    word1 = word1.lower()
    word2 = word2.lower()
    if not basic_checks(word1, word2):
        return False
    
    perm = ["".join(i) for i in itertools.permutations(word1)]

    for i in perm:
        if i == word2:
            return True
    return False
    
    
    
    

    ### END SOLUTION 

def is_anagram_checkoff(word1:str, word2:str)->bool:
    '''Create a parallel list-based version of the second word (strings are immutable).
       Check off letters in the list as they are found by setting the value to None.

       Args:
        word1: The first word
        word2: The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''
    ### BEGIN SOLUTION
    word1 = word1.lower()
    word2 = word2.lower()
    if not basic_checks(word1, word2):
        return False
    
    wordlist1 = [i for i in word1]
    wordlist2 = [i for i in word2]
    
    for i in range(len(word1)):
        for j in range(len(word2)):
            if wordlist1[i] == wordlist2[j]:
                wordlist1[i] = None
                wordlist2[j] = None
                break
    for i in range(len(wordlist1)):
        if wordlist1[i] != None:
            return False
    return True
       
    ### END SOLUTION 

def is_anagram_lettercount(word1:str, word2:str)->bool:
    '''Two approaches:
      Approach 1) Create two lists of length 26 to keep track of letter counts in each word.
                    ie. [0] represents the letter a, [1] represents the letter b, and so on…
                  HINT- ASCII conversions will be helpful: ord("A") → 65. chr(65)  -> “A”
 
      Approach 2) Create two dictionaries  to keep track of letter counts in each word.

      Compare final versions of each list to determine if the words are anagrams.
      
       Args:
        word1 (str): The first word
        word2 (str): The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''
    ### BEGIN SOLUTION
    word1 = word1.lower()
    word2 = word2.lower()
    if not basic_checks(word1, word2):
        return False
    list = [0 for i in range(0, 128)]
    
    for i in word1:
       list[ord(i)] = list[ord(i)] + 1
    for i in word2:
       list[ord(i)] = list[ord(i)] - 1
       
    for i in range(0, 128):
        if list[i] != 0:
            return False
    return True
    ### END SOLUTION 

def is_anagram_sort_hash(word1:str, word2:str)->bool:
    '''Sort both words, then compare to see if they are exactly the same.

       Args:
        word1 (str): The first word
        word2 (str): The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''
    ### BEGIN SOLUTION
    word1 = word1.lower()
    word2 = word2.lower()
    if not basic_checks(word1, word2):
        return False
    wordlist1 = [i for i in word1]
    wordlist2 = [i for i in word2]
    
    wordlist1.sort()
    wordlist2.sort()
    if wordlist1 == wordlist2:
        return True
    else:
        return False
    ### END SOLUTION 

ch_to_prime = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13,
    'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43,
    'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79,
    'w': 83, 'x': 89, 'y': 97, 'z': 101 }

def is_anagram_prime_hash(word1:str, word2:str)->bool:
    '''Create a dictionary of prime numbers (see chToprime above). Use the ascii value of each letter in both
      words to construct a unique numeric representation of the word (called a 'hash').
      Words with the same hash value are anagrams of each other.

       Args:
        word1 (str): The first word
        word2 (str): The second word

       Returns:
        bool: True if word1 and word2 are anagrams, False otherwise 
    '''
    ### BEGIN SOLUTION
    word1 = word1.lower()
    word2 = word2.lower()
    if not basic_checks(word1, word2):
        return False
    prime1 = 1
    prime2 = 1
    for i in word1:
        prime1 = prime1 * ch_to_prime[i]
    for i in word2:
        prime2 = prime2 * ch_to_prime[i]
    if prime1 == prime2:
        return True
    else:
        return False
    
    
    ### END SOLUTION 

if __name__ == "__main__":
    algorithms = [is_anagram_exhaustive, is_anagram_checkoff, is_anagram_lettercount, is_anagram_sort_hash, is_anagram_prime_hash]
    word1 = "beast"
    word2 = "baste"

    for algorithm in algorithms:
        print(f"{algorithm.__name__}- {word1}, {word2}: {algorithm(word1, word2)}")