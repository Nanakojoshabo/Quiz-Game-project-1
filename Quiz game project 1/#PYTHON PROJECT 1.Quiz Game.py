#PYTHON PROJECT 1
#QUIZ GAME
print("Welcome to Nana Kojo Quiz!") 

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
print("Okay! Let's play :)")
score = 0

#Question 1
print("Question 1")
answer = input("What does CRO stand for? ")
if answer.lower() == "cathode ray oscilloscope":
    print("Correct")
    score += 1
else:
    print("Incorrect")

#Question 2
print("Question 2")
answer = input("What does WWW stand for? ")
if answer.lower() == "world wide web":
    print("Correct")
    score += 1
else:
    print("Incorrect")

#Question 3
print("Question 3")
answer = input("Where is DNA stored? ")
if answer.lower() == "nucleus":
    print("Correct")
    score += 1
else:
    print("Incorrect")

#Question 4
print("Question 4")
answer = input("What is the efficiency of class A amplifier... ")
if answer.lower() == "25%" or answer == "25":
    print("Correct")
    score += 1
else:
    print("Incorrect")

#Question 5
print("Question 5")
answer = input("A force of 100N compresses a spring,the spring constant is 20N/m,Find the extension...")
if answer.lower() == "5m" or answer == "5":
    print("Correct")
    score += 1
else:
    print("Incorect")

#Question 6
print("Let's continue with programming questions")
print("Question 6")
playing = input("do you want to coninue.. ")
if playing.lower() != "yes":
    quit()
print("Let's play")

answer = input("what is the full form of POP ")
if answer.lower() == ("procedure oriented programming"):
    print("Correct")
    score += 1
else:
    print("Incorrect")

#Question 7
print("Question 7")
answer = input("Which year was python introduced ")
if answer.lower() == "1991":
    print("Correct")
    score += 1
else:
    print("Incorrect")

#Question 8
print("Questiom 8")
answer = input("What is the full form of OOP ")
if answer.lower() == "object oriented programming":
    print("Correct")
    score += 1
else:
    print("Incorrect")

#Question 9
print("Welcome to General Knowledge ")
print("Question 9")
answer = input("The Second World War took place within 1939 to.. ")
if answer.lower() == "1945":
    print("Correct")
    score += 1
else:
    print("Incorrect")

#Question 10
print("Question 10")
answer = input("India is part of which continent? ")
if answer.lower() == "asia":
    print("Correct")
    score += 1
else:
    print("Incorrect")
    
#Total questions 
print("TOTAL QUESTIONS ANSWERED:")
print("You got " + str(score) + " questions correct!" )
percentage = (score/10) * 100
print("You got " + str(percentage) + "%." )

#performance message
if percentage < 50:
    print("FAIL")
elif percentage == 50:
    print ("FAIR")
elif percentage == 100:
    print("EXCELLENT")
else:
    print("VERY GOOD")







