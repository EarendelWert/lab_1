# TODO Напишите функцию find_common_participants
def find_common_participants(participants_f, participants_s, separator=','):
    first_group_list = participants_f.split(separator)
    second_group_list = participants_s.split(separator)
    common_p = set(first_group_list).intersection(set(second_group_list))
    return sorted(common_p)

participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group, participants_second_group)

print(f"Общие участники: {', '.join(common_participants)}")