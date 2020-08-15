class Employee:

    # this are known as class variables.which are common for all the instances.
    num_of_emps = 0
    raise_amt = 1.04 

    # this is init method(methos is class fuction). 
    # Every time when instance is created init method runs by default.
    # In the class when we run a method, instance of that class is passed as argument
    # so self is the name of that arguments
     
    def __init__(self, first, last, pay):
        self.fisrt = first # it is not necessory to give samge name both side. like here first...
        self.last = last
        self.pay = pay

        # Every instance increasse the num_of_employee count
        Employee.num_of_emps += 1


    # These are regular method
    # function in class is known as method or regular method
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


    # It is used to use methods of class as attributes
    @property
    def email(self):
        return '{} {}@email.com'.format(self.first, self.last)

        # to use this 
        # just rpint(eml_1.email) instead of eml_1.email()

    # this is for setter and deleter examples
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # to use this
    # emp_1.fullname = 'Demo User'
    # print(emp_1.first)
    # print(emp_1.email)
    # print(emp_1.fullname)
    # if we dont use @fullname.setter then by running abouve code 
    # it throghs error like can not set attribute for fullname

    @fullname.deleter
    def fullname(self, name):
        print('Delete Name!')
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay + self.raise_amt)

    
    
    
    
    # Special Methods(Magic/Dunder)
    # is used to give added value to aur class
    # is surrounded by double underscore(__name_of_method__)

    def __repr__(self): # is used to unabicuese representation of object
        return "Employee('{}', '{}', '{}')". format(self.first, self.last, self.pay)

    def __str__(self): # is readable represenataion of object.
        return '{} - {}'.format(self.fullname(), self.pay)

        # when dunder str is used and if we call employee instance 
        # then is will print a str rather than repr
        # to use this 
        # print(eml_1) will give you kaushal kokhar - 25000

    # arithmatic dunder method
    def __add__(self, other):
        return self.pay + other.pay

        # to use this 
        # print(emp_1 + emp_2) will give you total salary of that two employee..
        # without dunder add it will throgh an eror

    
    
    
    # these are class methods
    # To take the class as first argument unlike regular method takes intance as first argu..
    # used to change or edit class variable
    @classmethod
    def set_raise_amt(cls, amount): # cls is common convention to use class variable
        cls.raise_amt = amount
        # cls means the name of class. Here cls == Employee
        # cls.raise_amt is name of class variable created at top...
        
            # to use this
            # Employee.set_raise_amt(1.05)

    # atlternative construcor to separate string
    # basically constuctor means to customise the class methods
    @classmethod
    def from_string(cls, emp_str)
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

            # To run this
            # new_eml = Employee.from_string('kaushal-khokhar-25000')
         
    
    # These are static methods
    # static methods don't pass anything automatically as regular and class methods
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            # 5 is saturday and 6 is suunday, defualts in python
            return False
        return True

        # in this method we does not use instance or class as self or cls.
        # to use this
        # Employee.is_workday('pass the day in proper format')
    
# inheritance (subclass)
# basicallu it is modified verison of previous class
# we can use same attributes and methods of previous class here.........
class Developer(Employee):
    # When we instanciate a develpoer class first it find a method or atributes
    # in Develpoer class if not foud there then go to Employee class...
    raise_amt = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
                # or
        # Employee.__init__(self, first, last, pay)

        # Above both of this method use to pass first, lat and pay
        # to be hadled by Employee class
        # so basically it is used to pass this argumetns to parent class..

        self.prog_lang = prog_lang


class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)        
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_amp(self, emp):
        if amp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

# isinstance and issubclass are two function 
# used for inheritance classses to check 
# whether given intance/class is belog to given parent class
# to use it
# print(isinstance(eml_1, Developer) will return true or false

# Special Methods(Magic/Dunder)
# is used to give added value to aur class
# is surrounded by double underscore(__name_of_method__)







emp_1 = Employee("kaushal", "khokhar", 25000)
emp_2 = Employee("test", "user", 15000)

print(emp_1)

