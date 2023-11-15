# TODO импортировать необходимые молули

import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    data = []

    # Чтение CSV файла
    with open(INPUT_FILENAME, "r", newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    # Запись в JSON файл с отступами равными 4
    with open(OUTPUT_FILENAME, "w") as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


