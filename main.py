def ask_the_questions(file):
    with open(file, 'r') as f:
        device_data = f.readlines()[0]
        questions = device_data.split(' | ')
    outputs = []
    for question in questions.split(','):
        outputs.append(input(question+" "))
    return outputs

def remove_new_lines(array):
    out = []
    for item in array:
        out.append(item[:-2])
    return out

def process(questionnaire_results, file):
    with open(file, 'r') as f:
        for line in f.readlines():
            for name in line.split(' | '):
                if name[1].split(',') == questionnaire_results:
                    return name

if __name__ == '__main__':
    print(process(["y", "n", "n", "y"], "device.txt"))
