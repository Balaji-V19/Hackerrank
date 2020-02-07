class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self,fname,lname,idno,score):
        super().__init__(fname, lname, idno)
        self.fname=fname
        self.lname=lname
        self.idno=idno
        self.score=score
    def calculate(self):
        ls=self.score
        le=len(ls)
        res=0
        for i in range(le):
            res+=ls[i]
        va=res/le
        if(va>=90 and va<=100):
            return 'O'
        elif(va>=80 and va<90):
            return 'E'
        elif(va>=70 and va<80):
            return 'A'
        elif(va>=55 and va<70):
            return 'P'
        elif(va>=40 and va<55):
            return 'D'
        else:
            return 'T'    
    
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

line = input().split()
