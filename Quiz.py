import random
import json
qnr = 0
qlimit = False

with open('questions.json') as f:  
    data =json.load(f)



while qlimit == False:
    live = random.choice (data['questions'])
    if (live['used']) == False:
        (live['used']) = True
        qnr = qnr + 1
        print (live['question'])
        print (live['alt'])
        answer = input()
        if answer == live['correcta']:
            print('correct answer')

        else:
            print('wrong answer')

    else:
        qnr = qnr
    
    if qnr == 3:
        qlimit = True

print ("Congratulations")