class Question:
    def __init__(self, question, opt1, opt2, opt3, opt4, ans):
        self.__question = question
        self.__option1 = opt1
        self.__option2 = opt2
        self.__option3 = opt3
        self.__option4 = opt4
        self.__answer = ans
        
    def __str__(self):
        string = self.__question + '\n' + '1) ' + self.__option1 + '\n2) ' + self.__option2 + '\n3) ' + self.__option3 + '\n4) ' + self.__option4
        return string

        
#Getters  
    def getQuestion(self):
        return self.__question
        
    def getAnswer(self):
        return self.__answer

#Setters
    def setQuestion(self, question, opt1, op2, op3, op4, ans):
        self.__question = question
        self.__option1 = opt1
        self.__option2 = opt2
        self.__option3 = opt3
        self.__option4 = opt4
        self.__answer = ans