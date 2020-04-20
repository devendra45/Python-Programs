class Student(Person):
    def __init__(self,firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores=scores

    def calculate(self):
        avg=sum(scores)/len(scores)
        if avg in range(90,101):
            return "O"
        elif avg in range(80,90):
            return "E"
        elif avg in range(70,80):
            return "A"
        elif avg in range(55,70):
            return "P"
        elif avg>=40 and avg<55:
            return "D"
        else:
            return "T"