import csv
import pkg_resources

def find_answer(task_text):
    data_path = pkg_resources.resource_filename('osy', 'data/oneliner.csv')
    with open(data_path, 'r', encoding='utf-8', errors='ignore') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 2:
                task, answer = row
                if task_text in task:
                    return task, answer
    return task_text, "Ответ не найден"