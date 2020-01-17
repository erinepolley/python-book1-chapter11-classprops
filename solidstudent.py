class Student():
    def __init__(self, first_name, last_name, age, cohort): 
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.cohort = cohort

    def __str__(self):
       return f"{self.full_name} is {self.age} years old and is in cohort {self.cohort}."
    # def full_name(self):
    #     return (f"{first_name}  {last_name}")
 
    @property # The getter
    def first_name(self):
        try:
            return self.__first_name # Note there are 2 underscores here
        except AttributeError:
            return "No name"

    @first_name.setter # The setter
    def first_name(self, first_name):
        if type(first_name) is str:
            self.__first_name = first_name
        else:
            raise TypeError('Please provide a name')

    #LAST NAME
    @property # The getter
    def last_name(self):
        try:
            return self.__last_name 
        except AttributeError:
            return "No name"

    @last_name.setter # The setter
    def last_name(self, last_name):
        if type(last_name) is str:
            self.__last_name = last_name
        else:
            raise TypeError('Please provide a name')

    #AGE
    @property # The getter
    def age(self):
        try:
            return self.__age 
        except AttributeError:
            return "Please enter a number"

    @age.setter # The setter
    def age(self, age):
        if type(age) is int:
            self.__age = age
        else:
            raise TypeError('Please enter a number')

    #COHORT
    @property # The getter
    def cohort(self):
        try:
            return self.__cohort 
        except AttributeError:
            return "Please enter a number"

    @cohort.setter # The setter
    def cohort(self, cohort):
        if type(cohort) is int:
            self.__cohort = cohort
        else:
            raise TypeError('Please enter a number')
    
    #FULL NAME
    @property
    def full_name(self):
        try:
            return f"{self.first_name} {self.last_name}"
        except AttributeError:
            return "no full name, sry"
            

erin = Student("Erin", "Polley", 34, 36)

print(erin.first_name)
print(erin.last_name)
print(erin.age)
print(erin.cohort)
print(erin.full_name)
print(erin)