from datetime import date
class User:
    def __init__(self, type, name, pass_id, email, bd, gender, nationality, phone):
        self.set_type(type)
        self.set_name(name)
        self.set_pass_id(pass_id)
        self.set_email(email)
        self.set_birth_date(bd)
        self.set_gender(gender)
        self.set_nationality(nationality)
        self.set_phone(phone)
#setter
    def set_type(self, type):
        with open("type.txt", "r") as f:
            content = f.read().strip()
            type_list = content.split()
        if type.lower() in type_list:
            self.__type = type
        else:
            raise Exception("Something went wrong!")

    def set_name(self, name):
        if all(not letter.isdigit() for letter in name) and len(name) >= 2:
            self.__name = name
        else:
            raise ValueError("Please, enter your name as your passport!")

    def set_pass_id(self, pass_id):
        if (pass_id[:2].isupper() and pass_id[2:].isdigit() and len(pass_id) == 9) :
            self.__pass_id = pass_id
        else:
            raise Exception("Please, enter your pass ID as your passport")

    def set_email(self, email):
        if (email.endswith(".com") and email.__contains__("@")):
            self.__email = email
        else:
            raise ValueError("Email should contain @gmail.com")

    def set_birth_date(self, bd):
        if (bd[:4].isdigit() and  bd[4] == "/" and bd[5:7].isdigit() and  bd[7] == "/" and bd[8:10].isdigit()):
            if (int(bd[:4]) <= date.today().year and int(bd[5]) <= 1 and int(bd[6]) < 10 and int(bd[8]) <= 3 and int(bd[9]) < 10):
                self.__bd = bd
        else:
            raise ValueError("Please, enter your bd : YYYY/MM//DD")

    def set_gender(self, gender):
        if gender.lower() == "male" or gender.lower() == "female":
            self.__gender = gender
        else:
            raise ValueError("Something went wrong")

    def set_nationality(self, nationality):
        if isinstance(nationality, str):
            self.__nationality = nationality
        else:
            raise ValueError("Something went wrong, please enter your gender!")

    def set_phone(self, phone):
        if phone.startswith("998") and len(phone) == 12:
            self.__phone = phone
        else:
            raise ValueError("You entered wrong num!")
#getter
    def get_type(self):
        return self.__type
    def get_name(self):
        return self.__name
    def get_pass_id(self):
        return self.__pass_id
    def get_email(self):
        return self.__email
    def get_birth_date(self):
        return self.__bd
    def get_gender(self):
        return self.__gender
    def get_nationality(self):
        return self.__nationality
    def get_phone(self):
        return self.__phone

type = input("Enter your position: ")
name = input("Enter your name: ")
pass_id = input("Enter your Passport ID: ")
email = input("Enter your email: ")
bd = input("Enter your birthday date as YYYY/MM/DD: ")
gender = input("Enter your gender: ")
nationality = input("Enter your nationality: ")
phone = input("Enter your phone: ")

user = User(type, name, pass_id, email, bd, gender, nationality, phone)

print(user.get_type())
print(user.get_name())
print((user.get_pass_id()))
print(user.get_email())
print(user.get_birth_date())
print(user.get_gender())
print(user.get_nationality())
print(user.get_phone())