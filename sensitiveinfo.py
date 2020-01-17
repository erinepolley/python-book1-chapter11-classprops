#SSN, DOB, health insurance:  can LOOK(GET) but no change(SET)
#first name, last name--cannot GET
#address: can both GET and SET
class Patient():
    def __init__(self, social, birth, insurance, first_name, last_name, address):
        self.__social = social
        self.__birth = birth
        self.__insurance = insurance 
        self.__address = address
#fullname = firstname + lastname
    # def full_name(self):
    #     return (f"{first_name}  {last_name}")

#SSN
    # @property # The getter
    # def social(self):
    #     try:
    #         return self.__social # Note there are 2 underscores here
    #     except AttributeError:
    #         return "No SSN"

    # @property
    # def full_name(self):
    #     try:
    #         return f"{self.first_name} {self.last_name}"
    #     except AttributeError:
    #         return "no full name, sry"

# ADDRESS GETTER
    @property 
    def address(self):
        try:
            return self.__address
        except AttributeError:
            return "Please enter an address"

    @address.setter # The setter
    def address(self, address):
        if type(address) is str:
            self.__address = address
        else:
            raise TypeError('Please enter a number')
#SSN!!!!!!!!!!!!!!!!!!!!!!!!!
    @property 
    def social(self):
        try:
            return self.__social # Note there are 2 underscores here
        except AttributeError:
            return "No SSN"

    # @first_name.setter # The setter
    # def first_name(self, first_name):
    #     if type(first_name) is str:
    #         self.__first_name = first_name
    #     else:
    #         raise TypeError('Please provide a name')

erin = Patient("666-66-6666", "11/06/85", 666, "Erin", "Polley", "666 Satan St")

print(erin.social)
