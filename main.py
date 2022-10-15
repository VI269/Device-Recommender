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
    with open(file) as f:
        outs = []
        questions = remove_new_lines(f.readlines()[1:])
        for _ in questions:
            for exp in _.split(" | ")[1].split(","):
                for response in questionnaire_results:
                    if exp == response:
                        outs.append(_.split(' | ')[0])
        if len(outs) == 0:
            matches = {}
            for _ in questions:
                for exp in _.split(" | ")[1].split(","):
                    

if __name__ == '__main__':
    print(process("", "device.txt"))
