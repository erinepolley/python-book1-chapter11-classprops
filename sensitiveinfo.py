#SSN, DOB, health insurance:  can LOOK(GET) but no change(SET)
#first name, last name--cannot GET
#address: can both GET and SET
class Patient():
    def __init__(self, birth, insurance):
        self.social = "666-66-6666"
        self.birth = birth
        self.insurance = insurance 
        # self.full_name = self.first_name + self.last_name 

    # def full_name(self):
    #     return (f"{first_name}  {last_name}")

#SSN
    @property # The getter
    def social(self):
        try:
            return self.__social # Note there are 2 underscores here
        except AttributeError:
            return "No SSN"

    # @property # The getter
    # def social(self):
    #     try:
    #         return self.__social # Note there are 2 underscores here
    #     except AttributeError:
    #         return "No SSN"
    # @first_name.setter # The setter
    # def first_name(self, first_name):
    #     if type(first_name) is str:
    #         self.__first_name = first_name
    #     else:
    #         raise TypeError('Please provide a name')

erin = Patient()

print(erin.social)
