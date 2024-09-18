class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def get_info(self):
    return self.firstname + " "+ self.lastname

if __name__ == "__main__":
  someone = Person("Donald","Knuth")
  print(someone.get_info())