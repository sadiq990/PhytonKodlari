# this is a quiz game made by Sadig Musazade

print("welcome to Quiz game version 1")

intro = input("Do you want to start? ")

if intro.lower() != 'yes':
    print("Thank you for your time")
    quit()
else:
    print("We can start")

# questions
score = 0

answer1 = input("What was Meta Platforms Inc formerly known as?  ")
if answer1.lower() == "facebook":
    print("correct")
    score = score + 1
    print("current " + str(score))
else:
    print("not correct")

answer2 = input("Which English city is known as the Steel City?  ")
if answer2.lower() == "sheffield":
    print("correct")
    score = score + 1
    print("current " + str(score))
else:
    print("not correct")

answer3 = input(
    "Which former British colony was given back to China in 1997?  ")
if answer3.lower() == "hong kong":
    print("correct")
    score = score + 1
    print("current " + str(score))
else:
    print("not correct")

answer4 = input(
    "The logo for luxury car maker Porsche features which animal?  ")
if answer4.lower() == "horse":
    print("correct")
    score = score + 1
    print("current " + str(score))
else:
    print("not correct")

print("you got " + str(score) + "  questions correct")
