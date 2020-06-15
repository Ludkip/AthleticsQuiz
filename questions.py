import json

questions_string = '''
{
    "questions" : [
        {
        "question" : "What is the mens pole vault world record?",
        "correcta" : "b",
        "alt" : [
            "a" : "a. 6 m",
            "b" : "b. 6,18 m",
            "c" : "c. 5,54 m",
            "d" : "d. 20,71 m",
        ]
        }
    ]
}
'''

data = json.loads(questions_string)
print (data)