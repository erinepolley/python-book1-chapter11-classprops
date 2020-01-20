#SSN, DOB, health insurance:  can LOOK(GET) but no change(SET)
#first name, last name--cannot GET
#address: can both GET and SET
class Patient():
    def __init__(self, social, birth, insurance, first_name, last_name, address):
        self.__social = social
        self.__birth = birth
        self.__insurance = insurance 
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address
#fullname = firstname + lastname
    # def full_name(self):
    #     return (f"{first_name}  {last_name}")

#SSN
    @property # The getter
    def social(self):
            return self.__social

#BIRTHDAY
    @property # The getter
    def birth(self):
            return self.__birth

#INSURANCE
    @property # The getter
    def insurance(self):
            return self.__insurance

#FULL NAME!!!!!!!
    @property
    def full_name(self):
            return f"{self.__first_name} {self.__last_name}"

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
            raise TypeError('Please enter an address')

erin = Patient("666-66-6666", "11/06/85", 666, "Erin", "Polley", "666 Satan St")

print(erin.social) 
print(erin.full_name)
# print(erin.first_name)4