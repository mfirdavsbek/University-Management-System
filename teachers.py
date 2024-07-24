from faculty_class import Faculty
class TeachingAssistant(Faculty):
    def __init__(self,type, name, pass_id, email, bd, gender, nationality, phone, course, occupation, hours, salary, title, employee_id, research_topic):
        super().__init__(type, name, pass_id, email, bd, gender, nationality, phone, course, occupation, hours, salary, title)
        self.set_employee_id(employee_id)
#setters
    def set_employee_id(self, employee_id):
        if employee_id[:2].isupper() and employee_id[2:].isdigit():
            self.__employee_id = employee_id
        else:
            raise ValueError("Employee ID cannot be empty.")
    def get_employee_id(self):
        return self.__employee_id
    def teaches(self):
        print("Helps the teacher with teaching tasks and managing the classroom.")

teachingAssistant = TeachingAssistant("Faculty",
                                      "Firdavsbek",
                                      "AC2924862",
                                      "mamasoliyevfirdavsbek9@gmail.com",
                                      "2004/04/05",
                                      "male",
                                      "uzbek",
                                      "998907877897",
                                      "economics",
                                      "full-time",
                                      18, 2200,
                                      "teaching assistant",
                                      "AA122333",
                                      "Economy")
teachingAssistant.teaches()
class Lecturers(Faculty):
    def __init__(self, type, name, pass_id, email, bd, gender, nationality, phone, course, occupation, hours, salary,
                 title, research_topic):
        super().__init__(type, name, pass_id, email, bd, gender, nationality, phone, course, occupation, hours, salary,
                         title)
    def teaches(self):
        print("The lecturer delivers educational content to students, often through presentations, discussions, and assessments.")

lecturer = Lecturers("Faculty",
                     "Adam Jons",
                     "AC97526545",
                     "adamjons7@gmail.com",
                     "1988/02/25",
                     "male",
                     "swedish",
                     "998918742622",
                     "international econimics",
                     "full-time",
                     18,
                     3000,
                     "lecturer",)
lecturer.teaches()
class AssistantProffessor(Faculty):
    def teaches(self):
        print("The assistant professor conducts research, teaches courses, and engages in academic service while working towards tenure.")

assistantProfessor = AssistantProffessor("Faculty", "Tom Holland", "AB1234567",
                                         "tomholland@gmail.com", "1979/04/08", "male",
                                         "british", "998907770707", "engineering",
                                         "full-time", 18, 4000, "assistant professor")
assistantProfessor.teaches()
class Academician(Faculty):
    def teaches(self):
        print("The professor conducts research, teaches courses, and engages in academic service while contributing to their field and the academic community.")
academician = Academician("Faculty", "Cai Yuhe", "AA3337799", "caiyuhe7@gmail.com",
                          "1970/01/01", "male", "chinese", "998900077897",
                          "physics", "full-time", 18, 5000, "academician")
academician.teaches()
