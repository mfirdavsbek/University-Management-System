from user import User
from abc import ABC, abstractmethod
class Staff(User):
    def __init__(self, type, name, pass_id, email, bd, gender, nationality, phone, occupation, profile, wage, title):
        super().__init__(type, name, pass_id, email, bd, gender, nationality, phone)
        self.set_occupation(occupation)
        self.set_profile(profile)
        self.set_wage(wage)
        self.set_title(title)
    #setters
    def set_occupation(self, occupation):
        if occupation.lower() == "full-time" or occupation.lower() == "lower-time":
            self.__occupation = occupation
        else:
            raise ValueError("It has to be only full time or part time")
    def set_profile(self, profile):
        self.__profile = profile
    def set_wage(self, wage):
        if isinstance(wage, int):
            self.__wage= wage
        else:
            raise ValueError("Something went wrong!")
    def set_title(self, title):
        title_list = []
        with open("title.txt", "r") as f:
            content  = f.readlines()
            for line in content:
                words = line.strip().split(",")
                for word in words:
                    title_list.append(word.strip())
        if title.lower() in (word.lower() for word in title_list):
            self.title = title
        else:
            raise Exception("Something went wrong!")
    #getters
    def get_occupation(self):
        return self.__occupation
    def get_profile(self):
        return self.__profile
    def get_wage(self):
        return self.__wage
    def get_title(self):
        return self.__title
    @abstractmethod
    def employees(self):
        pass

staff = Staff("staff", "Firdavsvek Mamasoliyev", "AC2924862", "mamasoliyevfirdavsbek9@gmail.com", "2004/04/05", "male", "uzbek", "998907877897", "full-time", "mfirdavsbek", 2200, "teacher assistant")
print(staff.get_profile())


