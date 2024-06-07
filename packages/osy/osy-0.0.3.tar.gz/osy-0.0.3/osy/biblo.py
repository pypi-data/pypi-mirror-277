import csv
def find_answer(task_text):
    with open('oneliner.csv', 'r', encoding='utf-8', errors='ignore') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 2:
                task, answer = row
                if task_text in task:
                    return task, answer
    return task_text, "Ответ не найден"