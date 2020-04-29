import random

questions = ["q1", "q2", "q3"]

qu1 = {"question" : "What is the mens pole vault world record?", "correcta" : "b", "answers" : {"a" : "a. 6 m", "b" : "b. 6,18 m","c" : "c. 5,54 m", "d" : "d. 20,71 m"}}
correcta = "b"

q2 = ("Who has the mens triple jump world record?")
q2a = ["a. Christian Taylor", "b. Carl Lewis", "c. Jonathan Edwards", "d. Mike Powell"]

q3 = ("How long is a full outdoor track?")
q3a =  ["a. 200 m", "b. 100 m", "c. 300 m", "d. 400 m"]

qvalue = random.choice(questions)

if qvalue == "q1":
    print (qu1["answers"])
    
    for a in (qu1["answers"]):
        print(type(a))
        print (a.values())
    answer = input()
    if answer == correcta:
        print ("Correct answer")

    else:
        print ("Wrong answer")

elif qvalue == "q2":
    print (q2)
    print (q2a)
    answer = input()
    if answer == "c":
        print ("Correct answer")

    else:
        print ("Wrong answer")

if qvalue == ("q3"):
    print (q3)
    print (q3a)
    answer = input()
    if answer == "d":
        print ("Correct answer")
    
    else:
        print ("Wrong answer")
    