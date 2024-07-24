from user import User
from abc import ABC, abstractmethod

class Faculty(User):
    def __init__(self, type, name, pass_id, email, bd, gender, nationality, phone, course, occupation, hours, salary,title):
        super().__init__(type, name, pass_id, email, bd, gender, nationality, phone)
        self.set_course(course)
        self.set_occupation(occupation)
        self.set_hours(hours)
        self.set_salary(salary)
        self.set_title(title)
        self.weight = 0
        self.__titles = {
            "TEACHING ASSISTANTS": 1,
            "LECTURERS": 1.5,
            "SENIOR LECTURERS": 2,
            "ASSISTANT PROFESSOR": 2.5,
            "ASSOCIATE PROFESSOR": 3,
            "FULL PROFESSOR": 3.5,
            "ACADEMICIAN": 4
        }
#setter
    def set_course(self, course):
        course_list = []
        with open("course.txt", "r") as f:
            content = f.readlines()
            for line in content:
                words = line.split()
                for word in words:
                    course_list.append(word)
        if course.lower() in course_list:
            self.__course = course
        else:
            raise Exception("Something went wrong!")


    def set_occupation(self, occupation):
        if occupation.lower() == "part-time" or occupation.lower() == "full-time":
            self.__occupation = occupation
        else:
            raise Exception("Something went wrong!")
    def set_hours(self, hours):
        if type(hours) == int and hours >= 2:
            self.__hours = hours
        else:
            raise Exception("Something went wrong")

    def set_salary(self, salary):
        hrs = self.get_hours()
        extra_hrs = int(hrs) - 18
        if 2 <= hrs <= 18 and self.get_occupation().lower() == "full-time":
            self.__salary = salary
        elif 1 <= hrs <= 9 and self.get_occupation().lower() == "part-time":
            self.__salary = salary
        elif extra_hrs >= 0:
            hr_salary = self.get_salary() / 18
            if extra_hrs > 0:
                salary += 2 * extra_hrs * hr_salary
            self.__salary = salary
        else:
            raise ValueError("")
    def set_title(self, title):
        title_list = []
        with open("title.txt", "r") as f:
            content = f.readlines()
            for line in content:
                words = line.strip().split(",")
                for word in words:
                    title_list.append(word.strip())

        if title.lower() in (word.lower() for word in title_list):
            self.__title = title
        else:
            raise Exception("Invalid title")
#getter
    def get_course(self):
        return self.__course
    def get_occupation(self):
        return self.__occupation
    def get_hours(self):
        return self.__hours
    def get_salary(self):
        return self.__salary
    def get_title(self):
        return self.__title
    def __bonus(self, salary):
        self.__salary = salary
        extra_hrs = int(self.get_hours()) - 18
        if extra_hrs >= 1:
            hr_salary = self.get_salary() / 18
            salary += 2 * extra_hrs * hr_salary
        return salary

    @abstractmethod
    def teaches(self):
        pass

course = input("Enter courses: ")
occupation = input("Enter your occupation: ")
hours = int(input("Enter your hours: "))
salary = int(input("Enter your salary: "))
title = input("Enter your position: ")

faculty = Faculty("Faculty",
                  "Firdavsbek",
                  "AC2924862",
                  "mamasoliyevfirdavsbek9@gmail.com",
                  "2004/04/05",
                  "male",
                  "uzbek",
                  "998907877897",
                  "economics",
                  "part-time",
                  9,
                  2200,
                  "teaching assistant")