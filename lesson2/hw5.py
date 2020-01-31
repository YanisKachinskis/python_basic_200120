my_list = [7, 5, 3, 3, 2]
new_element = int(input('Введите новый элемент рейтинга:\n'))
if new_element <= my_list[-1]:
    my_list.append(new_element)
elif new_element >= my_list[0]:
    my_list.insert(0, new_element)
elif new_element in my_list:
    my_list.reverse()
    my_list.insert(my_list.index(new_element), new_element)
    my_list.reverse()
print(my_list)
