class Student(object):
    """Creates a Student object"""
    def __init__(self, idNumber, fullName):
        self.idNumber= idNumber
        self.fullName = fullName
        self.firstName, self.lastName = self.splitName()


    def splitName(self):
        firstSpace = self.fullName.find(' ')
        comma = self.fullName.find(',')
        secondSpace = self.fullName.find(' ', comma+2)
        lastName = None
        if firstSpace < comma:
            lastName = self.fullName[:firstSpace]
        else:
            lastName = self.fullName[:comma]
        if secondSpace != -1:
            firstName = self.fullName[comma+2: secondSpace]
        else:
            firstName = self.fullName[comma+2: ]
        return firstName, lastName

    def __str__(self):
        return "ID: " + str(self.idNumber) + "\nFirstName: " +str(self.firstName) + "\nLastName: " +str(self.lastName)

class GradedStudent(Student):
    """Graded student is a student with a dictionary of grades"""
    def __init__(self, idNumber:int, fullName:str, grades: dict):
        super(GradedStudent,self).__init__(idNumber, fullName)
        self.grades = grades

    def getMissingAssignments(self):
        """Returns a list of missing assignments, returns None if none"""
        if "NHI" not in self.grades.values():
            return None
        missing = []
        for assignmentName, grade in self.grades.items():
            if grade == "NHI":
                missing.append(assignmentName)
        return missing

    def getStudentAverage(self):
        """Returns the students average"""
        return self.grades['Average']

    def getLetterGrade(self):
        """Returns the letter grade of a student"""
        return self.grades['Grade']