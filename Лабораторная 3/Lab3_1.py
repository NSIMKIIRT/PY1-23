# TODO Напишите функцию для поиска индекса товара
def warehouse(items_list, find_item):
    for item in items_list:
        if item == find_item:
            return items_list.index(find_item)



items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = warehouse(items_list=items_list, find_item=find_item)  # TODO Вызовите функцию
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
