class User:

    def __init__(self,employee_ref,name, address,mobile,gender):
        self.__employeerefrence = employee_ref
        self.__username = name
        self.__address = address
        self.__phone = mobile
        self.__gen = gender


    def set_emplyoeerefrence(self,employee_ref):
        self.__customerefrence=employee_ref

    def get_employeerefrence(self):
        return self.__employeerefrence

    def set_username(self,name):
        self.__username=name

    def get_username(self):
        return self.__username

    def set_address(self, address):
        self.__address = address

    def get_address(self):
        return self.__address

    def set_phonenumber(self, mobile):
        self.__phone = mobile

    def get_phonenumber(self):
        return self.__phone


    def set_gender(self,gender):
        self.__gen = gender

    def get_gender(self):
        return self.__gen


    def set_pno(self,mobile):
        self.__pno = mobile

    def get_pno(self):
        return self.__pno


