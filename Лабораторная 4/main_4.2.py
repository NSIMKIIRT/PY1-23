import csv
import json
# TODO импортировать необходимые молули


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(csv_file_path=INPUT_FILENAME, json_file_path=OUTPUT_FILENAME, delimiter=",", newline="\n") -> None:
    try:
        with open(csv_file_path, 'r', newline=newline, encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=delimiter)
            data_list = [row for row in reader]  # TODO считать содержимое csv файла

        with open(json_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4, ensure_ascii=False)   # TODO Сериализовать в файл с отступами равными 4
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
