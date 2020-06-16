import random
import json

with open('questions.json') as f:  
    data =json.load(f)


live = random.choice (data['questions'])
print (live['question'])
print (live['alt'])
answer = input()
if answer == live['correcta']:
    print('correct answer')

else:
    print('wrong answer')
