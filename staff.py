from user import User
from abc import ABC, abstractmethod
class Staff(User):
    def __init__(self, type, name, pass_id, email, bd, gender, nationality, phone, occupation, profile, wage, title):
        super().__init__(type, name, pass_id, email, bd, gender, nationality, phone)
        self.set_occupation(occupation)
        self.set_profile(profile)
        self.set_wage(wage)
        self.set_title(title)
    def set_occupation(self, occupation):
        if occupation.lower() == "full-time" or occupation.lower() == "lower-time":
            self.__occupation = occupation
        else:
            raise ValueError("It has to be only full time or part time")
    def set_profile(self, profile):
        self.__profile = profile
    def set_salary(self, salary):
        if isinstance(salary, int):
            self.__salary= salary
        else:
            raise ValueError("Something went wrong!")
    def set_title(self, title):
        title_list = []
        with open("title.txt", "r") as f:
            content  = f.readlines()
            for line in content:
                words = line.split("").strip()
                for word in words:
                    title_list.append(word.strip())
        if title.lower() in (word.lower() for word in title_list):
            self.title = title
        else:
            raise Exception("Something went wrong!")
        
