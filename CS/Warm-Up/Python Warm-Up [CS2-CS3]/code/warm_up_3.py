def get_side_lengths():
    """Prompts the user to enter three side lengths of a triangle.

    Returns:
      Three float values reprsenting the side lengths of the triangle
    """
    side_1 = float(input("Side 1: "))
    side_2 = float(input("Side 2: "))
    side_3 = float(input("Side 3: "))
    return side_1, side_2, side_3

def classify_triangle(side_1:float, side_2:float, side_3:float)->str:
    if side_1 > side_2:
      t = side_1
      side_1 = side_2
      side_2 = t
    if side_2 > side_3:
      t = side_3
      side_3 = side_2
      side_2 = t
    if side_1 > side_2:
      t = side_1
      side_1 = side_2
      side_2 = t
    
    if (side_1 + side_2) <= side_3:
      return "does not exist"
    elif (side_1*side_1 + side_2*side_2) > side_3*side_3:
      return "acute"
    elif (side_1*side_1 + side_2*side_2) < side_3*side_3:
      return "obtuse"
    elif (side_1*side_1 + side_2*side_2) == side_3*side_3:
      return "right"
    

if __name__ == "__main__":
    side1, side2, side3 = get_side_lengths()
    result = classify_triangle(side1, side2, side3)

    print(f"The given side lengths {side1}, {side2}, {side3}", end="") #skips line break
    if result == "does not exist":
        print(" DO NOT form a valid triangle.")
    else:
        print(f" form a valid {result} triangle.")