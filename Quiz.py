import random
import json

with open('questions.json') as f:  
    data =json.load(f)

#for q in data['questions']:
    #print (q['question'], q['alt'])

live = random.choice in data['questions']
print (live)
'''  
questions = ["q1", "q2", "q3"]

qu1 = {"question" : "What is the mens pole vault world record?", "correcta" : "b", "alt" : {"a" : "a. 6 m", "b" : "b. 6,18 m","c" : "c. 5,54 m", "d" : "d. 20,71 m"}}

"""
q2 = ("Who has the mens triple jump world record?")
q2a = ["a. Christian Taylor", "b. Carl Lewis", "c. Jonathan Edwards", "d. Mike Powell"]

q3 = ("How long is a full outdoor track?")
q3a =  ["a. 200 m", "b. 100 m", "c. 300 m", "d. 400 m"]
"""
#qvalue = random.choice(questions)
qvalue="q1"


if qvalue == "q1":
    print (qu1["question"])
    
    for a in (qu1["alt"]):
        print (qu1["alt"][a])
    answer = input()
    if answer == (qu1["correcta"]):
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
    
'''