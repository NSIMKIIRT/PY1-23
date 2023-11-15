import json


def task(json_file_path) -> float:
    try:
        json_file_path = "input.json"
        with open(json_file_path) as file:
            data = json.load(file)
            sum_values = [item["score"] * item["weight"]  for item in data]
            total_sum = sum(sum_values)
            return round(total_sum, 3)
    except Exception as e:
        return f"Ошибка: {e}"


json_file_path = "input.json"

print(task(json_file_path))
