from itertools import combinations



def build_sorted_hash_dict(corpus: list) -> dict:
    '''Creates a fast dictionary look-up of words in a word corpus by anagrammability.
      
       Args:
        corpus (list): A list of words which should be considered

       Returns:
        dict: Returns a dictionary with sorted tuple keys that return sorted lists of all anagrams of the key (per the corpus)
              Keys: tuples of sorted letters
              Values: alphabetized list of words from the corpus which are all anagrams of each other

       Examples
       ----------
       >>> get_prime_hash_dict(["abed", "abled", "bade", "baled", "bead", "blade"])
       {
           ("a", "b", "d", "e"): ["abed", "bade", "bead"],
           ("a", "b", "d", "e", "l"): ["abled", "baled", "blade"]
       }
    
    '''
    ### BEGIN SOLUTION
    dict_of_letters = dict()
    for i in corpus:
        t = tuple(sorted([j for j in i]))
        if t in dict_of_letters:
            dict_of_letters[t].append(i)
        else:
            dict_of_letters[t] = [i]
    for i in dict_of_letters:
        dict_of_letters[i].sort()
    
    return dict_of_letters
    ### END SOLUTION 


prime_map = {'a': [2, 3], 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13,
    'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43,
    'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79,
    'w': 83, 'x': 89, 'y': 97, 'z': 101 }

def prime_hash(word: str):
  #calculates the prime hash value for a given word
  hash_value = 1
  for letter in word:
     hash_value *= prime_map[letter]
  return hash_value

def build_prime_hash_dict(corpus):
    '''Creates a fast dictionary look-up of words in a word corpus by anagrammability.

       Args:
        corpus (list): A list of words which should be considered

       Returns:
        dict: Returns a dictionary with prime hash keys that return sorted lists of all anagrams of the key (per the corpus)
              Keys: Prime hash values (ie. each letter mapped to a prime number, then multiplied together)
              Values: alphabetized list of words from the corpus which are all anagrams of each other

       Examples
       ----------
       >>> get_prime_hash_dict(["abed", "abled", "bade", "baled", "bead", "blade"])
       {
           462: ["abed", "bade", "bead"],
           17094: ["abled", "baled", "blade"]
       }
    '''
    ### BEGIN SOLUTION
    dict_of_primes = dict()
    for i in corpus:
        if prime_hash(i) in dict_of_primes:
            dict_of_primes[prime_hash(i)].append(i)
        else:
            dict_of_primes[prime_hash(i)] = [i]
            
    return dict_of_primes

    ### END SOLUTION 


def get_most_anagrams(corpus:list)->list:
    '''Uses a fast dictionary look-up to explore all anagram combinations in a word corpus.
  
       Args:
        corpus (list): A list of words which should be considered

       Returns:
        list: An alphabetized list of words
              -The returned list contains the alphabetized list of the first word 
               in the alphabetized list of words in each anagram group that produces 
               the maximum number of anagrams. 
               If no anagrams can be made from the corpus an empty list is returned.

       Examples
       ----------
       >>> get_most_anagrams(["rat", "mouse", "tar", "art", "chicken", "stop", "pots", "tops" ])
       ['art', 'pots']
       
    '''
    ### BEGIN SOLUTION
    dict_of_letters = build_sorted_hash_dict(corpus)
    max_lengths = 1
    
    for i in dict_of_letters:
        if max_lengths < len(dict_of_letters[i]):
            max_lengths = len(dict_of_letters[i])
    if max_lengths == 1:
        return []
    list_of_words = []
    for i in dict_of_letters:
        if max_lengths == len(dict_of_letters[i]):
            list_of_words.append(dict_of_letters[i][0])
    return sorted(list_of_words)

    

    ### END SOLUTION 

def get_all_anagrams(corpus:list[str])->set:
    '''Creates a set of all unique words in a word corpus that could have been used to form an anagram pair.
        Words which can't create any anagram pairs should not be included in the set.

        Args:
          corpus (list): A list of words which should be considered

        Returns:
          set: all unique words in wordlist which form at least 1 anagram pair

        Examples
        ----------
        >>> get_all_anagrams(["abed","mouse", "bead", "baled", "abled", "rat", "blade"])
        {"abed",  "abled", "baled", "bead", "blade"}
    '''
    ### BEGIN SOLUTION
    dict_of_letters = build_sorted_hash_dict(corpus)
    list_of_words = []
    
    for i in dict_of_letters.keys():
        if len(dict_of_letters[i]) > 1:
            list_of_words += dict_of_letters[i]
    return set(sorted(list_of_words))

    ### END SOLUTION 

if __name__ == "__main__":
    words1 = ["abed","abet","abets","abut","acme","acre","acres","actors","actress","airmen","alert","alerted","ales","aligned","allergy","alter","altered","amen","anew","angel","angle","antler","apt",
    "bade","baste","bead","beast","beat","beats","beta","betas","came","care","cares","casters","castor","costar","dealing","gallery","glean","largely","later","leading","learnt","leas","mace","mane",
    "marine","mean","name","pat","race","races","recasts","regally","related","remain","rental","sale","scare","seal","tabu","tap","treadle","tuba","wane","wean"]

    words2 = ["rat", "mouse", "tar", "art", "chicken", "stop", "pots", "tops" ]

    print(f"Sorting via the prime hashing function: {sorted(words2, key=prime_hash)}\n")
    
    print(f"Sorted tuple lookup dictionary: {build_sorted_hash_dict(words1)}")
    print(f"Prime hash lookup dictionary: {build_prime_hash_dict(words2)}\n")
    
    print(f"Most anagrams in words1:{get_most_anagrams(words1)}\n")
    print(f"Most anagrams in words2: {get_all_anagrams(words2)}")
