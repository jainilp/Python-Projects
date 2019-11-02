#Made by Jainil Patel
#CS171 Homework assignment one

from question import Question

if __name__ == "__main__":
    print('\nWelcome to The Trivia Show\n\n')
    questions = []
#Creates the list for the Objects, the questions are added below
    questions.append(Question('Who lives under the sea?', 'Perry The Platypus', 'Spongebob', 'Ash Ketchum', 'Monkey D. Luffy', 2))
    questions.append(Question('According to Phineas and Ferb, how many days are there of summer vacation.', '140', '410', '104', '180', 3))
    questions.append(Question('What is 25 squared?', '625', '225', '525', '24', 1))
    questions.append(Question('What is the integral of dx?', 'x', 't', 'dx', 'd', 1))
    questions.append(Question('What is third smallest element?', 'Helium', 'Javagen', 'Lithium', 'Pythonium', 3))
    questions.append(Question('Who wants to become the king of the pirates?', 'Sasuke Uchicha', 'Gon', 'Naruto Uzamaki', 'Monkey D. Luffy', 4))    
    questions.append(Question('What is a 3-d shape?', 'Sponge', 'Rectangle', 'Square', 'Pyramid', 4))
    questions.append(Question('Select the correct spelling.', 'Vacumm', 'Vacuum', 'Vaccum', 'Vaacum', 2))
    questions.append(Question('Select the working programming language.', 'Hyper-text Mining Language', 'Anaconda', 'Personal Home Page', 'Hyper-text Preprocessor', 4))
    questions.append(Question('Binary Representation of 3? (2 bits)', '10', '11', 'II', 'IO', 2))
    questions.append(Question('What is the abbreviation of Philadelphia?', 'NYC', 'LA', 'Philta', 'Phila', 4))
    questions.append(Question('Which number is not prime?', '2', '3', '4', '5', 3))
#These variables help keep track of the scores and whoes turn it is.
    one = 0
    two = 0
    playerTurn = 1
#for loop, which is used to use each object created with the questions beforehand.    
    for question in questions:
        print('Player', playerTurn, 'here is your question:')
#Gets questions and options in relation with object
        print(question)
        
        userAnswer = int(input('Enter your answer: '))
#Error Checking
        while userAnswer > 4 or userAnswer < 1:
            print('Error: Your answer has to be either 1, 2, 3, or 4. Try again.')
            userAnswer = int(input('Enter your answer: '))
#Answer Checking and Score Keeping
        if userAnswer == question.getAnswer():
            print('Correct! You are a genius.\n')
            if playerTurn % 2 == 0:
                two += 1
            else:
                one += 1
        else:
            print('That is incorrect.\n')
#Keeps track of turns.
        if playerTurn == 1:
            playerTurn = 2
        else:
            playerTurn = 1
        
    print('FINAL SCOREBOARD')
    print('Player One:', one)
    print('Player Two:', two)
    if one > two:
        print('Player One is the WINNER!')
    elif one == two:
        print('Draw!')
    else:
        print('Player Two is the WINNER!')