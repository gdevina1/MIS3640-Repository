from BabsonPerson import BabsonPerson

class Professor(BabsonPerson):

    def __init__(self, name, courses):
        BabsonPerson.__init__(self, name)
        self.courses = courses

    def getCourses(self):
        return self.courses
    
    def speak(self, utterance):
        return BabsonPerson.speak(self, "Folks, " + utterance)

    def isProfessor(obj):
        return isinstance(obj, Professor)


def main():

    faculty = Professor("Zhi Li", "MIS2640")
    print(faculty)
    print(faculty.speak("Python is cool."))
    print(isProfessor(faculty))


if __name__ == '__main__':
    main()
