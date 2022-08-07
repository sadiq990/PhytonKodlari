## this is a quiz game made by Sadig Musazade

print("welcome to Quiz game version 1")

intro = input("Do you want to start? ")

if intro.lower() != 'yes':
    print("Thank you for your time")
    quit()
else:
    print("We can start")

answer1 = input ("What was Meta Platforms Inc formerly known as?  ")
if answer1.lower() == "facebook":
    print("correct")
else:
    print("not correct")

answer2 = input ("Which English city is known as the Steel City?  ")
if answer2.lower() == "Sheffield":
    print("correct")
else:
    print("not correct")

answer3 = input ("Which former British colony was given back to China in 1997?  ")
if answer3.lower() == "Hong Kong":
    print("correct")
else:
    print("not correct")

answer4 = input ("The logo for luxury car maker Porsche features which animal?  ")
if answer4.lower() == "Horse":
    print("correct")
else:
    print("not correct")