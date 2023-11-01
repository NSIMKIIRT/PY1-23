# TODO Напишите функцию find_common_participants

def find_common_participants(participants_first_group, participants_second_group, delimeter='|'):
    participants1 = set(participants_first_group.split(delimeter))
    participants2 = set(participants_second_group.split(delimeter))
    common_participants = participants1.intersection(participants2)
    return sorted(list(common_participants))


participants_first_group = ["Иванов|Петров|Сидоров"]
participants_second_group = ["Петров|Сидоров|Смирнов"]

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group[0], participants_second_group[0])
print(common_participants)
print(find_common_participants(participants_first_group[0], participants_second_group[0], ))
