from Person import Person 

class AMPer(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.enrollment_year = year

  def get_info(self):
    info_str = "AMP" +" " + self.enrollment_year + " " + super().get_info()
    return info_str


if __name__ == "__main__":
  one_amper = AMPer("Lidiann","Speers","2024")
  print(one_amper.get_info())