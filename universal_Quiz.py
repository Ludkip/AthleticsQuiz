import random
import json
qnr = 0  #number of questions
qlimit = False   #question limit(if all questions are used)
score = 0    #users score


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
            score = score +1

        else:
            print('wrong answer')

    else:
        pass

    if qnr == len(data['questions']):
        qlimit = True

print('Your score was', score, "/", qnr)
if score == qnr:
    print ("Congratulations! 100%")
elif score > qnr/2:
    print('Congratulations! more than 50% correct')
elif score > 0:
    print('There is some potential...')
else:
    print('yikes...')    