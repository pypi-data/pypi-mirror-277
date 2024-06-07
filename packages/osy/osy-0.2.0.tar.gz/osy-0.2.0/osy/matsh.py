import csv
import pkg_resources

def sol(text):
    data_path = pkg_resources.resource_filename('osy', 'data/oneliner.csv')
    with open(data_path, 'r', encoding='utf-8', errors='ignore') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 2:
                task, answer = row
                if text in task:
                    return task, answer
    return text, "Ответ не найден"
