import json

def ask_the_questions(file):
    with open(file, 'r') as f:
        device_data = f.readlines()[0]
        questions = device_data.split(' | ')
    outputs = []
    for question in questions.split(','):
        outputs.append(input(question+" "))
    return outputs

def process(questionnaire_results, file):
    pass

if __name__ == '__main__':
    print(process(ask_the_questions('device.json'), 'device.json'))
