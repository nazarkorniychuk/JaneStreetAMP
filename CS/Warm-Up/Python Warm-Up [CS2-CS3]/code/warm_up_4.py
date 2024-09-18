def get_menu_choice()->list:
    """Prompts the use to enter a valid menu choice to indicate which sequence should be generated.
       Also prompts the user to enter how many terms they would like to see.

       Returns:
          A list consisting of two items:
            - the number of terms in the sequence
            - a single letter indicating the desired type of sequence 
    """
    print("Enter your choice:")
    print("-----------------")
    print("  (O)dd Integers")
    print("  (M)ultiples")
    print("  (S)quare numbers")
    print("  (T)riangular numbers")
    print("  (A)rithmetic Sequence")
    print("  (F)ibonacci Sequence")
    choice = input("Which sequence would you like to generate?\n")

    while choice.lower() not in ["o", "m", "s", "t", "a", "f"]:
        choice = input("Which sequence would you like to generate?\n")

    n = int(input("How many terms would you like to see?\n"))

    return [n, choice.lower()] 


def positive_odds(n: int)->list:
    return [2*i + 1 for i in range(n)]

def positive_multiples(n: int, m: int)->list:
    if m > 0: 
      return [i*m for i in range(1, n+1)]
    else:
      return []
      


def square_numbers(n: int)->list:
    return [i*i for i in range(n)]


def triangle_numbers(n: int)->list:
    if n > 0:
      list = [1]
      for i in range(1, n):
        list.append(list[i-1] + i + 1)
      return list
    else:
      return []
      
    

def arithmetic_sequence(n: int, t1: int, t2: int)->list:
    if n > 0:
      list = [t1]
      for i in range(1, n):
        list.append(list[i-1] + t2 - t1)
      return list
    else:
      return []


def fibonacci_sequence(n: int)->list:
    if n > 1:
      list = [1, 1]
      for i in range(2, n):
        list.append(list[i-1] + list[i-2])
      return list
    elif n == 1:
      return [1]
    else: 
      return []


if __name__ == "__main__":
    n, choice = get_menu_choice()
  
    match choice:
        case "o":
            seq = positive_odds(n)
            label = "Positive Odd Integers"
        case "m":
            multiple = int(input("Which multiple would you like to use?"))
            seq = positive_multiples(n, multiple)
            label = "Positive Integer Multiples"
        case "s":
            seq = square_numbers(n)
            label = "Square Numbers"
        case "t":
            seq = triangle_numbers(n)
            label = "Triangle Numbers"
        case "a":
            term_1 = int(input("What is the first term of the arithmetic sequence?"))
            term_2 = int(input("What is the second term of the arithmetic sequence?"))
            seq = arithmetic_sequence(n, term_1, term_2)
            label = "Arithmetic Sequence"
        case  "f":
            seq = fibonacci_sequence(n)
            label = "Fibonacci Numbers"
        case _:
            seq = None

    print(f"The first {n} terms of the {label}: {seq}")
    