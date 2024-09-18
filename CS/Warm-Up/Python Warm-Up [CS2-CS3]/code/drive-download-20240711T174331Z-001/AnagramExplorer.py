class AnagramExplorer:
    def __init__(self, all_words: list[str]):
       self.__corpus = all_words
       self.anagram_lookup = self.build_lookup_dict() # Only calculated once, when the explorer object is created
       

    @property
    def corpus(self):
      return self.__corpus
    
    def prime_hash(self, word: str):
      #calculates the prime hash value for a given word
      prime_map = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13,
    'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43,
    'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79,
    'w': 83, 'x': 89, 'y': 97, 'z': 101 }
      hash_value = 1
      for letter in word:
        hash_value *= prime_map[letter]
      return hash_value

    def is_valid_anagram_pair(self, pair:tuple[str], letters:list[str]) -> bool:
        '''Checks whether a pair of words:
            -are both included in the allowable word list (self.corpus)
            -are both at least 3 letters long (and the same)
            -form a valid anagram pair
            -consist entirely of letters chosen at the beginning of the game

            Args:
                pair (tuple): Two strings representing the guessed pair
                letters (list): A list of letters from which the anagrams should be created

            Returns:
                bool: Returns True if the word pair fulfills all validation requirements, otherwise returns False
        '''
        ### BEGIN SOLUTION
        letters1 = letters.copy()
        
        if (len(pair[0]) != len(pair[1])) or (len(pair[0]) < 3) or (len(pair[1]) < 3) or (pair[1].lower() == pair[0].lower()):
            return False 
        if sorted(pair[0].lower()) != sorted(pair[1].lower()):
          return False
        if not (pair[0].lower() in self.corpus):
           return False
        for j in pair[0].lower():
          if not (j in letters1):
            return False
          else:
            pair[0].replace(j, "", 1)
            letters1.remove(j)
        return True
           

        ### END SOLUTION 
        
    def build_lookup_dict(self) -> dict:
        '''Creates a fast dictionary look-up (via either prime hash or sorted tuple) of all anagrams in a word corpus.
       
            Args:
                corpus (list): A list of words which should be considered

            Returns:
                dict: Returns a dictionary with  keys that return sorted lists of all anagrams of the key (per the corpus)
        '''
        ### BEGIN SOLUTION
        dict_of_letters = dict()
        for i in self.corpus:
          if (len(i) > 2):
            t = self.prime_hash(i)
            if t in dict_of_letters:
                dict_of_letters[t].append(i)
            else:
                dict_of_letters[t] = [i]
        for i in dict_of_letters:
            dict_of_letters[i].sort()
        
        return dict_of_letters
        ### END SOLUTION 

    def get_all_anagrams(self, letters: list[str]) -> set:
        '''Creates a set of all unique words that could have been used to form an anagram pair.
           Words which can't create any anagram pairs should not be included in the set.

            Ex)
            corpus: ["abed", "mouse", "bead", "baled", "abled", "rat", "blade"]
            all_anagrams: {"abed",  "abled", "baled", "bead", "blade"}

            Args:
              letters (list): A list of letters from which the anagrams should be created

            Returns:
              set: all unique words in corpus which form at least 1 anagram pair
        '''
        ### BEGIN SOLUTIONs
        set_of_words = set()
        letters_word = "".join(letters)
        for i in self.anagram_lookup.keys():
          if (len(self.anagram_lookup[i]) > 1) and (self.prime_hash(letters_word) % self.prime_hash(self.anagram_lookup[i][0]) == 0):
            for j in self.anagram_lookup[i]:
              set_of_words.add(j)
        return set_of_words
        ### END SOLUTION 

    def get_most_anagrams(self, letters:list[str]) -> str:
        '''Returns any word from one of the largest lists of anagrams that 
           can be formed using the given letters.
           
            Args:
              letters (list): A list of letters from which the anagrams should be created

            Returns:
              str: a single word from the largest anagram families
        '''
        ### BEGIN SOLUTION
        most_anagrams = 0
        letters_word = "".join(letters)
        for i in self.anagram_lookup.keys():
          if (len(self.anagram_lookup[i]) > 1) and (self.prime_hash(letters_word) % self.prime_hash(self.anagram_lookup[i][0]) == 0):
            if len(self.anagram_lookup[i]) > most_anagrams:
                most_anagrams = len(self.anagram_lookup[i])
        
        for i in self.anagram_lookup.keys():
          if (len(self.anagram_lookup[i]) > 1) and (self.prime_hash(letters_word) % self.prime_hash(self.anagram_lookup[i][0]) == 0):
            if len(self.anagram_lookup[i]) == most_anagrams:
              return self.anagram_lookup[i][0]
        
            
        
        ### END SOLUTION 

if __name__ == "__main__":
  words1 = [
     "abed","abet","abets","abut","acme","acre","acres","actors","actress","airmen","alert","alerted","ales","aligned","allergy","alter","altered","amen","anew","angel","angle","antler","apt",
     "bade","baste","bead","beast","beat","beats","beta","betas","came","care","cares","casters","castor","costar","dealing","gallery","glean","largely","later","leading","learnt","leas","mace","mane",
     "marine","mean","name","pat","race","races","recasts","regally","related","remain","rental","sale","scare","seal","tabu","tap","treadle","tuba","wane","wean"
  ]
  words2 = ["rat", "mouse", "tar", "art", "chicken", "stop", "pots", "tops" ]

  letters = ["l", "o", "t", "s", "r", "i", "a"]

  my_explorer = AnagramExplorer(words2)

  print(my_explorer.is_valid_anagram_pair(("rat", "tar"), letters))
  print(my_explorer.is_valid_anagram_pair(("stop", "pots"), letters))
  print(my_explorer.get_most_anagrams(letters))
  print(my_explorer.get_all_anagrams(letters))